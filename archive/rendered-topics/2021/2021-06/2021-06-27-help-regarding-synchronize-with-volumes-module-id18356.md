---
topic_id: 18356
title: "Help Regarding Synchronize With Volumes Module"
date: 2021-06-27
url: https://discourse.slicer.org/t/18356
---

# Help regarding "Synchronize with Volumes module"

**Topic ID**: 18356
**Date**: 2021-06-27
**URL**: https://discourse.slicer.org/t/help-regarding-synchronize-with-volumes-module/18356

---

## Post #1 by @pranaysingh (2021-06-27 17:26 UTC)

<p>Hi,<br>
I am trying to do volume rendering of my dicom dataset. I want it to render the object with exact intensity values of the voxels, for this I was suggested “Synchronize with Volumes module” on community, which I did after reading the documentation of volume rendering module. But I am still clueless about a few things regarding the various settings on the module. On the 1st photo attached, you can see the volume rendered originally.<br>
After checking the box of “Synchronize with Volumes module” the volume changed to this as shown in 2nd picture attached along with scalar and color transfer function on the left. I wanted to understand the “Scalar opacity mapping” given on the left pane, basically I want to create a Step function for opacity where below a certain threshold I want all the pixels to be transparent(those will be dark color noise pixel surrounding the tooth as shown in picture) and all the pixels above that threshold would be opaque. How can I achieve that with the given settings panel on the left ?<br>
Secondly, regarding the “Scaler color mapping” setting, there I can see 6 points which are distributed across the intensity of the object, can we just shift the points manually? like I want point number 0 to be shifted a little ahead which is presently at zero.</p>
<p>Kindly help me understand how can I make use of this feature to view my object with accurate and original intensity. I am also attaching the snipped of 3D slicer volume rendering documentation I referred to.</p>
<p>Thanks,<br>
Pranay</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a23d31bc315ffe67a182552a36fe509628aedf68.png" data-download-href="/uploads/short-url/n9espTfswvJGKNgoX7BOwUipgAo.png?dl=1" title="ss3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a23d31bc315ffe67a182552a36fe509628aedf68_2_690x461.png" alt="ss3" data-base62-sha1="n9espTfswvJGKNgoX7BOwUipgAo" width="690" height="461" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a23d31bc315ffe67a182552a36fe509628aedf68_2_690x461.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a23d31bc315ffe67a182552a36fe509628aedf68_2_1035x691.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a23d31bc315ffe67a182552a36fe509628aedf68.png 2x" data-dominant-color="B4B4BD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ss3</span><span class="informations">1049×702 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/867aa34719c6c2bedc39bf6fe696f769035eea3f.png" data-download-href="/uploads/short-url/jbEJlcGis70jHuaxW4LQUFgGjmf.png?dl=1" title="ss1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/867aa34719c6c2bedc39bf6fe696f769035eea3f_2_690x461.png" alt="ss1" data-base62-sha1="jbEJlcGis70jHuaxW4LQUFgGjmf" width="690" height="461" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/867aa34719c6c2bedc39bf6fe696f769035eea3f_2_690x461.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/867aa34719c6c2bedc39bf6fe696f769035eea3f_2_1035x691.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/867aa34719c6c2bedc39bf6fe696f769035eea3f.png 2x" data-dominant-color="AEAFB6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ss1</span><span class="informations">1049×702 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/905ecf70769e5c2706b5d98de511c59911fb66d5.png" data-download-href="/uploads/short-url/kB9SVnXJhWvfftjMpjyQz8INVRz.png?dl=1" title="ss2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/905ecf70769e5c2706b5d98de511c59911fb66d5.png" alt="ss2" data-base62-sha1="kB9SVnXJhWvfftjMpjyQz8INVRz" width="690" height="481" data-dominant-color="EDEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ss2</span><span class="informations">742×518 31.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-06-27 19:15 UTC)

