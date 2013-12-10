# !c:\python26\python.exe
#  -*- coding: UTF-8 -*-
#  +----------------------------------------+
#  |Author: Lau Gin San (CopyLiu)           |
#  |Email:copyliu@gmail.com                 |
#  |                                        |
#  |License:BSD License                     |
#  +----------------------------------------+
#  $Id: setup.py 284 2010-07-29 10:23:39Z copyliu $



# setup.py
# ...
# ModuleFinder can't handle runtime changes to __path__, but win32com uses them
try:
    # py2exe 0.6.4 introduced a replacement modulefinder.
    # This means we have to add package paths there, not to the built-in
    # one.  If this new modulefinder gets integrated into Python, then
    # we might be able to revert this some day.
    # if this doesn't work, try import modulefinder
    try:
        import py2exe.mf as modulefinder
    except ImportError:
        import modulefinder
    import win32com, sys
    for p in win32com.__path__[1:]:
        modulefinder.AddPackagePath("win32com", p)
    for extra in ["win32com.shell"]: #,"win32com.mapi"
        __import__(extra)
        m = sys.modules[extra]
        for p in m.__path__[1:]:
            modulefinder.AddPackagePath(extra, p)
except ImportError:
    # no build path setup, no worries.
    pass

from distutils.core import setup
import py2exe
includes = ["encodings", "encodings.*"  ]
filelist= []

py2exe_options = dict(
                      ascii=True,  # Exclude encodings
                      excludes=['_ssl',],  # Exclude _ssl
                                #'pyreadline', 'difflib', 'doctest',
                                #'optparse', 'pickle', 'calendar'],  # Exclude standard library
                      dll_excludes=['msvcp90.dll'],  # Exclude msvcr71
                      compressed=True,  # Compress library.zip
                      includes= includes,
                      bundle_files=1,
                      optimize= 2,
                      typelibs = [
        # typelib for 'Word.Application.8' - execute
        # 'win32com/client/makepy.py -i' to find a typelib.
        ('{C866CA3A-32F7-11D2-9602-00C04F8EE628}', 0,5, 4),
    ]
                      )



setup(
#data_files=filelist,
console=[{"script":"acfun_tts.py"}],
version = "1.2.0.0",
#description = u"永恆之塔字體替換工具",
name = u"ACFUN生放送彈幕播報",
author ="CopyLiu",
options = {"py2exe":py2exe_options
   
           },
zipfile = None,


)


