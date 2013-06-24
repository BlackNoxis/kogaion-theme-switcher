# -*- coding: utf-8 -*-

from subprocess import call

def set_theme(desktop_env, theme_id):
    if desktop_env == "xfce":
	if theme_id == 0:
	   call("xfconf-query -c xfwm4 -p /general/theme -s Kogaion-dark", shell=True)
	   call("xfconf-query -c xsettings -p /Net/ThemeName -s Kogaion-dark", shell=True)
	   call("xfconf-query -c xsettings -p /Net/IconThemeName -s Faenza-Kupertino-Dark", shell=True)   
    	elif theme_id == 1:
	   call("xfconf-query -c xfwm4 -p /general/theme -s Kogaion-light", shell=True)
	   call("xfconf-query -c xsettings -p /Net/ThemeName -s Kogaion-light", shell=True)
	   call("xfconf-query -c xsettings -p /Net/IconThemeName -s Faenza-Kupertino-Light", shell=True)
    elif desktop_env == "gnome":
	if theme_id == 0:
	    call('gsettings set org.gnome.desktop.interface gtk-theme "Kogaion-dark"', shell=True)
	    call('gsettings set org.gnome.desktop.wm.preferences theme "Kogaion-dark"', shell=True)
	    call('gsettings set org.gnome.desktop.interface icon-theme "Faenza-Kupertino-Dark"', shell=True)
	elif theme_id == 1:
	    call('gsettings set org.gnome.desktop.interface gtk-theme "Kogaion-light"', shell=True)
	    call('gsettings set org.gnome.desktop.wm.preferences theme "Kogaion-light"', shell=True)
	    call('gsettings set org.gnome.desktop.interface icon-theme "Faenza-Kupertino-Light"', shell=True)
    elif desktop_env == "mate":
	if theme_id == 0:
	    call('gsettings set org.mate.interface gtk-theme "Kogaion-dark"', shell=True)
	    call('gsettings set org.mate.interface icon-theme "Faenza-Kupertino-Dark"', shell=True)
	elif theme_id == 1:
	    call('gsettings set org.mate.interface gtk-theme "Kogaion-light"', shell=True)
	    call('gsettings set org.mate.interface icon-theme "Faenza-Kupertino-Light"', shell=True)
    elif desktop_env == "cinnamon":
	raise Exception("Not implemented yet.")
    elif desktop_env == "kde":
	raise Exception("Not implemented yet.")
		
	    
