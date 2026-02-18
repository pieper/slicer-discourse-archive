# How to capture the return/output of a python script executed from slicer's python interpreter

**Topic ID**: 7395
**Date**: 2019-07-03
**URL**: https://discourse.slicer.org/t/how-to-capture-the-return-output-of-a-python-script-executed-from-slicers-python-interpreter/7395

---

## Post #1 by @talmazov (2019-07-03 15:23 UTC)

<p>Hey,<br>
I am trying to develop a script that is independent of slicer’s main execution process. I want to launch this python script using the built-in python interpreter (this way the user does not need to have an independent python installation), perform a task, then return the data back to the slicer python extension that executed it. From the Script Repository and Launcher Wikis I saw there is the option to start a script this way:</p>
<blockquote>
<p>Slicer.exe --python-script “[path to script]\myScript.py --script_argument” --testing --no-splash --no-main-window</p>
</blockquote>
<p>I can pass some data to myScript.py via setting up command argument input like you do in the terminal but what would be the best way to capture the return data once this script has completed execution?<br>
Essentially I just want to use the supplied python interpreter Slicer comes with to run python script then return the data back to the extension for further processing.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2019-07-04 19:25 UTC)

<p>This is what Python CLI modules are developed for. If you have a Python script that you can launch from the command-line, then you can launch it from Slicer, too. But it gets much better: you get a nice GUI so that users that are not familiar with the command line can use the module, and Slicer can launch the processing in the background and automatically writes input nodes to files and reads outputs from files when the processing is completed.</p>
<p>All you need to do is to create an XML file that describes the input and output arguments of your Python script.</p>
<p>See a complete example and explanation here: <a href="https://github.com/lassoan/SlicerPythonCLIExample" rel="nofollow noopener">https://github.com/lassoan/SlicerPythonCLIExample</a></p>
<p>A bit more complicated example, showing how to parse more complicated command lines and add automatic testing: <a href="https://github.com/SlicerDMRI/SlicerDMRI/tree/master/Modules/CLI/ExtractDWIShells" rel="nofollow noopener">https://github.com/SlicerDMRI/SlicerDMRI/tree/master/Modules/CLI/ExtractDWIShells</a></p>

---
