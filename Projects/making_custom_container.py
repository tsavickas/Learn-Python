# With this class we are able to track of the number of various tags on a blog/article
# For exmample we wnat to know how many articles do we have with tag "Python"

class TagCloud:
    def __init__(self):     # define a constructor and initialize tags atributes
        # use dictionary because its allows quickly get us a number of a given tag
        # tag atribute we make private atribute with two underlines (__tag). That way we hide atribute from outside so we cannot easily access it
        self.__tags = {}

    def add(self, tag):
        # check if we have the tag in the dictionary. If don't have we set the value to 0, otherwise we incremented by 1
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        # this function returns an iterator object which gives us one item in a time in a for loop
        return iter(self.__tags)


# creating an object
cloud = TagCloud()

# Adding the tag with method add
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.__tags)

# getting a number of items in the container with magic method __len__
len(cloud)

# getting an item by its tag with magic method __getitem__
cloud["python"]

# set a number for a given tag with magic method __setitem__
cloud["python"] = 10

# iterrating over the container with magic method __iter__
for tag in cloud:
    print(tag)
