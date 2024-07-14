# Select Database


## Options:

* **ChromaDb**
    Excluded in the task :)

* **FAISS**
    * pros: Pros: Fast and efficient for in-memory operations.
    * Cons: There is no built-in persistence and metadata management. Requires integration with other databases (like postgreSQL) for full functionality.
* **Milvus**L
    * Pros: Combines in-memory and on-disk storage, supports distributed deployment, and integrates well with other databases for metadata.
    * Cons: Requires setup and management of the infrastructure.
* **Pinecone**
    * Pros: Fully managed service, easy to scale, no infrastructure management required.
    * Cons: Cost associated with using a managed service.**

## MY CHOISE

Given the task requirements, **Milvus** is a strong choice due to its open-source nature, high performance, scalability, and community support. It allows us to have control over the deployment and integrates well with other databases for metadata storage if needed in the future of a real project. In this task for simplicity I used **FAISS** db integrated with **PostgreSQL** by default. But using strategy desgin pattern, this code structuers allows us to switch very easily among database mentioned above. 