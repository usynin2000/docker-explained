
# Help Commands to Run Containers

Explanation in YouTube: (TO-DO: Add source after posting)


After installing dependencies from requirements.txt:

```bash
cd 0_run_first_container

pip install -r requirements.txt
```
Run the app locally:

```shell
python app.py
```


## Build the image
```bash
docker build -t docker-demo .
```

## Run the container using docker-demo image
```bash
docker run -p 8000:8000 docker-demo
```


## Check if docker is installed
```bash
docker --version
```


## Run real service:
```bash
docker run -d --name my-nginx -p 8080:80 nginx:alpine
```


## To see all running containers
```bash
docker ps
```


## To get inside the container
```bash
docker exec -it my-nginx sh
```


## To show logs of container
```bash
docker logs my-nginx
```


## To stop a container
```bash
docker stop my-nginx
```


## To remove the container
```bash
docker rm my-nginx
```
