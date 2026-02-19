---
topic_id: 35374
title: "Painting Function Being Clipped"
date: 2024-04-09
url: https://discourse.slicer.org/t/35374
---

# painting function being clipped

**Topic ID**: 35374
**Date**: 2024-04-09
**URL**: https://discourse.slicer.org/t/painting-function-being-clipped/35374

---

## Post #1 by @david (2024-04-09 01:10 UTC)

<p>Operating system: Apple Sonoma 14<br>
Slicer version: 5.6.1<br>
Expected behavior: paint tool<br>
Actual behavior: paint tool effect being cropped</p>
<p>I’m new to 3D Slicer. When I use the paint tool, it is cropping.<br>
(Image of example below)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eae15842f8907c57c75b9a10123142042047fca7.jpeg" data-download-href="/uploads/short-url/xvQwFUxag68Mbpvg8SNzcQBu0Cj.jpeg?dl=1" title="question" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eae15842f8907c57c75b9a10123142042047fca7_2_658x500.jpeg" alt="question" data-base62-sha1="xvQwFUxag68Mbpvg8SNzcQBu0Cj" width="658" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eae15842f8907c57c75b9a10123142042047fca7_2_658x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eae15842f8907c57c75b9a10123142042047fca7_2_987x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eae15842f8907c57c75b9a10123142042047fca7_2_1316x1000.jpeg 2x" data-dominant-color="7D7973"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">question</span><span class="informations">1522×1156 222 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-04-09 15:55 UTC)

<p>Probably the segmentation geometry doesn’t match the background volume.  Try starting by following tutorials and if you get to something you can’t explain provide the shortest step by step method that gets your to a point where things don’t behave as you expect.</p>

---

## Post #3 by @david (2024-04-09 17:08 UTC)

<p>Thanks for your reply Steve.</p>
<p>I saw a background segmentation used in a “seeding” tutorial. Do I need to create a background segmentation in order to paint (or create) a new segmentation?</p>
<p>I’m learning on the test data provided within the software. (Dental Surgery)</p>
<p>Unfortunately I am only able to paint (or create brush-strokes) within a certain box or zone in on all 3 angles. (Y, R, and G)</p>

---

## Post #4 by @pieper (2024-04-09 17:36 UTC)

<p>What I mean is that you should be able start with a fresh instance of Slicer, download any of the sample data (e.g. Dental Surgery), right click on it in the Data module and pick ‘Segment this’, add a segment and start painting.  If this sequence isn’t working there’s something fundamentally wrong.  But if it is working, then we’d need to know what steps you take that end up in the situation you are reporting.</p>

---

## Post #5 by @david (2024-04-09 20:28 UTC)

<p>You are correct. Restarting Slicer worked. Thanks again for your time and response!</p>

---

## Post #6 by @lassoan (2024-04-10 04:12 UTC)

<p>See explanation of why restarting Slicer worked in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries">Segment Editor documentation</a> (in short: default segment geometry is determined by the image that you selected <em>first</em>).</p>

---
