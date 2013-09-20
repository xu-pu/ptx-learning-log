#!/usr/bin/env python

import gtk, webkit

class MyWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self.connect('delete-event', gtk.main_quit)

        self.container = gtk.Box()

        self.webpage = webkit.WebView()
        main_html = open('/home/sheep/Dropbox/code/random-tests/pygtk/main.html', 'rb').read()
        page.load_html_string(main_html, 'file:///')

        self.button1 = gtk.Button(label='Button1')
        self.button1.connect('clicked', self.on_button_clicked)

        self.button2 = gtk.Button(label='Button2')
        self.button2.connect('clicked', self.on_button_clicked)

        self.add(self.container)
        self.container.pack_start(self.webpage, True, True, 0)
        self.container.pack_start(self.button1, True, True, 0)
        self.container.pack_start(self.button2, True, True, 0)

    def on_button_clicked(self, view):
        print 'Hello, World'


my_window = MyWindow()
my_window.set_title('My Web App')
my_window.show_all()
gtk.main()


