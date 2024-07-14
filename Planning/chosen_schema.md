## Chosen Schema


## DB vector index

I used faiss.IndexFlatL2 and L2 Metric in Malvuss, for indexting, which utilizes, L2 measure to calculate distances to find the nearest neighbors. As I used BERT algorithm to genearte the vecotrs, I used typical dimention for bert in db config: 768 dimentions.

**Speed and Efficiency**: L2 metric implementation in vector databases is fast in calculation and retrival which is important for the RAG system.

**Compatibility with NLP Models**: It is fast for our selected model (BERT model), which generates dence vector embedings.

## Integration with PostgreSQL:

In the case of FAISSDB as the process runs fully on RAM to presists data on the disk. As programm restarts data stores in PostgreSQL, loads in to FAISS index to use in the distance calcualtion process. 

In fact:

**Data Presistence**: to presists the data gathering during the procedure after a restart of our RAG app.
**Scalability**: Large datasets can stores and efficiently retrieved in PostgreSQL.
**Flexibility**: Suitable to CRUD operations on vector data.
**Nice Extentions**: As my experience in Abrbar company, good extentions to process and manipulate the data is available for the PostgreSQL.