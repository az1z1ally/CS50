class Book:
	"""Book Class"""

	def __init__(self, title, author):
		#super(Book, self).__init__()
		self.title = title
		self.author = author

	def print_info(self):
		print(f'{self.title} by {self.author}')


	def __repr__(self):
		return self.title
		