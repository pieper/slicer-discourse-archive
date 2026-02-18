# Bone Surface Ultrasound Simulation Image

**Topic ID**: 10675
**Date**: 2020-03-13
**URL**: https://discourse.slicer.org/t/bone-surface-ultrasound-simulation-image/10675

---

## Post #1 by @hripat (2020-03-13 15:59 UTC)

<p>Hello,</p>
<p>I’m trying to use Slicer to get simulated ultrasound images of femur and radius STL files. However, the ultrasound bone surface images only come up when the transducer is almost touching the bone model. I was wondering if this is supposed to happen? Shouldn’t the US images come up when the transducer is above the gel block?</p>
<p>Also, the femur model doesn’t show the bone surface line on the ultrasound (2nd image). I don’t know why that is happening either. I am using the acoustic properties of the bone in the Plus server file.</p>
<p>Thank you for any help.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20c581652a8be497d01ebed5651fb243cb8c7cd9.png" data-download-href="/uploads/short-url/4FUqODPNrOVM6Y1N9ETvBQwDoyR.png?dl=1" title="radius" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20c581652a8be497d01ebed5651fb243cb8c7cd9_2_277x500.png" alt="radius" data-base62-sha1="4FUqODPNrOVM6Y1N9ETvBQwDoyR" width="277" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20c581652a8be497d01ebed5651fb243cb8c7cd9_2_277x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20c581652a8be497d01ebed5651fb243cb8c7cd9_2_415x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20c581652a8be497d01ebed5651fb243cb8c7cd9.png 2x" data-dominant-color="51535E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">radius</span><span class="informations">490×882 81.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-03-18 03:30 UTC)

<aside class="quote no-group" data-username="hripat" data-post="1" data-topic="10675">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/5f8ce5/48.png" class="avatar"> hripat:</div>
<blockquote>
<p>the ultrasound bone surface images only come up when the transducer is almost touching the bone model. I was wondering if this is supposed to happen?</p>
</blockquote>
</aside>
<p>The image should appear when the transducer touches the gel block’s surface. If this is not the case then check the Plus device set configuration file.</p>
<p>You can post on the <a href="https://github.com/PlusToolkit/PlusLib/issues">Plus issue tracker</a> if you cannot figure out what’s wrong with the configuration file.</p>

---
