# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects
class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        # Use references to other objects, like author and chapters
        self.author = author
        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result


class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount


auth = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.95, auth)

b1.addchapter(Chapter("Chapter 1", 104))
b1.addchapter(Chapter("Chapter 2", 89))
b1.addchapter(Chapter("Chapter 3", 124))

print(b1.title)
print(b1.author)
print(b1.getbookpagecount())

'''information about the author. Rather than defining all of the author related information, directly within the book class hierarchy. 
This type of model lets us extract distinct ideas, and put them into their own classes. Now, inheritance and composition are not exclusive, 
you can combine both depending on what your applications needs are. So let's apply this concept in some real code, to see how it works. 
Well here in VS code, let's go ahead and open up the composition underscore start. And I've defined a book class that's a little 
bit different than the one we've been using so far. So there's the title and the price, along with some author information, 
the first and last name, and there's an attribute to hold the list of chapter information.
There's also a method to add chapters to the book, and it takes the name of the chapter and the pages
count and just adds a tuple to this collection right here. Now, this particular class definition is all fine and good, 
but it's pretty monolithic. There are pieces of information like the author, and maybe the chapter information that might
make sense to treat as separate entities. It's not hard to imagine a scenario where we might want to work with just a 
 group of authors or get information about specific book chapters. 
 So we can use composition to separate these discrete pieces of information from the overall book object. 
 So let's start by extracting the author information into its own class. So I'll make a class called author, and we'll go ahead and implement the init method, 
 and that will take a first and last name, and we'll just go ahead and store that on some attributes. 
 Okay? And while we're at it, let's go ahead and give that author class A nice string representation, 
 and we'll learn more about this when we get to the chapter on magic methods. But I'm going to override this string method, 
 and I'm going to return just a nicely formatted string consisting of the first name, and the last name. So then I have to modify the book class, 
 to take an author object as an argument. So I'll go ahead and replace this with author, and that's going to default to none. And then I can get rid of these two, 
 and replace that with self dot author equals author. So now, we've created a relationship where a book has an author associated with it, instead of keeping that 
 implementation details of the author data, wrapped up within the book class. We can do the same thing with the chapter information. So let's go ahead and create a separate class for the chapters. 
 And I'll create chapter objects and I'll, implement the init method for that. And that's going to take a chapter name and a page count. And we'll just go ahead and set those properties. All right. And now we have to modify the add chapter, 
method in the book class 'cause it no longer takes separate name and pages, it takes a chapter, and our chapters collection, just adds that chapter to the list. And so here again, we've now created 
a relationship where a book has a collection of chapter objects. We can even add a new method, and we'll call this get book page count, whereby the book can calculate its own page count. So we'll start off with zero and
we'll just iterate over each one of the chapters, and then we'll add up the chapter page count, and then we'll return that result. All right. So now let's clean up the code that uses these classes down here. So for the book,
I now need to pass an author constructor in here, so I'll just go ahead and create an author. All right, and we'll pass that in as the second argument here. Alright, and now we have to add chapter objects to the book. 
So this is going to become a chapter object. Alright and I'm going to just copy and paste that each time, and we'll close that off. Looks like they've added an extra one. There we go. Okay, so now we get some nice separation of responsibilities. 
So for example, printing the full name of the author, is done within the author class. So we can print out the books author, and we'll leave the title alone. And calculating the book size is done by using the data, that's in the chapter class. 
So we'll print out the page count. Alright, so it looks like everything is now in place. We've got our extracted chapter and author objects, and we've updated the book class to use that data instead. So let's go ahead and run our updated code. 
And you can see, right here, so the title is unchanged, and now here is the author information being printed out from the author class, and there is the total page count. So what we've done is taken a monolithic class definition, 
and made it more extensible and flexible, by composing it from simpler class objects, each of which is responsible, for its own features and data.'''