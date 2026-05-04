
## To see that container and info inside

1. Start a simple container, get inside container
```bash
docker run -it --name temp alpine sh
```

2. Create file
```bash
echo "important data" > data.txt
```

3. Make sure it is here
```bash
ls
cat data.txt
```

4. Exit the container
```bash
exit
```

5. Remove the container
```bash
docker rm temp
```


6. Start new container, try to look at data.txt file content
```bash
docker run alpine cat data.txt
```


### Try using volume

1. Create the volume
```bash
docker volume create myvolume
```

2. Check if volume is here
```bash
docker volume ls
```

3. Start new container with volume, get inside container
```bash
docker run -it -v myvolume:/data alpine sh
```

4. Create file
```bash
echo "hello volume" > /data/file.txt
```

5. Exit the container
```bash
exit
```

6. Start new container, check that file in volume exists
```bash
docker run -v myvolume:/data alpine cat /data/file.txt
```


### Volume with DB

1. Create volume
```bash
docker volume create pg-data
```

2. Run Postgres with the pg-data volume mounted
```bash
docker run -d \
    --name pg-with-volume \
    -e POSTGRES_PASSWORD=secret \
    -v pg-data:/var/lib/postgresql/data \
    postgres:15
```

3. Create the table inside container
```bash
# open psql
docker exec -it pg-with-volume psql -U postgres

## create table
CREATE TABLE users(name TEXT);

# insert one record
INSERT INTO users VALUES ('Sergei');

# make sure the record exists
SELECT * FROM users;

# exit from container
exit

```

4. Remove the container
```bash
docker rm -f pg-with-volume
```

5. Recreate the container with same image and same volume
```bash
docker run -d \
    --name pg-with-volume2  \
    -e POSTGRES_PASSWORD=secret \
    -v pg-data:/var/lib/postgresql/data \
    postgres:15
```


6. Get inside container, check if data is still here
```bash
docker exec -it pg-with-volume2  psql -U postgres

# inside psql 
SELECT * FROM users;
```
