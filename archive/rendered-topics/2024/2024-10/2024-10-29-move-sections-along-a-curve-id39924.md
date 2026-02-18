# Move sections along a curve

**Topic ID**: 39924
**Date**: 2024-10-29
**URL**: https://discourse.slicer.org/t/move-sections-along-a-curve/39924

---

## Post #1 by @mohammed_alshakhas (2024-10-29 15:46 UTC)

<p>i want move my volume around curve to evaluate bone in this specific orientation .</p>
<p>is there a way i can do that ?<br>
thanks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b76e2fc4946f1c88b6a292af1e233ce1331d6a1.jpeg" data-download-href="/uploads/short-url/aLAwtq1GIcqm8tuOiWc6V1AVYtj.jpeg?dl=1" title="Screenshot 2024-10-29 at 18.39.33" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b76e2fc4946f1c88b6a292af1e233ce1331d6a1_2_645x500.jpeg" alt="Screenshot 2024-10-29 at 18.39.33" data-base62-sha1="aLAwtq1GIcqm8tuOiWc6V1AVYtj" width="645" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b76e2fc4946f1c88b6a292af1e233ce1331d6a1_2_645x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b76e2fc4946f1c88b6a292af1e233ce1331d6a1_2_967x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b76e2fc4946f1c88b6a292af1e233ce1331d6a1_2_1290x1000.jpeg 2x" data-dominant-color="535050"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-10-29 at 18.39.33</span><span class="informations">1434×1110 72.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2024-10-29 16:13 UTC)

<p>You mean you want to create a panorma image using the volume and the curve?</p>
<p>If so, please try the “Cuved Planar Reformat” module in the Sandbox extension.</p>

---

## Post #3 by @mohammed_alshakhas (2024-10-29 17:51 UTC)

<p>not exactly , i meant insteaa sagittal follwoing a straight line , it follow a curved line as in the pic .<br>
the idea is that to be prependivular tp the teeth/bone in each view .</p>

---

## Post #4 by @chir.set (2024-10-29 18:45 UTC)

<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="3" data-topic="39924">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>follow a curved line</p>
</blockquote>
</aside>
<p>You may consider the ‘Cross-section analysis’ module in the ‘SlicerVMTK’ extension.</p>

---
