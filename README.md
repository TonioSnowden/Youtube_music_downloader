# Project Name

Brief description of your project.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have [Anaconda](https://www.anaconda.com/products/individual) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed on your system to manage environments and dependencies.

### Setting Up the Environment

1. **Clone the Repository**

    First, clone the repository to your local machine using Git:

    ```
    git clone https://github.com/yourusername/yourprojectname.git
    cd yourprojectname
    ```

2. **Create the Conda Environment**

    Create a new Conda environment with the required libraries:

    ```bash
    conda create --name myenv python=3.8 pandas requests
    ```

    This will install Python and the `pandas` and `requests` libraries, which are necessary for the project.

3. **Activate the Environment**

    Activate the newly created Conda environment:

    ```bash
    conda activate myenv
    ```

4. **Additional Dependencies**

    Although most dependencies are installed with the environment, ensure you have a web browser installed on your system as the script utilizes `webbrowser`, a built-in Python library.

### Preparing the Links File

Create a file named `links.xlsx` in the project's root directory. The file should contain a list of YouTube links you wish to download, each in a new row in the first column of the spreadsheet.

### Running the Script

With the environment set up and activated, and the `links.xlsx` file prepared, you are now ready to run the script:

```bash
python download_music.py
```

### Contribution

Me and only me
