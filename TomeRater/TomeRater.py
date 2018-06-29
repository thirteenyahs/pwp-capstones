class User(object):
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.books = {}
		
	def get_mail(self):
		return self.email
	
	def change_email(self, address):
		self.email = address
		print(self.name + " has updated their email address to " + self.email)
		
	def get_average_rating(self):
		average = 0
		books_rated = 0
		for value in self.books.values():
			if value:
				average += value
				books_rated += 1
		average = average/books_rated
		return average
		
	def read_book(self, book, rating = None):
		self.books[book] = rating
		
	def _repr_(self):
		return "User " + self.name + ", EMAIL ADDRESS: " + self.email + ", number of books read: " + str(len(self.books))
		
	def __eq__(self, other_user):
		if self.name == other_user.name and self.email == other_user.email:
			return True
		return False
		
class Book(object):
	def __init__(self, title, isbn):
		self.title = title
		self.isbn = isbn
		self.ratings = []
	
	def get_title(self):
		return self.title
	
	def get_isbn(self):
		return self.isbn
	
	def set_isbn(self, isbn):
		self.isbn = isbn
		print("The title: " + self.title + " now has a ISBN of "+ str(self.isbn))
		
	def add_rating(self, rating):
		if rating > 0 and rating <= 4:
			self.ratings.append(rating)
		else:
			print ("Invalid Rating")

	def __eq__(self, other_book):
		if self.title == other_book.title and self.isbn == other_book.isbn:
			return True
		return False
		
	def get_average_rating(self):
		average = 0
		for value in self.ratings:
			average += rating
		average = average/len(self.ratings)
		return average
	
	def	__hash__(self):
		return hash((self.title, self.isbn))

class Fiction(Book):
	def __init__(self, title, author, isbn):
		Book.__init__(self, title, isbn)
		self.author = author
	
	def get_author(self):
		return self.author
		
	def __rep__(self):
		return self.title + " by " + self.author
		
class Non_Fiction(Book):
	def __init__(self, title, subject, level, isbn):
		Book.__init__(self, title, isbn)
		self.subject = subject
		self.level = level
	
	def get_subject(self):
		return self.subject
		
	def get_level(self):
		return self.level
		
	def __rep__(self):
		return self.title + ", a " + self.level + " manual on " + self.subject
		
class TomeRater(object):
	def __init__(self):
		self.users = {}
		self.books = {}
		
	def create_book(self, title, isbn):
		created_book = Book(title, isbn)
		return created_book
		
	def create_novel(self, title, author, isbn):
		created_book = Novel(title, author, isbn)
		return created_book
	
	def create_non_fiction(self, title, subject, level, isbn):
		created_book = Non_Fiction(title, subject, level, isbn)
		return created_book
	
	def add_book_to_user(self, book, email, rating = None):
		user = self.users.get(email, None)
		if user:
			user.read_book(book, rating)
			if book not in self.books:
				self.books[book] = 0
			self.books[book] +=1
			book.add_rating(rating)
		else:
			print("No user with email " + email + "!")
				
	def add_user(self, name, email, book_list = None):
		new_user = User(name, email)
		self.users[email] = new_user
		if user_books:
			for book in user_books:
				self.add_book_to_user(book, email)
				
	def print_catalog(self):
		for books in self.books:
			print (books)
			
	def print_users(self):
		for users in self.users.values():
			print (users)
			
	def most_read_book(self):
		max_reads = float("-inf")
		most_read = None
		
		for book in self.books:
			read = self.books[book]
			if read > max_reads:
				max_reads = read
				most_read = book
		return most_read
		
	def highest_rated_book(self):
		highest_rating = float("-inf")
		highest_rated_book = None

		for book in self.books:
			average = book.get_average_rating()
			if average > highest_rating:
				highest_rating = average
				highest_rated_book = book

		return highest_rated_book
		
	def most_positive_user(self):
		highest_rated = flat("-inf")
		most_positive = None
		
		for user in self.users:
			average = user.get_average_rating()
			if average > highest_rated:
				highest_rated = average
				most_positive = user
				
		return most_positive
		
		