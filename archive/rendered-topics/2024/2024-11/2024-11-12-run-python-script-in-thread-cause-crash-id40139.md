---
topic_id: 40139
title: "Run Python Script In Thread Cause Crash"
date: 2024-11-12
url: https://discourse.slicer.org/t/40139
---

# Run python script in thread cause crash

**Topic ID**: 40139
**Date**: 2024-11-12
**URL**: https://discourse.slicer.org/t/run-python-script-in-thread-cause-crash/40139

---

## Post #1 by @fqzhice (2024-11-12 01:42 UTC)

<p>Hi<br>
I try to run heavy calculation  by qtimer<br>
cmd = “pythonSlicerExecutablePath=os.path.dirname(sys.executable)+‘/PythonSlicer.exe’\n”<br>
“commandLine = [pythonSlicerExecutablePath, script, ‘%1’]\n”<br>
“proc=slicer.util.launchConsoleProcess( commandLine ,useStartupEnvironment=True)\n”</p>
<p>…<br>
PythonQt::init();<br>
PythonQtObjectPtr context = PythonQt::self()-&gt;getMainModule();<br>
QTimer timer;<br>
timer.singleShot(0,this, <a>&amp;</a> {<br>
context.evalScript(cmd);<br>
});<br>
the  set a progressbar for main thread.<br>
but it cashed with PythonQt accession error</p>
<p>Any suggestion vill very appreciated</p>

---
