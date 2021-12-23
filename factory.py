from . import file
from . import  output_cond
from . import screen
from . import options

def create(OutputType):
    if OutputType == "file":
        options = options.Options()
        fileoptions.filename = "arquivo.txt"
        CreatedObjetc = file.File()
    elif OutputType == "screen":
        CreatedObject = screen.Screen()

    CreatedObject.initialize(ObjectOptions)
    return createdObject
