import requests
from PIL import Image, ImageFont, ImageDraw
import random
import pandas as pd

api_key = '99397087-b601-4262-822a-f5257701480f'
word = "subsequent"

def get_response(url):

	x = requests.get(url)
	resp = x.json()

	return resp

def make_card(word, etymology, date, definition, example):

	preset_colors = [
	(255, 0, 0),    # Red
	(0, 255, 0),    # Green
	(0, 0, 255),    # Blue
	(255, 255, 0),  # Yellow
	(255, 0, 255),  # Magenta
	(0, 255, 255),  # Cyan
	]

	random_color = random.choice(preset_colors)

	image_width = 800
	image_height = 400

	image = Image.new("RGB", (image_width, image_height),
	random_color)
	draw = ImageDraw.Draw(image)#font = ImageFont.truetype("sans-serif.ttf", 16)

	word_font = ImageFont.truetype("/home/ayush/Downloads/Helvetica-Bold.ttf", 36)
	sub_font =  ImageFont.truetype("/home/ayush/Downloads/Helvetica.ttf", 25)
	subsub_font =  ImageFont.truetype("/home/ayush/Downloads/Helvetica-Oblique.ttf",20)



	draw.text((50, 50),word,(0,0,0),font=word_font)
	draw.text((50, 140),definition,(0,0,0),font=sub_font)
	draw.text((50, 210),date+": "+etymology,(0,0,0),font=subsub_font)


	image.save("w.png")

	image.show()


def get_details(word):
	url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"
	resp = get_response(url)

	success = True
	try:
		data = resp
		etymology = data[0]["et"][0][1]
		date = data[0]["date"]
		definition = data[0]['def'][0]['sseq'][0][0][1]['dt'][0][1]
		example =  data[0]['def'][0]['sseq'][0][0][1]['dt'][1]

	except:
		success = False

	if not success:
		print("Failed for ", word, "!")
	else:
		print("Etymology:", etymology)
		print("Date:", date)
		print("Definition: ", definition)
		print("Example: ", example)
	
		make_card(word, etymology, date, definition, example)



p1 = '/home/ayush/Desktop/GRE/words_csv/barron_333.csv'
p2 = '/home/ayush/Desktop/GRE/words_csv/magoosh_1000.csv'
p3 = '/home/ayush/Desktop/GRE/words_csv/manhattan_500.csv'

magoosh_words = pd.read_csv(p2)
mag_list = magoosh_words['word'].to_list()
for w in mag_list:

	get_details(w)	

# get_details("cursory")
