class File(self, options):
    def __init__(self):
        self.file = None

    def initialize(self, options):
        self.file = open(options.filename, 'w')

    def print(self, name, date):
        try:

