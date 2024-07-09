# Docker Deployment


## Build

```bash
sudo docker build -t rag-app .
```

## Run

```bash
sudo docker run -d --name rag-app  -p 8000:8000 rag-app 
```

## log

```bash
sudo docker logs rag-app 
```

**Note**: You can logs in real time you can use -f flag:

```bash
sudo docker logs -f rag-app
```

## stop

```bash
sudo docker stop rag-app 
```