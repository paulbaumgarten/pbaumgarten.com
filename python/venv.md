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

### Using Github Desktop + VS Code

1 - Create or clone your repository

2 - Use the Git Ignore template for Python (to ignore venv by default) 

3 - Enter a terminal and create a virtual environment

* Github desktop menu: Repository / Open in terminal

```bash
python -m venv venv                 # Create venv
source venv/bin/activate            # Activate the virtual environment
pip install -r requirements.txt     # Install requirements into it
exit                                # Exit the virtual envionment
```

Build your project!

* Just ensure VS Code is using the correct Python interpreter (bottom-left corner in the blue bar)

### Mac terminal

```bash
cd thematrix                        # Change into your project folder
python3 -m venv venv                # Create a virtual environment (venv)
source venv/bin/activate            # Activate the virtual environment
which python                        # Confirm virtual environment
pip3 install -r requirements.txt    # Install your packages
python3 main.py                     # Test your project
deactivate                          # Deactivate venv
```

### Windows DOS command line

```bash
cd thematrix                        # Change into your project folder
python -m venv venv                 # Create a virtual environment (venv)
source venv/bin/activate            # Activate the virtual environment
which python                        # Confirm virtual environment
pip install -r requirements.txt     # Install your packages
python main.py                      # Test your project
deactivate                          # Deactivate the virtual environment
```

### IDLE

```bash
python -m venv venv                 # Create a virtual environment (venv) in the folder venv
source venv/bin/activate            # Activate the virtual environment
python -m idlelib.idle              # Launch IDLE via the Python module
deactivate                          # Deactivate the virtual environment when finished
```

### PyCharm

* File / settings / project interpreter
