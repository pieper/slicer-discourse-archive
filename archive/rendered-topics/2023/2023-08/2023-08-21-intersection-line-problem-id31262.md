---
topic_id: 31262
title: "Intersection Line Problem"
date: 2023-08-21
url: https://discourse.slicer.org/t/31262
---

# Intersection line problem

**Topic ID**: 31262
**Date**: 2023-08-21
**URL**: https://discourse.slicer.org/t/intersection-line-problem/31262

---

## Post #1 by @icedream (2023-08-21 13:48 UTC)

<p>why the red intersection line is shorter than the others?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bd6c550cf2063fc81b5a4f7a9d6ff15452b4e86.jpeg" data-download-href="/uploads/short-url/hFwS8dvqOlgMsGeRVtJpImnTQ9g.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bd6c550cf2063fc81b5a4f7a9d6ff15452b4e86_2_690x402.jpeg" alt="image" data-base62-sha1="hFwS8dvqOlgMsGeRVtJpImnTQ9g" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bd6c550cf2063fc81b5a4f7a9d6ff15452b4e86_2_690x402.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bd6c550cf2063fc81b5a4f7a9d6ff15452b4e86_2_1035x603.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bd6c550cf2063fc81b5a4f7a9d6ff15452b4e86_2_1380x804.jpeg 2x" data-dominant-color="484854"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1431×835 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
can i use some code to make the red intersection line as long as others?</p>

---

## Post #2 by @pieper (2023-08-21 17:37 UTC)

<p>The slice intersection length is the size of the field of view (it will change size as you zoom in and out).  Maybe you want the basic crosshair instead.</p>

---

## Post #3 by @icedream (2023-08-22 08:27 UTC)

<p>thank you pieper , i change the field of view from 256 default to 128 or change 256 default to 512 ,like the picture below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/595849806c3ac6b75d7abed075eb67d7fc3e61cd.jpeg" data-download-href="/uploads/short-url/cKnEfj0Ov4Pic3arpESte72BaLH.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/595849806c3ac6b75d7abed075eb67d7fc3e61cd_2_690x416.jpeg" alt="image" data-base62-sha1="cKnEfj0Ov4Pic3arpESte72BaLH" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/595849806c3ac6b75d7abed075eb67d7fc3e61cd_2_690x416.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/595849806c3ac6b75d7abed075eb67d7fc3e61cd_2_1035x624.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/595849806c3ac6b75d7abed075eb67d7fc3e61cd_2_1380x832.jpeg 2x" data-dominant-color="74747F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1432×865 96.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/825e9a472bb0a4fcf2b6e9fffc8cc7959c342cd4.png" data-download-href="/uploads/short-url/iBiKTAOvDSEgw0C1FerYY9IV2gk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/825e9a472bb0a4fcf2b6e9fffc8cc7959c342cd4_2_690x406.png" alt="image" data-base62-sha1="iBiKTAOvDSEgw0C1FerYY9IV2gk" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/825e9a472bb0a4fcf2b6e9fffc8cc7959c342cd4_2_690x406.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/825e9a472bb0a4fcf2b6e9fffc8cc7959c342cd4_2_1035x609.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/825e9a472bb0a4fcf2b6e9fffc8cc7959c342cd4_2_1380x812.png 2x" data-dominant-color="373742"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1426×840 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
the right bottom red slice is shorter than the red slice left bottom</p>

---

## Post #4 by @icedream (2023-08-22 08:31 UTC)

<p>yes ,crosshair is fine,thank you!!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abbdd519aad6ae665b8c285d9240ef5bc1fe8a65.jpeg" data-download-href="/uploads/short-url/ovimpKpPJqjCaiQD2Z6YaV2NZuR.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abbdd519aad6ae665b8c285d9240ef5bc1fe8a65_2_690x399.jpeg" alt="image" data-base62-sha1="ovimpKpPJqjCaiQD2Z6YaV2NZuR" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abbdd519aad6ae665b8c285d9240ef5bc1fe8a65_2_690x399.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abbdd519aad6ae665b8c285d9240ef5bc1fe8a65_2_1035x598.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abbdd519aad6ae665b8c285d9240ef5bc1fe8a65_2_1380x798.jpeg 2x" data-dominant-color="494953"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1437×832 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @slicer365 (2023-08-22 14:19 UTC)

<p>Recently, we have also encountered this problem.</p>
<p>Our customers have asked to spread these three wires all over the window.</p>
<p>We can replace this through crosshair, but croosshair does not support rotation.</p>
<p>In the old version, we also need to operate together through shortcut keys and mouse.</p>
<p>Do you have a way to spread the three wires of MPR all over the window directly?</p>
<p>we have rebuilt the source code of slicer</p>
<p>thank you.</p>
<p>like this<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/618fbc047b0774a3c7738cec2e276a330a08555b.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/618fbc047b0774a3c7738cec2e276a330a08555b.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/618fbc047b0774a3c7738cec2e276a330a08555b.mp4</a>
    </video>
  </div><p></p>

---
