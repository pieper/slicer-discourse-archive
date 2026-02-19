---
topic_id: 18321
title: "Import Issue Of Vmtk Libraries"
date: 2021-06-24
url: https://discourse.slicer.org/t/18321
---

# Import issue of vmtk libraries

**Topic ID**: 18321
**Date**: 2021-06-24
**URL**: https://discourse.slicer.org/t/import-issue-of-vmtk-libraries/18321

---

## Post #1 by @Bastien_Saunois (2021-06-24 12:39 UTC)

<p>I am trying to re-use the ExtractCenterline.py code.</p>
<p>In the script there are 2 imports that interest me :</p>
<ul>
<li>
<pre><code>      import vtkvmtkComputationalGeometryPython as vtkvmtkComputationalGeometry
</code></pre>
</li>
<li>
<pre><code>      import vtkvmtkMiscPython as vtkvmtkMisc
</code></pre>
</li>
</ul>
<p>I found the two libraries in the extension folder of vmtkSlicer with a .pyd extension and copied them in my folder project.</p>
<p>Unfortunately, when I launch my python script importing this libraries, it fails to import those.<br>
Those anyone know how to use this libraries and how to import them?</p>
<p>Bastien</p>

---

## Post #2 by @lassoan (2021-06-24 12:55 UTC)

<p>What Python environment do you use for your project?</p>

---

## Post #3 by @Bastien_Saunois (2021-06-24 12:59 UTC)

<p>I am using the anaconda environment with Python 3.8.</p>

---

## Post #4 by @Bastien_Saunois (2021-06-25 15:26 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I downgraded my version of Python to 3.6 in order to meet the installation of vmtk but I am still not able to import the libraries.</p>
<p>I get the following error :</p>
<p>Traceback (most recent call last):<br>
File “test.py”, line 16, in <br>
import vtkvmtkMiscPython as vtkvmtkMisc<br>
ImportError: DLL load failed: The specified module could not be found.</p>
<p>I am stuck, I don’t understand why it can’t access to the library…</p>

---

## Post #5 by @lassoan (2021-06-25 15:56 UTC)

<p>You probably need to add the folder that contains the DLLs to you PYTHONPATH environment variable. Also make sure that all other DLLs that VMTK DLLs depend on (such as entire VTK) are available on the path. You can use Dependency Walker to find out what DLLs you need.</p>

---

## Post #6 by @Bastien_Saunois (2021-06-28 08:45 UTC)

<p>Thanks a lot, it worked, I didn’t know about Dependency Walker, it is a very useful tool !</p>

---
