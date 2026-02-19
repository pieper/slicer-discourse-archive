---
topic_id: 1061
title: "Editor And Crop Volume Modules"
date: 2017-09-15
url: https://discourse.slicer.org/t/1061
---

# Editor and Crop Volume modules

**Topic ID**: 1061
**Date**: 2017-09-15
**URL**: https://discourse.slicer.org/t/editor-and-crop-volume-modules/1061

---

## Post #1 by @Researcher_2017 (2017-09-15 15:51 UTC)

<p>I am using 3D Slicer version 4.6.2 to convert MRI data into a 3D representation of a head. I have two questions -</p>
<ol>
<li>
<p>When I use the “Paint Effect” in the Editor Module to fill in empty spaces and then I use “Make Model Effect” to create a new model, I cannot undo changes in the previous model. Is there any solution to this?</p>
</li>
<li>
<p>Also, I am having issues using the Crop Volume module. I initially created an island around the head in the Editor module, which essentially built a cube around the head, and then applied that to create a new model. I am now trying to use the Crop Volume module to make the cube smaller and the program is not allowing me to do this.</p>
</li>
</ol>
<p>Any help would be appreciated. Thanks!</p>

---

## Post #2 by @lassoan (2017-09-15 16:03 UTC)

<p>It should all work well if you use latest nightly version of Slicer and the Segment Editor module (instead of the legacy Editor module).</p>

---
