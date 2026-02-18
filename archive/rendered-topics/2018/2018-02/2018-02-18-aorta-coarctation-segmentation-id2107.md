# Aorta coarctation segmentation

**Topic ID**: 2107
**Date**: 2018-02-18
**URL**: https://discourse.slicer.org/t/aorta-coarctation-segmentation/2107

---

## Post #1 by @slicangelo (2018-02-18 14:03 UTC)

<p>as a correctness I want first to introduce myself to the community<br>
I am a italian technographer of hemodynamics<br>
I do not have the right skills but I have to convert a study ct into a stl file for printing the preoperative model. I have already performed a segmentation but the results are approximate and not transferable in the operative field. I would need a tutorial that allows me to complete the project with a complete stl file with the blood mold and the inside of the aorta with the pathology of the coarctation, empty and transparent, so that I can follow the course of the catheter. sorry if I posted here if there is a discussion in the medical field I would be happy to move<br>
Best regards</p>
<p>Francesco ,TSRM</p>

---

## Post #2 by @lassoan (2018-02-18 14:23 UTC)

<p>Have you completed these segmentation tutorials yet?</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation</a></p>
<p>I would suggest to try “Grow from seeds” effect.</p>
<p>You can create a hollow vessel model by copying the blood segment, expanding using Margin effect, and subtracting the blood segment using Logical operators effect.</p>
<p>If segmentation quality is not good enough (not smooth, etc.) then post screenshots and we can give more specific advice.</p>

---
