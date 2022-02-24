#!/usr/bin/env python3

import datetime
from lxml.html.soupparser import fromstring
import urllib.request
import time

base_url = "https://www.20minutos.es/horoscopo/solar/prediccion/"

signs = ["aries", "tauro", "geminis", "cancer", "leo", "virgo", "libra", "escorpio", "sagitario", "capricornio", "acuario", "piscis"]

year = 2016

start = datetime.date(year,1,1)
stop = datetime.date(year,12,31)

delay = 1

print("sign\tdate\tprediction")

while start < stop:

	for sign in signs:

		url = base_url+sign+start.strftime("/%d/%m/%Y/")
		
		#print(url)

		htmlpage = urllib.request.urlopen(url).read().decode('utf-8')
		
		tree = fromstring(htmlpage)
		
		text = ""
		
		if len(tree.xpath("//div[@class='prediction "+sign+"']/p/p")) != 0:
			
			res = tree.xpath("//div[@class='prediction "+sign+"']/p/p")
			
		else:
			
			res = tree.xpath("//div[@class='prediction "+sign+"']/p")
		
		for element in res:
			
			if not "class" in element.attrib and element.text is not None:
			
				text += " "+element.text
				
		
		print (sign, start.isoformat(), text, sep="\t")
		
		time.sleep(delay)
		
	start += datetime.timedelta(days=1)
	
