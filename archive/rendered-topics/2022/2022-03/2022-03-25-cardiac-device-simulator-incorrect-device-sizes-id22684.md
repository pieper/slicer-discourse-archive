# Cardiac Device Simulator - incorrect device sizes

**Topic ID**: 22684
**Date**: 2022-03-25
**URL**: https://discourse.slicer.org/t/cardiac-device-simulator-incorrect-device-sizes/22684

---

## Post #1 by @SassanHashemi (2022-03-25 17:04 UTC)

<p>Slicer 4.30.0<br>
Windows 10<br>
Core i7-7700H</p>
<p>Hi,</p>
<p>I noticed the size of Harmony device is quite different between what the sliders on the left say and the actual size on the dicoms as shown in the attached picture. Measurements of the cardiac structures on dicoms are accurate, so I am confused about the cause of this.</p>
<p>I really appreciate any help.</p>
<p>Sassan<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/293c20bc9ced336933481722d3fd39fcd4473290.jpeg" data-download-href="/uploads/short-url/5SMoMlfeuAcHIw3qZeOS0yWgTbG.jpeg?dl=1" title="slicer device simulator" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/293c20bc9ced336933481722d3fd39fcd4473290_2_690x388.jpeg" alt="slicer device simulator" data-base62-sha1="5SMoMlfeuAcHIw3qZeOS0yWgTbG" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/293c20bc9ced336933481722d3fd39fcd4473290_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/293c20bc9ced336933481722d3fd39fcd4473290_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/293c20bc9ced336933481722d3fd39fcd4473290.jpeg 2x" data-dominant-color="656378"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer device simulator</span><span class="informations">1296×729 86.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-03-25 22:47 UTC)

<p>Everything looks good. You specified a <em>radius</em> with the slider and then measured the <em>diameter</em>, which is expected to be 2x larger. In most other devices we use diameter to avoid this confusion but for some reason we kept using radius values for the Harmony device.</p>

---

## Post #3 by @SassanHashemi (2022-03-25 23:03 UTC)

<p>My bad! I am just not used to using radius I suppose.</p>
<p>Thanks you.</p>
<p>Sassan</p>

---
