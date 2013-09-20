#!/usr/bin/env python

import gtk, gobject

class MyWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self.connect("destroy", gtk.main_quit) 

        self.box = gtk.VBox()
        self.add(self.box)

        self.push_button = gtk.Button(label='push')
        self.push_button.connect('clicked', self.on_button_clicked)
        self.box.pack_start(self.push_button, True, True, 0)

        self.sbar = gtk.Statusbar()
        self.box.pack_start(self.sbar, True, True, 0)
        self.sbar_context_id = self.sbar.get_context_id('printer')
        
        self.pbar = gtk.ProgressBar()
        self.box.pack_start(self.pbar, True, True, 0)
        self.progress = 0.0

        self.timer = gobject.timeout_add(1000, self.pbar_timeout)

        self.show_all()

    def pbar_timeout(self):
        self.progress += 0.1
        self.pbar.set_fraction(self.progress)
        if self.progress < 1:
            return True
        else:
            return False

    def on_button_clicked(self, widget):
        self.sbar.push(self.sbar_context_id, str(self.progress))
        return

if __name__ == '__main__':
    # UI initialization
    win = MyWindow()
    gtk.main()


