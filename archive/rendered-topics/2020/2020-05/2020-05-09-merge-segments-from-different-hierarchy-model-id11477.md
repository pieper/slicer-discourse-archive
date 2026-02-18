# Merge segments from different Hierarchy model

**Topic ID**: 11477
**Date**: 2020-05-09
**URL**: https://discourse.slicer.org/t/merge-segments-from-different-hierarchy-model/11477

---

## Post #1 by @Acantharia (2020-05-09 07:42 UTC)

<p>Dear all, I am wondering how to merge segments of different model hierarchy. I did not pay attention at the beginning but I created different “segments” from the same object I want to segment. In other words, the same object A has two similar segments.Please see below the image.<br>
The logical operator effect can merge two segments from the same hierarchymodel but also from different models? Sorry If it is not clear.</p>
<p>Finally, I would be very grateful to know the differences between the segments into the “Segmentation” and the “ModelHierarchy” nodes.</p>
<p>Thanks a lot for your help</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc84798dbad84f563db7e7318615209ea1c7dd53.jpeg" data-download-href="/uploads/short-url/qTHABDa3SJm4uB56OBP34kXmRqP.jpeg?dl=1" title="3DSlicer_Help" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc84798dbad84f563db7e7318615209ea1c7dd53_2_366x499.jpeg" alt="3DSlicer_Help" data-base62-sha1="qTHABDa3SJm4uB56OBP34kXmRqP" width="366" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc84798dbad84f563db7e7318615209ea1c7dd53_2_366x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc84798dbad84f563db7e7318615209ea1c7dd53_2_549x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc84798dbad84f563db7e7318615209ea1c7dd53.jpeg 2x" data-dominant-color="EAEFF2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3DSlicer_Help</span><span class="informations">589×804 64.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @cpinter (2020-05-09 13:18 UTC)

<p>You can find a diagram that demonstrates the role of the different data types such as segmentation and model:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html" class="onebox" target="_blank">https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html</a><br>
Basically model hierarchy nodes are simple folders.</p>
<p>You can convert these model hierarchies to segmentations (and back) by right-clicking the respective nodes. Once you have the segmentations, you can drag&amp;drop segments between segmentations that then you can merge (I guess you want to use union) with the logical operators.</p>

---

## Post #3 by @Acantharia (2020-05-13 08:54 UTC)

<p>Thank you very much for this information<br>
Best regards</p>

---
