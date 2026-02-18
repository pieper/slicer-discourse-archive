# Automate extract centerline with unconnected segment

**Topic ID**: 25851
**Date**: 2022-10-23
**URL**: https://discourse.slicer.org/t/automate-extract-centerline-with-unconnected-segment/25851

---

## Post #1 by @hbr (2022-10-23 14:09 UTC)

<p>Hi.</p>
<p>I wanna extract center line of a segmentation that is unconnected. I have a script that do it automatically but when get this segmentation just extract center line partly not all.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69dbf934e54c994af70997f94c5ac1ffeeef0c48.png" data-download-href="/uploads/short-url/f6tqn7jbOV5Pf5FAZBWR8OiQMbu.png?dl=1" title="Screenshot from 2022-10-23 17-41-40" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69dbf934e54c994af70997f94c5ac1ffeeef0c48_2_690x445.png" alt="Screenshot from 2022-10-23 17-41-40" data-base62-sha1="f6tqn7jbOV5Pf5FAZBWR8OiQMbu" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69dbf934e54c994af70997f94c5ac1ffeeef0c48_2_690x445.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69dbf934e54c994af70997f94c5ac1ffeeef0c48_2_1035x667.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69dbf934e54c994af70997f94c5ac1ffeeef0c48.png 2x" data-dominant-color="9D9DD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-10-23 17-41-40</span><span class="informations">1343×867 81.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do anybody have a solution for it?</p>
<p>thanks</p>

---

## Post #2 by @lassoan (2022-10-24 02:47 UTC)

<p>For best results, it would be better to improve the segmentation so that there is no discontinuity in the vessel tree. If you find that too difficult to do it automatically then you can split the segments, detect centerline in each segment separately, and then create an automatic algorithm that merges centerlines.</p>

---

## Post #3 by @hbr (2022-10-24 08:06 UTC)

<p>thanks for response.</p>
<p>is there a method to get endpoints for hole sementation instead of partly like my example with unconnected segment?</p>
<p>thanks</p>

---

## Post #4 by @lassoan (2022-10-24 11:22 UTC)

<p>It would be straightforward to implent such algorithm, for example by splitting the polydata so that you have one connected component in each resulting polydata and process each polydata one by one. However, does not seem to be commonly needed and it would make the current implementation more complex, so I don’t think anyone would start working on this right now (until many small projects or one funded projects need this).</p>
<p>Fortunately, the Extract Centerline module is just a Python scripted module, if you have a little experience in Python and interested in learning a bit about VTK and VMTK libraries then you can add this feature. We can help you if you get stuck at any point.</p>

---

## Post #5 by @hbr (2022-10-24 16:12 UTC)

<p>thank you Andras.</p>
<p>i will try it and if i have any problems let you know to help.</p>

---
