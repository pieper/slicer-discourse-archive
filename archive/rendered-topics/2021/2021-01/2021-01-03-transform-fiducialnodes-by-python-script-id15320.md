# Transform fiducialNodes by python script

**Topic ID**: 15320
**Date**: 2021-01-03
**URL**: https://discourse.slicer.org/t/transform-fiducialnodes-by-python-script/15320

---

## Post #1 by @1116 (2021-01-03 03:39 UTC)

<p>I want to transform some fiducialNodes by transformnode<br>
but i can only get same value of fiducialNodes before transform.</p>
<p>Could you indentify what’s wrong?<br>
The transformNode was created by elastix module</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0047fad6537059335770a29e71a63cd1ee07cc6.jpeg" data-download-href="/uploads/short-url/mPA25PYFexFG8UZR5FNyCR0FBrg.jpeg?dl=1" title="스크린샷 2021-01-03 오후 12.39.20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0047fad6537059335770a29e71a63cd1ee07cc6_2_690x175.jpeg" alt="스크린샷 2021-01-03 오후 12.39.20" data-base62-sha1="mPA25PYFexFG8UZR5FNyCR0FBrg" width="690" height="175" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0047fad6537059335770a29e71a63cd1ee07cc6_2_690x175.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0047fad6537059335770a29e71a63cd1ee07cc6_2_1035x262.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0047fad6537059335770a29e71a63cd1ee07cc6_2_1380x350.jpeg 2x" data-dominant-color="F6F6F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">스크린샷 2021-01-03 오후 12.39.20</span><span class="informations">1490×380 93.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d02ef082798ed74dcfb3e693cc1969dc50fc0bd.jpeg" data-download-href="/uploads/short-url/k7rBKd1iWIkuGMTmKoOTKNKynvL.jpeg?dl=1" title="스크린샷 2021-01-03 오후 12.37.54" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d02ef082798ed74dcfb3e693cc1969dc50fc0bd_2_690x158.jpeg" alt="스크린샷 2021-01-03 오후 12.37.54" data-base62-sha1="k7rBKd1iWIkuGMTmKoOTKNKynvL" width="690" height="158" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d02ef082798ed74dcfb3e693cc1969dc50fc0bd_2_690x158.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d02ef082798ed74dcfb3e693cc1969dc50fc0bd_2_1035x237.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d02ef082798ed74dcfb3e693cc1969dc50fc0bd_2_1380x316.jpeg 2x" data-dominant-color="F5F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">스크린샷 2021-01-03 오후 12.37.54</span><span class="informations">1476×340 82.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2021-01-03 04:31 UTC)

<p>Try using:</p>
<pre><code>narray = slicer.util.arrayFromMarkupsControlPoints(markupsNode, world=True)</code></pre>

---
