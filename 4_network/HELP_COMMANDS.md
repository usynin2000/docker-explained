
### Try without networks

1. Start the backend container
```bash
docker run -d --name backend flask-backend
```

2. Start the frontend container
```bash
docker run -d --name frontend nginx
```

3. Check the containers
```bash
docker ps
```

4. Get into the frontend container and try to call the backend
```bash
docker exec -it frontend sh

curl http://localhost:5000/api/hello
```


### Try with Networking

1. Create the network
```bash
docker network create app-network
```

2. Check the networks
```bash
docker network ls
```

3. Inspect metadata for app-network
```bash
docker network inspect app-network
```

4. Run the containers again with the network flag
```bash
docker run -d \
    --name backend \
    --network app-network \
    flask-backend

docker run -d \
    --name frontend \
    --network app-network \
    nginx
```


5. Inspect the app-network again
```bash
docker network inspect app-network
```

6. Again get into the frontend container and curl the backend
```bash
docker exec -it frontend sh

curl http://backend:5000/api/hello
```


### Another example with more complex frontend

1. Build frontend image
```bash
docker build -f Dockerfile.frontend -t frontend-image .
```

2. Check that images are ready
```bash
docker images
```

3. Create network
```bash
docker network create app-network
```

4. Run the containers:
```bash
docker run -d \
    --name backend \
    --network app-network \
    flask-backend

docker run -d \
    --name frontend \
    --network app-network \
    -p 8080:80 \
    frontend-image
```


5. Check result in the browser:
http://localhost:8080
