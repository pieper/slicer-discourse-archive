# nameError when using slicer.util.pip_install

**Topic ID**: 30160
**Date**: 2023-06-20
**URL**: https://discourse.slicer.org/t/nameerror-when-using-slicer-util-pip-install/30160

---

## Post #1 by @Justin_Kirby (2023-06-20 16:53 UTC)

<p>Hi, I’m working on the TCIABrowser extension.  Part of the code relies on a PyPI package called tcia_utils.  The code we used to load it worked fine in the 5.2 stable release, but in the 5.3 preview releases this is failing.  Did something change about how we should be doing things or is this a bug related to slicer.util?</p>
<p>slicer.util.pip_install(‘tcia_utils’)<br>
NameError: name ‘slicer’ is not defined</p>
<p>Here’s the full traceback:</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\neoma\Downloads\TCIABrowser-master\TCIABrowser\TCIABrowserLib\TCIAClient.py”, line 2, in <br>
import tcia_utils.nbia<br>
ModuleNotFoundError: No module named ‘tcia_utils’</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\neoma\AppData\Local\slicer.org\Slicer 5.3.0-2023-06-19\lib\Python\Lib\imp.py”, line 169, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 613, in _exec<br>
File “”, line 850, in exec_module<br>
File “”, line 228, in _call_with_frames_removed<br>
File “C:/Users/neoma/Downloads/TCIABrowser-master/TCIABrowser/TCIABrowser.py”, line 23, in <br>
from TCIABrowserLib import APISettingsPopup, clinicalDataPopup, TCIAClient<br>
File “C:\Users\neoma\Downloads\TCIABrowser-master\TCIABrowser\TCIABrowserLib\TCIAClient.py”, line 4, in <br>
slicer.util.pip_install(‘tcia_utils’)<br>
NameError: name ‘slicer’ is not defined</p>

---

## Post #2 by @lassoan (2023-06-20 16:54 UTC)

<blockquote>
<p>slicer.util.pip_install(‘tcia_utils’)<br>
NameError: name ‘slicer’ is not defined</p>
</blockquote>
<p>Calling <code>import slicer</code> before <code>slicer.util....</code> should fix the problem.</p>

---

## Post #3 by @Justin_Kirby (2023-06-20 17:06 UTC)

<p>Yikes…how did I miss that? <img src="https://emoji.discourse-cdn.com/twitter/laughing.png?v=12" title=":laughing:" class="emoji" alt=":laughing:" loading="lazy" width="20" height="20">  Thanks.</p>

---
