

## Basic Requirements

Run milvus service in docker:

```bash
sudo docker run -d --name milvus-standalone -p 19530:19530 -p 3000:3000 milvusdb/milvus:v2.2.9
```

## Python

create a virtual environment:

```
python3 -m venv .venv
```

**Note**: `.venv` ingored in git so this name is recomended.


install python requirements:

```python
pip3 install -r requirements.txt
```
