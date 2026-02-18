# Is there a way to change the ROI to a sphere

**Topic ID**: 15650
**Date**: 2021-01-25
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-change-the-roi-to-a-sphere/15650

---

## Post #1 by @slicer365 (2021-01-25 11:10 UTC)

<p>As this picture shows, the ROI is a cube, and sometimes it may be better to change it to a sphere. Of course, this function PRISM rendering can be implemented, but it will be more convenient if you can directly adjust the ROI. Or is there a corresponding script code to achieve<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7153ba8f7bf2c32fcf92524f8c692b0694a7b545.jpeg" data-download-href="/uploads/short-url/gaxldm6UtUd4LZgsF6F8Hj9vUqx.jpeg?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7153ba8f7bf2c32fcf92524f8c692b0694a7b545_2_690x353.jpeg" alt="捕获" data-base62-sha1="gaxldm6UtUd4LZgsF6F8Hj9vUqx" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7153ba8f7bf2c32fcf92524f8c692b0694a7b545_2_690x353.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7153ba8f7bf2c32fcf92524f8c692b0694a7b545_2_1035x529.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7153ba8f7bf2c32fcf92524f8c692b0694a7b545.jpeg 2x" data-dominant-color="ABABAF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">1365×699 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @lassoan (2021-04-27 18:52 UTC)

<p>Right now you need to create a custom markup node for this, but we plan to provide ellipsoid ROI shape in the near future.</p>

---

## Post #4 by @slicer365 (2021-04-28 00:20 UTC)

<p>I believe this change is very meaningful，as a neurosurgeon, I often use slicer for surgical planning.This function should be needed by many clinicians.Thank you very much to the team of Dr. Andras Lasso. <img src="https://emoji.discourse-cdn.com/twitter/100.png?v=9" title=":100:" class="emoji" alt=":100:"></p>

---

## Post #5 by @lassoan (2021-04-28 01:07 UTC)

<p>What would you use the ellipsoid ROI for?</p>
<p>You can already paint an arbitrary shape region to hide certain parts of the volume from volume rendering.</p>

---

## Post #6 by @slicer365 (2021-04-28 02:41 UTC)

<p>For example, brain surgery incisions are often oval or irregular. If I use a cube ROI, this kind of simulated incision is not very realistic. In addition, we hope that the area inside the ROI can be hidden, so that the internal situation can be seen in real time. Of course, this function can be achieved through PRISM，This function is really necessary for many neurosurgeons.Currently we are more dependent on Volume Rendering than PRISM.<br>
Just like the picture above, if I want to make a circular surgical skull incision, there are many methods, but my purpose is to hide the skull inside ROI so that I can observe the internal structure of the skull. However, currently ROI is to show the selected area instead of hiding it.</p>

---

## Post #7 by @muratmaga (2021-04-28 04:35 UTC)

<p>You might find the VolumeRenderingSpecialEffects module in Sandbox extension easier to use then PRISM. It just uses regular volume rendering.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c8c9eb30c066ea085f2669ff44bb7d91bcc86fd.jpeg" data-download-href="/uploads/short-url/1N10oJhZxN3z07Txqi8ewTv8srP.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c8c9eb30c066ea085f2669ff44bb7d91bcc86fd_2_667x500.jpeg" alt="image" data-base62-sha1="1N10oJhZxN3z07Txqi8ewTv8srP" width="667" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c8c9eb30c066ea085f2669ff44bb7d91bcc86fd_2_667x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c8c9eb30c066ea085f2669ff44bb7d91bcc86fd_2_1000x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c8c9eb30c066ea085f2669ff44bb7d91bcc86fd.jpeg 2x" data-dominant-color="ACADAD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1006×753 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @slicer365 (2021-04-28 06:19 UTC)

<p>Yeah,it is very convenient.Thank you very much! <img src="https://emoji.discourse-cdn.com/twitter/ok_hand.png?v=9" title=":ok_hand:" class="emoji" alt=":ok_hand:"></p>

---

## Post #9 by @lassoan (2021-04-30 03:10 UTC)

<p>You can remove the skull from MRI images using SwillSkullStripper module, and using SegmentEndoCranium module of SlicerMorph extension (or SurfaceWrapSolidify extension) + Mask volume effect. This approach has the advantage that you can specify arbitrary shape.</p>
<p>Volume masking using a segment:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="xZwyW6SaoM4" data-video-title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=xZwyW6SaoM4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/xZwyW6SaoM4/maxresdefault.jpg" title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' width="" height="">
  </a>
</div>


---

## Post #10 by @slicer365 (2021-04-30 14:11 UTC)

<p>Thanks to Mr. Lassoan for the answer. One disadvantage of this method is that it is irrevocable and not in real time.</p>

---

## Post #11 by @lassoan (2021-04-30 14:26 UTC)

<p>Changing the masked volume requires two clicks, it is reversible and happens in a fraction of a second. You can update the ROI anytime, because the original volume is preserved by default and you just update the masked volume (see the demo video above).</p>
<p>I agree though that the two extra clicks (and going to segment editor, creating a segmentation, etc.) is significantly more complicated than just defining an ROI, that’s why we’ll add clipping with ellipsoid ROI. We’ll also add clipping with an ROI box where you can push in/out one side with an ellipsoid shape, which is essential for cropping 4D cardiac ultrasound volumes, but may be useful for quick approximate removal of the skull in brain images, too.</p>

---
