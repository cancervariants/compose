# Compose services for metakb

> Runs metakb services in containers using docker compose.

## Installation

You will need [docker-compose](https://docs.docker.com/compose/install/)

## Quickstart

### After cloning this repo, you will need to clone metakb services.

At this time, we only have one: `therapy-normalizer`

```
cd compose

git clone https://github.com/cancervariants/therapy-normalization
cd therapy-normalization
# Dockerfile currently on this branch
git checkout issue-123

cd ..
```

### Launch

```
# build services
docker-compose build

# launch all services in the background
docker-compose up -d
```

### Test

* Services should be up and running
```
$docker-compose ps

  Name                Command                       State                   Ports
------------------------------------------------------------------------------------------
dynamodb   java -jar DynamoDBLocal.ja ...   Up                      0.0.0.0:8000->8000/tcp
test       /bin/sh -c tail -f /dev/null     Up
therapy    /bin/sh -c pipenv run uvic ...   Up (health: starting)   0.0.0.0:8001->80/tcp
```


* You should see dynamo datastore

```
ls -l data/dynamodb/shared-local-instance.db

-rw-r--r--  1 xxxx  yyyy  24576 Mar 24 09:21 data/dynamodb/shared-local-instance.db
```

* You can run high level integration "smoke-tests"

```
docker-compose  exec test sh -c "pipenv run pytest  tests/integration"

Note: expected error
test_query - AssertionError: Therapy server should find `cisplatin`.
```


### Shutdown

```
docker-compose down

# if you wish to remove any volumes
# docker-compose down -v

```
