# Linux system service guide

## Create your virtual environment

venv is a tool to create isolated Python environments. venv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

By default, every project on your system will use these same directories to store and retrieve site packages (third party libraries). At first glance, this may not seem like a big deal, and it isn’t really, for system packages (packages that are part of the standard Python library), but it does matter for site packages.

Consider the following scenario where you have two projects: ProjectA and ProjectB, both of which have a dependency on the same library, ProjectC. The problem becomes apparent when we start requiring different versions of ProjectC. Maybe ProjectA needs v1.0.0, while ProjectB requires the newer v2.0.0, for example.

This is a real problem for Python since it can’t differentiate between versions in the site-packages directory. So both v1.0.0 and v2.0.0 would reside in the same directory with the same name:

/System/Library/Frameworks/Python.framework/Versions/3.5/Extras/lib/python/ProjectC
Since projects are stored according to just their name, there is no differentiation between versions. Thus, both projects, ProjectA and ProjectB, would be required to use the same version, which is unacceptable in many cases.

This is where virtual environments and the virtualenv/venv tools come into play.

Create your virtual environment through the following console commands. This is for an example project called *thematrix*, replace all references to the fake name with your actual project name.

```bash
# Change into your project folder
cd thematrix

# Create your virtual environment
# Runs the venv package to create a folder venv
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

# Deactivate the virtual environment
deactivate
```

## Create the system service

```bash
# Create a systemd service configuration
sudo vi /etc/systemd/system/thematrix.service
```

Example content of the .service file. Use the *Environment* command to add any other environment settings you want for the project (such as paths to API keys etc)

```text
[Unit]
Description=The matrix project
After=network.target

[Service]
User=pbaumgarten
WorkingDirectory=/projects/thematrix
Environment="PATH=/projects/thematrix/venv/bin"
Environment="PYTHONPATH=/projects/thematrix"
ExecStart=/projects/thematrix/venv/bin/python main.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Finally, enable and start the service

```bash
# Enable the service
sudo systemctl enable thematrix

# Start the service
sudo systemctl start thematrix

# Check status of service
sudo systemctl status thematrix.service

# Show logs for the service
journalctl -u thematrix
```

