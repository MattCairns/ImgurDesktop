import requests
import json
import random
import time
import settings
from gi.repository import Gio


def get_urls(subreddit):
	url = 'https://api.imgur.com/3/gallery/r/%s/' % subreddit
	print url
	headers = {'Content-Type': 'text', 'Authorization': 'Client-ID %s' % settings.CLIENT_ID}
	print headers
	try:
		subreddit_data = requests.get(url, headers=headers, verify=False)
	except:
		return "Could not collect list of images from Imgur"

	subreddit_data = subreddit_data.json()

	urls = []
	for d in subreddit_data['data']:
		urls.append(d['link'])

	return urls

time.sleep(5)

r = requests.get(random.choice(get_urls('wallpapers')), stream=True)
with open('/home/matt/ImgurDesktop/desktop.jpg', 'w') as f:
	print f
	try:
		f.write(r.content)
		f.close()
	except:
		print "Could not write the image to desktop.jpg."


settings = Gio.Settings.new('org.gnome.desktop.background')
settings.set_string('picture-uri', 'file:///home/matt/ImgurDesktop/desktop.jpg')
