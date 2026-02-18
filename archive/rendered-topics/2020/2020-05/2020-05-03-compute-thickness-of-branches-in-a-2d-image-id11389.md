# Compute thickness of branches in a 2D image

**Topic ID**: 11389
**Date**: 2020-05-03
**URL**: https://discourse.slicer.org/t/compute-thickness-of-branches-in-a-2d-image/11389

---

## Post #1 by @Deepa (2020-05-03 07:23 UTC)

<p>I would like to ask for suggestions on how to obtain the thickness of the edges in a given input image</p>
<p>Sample image:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d197d23e0913083c94b74241ea4b2382ec92593.png" alt="image" data-base62-sha1="dhB0T1KRpkNoIfry97yVIAS58C7" width="690" height="325"></p>
<p>Suggestions on how to proceed will be really helpful.</p>
<p>In the end, I would like to obtain the centerline skeleton and find the thickness (/radius measure similar to maximal inscribed sphere radius for 3D) of each edge/branch.</p>

---

## Post #2 by @lassoan (2020-05-20 00:31 UTC)

<p>Have you tried to use <a href="https://github.com/vmtk/vmtk">VMTK</a> for this? SlicerVMTK’s centerline extraction module may give you this information directly.</p>
<p>If VMTK does not work on your data then you can do what is described in this post: <a href="https://discourse.slicer.org/t/how-to-analyze-the-thickness-of-the-model/2735" class="inline-onebox">How to analyze the thickness of the model</a></p>

---

## Post #3 by @Deepa (2020-05-20 15:30 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks for the response. Yes, I could successfully obtain the thickness using Fiji. I will<br>
check VMTK, I wasn’t sure about how the thickness is computed for 2D in VMTK .</p>

---
