# Start a project in python 

1. Generate python sandbox (virtual environment). The . is the folder for dependencies
```
python3 -m venv .
```
2. Activate the virtual environment (linux is source command)
```
source bin/activate 
```
3. Install the dependencies inside the virtual environment (-r recursive)
```
pip install -r requirements.txt
```
4. For lock the dependencies inside the file
```
pip freeze > requirements.txt
```


