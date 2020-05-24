import os

fer="[MTABLE FATAL ERROR] "
class Mtable:
	# constructor 
	def __init__(self,path_to=""):
		if not os.path.exists(path_to):
			print(fer+"constructor input path not valid")
			raise TypeError
		self.row = []
		self.col = []
		self.rcomp = []
		self.ccomp = []
		self.in_file = open(path_to,"r")
		self.out_file = None
		# complete the row and col lists
		if ".csv" in path_to:
			for line in self.in_file:
				add = self.parse_csv_line(line.strip(" "))
				self.row.append(add)
		if ".tsv" in path_to:
			for line in self.in_file:
				add = self.parse_csv_line(line.strip(" "))
				self.row.append(add)
		# get max row length
		max_len = 0
		for row in self.row:
			if max_len<len(row):
				max_len=len(row)
		# create self.col
		for i in range(max_len):
			self.col.append([])
		# add all elements to correct colomn 
		for i in range(self.row):
			for j in range(self.row[i]):
				self.col[j].append(self.row[i][j])
	# parse a line of csv
	def parse_csv_line(self,line=""):
		return line.split(',')
	# parse a line of tsv
	def parse_tsv_line(self,line=""):
		return line.split('\t')
	# getter for row
	def get_row(self,index=0):
		if index>=len(self.row):
			return None
		return self.row[index]
	# getter for col
	def get_col(self,index=0):
		if index>=len(self.col):
			return None
		return self.col[index]
	# getter for rcomp
	def get_ccomp(self,index=0):
		if index>=len(self.ccomp):
			return None
		return self.ccomp[index]
	# getter for ccomp
	def get_rcomp(self,index=0):
		if index>=len(self.rcomp):
			return None
		return self.rcomp[index]
# EOF
