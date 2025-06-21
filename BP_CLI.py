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
    """
        To Execute CLI command using Subprocess module
    """
    try:
        # p = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True, shell=True, cwd=working_dir)  # doesnt work for the export_ReleaseFromPackage, becoz of the console cursor position
        p = subprocess.Popen(cmd, text=True, shell=True, cwd=working_dir)
        output, _ = p.communicate()
        return output
    except Exception as e:
        return "Error : " + e

def import_processORobjects(process_or_object_filename: str):
    """ Import Process or Objects in Blue Prism """
    base_folder = "\Blue Prism\Process_Objects"
    cli_command = f'"{bp_software_folderpath}" /import "{process_or_object_filename}" /overwrite /user {username} {password}'
    return execute_command(cli_command, os.getcwd()+base_folder)


def import_releaseORskills(release_or_skill_name: str):
    """ Import Release or Skills in Blue Prism """
    base_folder = "\Blue Prism\Package_Release"
    cli_command = f'"{bp_software_folderpath}" /importrelease "{release_or_skill_name}" /overwrite /user {username} {password}'
    return execute_command(cli_command, os.getcwd()+base_folder)


def export_processORobjects(process_Or_object_name: str):
    """ Export Process or Objects from Blue Prism to the specified folder location """
    base_folder = "\Blue Prism\Process_Objects"
    cli_command = f'"{bp_software_folderpath}" /export "{process_Or_object_name}" /user {username} {password}'
    execute_command(cli_command, os.getcwd()+base_folder)


def export_ReleaseFromPackage(package_name: str):
    """ Export Package Release from Blue Prism Release Tab to the Specified folder location, for this the Package should be created in the blueprism """
    base_folder = "\Blue Prism\Package_Release"
    cli_command = f'"{bp_software_folderpath}" /exportpackage "{package_name}" /user {username} {password}'
    return execute_command(cli_command, os.getcwd() + base_folder)


print(export_ReleaseFromPackage(r"All BluePrism Process and Objects"))