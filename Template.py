import os
from pathlib import Path

PROJECT_NAME="WinePrediction"
list_files=[
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/utilities/__init__.py",
    f"src/{PROJECT_NAME}/utilities/common.py",
    "research/research.ipynb",
    "params.yaml"
]
for filepath in list_files:
    filepath = Path(filepath)
    dir,filename = os.path.split(filepath)
    if dir!= "":
        os.makedirs(dir,exist_ok=True)
    if (not os.path.exists(filepath) ) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
