---
topic_id: 47396
title: "Measuring diameter of mouse lung airway"
date: 2026-06-19
url: https://discourse.slicer.org/t/47396
last_bumped: 2026-06-20T03:56:15.163Z
---

# Measuring diameter of mouse lung airway

**Topic ID**: 47396
**Date**: 2026-06-19
**URL**: https://discourse.slicer.org/t/measuring-diameter-of-mouse-lung-airway/47396

---

## Post #1 by @ljuno (2026-06-19 20:40 UTC)

<p>Hi all,</p>
<p>I have created this segmentation of part of the airways of a mouse lung. The images were generated from lightsheet microscopy and I used various tools to segment them - thresholding, painting, etc. I eventually ended up with this (which is just a small portion of the whole lung I segmented), which shows one airway leading to a TB lesion. I am hoping to measure the diameter of multiple airways from this lung to see how they change in diameter as the airway moves from the main branch near the trachea to the periphery (or in this case as it moves from the main branches and terminates in the lesion). Does anyone have any suggestions for how to measure the diameter of an object like this? Thank you very much in advance!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/0598cd7efd9e77c990c30fd224779ebd7004daf7.jpeg" data-download-href="/uploads/short-url/NvLte4BuJCV5bHVOyBfbUZJDIb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0598cd7efd9e77c990c30fd224779ebd7004daf7_2_616x500.jpeg" alt="image" data-base62-sha1="NvLte4BuJCV5bHVOyBfbUZJDIb" width="616" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0598cd7efd9e77c990c30fd224779ebd7004daf7_2_616x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0598cd7efd9e77c990c30fd224779ebd7004daf7_2_924x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/0598cd7efd9e77c990c30fd224779ebd7004daf7.jpeg 2x" data-dominant-color="9597CD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1176×954 99.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @chir.set (2026-06-19 20:47 UTC)

<p><code>ExtractCenterline</code> and <code>CrossSectionAnalysis</code> modules of the <code>SlicerVMTK</code> extension should be helpful. You can install it in the <code>Extensions manager</code>.</p>

---

## Post #3 by @ljuno (2026-06-19 23:49 UTC)

<p>Hi,</p>
<p>Thank you very much for your suggestion. I installed the VMTK extension and have started to try to make my centerline. For reference, here is the picture of my full lung segmentation. I don’t need to get a diameter for every single airway so I took a crop of the segmentation to run through the VMTK module to hopefully make it go a little faster. I wasn’t sure how to set my endpoints since it’s not like a vessel where I would want to dictate the direction of flow (at least after reading the github page I think that is what the endpoints are for?)</p>
<p>In my cropped sample I just put one markup point at one edge of the airway and another point at the branching junction, I did surface = my segmentation, and then network model = create new model. Is this correct to get it started?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/6807bd135818883e336703bae22f2cf2614c5804.jpeg" data-download-href="/uploads/short-url/eQieG4cFMBQ0OfNoSfDD6kgkAaE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/6807bd135818883e336703bae22f2cf2614c5804_2_639x500.jpeg" alt="image" data-base62-sha1="eQieG4cFMBQ0OfNoSfDD6kgkAaE" width="639" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/6807bd135818883e336703bae22f2cf2614c5804_2_639x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/6807bd135818883e336703bae22f2cf2614c5804_2_958x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/6807bd135818883e336703bae22f2cf2614c5804.jpeg 2x" data-dominant-color="8386C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1232×964 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @chir.set (2026-06-20 03:56 UTC)

<aside class="quote no-group" data-username="ljuno" data-post="3" data-topic="47396">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/59ef9b/48.png" class="avatar"> ljuno:</div>
<blockquote>
<p>so I took a crop of the segmentation</p>
</blockquote>
</aside>
<p>Very good step. The more so that some distal parts do not seem completely tubular.</p>
<aside class="quote no-group" data-username="ljuno" data-post="3" data-topic="47396">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/59ef9b/48.png" class="avatar"> ljuno:</div>
<blockquote>
<p>network model = create new model</p>
</blockquote>
</aside>
<p>The centerline in <code>Network mode</code> is calculated from the geometry of the input surface. It will always succeed and is always fast. It does not need endpoints and will be bifurcated if the input is bifurcated.</p>
<p>We usually use <code>Tree mode</code>. It is calculated from the largest sphere that could be determined inside the surface at any point (<code>maximum inscribed sphere</code> in <code>VMTK</code>’s terminology). It can be better controlled with the endpoints.</p>
<aside class="quote no-group" data-username="ljuno" data-post="3" data-topic="47396">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/59ef9b/48.png" class="avatar"> ljuno:</div>
<blockquote>
<p>I wasn’t sure how to set my endpoints</p>
</blockquote>
</aside>
<p>The centerline is calculated in the order in which the endpoints were placed indeed. But you can force one point to be the starting point by unselecting it: right click, or go to the <code>Markups module</code> for that.</p>

---
