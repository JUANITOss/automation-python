#!/usr/bin/env python3

import webbrowser, sys, clipy

# Get the URL from the command-line arguments
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:  ])
else:
    address = clipy.paste()
  
# Open Google Maps and search for the address
maps_url = f"https://www.google.com/maps/search/{address}"
webbrowser.open(maps_url)
