# -*- coding: utf-8 -*-

from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

def main():
    token = "3rOK5z842Ny-ytTshbAVShHAXjsAUAUoorXEaC_Q_c6-NRduJ7yy8OhdwLfaYNKUc3uyOvhtNBncu8t9IKBQog=="
    org = "example-org"
    bucket = "tst"

    client = InfluxDBClient(url="http://localhost:8086", token=token)

# Option 1: Use InfluxDB Line Protocol to write data
    write_api = client.write_api(write_options=SYNCHRONOUS)

    data = "mem,host=host1 used_percent=1.1"
    write_api.write(bucket, org, data)

# Option 2: Use a Data Point to write data
    point = Point("mem").tag("host", "host1").field("used_percent", 2.2).time(datetime.utcnow(), WritePrecision.NS)
    write_api.write(bucket, org, point)

# Option 3: Use a Batch Sequence to write data
    sequence = ["mem,host=host1 used_percent=3.3",
            "mem,host=host1 available_percent=4.4"]
    write_api.write(bucket, org, sequence)

# Execute a Flux query
#    query = f'from(bucket: \\"{bucket}\\") |> range(start: -1h)'
#    tables = client.query_api().query(query, org=org)


if __name__ == "__main__":
    # execute only if run as a script
    main()
    
