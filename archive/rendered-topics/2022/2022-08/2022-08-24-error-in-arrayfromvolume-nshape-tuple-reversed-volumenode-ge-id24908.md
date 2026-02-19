---
topic_id: 24908
title: "Error In Arrayfromvolume Nshape Tuple Reversed Volumenode Ge"
date: 2022-08-24
url: https://discourse.slicer.org/t/24908
---

# Error: in arrayFromVolume nshape = tuple(reversed(volumeNode.GetImageData().GetDimensions())) AttributeError: 'NoneType' object has no attribute 'GetDimensions'

**Topic ID**: 24908
**Date**: 2022-08-24
**URL**: https://discourse.slicer.org/t/error-in-arrayfromvolume-nshape-tuple-reversed-volumenode-getimagedata-getdimensions-attributeerror-nonetype-object-has-no-attribute-getdimensions/24908

---

## Post #1 by @leeyrics (2022-08-24 14:50 UTC)

<p>Hello everyone and expert</p>
<p>slicer 4.11.20210226</p>
<p>I wanna get the coordinates and HU data from my segment. i wrote a script to use python. but there is a problem. it occurs an Error: <em>Traceback (most recent call last):</em></p>
<ul>
<li>File “”, line 1, in *</li>
<li>File “D:\3D\Slicer 4.11.20210226\bin\Python\slicer\util.py”, line 1439, in arrayFromVolume*</li>
<li>nshape = tuple(reversed(volumeNode.GetImageData().GetDimensions()))*<br>
<em>AttributeError: ‘NoneType’ object has no attribute ‘GetDimensions’</em>
</li>
</ul>
<p>i found out all the forum and didnt get an answer about it. could u help me? Thanks a lot in advance!</p>
<p>my script:</p>
<pre><code class="lang-auto">segmentationNode =slicer.mrmlScene.GetNodeByID("kortikalis")
masterVolumeNode = slicer.util.getNode("8: Schulter li.   3.0 sag - imageType DERIVED-PRIMARY-AXIAL-CT_SOM5 SPO")

labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")

slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode,labelmapVolumeNode,masterVolumeNode)



volumeArray = slicer.util.arrayFromVolume(masterVolumeNode)

labelArray = slicer.util.arrayFromVolume(labelmapVolumeNode)

labelValue = slicer.mrmlScene.GetNodeByID('LabelMapVolume')

segmentVoxels = volumeArray[labelArray==labelValue]



import numpy as np

coordinates = np.where(labelArray==labelValue)

hu = volumeArray[coordinates]



coordinateWithHU = np.zeros([len(coordinates[0]),4])

coordinateWithHU[:,0:3] = np.array(coordinates).T

coordinateWithHU[:,3] = hu

slicer.util.pip_install('pandas')

import pandas as pd

pd.DataFrame(coordinateWithHU).to_csv("c:/tmp/coordshu.csv")
</code></pre>
<p><img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji only-emoji" alt=":grinning:" loading="lazy" width="20" height="20"></p>

---

## Post #3 by @lassoan (2022-09-19 07:39 UTC)

<p>The error indicates that the chosen volume is empty (no image data is set). Probably you did not select the correct volume.</p>
<p>Please use the latest Slicer Stable Release. Lots of improvements and fixes have been implemented in the past 1.5 years - maybe one of them will help finding the root cause of the issue more easily.</p>

---
