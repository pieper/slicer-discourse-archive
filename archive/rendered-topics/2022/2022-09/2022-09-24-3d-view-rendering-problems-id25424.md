# 3D View Rendering Problems

**Topic ID**: 25424
**Date**: 2022-09-24
**URL**: https://discourse.slicer.org/t/3d-view-rendering-problems/25424

---

## Post #1 by @SlicerDK (2022-09-24 19:30 UTC)

<p>Hi everyone, I’m very new to Slicer and have found some bugs that I cannot find an explanation for. I’m using Slicer v5.0.3.</p>
<p>I’ll explain it in order of the steps I performed.</p>
<ol>
<li>
<p>I used ‘Threshold’ to segment a tooth from a CBCT scan<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c75d9259ca51d63490a6ccac2dd2cade26902084.png" data-download-href="/uploads/short-url/srFuzbB0OQcg76sTRYwC9BCCvC4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c75d9259ca51d63490a6ccac2dd2cade26902084_2_690x404.png" alt="image" data-base62-sha1="srFuzbB0OQcg76sTRYwC9BCCvC4" width="690" height="404" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c75d9259ca51d63490a6ccac2dd2cade26902084_2_690x404.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c75d9259ca51d63490a6ccac2dd2cade26902084_2_1035x606.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c75d9259ca51d63490a6ccac2dd2cade26902084_2_1380x808.png 2x" data-dominant-color="B1B6D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1398×819 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Turned off the ‘eye’ on that segment, created a new segment, and performed manual segmentation using the ‘Draw’ tool and ‘Fill between the Slices’.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d735d8f95af1f6d6e59306b379b49cc909dd1cc7.png" data-download-href="/uploads/short-url/uHQ1ug3jxFjPPdSv2sH43VrefDV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d735d8f95af1f6d6e59306b379b49cc909dd1cc7_2_620x499.png" alt="image" data-base62-sha1="uHQ1ug3jxFjPPdSv2sH43VrefDV" width="620" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d735d8f95af1f6d6e59306b379b49cc909dd1cc7_2_620x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d735d8f95af1f6d6e59306b379b49cc909dd1cc7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d735d8f95af1f6d6e59306b379b49cc909dd1cc7.png 2x" data-dominant-color="9D9CD1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">755×608 73.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Now, I turned on both segments one by one, and that looks like one would expect<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c2c66cd2161ef53d4586fe88770e73dbd7bdcf4.png" data-download-href="/uploads/short-url/d9p3xSBJaEGbAw839d133hcrumw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c2c66cd2161ef53d4586fe88770e73dbd7bdcf4_2_690x292.png" alt="image" data-base62-sha1="d9p3xSBJaEGbAw839d133hcrumw" width="690" height="292" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c2c66cd2161ef53d4586fe88770e73dbd7bdcf4_2_690x292.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c2c66cd2161ef53d4586fe88770e73dbd7bdcf4_2_1035x438.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c2c66cd2161ef53d4586fe88770e73dbd7bdcf4_2_1380x584.png 2x" data-dominant-color="B3B5DB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1452×615 69.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e756d5acc20fc4841aea3276e6e428cb83cc8ed.jpeg" data-download-href="/uploads/short-url/bc4PpAXTTvLv5bQxzFIELmvmrSJ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e756d5acc20fc4841aea3276e6e428cb83cc8ed_2_575x500.jpeg" alt="image" data-base62-sha1="bc4PpAXTTvLv5bQxzFIELmvmrSJ" width="575" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e756d5acc20fc4841aea3276e6e428cb83cc8ed_2_575x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e756d5acc20fc4841aea3276e6e428cb83cc8ed.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e756d5acc20fc4841aea3276e6e428cb83cc8ed.jpeg 2x" data-dominant-color="9996C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">745×647 50.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="4">
<li>However, as soon as I turn off the ‘eye’ on the Thresholded segment, this is what remains of the Manual-slice-interpolated segment:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/863a24309aed980402f306d74a068deab91b16ee.png" data-download-href="/uploads/short-url/j9qxZPFhL6kGnDzxUi9VcVouFhY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/863a24309aed980402f306d74a068deab91b16ee_2_606x500.png" alt="image" data-base62-sha1="j9qxZPFhL6kGnDzxUi9VcVouFhY" width="606" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/863a24309aed980402f306d74a068deab91b16ee_2_606x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/863a24309aed980402f306d74a068deab91b16ee.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/863a24309aed980402f306d74a068deab91b16ee.png 2x" data-dominant-color="9E9ACF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">840×693 97 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>
<p>All of the intersections have been subtracted somehow and there is no way to refresh the 3D view or load the original model back into memory.<br>
If I save it in this state and reopen, the SAME PROBLEM persists (intersections have automatically been subtracted). The only thing I can do is hit ‘Undo’ until the Segment is restored to what it was.</p>
<p>Please help me out on this! It’s utterly frustrating and I haven’t been able to find a solution to this so far.</p>
<p>Thanks and Regards,<br>
Deba.</p>

---

## Post #2 by @chir.set (2022-09-24 19:56 UTC)

<p>Your second segment has eroded the first one, because you are using the default masking option.</p>
<p>You may use ‘Outside * segments’ for ‘Editable area’, or use ‘Allow overlap’ for ‘Modify other segments’. I still get caught with this after 10 years !</p>

---

## Post #3 by @SlicerDK (2022-09-29 13:20 UTC)

<p>Okay thank you so much! I do remember playing around with these, but I think I’ll have to properly understand what each of these settings actually do.</p>

---
