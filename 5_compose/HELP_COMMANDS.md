## Try to use the easiest docker-compose

1. Get to the first demo:
```bash
cd demo_without_db
```

2. Build the images, create the networks, start all containers
```bash
docker compose up --build
```

3. Check that everything works
```
http://localhost:8080
```

4. Stop all containers
```bash
docker compose down
```



### Try to use compose with Database

1. Get to the second demo
```bash
cd ..
cd demo_with_db
```

2. Build the images, create the networks, start all containers again
```bash
docker compose up --build
```

3. Get to the db shell using psql
```bash
docker compose exec db psql -U demo demo
```

4. Create the table
```sql
CREATE TABLE messages (message TEXT);
```

5. Add one message to the table
```sql
INSERT INTO messages VALUES ('Hello from Postgres');
```

6. Exit psql
```sql
\q
```

7. Check that everything works
```
http://localhost:8080
```
