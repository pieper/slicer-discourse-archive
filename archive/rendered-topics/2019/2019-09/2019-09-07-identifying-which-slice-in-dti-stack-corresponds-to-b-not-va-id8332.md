# Identifying which slice in DTI stack corresponds to b(not) value

**Topic ID**: 8332
**Date**: 2019-09-07
**URL**: https://discourse.slicer.org/t/identifying-which-slice-in-dti-stack-corresponds-to-b-not-value/8332

---

## Post #1 by @mshah (2019-09-07 19:32 UTC)

<p>Hi everyone,</p>
<p>I was wondering if there is a specific way in slicer to identify which image in a dti stack corresponds to the non weighted T2 image that corresponds to the b= 0 value? For example, the dimensions of my image stack is (25 256 256 26), meaning it is a dti image with 25 slices in 26 directions. which one of these 25 slices corresponds with the non weighted image? Is there anyway to check this in slicer?</p>
<p>thanks</p>

---

## Post #2 by @ljod (2019-09-07 19:49 UTC)

<p>One way is to visualize in the Volumes module and see which components are bright (not diffusion weighted). There should be an example in the DTI tutorial here:<br>
<a href="http://dmri.slicer.org/docs/" class="onebox" target="_blank" rel="nofollow noopener">http://dmri.slicer.org/docs/</a></p>
<p>Otherwise you can do this programatically or by looking at the image header in a text editor.</p>

---

## Post #3 by @mshah (2019-09-07 20:36 UTC)

<p>Than you for the response! Which tutorial is it, I cant seem to find a relevant one? how does this correspond to the slice in the 25 256 256 26 array?</p>

---
