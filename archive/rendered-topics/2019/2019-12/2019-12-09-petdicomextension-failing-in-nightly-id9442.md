---
topic_id: 9442
title: "Petdicomextension Failing In Nightly"
date: 2019-12-09
url: https://discourse.slicer.org/t/9442
---

# PETDICOMExtension failing in nightly

**Topic ID**: 9442
**Date**: 2019-12-09
**URL**: https://discourse.slicer.org/t/petdicomextension-failing-in-nightly/9442

---

## Post #1 by @Alex_Vergara (2019-12-09 11:00 UTC)

<p>The <code>PETDICOMExtension</code> is failing in nightly with this error</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/Applications/Slicer.app/Contents/Extensions-28653/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules/DICOMPETSUVPlugin.py", line 7, in &lt;module&gt;
    import dicom
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/dicom.py", line 11, in &lt;module&gt;
    raise ImportError(msg)
ImportError: 
Pydicom via 'import dicom' has been removed in pydicom version 1.0.
Please install the `dicom` package to restore function of code relying
on pydicom 0.9.9 or earlier. E.g. `pip install dicom`.
Alternatively, most code can easily be converted to pydicom &gt; 1.0 by
changing import lines from 'import dicom' to 'import pydicom'.
See the Transition Guide at
https://pydicom.github.io/pydicom/stable/transition_to_pydicom1.html.

Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/Applications/Slicer.app/Contents/Extensions-28653/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules/DICOMRWVMPlugin.py", line 3, in &lt;module&gt;
    import dicom
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/dicom.py", line 11, in &lt;module&gt;
    raise ImportError(msg)
ImportError: 
Pydicom via 'import dicom' has been removed in pydicom version 1.0.
Please install the `dicom` package to restore function of code relying
on pydicom 0.9.9 or earlier. E.g. `pip install dicom`.
Alternatively, most code can easily be converted to pydicom &gt; 1.0 by
changing import lines from 'import dicom' to 'import pydicom'.
See the Transition Guide at
https://pydicom.github.io/pydicom/stable/transition_to_pydicom1.html.

Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/Applications/Slicer.app/Contents/Extensions-28653/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules/PETDicomExtensionSelfTest.py", line 3, in &lt;module&gt;
    import dicom
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/dicom.py", line 11, in &lt;module&gt;
    raise ImportError(msg)
ImportError: 
Pydicom via 'import dicom' has been removed in pydicom version 1.0.
Please install the `dicom` package to restore function of code relying
on pydicom 0.9.9 or earlier. E.g. `pip install dicom`.
Alternatively, most code can easily be converted to pydicom &gt; 1.0 by
changing import lines from 'import dicom' to 'import pydicom'.
See the Transition Guide at
https://pydicom.github.io/pydicom/stable/transition_to_pydicom1.html.
</code></pre>
<p>Obviously it is using an old pydicom module</p>

---

## Post #2 by @jamesobutler (2019-12-09 12:25 UTC)

<p>It appears you are using an old nightly (28653). Use the current nightly (28668) and reinstall the extension using the extension manager.</p>
<p>This specific issue was solved 7 days ago in <a href="https://github.com/QIICR/Slicer-PETDICOMExtension/commit/f715f85b06d79ec4d254253cfb9cfc046b2ee804" rel="nofollow noopener">https://github.com/QIICR/Slicer-PETDICOMExtension/commit/f715f85b06d79ec4d254253cfb9cfc046b2ee804</a>. Everything appears to have been solved as the current nightly tests are not showing this failure.</p>

---

## Post #3 by @Alex_Vergara (2019-12-09 13:38 UTC)

<p>Yes that was solved, thanks</p>

---
