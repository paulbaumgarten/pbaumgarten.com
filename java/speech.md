# Java text to speech

To be honest, probably the easiest way to do this is to execute a command line tool via Java.

## To execute command line from Java in Windows

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class PowerShellCommand {

    public static void main(String[] args) throws IOException {

    //String command = "powershell.exe  your command";

    //Getting the version
    String command = "powershell.exe  $PSVersionTable.PSVersion";

    // Executing the command
    Process powerShellProcess = Runtime.getRuntime().exec(command);

    // Getting the results
    powerShellProcess.getOutputStream().close();
    String line;
    System.out.println("Standard Output:");
    BufferedReader stdout = new BufferedReader(new InputStreamReader(
        powerShellProcess.getInputStream()));
    while ((line = stdout.readLine()) != null) {
        System.out.println(line);
    }
    stdout.close();
    System.out.println("Standard Error:");
    BufferedReader stderr = new BufferedReader(new InputStreamReader(
        powerShellProcess.getErrorStream()));
    while ((line = stderr.readLine()) != null) {
        System.out.println(line);
    }
    stderr.close();
    System.out.println("Done");
    }
}
```

source: https://stackoverflow.com/a/29545926

## Command lines to generate speech

on Win using PowerShell.exe

```shell
PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('hello');"
```

on Win using mshta.exe

```shell
mshta vbscript:Execute("CreateObject(""SAPI.SpVoice"").Speak(""Hello"")(window.close)")
```

on OSX using say

```bash
say "hello"
```

on any other Linux

refer to How to text-to-speech output using command-line?

on Raspberry Pi, Win, OSX using Node-Red

```bash
npm i node-red-contrib-sysmessage
```

source: https://stackoverflow.com/a/39647762

