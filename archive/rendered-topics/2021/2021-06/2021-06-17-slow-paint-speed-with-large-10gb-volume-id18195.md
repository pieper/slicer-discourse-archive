# Slow paint speed with large (10GB) volume

**Topic ID**: 18195
**Date**: 2021-06-17
**URL**: https://discourse.slicer.org/t/slow-paint-speed-with-large-10gb-volume/18195

---

## Post #1 by @hherhold (2021-06-17 21:41 UTC)

<p>I have a colleague with a fairly large micro-CT scan (10GB), and he is experiencing sluggish response times when painting with a sphere brush in the 2D slices (Show 3D not enabled). His machine is windows with 128GB RAM. Not sure on specs for the CPU.</p>
<p>Seems to me this is a pretty large volume, and it’s just a lot of data to go through for painting with intensity range turned on? Any suggestions? I’m thinking the best way to proceed is probably to chop it into a few pieces and work on it in sections.</p>
<p>Any ideas would be most appreciated - thanks!!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2021-06-18 20:00 UTC)

<p>This volume is about 30-50x larger than average volumes, which exposes performance bottlenecks that we normally don’t perceive at all. A 0.5s operation may turn into a 20s operation.</p>
<p>Potential solutions:</p>
<ul>
<li>crop and/or downsample: as you suggested, to work with smaller pieces at a time</li>
<li>use larger hardware: if it’s just a one-off case then you can try to rent a very powerful computer from a cloud provider and see if it makes the workflow fast enough</li>
<li>optimize performance: build Slicer in “release with debug info” mode and do the segmentation with a profiler attached; if you identify the performance bottlenecks then we can give advice about how to improve the update speed</li>
</ul>

---
