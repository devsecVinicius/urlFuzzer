import requests

print('\n\n\tWeb Fuzzer by @devsecvinicius\n\n')
f = open("output.txt", "a")

site = input(" Target / Url: ")
# http://testphp.vulnweb.com/
payload = open('lista.txt') # put the name of your file here
lenOfList = 100000

index = 0
print("\n\n ---------------------------------------------------\n\n")
while(index < lenOfList):
	
	try:
		target = site + payload.readline().rstrip("\n")
	
		if target == site:
			break;
		try:
			r = requests.get(target)
			
			if r.status_code == 200:
				print(' Target = "' + target + '" - status code = 200')
				f.write(target + "\n")
			if r.status_code != 404:
				print(' Target = "' + target + '" - status code = ' + r.status_code)
				f.write(target + "\n")
		except:
			pass
	except ConnectionRefusedError:
			print("\n Connection Refused.")
			
	finally:
			index += 1

f.close()
