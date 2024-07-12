import os
import faiss
import numpy as np
import psycopg2
from typing import List
from rag_app.services.interfaces.vector_db_interface import VectorDatabaseInterface

class FAISSDatabase(VectorDatabaseInterface):
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.texts = []

        # Read PostgreSQL configuration from environment variables
        self.db_host = os.getenv('POSTGRES_HOST', 'localhost')
        self.db_name = os.getenv('POSTGRES_DB', 'mydatabase')
        self.db_user = os.getenv('POSTGRES_USER', 'myuser')
        self.db_password = os.getenv('POSTGRES_PASSWORD', 'mypassword')

        self.conn = psycopg2.connect(
            host=self.db_host,
            dbname=self.db_name,
            user=self.db_user,
            password=self.db_password
        )
        self.cursor = self.conn.cursor()
        self.create_table()
        self.load_vectors_from_db()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vectors (
                id SERIAL PRIMARY KEY,
                vector FLOAT8[],
                text TEXT
            );
        """)
        self.conn.commit()

    def add_vector(self, vector: List[float], text: str):
        vector_np = np.array([vector], dtype=np.float32)
        assert vector_np.shape[1] == self.dimension, f"Vector dimension {vector_np.shape[1]} does not match index dimension {self.dimension}"
        self.index.add(vector_np)
        self.texts.append(text)
        self.save_vector_to_db(vector_np, text)

    def search(self, query: List[float], k: int):
        query_np = np.array([query], dtype=np.float32)
        distances, indices = self.index.search(query_np, k)
        return [self.texts[idx] for idx in indices[0]]

    def save_vector_to_db(self, vector: np.ndarray, text: str):
        vector_list = vector.flatten().tolist()
        self.cursor.execute("INSERT INTO vectors (vector, text) VALUES (%s, %s)", (vector_list, text))
        self.conn.commit()

    def load_vectors_from_db(self):
        self.cursor.execute("SELECT vector, text FROM vectors")
        for record in self.cursor.fetchall():
            vector = np.array(record[0], dtype=np.float32).reshape(1, -1)
            text = record[1]
            self.index.add(vector)
            self.texts.append(text)
