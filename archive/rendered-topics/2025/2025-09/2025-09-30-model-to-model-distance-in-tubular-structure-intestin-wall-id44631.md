---
topic_id: 44631
title: "Model To Model Distance In Tubular Structure Intestin Wall"
date: 2025-09-30
url: https://discourse.slicer.org/t/44631
---

# Model to Model Distance in tubular structure - Intestin wall

**Topic ID**: 44631
**Date**: 2025-09-30
**URL**: https://discourse.slicer.org/t/model-to-model-distance-in-tubular-structure-intestin-wall/44631

---

## Post #1 by @winter (2025-09-30 10:50 UTC)

<p>Dear Slicer Community,</p>
<p>I am working on a heat map representation of the thickness of colon wall in mice. I Segmented the  lumen, the colon wall and the area outside the outer colon wall, and exported the segments to models. Using Model To Model Distance module I got the distance map in a VTK Output File. In the Model to Model Distance module I am using the lumen as Source and the “outside area” as target. The VTK output than has the distance information and a shape of the source model. But I want to show this information on the colon wall. Is it possible to transfer the color coding (I mean the thickness coding) to the model of the colon wall?<br>
The pixel size is too big for the segmentation of the outer and inner surface of the colon wall.</p>
<p>Thank you for your help.</p>

---

## Post #2 by @cpinter (2025-09-30 11:00 UTC)

<p>Just seeing this in a rush, a quick idea: can’t you just swap the inputs? Then the reference will be the higher quality colon wall</p>

---

## Post #3 by @winter (2025-09-30 13:20 UTC)

<p>Thank you Csaba!<br>
Unfortunately no, the colon wall is actually the “gap” between the 2 models… <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @cpinter (2025-09-30 14:30 UTC)

<p>Well, transferring the coloring is not possible, at least far from straightforward. How about calculating the difference of the two models you are interested in from the colon model, and combine (e.g. average) the two scalar arrays that you can show in the model of interest?</p>

---

## Post #5 by @winter (2025-10-01 10:30 UTC)

<p>Dear Csaba,</p>
<p>Thank you for your suggestions. I’ve found the solution, and it turned out to be quite simple. The core issue was my incorrect approach of trying to use the colon wall directly as a tubular structure for measurement.</p>
<p>My corrected workflow is as follows:</p>
<p>I used the combined segmentation of the colon wall and lumen and performed oversampling of the segment.</p>
<p>I then applied the hollow function (using the segment as the inside surface) on this segment.</p>
<p>This generated a thin layer surrounding the external surface of the colon wall.</p>
<p>Finally, I exported this newly generated layer, along with the lumen segmentation to models, and used them as inputs for the Model To Model Distance module.</p>
<p>This process successfully produced the distance map on the colon wall.</p>

---

## Post #6 by @cpinter (2025-10-02 09:06 UTC)

<p>OK, great that you found a solution! I think we could have reached this (or another good) conclusion much faster if you had provided screenshots etc. Only based on short descriptions we are kind of shooting around in the dark… Just saying this for next time <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
