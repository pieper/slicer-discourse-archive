---
topic_id: 43415
title: "Opening Alpaca For The First Time And Stuck On Installing Al"
date: 2025-06-18
url: https://discourse.slicer.org/t/43415
---

# Opening ALPACA for the first time and stuck on "Installing ALPACA Python Packages...."

**Topic ID**: 43415
**Date**: 2025-06-18
**URL**: https://discourse.slicer.org/t/opening-alpaca-for-the-first-time-and-stuck-on-installing-alpaca-python-packages/43415

---

## Post #1 by @jsguerra (2025-06-18 19:13 UTC)

<p>I recently upgraded my SSD and re-installed Slicermorph and the ALPACA extension. I went ahead and tried to open ALPACA for the first time since the new install and I seem to be stuck in the “Installing ALPACA Python Packages. This may take a minute..” pop-up for about 10 minutes (before writing this).</p>
<p>When I look at the Python console, the following output is in red letters:<br>
In the future <code>np.bool</code> will be defined as the corresponding NumPy scalar.<br>
Traceback (most recent call last):<br>
File “C:/Users/JSG/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/ALPACA.py”, line 126, in setup<br>
import itk<br>
File “C:\Users\JSG\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\itk_<em>init</em>_.py”, line 59, in <br>
from itk.support.extras import *<br>
File “C:\Users\JSG\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\itk\support\extras.py”, line 37, in <br>
import itk.support.types as itkt<br>
File “C:\Users\JSG\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\itk\support\types.py”, line 178, in <br>
) = itkCType.initialize_c_types_once()<br>
File “C:\Users\JSG\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\itk\support\types.py”, line 143, in initialize_c_types_once<br>
<em>B: “itkCType” = itkCType(“bool”, “B”, np.dtype(np.bool))<br>
File "C:\Users\JSG\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\numpy_<em>init</em></em>.py", line 353, in <strong>getattr</strong><br>
raise AttributeError(<strong>former_attrs</strong>[attr])<br>
AttributeError: module ‘numpy’ has no attribute ‘bool’.<br>
<code>np.bool</code> was a deprecated alias for the builtin <code>bool</code>. To avoid this error in existing code, use <code>bool</code> by itself. Doing this will not modify any behavior and is safe. If you specifically wanted the numpy scalar type, use <code>np.bool_</code> here.<br>
The aliases was originally deprecated in NumPy 1.20; for more details and guidance see the original release note at:<br>
<a href="https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations" class="inline-onebox" rel="noopener nofollow ugc">NumPy 1.20.0 Release Notes — NumPy v2.4.dev0 Manual</a></p>
<p>Any help would be greatly appreciated!</p>

---

## Post #2 by @muratmaga (2025-06-18 19:46 UTC)

<p>Thanks for reporting. I can reproduce this in a fresh install. Opened an issue <a href="https://github.com/SlicerMorph/SlicerMorph/issues/402" class="inline-onebox" rel="noopener nofollow ugc">ALPACA failing to install on 5.8.1 on windows due to ITK error · Issue #402 · SlicerMorph/SlicerMorph · GitHub</a> you can track its update.</p>

---

## Post #3 by @muratmaga (2025-06-19 16:06 UTC)

<p><a class="mention" href="/u/jsguerra">@jsguerra</a> If you are tracking the github issue, until the fix is integrated, the workaround is to manually install the numpy. These steps worked for me:</p>
<ol>
<li>in Python console type `pip_install(“numpy==2.00”)’</li>
<li>Restart Slicer</li>
<li>Switch to ALPACA</li>
</ol>
<p>It should continue installing remaining packages (pandas) and then ALPACA should be working.</p>

---

## Post #4 by @jsguerra (2025-06-19 16:37 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Yes, I was literally just looking through the github issue! I’ll try your instructions, thank you!</p>

---
