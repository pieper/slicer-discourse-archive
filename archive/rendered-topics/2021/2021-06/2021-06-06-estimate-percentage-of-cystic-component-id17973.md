# Estimate percentage of cystic component

**Topic ID**: 17973
**Date**: 2021-06-06
**URL**: https://discourse.slicer.org/t/estimate-percentage-of-cystic-component/17973

---

## Post #1 by @Gabriel1 (2021-06-06 12:30 UTC)

<p>Hello,</p>
<p>I would like to estimate the cystic composant of a tumor. Maybe using a percentage of voxel with high value (near water)?<br>
I didn’t find anything like this in segment statistics.<br>
Does anyone have an idea?</p>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @lassoan (2021-06-06 19:02 UTC)

<p>You can segment each component separately in Segment Editor (you can use Threshold effect with appropriate masking settings to split a part of a segment in a specific intensity range - see Masking section at the bottom). Then, you can get the volumes using Segment Statistics module.</p>
<p>I thing the neurosurgery planning tutorial explains this. It may even use a better tool for this - Grow from seeds - that segments all the different regions in one step, from a few scribbles.</p>

---
