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

words = [
	{ "isl": "ég", "sve": "jag" },
	{ "isl": "þú", "sve": "du" },
	{ "isl": "við", "sve": "vi" },
]

# Give every item a score
[item.setdefault("score", 0) for item in words]

def get_hardest_words():
	return words

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

practice_count = 3

while(practice_count > 0):
	item = pick_word()
	language = pick_language()
	word = item[language]
	sys.stdout.write(word + " = ")
	guess = raw_input("")
	analyze(guess, item, language)
	practice_count -= 1

def print_item(item):
	score = item["score"]
	print item["isl"] + "/" + item["sve"] + ", score: " + str(score)

print "Result:"
[print_item(item) for item in words]

