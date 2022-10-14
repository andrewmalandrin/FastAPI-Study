# Food Facts
## By Andrew Malandrin

## Intro

Project created to practice Python with Fast API and some concepts of clean architecture mixed with DTO and dependencies injection.

## Instructions

Here goes the initial instructions to build the environment locally in your machine and use the food facts API and some important informations about the API.

### Observations

- The products data file is fullfilled with Brazillian products, to create a new dataset, maintain the first two rows of the file that have the headers and a blank line separating the data itself from the header.
- If you chose to erase the content and start a new data-set, we recomend you let another second blank line to start to put the data by the create product endpoint.

### First steps

First of all, fork the project or download it via git clone.

After downloading the project to your computer, you have to create a new virtual environment using Python.
Make sure you have python installed and PATH variables configured
Open the git bash on the project root folder and create the venv with the above command:

    python -m venv venv

After creating the venv, activate it with one of the bove commands:

Linux:
    
    source venv/bin/activate

Windows:
    
    With git bash
    source venv/scripts/activate

    With CMD or powershell
    /venv/scripts/activate.bat

Make sure that the virtual env is activated by looking on top of the folder location path, if it's already activated it will appear (venv) on top or left of the path.

After activating the venv, install the dependencies using the above command:

    pip install -r requirements.txt

From now on, you may be able to start the server

    uvicorn main:app --reload --port 80

Or if you are in linux or wsl

    sh uvicorn-start.sh

### Docs

To see the docs, access http://localhost/docs after starting the Uvicorn server

    