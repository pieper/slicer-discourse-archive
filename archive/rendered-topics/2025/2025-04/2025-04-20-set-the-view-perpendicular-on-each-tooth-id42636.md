---
topic_id: 42636
title: "Set The View Perpendicular On Each Tooth"
date: 2025-04-20
url: https://discourse.slicer.org/t/42636
---

# Set the view perpendicular on each tooth

**Topic ID**: 42636
**Date**: 2025-04-20
**URL**: https://discourse.slicer.org/t/set-the-view-perpendicular-on-each-tooth/42636

---

## Post #1 by @Yasser_Ahmad (2025-04-20 19:54 UTC)

<p>I have a 3D dental model which I can rotate in infinite directions and angles. But, I want to be able to set a view where I will be looking directly at the facial surface of each tooth</p>
<p>What I’ve tried to do is:</p>
<ol>
<li>
<p>Draw a cuve (polynomial worked well to draw a 2D curve on the occlusal plane)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24a39e246b0568c64d5ecc2b090751a7abf44aef.jpeg" data-download-href="/uploads/short-url/5e7JM9IThMzmpUJpeCYs3HLQl3N.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24a39e246b0568c64d5ecc2b090751a7abf44aef_2_609x500.jpeg" alt="image" data-base62-sha1="5e7JM9IThMzmpUJpeCYs3HLQl3N" width="609" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24a39e246b0568c64d5ecc2b090751a7abf44aef_2_609x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24a39e246b0568c64d5ecc2b090751a7abf44aef.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24a39e246b0568c64d5ecc2b090751a7abf44aef.jpeg 2x" data-dominant-color="B8B2B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">769×631 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Put a plane vertically to intersect that curve at the center of each tooth, hopefully close to 90 degrees<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb8f03a0de8d4e9dbecfe2be0af2967975e4f6d9.jpeg" data-download-href="/uploads/short-url/zTofAU6sMWrq3UqVlynrxyknoLf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb8f03a0de8d4e9dbecfe2be0af2967975e4f6d9_2_427x500.jpeg" alt="image" data-base62-sha1="zTofAU6sMWrq3UqVlynrxyknoLf" width="427" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb8f03a0de8d4e9dbecfe2be0af2967975e4f6d9_2_427x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb8f03a0de8d4e9dbecfe2be0af2967975e4f6d9_2_640x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb8f03a0de8d4e9dbecfe2be0af2967975e4f6d9.jpeg 2x" data-dominant-color="A09CB9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">648×758 72.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Rotate the screen or model until the plane becomes a line so that I’m sure I’m looking directly perpendicular on the tooth<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6cec82773d5d0fb642ac196d5a26194cfb0af790.png" data-download-href="/uploads/short-url/fxAhKL7UCSDAUxdRwg57IVwhoCA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6cec82773d5d0fb642ac196d5a26194cfb0af790_2_423x500.png" alt="image" data-base62-sha1="fxAhKL7UCSDAUxdRwg57IVwhoCA" width="423" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6cec82773d5d0fb642ac196d5a26194cfb0af790_2_423x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6cec82773d5d0fb642ac196d5a26194cfb0af790.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6cec82773d5d0fb642ac196d5a26194cfb0af790.png 2x" data-dominant-color="9E9DC7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">583×689 72.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>what I am looking for is a simple way to set the view perpendicular on each tooth to evaluate its axis on two models superimposed</p>
<p>And I want to follow this method showed here but in 3D Slicer<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c0811bd496fe3cd198a3c049eb5f7cf670c4741.jpeg" data-download-href="/uploads/short-url/8z3W4kzgxhDEgboriBg7MXmedoJ.jpeg?dl=1" title="Perpendicular lines to arch curve" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c0811bd496fe3cd198a3c049eb5f7cf670c4741_2_690x355.jpeg" alt="Perpendicular lines to arch curve" data-base62-sha1="8z3W4kzgxhDEgboriBg7MXmedoJ" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c0811bd496fe3cd198a3c049eb5f7cf670c4741_2_690x355.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c0811bd496fe3cd198a3c049eb5f7cf670c4741.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c0811bd496fe3cd198a3c049eb5f7cf670c4741.jpeg 2x" data-dominant-color="373836"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Perpendicular lines to arch curve</span><span class="informations">850×438 49.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you in advance</p>

---

## Post #2 by @chir.set (2025-04-21 12:56 UTC)

<p>May be <code>Cross section analysis</code> module in <code>SlicerVMTK</code> extension could help you. I broadly understand that you might be looking for reslicing along a markups curve.</p>

---
