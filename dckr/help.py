
def PrintHelp():
    helptext = """

    dckr is a docker CLI alternative with shortcuts and added functionalities

    How to use dckr in CLI :
    ./dckr [arg1] [arg2] [arg3]

    arg1 :
        container or c : all commands related to containers
        image     or i : all commands related to images
        volume    or v : all commands related to volumes
        help           : print dckr help

    arg2 : applicable on object mentioned in arg1
        search    or s : search for a string within the object. Provide search string in arg3
        ls             : list all the object
        clean          : delete all the object

    arg3 : input to command mentioned in arg2
    
    """

    print(helptext)