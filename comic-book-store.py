from bottle import run, route, get, post, request, view, static_file
from itertools import count
 #BUILD LOG
 #Ver1.0, create main pytohn framework with test data, class and run code.
 
 
 
 
#Ver1.0 Creation of ComicBook class
class ComicBook:
    _ids = count(0)

    def __init__(self,title,stock, price, description, image):
        self.id = next(self._ids)
        self.title = title
        self.stock = stock
        self.price = price
        self.description = description
        self.image = image

#ver1.0 Creatioon of test data       
comicBooks = [
    ComicBook("Water Woman", 0, 19.99, "This book sucks, don't buy it.", "/image/bookstore-cat.jpg"),
    ComicBook("Not Water Woman", 1, 15.99, "This book is very good thus you should buy it.", "/image/bookstore-cat.jpg"),
    ComicBook("Wagon Wars", 3, 8.49, "In a world full of wagons, one wagon will destroy them all!", "/image/bookstore-cat.jpg")
    ]

#Images
@route('/image/<filename>')
def server_static(filename):
    return static_file(filename, root='./assets')


#Code to be able to link custom css Ver1.1
@route('/<filename>.css')
def stylesheets(filename):
    return static_file('{}.css'.format(filename), root='./assets')



#Ver1.0
#PAGES 

@route('/')
@view('index')
def index():
    #need this function to attatch decorators above
    pass


#Ver1.2 Book List Page
@route('/book-list')
@view('book-list')
def book_list(): 
    #make a dictionary of the comicBooks in stock
    data = dict(comics = comicBooks)
    return data

#Ver1.3 Book List Success Page
@route('/book-list-success/<comic_id>')
@view('book-list-success')
def book_list_success(comic_id):
    comic_id = int(comic_id)
    found_comic = None
    for comic in comicBooks:
        if comic.id == comic_id:
            found_comic = comic
            break
    data = dict(comic = found_comic)
    return data 

#Ver1.3 Buy book success page
@route('/buy-book-success/<comic_id>', method="POST")
@view('buy-book-success')
def buy_book_success(comic_id):
    comic_id = int(comic_id)
    found_comic = None
    for comic in comicBooks:
        if comic.id == comic_id:
            found_comic = comic
            break
    data = dict(comic = found_comic)
    found_comic.stock -= 1
    return data   

#ver1.4 Restock Page
@route("/restock-page")
@view('restock-page')
def restock_page():
    data = dict(comics = comicBooks)
    return data

#ver1.4 Success page for a new book 
@route("/new-book-success", method="POST")
@view("new-book-success")
def new_book_success():
    title = request.forms.get("title")
    stock = request.forms.get("stock")
    price = request.forms.get("price")
    description = request.forms.get("description")
    image = "/image/bookstore-cat.jpg"
    
    new_comic = ComicBook(title, stock, price, description, image)
    comicBooks.append(new_comic)

#Ver1.4.1 Restock Success Page for the actual restocking of a book
@route("/restock-success/<comic_id>")
@view("restock-success")
def restock_success(comic_id):
    pass
    
#reloader = True breaks the code? Only at home PC though???? apparantly is a server issue
run(host='localhost', port=8080, debug=True)
#run(host='0.0.0.0', port=8080, reloader= True, debug=True)