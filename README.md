# Plate Buckling

This repository solves the plate buckling formula provided in Niu's "Airframe Stress Analysis and Sizing". Currently it only supports compressive loading and requires the user to find the buckling coefficient from the curves in the book. 

## Dependencies

- Install the following libraries from pip:
    - scipy
    - fastapi


## Usage:
### Web App
    - Execute the following command from a terminal: uvicorn main:app --host 0.0.0.0
        - In a browser, go to http://0.0.0.0:8000/
    - Fill out the inputs in the form and click "Calculate"
    - Type "ctrl + C" from the command line to quit the program