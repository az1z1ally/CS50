from book import Book

class LibraryBook(Book):
	"""Special vesrion of a Book class for a Library"""

	def __init__(self, title, author, inventory):
		super().__init__(title, author)
		self.inventory = inventory
		self.borrowers = []


	def check_out(self, name):
		if self.inventory < 1:
			print('Sorry! Not available')
			return

		self.inventory -= 1

		self.borrowers.append(name)
