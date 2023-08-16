class Author:
    def __init__(self,name):
        self.name = name
        self.author_contracts = []
        self.author_books = []

    def add_contract(self, contract):
        self.author_contracts.append(contract)

    def contracts(self):
        return self.author_contracts
    
    def add_book(self, book):
        self.author_books.append(book)

    def books(self):
        return self.author_books
    
    def sign_contract(self, author, date, royalties):
        contract = Contract(self, author, date, royalties)
        return contract
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
    
class Book:

    def __init__(self, title):
        self.title = title
        self.book_contracts = []
        self.book_authors = []

    def add_contract(self, contract):
        self.book_contracts.append(contract)

    def contracts(self):
        return self.book_contracts
    
    def add_author(self, author):
        self.book_authors.append(author)

    def authors(self):
        return self.book_authors

class Contract:
    
    all=[]

    def __init__(self, author, book, date="", royalties=0):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all.append(self)
    
        if not isinstance(author, Author):
            raise Exception("Not an author")
        
        if not isinstance(book, Book):
            raise Exception("Not a book")
        
        if not isinstance(date, str):
            raise Exception("Date is not a string")
        
        if not isinstance(royalties, int):
            raise Exception("Not an int")
    
        author.add_contract(self)
        author.add_book(book)
        book.add_contract(self)
        book.add_author(author)

    
    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda contract: contract.date)