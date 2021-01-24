# Windows service

*To install Python as a Windows service in the background*

[source](https://stackoverflow.com/a/46450007/10971929)

---

The simplest way is to use the: NSSM - the Non-Sucking Service Manager. Just download and unzip to a location of your choosing. It's a self-contained utility, around 300KB (much less than installing the entire pywin32 suite just for this purpose) and no "installation" is needed. The zip contains a 64-bit and a 32-bit version of the utility. Either should work well on current systems (you can use the 32-bit version to manage services on 64-bit systems).

GUI approach

1 - install the python program as a service. Open a Win prompt as admin

```dos
c:\>nssm.exe install WinService
```

2 - On NSSM´s GUI console:

path: C:\Python27\Python27.exe

Startup directory: C:\Python27

Arguments: c:\WinService.py

3 - check the created services on services.msc

Scripting approach (no GUI)
This is handy if your service should be part of an automated, non-interactive procedure, that may be beyond your control, such as a batch or installer script. It is assumed that the commands are executed with administrative privileges.

For convenience the commands are described here by simply referring to the utility as nssm.exe. It is advisable, however, to refer to it more explicitly in scripting with its full path c:\path\to\nssm.exe, since it's a self-contained executable that may be located in a private path that the system is not aware of.

1. Install the service

You must specify a name for the service, the path to the proper Python executable, and the path to the script:

```dos
nssm.exe install ProjectService "c:\path\to\python.exe" "c:\path\to\project\app\main.py"
```

More explicitly:

```dos
nssm.exe install ProjectService 
nssm.exe set ProjectService Application "c:\path\to\python.exe"
nssm.exe set ProjectService AppParameters "c:\path\to\project\app\main.py"
```

Alternatively you may want your Python app to be started as a Python module. One easy approach is to tell nssm that it needs to change to the proper starting directory, as you would do yourself when launching from a command shell:

```dos
nssm.exe install ProjectService "c:\path\to\python.exe" "-m app.main"
nssm.exe set ProjectService AppDirectory "c:\path\to\project"
```

This approach works well with virtual environments and self-contained (embedded) Python installs. Just make sure to have properly resolved any path issues in those environments with the usual methods. nssm has a way to set environment variables (e.g. PYTHONPATH) if needed, and can also launch batch scripts.

2. To start the service

```dos
nssm.exe start ProjectService 
```

3. To stop the service

```dos
nssm.exe stop ProjectService
```

4. To remove the service, specify the confirm parameter to skip the interactive confirmation.

nssm.exe remove ProjectService confirm
