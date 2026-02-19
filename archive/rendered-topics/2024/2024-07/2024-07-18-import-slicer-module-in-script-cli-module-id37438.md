---
topic_id: 37438
title: "Import Slicer Module In Script Cli Module"
date: 2024-07-18
url: https://discourse.slicer.org/t/37438
---

# Import slicer module in script cli module

**Topic ID**: 37438
**Date**: 2024-07-18
**URL**: https://discourse.slicer.org/t/import-slicer-module-in-script-cli-module/37438

---

## Post #1 by @fqzhice (2024-07-18 02:43 UTC)

<p>I create a script cli module and call this script as below：</p>
<pre><code class="lang-auto">PythonQt::init();
PythonQtObjectPtr context = PythonQt::self()-&gt;getMainModule();

QString cmd = QString(
    "import os\n"
    "import sys\n"
    "CTASegExePath=slicer.app.slicerHome + '/CTAModule/lib/VesselCenterline.py'\n"
    "pythonSlicerExecutablePath=os.path.dirname(sys.executable)+'/PythonSlicer.exe'\n"
    "commandLine = [pythonSlicerExecutablePath, CTASegExePath]\n"
    "proc=slicer.util.launchConsoleProcess( commandLine ,useStartupEnvironment=True)\n"
    "slicer.util.logProcessOutput(proc)\n"
);  
context.evalScript(cmd);
</code></pre>
<p>in VesselCenterline.py scirpt</p>
<p>I cant import slicer module and call slicer python API, it says no module named “xxx”</p>
<p>How can i do about this ?</p>

---
