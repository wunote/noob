#!/usr/bin/python
#coding=utf-8

import paramiko

ip = '106.75.142.189'
port = 59878
user = 'developer'
pwd = 'TD7IEtMhg'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ip, port, username=user, password=pwd, timeout=4)
stdin, stdout, stderr = client.exec_command('cd /tmp/ && ls -l')
for std in stdout.readlines():
  print std,
client.close()

