# Slicer fails to start after adding a scripted module

**Topic ID**: 6807
**Date**: 2019-05-15
**URL**: https://discourse.slicer.org/t/slicer-fails-to-start-after-adding-a-scripted-module/6807

---

## Post #1 by @batuhan_edguer (2019-05-15 20:02 UTC)

<p>Hello I’m getting this error, tried to reinstall but it did not…</p>
<p>Traceback (most recent call last):<br>
File “D:\Program Files\Slicer 4.10.1\bin\Python\slicer\ScriptedLoadableModule.py”, line 202, in onReloadAndTest<br>
self.onReload()<br>
File “D:\Program Files\Slicer 4.10.1\bin\Python\slicer\ScriptedLoadableModule.py”, line 195, in onReload<br>
slicer.util.reloadScriptedModule(self.moduleName)<br>
File “D:\Program Files\Slicer 4.10.1\bin\Python\slicer\util.py”, line 623, in reloadScriptedModule<br>
moduleName, fp, filePath, (’.py’, ‘r’, imp.PY_SOURCE))<br>
UnicodeEncodeError: ‘ascii’ codec can’t encode character u’\xf6’ in position 31: ordinal not in range(128)<br>
Reload and Test: Exception!</p>
<p>‘ascii’ codec can’t encode character u’\xf6’ in position 31: ordinal not in range(128)</p>
<p>See Python Console for Stack Trace</p>

---

## Post #2 by @cpinter (2019-05-15 20:06 UTC)

<p>It would help if you described what you tried to do when you got this error.</p>
<p>Also if this was a crash then python errors probably won’t be conclusive, but a full log might help.</p>
<p>Thanks!</p>

---

## Post #3 by @batuhan_edguer (2019-05-15 20:08 UTC)

<p>I solved. I used the “ö” for folder name. The system does not recognize the “ö”.</p>

---
