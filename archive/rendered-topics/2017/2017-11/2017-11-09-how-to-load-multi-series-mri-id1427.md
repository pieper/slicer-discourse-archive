# How to load multi series mri

**Topic ID**: 1427
**Date**: 2017-11-09
**URL**: https://discourse.slicer.org/t/how-to-load-multi-series-mri/1427

---

## Post #1 by @Jake_Simon (2017-11-09 23:35 UTC)

<pre><code class="lang-auto">Operating system : Windows 10
Slicer version   : 4.8
Expected behavior: Load multi series Dicom correctly
Actual behavior  : Can only view bits and pieces of the scan
</code></pre>
<p>So I have an actual MRI file of my left elbow and I was wanting to model it and view it.</p>
<p>But when I imported the file it had 11 different series to choose from.<br>
I tried loading them all at once to view and it gave me an error.</p>
<p>When I try to load one individual series it shows up as a blury image and cuts half of it off with only a few slices.</p>
<p>When I load a couple at a time it gives me the same issue. And when I still try to model that, no bones come up and its one big blob. My question is, how do I successfully load and model my MRI scan of my elbow without issues?</p>
<p>Also the files that was given to me have no file extension. Hopefully that doesn’t play a role.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2017-11-09 23:56 UTC)

<p>Have you used the DICOM module to load it?</p>
<p>If not, follow instructions on this page: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM</a> for DICOM import and loading.</p>

---

## Post #3 by @Jake_Simon (2017-11-10 00:11 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc64b19b981dcf3fd6521bdc6756c4c0c793a332.png" data-download-href="/uploads/short-url/ta98DRdbZj4AbudWWy7ZGYoG1qO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/cc64b19b981dcf3fd6521bdc6756c4c0c793a332_2_690x367.png" alt="image" data-base62-sha1="ta98DRdbZj4AbudWWy7ZGYoG1qO" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/cc64b19b981dcf3fd6521bdc6756c4c0c793a332_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/cc64b19b981dcf3fd6521bdc6756c4c0c793a332_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/cc64b19b981dcf3fd6521bdc6756c4c0c793a332_2_1380x734.png 2x" data-dominant-color="E2E1DE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2048×1092 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I loaded the files and examined them but they all seemed to have warnings on every single one.</p>

---
