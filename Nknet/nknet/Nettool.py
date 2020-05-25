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
		ifconfig_list=subprocess.check_output(['ifconfig']).split('inet ')
		ip=[]
		for chunk in ifconfig_list:
			line_list=chunk.split('\n')
			for line in line_list:
				word_list=line.split(' ')
				for word in word_list: 
					if '.' in word:
						ip.append(word)
		ip.pop()
		self.local_ip=ip
		return self.local_ip
	# get all ip address on the local subnet 
	def get_all_local_ip(self):
		if self.all_local_ip is not None:
			return self.all_local_ip
		arp_list=subprocess.check_output(['arp','-a']).split('\n')
		arp_list.pop()
		ip_list=[]
		i=0
		for line in arp_list:
			word_list=line.split(' ')
			ip_list.append([])
			for word in word_list:
				if '.' in word:
					ip=str(word)
					ip=ip.strip('(')
					ip=ip.strip(')')
					ip_list[i].append(ip)
				if ':' in word:
					mac=str(word)
					ip_list[i].append(mac)
			i+=1
		self.all_local_ip=ip_list
		return self.all_local_ip
