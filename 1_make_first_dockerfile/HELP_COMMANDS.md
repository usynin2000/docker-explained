```bash
# Get to the dir
cd 1_make_first_dockerfile/app

# Make an image
docker build -t my-python-app .

# To look what images we have
docker images

# Run the container with new image
docker run -p 5000:5000 my-python-app

# See if it works
curl localhost:5000
```
