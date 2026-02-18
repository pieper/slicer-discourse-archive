# How can I run a python script on slicer?

**Topic ID**: 25527
**Date**: 2022-10-03
**URL**: https://discourse.slicer.org/t/how-can-i-run-a-python-script-on-slicer/25527

---

## Post #1 by @MarcoSaguatti (2022-10-03 13:02 UTC)

<p>Operating system: Windows 11 pro<br>
Slicer version: 5.0.3</p>
<p>Hi,<br>
I’m trying to run a simple python scripts that loads a patient on Slicer.<br>
If I run the code line by line in the python interactor all goes as espected.<br>
Instead, if I try to run a script that contains the same lines of code using C:\Users\Marco\Slicer-5.0.3\Slicer.exe --python-script “C:\Users\Marco\Desktop\tirocinio\scripting_3DSlicer\Dice_Hausdorff.py” nothing happens.<br>
What am I doing wrong?<br>
Thank you for the support.</p>

---

## Post #2 by @rbumm (2022-10-03 15:21 UTC)

<p>You could run</p>
<pre><code class="lang-auto">exec(open(r"C:\Users\Marco\Desktop\tirocinio\scripting_3DSlicer\Dice_Hausdorff.py").read())
</code></pre>
<p>from the Python Interactor.</p>

---
