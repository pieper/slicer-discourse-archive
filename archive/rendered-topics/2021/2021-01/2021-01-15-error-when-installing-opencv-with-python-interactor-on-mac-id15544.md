---
topic_id: 15544
title: "Error When Installing Opencv With Python Interactor On Mac"
date: 2021-01-15
url: https://discourse.slicer.org/t/15544
---

# Error when installing opencv with Python Interactor on mac

**Topic ID**: 15544
**Date**: 2021-01-15
**URL**: https://discourse.slicer.org/t/error-when-installing-opencv-with-python-interactor-on-mac/15544

---

## Post #1 by @HodaGH (2021-01-15 20:54 UTC)

<p>Hi everyone,</p>
<p>I have MacOS 10.14. I’m trying to install opencv in the python interactor by this code:</p>
<p>from slicer.util import pip_install<br>
pip_install(“opencv”)</p>
<p>I get this error:</p>
<p>ERROR: Could not find a version that satisfies the requirement opencv (from versions: none)<br>
ERROR: No matching distribution found for opencv<br>
WARNING: You are using pip version 20.1.1; however, version 20.3.3 is available.<br>
You should consider upgrading via the ‘/Applications/Slicer.app/Contents/bin/./python-real -m pip install --upgrade pip’ command.<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 2569, in pip_install<br>
_executePythonModule(‘pip’, args)<br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 2545, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 2517, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[’/Applications/Slicer.app/Contents/bin/…/bin/PythonSlicer’, ‘-m’, ‘pip’, ‘install’, ‘opencv’]’ returned non-zero exit status 1.</p>
<p>Also regarding the Warning that I get for the update for pip when I open the python real, it is not editable to be able to put this code:</p>
<p>/Applications/Slicer.app/Contents/bin/./python-real -m pip install --upgrade pip</p>
<p>Thanks for your help.</p>

---

## Post #2 by @adamrankin (2021-01-15 21:02 UTC)

<p>This doesn’t exactly answer your question, but you could install the SlicerOpenCV extension, which will install opencv and python bindings.</p>

---

## Post #3 by @HodaGH (2021-01-15 21:42 UTC)

<p>I searched for SlicerOpenCV in the slicer extensions but I couldn’t find it.</p>

---

## Post #4 by @jamesobutler (2021-01-15 22:08 UTC)

<p>I believe the correct name to use to pip install OpenCV is “opencv-python”. So in Slicer it would be <code>slicer.util.pip_install("opencv-python")</code> instead of <code>slicer.util.pip_install("opencv")</code> as you tried.</p>
<p>See <a href="https://pypi.org/project/opencv-python/" class="inline-onebox" rel="noopener nofollow ugc">opencv-python · PyPI</a></p>

---
