# Determine performance metrics

**Topic ID**: 7370
**Date**: 2019-07-01
**URL**: https://discourse.slicer.org/t/determine-performance-metrics/7370

---

## Post #1 by @safa (2019-07-01 14:05 UTC)

<p>can i determine performance metrics (Dice, Accuracy, sensitivity,…) with slicer ?</p>

---

## Post #2 by @lassoan (2019-07-01 15:19 UTC)

<p>You can use Segment Comparison module in SlicerRT extension for computing Hausdorff and Dice metrics.</p>

---

## Post #3 by @safa (2019-07-01 16:20 UTC)

<p>thank you<br>
but i can’t select the image in referent segment or compare segment<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05ac428c12345e6fc0d78fa364deb68dc284e0f9.png" data-download-href="/uploads/short-url/Obs3LuxCfF6Nw1dSBiXJxafgVz.png?dl=1" title="icone" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05ac428c12345e6fc0d78fa364deb68dc284e0f9_2_453x500.png" alt="icone" data-base62-sha1="Obs3LuxCfF6Nw1dSBiXJxafgVz" width="453" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05ac428c12345e6fc0d78fa364deb68dc284e0f9_2_453x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05ac428c12345e6fc0d78fa364deb68dc284e0f9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05ac428c12345e6fc0d78fa364deb68dc284e0f9.png 2x" data-dominant-color="F5F5F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">icone</span><span class="informations">549×605 50.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2019-07-01 17:55 UTC)

<p>If you have your structures in a labelmap then you need to import them into a segmentation node (using Segmentations module) before using Segment Comparison.</p>

---

## Post #5 by @safa (2019-07-01 18:51 UTC)

<p>ok thank you</p>
<p>how can I import a segmentation not a data that I’m going to segment manually?<br>
i have already a segmentation, i need to import it not as normal data but  as segmentation data</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62e7a0e04ad10b7f1d030f41ebed48c421707e38.png" data-download-href="/uploads/short-url/e6X3ksFOF3NyDNi9SMQoH7asMMU.png?dl=1" title="import" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62e7a0e04ad10b7f1d030f41ebed48c421707e38.png" alt="import" data-base62-sha1="e6X3ksFOF3NyDNi9SMQoH7asMMU" width="439" height="500" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">import</span><span class="informations">571×650 14.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I can’t import the file from there I click several times on import and it does not work</p>

---

## Post #6 by @cpinter (2019-07-02 00:06 UTC)

<p>Darg&amp;drop the file into Slicer. If it’s DICOM then select the DICOM option.</p>
<p>The Import button in your screenshot imports labelmaps or models already loaded into Slicer as segmentation.</p>

---

## Post #7 by @safa (2019-07-02 14:00 UTC)

<p>the segmentation images that I have are nifti type<br>
i just want to import and compare them<br>
and when I load the data, they are read as normal data, no segmentation<br>
so I can’t compare them</p>

---
