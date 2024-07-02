# Select Database


Options:

* **ChromaDb**
    Excluded in the task :)

* **FAISS**
    * pros: Pros: Fast and efficient for in-memory operations.
    * Cons: There is no built-in persistence and metadata management. Requires integration with other databases (like postgresql) for full functionality.
* **Milvus**
    * Pros: Combines in-memory and on-disk storage, supports distributed deployment, and integrates well with other databases for metadata.
    * Cons: Requires setup and management of the infrastructure.
* **Pinecone**
    * Pros: Fully managed service, easy to scale, no infrastructure management required.
    * Cons: Cost associated with using a managed service.**

## MY CHOISE

Given your requirements, **Milvus** is a strong choice due to its open-source nature, high performance, scalability, and community support. It allows us to have control over the deployment and integrates well with other databases for metadata storage if needed in the future of a real projectt.