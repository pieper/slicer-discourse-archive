---
topic_id: 3965
title: "Using Model To Model Distance And Shape Population Viewer To"
date: 2018-09-01
url: https://discourse.slicer.org/t/3965
---

# Using model-to-model distance and shape population viewer to find cortical thickness

**Topic ID**: 3965
**Date**: 2018-09-01
**URL**: https://discourse.slicer.org/t/using-model-to-model-distance-and-shape-population-viewer-to-find-cortical-thickness/3965

---

## Post #1 by @jamesredd (2018-09-01 01:59 UTC)

<p>Operating system: Ubuntu 18.04<br>
Slicer version: 4.8.1-linux-amd64</p>
<p>I’m using the extensions model-to-model distance and shape population viewer with the purpose of finding distance between cortical surface and white matter on the sagittal axis.</p>
<p>My current process is running model to model distance on the grey matter and white matter models, then putting the created model into shape population viewer. There, the absolute measurement looks good and what I’d expect it to look.</p>
<p>However, I want not the absolute distance, but instead the distance between a point on the surface of the grey matter and the closest point on the white matter directly downwards.</p>
<p>To get that, I select the PointToPointAlongY attribute.</p>
<p>Now here is when things get strange.</p>
<p>For an example: Let’s say we have chunk of grey matter, intersected on both sides by lines of white matter, with y axis being upwards.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27b94fa79731efe76018108f10f21f53e9e03cb0.jpeg" alt="image" data-base62-sha1="5FpEdrdWdPAvwKEdH0c18plAhsk" width="328" height="322"></p>
<p>The distance from GM to the nearest WM below it should look something like this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d7a5434529f5146867474292339f2b61c24ff54.png" alt="image" data-base62-sha1="mt73bsVXWADP8JOG5GbkdA6gx0M" width="184" height="266"></p>
<p>Where, on the surface of the GM, it is red until you reach the rightward limit of the WM, in which case it immediately switches back to green, indicating there is no more WM below it.</p>
<p>Instead I get strange patterns like this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09b18fcd513630c778a605452cb4d36bd4dd0bca.jpeg" alt="image" data-base62-sha1="1nKIJmCgUCrNcU5qinIuP7criUG" width="187" height="300"></p>
<p>I’ve tried multiple axes, and have made sure I’m on the right one. I can’t seem to find an attribute that actually maps to vertical distance to closest white matter.</p>
<p>Is there something I’m misunderstanding?</p>

---
