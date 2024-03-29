:Date: 2022-07-10
:Version: 1.0.3
:Authors:
    * Mohammad Alghafli <thebsom@gmail.com>

cofan is an http server library for serving files and any other things. You use
it to share content in the form of a website. The current classes give you the
following:
    
  * Serve the content of a local directory in a form similar to file browser
    with icons for directories and files based on their extension.
  * Serve the content of a local zip file the same way as the local
    directories.
  * Serve local html files as a web site.
  * Upload to existing directory.
  * Organize your urls in prefix trees.
  * Response differently for different ip addresses

It also supports requests of partial files to resume previously interrupted
download.

Here is an example of how to use it::
    
  from cofan import *
  
  #allows uploads
  from cofan.utils.tfman import TFMan
  import pathlib
  
  #our site will be like this:
  # /           (this is our root. will list all the branches below)
  # |
  # |- vid/
  # |  this branch is a file browser for videos
  # |
  # -- site/
  #    this will be a web site. just a collection of html files
  
  #lets make an http file browser and share our videos
  #first, we specify the icons used in the file browser
  #you can omit the theme. it defaults to `humanity`
  icons = Iconer(theme='humanity')
  
  #now we create a Filer and specify the path we want to serve
  vid = Filer(pathlib.Path.home() / 'Videos', iconer=icons, tfman=TFMan())
  
  #we also want to serve a web site. lets create another filer. since the root
  #directory of the site contains `index.html` file, the filer
  #will automatically redirect to it instead of showing a file browser
  #no file browser also means we do not need to specify `iconer`
  #parameter. you can still use it if you want but that would not be very
  #useful
  site = Filer(pathlib.Path.home() / 'mysite')
  
  #now we need to give prefixes to our branches
  #we create a patterner
  patterns = Patterner()
  
  #then we add the filers with their prefixes
  #make sure to add a trailing slash
  patterns.add('vid/', vid)
  patterns.add('site/', site)
  
  #now we have all branches. but what if the user types our root url?
  #the path we will get will be an empty string which is not a prefix of any
  #branch. that will be a 404
  #lets make the root list and other branches added to `patterns`
  #the branches will be shown like the file browser but now the icons will be
  #for the patterns instead of file extensions
  #we need to specify where the icons are taken from
  #the icons file should contain an icon named `vid.<ext>` and an icon named
  #`site.<ext>` where <ext> can be any extension.
  root = PatternLister(patterns, root=pathlib.Path.home() / 'icons.zip')
  
  #and we add our root to the patterns with empty prefix
  patterns.add('', root)
  
  #now we create our handler like in http.server. we give it our patterner
  handler = BaseHandler(patterns)
  
  #and create our server like in http.server
  srv = Server(('localhost', 8000), handler)
  
  #and serve forever
  srv.serve_forever()
  
  #now try to open your browser on http://localhost:8000/

This module can also be run as a main python script to serve files from a
directory.

commandline syntax::

    python -m cofan.py [-a <addr>] [-u] [-nu] [<root>]

options:

    * -a <addr>, --addr <addr>: specify the address and port to bind to. <addr>
      should be in the form `<ip>:<port>` where `<ip>` is the ip address and
      `<port>` is the tcp port. defaults to `localhost:8000`.
    * -u, --upload: allow uploads. defaults to False.
    * -nu, --no-upload: opposite -u option. disallow uploads. this is selected
      by default.

args:

    * root: The root directory to serve. Defaults to the current directory.

--------
Tutorial
--------
Check out cofan tutorial at http://cofan.readthedocs.io/

