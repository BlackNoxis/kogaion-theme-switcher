#! /usr/bin/env python
# -*- coding: utf-8 -*-

import gtk
import sys

from core.configurator import set_theme
from core.desktop_env_detect import desktop_env_detect
from core.desktop_env_detect import desktop_environments


def main():
    label = gtk.Label((" "*9) +"""Welcome to Kogaion theme switcher!\nAttempting Desktop Environment auto detection.\n""")
    dialog = gtk.Dialog("Kogaion theme switcher", None,
			gtk.DIALOG_MODAL,
			(gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT, gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))
    dialog.vbox.pack_start(label)
    label.show()
    response = dialog.run()
    dialog.destroy()


    if response == -3:
        desktop_env = desktop_env_detect()

        env = filter(lambda x: desktop_env in x, desktop_environments)[0]
        if env:
            if env == 'generic' :
	        label = gtk.Label("Cannot detect Desktop Environment!\n Please choose one of the following: \n")
                dialog = gtk.Dialog("Kogaion theme switcher", None,
			gtk.DIALOG_MODAL, (gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT))
                dialog.vbox.pack_start(label)
	        label.show()
	        dialog.add_button("MATE", -13)
	        dialog.add_button("Cinnamon", -14)
	        response = dialog.run()
	        if response == -13:
		    label = gtk.Label((" "*9) +"""MATE Desktop Environment selected.\nWould you like Kogaion Theme in Light or Dark colors?\n""")
		    dialog = gtk.Dialog("Kogaion theme switcher", None,
					gtk.DIALOG_MODAL, (gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT))
                    dialog.vbox.pack_start(label)
	            label.show()
		    dialog.add_button("Dark", 0)
		    dialog.add_button("Light", 1)
		    response = dialog.run()

		    if response == 0:
		        set_theme("mate", 0)
		    elif response == 1:
		        set_theme("mate", 1)
		    else:
		        if response == -2 or response == -1:
			    sys.exit(0)

	            dialog.destroy()
              
		elif response == -14:
		    label = gtk.Label((" "*9) +"""Cinnamon Desktop Environment selected.\nWould you like Kogaion Theme in Light or Dark colors?\n""")
		    dialog = gtk.Dialog("Kogaion theme switcher", None,
					gtk.DIALOG_MODAL, (gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT))
                    dialog.vbox.pack_start(label)
	            label.show()
		    dialog.add_button("Dark", 0)
		    dialog.add_button("Light", 1)
		    response = dialog.run()

		    if response == 0:
		        set_theme("cinnamon", 0)
		    elif response == 1:
		        set_theme("cinnamon", 1)
		    else:
		        if response == -2 or response == -1:
			    sys.exit(0)

	            dialog.destroy()
		else:
		    if response == -2 or response == -1:
		        sys.exit(0)
	        dialog.destroy() 
    	    elif env == 'xfce':
                label = gtk.Label((" "*9) +"""Xfce Desktop Environment detected.\nWould you like Kogaion Theme in Light or Dark colors?\n""")
		dialog = gtk.Dialog("Kogaion theme switcher", None,
					gtk.DIALOG_MODAL, (gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT))
                dialog.vbox.pack_start(label)
	        label.show()
		dialog.add_button("Dark", 0)
		dialog.add_button("Light", 1)
		response = dialog.run()

		if response == 0:
		    set_theme("xfce", 0)
		elif response == 1:
		    set_theme("xfce", 1)
		else:
		    if response == -2 or response == -1:
			sys.exit(0)

	        dialog.destroy()
              
	    elif env == 'gnome':
	        label = gtk.Label((" "*9) +"""Gnome Desktop Environment detected.\nWould you like Kogaion Theme in Light or Dark colors?\n""")
		dialog = gtk.Dialog("Kogaion theme switcher", None,
			gtk.DIALOG_MODAL, (gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT))
                dialog.vbox.pack_start(label)
	        label.show()
		dialog.add_button("Dark", 0)
		dialog.add_button("Light", 1)
		response = dialog.run()

		if response == 0:
		    set_theme("gnome", 0)
		elif response == 1:
		    set_theme("gnome", 1)
		else:
		    if response == -2 or response == -1:
			sys.exit(0)

	        dialog.destroy()
              
	    elif env == 'kde':
	        label = gtk.Label((" "*9) +"""KDE Desktop Environment detected.\nWould you like Kogaion Theme in Light or Dark colors?\n""")
		dialog = gtk.Dialog("Kogaion theme switcher", None,
					gtk.DIALOG_MODAL, (gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT))
                dialog.vbox.pack_start(label)
	        label.show()
		dialog.add_button("Dark", 0)
		dialog.add_button("Light", 1)
		response = dialog.run()

		if response == 0:
		    set_theme("kde", 0)
		elif response == 1:
		    set_theme("kde", 1)
		else:
		    if response == -2 or response == -1:
			sys.exit(0)

	        dialog.destroy()
              
	    else:
	        label = gtk.Label(" "*5+ "Cannot detect Desktop Environment\nPlease choose one of the following: \n")
                dialog = gtk.Dialog("Kogaion theme switcher", None,
			gtk.DIALOG_MODAL, (gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT))
                dialog.vbox.pack_start(label)
	        label.show()
	        dialog.add_button("MATE", -13)
	        dialog.add_button("Cinnamon", -14)
	        response = dialog.run()
		
		if response == -13:
		    label = gtk.Label((" "*9) +"""MATE Desktop Environment selected.\nWould you like Kogaion Theme in Light or Dark colors?\n""")
		    dialog = gtk.Dialog("Kogaion theme switcher", None,
					gtk.DIALOG_MODAL, (gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT))
                    dialog.vbox.pack_start(label)
	            label.show()
		    dialog.add_button("Dark", 0)
		    dialog.add_button("Light", 1)
		    response = dialog.run()

		    if response == 0:
		        set_theme("mate", 0)
		    elif response == 1:
		        set_theme("mate", 1)
		    else:
		        if response == -2 or response == -1:
			    sys.exit(0)


	            dialog.destroy()
              
		elif response == -14:
		    label = gtk.Label((" "*9) +"""Cinnamon Desktop Environment selected.\nWould you like Kogaion Theme in Light or Dark colors?\n""")
		    dialog = gtk.Dialog("Kogaion theme switcher", None,
					gtk.DIALOG_MODAL, (gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT))
                    dialog.vbox.pack_start(label)
	            label.show()
		    dialog.add_button("Dark", 0)
		    dialog.add_button("Light", 1)
		    response = dialog.run()

		    if response == 0:
		        set_theme("cinnamon", 0)
		    elif response == 1:
		        set_theme("cinnamon", 1)
		    else:
		        if response == -2 or response == -1:
			    sys.exit(0)


	            dialog.destroy()
		else:
		    if response == -2 or response == -1:
		        sys.exit(0)
	 
	        dialog.destroy()
    else:
        if response == -2 or response == -1:
           sys.exit(0)
			
   
    
if __name__ == '__main__':
    main()





