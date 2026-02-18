# When I finish processing in TotalSegmentator, "Show 3d" is not clickable

**Topic ID**: 44721
**Date**: 2025-10-10
**URL**: https://discourse.slicer.org/t/when-i-finish-processing-in-totalsegmentator-show-3d-is-not-clickable/44721

---

## Post #1 by @cp15 (2025-10-10 12:24 UTC)

<p>When I finsih processing a file, it says processing complete and there are no errors listed. I am unable to toggle the “show 3d” button. I’m nor sure what I’m missing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e34eb4deb4e38ac2329821492595ebf01a812d9.jpeg" data-download-href="/uploads/short-url/mzyOMDhuMr7MT0CMgI2bxg32OKd.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e34eb4deb4e38ac2329821492595ebf01a812d9_2_690x375.jpeg" alt="image" data-base62-sha1="mzyOMDhuMr7MT0CMgI2bxg32OKd" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e34eb4deb4e38ac2329821492595ebf01a812d9_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e34eb4deb4e38ac2329821492595ebf01a812d9_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e34eb4deb4e38ac2329821492595ebf01a812d9_2_1380x750.jpeg 2x" data-dominant-color="5E5E66"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1044 90.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2025-10-10 12:35 UTC)

<p>The button is disabled because TotalSegmentator could not segment anything in the image.</p>
<p>Does TotalSegmentator work well on sample data sets, for example CTChest?</p>
<p>Since the “total” model is for whole body CTs, which do not include extremities, it is valid that it cannot find anything. Try the appendicular bones model instead, which can segment bones of the feet. For this model, you need to obtain a license key (free for academic use) from the TotalSegmentator team.</p>

---
