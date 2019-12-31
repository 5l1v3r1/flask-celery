
## Running flask with celery

### Run docker

define how many worker do you want to use
```
	docker-compose up -d --scale worker=5 --build
```
### Stop docker
```
	docker-compose down
```

## Flower monitoring
Monitoring with flower [localhost:5555](localhost:5555)