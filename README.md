
## Running flask with celery

### Run docker

Define how many worker do you want to use
```
docker-compose up -d --scale worker=5 --build
```
### Stop docker
```
docker-compose down
```

## Flower monitoring
Monitoring with flower [http://localhost:5555](http://localhost:5555)