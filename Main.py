class Author:
    def __init__(self, name):
        self.Name = name

    def showAuthor(self):
        print("Author: ", self.Name)


class Album:
    def __init__(self, title, format, label):
        self.Title = title
        self.Format = format
        self.Label = label

    def addAuthor(self, author):
        self.Author = author

    def showAlbum(self):
        print("------- Album -------")
        self.Author.showAuthor()
        print("Title : ", self.Title)
        print("Format: ", self.Format, "\nLabel : ", self.Label)

    def getTitle(self):
        return self.Title


class Collection:
    def __init__(self):
        self.CollectionList = []

    def NumAlbums(self):
        return len(self.CollectionList)

    def AddAlbum(self, album):
        self.CollectionList = self.CollectionList + [album]

    def ShowCollection(self):
        print("#####################################")
        for item in self.CollectionList:
            item.showAlbum()
        print("#####################################")

    def DeleteAlbum(self, title):
        found = False
        positionDelete = -1
        for item in self.CollectionList:
            positionDelete += 1
            if item.getTitle() == title:
                found = True
                break
        if found:
            del self.CollectionList[positionDelete]
            print("Album deleted correctly!")
        else:
            print("Album not found")


def ShowMenu():
    print("""****** MENU ******
1) Add Album
2) Show Collection
3) Delete Album
4) Collection
5) Exit""")


def AddCollectionAlbum(collection):
    authorName = input("Artist name: ")
    title = input("Album title: ")
    format = input("Format: ")
    label = input("label: ")
    author = Author(authorName)
    album = Album(title, format, label)
    album.addAuthor(author)
    collection.AddAlbum(album)
    return collection


def ShowCollection(collection):
    collection.ShowCollection()


def DeleteAlbum(collection):
    title = input("Enter Album title to delete: ")
    collection.DeleteAlbum(title)


def NumAlbums(collection):
    print("Number of albums in collection: ", collection.NumAlbums())


end = False
collection = Collection()

while not end:
    ShowMenu()
    option = int(input("Select option:"))
    if (option == 1):
        collection = AddCollectionAlbum(collection)
    elif (option == 2):
        ShowCollection(collection)
    elif (option == 3):
        DeleteAlbum(collection)
    elif (option == 4):
        NumAlbums(collection)
    elif (option == 5):
        end = True

print("Bye!")
