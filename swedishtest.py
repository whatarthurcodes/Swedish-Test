import sys
import random 

bank_one = [['bor', 'live'], ['de','they'],['den', 'it'],['det', 'it'],['det ar', 'it is'],['du', 'you'],['fran', 'from'],['gillar', 'like'],['gor', 'do', "does"],['han', 'he'],['heter', 'is called'],['hon', 'she'],['har', 'here'],['horsal', 'lecture hall'],['i', 'in'],['idag', 'today'],['jag', 'I'],['kommer', 'come']]
# bank_two = [['english', 'swedish'], ['english2','swedish2']]

def swedishtest():
	
	word_bank = choose_module()
	
	questions(word_bank)

	
def choose_module():
	word_bank = False
	while word_bank is False:
		module_choice = raw_input('What module do you want to be tested on? ')
		print module_choice

		if module_choice == '1' or module_choice == 'one':
			print "You have selected " + module_choice
			return bank_one 
		
		# if module_choice == '2' or module_choice == 'two':
		# 	print "You have selected " + module_choice
		# 	return bank_two

		else:
			print "No module exists for " + module_choice
			print "Please select again."
			word_bank = False



def questions(word_bank):
	answer = 'answer'
	quit = False
	number_of_words = len(word_bank)
	correct_answers = 0
	number_of_questions =0

	while quit is False:
		rand = random.randint(0, number_of_words-1)
		question = word_bank[rand]
		answer = raw_input(question[0] + '\n')

		if answer == 'q' or answer == 'quit':
			quit = True
			print "You got " + str(correct_answers) + " corect out of " + str(number_of_questions)


		if question[1] == answer:
			print "Correct!"
			correct_answers = correct_answers + 1 
			number_of_questions = number_of_questions + 1
		else:
			print "Wrong!"
			number_of_questions = number_of_questions + 1



swedishtest()