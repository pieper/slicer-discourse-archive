# TotalSegmentator failed to compute – ModuleNotFoundError: No module named 'skimage.morphology'

**Topic ID**: 43577
**Date**: 2025-07-02
**URL**: https://discourse.slicer.org/t/totalsegmentator-failed-to-compute-modulenotfounderror-no-module-named-skimage-morphology/43577

---

## Post #1 by @Mael (2025-07-02 14:40 UTC)

<p>Hi everyone,</p>
<p>I’m trying to use the TotalSegmentator extension in 3D Slicer, but I get an error when I try to compute the segmentation.</p>
<p>The error message is:</p>
<pre><code class="lang-auto">ModuleNotFoundError: No module named 'skimage.morphology'
</code></pre>
<p>It seems quite similar to <a href="https://discourse.slicer.org/t/totalsegmentator-failed-to-compute-results-returned-non-zero-exit-status-1/38142">this issue</a>, except in my case the missing module is <em>skimage.morphology</em> instead of <em>acvl_utils</em>.</p>
<p>Here are my system details:</p>
<p>Windows 11 Home<br>
Slicer version: 5.9.0</p>
<p>Any ideas on how to fix this? Should I manually install scikit-image somewhere?</p>
<p>Thanks in advance for your help!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40891cccbaae6445d39e5ed43a28c4e1d9a25502.png" data-download-href="/uploads/short-url/9cUjRan8C52nKrYDQ30cuv2589s.png?dl=1" title="Screenshot 2025-07-02 141153" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40891cccbaae6445d39e5ed43a28c4e1d9a25502_2_504x500.png" alt="Screenshot 2025-07-02 141153" data-base62-sha1="9cUjRan8C52nKrYDQ30cuv2589s" width="504" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40891cccbaae6445d39e5ed43a28c4e1d9a25502_2_504x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40891cccbaae6445d39e5ed43a28c4e1d9a25502_2_756x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40891cccbaae6445d39e5ed43a28c4e1d9a25502_2_1008x1000.png 2x" data-dominant-color="3A3A3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-07-02 141153</span><span class="informations">1037×1028 51.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11e094b2a4b8f19fa6abd7cae15832201b82808c.png" data-download-href="/uploads/short-url/2y9hjrsMzJvPgsx5WkbmESVDNWA.png?dl=1" title="Screenshot 2025-07-02 141234" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11e094b2a4b8f19fa6abd7cae15832201b82808c.png" alt="Screenshot 2025-07-02 141234" data-base62-sha1="2y9hjrsMzJvPgsx5WkbmESVDNWA" width="232" height="500" data-dominant-color="393C3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-07-02 141234</span><span class="informations">427×917 37 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
