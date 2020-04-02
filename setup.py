import os

print("\n\nTo use Bettershift, you need redshift and libappindicator3.\n\nsudo apt install redshift libappindicator3\n\n")

dir = os.path.abspath(os.path.dirname(__file__))

os.system("touch "+dir+"/abetterredshift.desktop")
os.system("chmod 777 "+dir+"/abetterredshift.desktop")
file_name = dir + "/abetterredshift.desktop"
with open(file_name, 'w') as f:
	try:
		f.write("[Desktop Entry]\n")
		f.write("Name=A Better Redshift\n")
		f.write("Terminal=false\n")
		f.write("Type=Application\n")
		f.write("Exec="+dir+"/a-better-redshift.py\n")
		f.write("Icon="+dir+"/icon.png\n")
		f.close()
		os.system("mkdir -p ~/.local/share/applications")
		os.system("mv "+dir+"/abetterredshift.desktop ~/.local/share/applications")
		print ("A menu entry has been added to ~/.local/share/applications")
	except:  
		print("ERROR\n\n")
		



