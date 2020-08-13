from version import __version__
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import json
import os
import sys
import platform
import pyperclip
import argparse
import logging

parser = argparse.ArgumentParser()
parser.add_argument(
    '-d', '--debug',
    help="Print debugging info",
    action="store_const", dest="log_level", const=logging.DEBUG,
    default=logging.WARNING
)
parser.add_argument(
    '--verbose',
    help="Verbose logging",
    action="store_const", dest="log_level", const=logging.INFO,
)
parser.add_argument(
    "-v", "--version",
    help="Print version and exit",
    action="store_true"
)
parser.add_argument(
    "-b", "--basic",
    help="Run only a basic GUI",
    action="store_true"
)
args = parser.parse_args()

if args.version:
    print("Version "+__version__)
    exit()

logging.basicConfig(level=args.log_level)
logging.info("Version "+__version__)

class simpleClass():
  def toJSON(self):
        return json.dumps(self, default=lambda i: i.__dict__)

sys_info = simpleClass()

if getattr(sys, 'frozen', False):
        # we are running in a bundle
        sys_info.executed_by = "PyInstaller"
        bundle_dir = sys._MEIPASS
else:
        # we are running in a normal Python environment
        sys_info.executed_by = "Directly Python "+platform.python_version()
        bundle_dir = os.path.dirname(os.path.abspath(__file__))

sys_info.platform_all = platform.platform()
sys_info.os_system = platform.system()
sys_info.os_release = platform.release()+" - "+platform.version()
try:
    sys_info.linux_distro = platform.linux_distribution() #for Linux distro
except:
    sys_info.linux_distro = "N/A"

sys_info.mac_ver = platform.mac_ver() #for Mac version
if sys_info.mac_ver == ('', ('', '', ''), ''):
    sys_info.mac_ver = "N/A"

sys_info.win32_ver = platform.win32_ver() #for Mac version
if sys_info.win32_ver == ('', ('', '', ''), ''):
    sys_info.win32_ver = "N/A"

sys_info.machine = platform.machine()
sys_info.uname = platform.uname()
sys_info.sys_version = platform.version()

logging.info(sys_info.toJSON())
window = tk.Tk()
window.title("Simple Test Program")
logging.debug("tk window initialized")

img = ImageTk.PhotoImage(Image.open(os.path.join(bundle_dir, "res", "pythonlogo.png")))
image = tk.Label(image = img)
image.pack(side = "top", fill = "both", expand = "yes")
label = tk.Label(text="Hello from version "+__version__)
label.pack()

def copySystemInfoCallBack():
    pyperclip.copy(sys_info.toJSON())

def openFileCallBack():
    path = filedialog.askopenfilename(title = "Select a file")
    if path is None:
        return
    path_text.set(path)
    logging.info("File selected: "+str(path))
    stat = os.stat(path)
    size_text.set(status.st_size)
    status_text.set("ok")

def exportSystemInfoCallBack():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".json", filetypes=(("JSON file", "*.json"),("All Files", "*.*") ))
    if f is None:
        return
    logging.info("File selected")
    f.write(sys_info.toJSON())
    f.close()

if not args.basic:
    logging.info("Full GUI")
    notebook = ttk.Notebook(window)
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text='System info')
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text='Read file info')
    tab3 = ttk.Frame(notebook)
    notebook.add(tab3, text='List directory')
    notebook.pack(expand=1, fill="both")
    ttk.Label(tab1, text="Executed by").grid(column=0, row=0, padx=4)
    ttk.Label(tab1, text=sys_info.executed_by).grid(column=1, row=0, padx=10)
    ttk.Label(tab1, text="Platform").grid(column=0, row=1)
    ttk.Label(tab1, text=sys_info.platform_all).grid(column=1, row=1)
    ttk.Label(tab1, text="OS System").grid(column=0, row=2)
    ttk.Label(tab1, text=sys_info.os_system+" "+sys_info.os_release).grid(column=1, row=2)
    ttk.Label(tab1, text="Linux distro").grid(column=0, row=3)
    ttk.Label(tab1, text=sys_info.linux_distro).grid(column=1, row=3)
    ttk.Label(tab1, text="MacOS version").grid(column=0, row=4)
    ttk.Label(tab1, text=sys_info.mac_ver).grid(column=1, row=4)
    ttk.Label(tab1, text="win32 version").grid(column=0, row=5)
    ttk.Label(tab1, text=sys_info.win32_ver).grid(column=1, row=5)
    ttk.Label(tab1, text="Machine").grid(column=0, row=6)
    ttk.Label(tab1, text=sys_info.machine).grid(column=1, row=6)
    ttk.Label(tab1, text="uname").grid(column=0, row=7)
    ttk.Label(tab1, text=sys_info.uname, wraplength=800).grid(column=1, row=7)
    ttk.Label(tab1, text="System version").grid(column=0, row=8)
    ttk.Label(tab1, text=sys_info.sys_version).grid(column=1, row=8)
    ttk.Button(tab1, text="Copy system info", command=copySystemInfoCallBack).grid(column=0, row=9)
    ttk.Button(tab1, text="Export system info to file", command=exportSystemInfoCallBack).grid(column=0, row=10)
    
    ttk.Button(tab2, text="Open file", command=openFileCallBack).grid(column=0, row=0, rowspan=1)
    ttk.Label(tab2, text="File path").grid(column=0, row=1, padx=4)
    path_text = tk.StringVar().set("N/A")
    ttk.Label(tab2, textvariable=path_text).grid(column=1, row=1, padx=10)
    ttk.Label(tab2, text="File size").grid(column=0, row=2)
    size_text = tk.StringVar().set("N/A")
    ttk.Label(tab2, textvariable=size_text).grid(column=1, row=2)
    ttk.Label(tab2, text="Status").grid(column=0, row=3)
    status_text = tk.StringVar().set("N/A")
    ttk.Label(tab2, textvariable=status_text).grid(column=1, row=3)

    ttk.Label(tab3, text="TODO").grid()
else:
    logging.info("Basic GUI")
logging.debug("tk mainloop")
window.mainloop()
logging.debug("tk window closed")