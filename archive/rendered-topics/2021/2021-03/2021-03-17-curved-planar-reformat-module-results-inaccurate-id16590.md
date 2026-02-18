# Curved Planar Reformat module results inaccurate

**Topic ID**: 16590
**Date**: 2021-03-17
**URL**: https://discourse.slicer.org/t/curved-planar-reformat-module-results-inaccurate/16590

---

## Post #1 by @mikebind (2021-03-17 07:14 UTC)

<p>Hello,  I am again trying to use the Curved Planar Reformat module and finding that it does not seem to produce a reasonable straightened volume for an airway I am trying to process.  Here is an outline of the steps followed to get to this point:</p>
<ul>
<li>Threshold CT to generate Air segment and then cut this down using scissors tool so that it only contains the airway segment of interest</li>
<li>Manually place 2 endpoints at either end of the airway using the VMTK ExtractCenterline module</li>
<li>Extract centerline curve node using VMTK ExtractCenterline module</li>
<li>Generate straightened volume and straighten transform by using CurvedPlanarReformat module with all default settings (1 mm curve resolution, 1 mm slice resolution 30x30mm slice size)</li>
</ul>
<p>The resulting straightened volume does NOT follow the supplied centerline curve.  This is most obvious in the upper portion of the airway, where the center of the straightened volume’s “axial” slice (the one perpendicular to the curve) does not remain in the airway, despite the fact that the centerline curve does remain in the center of the airway in the original volume.</p>
<p>Here is a view of the straightened volume:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b84ada2df9340abb7b7d92724cf32e9ab7b4a038.png" data-download-href="/uploads/short-url/qikdW7O0nOoF2rtYPRi48V1RXgA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b84ada2df9340abb7b7d92724cf32e9ab7b4a038_2_690x418.png" alt="image" data-base62-sha1="qikdW7O0nOoF2rtYPRi48V1RXgA" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b84ada2df9340abb7b7d92724cf32e9ab7b4a038_2_690x418.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b84ada2df9340abb7b7d92724cf32e9ab7b4a038_2_1035x627.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b84ada2df9340abb7b7d92724cf32e9ab7b4a038_2_1380x836.png 2x" data-dominant-color="989A9C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1820×1105 454 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The cyan outline is the airway segmentation on the original volume, transformed by the straightening transform, and overlaid on the straightened volume. The yellow outline is an airway segmentation with the straightened volume as the master volume, using the same air threshold. If the reformat and the transform were good, the yellow and cyan segmentations should closely coincide.  Instead, in some places, they barely overlap (see the red slice view). In the 3D view it is possible to see that the yellow and cyan segmentations have broadly similar shapes, but the cyan segmentation seems to have been perhaps under-straightened compared to the yellow one.</p>
<p>Here’s how they look back in the original volume space (i.e. the cyan segmentation has no transform applied, and the yellow segmentation has the inverse of the straightening transform applied):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aaf7fc518ac8dd28c55758acf5ade07b8a91656b.jpeg" data-download-href="/uploads/short-url/oostyuzMYqbjWtuR1kFNRygIB2X.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aaf7fc518ac8dd28c55758acf5ade07b8a91656b_2_690x418.jpeg" alt="image" data-base62-sha1="oostyuzMYqbjWtuR1kFNRygIB2X" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aaf7fc518ac8dd28c55758acf5ade07b8a91656b_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aaf7fc518ac8dd28c55758acf5ade07b8a91656b_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aaf7fc518ac8dd28c55758acf5ade07b8a91656b_2_1380x836.jpeg 2x" data-dominant-color="979A9C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1823×1105 346 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I know CurvedPlanarReformat has been significantly reworked since this time, but just in case it is relevant, this was my post from last time I ran into problems with it: <a href="https://discourse.slicer.org/t/curved-planar-reformat-module-reslicing-error/10248">https://discourse.slicer.org/t/curved-planar-reformat-module-reslicing-error/10248</a></p>
<p>I tried to reproduce this issue with the MRHead volume from SampleData, but I do not see the same deviation.  Because it is MR and an adult, the segmentation I could get was different and less curved, but within that constraint, the reformat looked pretty good to me.  One difference I noticed was that the MRHead IJK to RAS matrix  has only ones and zeros, whereas the volume I was working with had been reoriented and has slightly tilted axes.</p>
<p>If someone is willing to take a look at this, I can create an anonymized dataset I can share. I’m also open to suggestions.  Thanks!</p>

---

## Post #2 by @mikebind (2021-03-17 07:34 UTC)

<p>I just realized that the original volume node I was using had a linear transform applied to it. When I hardened this transform and tried the CPR again, it worked beautifully.  So, I think the CPR module must resample in the VolumeRAS coordinate system rather than the WorldRAS coordinate system.  This is somewhat confusing as a user, because the centerline curve node is in the WorldRAS coordinate system, and was derived from the same (linearly transformed) volume.  Perhaps, if the CurvedPlanarReformatModule is not going to take parent transforms into account (and maybe there are good reasons it shouldn’t?), it should at least warn the user when there are parent transforms which are being ignored?</p>

---

## Post #3 by @lassoan (2021-03-17 14:32 UTC)

<p>Thanks for reporting and investigating this. The module is in Sandbox extension exactly because of this kind of small things. I agree that the parent transform should be taken into account (or at least an error/warning should be reported if there is a non-identity parent transform). I’ve added an issue to track this: <a href="https://github.com/PerkLab/SlicerSandbox/issues/9" class="inline-onebox">Make CurvedPlanarReformat module take into accound parent transform of volume · Issue #9 · PerkLab/SlicerSandbox · GitHub</a> - maybe you could give it a try to fix it.</p>

---
