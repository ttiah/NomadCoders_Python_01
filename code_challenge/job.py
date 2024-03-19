class Job:
    def __init__(self, title, company, location, link):
        self.title = title
        self.company = company
        self.location = location
        self.link = link

    def __str__(self):
        return f'[Title] {self.title}, [Company] {self.company}, [Link] {self.link}'
