# Building the Monopoly Application into an Executable

This guide provides step-by-step instructions on how to build the Monopoly application into a standalone executable file using PyInstaller.

## Prerequisites

Before you begin, ensure you have **Python 3** installed on your system. If you don't have it, download it from [python.org](https://python.org/).

## Step 1: Set Up a Virtual Environment

It is highly recommended to use a Python virtual environment to manage project dependencies. This isolates your project's packages from your global Python installation.

1.  **Create a virtual environment:**
    Open your terminal or command prompt in the root directory of this project and run:
    ```bash
    python3 -m venv venv
    ```
    This will create a `venv` folder in your project directory.

2.  **Activate the virtual environment:**
    *   On **Windows**:
        ```bash
        .\venv\Scripts\activate
        ```
    *   On **macOS and Linux**:
        ```bash
        source venv/bin/activate
        ```
    Your terminal prompt should now show `(venv)` at the beginning, indicating that the virtual environment is active.

## Step 2: Install Dependencies

With the virtual environment active, install the required Python packages. This includes the game's dependency, `pygame`, and the tool we'll use to create the executable, `pyinstaller`.

Run the following commands in your terminal:

```bash
# Install pygame from the requirements file
pip install -r requirements.txt

# Install PyInstaller
pip install pyinstaller
```

## Step 3: Run PyInstaller

PyInstaller analyzes your Python script and bundles it with all its dependencies into a single package. We will run a command from the root directory of the project to build the executable.

The command includes a few important options:
*   `--onefile`: Creates a single executable file.
*   `--windowed`: Prevents a console window from opening when the application runs.
*   `--name Monopoly`: Sets the name of the executable to "Monopoly".
*   `--add-data "src/assets:assets"`: This is a crucial step. It tells PyInstaller to copy the `src/assets` directory into the executable's temporary folder at runtime and make it available in a folder named `assets`. This ensures the game can find its images and resources.
*   `--paths src`: Adds the `src` directory to the Python path so that PyInstaller can find the game's modules, like `pplay`.

Open your terminal in the root directory of this project (with the virtual environment still active) and run the following command:

```bash
pyinstaller --onefile --windowed --name Monopoly --add-data "src/assets:assets" --paths src src/main.py
```

## Step 4: Locate the Executable

PyInstaller will create a few folders in your project's root directory (`build` and `dist`) and a `.spec` file.

Your standalone executable file will be located in the `dist` directory. The file will be named `Monopoly` (or `Monopoly.exe` on Windows). You can now run this file to play the game without needing to have Python or any dependencies installed.
