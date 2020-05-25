import subprocess
import socket
import os

class Nettool:
	# constructor
	def __init__(self):
		self.local_ip=None
		self.all_local_ip=None
	# get the ip of localhost
	def get_local_ip(self):
		if self.local_ip is not None:
			return self.local_ip
		self.local_ip=socket.gethostbyname(socket.gethostname())
		return self.local_ip
	# get all ip address on the local subnet 
	def get_all_local_ip(self):
		if self.all_local_ip is not None:
			return self.all_local_ip
		arp_list=subprocess.check_output(['arp','-a']).split('\n')
		ip_list=[]
		word_list=[]
		for i in len(arp_list):
			line = arp_list[i].split(' ')
			word_list.append(line)
			ip_list.append([])
			for j in range(len(word_list)):
				if '.' in word_list[j]:
					ip=str(temp[j])
					ip=ip.strip('(')
					ip=ip.strip(')')
					ip_list[i].append(ip)
				if ':' in word_list[j]:
					mac=str(temp[j])
					ip_list[i].append(mac)
		return self.all_local_ip=ip_list
