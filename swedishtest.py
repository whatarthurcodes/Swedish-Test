import sys
import random 
import csv

def swedishtest():
	
	word_bank = select_module()
	lang = choose_lang()
	questions(word_bank, lang)

	

def select_module():
	
	file_found = False
	while file_found is False:
		try:
			module_choice = raw_input('Enter the file name. ex. module1.csv \n')
			module = open(module_choice)
			csv_f = csv.reader(module)
			file_found = True
		except Exception: 
			print ("Cannot Find file ") + module_choice + ("\n")

	word_bank =[]
	for row in csv_f:
  		word_bank.append(row)
  	return word_bank
			
def choose_lang():
	lang = False
	while lang is False:
		lang = input('For Swedish to English enter 0 For English to Swedish enter 1 \n')

		if lang == 0 or lang == 1:
			return lang

		else:
			print ('Please enter 0 for English to Swedish or 1 for Swedish to English \n')
			lang = False
			
def questions(word_bank, lang):
	answer = 'answer'
	quit = False
	number_of_words = len(word_bank)
	print number_of_words
	correct_answers = 0
	number_of_questions =0
	print ('\nTo quit, enter q or quit')

	if lang == 0:
		print ('The word is given in Swedish, please type in the English word \n')
		lang_answer = 1

	if lang == 1:
		print ('The word is given in English, please type in the Swedish word \n')
		lang_answer = 0 

	while quit is False:
		rand = random.randint(0, number_of_words-1)
		question = word_bank[rand]
		answer = raw_input(question[lang] + '\n')

		if answer == 'q' or answer == 'quit':
			quit = True
			print "You got " + str(correct_answers) + " correct out of " + str(number_of_questions)

		elif question[lang_answer] == answer:
			print "Correct! \n"
			correct_answers = correct_answers + 1 
			number_of_questions = number_of_questions + 1
		
		else:
			print "Wrong! The answer is: " + question[lang_answer] + "\n"
			number_of_questions = number_of_questions + 1


swedishtest()