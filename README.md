# MINIO

```
conda install -c conda-forge minio
conda install -c conda-forge influxdb
```
## Server
```
docker run -p 9000:9000 minio/minio server /data
```
- Endpoint: http://127.0.0.1:9000
- Root User (Access Key): minioadmin
- Root Password (Secret Key): minioadmin

Create new ```bucket123``` - red circle "+" button in right bottom

for development:
```

```
## Client - actually not especially needed
```
docker run --name my-mc --hostname my-mc -it --entrypoint /bin/bash --rm minio/mc
[root@my-mc /]# mc alias set myminio/ https://my-minio-service MY-USER MY-PASSWORD
[root@my-mc /]# mc ls myminio/mybucket
```

## Test 
http://127.0.0.1:9000/minio/login

# INFLUXDB


InfluxDB v2.0

```
docker run \
    --rm \
    --detach \
    --name influxdb2.0.4 \
    -p 8086:8086 \
    --volume $PWD:/root/.influxdbv2 \
    influxdb:2.0.4
```
console into the InfluxDB container
```
docker exec -it influxdb2.0.4 /bin/bash
```
Set up and use the influx CLI
```
influx config create -n default \
    -u http://localhost:8086 \
    -o example-org \
    -t admin123 \
    -a
```

url:    localhost:8086
user:   admin
pwd:    admn123
org:    example-org
bucket: tst


get token from http://localhost:8086/orgs/a2c1e3fec09f3ea7/load-data/tokens
------------------------------------------
influx write \
  -t tQu8QihLJcxNZgarC-FYCbay7IbwpmTrwNltDPYRAX16ZoXk7tJ8qqVz2muY-7SKAfVfnh5A-sQcF5uD6z3jtQ== \
  -b tst \
  -o example-org \
  'my_bike_id_12345,v=1 bat=25.3 1619471506271764344'


influx write \
  -t tQu8QihLJcxNZgarC-FYCbay7IbwpmTrwNltDPYRAX16ZoXk7tJ8qqVz2muY-7SKAfVfnh5A-sQcF5uD6z3jtQ== \
  -b tst \
  -o example-org \
  'my_bike_id_12345,v=1 bat=25.4 1619471506271764344'

  influx write \
  -t tQu8QihLJcxNZgarC-FYCbay7IbwpmTrwNltDPYRAX16ZoXk7tJ8qqVz2muY-7SKAfVfnh5A-sQcF5uD6z3jtQ== \
  -b tst \
  -o example-org \
  'my_bike_id_12345,v=2 bat=25.5 1619471506271764344'
---------------------------


influx query \
  -t tQu8QihLJcxNZgarC-FYCbay7IbwpmTrwNltDPYRAX16ZoXk7tJ8qqVz2muY-7SKAfVfnh5A-sQcF5uD6z3jtQ== \
  -o example-org \
  'from(bucket:"tst")|>range(start:-1h)|>filter(fn: (r)=>r._measurement == "my_bike_id_12345")'

---------------------------

sudo pip3 install influxdb-client


export INFLUX_USERNAME=admin
export INFLUX_PASSWORD=admn123
echo $INFLUX_USERNAME $INFLUX_PASSWORD


---------------------------------------

client.query('from(bucket:"tst")|>range(start:-1h)|>filter(fn: (r)=>r._measurement == "my_bike_id_12345")')