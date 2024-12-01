def read_file(filename):
	lines = ""
	with open(filename,'r',encoding='utf-8-sig') as f:
		for line in f:
			line=line.rstrip("\t").rstrip("\n")
			line=line.replace("\t","")
			lines = lines + line
	return lines
	


def new_lines(lines):
	for line in lines:
		if line == "上午":
			break
	return lines



def write_file(filename,lines):
	with open(filename,'w',encoding='utf-8-sig') as f:
		f.write(lines)
		

def main():
	lines = read_file('9-10.txt')
	lines = new_lines(lines) 
	write_file('output.txt',lines)

main()