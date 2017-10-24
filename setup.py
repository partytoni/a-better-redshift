import os

os.system("sudo apt-get install redshift")
os.system("touch "+os.path.abspath(os.path.dirname(__file__))+"/abetterredshift.desktop")
os.system("chmod 777 "+os.path.abspath(os.path.dirname(__file__))+"/abetterredshift.desktop")
file_name = os.path.abspath(os.path.dirname(__file__)) + "/abetterredshift.desktop"
with open(file_name, 'w') as f:
    try:
        f.write("Name=A Better Redshift\n")
        f.write("Exec="+os.path.abspath(os.path.dirname(__file__))+"/a-better-redshift.py\n")
        f.write("Icon="+os.path.abspath(os.path.dirname(__file__))+"/icon.png\n")
        f.write("Hidden=true")
        f.close()
    except:  # whatever reader errors you care about
        print("ERROR\n\n")
        # setting temperature
os.system("mv "+os.path.abspath(os.path.dirname(__file__))+"/abetterredshift.desktop ~/.local/share/applications")
