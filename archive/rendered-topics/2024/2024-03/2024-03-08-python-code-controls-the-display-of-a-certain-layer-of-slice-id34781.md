---
topic_id: 34781
title: "Python Code Controls The Display Of A Certain Layer Of Slice"
date: 2024-03-08
url: https://discourse.slicer.org/t/34781
---

# Python code controls the display of a certain layer of slices in the view

**Topic ID**: 34781
**Date**: 2024-03-08
**URL**: https://discourse.slicer.org/t/python-code-controls-the-display-of-a-certain-layer-of-slices-in-the-view/34781

---

## Post #1 by @petit223 (2024-03-08 15:05 UTC)

<p>In the development of the 3D Slicer plug-in, I want to automatically display the corresponding slice on the Green view based on the serial number of the magnetic resonance image entered by the user (I don’t care about the images on the Red and Yellow views)<br>
For example, I want to use python code to display the 0th magnetic resonance image in the view (I don’t know if this is the right description: coordinates_ijk[2]=0),<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bbae0c055b79f61cda6a1bec603159f681a4edb.png" data-download-href="/uploads/short-url/8woyoYGO9TtSWbxH7tQYFnrnqtl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bbae0c055b79f61cda6a1bec603159f681a4edb_2_690x215.png" alt="image" data-base62-sha1="8woyoYGO9TtSWbxH7tQYFnrnqtl" width="690" height="215" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bbae0c055b79f61cda6a1bec603159f681a4edb_2_690x215.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bbae0c055b79f61cda6a1bec603159f681a4edb_2_1035x322.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bbae0c055b79f61cda6a1bec603159f681a4edb_2_1380x430.png 2x" data-dominant-color="888784"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2864×894 229 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I already know</p>
<pre><code class="lang-auto">i2rasMatrix = vtk.vtkMatrix4x4()
volumeNode.GetIJKToRASMatrix(i2rasMatrix)
origin = volumeNode.GetOrigin()
spacing = volumeNode.GetSpacing()
</code></pre>
<p>and I can use</p>
<pre><code class="lang-auto">greenSliceNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSliceNodeGreen")
greenSliceNode.SetSliceOffset(rasCoordinates[2])
</code></pre>
<p>to control the position under Green view<br>
However, executing the SetSliceOffset function requires knowing the value of AR (AR: 38.1683mm in the picture) (Is this reasoning correct?)<br>
The obstacle I encountered was that I could not convert the number of magnetic resonance images and the value of AR.<br>
Just knowing the value of AR for image 0 is completely enough for me<br>
Thx!!!</p>

---
