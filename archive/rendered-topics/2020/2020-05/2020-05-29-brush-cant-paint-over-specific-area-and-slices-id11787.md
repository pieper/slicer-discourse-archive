# Brush can't paint over specific area and slices

**Topic ID**: 11787
**Date**: 2020-05-29
**URL**: https://discourse.slicer.org/t/brush-cant-paint-over-specific-area-and-slices/11787

---

## Post #1 by @Tedd (2020-05-29 18:53 UTC)

<p>Hello everyone. I am using slicer 2 years so far. Lately I faced first time a problem that I cant resolve.<br>
When i load a CT dataset, my brush behavior isn’t working properly as I can paint over specific areas and below them the paint is been cut. I use the segment editor module. The weird is that I have counter that problem at 3 different pc’s but not in another one, and that if I use the simple “editor” module I can paint everywhere… I can’t resolve it and cant understand what’s wrong. I tried to rotate the volume plane but nothing worked. Can someone help me?<br>
Thanks.</p>
<p>Operating system: Windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior: Normal paint over slices<br>
Actual behavior: doesn’t working</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a90e08d7e6b05b3adc34f8ba48d9ff5e71beac14.png" alt="Screenshot_2" data-base62-sha1="o7wLcJPywZo49DEcP8qkMHIiRCY" width="618" height="351"></p>

---

## Post #2 by @lassoan (2020-05-29 23:51 UTC)

<p>This looks like a rendering issue related to display scaling (you might have changed the resolution of your screen after you have logged, you use multiple monitors, etc.). This issue has been fixed in Slicer-4.11, so please try a recent Slicer-4.11 release.</p>

---

## Post #3 by @Tedd (2020-06-09 06:42 UTC)

<p>I tried the recent 4.11 version but still the same error occurs. I tested to two different PC but still the same.The only solution I found until now, is  to use simple “editor” module for painting (at 4.10 version) where I can paint over all the slices.</p>

---

## Post #4 by @lassoan (2020-06-09 06:50 UTC)

<p>Great, then it means that everything works well and you just need to adjust the segmentation’s geometry.</p>
<p>Segmentation geometry (origin, spacing, axis directions, and extent) is determined from the first selected master volume by default, so if you later change that or transform the segmentation or the master volume, etc. then the extents may not cover the entire region where you want to draw.</p>
<p>You can adjust the segmentation’s geometry by clicking on the “Specify geometry” button next to the master volume selector, then choosing the volume that you want to segment as “Source geometry”, and clicking OK.</p>

---
