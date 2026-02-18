# Unable to see moving segment on 3d view

**Topic ID**: 8445
**Date**: 2019-09-16
**URL**: https://discourse.slicer.org/t/unable-to-see-moving-segment-on-3d-view/8445

---

## Post #1 by @Andrew_Kanawati (2019-09-16 14:29 UTC)

<p>Hello<br>
I’ve performed segment registration on a ct and mri model<br>
The models are aligned on the slice view but not on the 3d view<br>
I’ve tried changing settings in data and segmentations modules without any luck<br>
Thank you for you help<br>
Andrew</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4399a5d086cfe87b48c6e13b6450e14cc4eb82d6.jpeg" data-download-href="/uploads/short-url/9E1b6WRM4AhuYpZZemZoyDj7Fzw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4399a5d086cfe87b48c6e13b6450e14cc4eb82d6_2_690x388.jpeg" alt="image" data-base62-sha1="9E1b6WRM4AhuYpZZemZoyDj7Fzw" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4399a5d086cfe87b48c6e13b6450e14cc4eb82d6_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4399a5d086cfe87b48c6e13b6450e14cc4eb82d6_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4399a5d086cfe87b48c6e13b6450e14cc4eb82d6_2_1380x776.jpeg 2x" data-dominant-color="767179"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">5120×2880 1.74 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @cpinter (2019-09-16 14:33 UTC)

<p>Which Slicer version do you use?</p>
<aside class="quote no-group" data-username="Andrew_Kanawati" data-post="1" data-topic="8445">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/andrew_kanawati/48/3983_2.png" class="avatar"> Andrew_Kanawati:</div>
<blockquote>
<p>The models are aligned on the slice view but not on the 3d view</p>
</blockquote>
</aside>
<p>What does this mean exactly?</p>
<p>When I tried transforming a segmentation in the latest version, it moved in all views. So we need some more information to understand the issue and to reproduce it if it is an error.</p>

---

## Post #3 by @Andrew_Kanawati (2019-09-16 15:15 UTC)

<p>I’m using 4.10.2<br>
I’m so sorry - I didn’t express myself well. the models are well aligned on all slice views, however only one model (the fixed one) is appearing on the 3d view</p>

---

## Post #4 by @cpinter (2019-09-16 15:23 UTC)

<p>No problem, just trying to understand the situation.</p>
<p>It seems to me that you use the Segment Registration extension. I tried it quite recently when I created the tutorial for the MRI-US Prostate Contour Propagation module, and it seemed to work properly.</p>
<p>If you go to the Segmentations module and select “Segmentation MRI”, then what do you see in the Representations section?</p>

---

## Post #5 by @Andrew_Kanawati (2019-09-16 15:54 UTC)

<p>Yes - it was a ‘binary label map’ and I changed to ‘closed surface’ - this fixed the problem… thank you very much</p>
<p>Is there a way of making the colour map change according to the distance difference? I’ve used a similar function in mesh lab</p>

---

## Post #6 by @cpinter (2019-09-16 15:58 UTC)

<p>Great, thanks for the update.</p>
<p>We’re trying to keep the forum posts on a single topic. Could you please submit a new one with the color mapping question? Thank you!</p>

---

## Post #7 by @Andrew_Kanawati (2019-09-16 16:01 UTC)

<p>Yes of course. Thanks again</p>

---
