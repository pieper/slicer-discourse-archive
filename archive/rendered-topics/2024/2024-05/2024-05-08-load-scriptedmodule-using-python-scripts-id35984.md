# Load ScriptedModule using python scripts

**Topic ID**: 35984
**Date**: 2024-05-08
**URL**: https://discourse.slicer.org/t/load-scriptedmodule-using-python-scripts/35984

---

## Post #1 by @park (2024-05-08 07:26 UTC)

<p>Hi all,</p>
<p>For security reasons, we want to place our module on a web server and use web APIs to read it when Slicer is opened. This way, we can identify who called the module and execute it without downloading the source code to the local computer.</p>
<hr>
<p>We are attempting a simple test implementation for this by trying to load the scripted module using Python programming (etc console).</p>
<p>After examining the C++ source code, it seems like <code>imp.load_source</code> is being used, but attempting it in the console doesn’t seem to work well. Can we get some insights on this?</p>
<p>Specifically, when apply <code>imp.load_source('MyModule', 'Path\MyModule.py')</code>, the  <code>MyModuleLibs</code> was not integrated in the <code>load_source</code> process.</p>

---
