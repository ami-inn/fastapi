FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.

The key features are:

Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
Fast to code: Increase the speed to develop features by about 200% to 300%. *
Fewer bugs: Reduce about 40% of human (developer) induced errors. *
Intuitive: Great editor support. Completion everywhere. Less time debugging.
Easy: Designed to be easy to use and learn. Less time reading docs.
Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
Robust: Get production-ready code. With automatic interactive documentation.
Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

pydantic - used for data validation and settings management using Python type annotations


start command
python3 -m venv .venv
to activate . .venv/bin/activate
to deactivate deactivate
git ignore echo ".venv/" >> .gitignore
cat .gitignore to verify
pip install --upgrade pip 
pip install "fastapi[standard]" 
pip freeze > requirements.txt for dependencies

<!-- explain what are it from start command -->
python3 -m venv .venv means to create a virtual environment named .venv for the project. A virtual environment is an isolated Python environment that allows you to manage dependencies for your project without affecting the global Python installation.
to activate . .venv/bin/activate is the command to activate the virtual environment you just created. Once activated, any Python packages you install will be contained within this environment.
git ignore echo ".venv/" >> .gitignore is a command to add the .venv/ directory to the .gitignore file. This prevents the virtual environment from being tracked by Git
pip install --upgrade pip is used to upgrade the pip package manager to the latest version within the virtual environment.
pip install "fastapi[standard]" installs the FastAPI framework along with its standard dependencies.
pip freeze > requirements.txt is a command that generates a requirements.txt file listing all the installed packages and their versions in the virtual environment. This file can be used to recreate the same environment later.


Select the virtual environment in VS Code:

Press Ctrl+Shift+P
Type "Python: Select Interpreter"
Look for and select: .venv (Python 3.12.x) or the path python
If you don't see the .venv interpreter in the list:

Manually enter the interpreter path:

Press Ctrl+Shift+P
Type "Python: Select Interpreter"
Click "Enter interpreter path..."
Enter: python
Then reload VS Code:

Press Ctrl+Shift+P
Type "Developer: Reload Window"
After reloading, the import error should disappear. You can verify the correct interpreter is selected by checking the bottom-right corner of VS Code - it should show .venv or Python 3.12.x ('.venv').

path /home/ami/Desktop/findingso/fastapi/fast-api/omnicopy/.venv/bin/python


to start 
fastapi dev main.py to start the server
fast api generate autodocs at /docs 


