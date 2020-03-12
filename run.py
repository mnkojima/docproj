from python_webex.v1.Bot import Bot
from python_webex import webhook
from datetime import datetime
#from version import *

#version = 0


bot = Bot()         # the program will automatically know the bot being referred to y the auth_token

# create a webhook to expose it to the internet
# rememer that url we got from step 2, this is where we use it. In my case it was http://87a942a1.ngrok.io. 
# We will be creating a webhook that will be listening when messages are sent
bot.create_webhook(
    name="quickstart_webhook", target_url="http://666c1e93.ngrok.io", resource="messages", event="created"
)

# we create a function that responds when someone says hi
# the room_id will automatically be filled with the webhook. Do not forget it
@bot.on_hears("codigo")

def greet_back(room_id=None):
	global ver
	with open('version.txt', 'r') as file:
		ver = int(float(file.read().replace('\n','') ))
	now = datetime.now()
	year = now.strftime("%Y")
	year = year[-2:]
	month = now.strftime("%m")
	day = now.strftime("%d")
	codproj="5F"+year+month+day
	ver = ver + 1
	#file.write(str(ver))
	with open('version.txt', 'w') as file:
		file.write(str(ver))
	return bot.send_message(room_id=room_id, text=codproj+str(ver)+"v1")

# We create a default response in case anyone types anything else that we have not set a response for
# this is done using * [ don't ask me what happend when someone sends '*' as the message, that's on my TODO]
@bot.on_hears("*")

def default_response(room_id=None):
    return bot.send_message(room_id=room_id, text="Desculpe, não entendi")


# make the webhook know the bot to be listening for, and we are done
webhook.bot = bot

if __name__ == "__main__":
    webhook.app.run(debug=True)         # don't keep debug=True in production