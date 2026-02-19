---
topic_id: 43256
title: "Crashing Of 3Dslicer Version 5 8 1 After Importing Opengate"
date: 2025-06-07
url: https://discourse.slicer.org/t/43256
---

# Crashing of 3DSlicer version 5.8.1 after importing openGate Python package

**Topic ID**: 43256
**Date**: 2025-06-07
**URL**: https://discourse.slicer.org/t/crashing-of-3dslicer-version-5-8-1-after-importing-opengate-python-package/43256

---

## Post #1 by @shahrokh (2025-06-07 11:47 UTC)

<p>Hello Dear Developers and Users</p>
<p>I installed the <a href="https://opengate-python.readthedocs.io/en/master/user_guide/index.html" rel="noopener nofollow ugc">opengate</a> library in python of 3DSlicer. But after importing it in python interactor and pressing the <em>menu key</em> or pressing the <em>tab key</em> for completing the names of imported libraries, on keyword, suddenly 3DSlicer crash and close, and I see below message in terminal.</p>
<pre><code class="lang-auto">sn@mph:~$ /home/sn/Slicer-5.8.1-linux-amd64/Slicer 
Switch to module:  "Welcome"
Python console user input: import opengate
nativeResourceForScreen: null screen
nativeResourceForScreen: null screen
Cannot create window: no screens available
error: [/home/sn/Slicer-5.8.1-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.
sn@mph:~$ 
</code></pre>
<p>Please guide me to solve it.<br>
Best regards.<br>
Shahrokh.</p>

---

## Post #2 by @lassoan (2025-06-07 13:28 UTC)

<p>Pressing “Tab” key evaluates all attributes available in that module (to determine if they are callable functions and so parenthesis should be added after the name). If <code>opengate</code> is not implemented robustly then these evaluations cause a crash, which brings down the Slicer application.</p>
<p>I would recommend to find which exact attribute is implemented inappropriately by running this code in the Slicer Python console and then report that problem to opengate developers:</p>
<pre data-code-wrap="python"><code class="lang-python">moduleName = 'opengate'
attributeNames = dir(moduleName)
for attributeName in attributeNames:
    print(f"{attributeName}:")
    print(f"    value: {getattr(moduleName, attributeName)}")
    print(f"    callable: {callable(getattr(moduleName, attributeName))}")
</code></pre>

---

## Post #3 by @shahrokh (2025-06-08 04:12 UTC)

<p>Thank you very much for your guidance.</p>

---
