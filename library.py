from book import Book


class Library:
	"""Library Class"""

	def __init__(self):
		self.books = []


	def add_book(self, book):
		self.books.append(book)


	def check_out(self, title, name):
		for book in self.books:
			if book.title == title:
				book.check_out(name)
				return

		print('Book Not Found!')
		