---
topic_id: 24955
title: "Fail To Import Matlab Engine From Python Script"
date: 2022-08-28
url: https://discourse.slicer.org/t/24955
---

# Fail to import matlab.engine from python script

**Topic ID**: 24955
**Date**: 2022-08-28
**URL**: https://discourse.slicer.org/t/fail-to-import-matlab-engine-from-python-script/24955

---

## Post #1 by @wpgao (2022-08-28 01:08 UTC)

<p>Hi Guy,</p>
<p>Recently, I try to call matlab R2022a in 3D Slicer 5.1.0, but failed!<br>
when “import matlab.engine”, 3D Slicer crashed.<br>
The problem may occur in line 8 in the file “enginesession.py” in the matlabengine for python packages, when calling pythonengine.createProcess().</p>
<p>However, it works in PythonSlicer script.</p>
<p>Any advices are welcome!</p>
<p>Thanks !</p>

---

## Post #2 by @lassoan (2022-08-28 11:19 UTC)

<p>Matlab engine may use different version of some shared libraries than those in Slicer’s Python environment, therefore you may need to put the script that relies on Matlab into a separate .py file and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#launch-external-process-in-startup-environment">launch it as an external process</a>.</p>
<p>You may also try to use Matlab engine from a Python CLI module - see example <a href="https://github.com/lassoan/SlicerPythonCLIExample">here</a>.</p>

---

## Post #3 by @wpgao (2022-08-29 02:23 UTC)

<p>It’s a good suggestion. However, Matlab (R2019) engine can be imported successfully in Slicer ( version 4.11 ). There  must be changes in Slicer v5. Is there any difference between PythonSlicer and the python integrated in Slicer?<br>
Thanks!</p>

---

## Post #4 by @lassoan (2022-08-29 03:01 UTC)

<p>We upgraded Python version and several libraries. Maybe previously we accidentally used the same shared library versions, but now they are conflicting.</p>

---

## Post #5 by @wpgao (2022-08-29 04:16 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="24955">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>rsion and s</p>
</blockquote>
</aside>
<p>One problem of using CLI is that if the size of the volume data is very large, it will take a long time for data exchange between CLI and Slicer. For example, Slicer should save the data into a temporary file and CLI will read the data from the temporary file, after the CLI execution, CLI had to save the result into a temporary file and Slicer had to read it from the temporary file. Anyway, there is no other options.</p>

---

## Post #6 by @lassoan (2022-08-29 04:45 UTC)

<p>If you don’t compress the volume then writing to disk and reading from disk should take negligible time. If you have enough memory then most likely the file will be transferred via memory, so disk speed should not even matter.</p>
<p>You may also reconsider using Matlab. Licensing hassles, difficulty of debugging a closed-source software, complications with distributing your final software might not worth the trouble of using Matlab. You can probably find free, open-source Python modules that can do the same as the proprietary Matlab functions.</p>

---
