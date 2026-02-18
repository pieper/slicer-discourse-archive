# volumetric analysis of mouse brain structures 

**Topic ID**: 4180
**Date**: 2018-09-24
**URL**: https://discourse.slicer.org/t/volumetric-analysis-of-mouse-brain-structures/4180

---

## Post #1 by @jsramos (2018-09-24 17:45 UTC)

<p>Using MR T1 weighted images in DICOM format,  I am not sure how to manually designate the  anatomical structures of interest  and to calculate volumes of these structures as well as the signal density within these structures. Or is there someone who has a semi-automated way to threshold anatomical structures based on public mouse brain atlases.</p>

---

## Post #2 by @muratmaga (2018-09-24 20:19 UTC)

<p>I think this link would give you a good place to start.<br>
<a href="https://wiki.mouseimaging.ca/display/MICePub/Mouse+Brain+Atlases" class="onebox" target="_blank" rel="nofollow noopener">https://wiki.mouseimaging.ca/display/MICePub/Mouse+Brain+Atlases</a></p>
<p>In short, you need to register one of those templates to one of the samples and then transfer labels from the atlas to your own sample using the resultant transformation, and finally measure the sizes/volumes of ROI. In practice a lot of things can go wrong, and the outcome will be dependent on your choice of parameters along the way.</p>

---

## Post #3 by @lassoan (2018-09-25 03:03 UTC)

<p>You may try to use SlicerElastix extension for registration, which tends to be more robust that “General registration (BRAINS)” module that is bundled with Slicer.</p>
<p>You can expect better results if your “atlas” image is similar to your images (acquired using the same imaging protocol, of the same anatomy, etc.). To achieve this, you can segment one of your images manually (or semi-automatically, or automatically - starting from a generic atlas) and use that as atlas.</p>

---
