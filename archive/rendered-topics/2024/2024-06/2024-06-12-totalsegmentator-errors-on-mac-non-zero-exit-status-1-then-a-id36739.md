# TotalSegmentator Errors on Mac "...non-zero exit status 1" then "Application is required"

**Topic ID**: 36739
**Date**: 2024-06-12
**URL**: https://discourse.slicer.org/t/totalsegmentator-errors-on-mac-non-zero-exit-status-1-then-application-is-required/36739

---

## Post #1 by @nbn (2024-06-12 22:51 UTC)

<p>Hello, what is the process for using the TotalSegmentator module on a Mac?<br>
Operating System: macOS Monterey Version 12.1<br>
Slicer Version: 5.6.2</p>
<p>I tried installing PyTorch and TotalSegmentator normally. Then I uninstalled both and tried installing PyTorch with CPU (using the application and through typing into the terminal), then installing TotalSegmentator. In between each step of installing extensions, I restarted Slicer as well. At first, the error I was getting was “…non-zero exit status 1” (see image below),<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f2af98f0773fcd2f0290374ac4f79bed4701bc4.jpeg" data-download-href="/uploads/short-url/mI3ZrhAaPFzgu90OOzhemjnedH6.jpeg?dl=1" title="Slicer_Error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f2af98f0773fcd2f0290374ac4f79bed4701bc4_2_690x437.jpeg" alt="Slicer_Error" data-base62-sha1="mI3ZrhAaPFzgu90OOzhemjnedH6" width="690" height="437" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f2af98f0773fcd2f0290374ac4f79bed4701bc4_2_690x437.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f2af98f0773fcd2f0290374ac4f79bed4701bc4_2_1035x655.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f2af98f0773fcd2f0290374ac4f79bed4701bc4.jpeg 2x" data-dominant-color="8F9091"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_Error</span><span class="informations">1146×727 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>then after uninstalling everything (including the application) and trying to install it after downloading Git, it still did not work but I am getting an error that the TotalSegmentator “Application is required”, even though I can see it is installed in my extension manager and restarted Slicer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b85d64462cd17a9b62e245b273013e7f8db0ed30.jpeg" data-download-href="/uploads/short-url/qiXWBUUgShMVvv2gUaTqKsMvljW.jpeg?dl=1" title="Slicer_Error_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b85d64462cd17a9b62e245b273013e7f8db0ed30_2_690x324.jpeg" alt="Slicer_Error_2" data-base62-sha1="qiXWBUUgShMVvv2gUaTqKsMvljW" width="690" height="324" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b85d64462cd17a9b62e245b273013e7f8db0ed30_2_690x324.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b85d64462cd17a9b62e245b273013e7f8db0ed30_2_1035x486.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b85d64462cd17a9b62e245b273013e7f8db0ed30_2_1380x648.jpeg 2x" data-dominant-color="99979C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_Error_2</span><span class="informations">1920×902 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I followed the normal installation steps on my Windows PC and had no problems, but on Mac, it won’t work. Thank you for your help!</p>

---

## Post #2 by @nbn (2024-06-13 01:26 UTC)

<p>I figured out that the second error is due to not fully uninstalling the previous instance of Slicer, but the first error is still occurring.</p>

---

## Post #3 by @lassoan (2024-06-18 19:52 UTC)

<p>The macOS issue is <a href="https://github.com/lassoan/SlicerTotalSegmentator/issues/61">fixed now</a>. TotalSegmentator will work again in Slicer Preview Releases from tomorrow.</p>

---
