# Model/Markups Coordinate systems

**Topic ID**: 43691
**Date**: 2025-07-11
**URL**: https://discourse.slicer.org/t/model-markups-coordinate-systems/43691

---

## Post #1 by @Ryan_Jones (2025-07-11 21:44 UTC)

<p>I have a model, that I am exporting from 3D slicer by right clicking the model and exporting to file- selecting stl. There is no option to choose coordinate system. I also have a list of closed curves that I want to output as .fcsv point list to send to SpaceClaim. But when I load the stl, and point cloud, they are no longer in the same coordinate system. What can I do to ensure that they are aligned correctly?</p>

---

## Post #2 by @muratmaga (2025-07-11 22:11 UTC)

<aside class="quote no-group" data-username="Ryan_Jones" data-post="1" data-topic="43691">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/ryan_jones/48/78229_2.png" class="avatar"> Ryan_Jones:</div>
<blockquote>
<p>But when I load the stl, and point cloud, they are no longer in the same coordinate system.</p>
</blockquote>
</aside>
<p>All models and markups are written as left handed coordinate system in the Slicer. I am not sure what coordinate system SpaceClaim uses or assumes with the data. I assume when you mean they no longer in the same coordinate system, markups doesn’t overlap with model? If so, you can try changing the signs the first two coordinates of the markups in your fcsv file and see that helps.</p>

---

## Post #3 by @lassoan (2025-07-12 14:41 UTC)

<p>Slicer saves all data (markups, models, images, transforms, etc.) in LPS coordinate system by default. For compatibility with legacy software that uses RAS coordinate system, Slicer can also save in RAS, and it adds this information to the STL file header. However, if you edit the STL file in some software and that software removes the coordinate system information from the header, then Slicer will interpret the file as LPS by default, while the coordinates were actually in RAS. When you load such file, choose to use RAS in the additional options section of the “Add data” window:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/170d65bd4b8d68995dc169245a9fdbdf69c0a6d9.png" data-download-href="/uploads/short-url/3hVGvFSjsh1GFTy3HPBKW4dvtiN.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/170d65bd4b8d68995dc169245a9fdbdf69c0a6d9_2_690x137.png" alt="image" data-base62-sha1="3hVGvFSjsh1GFTy3HPBKW4dvtiN" width="690" height="137" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/170d65bd4b8d68995dc169245a9fdbdf69c0a6d9_2_690x137.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/170d65bd4b8d68995dc169245a9fdbdf69c0a6d9_2_1035x205.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/170d65bd4b8d68995dc169245a9fdbdf69c0a6d9_2_1380x274.png 2x" data-dominant-color="F5F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1802×358 26.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>By default, the file will be saved in the same coordinate system. You can find out what it is by using this code snippet:</p>
<pre data-code-wrap="python"><code class="lang-python">modelNode = getNode('BasePiece')
storageNode = modelNode.GetStorageNode()
print(slicer.vtkMRMLStorageNode.GetCoordinateSystemTypeAsString(storageNode.GetCoordinateSystem()))
</code></pre>
<p>If RAS is printed as a result, I would recommend to switch to LPS (as that is assumed by default by most software):</p>
<pre data-code-wrap="python"><code class="lang-python">storageNode.SetCoordinateSystem(slicer.vtkMRMLStorageNode.GetCoordinateSystemTypeFromString("LPS"))
</code></pre>

---