<aside class="quote no-group" data-username="pranaysingh" data-post="1" data-topic="18356">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pranaysingh/48/10876_2.png" class="avatar"> pranaysingh:</div>
<blockquote>
<p>I want to create a Step function for opacity where below a certain threshold I want all the pixels to be transparent(those will be dark color noise pixel surrounding the tooth as shown in picture) and all the pixels above that threshold would be opaque. How can I achieve that with the given settings panel on the left ?</p>
</blockquote>
</aside>
<p>You can move the points of all transfer functions by drag-and-drop. You can also choose a point index (<code>Point</code>) above the transfer function plot and enter intensity (<code>X</code>) and opacity (<code>O</code>) values.</p>
<p>Note that the intensity values on screen will be different in slice and 3D views due to shading (lighting). If you turn off shading (in Advanced section) then the volume will not look like a 3D object anymore.</p>
<p>What would you like to achieve?</p>

---

## Post #3 by @pranaysingh (2021-06-30 05:09 UTC)

<p>Hi,</p>
<p>Thanks, your suggestion helped understanding things alot, especially drag and drop of points.<br>
I need to understand what I am now seeing, basically regarding the scalar opacity mapping function… From what my understanding is, it is a transfer function for opacity, and therefore I wanted to create a step function where under a certain threshold I can see the object completely (in original intensity ) and below that Everything is transparent, that I created successfully by dragging points in the map.<br>
But i see when the map is linear and not step, it is able to preserve the shades and difference is contrast in the rendered volume, and when the map is step, it just displays the whole black object.<br>
Now from what I understand, it should have shown me the object in original contrast(if not color) when the function is step, while what it is doing is when I am making the opacity mapping a linear function I am able to see exact contrast in my object at right places. How does linear mapping shows contrast and step mapping does not??</p>

---

## Post #4 by @lassoan (2021-06-30 05:11 UTC)

<p>In slice views, the volume is displayed using a linear ramp (value*scale+offset). Step function would correspond to thresholding.</p>

---

## Post #5 by @pranaysingh (2021-06-30 06:53 UTC)

<p>Pardon me, could you please tell what value, scale and offset are in our context ?<br>
Is there any documentation i can refer to for this ?</p>

---

## Post #6 by @lassoan (2021-07-01 16:28 UTC)

<p>I just meant that the window/level or min/max values that you set in Volumes module are ultimately translated to a linear scaling and offset (with clipping to the displayable scalar range of 0-255).</p>

---

## Post #7 by @pranaysingh (2021-07-14 06:52 UTC)

<p>So, I have to keep the opacity transfer function linear or step ? To view some voxels completely and hide others completely.</p>

---

## Post #8 by @lassoan (2021-07-15 03:48 UTC)

<p>I don’t know what your goal with the 3D visualization is. If you want to see the exact same intensities in 3D view as in 2D then click the “Synchronize with volumes module” button, disable shading, and set the scalar opacity to 1.0 everywhere. However this would result in quite boring 3D visualization - a black cube. If you cut into it using cropping then you’ll see the exact same intensity values as in slice views.</p>
<p>You can crop away the black box or the cylinder by setting scalar opacity to 0 below a certain intensity and leave 1.0 elsewhere (step function). Then the voxels that remain visible are still displayed with the exact same intensity in 2D and 3D views. You may see artifacts at the boundary that you may soften by using a ramp instead of a step function - but in this case at the boundary you won’ see exactly the same voxel values as in slice views, because there will be some some-transparent voxels at the boundary.</p>
<p>If you want to further reduce artifacts at the boundary or just want to be able to see inside the volume then you can reduce the opacity from 1.0 to 0.5 or 0.2 or even smaller value. Then at each pixel position you will see a mix of many voxels of the original volume, so it won’t be the same as what you see in slice views.</p>
<p>If you want to give more depth perception then you could enable shading, and to allow users to more easily distinguish different tissue types then you could add some colors to the color transfer functions. These of course would make the 3D rendering look even more different from slice views.</p>

---
