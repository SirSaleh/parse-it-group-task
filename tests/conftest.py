import sys
from pathlib import Path

# Add the project directory to sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import pytest
from fastapi.testclient import TestClient
from main import app
from rag_app.services.factories.db_factory import DatabaseFactory
from rag_app.services.nlp.nlp_model import NLPModel

@pytest.fixture(scope='module')
def test_app():
    client = TestClient(app)
    yield client

@pytest.fixture(scope='module')
def test_db():
    dimension = 300  # Use the same dimension as in your main app
    db = DatabaseFactory.create_database('faiss', 'test_text_data', dimension)
    yield db

@pytest.fixture(scope='module')
def nlp_model():
    model = NLPModel()
    yield model
