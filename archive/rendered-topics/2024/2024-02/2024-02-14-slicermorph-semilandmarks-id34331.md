---
topic_id: 34331
title: "Slicermorph Semilandmarks"
date: 2024-02-14
url: https://discourse.slicer.org/t/34331
---

# SlicerMorph - semilandmarks

**Topic ID**: 34331
**Date**: 2024-02-14
**URL**: https://discourse.slicer.org/t/slicermorph-semilandmarks/34331

---

## Post #1 by @Katya_Stansfield (2024-02-14 16:40 UTC)

<p>Hello –</p>
<p>may I ask for help with semilandmark projection using either Alpaca or ProjectSemiLM. I have fairly simple surface objects so that Alpaca struggles to superimpose meshes without errors. Sometime it works just fine but not always. In some cases surfaces flip. I tried to use ProjectSemiLM module (having introduced some fixed lm points specifically for that) but the module does not run. I am stuck. May I please ask:</p>
<pre><code>is there any way I can control surface superimposition process in Alpaca?
is ther anything I am missing in ProjectSemiLM in terms of file setup? I have exported my landmark and semilandmarks into fcsv format, stored the template and target surfaces in the same folder, as well as fixed landmarks (with the names as in surfaces) and the semilandmarks (also in fcsv but a different name). The order and names of fixed landmarks is correct.
</code></pre>
<p>I am happy to tinker with Python code, if there is an option to hack into the brains of the SlicerMorph.</p>
<p>Look forward to hearing from you,<br>
With best wishes<br>
Katya Stansfield<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aea859ebfcf84a96f7537f8cddb57c4ab245f607.png" data-download-href="/uploads/short-url/oV5LMOqckAHCEXL5HqXFdnPPcP5.png?dl=1" title="Screenshot 2024-02-14 174239" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aea859ebfcf84a96f7537f8cddb57c4ab245f607_2_690x445.png" alt="Screenshot 2024-02-14 174239" data-base62-sha1="oV5LMOqckAHCEXL5HqXFdnPPcP5" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aea859ebfcf84a96f7537f8cddb57c4ab245f607_2_690x445.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aea859ebfcf84a96f7537f8cddb57c4ab245f607_2_1035x667.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aea859ebfcf84a96f7537f8cddb57c4ab245f607_2_1380x890.png 2x" data-dominant-color="C0BACA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-02-14 174239</span><span class="informations">2694×1738 759 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/774e852069e4fd23609415d0ee87b0fd5c096bb1.jpeg" data-download-href="/uploads/short-url/h1r2W3UN037z5gJ5xGakpFSBB7j.jpeg?dl=1" title="Screenshot 2024-02-14 174827" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/774e852069e4fd23609415d0ee87b0fd5c096bb1_2_690x411.jpeg" alt="Screenshot 2024-02-14 174827" data-base62-sha1="h1r2W3UN037z5gJ5xGakpFSBB7j" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/774e852069e4fd23609415d0ee87b0fd5c096bb1_2_690x411.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/774e852069e4fd23609415d0ee87b0fd5c096bb1_2_1035x616.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/774e852069e4fd23609415d0ee87b0fd5c096bb1_2_1380x822.jpeg 2x" data-dominant-color="C4BCD2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-02-14 174827</span><span class="informations">1920×1146 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-02-14 18:23 UTC)

<p>Can you share an example dataset? It is a little hard to tell what’s going on from the screen captures.</p>
<p>also I will need the fixed landmarks to test the issue with the ProjectSemiLMs module.</p>
<p>Your two surface are too similar, and there is not much difference top from the bottom. This is actually a fairly challenging registration problem, and I am not surprised occasssionally things are flipped upside down. perhaps increasing the point cloud sampling would help, but hard for me to make suggestions without seeing the data.</p>
<p>So if you can upload those two models, their corresponding points and the template you want to transfer as a zip file to a cloud file share (google drive, onedrive, dropbox etc), and share the link, I can try to take a look</p>

---

## Post #3 by @agporto (2024-02-14 18:30 UTC)

<p>Just to echo Murat and add some additional insight. Having a dataset would be helpful in figuring out how to improve ALPACA registration. In my experience, when surfaces are flat or homogeneously round, it is hard to find geometric correspondences. One strategy that has worked for me in the past is to increase the Normal Search Radius and FPFH Search Radius in the Advanced Settings (e.g., doubling them). Essentially, you want to use broader (area-wise) geometric descriptors.</p>

---

## Post #4 by @nsvitek (2025-04-23 18:11 UTC)

<p>Different dataset, related question: Is there a limit on ALPACA working with completely flat surfaces? I’ve been trying to explore its use on samples like this one (<a href="https://drive.google.com/drive/folders/1Hbmaej2Ztiv3lJOyKNhFJI3KygPKSCXr?usp=sharing" rel="noopener nofollow ugc">example files</a>), but ALPACA crashes when attempting to align.</p>
<p>I can project semiLM (with associated fixed landmarks) with moderate success, but I’m wondering if there is any a priori reason why these flat surfaces <em>can’t</em> work, or if there is something in particular about my dataset/situation.</p>

---

## Post #5 by @muratmaga (2025-04-23 18:43 UTC)

<p>We never considered such a use case. It crashes for me too. I am sure all points being co-planar creates all sorts of issues. Unfortunately, we do not have time to chase this. Unless <a class="mention" href="/u/agporto">@agporto</a> has…</p>
<p>M</p>

---

## Post #6 by @agporto (2025-04-23 19:13 UTC)

<p>ALPACA uses FPFH features to find the initial rough alignment between objects. FPFH relies on curvature variation. So, when matching two models, you look for points whose FPFH vectors are similar. On a flat area, <em>every</em> point looks equally similar (no curvature variation), so RANSAC or any matching algorithm has no cue to pick the correct correspondences. If you are working with 2d masks (as seem to be the case), you are better off using 2D approaches.</p>

---
