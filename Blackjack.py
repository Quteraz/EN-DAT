class Blackjack():
	"""a simple card counter for Blackjack"""
	
	def __init__(self, number_of_decks=1):
		self.number_of_decks = number_of_decks
		self.running_count = 0
	
	#When new card is revealed
	def add_card(self, card):
		if card in ['A' , 'K', 'Q', 'J', '10']:
			self.running_count += -1
		elif card in ['2','3','4','5','6']:
			self.running_count += 1

	def get_running_count(self):
		return self.running_count // self.number_of_decks


# Testing
if __name__ == '__main__':
	import random

	cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
	bj = Blackjack()
	for _ in range(14):   		#['3','10','8','7','4','6','7']:
		card = cards[ random.randint(0,12*4) % 12]
		print("Adding card: \t {}".format(card))
		bj.add_card(card)
		print("RC: {}".format(bj.get_running_count()))