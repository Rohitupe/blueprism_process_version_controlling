
# Blue Prism CLI GUI Manager

This project provides a simple Python-based GUI and CLI wrapper for managing Blue Prism processes, objects, and releases using Blue Prism's command-line interface (CLI). It allows you to import/export processes, objects, and releases via a user-friendly Tkinter interface or directly through Python functions.

## Features

- **Import Process/Object**: Import a Blue Prism process or object file.
- **Import Release/Skill**: Import a Blue Prism release or skill file.
- **Export Process/Object**: Export a Blue Prism process or object to a specified folder.
- **Export Package/Release**: Export a Blue Prism release package to a specified folder.
- **GUI Interface**: Simple Tkinter-based GUI for easy operation.
- **Environment Variable Support**: Securely store Blue Prism credentials and paths in a `.env` file.

## Requirements

- Python 3.11+
- python-dotenv==1.1.0

## Setup

1. **Clone / Download the Repository**

   ```sh
   git clone <your-repo-url>
   cd blueprism_github_release_manager
   ```

2. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

3. **Create a `.env` File**

   In the project root, create a `.env` file with the following content (replace with your actual values):

   ```
   USERNAME_bp=your_blueprism_username
   PASSWORD_bp=your_blueprism_password
   BP_Software_FolderPath=C:\Program Files\Blue Prism Limited\Blue Prism Automate\AutomateC.exe
   ```

4. **Ensure Blue Prism Folders Exist**

   The following folders should exist in your project directory:
   - `Blue Prism\Process_Objects`
   - `Blue Prism\Package_Release`

   If not, create them to avoid errors during import/export.

## Usage

### 1. GUI Application

Run the Tkinter GUI:

```sh
python UiTkinter.py
```

- **Select Action**: Choose from Import/Export Process or Release/Package.
- **Enter Name**: Provide the process/object or release/skill name for Importing use the same name as it is there in the blueprism process / object, same goes for export.
- **Execute**: Click "Execute" to run the selected action.

The GUI will display the result of the operation in a popup.

### 2. CLI/Python Functions

You can also use the functions in `BP_CLI.py` directly in your own scripts:

## Troubleshooting
- **Permissions**: Ensure you have write permissions to the target folders

## More Information

For detailed information on Blue Prism command-line options, see the official documentation:  
[Blue Prism Command Line Help](https://docs.blueprism.com/en-US/bundle/blue-prism-enterprise-7-4/page/helpCommandLine.htm)

---