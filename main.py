# main.py
# ShiroFramework 1.0
import config, response

__version__     = config.VERSION
__update__      = config.DATE
__author__      = '@WhiteFish_Shiromi'
__maintainer__  = "@WhiteFish_Shiromi"
__framwork__    = "Shiromi Bot Framework (Python)"

class app:
    def __init__(self):
        '''Active Bot'''
        response.botActive()

if __name__ == '__main__':
    app = app()