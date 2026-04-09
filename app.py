from flask import Flask,request,jsonify

app=Flask(__name__)

books=[]#a list of book objects,each is a dict{id:int,title:str,author:str,price:float}
idCounter=1
@app.route("/books",methods=["GET"])
def getBooks():
    return jsonify(books),200

@app.route("/books/<int:id>",methods=["GET"])
def getBook(id):
    for book in books:
        if book["id"]==id:          
            return jsonify(book),200
    return jsonify({"error":"book not found"}),404

@app.route("/books",methods=["POST"])
def createBook():
    global idCounter

    data=request.get_json()
    if not data:
        return jsonify({"error":"you must at least provide title,author,or price"}),400
    book={}
    book["id"]=idCounter
    book["title"]=data.get("title","")
    book["author"]=data.get("author","")
    book["price"]=data.get("price",0)
    books.append(book)
    idCounter+=1
    return jsonify(book),201

@app.route("/books/<int:id>",methods=["PUT"])
def updateBook(id):
    data=request.get_json()
    if not data:
        return jsonify({"error":"no updated info"}),400
    
    for book in books:
        if book["id"]==id:
            book["title"]=data.get("title",book["title"])
            book["author"]=data.get("author",book["author"])
            book["price"]=data.get("price",book["price"])
            return jsonify(book),200
            

    return jsonify({"error":"book not found"}),404

@app.route("/books/<int:id>",methods=["DELETE"])
def deleteBook(id):
    global books
    for book in books:
        if book["id"]==id:
            books=[book for book in books if book["id"]!=id]
            return "",204
    return jsonify({"error":"book not found"}),404

