# Exporting surface model after applying transformation

**Topic ID**: 39935
**Date**: 2024-10-30
**URL**: https://discourse.slicer.org/t/exporting-surface-model-after-applying-transformation/39935

---

## Post #1 by @mdhan (2024-10-30 13:05 UTC)

<p>Hello, I am having trouble with some features of Slicer, and would be grateful for advice. Images are copied for reference.</p>
<p>I have 3 models - 1) Initial (Green), 2) Final (Yellow), 3) Shell (Purple)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0305ee9e773b6adcf77ccc224a7c45f157bf277c.jpeg" data-download-href="/uploads/short-url/qK8Nq3VAnPqmnXPRk5mq55oh3e.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/0305ee9e773b6adcf77ccc224a7c45f157bf277c_2_690x441.jpeg" alt="image" data-base62-sha1="qK8Nq3VAnPqmnXPRk5mq55oh3e" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/0305ee9e773b6adcf77ccc224a7c45f157bf277c_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0305ee9e773b6adcf77ccc224a7c45f157bf277c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0305ee9e773b6adcf77ccc224a7c45f157bf277c.jpeg 2x" data-dominant-color="9493B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">954×611 74.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What I am trying to do is to transform the “Initial” (Green) to match “Final” (Yellow), and apply that transformation to “Shell” (Purple). I used SlicerCMF’s surface-based registration feature for this, and when I applied the transformation to the “Shell” (Purple), it worked exactly as I had intended (here the transformation matrix is named “SurfaceReg”).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc4cf0a0539c42b3c2c0925a22e931cba97146c2.jpeg" data-download-href="/uploads/short-url/zZXagFNLCAKO4AkvktfI5DHMj3I.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc4cf0a0539c42b3c2c0925a22e931cba97146c2_2_689x211.jpeg" alt="image" data-base62-sha1="zZXagFNLCAKO4AkvktfI5DHMj3I" width="689" height="211" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc4cf0a0539c42b3c2c0925a22e931cba97146c2_2_689x211.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc4cf0a0539c42b3c2c0925a22e931cba97146c2_2_1033x316.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc4cf0a0539c42b3c2c0925a22e931cba97146c2.jpeg 2x" data-dominant-color="A19AB8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1290×395 99.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7aa4006838e940e0522a508eb6e0e0d0e77d637a.png" data-download-href="/uploads/short-url/huVCDvBkb92GUQW44YIXwxuOWwy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7aa4006838e940e0522a508eb6e0e0d0e77d637a_2_690x482.png" alt="image" data-base62-sha1="huVCDvBkb92GUQW44YIXwxuOWwy" width="690" height="482" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7aa4006838e940e0522a508eb6e0e0d0e77d637a_2_690x482.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7aa4006838e940e0522a508eb6e0e0d0e77d637a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7aa4006838e940e0522a508eb6e0e0d0e77d637a.png 2x" data-dominant-color="B7B6D4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">908×635 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But when I export the “Shell” (Purple), and open it in another software (Meshmixer), it give me the original, untransformed model. Here, “Shell” is in brown.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0e1637414d7c9f1c5d63dc89d803a45cefbbdf2.jpeg" data-download-href="/uploads/short-url/tNQcNEFB4nRCtUUTp643c4d4e8q.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0e1637414d7c9f1c5d63dc89d803a45cefbbdf2_2_690x386.jpeg" alt="image" data-base62-sha1="tNQcNEFB4nRCtUUTp643c4d4e8q" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0e1637414d7c9f1c5d63dc89d803a45cefbbdf2_2_690x386.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0e1637414d7c9f1c5d63dc89d803a45cefbbdf2_2_1035x579.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0e1637414d7c9f1c5d63dc89d803a45cefbbdf2.jpeg 2x" data-dominant-color="E0DDDE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1120×627 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Again, I would be really grateful for any advice. Thank you!!</p>

---

## Post #2 by @pieper (2024-10-30 13:18 UTC)

<p>Did you harden the transform before exporting?</p>

---

## Post #3 by @mdhan (2024-10-30 14:48 UTC)

<p>That worked perfectly - embarrassingly, I did not know that feature. Thank you so much, and sorry to clutter the forum with such an amateur question!!</p>

---

## Post #4 by @cpinter (2024-10-31 10:40 UTC)

<p>No need to apologize, this is not trivial I think. But I cannot think of a good way to facilitate this. Maybe a popup asking about hardening on save, but the saving mechanism is not really designed to incorporate such warnings. Maybe there could be an option in the save dialog in the row of the model (if not there already), but it’s really not visible. Hopefully others with the same problem will find this topic.</p>

---
