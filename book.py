class Book:
    def __init__(self, title, author, year, pages):
        self._title = title
        self._author = author
        self._year = year
        self._pages = pages

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def __str__(self):
        return f"{self._title}, {self._author}, {self._year}, {self._pages}"

    def __eq__(self, other):
        return self._title == other._title and self._author == other._author

    def __lt__(self, other):
        if self._year == other._year:
            return self._pages > other._pages
        else:
            return self._year < other._year