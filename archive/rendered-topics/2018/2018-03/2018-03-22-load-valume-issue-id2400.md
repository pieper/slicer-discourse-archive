---
topic_id: 2400
title: "Load Valume Issue"
date: 2018-03-22
url: https://discourse.slicer.org/t/2400
---

# Load valume issue

**Topic ID**: 2400
**Date**: 2018-03-22
**URL**: https://discourse.slicer.org/t/load-valume-issue/2400

---

## Post #1 by @anandmulay3 (2018-03-22 13:33 UTC)

<p>i’m trying to load volume in python scriptable module script</p>
<p>code :[success, loadedVolumeNode] = slicer.util.loadVolume(path, returnNode=True)</p>
<p>error :</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:/Anand Work/PythonInterfacer.py”, line 9, in <br>
[success, loadedVolumeNode] = slicer.util.loadVolume(path, returnNode=True)<br>
File “C:\Program Files\Slicer 4.8.1\bin\Python\slicer\util.py”, line 377, in loadVolume<br>
return loadNodeFromFile(filename, filetype, properties, returnNode)<br>
File “C:\Program Files\Slicer 4.8.1\bin\Python\slicer\util.py”, line 306, in loadNodeFromFile<br>
success = app.coreIOManager().loadNodes(filetype, properties)<br>
ValueError: Could not find matching overload for given arguments:<br>
(‘VolumeFile’, {‘fileName’: ‘C:\Anand Work\Sft.nrrd’})<br>
The following slots are available:<br>
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters, vtkCollection loadedNodes) -&gt; bool<br>
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters) -&gt; bool<br>
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters, vtkCollection loadedNodes) -&gt; bool<br>
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters) -&gt; bool</p>

---

## Post #2 by @lassoan (2018-03-24 04:59 UTC)

<p>Most likely the problem is that your path contains special characters (<code>\A</code> and <code>\S</code>, note that <code>\</code> is an escape character). You can use any of these syntaxes instead:</p>
<ul>
<li>
<code>r‘C:\Anand Work\Sft.nrrd’</code> =&gt; <code>r</code> prefix specifies raw string, <code>\</code> is not interpreted as escape character in these strings</li>
<li>
<code>‘C:\\Anand Work\\Sft.nrrd’</code> =&gt; double backslash encodes backslash</li>
<li>
<code>‘C:/Anand Work/Sft.nrrd’</code> =&gt; forward slashes can be use instead of backslashes</li>
</ul>

---
