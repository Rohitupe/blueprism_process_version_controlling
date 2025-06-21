import os
from dotenv import load_dotenv
import subprocess

load_dotenv()

username = os.getenv("USERNAME_bp")
password = os.getenv("PASSWORD_bp")
bp_software_folderpath = os.getenv("BP_Software_FolderPath")

# p = subprocess.Popen('echo Hello', stdout=subprocess.PIPE, text=True, shell=True)
# output, _ = p.communicate()
# print(output)


def execute_command(cmd: str, working_dir: str = None):
    # p = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True, shell=True, cwd=working_dir)  # doesnt work for the export_ReleaseFromPackage, becoz of the console cursor position
    p = subprocess.Popen(cmd, text=True, shell=True, cwd=working_dir)
    output, _ = p.communicate()
    return output


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
    return execute_command(cli_command, os.getcwd() + base_folder)


# print(import_releaseORskills(r"C:\Users\rohit\Desktop\blueprism_github_release_manager\Blue Prism\Package_Release\All BluePrism Process and Objects - Release 1.bprelease"))