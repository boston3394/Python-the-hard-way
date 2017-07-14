PYTHON NOTES

Use ATOM as your text editor

Escape	What it does.
\\	Backslash (\)
\'	Single-quote (')
\"	Double-quote (")
\a	ASCII bell (BEL)
\b	ASCII backspace (BS)
\f	ASCII formfeed (FF)
\n	ASCII linefeed (LF)
\N{name}	Character named name in the Unicode database (Unicode only)
\r	Carriage Return (CR)
\t	Horizontal Tab (TAB)
\uxxxx	Character with 16-bit hex value xxxx (u'' string only)
\Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (u'' string only)
\v	ASCII vertical tab (VT)
\ooo	Character with octal value ooo
\xhh	Character with hex value hh

https://first-web-scraper.readthedocs.io/en/latest/ - useful python tutorial

django-admin startproject firstdjango

get-pip.py 

python manage.py to see list of available commands

to run them its python manage.py <command name>

python manage.py runserver

localhost:8000

python manage.py startapp to start your app 

role of folders
manage.py runs commands
init_.py tells django where project folder is
wsgi.py provides a hook for webservers
settings.pyconfigures django - DO EDIT
urls.py routes requests on url - DO EDIT

Django - an app is a folder with python files. it is a componant
program is the overall thing that contains multiple apps
