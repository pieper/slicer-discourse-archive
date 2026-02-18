# SlicerMorph ImageStacks ROI transformation yields incorrect cropping

**Topic ID**: 42525
**Date**: 2025-04-10
**URL**: https://discourse.slicer.org/t/slicermorph-imagestacks-roi-transformation-yields-incorrect-cropping/42525

---

## Post #1 by @scutisorex (2025-04-10 15:53 UTC)

<p>Hi all,</p>
<p>I’m using ImageStacks to import ROIs of some larger CT stacks. I specified my ROI using Markups and transformed it to include only the portion of the scan I wanted (skull of the animal, see below). This included rotating the ROI out of the plane of the slices. However, when I did the subsequent ROI import at half resolution, it didn’t keep everything inside the ROI, and kept some of what I didn’t need (especially visible in the green slice and 3D view):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b58bcf8d388b7e8075c5c109f70b27c89eb12089.jpeg" data-download-href="/uploads/short-url/pU1XQBHSvJvqTVQpOmbQlHUGLUJ.jpeg?dl=1" title="ROIissue_04102025" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b58bcf8d388b7e8075c5c109f70b27c89eb12089_2_690x431.jpeg" alt="ROIissue_04102025" data-base62-sha1="pU1XQBHSvJvqTVQpOmbQlHUGLUJ" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b58bcf8d388b7e8075c5c109f70b27c89eb12089_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b58bcf8d388b7e8075c5c109f70b27c89eb12089_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b58bcf8d388b7e8075c5c109f70b27c89eb12089_2_1380x862.jpeg 2x" data-dominant-color="59484D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ROIissue_04102025</span><span class="informations">1920×1200 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any thoughts on why this occurred? Does the module have the capability to include just parts of a slice? I feel like I’ve had no issue with this in the past.</p>
<p>Many thanks for any insights here!</p>
<p><strong>Operating system:</strong> Windows 10<br>
<strong>Slicer version:</strong> 5.8.1<br>
<strong>SlicerMorph Version:</strong> 172e036</p>

---

## Post #2 by @muratmaga (2025-04-10 16:00 UTC)

<aside class="quote no-group" data-username="scutisorex" data-post="1" data-topic="42525">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/scutisorex/48/77239_2.png" class="avatar"> scutisorex:</div>
<blockquote>
<p>Does the module have the capability to include just parts of a slice?</p>
</blockquote>
</aside>
<p>I don’t think ImageStacks currently support cropping the volume while importing under a transformed ROI. If that’s what you want to do, you need to use the regular <code>Crop Volume</code>.</p>
<p>Also, if you can a feature request for this on the SlicerMorph github page, we might consider implementing (at some point)</p>

---

## Post #3 by @scutisorex (2025-04-10 16:01 UTC)

<p>Thanks Murat! I’ll do the feature request.</p>

---
