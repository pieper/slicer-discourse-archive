# Newbie question - combining segmentations

**Topic ID**: 12638
**Date**: 2020-07-20
**URL**: https://discourse.slicer.org/t/newbie-question-combining-segmentations/12638

---

## Post #1 by @Jaswant (2020-07-20 13:03 UTC)

<p>I have two summer students who are working with same CT contrast DICOM volume of a dog. They copied the same original  3D slicer data directory but worked independently on their laptops to segment forelimb structures (one student) and thoracic organs  (second student). We will now like to combine all segmentations into a single project. Please point us to “How to…” for this purpose.</p>

---

## Post #2 by @Sunderlandkyl (2020-07-20 13:56 UTC)

<p>If you save the segmentation as a seg.nrrd you can import both into the same Slicer scene:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a68be47fb783f4d3e2826b7740e9ff32197fc64.png" alt="image" data-base62-sha1="8kI6uCIFS4BM4D5s4dfvUd4Gp92" width="345" height="233"></p>
<p>If you would them to be combined, you can move segments from one segmentation to another in the same scene using the “Copy/move segments” section of the Segmentations module:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f721eb80222b691dcec71b896ff7bae70ad50f7.png" data-download-href="/uploads/short-url/mKwpXJ5qtVPO7btM7SDkimmHqbt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f721eb80222b691dcec71b896ff7bae70ad50f7_2_270x375.png" alt="image" data-base62-sha1="mKwpXJ5qtVPO7btM7SDkimmHqbt" width="270" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f721eb80222b691dcec71b896ff7bae70ad50f7_2_270x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f721eb80222b691dcec71b896ff7bae70ad50f7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f721eb80222b691dcec71b896ff7bae70ad50f7.png 2x" data-dominant-color="E9EBEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">396×547 21.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Jaswant (2020-07-20 18:36 UTC)

<p>Thank you Sunderlandkyl. That will be a perfect solution. Both segmentations are saved as as “*.seg.nrrd” files. How do import them in the scene? Can I simply copy-paste the file from one directory to another one. Thanks</p>

---

## Post #4 by @Sunderlandkyl (2020-07-20 18:51 UTC)

<p>You can drag and drop the seg.nrrd files into Slicer.</p>

---

## Post #5 by @Jaswant (2020-07-20 22:25 UTC)

<p>Thank you. That worked perfect!</p>

---
