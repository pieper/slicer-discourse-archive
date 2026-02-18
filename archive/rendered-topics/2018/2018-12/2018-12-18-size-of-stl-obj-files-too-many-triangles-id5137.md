# Size of STL/OBJ files - too many triangles

**Topic ID**: 5137
**Date**: 2018-12-18
**URL**: https://discourse.slicer.org/t/size-of-stl-obj-files-too-many-triangles/5137

---

## Post #1 by @sarvpriya1985 (2018-12-18 22:58 UTC)

<p>Operating system: windows 10<br>
Slicer version:4. 10<br>
Expected behavior:<br>
Actual behavior:<br>
Hi everyone,<br>
Is there a way to compress the size of 3D models before exporting them as STL or OBJ format. Sometimes these are about 100 MBs and its difficult to put them in presentations.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #2 by @cpinter (2018-12-18 23:33 UTC)

<p>There are two ways:</p>
<ul>
<li>Changes segmentation conversion parameter to enable decimation: Go to Segmentations module, long-click the Create button for Closed surface, select Advanced create or Update (depending on whether you had surfaces already or not). In the popup window choose the only path, and set a non-zero Decimation factor. 0.8 means that 80% of the triangles will be removed. Then export segmentation to STL</li>
<li>Export segmentation to Model node (in Segmentations module bottom section or in Data module by right-clicking the segmentation). Then go to the Surface Toolbox module and do decimation on the model.</li>
</ul>

---

## Post #3 by @lassoan (2018-12-19 03:46 UTC)

<p>2 posts were split to a new topic: <a href="/t/publishing-segmentations-on-the-web-sketchfab/5140">Publishing segmentations on the web (sketchfab)</a></p>

---

## Post #4 by @Coloradoultrasound (2019-11-12 05:22 UTC)

<p>I really appreciate you taking the time to share this with me. I tried to follow your instructions but maybe I’m missing some options in the Mac version. I see the tool and understand what you are talking about. My issue is that once I have a volume in the segment editor I don’t see that option for the segment. I am working with 3-D ultrasound images and GE files. Cartesian volume.</p>

---
