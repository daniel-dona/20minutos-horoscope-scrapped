#!/usr/bin/env python3

import csv
from pysentimiento import create_analyzer

tsv = csv.reader(open("2011.tsv"), delimiter="\t")

#print("Loading...")

analyzer = create_analyzer(task="emotion", lang="es")

n = -1 #header

print("day", "joy", "anger", "sadness", "surprise", "disgust", "fear", sep="\t")


for line in tsv:

	if n % 12 == 0: #aries

		probas = analyzer.predict(line[2]).probas
		

		print(line[1], probas['joy'], probas['anger'], probas['sadness'], probas['surprise'], probas['disgust'], probas['fear'], sep="\t")
		
	n+=1

'''

>>> analyzer.predict("Hoy no conseguirás ser positivo, deberás distribuir bien tus energías en el trabajo, y cambiar tus convicciones equivocadas y maliciosas. Pero al final del día, tu pareja te demostrará su cariño con un regalo, podría no ser algo material sino algo que tu estabas esperando de su parte.")
AnalyzerOutput(output=others, probas={others: 0.571, joy: 0.328, sadness: 0.067, anger: 0.018, disgust: 0.006, surprise: 0.006, fear: 0.004})
>>> 
'''
