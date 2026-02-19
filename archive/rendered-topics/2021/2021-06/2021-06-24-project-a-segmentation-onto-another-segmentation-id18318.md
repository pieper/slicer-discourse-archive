---
topic_id: 18318
title: "Project A Segmentation Onto Another Segmentation"
date: 2021-06-24
url: https://discourse.slicer.org/t/18318
---

# Project a segmentation onto another segmentation

**Topic ID**: 18318
**Date**: 2021-06-24
**URL**: https://discourse.slicer.org/t/project-a-segmentation-onto-another-segmentation/18318

---

## Post #1 by @Cody_Xie (2021-06-24 10:45 UTC)

<p>Hi to all,</p>
<p>I was wondering if there is a way to project a segmentation onto another segmentation.</p>
<p>For example, here we have two segmentations (see the figures below): A heart left ventricle (red) and a target (blue). As you can see, the blue segmentation is not completely on the red segmentation. Most of the part is inside the red segmentation, while a small part is outside the red segmentation.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d958138bb83d8ac9d421aa5d3c3edff9ddef1f6a.jpeg" alt="1" data-base62-sha1="v0IjseYDT8pPUc8bQxm8buIi3Ka" width="671" height="432"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f55c0eeb814f46baacfa30db1f1ae2fc9bea25bf.png" alt="2" data-base62-sha1="z0ydhs1papl4Wx8Fd8xyZuwTGGz" width="671" height="432"></p>
<p>Could you tell me how to project the blue segmentation onto the red segmentation? The result I need is shown in the figure below. Regarding the yellow segmentation, I first created a closed curve markup along the boundary of the blue segmentation from a specific view, then did curve cut in Dynamic Modeler. However, the result may not be precise, since the process is manual, and if change the view, the result will be different.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b09aba8d2a1a97285ce1333308516466fe7fa49.png" alt="3" data-base62-sha1="68Jfw3LuLZTLl5SRYTnVZZcdbUl" width="671" height="432"></p>
<p>I was thinking about extract the boundary of the blue segmentation, then find the closest points on the red segmentation and do a curve cut. I don’t know if this method is feasible, or maybe there’s a better way to achieve the goal.</p>
<p>Many thanks for your help!</p>

---

## Post #2 by @lassoan (2021-06-25 18:20 UTC)

<p>There are several potential approaches to implement this. What is the clinical application? What is your overall goal?</p>

---
