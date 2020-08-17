from simpletestprogram.version import __version__
import argparse
import logging
import os
import sys
import json
import yaml
import platform
import PySimpleGUI as sg
import pyperclip

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

if args.version: # if script is callled with "-v" flag, print version and exit
    print("Version "+__version__)
    exit()

logging.basicConfig(level=args.log_level)
logging.info("Version "+__version__)

class simpleClass(): # a simple js-object like class
    def toJSON(self):
        return json.dumps(self, default=lambda i: i.__dict__)
    def toYAML(self):
        return yaml.dump(self, explicit_start=True, default_flow_style=False)

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

sys_info.win32_ver = platform.win32_ver() #for Windows version
if sys_info.win32_ver == ('', ('', '', ''), ''):
    sys_info.win32_ver = "N/A"

sys_info.machine = platform.machine()
sys_info.uname = platform.uname()
sys_info.sys_version = platform.version()

logging.info(sys_info.toJSON()) # log sysinfo as json

if not args.basic: # if script is called with "-b", execute only a base GUI
    logging.info("Full GUI")
    tab1_layout = [
        [sg.Text("Executed by"),sg.Text(sys_info.executed_by)],
        [sg.Text("Platform"),sg.Text(sys_info.platform_all)],
        [sg.Text("OS System"),sg.Text(sys_info.os_system+" release "+sys_info.os_release)],
        [sg.Text("Linux distro"),sg.Text(sys_info.linux_distro)],
        [sg.Text("MacOS version"),sg.Text(sys_info.mac_ver)],
        [sg.Text("win32 version"),sg.Text(sys_info.win32_ver)],
        [sg.Text("Machine"),sg.Text(sys_info.machine)],
        [sg.Text("uname"),sg.Text(sys_info.uname)],
        [sg.Text("System version"),sg.Text(sys_info.sys_version)],
        [sg.Button('Copy JSON to clipboard', key="sys_info_copy")]
    ]
    open_file = simpleClass()
    open_file.path=sg.Text("N/A", key='open_file.path', size=(60,1))
    open_file.size=sg.Text("N/A", key='open_file.size', size=(15,1))
    open_file.status=sg.Text("idle", size=(30,1))
    # an example pseudo-code
    # open_file = [
    #   path = sg.Text,
    #   size = sg.Text,
    #   status = sg.Text,
    #   stat = os.stat(path) see line 158
    # ]

    save_file = simpleClass()
    save_file.path=sg.Text("N/A", key='save_file.path', size=(60,1))
    save_file.size=sg.Text("N/A", key='save_file.size', size=(15,1))
    save_file.status=sg.Text("idle", size=(30,1))
    # an example pseudo-code
    # save_file = [
    #   path = sg.Text,
    #   size = sg.Text,
    #   status = sg.Text,
    #   file = file(path), see line 175
    #   stat = os.stat(path) see line 182
    # ]

    tab2_layout = [
        [sg.Text("Open file", justification='center', font=("Helvetica", 15))],
        [sg.In(key='open_file_input')],
        [sg.FileBrowse(target='open_file_input'), sg.OK(key="open_file_button")],
        [sg.Text("File path"),open_file.path],
        [sg.Text("File size"),open_file.size],
        [sg.Text("Status"),open_file.status],
        [sg.Text("Save file", justification='center', font=("Helvetica", 15))],
        [sg.In(key='save_file_input')],
        [sg.FileSaveAs(target='save_file_input'), sg.OK(key="save_file_button")],
        [sg.Text("File path"),save_file.path],
        [sg.Text("File size"),save_file.size],
        [sg.Text("Status"),save_file.status]
    ]
    tab3_layout = [
        [sg.Text('TODO')] #TODO: write tab3 layout
    ]
    layout = [
        [sg.Image(os.path.join(os.path.dirname(os.path.abspath(__file__)), "res", "pythonlogo.png"))],
        [sg.Text("Version "+__version__)],
        [sg.TabGroup([[
            sg.Tab('System info', tab1_layout),
            sg.Tab('Files and directories', tab2_layout),
            sg.Tab('Others', tab3_layout)
        ]])]
    ]
else:
    logging.info("Basic GUI")
    layout = [
        [sg.Image(os.path.join(os.path.dirname(os.path.abspath(__file__)), "res", "pythonlogo.png"))],
        [sg.Text("Version "+__version__)]
    ]

window = sg.Window('Simple Test Program', layout)
logging.debug("window initialized")

def main():
    while True:    
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            logging.debug("window closed")  
            break
        logging.debug(json.dumps(event))
        logging.debug(json.dumps(values))
        if values["open_file_input"] and event == "open_file_button":
            # for open_file, see line 102
            open_file.path(values["open_file_input"])
            open_file.status("opening file...")
            open_file.stat = os.stat(values["open_file_input"])
            open_file.size(open_file.stat.st_size)
            open_file.status("ok")
        if values["save_file_input"] and event == "save_file_button":
            # for open_file, see line 113
            save_file.path(values["save_file_input"])
            save_file.status("writing file...")
            logging.debug("ext: "+os.path.splitext(values["save_file_input"]))
            save_file.file = open(values["save_file_input"], "w")
            file_content = {
                ".json": sys_info.toJSON(),
                ".yaml": sys_info.toYAML()
            }
            # get file extension, then get (and write to file) the value for the file extension. If no file extension is specified, use default sys_info.toJSON()
            save_file.file.write(file_content.get(os.path.splitext(values["save_file_input"])[1], sys_info.toJSON()))
            save_file.file.close()
            save_file.stat = os.stat(values["save_file_input"])
            save_file.size(save_file.stat.st_size)
            save_file.status("ok")
        if event == "sys_info_copy":
            pyperclip.copy(sys_info.toJSON())
            sg.popup_notify("JSON copied successfully", fade_in_duration=100, display_duration_in_ms=4000)
    window.close()

if __name__ == '__main__':
    main()