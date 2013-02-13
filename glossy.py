#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random
import sys

CONSOLE_COLOR_ERROR = "\033[91m"
CONSOLE_COLOR_NORMAL = "\033[0m"

question_languages = [
	"isl", 
	"sve",
]

def get_hardest_words():
	sorted_words = sorted(words, key = lambda(item): item["score"])
	word_count = 1 + int(0.25 * len(sorted_words))
	return sorted_words[:word_count]

def pick_word():
	return random.choice(get_hardest_words())

def pick_language():
	return random.choice(question_languages)

def other_language(language):
	return {
		"sve": "isl",
		"isl": "sve",
	}[language]

def analyze(guess, item, language):
	correct = item[other_language(language)]
	if guess == correct:
		item["score"] += 1
	else:
		item["score"] -= 1
		print CONSOLE_COLOR_ERROR + correct + CONSOLE_COLOR_NORMAL

def print_item(item):
	score = item["score"]
	print str(score) + "\t" + item["isl"] + " = " + item["sve"]

def print_result():
	print "Result:"
	[print_item(item) for item in sorted(words, key = lambda(item): item["score"])]

words = []

word_list_file = open("word_list.txt", "r")
lines = word_list_file.readlines()
word_list_file.close()

i = 0
while i < len(lines):
	try:
		isl = lines[i].strip()
		sve = lines[i + 1].strip()
		empty = lines[i + 2].strip()
	except:
		pass

	if isl == "":
		print "Error reading file on line " + str(i)
	elif sve == "":
		print "Error reading file on line " + str(i + 1)
	elif empty != "":
		print "Error reading file on line " + str(i + 2)

	item = {
		"isl": isl, 
		"sve": sve, 
		"score": 0
	}
	words.append(item)
	i += 3

practice_count = 3 * len(words)

while(practice_count > 0):
	item = pick_word()
	language = pick_language()
	word = item[language]
	sys.stdout.write(word + " = ")
	guess = raw_input("")
	analyze(guess, item, language)
	practice_count -= 1

print_result()
