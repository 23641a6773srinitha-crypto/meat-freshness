# Mini Project: Machine Learning Experiments

This repository contains a collection of machine learning experiments and a Tkinter desktop application for classifying Iris flowers. It also includes notebook work for meat-freshness image classification, related datasets, generated model files, and early-stage Python scripts.

## Projects in this Repository

### 1. Iris Flower Classification (Tkinter)

The completed desktop application is in `TKINTER/Step10Main.py`. It provides a graphical workflow for:

- Uploading a CSV dataset
- Removing missing values
- Encoding categorical columns
- Splitting data into training and test sets
- Training and comparing:
  - Random Forest Classifier
  - Extra Trees Classifier
- Displaying accuracy, precision, recall, F1 score, sensitivity, specificity, classification reports, and confusion matrices
- Comparing classifier performance in a bar chart
- Predicting the species of rows in a new CSV file

The application uses `TKINTER/Dataset/Iris.csv` as the training dataset and `TKINTER/Dataset/test.csv` for prediction.

### 2. Meat-Freshness Image Classification

The notebooks and image folders contain experiments for classifying meat images as fresh or spoiled. The main image dataset is stored in `Meat freshness/`, with separate folders for freshness categories. Supporting notebooks include:

- `Day2.ipynb`
- `day3.ipynb`
- `Day4.ipynb`
- `ML_image_VAMSHI.ipynb`
- `ML_Image_Vamshi_New.ipynb`

The notebooks are used for image loading, preprocessing, feature extraction/classification experiments, model training, and model saving.

## Repository Structure

```text
mini project/
|-- TKINTER/
|   |-- Step10Main.py          # Main completed Iris Tkinter application
|   |-- Step1.py ... step9.py  # Incremental application development files
|   |-- Dataset/
|   |   |-- Iris.csv           # Training dataset
|   |   `-- test.csv          # Prediction dataset
|   |-- model/
|   |   |-- RFC_model.pkl      # Random Forest model
|   |   `-- ETC_model.pkl      # Extra Trees model
|   `-- run.bat                # Optional environment helper
|-- Meat freshness/
|   |-- FRESH/                 # Fresh-meat images
|   `-- [other category folders]
|-- model/                     # Additional saved machine-learning models
|-- Day2.ipynb
|-- day3.ipynb
|-- Day4.ipynb
|-- ML_image_VAMSHI.ipynb
|-- ML_Image_Vamshi_New.ipynb
|-- Day4.py
|-- liver.csv
|-- read.md
`-- requirement.txt
```

Folder and file names shown above may vary depending on the downloaded dataset and completed notebook steps.

## Requirements

### Software

- Windows 10 or 11
- Python 3.10 or 3.11
- A desktop environment with Tkinter support
- Jupyter Notebook or JupyterLab
- 4 GB RAM or more (8 GB recommended for image experiments)
- Enough free disk space for image datasets and saved model files

### Python Packages

Install all listed packages with:

```powershell
py -m pip install --upgrade pip
py -m pip install -r requirement.txt
```

The required packages include:

- NumPy
- pandas
- Matplotlib
- Seaborn
- scikit-learn
- OpenCV
- Joblib
- Jupyter Notebook
- IPython

Tkinter is included with standard Python installations on Windows. If it is missing, reinstall Python and enable the Tk/Tcl feature.

## Setup Instructions

### 1. Open the project

Open a terminal in this project directory:

```powershell
cd "C:\Users\Srinitha\OneDrive\Desktop\mini project"
```

### 2. Create a virtual environment

```powershell
py -3.11 -m venv .venv
```

If Python 3.11 is unavailable, use:

```powershell
py -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks the activation script, allow it for the current process:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

Alternative Command Prompt activation:

```bat
.venv\Scripts\activate.bat
```

### 4. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirement.txt
```

## Run the Iris Tkinter Application

From the project root:

```powershell
cd TKINTER
python Step10Main.py
```

Keep the terminal in the `TKINTER` directory because the application initializes model storage relative to the current directory:

- Training models are saved in `TKINTER/model/RFC_model.pkl`
- Training models are saved in `TKINTER/model/ETC_model.pkl`

### Using the Application

1. Click **Dataset** and select `Dataset/Iris.csv`.
2. Click **Preprocessing**.
3. Click **Train Test Splitting**.
4. Click **Existing Classifier** to train or load the Random Forest model.
5. Click **Proposed Classifier** to train or load the Extra Trees model.
6. Click **Prediction** and select `Dataset/test.csv`.
7. Click **Comparison Graph** after both classifiers have been run.
8. Click **Exit** to close the application.

## Run the Jupyter Notebooks

Start Jupyter from the project root:

```powershell
jupyter notebook
```

Or:

```powershell
jupyter lab
```

Open a notebook and select the `.venv` Python kernel if it is available. Update hard-coded dataset or image paths in notebook cells before running them when the project is moved to another machine.

## Dataset Details

### Iris Dataset

The included `Iris.csv` file has the following columns:

- `Id`
- `SepalLengthCm`
- `SepalWidthCm`
- `PetalLengthCm`
- `PetalWidthCm`
- `Species`

The target column is `Species`. It contains the categories:

- `Iris-setosa`
- `Iris-versicolor`
- `Iris-virginica`

The `test.csv` file contains the feature columns but no target column, and is intended for prediction.

### Image Dataset

The image dataset is organized into category folders under `Meat freshness/`. Image paths used in notebooks may need to be adjusted to match the local project location.

## Model Files

Saved models use the `.pkl` format and are loaded with Joblib. The main Tkinter application loads existing models when available and trains them if missing.

Do not reuse a model for prediction data with different feature names or column order unless the preprocessing and feature layout are identical.

## Common Problems

### `ModuleNotFoundError`

Make sure the virtual environment is activated and dependencies are installed:

```powershell
python -m pip install -r requirement.txt
```

### Tkinter Window Does Not Open

- Confirm that the script is run with Python 3.
- Reinstall Python with the Tk/Tcl installation option.
- On Windows, run `python Step10Main.py` instead of a shell launch that opens a Python launcher.

### OpenCV or Notebook Import Errors

Restart the notebook kernel after installation and verify that the kernel uses the same environment:

```powershell
python -m pip install ipykernel
python -m ipykernel install --user --name mini-project
```

### Dataset or Image Path Errors

Run scripts from the directories described in this README. For notebooks, convert absolute paths to paths relative to the notebook or update the path manually.

### Matplotlib Windows Do Not Close

Close the open plot window before continuing. The Tkinter application displays separate Matplotlib windows for graphs and confusion matrices.

## Notes

- Generated model files may be architecture-, Python-, and scikit-learn-version-sensitive.
- Re-train models when dependencies or the input dataset change significantly.
- The `.ipynb_checkpoints` folders contain automatic notebook checkpoint copies.
- Keep original datasets and model files backed up before retraining or regenerating them.
- The saved models should be used as experimental outputs and should not be treated as medically or food-safety-authoritative predictions.
