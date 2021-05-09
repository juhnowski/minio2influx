# -*- coding: utf-8 -*-

from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

def main():
    token = "3rOK5z842Ny-ytTshbAVShHAXjsAUAUoorXEaC_Q_c6-NRduJ7yy8OhdwLfaYNKUc3uyOvhtNBncu8t9IKBQog=="
    org = "example-org"
    bucket = "tst"

    client = InfluxDBClient(url="http://localhost:8086", token=token)
    write_api = client.write_api(write_options=SYNCHRONOUS)

# Test data
    rec_time = datetime.utcnow()

    point = Point("SIM7000G").tag("Topic","SYSTEM")\
        .field("mod/bat", 1.1)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)

    point = Point("SIM7000G").tag("Topic","GPS")\
        .field("gps/fix", 2)\
        .field("gps/lat", 56.295424)\
        .field("gps/lon", 43.9549952)\
        .field("gps/speed", 13.12345)\
        .field("gps/head", 3.12345)\
        .field("gps/alt", 4.12345)\
        .field("gps/sec", 4.12345)\
        .field("gps/sat", 3)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)

    point = Point("SIM7000G").tag("Topic","NETWORK")\
        .field("mod/reg", True)\
        .field("mod/sig", 10)\
        .field("mod/opr", "Vodafone")\
        .field("mod/ip", "127.0.0.1")\
        .field("mod/netmode", "local")\
        .field("local_timestamp", "2021-05-09T17:29:36.619931538Z")\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)

    point = Point("SIM7000G").tag("Topic","MQTT")\
        .field("mod/mqttstat", "Error: not yet supported")\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)

    point = Point("SIM7000G").tag("Topic","MQTT")\
        .field("mod/mqttstat", "Error: not yet supported")\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)
    
    point = Point("MPU9250").tag("Topic","9dof")\
        .field("imu/accx", 1.000001)\
        .field("imu/accy", 2.000001)\
        .field("imu/accz", 3.000001)\
        .field("gyro_x", 4.000001)\
        .field("gyro_y", 5.000001)\
        .field("gyro_z", 6.000001)\
        .field("mag_x", 7.000001)\
        .field("mag_y", 8.000001)\
        .field("mag_z", 9.000001)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)
    
    point = Point("MPU9250").tag("Topic","DMP")\
        .field("imu/pitch", 1.000001)\
        .field("imu/roll", 2.000001)\
        .field("imu/yaw", 3.000001)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)
    
    point = Point("MPU9250").tag("Topic","system")\
        .field("imu/pitch", 1.000001)\
        .field("imu/roll", 2.000001)\
        .field("imu/yaw", 3.000001)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)
    
    point = Point("MPU9250").tag("Topic","system")\
        .field("imu/temp", 1.000001)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)
    
    point = Point("MPU9250").tag("Topic","service")\
        .field("calibration", True)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)
    
    point = Point("ACTUATORS").tag("Topic","NOTIFICATION")\
        .field("smrtgr/prio", 1)\
        .field("smrtgr/dur", 2)\
        .field("smrtgr/interv", 3)\
        .field("smrtgr/rep", 4)\
        .field("smrtgr/lh", 5)\
        .field("smrtgr/ll", 6)\
        .field("smrtgr/la", 7)\
        .field("smrtgr/rh", 8)\
        .field("smrtgr/rl", 9)\
        .field("smrtgr/ra", 10)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)
    
    point = Point("ACTUATORS").tag("Topic","HMI")\
        .field("smrtgrips/b", True)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)
    
    point = Point("BLE-CADENCE").tag("Topic","CADENCE")\
        .field("blecad/cad", 100)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)
    
    point = Point("BLE-CADENCE").tag("Topic","BATT LEVEL")\
        .field("blecad/batt", 99)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)
    
    point = Point("BLE-SPEED").tag("Topic","SPEED")\
        .field("blesp/speed", 20)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)
    
    point = Point("BLE-SPEED").tag("Topic","BATT LEVEL")\
        .field("blesp/batt", 99)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)
    
    
    
    point = Point("BLE-RADAR").tag("Topic","THREAT")\
        .field("blerr/dist", 9)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)
    
    point = Point("BLE-RADAR").tag("Topic","THREAT")\
        .field("blerr/speed", 19)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)
    
    point = Point("BLE-RADAR").tag("Topic","THREAT")\
        .field("blerr/sev", 29)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)
    
    point = Point("BLE-RADAR").tag("Topic","BATT LEVEL")\
        .field("blerr/batt", 99)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)
    
    
    point = Point("BLE-POWER METER").tag("Topic","POWER_METER")\
        .field("blepm/pf", 9)\
        .field("blepm/cad", 19)\
        .field("blepm/loc", 29)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)
    
    point = Point("BLE-POWER METER").tag("Topic","BATT LEVEL")\
        .field("blepm/batt", 9)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)

    point = Point("BLE - Heart rate monitor").tag("Topic","HEARTRATE")\
        .field("blehrm/bpm", 9)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)
    
    point = Point("BLE - Heart rate monitor").tag("Topic","BATT LEVEL")\
        .field("blehrm/batt", 9)\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)
    
    point = Point("boreal_ECU").tag("Topic","SYSTEM")\
        .field("ecu/ver", "firmware_version: 0.1")\
        .field("ecu/state", "record")\
        .field("ecu/reg_dev", "1,2,3")\
        .field("ecu/conn_dev", "1,2,3")\
        .field("ecu/disconn_dev", "1,2,3")\
        .field("ecu/ssid", "123XCV12342")\
        .field("ecu/ip", "127.0.0.1")\
        .field("ecu/address", "Some address")\
        .field("ecu/batt", "Some address")\
        .field("ecu/moved", True)\
        .field("ecu/tampered", True)\
        .field("ecu_uuid", "123bnmbm1231")\
        .time(rec_time, WritePrecision.NS)
    write_api.write(bucket, org, point)

    
if __name__ == "__main__":
    # execute only if run as a script
    main()
    
