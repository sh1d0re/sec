print("""┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n┃  ╭────╮  ┃   ┏┓  ╺━┓ ┏━╸   ┏━╸ ╻ ╻ ┏━┓ ━┳━                      ┃\n┃  │╭───╯  ┃   ┣┻┓ ┏━┛ ┣━╸   ┃   ┣━┫ ┣━┫  ┃                       ┃\n┃  ╰╯      ┃   ┗━┛ ┗━╸ ┗━╸   ┗━╸ ╹ ╹ ╹ ╹  ╹                       ┃\n┡━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩\n│                     PROGRAMMER : Kunihito Takada                │\n│                        LICENSE : GPL-v3                         │\n│                       LANGUAGE : Python                         │\n└────────────────────────────────┴────────────────────────────────┘""")
cluster,uri="",""
print("━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[ 1: LOADING    PyP ] ┃ \x1b[31mEnter \x1b[31;1mControl&C\x1b[0m\x1b[31m To Abort. Leave To Proceed.\x1b[0m")
try:import os
except Exception as e:
	print("                Error ┖╴\x1b[31m"+str(e)+"\nProgram aborted. Contact developer at github repository or admin.")
	quit()
print("            OS Module ┠╴\x1b[32mSUCCESS\x1b[39;49m")
try:import random
except Exception as e:
	print("                Error ┖╴\x1b[31m"+str(e)+"\nProgram aborted. Contact developer at github repository or admin.")
	quit()
print("        Random Module ┠╴\x1b[32mSUCCESS\x1b[39;49m")
try:import subprocess
except Exception as e:
	print("                Error ┖╴\x1b[31m"+str(e)+"\nProgram aborted. Contact developer at github repository or admin.")
	quit()
print("    Subprocess Module ┠╴\x1b[32mSUCCESS\x1b[39;49m")
try:import getpass
except Exception as e:
	print("                Error ┖╴\x1b[31m"+str(e)+"\nProgram aborted. Contact developer at github repository or admin.")
	quit()
print("       Getpass Module ┠╴\x1b[32mSUCCESS\x1b[39;49m")
try:import time
except Exception as e:
	print("                Error ┖╴\x1b[31m"+str(e)+"\nProgram aborted. Contact developer at github repository or admin.")
	quit()
print("          Time Module ┠╴\x1b[32mSUCCESS\x1b[39;49m")
try:from b2e import b2e
except Exception as e:
	print("                Error ┖╴\x1b[31m"+str(e)+"\nProgram aborted. Contact developer at github repository or admin.")
	quit()
print("           B2E Module ┠╴\x1b[32mSUCCESS\x1b[39;49m")
try:
	from pymongo.mongo_client import MongoClient
except Exception as e:
	print("                Error ┖╴\x1b[31m"+str(e)+"\nProgram aborted. Contact developer at github repository or admin.")
	quit()
print("       PyMongo Module ┠╴\x1b[32mSUCCESS\x1b[39;49m")
try:from datetime import datetime
except Exception as e:
	print("                Error ┖╴\x1b[31m"+str(e)+"\nProgram aborted. Contact developer at github repository or admin.")
	quit()
print("      Datetime Module ┖╴\x1b[32mSUCCESS\x1b[39;49m")
print("━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[ 2: LOADING Server ] ┃ \x1b[31mEnter \x1b[31;1mControl&C\x1b[0m\x1b[31m To Abort. Leave To Proceed.\x1b[0m")
try:
	MongoClient("mongodb+srv://b2c-chatuser:E81bAFzSDPlQwfPL@atlascluster.5mvaliq.mongodb.net/?retryWrites=true&w=majority").admin.command('ping')
except Exception as e:
	print("                Error ┖╴\x1b[31m"+str(e)+"\nProgram aborted. Contact developer at github repository or admin.")
	quit()
print("        Server Module ┖╴\x1b[32mSUCCESS\x1b[39;49m")
print("━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[ 3:  Executing B2C ] ┃ Run \x1b[0;1m/help\x1b[0m Or Read \x1b[0;1mREADME.md\x1b[0m For Info.")
cluster=MongoClient("mongodb+srv://b2c-chatuser:E81bAFzSDPlQwfPL@atlascluster.5mvaliq.mongodb.net/?retryWrites=true&w=majority")
db,id_=cluster["b2c"]["messages"],""
encode = getpass.getpass(prompt="   Enter Channel Code ┃ ")
while True:
	all = db.find({})
	date = str(datetime.now().strftime("%x"))
	delimiter,spaces="",""
	for msgs in all:
		if b2e.decode(str(encode),msgs['channel'])=="VALID":
			try:
				print("\n"+b2e.decode(str(encode),msgs['date'])+" - "+b2e.decode(str(encode),msgs['deltatime']))
				print(b2e.decode(str(encode),msgs['id'])+": "+b2e.decode(str(encode), msgs['message'])+"\n")
			except: pass
		id_="Test"#b2e.decode(str(encode),"poopy")
		time.sleep(random.randint(1,3)//100)
	sndmsg=input(">>> ")
	if sndmsg=="/exit":
		print("Exited Chat")
		break
	if sndmsg=="/help":
		print("       Outputing Help ┖╴")
	deltatime=str(datetime.now().strftime("%X"))
	msg={"id": b2e.encode(str(encode), id_), "message": b2e.encode(str(encode), sndmsg), "date": b2e.encode(str(encode),date), "deltatime": b2e.encode(str(encode),deltatime), "channel": b2e.encode(str(encode),"VALID")}
	db.insert_one(msg)