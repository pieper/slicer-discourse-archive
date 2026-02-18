# Export Default "Reformat" Registration

**Topic ID**: 39617
**Date**: 2024-10-09
**URL**: https://discourse.slicer.org/t/export-default-reformat-registration/39617

---

## Post #1 by @ThymusTheTrain (2024-10-09 20:44 UTC)

<p>I have an angled T2w sequence and a straight axial T1w. When I use the T2w as a base, the T1w seems to automatically adjust to nicely align with the anatomy in the T2w sequence and is called “Reformat” in the image viewer. Is there a way to export these reformatted sequences, specifically the T1w as NIFTIs?  Or do I need to do manual registration and resampling still?</p>
<p>From a previous <a href="https://discourse.slicer.org/t/resample-overlaid-volume/3671/2">thread</a>, it’s my understanding that manual registration/resampling isn’t necessary because Slicer displays volumes by their physical location.</p>
<p>Thank you in advance for any help!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65e4bc048f7d765e258c94b2a8b59c6e2a588d3a.png" data-download-href="/uploads/short-url/exohICNovnw7OwJhNSTYFakAsb0.png?dl=1" title="ReformatT2wT1w" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65e4bc048f7d765e258c94b2a8b59c6e2a588d3a_2_690x228.png" alt="ReformatT2wT1w" data-base62-sha1="exohICNovnw7OwJhNSTYFakAsb0" width="690" height="228" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65e4bc048f7d765e258c94b2a8b59c6e2a588d3a_2_690x228.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65e4bc048f7d765e258c94b2a8b59c6e2a588d3a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65e4bc048f7d765e258c94b2a8b59c6e2a588d3a.png 2x" data-dominant-color="756B6D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ReformatT2wT1w</span><span class="informations">724×240 46 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-10-09 23:13 UTC)

<p>If you just want to resample one volume in the space of another you can use this with an identity transform:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/resamplescalarvectordwivolume.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/resamplescalarvectordwivolume.html</a></p>

---
