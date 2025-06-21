import os
from dotenv import load_dotenv
import subprocess
import pwinput

load_dotenv()

username = os.getenv("USERNAME_bp")
password = os.getenv("PASSWORD_bp")
bp_software_folderpath = os.getenv("BP_Software_FolderPath")

# p = subprocess.Popen('echo Hello', stdout=subprocess.PIPE, text=True, shell=True)
# output, _ = p.communicate()
# print(output)

# username = input("Enter your username: ")
# password = pwinput.pwinput(prompt='Enter your password: ', mask='*')

"""
"C:\Program Files\Blue Prism Limited\Blue Prism Automate\AutomateC.exe" 
/exportpackage "All BluePrism Process and Objects"  /user username password
"""

def execute_command(cmd: str, working_dir: str = None):
    # p = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True, shell=True, cwd=working_dir)  # doesnt work for the export_ReleaseFromPackage, becoz of the console cursor position
    # p = subprocess.Popen(cmd, text=True, shell=True, cwd=working_dir)
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=working_dir)
    # output, _ = p.communicate()
    # return output


def import_processORobjects(file_name: str):
    cli_command = '\"' + bp_software_folderpath + '\" ' + "/import " + '\"'+ file_name + '\" ' + "/overwrite " + "/user " + username + " " + password
    return execute_command(cli_command)


def import_releaseORskills(file_name: str):
    cli_command = '\"' + bp_software_folderpath + '\" ' + "/importrelease " + '\"' +file_name+ '\" ' + "/overwrite " + "/user " + username + " " + password
    return execute_command( cli_command)


def export_processORobjects(process_Or_object_name: str):
    base_folder = "\Blue Prism\Process_Objects"
    cli_command = '\"' + bp_software_folderpath + '\" ' + "/export " + '\"' +process_Or_object_name+ '\" ' + "/user " + username + " " + password
    execute_command(cli_command, os.getcwd()+base_folder)


def export_ReleaseFromPackage(package_name: str):
    base_folder = "\Blue Prism\Package_Release\\"
    cli_command = '\"' + bp_software_folderpath + '\" ' + "/exportpackage " + '\"' + package_name + '\" ' + "/user " + username + " " + password
    execute_command(cli_command, os.getcwd() + base_folder)


print(export_processORobjects(r"python_scope_executions"))