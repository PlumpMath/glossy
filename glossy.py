#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random
import sys

CONSOLE_COLOR_ERROR = "\033[91m"
CONSOLE_COLOR_NORMAL = "\033[0m"
CONSOLE_COLOR_LANG_A = '\033[94m'
CONSOLE_COLOR_LANG_B = '\033[92m'

LANG_A = "isl"
LANG_B = "sve"

question_languages = [
	LANG_A,
	LANG_B,
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
		LANG_A: LANG_B,
		LANG_B: LANG_A,
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
	print str(score) + "\t" + item[LANG_A] + " = " + item[LANG_B]

def print_result():
	print "Result:"
	[print_item(item) for item in sorted(words, key = lambda(item): item["score"])]

def read_words_from_file(filename):
	words = []
	word_list_file = open(filename, "r")
	lines = word_list_file.readlines()
	word_list_file.close()

	i = 0
	while i < len(lines):
		try:
			word_a = lines[i].strip()
			word_b = lines[i + 1].strip()
			empty = lines[i + 2].strip()
		except:
			pass

		if word_a == "":
			print "Error reading file on line " + str(i)
		elif word_b == "":
			print "Error reading file on line " + str(i + 1)
		elif empty != "":
			print "Error reading file on line " + str(i + 2)

		item = {
			LANG_A: word_a,
			LANG_B: word_b,
			"score": 0
		}

		words.append(item)
		i += 3

	return words

def practice_loop(count):
	while(count > 0):
		item = pick_word()
		language = pick_language()
		word = item[language]
		sys.stdout.write(CONSOLE_COLOR_LANG_A + "[" + language + "] " + CONSOLE_COLOR_NORMAL + word + " = ")
		guess = raw_input("")
		analyze(guess, item, language)
		count -= 1



# Go!
words = read_words_from_file("word_list.txt")
practice_count = 1 * len(words)
practice_loop(practice_count)
print_result()
