import os

print("\n\nTo use Bettershift, you need redshift and libappindicator3.\n\n")

os.system("touch "+os.path.abspath(os.path.dirname(__file__))+"/abetterredshift.desktop")
os.system("chmod 777 "+os.path.abspath(os.path.dirname(__file__))+"/abetterredshift.desktop")
file_name = os.path.abspath(os.path.dirname(__file__)) + "/abetterredshift.desktop"
with open(file_name, 'w') as f:
	try:
		f.write("[Desktop Entry]\n")
		f.write("Name=A Better Redshift\n")
		f.write("Terminal=false\n")
		f.write("Type=Application\n")
		f.write("Exec="+os.path.abspath(os.path.dirname(__file__))+"/a-better-redshift.py\n")
		f.write("Icon="+os.path.abspath(os.path.dirname(__file__))+"/big_icon.png\n")
		f.close()
	except:  
		print("ERROR\n\n")
		
os.system("mv "+os.path.abspath(os.path.dirname(__file__))+"/abetterredshift.desktop ~/.local/share/applications")

print ("A menu entry has been added to ~/.local/share/applications")
