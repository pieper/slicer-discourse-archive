# Registration nii volumes

**Topic ID**: 8704
**Date**: 2019-10-08
**URL**: https://discourse.slicer.org/t/registration-nii-volumes/8704

---

## Post #1 by @Alessandro_Piol (2019-10-08 08:12 UTC)

<p>Good morning all,<br>
I cannot finalize a registration between two volumes, representing the same CT reconstruction (.nii). I have one volume smaller than the other, which is even not aligned. These are the steps I follow:</p>
<ul>
<li>I put the markers on the two volumes to identify common points;</li>
<li>I create a Similarity transform based on the just created markers;</li>
<li>I apply the transform to the volume I want to move (the smaller one);</li>
</ul>
<p>The result is that the volume rotates in the right way, but it is not scaled (it is still with the same dimensions).</p>
<p>Is the correct way to do what I want to do?<br>
Thanks in advance.</p>

---

## Post #2 by @lassoan (2019-10-08 11:53 UTC)

<p>Which modules do you use for this?</p>

---
