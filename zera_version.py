from datetime import datetime
import time

while True:
	now = datetime.now()	
	hora = now.hour
	min = now.minute
	print (str(hora)+":"+str(min))
	if hora==0 and min==1 :
		#print ("hora de zerar a versão")
		with open('version.txt', 'w') as file:
			file.write(str(0))
			print ("A versão foi zerada")
	time.sleep (60)

