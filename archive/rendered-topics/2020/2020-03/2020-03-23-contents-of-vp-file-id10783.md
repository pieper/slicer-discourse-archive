---
topic_id: 10783
title: "Contents Of Vp File"
date: 2020-03-23
url: https://discourse.slicer.org/t/10783
---

# Contents of .VP File

**Topic ID**: 10783
**Date**: 2020-03-23
**URL**: https://discourse.slicer.org/t/contents-of-vp-file/10783

---

## Post #1 by @bernland (2020-03-23 08:00 UTC)

<p>I created a MIP in Slicer, the contents of the .VP file are as follows:</p>
<pre><code>1: 1
2: 0
3: 1
4: 0.2
5: 0
6: 1
7: 8 -94 0 4.37255859375 0 322.636962890625 1 2706 1
8: 4 -94 1 161 1
9: 16 -94 0 0 1 4.37255859375 0 0 1 322.636962890625 0 0 1 2706 0 0 1
</code></pre>
<p>I would now like to use the exact same MIP settings in plain <strong>Pyhon</strong>, however, I can’t seem to be able to achieve the same results. I was able to extract Scalar Opacity Mapping from line 7 and Scalar Color Mapping from line 9:</p>
<p><strong>Scalar Opacity Mapping</strong></p>
<pre><code>self.opacityTransferFunction.AddPoint(-94.0, 0.0)
self.opacityTransferFunction.AddPoint(4.37, 0.0)
self.opacityTransferFunction.AddPoint(322.64, 1)
self.opacityTransferFunction.AddPoint(2706.0, 1)
</code></pre>
<p><strong>Scalar Color Mapping</strong></p>
<pre><code>self.colorTransferFunction.AddRGBPoint(-94.0, 0.0, 0.0, 1.0)
self.colorTransferFunction.AddRGBPoint(4.37, 0.0, 0.0, 1.0)
self.colorTransferFunction.AddRGBPoint(322.64, 0.0, 0.0, 1.0)
self.colorTransferFunction.AddRGBPoint(2706.0, 0.0, 0.0, 1.0)
</code></pre>
<p>What’s encoded in the other lines and is there any piece of (Python) code that reads in a .VP file and applies its settings?</p>

---

## Post #2 by @lassoan (2020-03-23 13:40 UTC)

<p>Format of volume property file is available here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/VolumeRendering#Format_of_Volume_Property_.28.vp.29_file">https://www.slicer.org/wiki/Documentation/Nightly/Modules/VolumeRendering#Format_of_Volume_Property_.28.vp.29_file</a></p>
<p>Since the file format is simple text file with fixed number of rows and space-separated values in each row, its parsing does not require any special technique.</p>
<p>In Slicer’s Python environment you may use vtkMRMLVolumePropertyStorageNode to read/write the text file content to/from a vtkMRMLVolumePropertyNode or use convenience functions in slicer.util:</p>
<pre><code class="lang-python"># read node from file
volumeProp = slicer.util.loadNodeFromFile(filename, 'TransferFunctionFile')
# write node to file
slicer.util.saveNode(volumeProp, filename)
</code></pre>

---
