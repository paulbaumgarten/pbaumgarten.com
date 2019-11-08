# Virtual environments

venv is a tool to create isolated Python environments. venv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

By default, every project on your system will use these same directories to store and retrieve site packages (third party libraries). At first glance, this may not seem like a big deal, and it isn’t really, for system packages (packages that are part of the standard Python library), but it does matter for site packages.

Consider the following scenario where you have two projects: ProjectA and ProjectB, both of which have a dependency on the same library, ProjectC. The problem becomes apparent when we start requiring different versions of ProjectC. Maybe ProjectA needs v1.0.0, while ProjectB requires the newer v2.0.0, for example.

This is a real problem for Python since it can’t differentiate between versions in the site-packages directory. So both v1.0.0 and v2.0.0 would reside in the same directory with the same name...

```bash
/System/Library/Frameworks/Python.framework/Versions/3.5/Extras/lib/python/ProjectC
```

Since projects are stored according to just their name, there is no differentiation between versions. Thus, both projects, ProjectA and ProjectB, would be required to use the same version, which is unacceptable in many cases.

This is where virtual environments and the virtualenv/venv tools come into play.

Create your virtual environment through the following console commands. This is for an example project called *thematrix*, replace all references to the fake name with your actual project name.

## Suggested workflows

### Using Github + VS Code

1. Create or clone your repository

2. Enter a terminal and create a virtual environment

* Github desktop menu: Repository / Open in terminal
* Create the virtual environment

```bash
python -m venv venv
```

2. Create an `.ignore` file

* Ignore the `/venv` folder.

3. Create a `requirements.txt` file if required

```bash
pip freeze > requirements.txt
```

4. Install your packages

```bash
pip install -r requirements.txt
```

5. Build your project

* Just ensure VS Code is using the correct Python interpreter (bottom-left corner in the blue bar)

### Mac terminal

```bash
# Change into your project folder
cd thematrix

# Create a virtual environment (venv) in the folder venv
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Confirm virtual environment will run the local python
which python

# Install your packages
pip3 install -r requirements.txt
pip3 install package1 package2 package3...

# Test your project
python3 main.py 

# Deactivate the virtual environment when finished
deactivate
```

### Windows DOS command line

```bash
# Change into your project folder
cd thematrix

# Create a virtual environment (venv) in the folder venv
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Confirm virtual environment will run the local python
which python

# Install your packages
pip install -r requirements.txt
pip install package1 package2 package3...

# Test your project
python main.py 

# Deactivate the virtual environment when finished
deactivate
```

### IDLE

```bash
# Create a virtual environment (venv) in the folder venv
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Launch IDLE via the Python module
python -m idlelib.idle

# Deactivate the virtual environment when finished
deactivate
```

* Last step from [https://stackoverflow.com/a/38104835](https://stackoverflow.com/a/38104835)

### PyCharm

* File / settings / project interpreter
