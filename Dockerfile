FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y libpq-dev && pip install --no-cache-dir -r requirements.txt

RUN python -c "from transformers import BertTokenizer, BertModel; BertTokenizer.from_pretrained('bert-base-uncased'); BertModel.from_pretrained('bert-base-uncased')"

COPY . .

ENV PYTHONPATH=/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
