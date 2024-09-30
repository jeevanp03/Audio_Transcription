# Audio Transcription

This repository contains utility functions to assist with transcribing audio recordings. The audio recordings are interviews conducted as part of the MSE 343 Human-Computer Interaction (HCI) project.

## Table of Contents

- [Audio Transcription](#audio-transcription)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Virtual Environment Setup](#virtual-environment-setup)
    - [Creating a Virtual Environment](#creating-a-virtual-environment)
    - [Activating the Virtual Environment](#activating-the-virtual-environment)
    - [Installing Dependencies](#installing-dependencies)
    - [Deactivating the Virtual Environment](#deactivating-the-virtual-environment)
  - [Managing Dependencies with `requirements.txt`](#managing-dependencies-with-requirementstxt)
    - [Creating a `requirements.txt` File](#creating-a-requirementstxt-file)
    - [Installing from `requirements.txt`](#installing-from-requirementstxt)

## Prerequisites

- Python 3.x installed on your machine
- Basic knowledge of command-line operations

## Virtual Environment Setup

Using a virtual environment is recommended to manage project-specific dependencies and avoid conflicts with other Python projects.

### Creating a Virtual Environment

1. **Navigate to the project directory**:

   ```bash
   cd path/to/Audio_Transcription
   ```

2. **Create the virtual environment**:

   ```bash
   python3 -m venv .venv
   ```

   - This command creates a folder named `.venv` in your project directory.
   - The `.venv` folder contains a standalone Python installation along with its own `pip`.

### Activating the Virtual Environment

- **On Windows**:

  ```bash
  .venv\Scripts\activate
  ```

- **On macOS/Linux**:

  ```bash
  source .venv/bin/activate
  ```

  - After activation, your command prompt will be prefixed with `(.venv)` to indicate that the virtual environment is active.

### Installing Dependencies

With the virtual environment activated, you can now install project dependencies.

- **If you have a `requirements.txt` file**:

  ```bash
  pip install -r requirements.txt
  ```

- **To install packages individually** (e.g., `numpy`, `pandas`):

  ```bash
  pip install package_name
  ```

### Deactivating the Virtual Environment

When you're done working on the project, deactivate the virtual environment:

```bash
deactivate
```

- This returns you to your system's default Python interpreter.

## Managing Dependencies with `requirements.txt`

A `requirements.txt` file lists all the Python packages needed to run the project, along with their versions.

### Creating a `requirements.txt` File

1. **Ensure all necessary packages are installed** in your virtual environment.

2. **Generate the `requirements.txt` file**:

   ```bash
   pip freeze > requirements.txt
   ```

   - This command writes all the installed packages and their versions to `requirements.txt`.

### Installing from `requirements.txt`

To install all the dependencies listed in `requirements.txt`:

1. **Activate the virtual environment** (if not already active).

2. **Run the installation command**:

   ```bash
   pip install -r requirements.txt
   ```

   - This installs all packages specified in the file, ensuring a consistent environment across different setups.

---

Feel free to contribute to this project by submitting issues or pull requests. For any questions or suggestions, please contact the repository maintainer.
