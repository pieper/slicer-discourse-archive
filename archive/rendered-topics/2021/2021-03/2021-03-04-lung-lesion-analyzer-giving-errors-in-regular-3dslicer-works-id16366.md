# Lung Lesion Analyzer giving errors in regular 3Dslicer, works properly in SlicerCIP

**Topic ID**: 16366
**Date**: 2021-03-04
**URL**: https://discourse.slicer.org/t/lung-lesion-analyzer-giving-errors-in-regular-3dslicer-works-properly-in-slicercip/16366

---

## Post #1 by @sraina (2021-03-04 16:32 UTC)

<p>Hi All,<br>
I am trying to use the Lung Lesion Analyzer in 3DSlicer 4.11.20210226 and upon clicking the New nodule button I do not see the option to place a seed in the nodule. It looks like this image below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/737957aee4eb14a3e45ab065b58fac2649bea7e8.png" data-download-href="/uploads/short-url/gtwSP056aHRRKUcF2xuFWujpMDe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/737957aee4eb14a3e45ab065b58fac2649bea7e8_2_568x500.png" alt="image" data-base62-sha1="gtwSP056aHRRKUcF2xuFWujpMDe" width="568" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/737957aee4eb14a3e45ab065b58fac2649bea7e8_2_568x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/737957aee4eb14a3e45ab065b58fac2649bea7e8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/737957aee4eb14a3e45ab065b58fac2649bea7e8.png 2x" data-dominant-color="F5F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">622×547 29 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However when I press the “Previous Modules” button and then press the “Next Modules” button up top The screen changes to this, showing the options to add the seed. However even after I press " Segment Nodule" the processing ends with message “Completed With Errors”. I have tried the same set of DICOMS in the latest SlicerCIP version and it works fine and segments the nodule well.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4dd780804532eade3a9550ec63cd4c94f18b3c8.png" data-download-href="/uploads/short-url/nwsNBibhGaOLO7E9cY8e25FnZO0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4dd780804532eade3a9550ec63cd4c94f18b3c8.png" alt="image" data-base62-sha1="nwsNBibhGaOLO7E9cY8e25FnZO0" width="528" height="499" data-dominant-color="F5F6F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">622×588 19.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Just wanted to make the programmers aware of it.</p>
<p>Thanks,<br>
SR</p>
<p>Operating system: Windows 10 Pro v. 1909<br>
Slicer version:4.11.20210226<br>
Expected behavior:<br>
Actual behavior:</p>

---
