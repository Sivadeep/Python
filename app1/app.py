import yaml
import paramiko
f=open('config.yaml')
config =  yaml.load(f)
for system in config:
	connect = config[system]
	ssh 


