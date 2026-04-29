1. Register at https://hub.docker.com

2. Login in your machine
 ```bash
docker login -u <your_username>
```

3. Make an image
```bash
cd 2_dockerhub/tiny_project

docker build -t docker-demo .
```


4. Make sure image is done
```bash
docker images
```

5. Start the container
```bash
docker run -p 8000:8000 docker-demo
```

6. Check if it works locally:
http://localhost:8000

### Prepare image to DockerHub

1. Tag image to dockerhub formta
```bash
docker tag docker-demo <your_username>/docker-demo:1.0
```

2. Push image to dockerhub
```bash
docker push <your_username>/docker-demo:1.0
```

### Try with a new clean machine

1. Get to the machine
```bash
ssh root@ip_address
```

2. Install docker
```bash
sudo apt update

curl -fsSl https://get.docker.com | sudo sh
```


3. Check if docker installed
```bash
docker version
```

4. Enable user to use docker
```bash
sudo usermod -aG docker
```


5. Pulling the image from DockerHub
```bash
docker pull <your_username>/docker-demo:1.0

docker images
```

6. Run the container with new image from Hub:
```bash
docker run -d -p 80:8000 <your_username>/docker-demo:1.0
```


7. Check if it works FROM ANOTHER MACHINE:
http://ip_address
