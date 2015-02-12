import sys
import random 

bank_one = [['bor', 'live'], ['de','they'],['den', 'it'],['det', 'it'],['det ar', 'it is'],['du', 'you'],['fran', 'from'],['gillar', 'like'],['gor', 'do', "does"],['han', 'he'],['heter', 'is called'],['hon', 'she'],['har', 'here'],['horsal', 'lecture hall'],['i', 'in'],['idag', 'today'],['jag', 'I'],['kommer', 'come']]
# bank_two = [['english', 'swedish'], ['english2','swedish2']]



def swedishtest():
	
	word_bank = choose_module()
	lang = choose_lang()
	
	questions(word_bank, lang)

	
def choose_module():
	word_bank = False
	while word_bank is False:
		module_choice = raw_input('What module do you want to be tested on? ')
		print module_choice

		if module_choice == '1' or module_choice == 'one':
			print "You have selected " + module_choice + "\n"
			return bank_one 
		
		# if module_choice == '2' or module_choice == 'two':
		# 	print "You have selected " + module_choice
		# 	return bank_two

		else:
			print "No module exists for " + module_choice
			print "Please select again."
			word_bank = False

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