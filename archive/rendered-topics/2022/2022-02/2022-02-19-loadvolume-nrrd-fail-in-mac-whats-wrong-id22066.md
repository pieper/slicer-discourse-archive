---
topic_id: 22066
title: "Loadvolume Nrrd Fail In Mac Whats Wrong"
date: 2022-02-19
url: https://discourse.slicer.org/t/22066
---

# Loadvolume nrrd Fail in mac, what's wrong?

**Topic ID**: 22066
**Date**: 2022-02-19
**URL**: https://discourse.slicer.org/t/loadvolume-nrrd-fail-in-mac-whats-wrong/22066

---

## Post #1 by @jumbojing (2022-02-19 12:16 UTC)

<p>Loadvolume .nrrd file failed in mac, what’s wrong?</p>
<pre><code class="lang-auto"> &gt;&gt;&gt; masterVolumeNode = slicer.util.loadVolume("/Users/liguimei/Documents/slicerTempt/pedicle-triangle-planner/testa/vertebra2stl/CT-chest.nrrd")


Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slice98.app/Contents/bin/Python/slicer/util.py", line 865, in loadVolume
    return loadNodeFromFile(filename, filetype, properties, returnNode)
  File "/Applications/Slice98.app/Contents/bin/Python/slicer/util.py", line 636, in loadNodeFromFile
    success = app.coreIOManager().loadNodes(filetype, properties, loadedNodesCollection)
ValueError: Could not find matching overload for given arguments:
('VolumeFile', {'fileName': '/Users/liguimei/Documents/slicerTempt/pedicle-triangle-planner/testa/vertebra2stl/CT-chest.nrrd'}, (vtkmodules.vtkCommonCore.vtkCollection)0x187e17f48)
 The following slots are available:
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters, vtkCollection loadedNodes, vtkMRMLMessageCollection userMessages) -&gt; bool
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters, vtkCollection loadedNodes) -&gt; bool
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters) -&gt; bool
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters, vtkCollection loadedNodes, vtkMRMLMessageCollection userMessages) -&gt; bool
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters, vtkCollection loadedNodes) -&gt; bool
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters) -&gt; bool
</code></pre>

---

## Post #2 by @lassoan (2022-02-19 14:13 UTC)

<p>This function should works well. What Slicer version did you use?</p>

---

## Post #3 by @jumbojing (2022-02-19 23:09 UTC)

<p>Slicer version is 4.13</p>

---

## Post #4 by @lassoan (2022-02-20 05:30 UTC)

<p>I could not reproduce this with the latest Slicer Preview Release on mac. Try the very latest version.</p>
<p>If the problem persists then you can try calling the <code>loadNodes</code> method directly as in the code snippet below and adjust the arguments to see which one caused trouble:</p>
<pre><code class="lang-python">loadedNodesCollection = vtk.vtkCollection()
slicer.app.ioManager().loadNodes('VolumeFile',{'fileName': '/Users/liguimei/Documents/slicerTempt/pedicle-triangle-planner/testa/vertebra2stl/CT-chest.nrrd'}, loadedNodesCollection)
</code></pre>

---
