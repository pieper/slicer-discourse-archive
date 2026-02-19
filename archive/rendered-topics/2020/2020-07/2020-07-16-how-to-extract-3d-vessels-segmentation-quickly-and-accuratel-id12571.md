---
topic_id: 12571
title: "How To Extract 3D Vessels Segmentation Quickly And Accuratel"
date: 2020-07-16
url: https://discourse.slicer.org/t/12571
---

# How to extract 3D vessels segmentation quickly and accurately?

**Topic ID**: 12571
**Date**: 2020-07-16
**URL**: https://discourse.slicer.org/t/how-to-extract-3d-vessels-segmentation-quickly-and-accurately/12571

---

## Post #1 by @wwx992881 (2020-07-16 09:51 UTC)

<p>Hi,All!<br>
I need to extract 3D vessels segmentation from 3d TOF MRA,I want to do that more quickly and accurately .Now I use threshold and islands in segment editor to that and my segmentation as follow.But is there a better way to do?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81c729ddb784a40d1e2340eeb0e8fd1649cc73b8.png" data-download-href="/uploads/short-url/iw4izFO8WhHWEupTlFDIcjJo2Ny.png?dl=1" title="QQ图片20200716175054" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81c729ddb784a40d1e2340eeb0e8fd1649cc73b8_2_593x500.png" alt="QQ图片20200716175054" data-base62-sha1="iw4izFO8WhHWEupTlFDIcjJo2Ny" width="593" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81c729ddb784a40d1e2340eeb0e8fd1649cc73b8_2_593x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81c729ddb784a40d1e2340eeb0e8fd1649cc73b8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81c729ddb784a40d1e2340eeb0e8fd1649cc73b8.png 2x" data-dominant-color="978ABB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">QQ图片20200716175054</span><span class="informations">686×578 73.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2020-07-16 13:02 UTC)

<p>As a start I’d suggest oversampling the segmentation.  Then you might try <a href="https://github.com/vmtk/SlicerExtension-VMTK">VMTK</a> vesselness filtering and other tools.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d67cf10d9aefdc34312aa18162eb850d94719143.jpeg" data-download-href="/uploads/short-url/uBrRCtMzzgjKiIOGdb5AIhLGD8T.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d67cf10d9aefdc34312aa18162eb850d94719143_2_690x397.jpeg" alt="image" data-base62-sha1="uBrRCtMzzgjKiIOGdb5AIhLGD8T" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d67cf10d9aefdc34312aa18162eb850d94719143_2_690x397.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d67cf10d9aefdc34312aa18162eb850d94719143_2_1035x595.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d67cf10d9aefdc34312aa18162eb850d94719143.jpeg 2x" data-dominant-color="C4C3C4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1243×716 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @lassoan (2020-07-16 13:22 UTC)

<p>Yes, oversampling is a good idea (if you need to segment thinner vessels and they are breaking up), and vesselness filtering can be useful too (to improve contrast of tubular structures in images). VMTK’s vessel segmentation methods only worked for me for very simple geometries (up to a few branches).</p>
<p>It seems that you get decent results with simple global thresholding and islands, which means that you would probably get even better results and faster by using “Local Threshold” effect (provided by SegmentEditorExtraEffects extension):</p>
<div class="youtube-onebox lazy-video-container" data-video-id="yi07mjr3JeU" data-video-title="New vessel branch extraction module for 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=yi07mjr3JeU" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/yi07mjr3JeU/maxresdefault.jpg" title="New vessel branch extraction module for 3D Slicer" width="" height="">
  </a>
</div>


---

## Post #4 by @wwx992881 (2020-07-17 08:37 UTC)

<p>Thank for you help! <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=9" title=":grinning:" class="emoji" alt=":grinning:"></p>

---

## Post #5 by @wwx992881 (2020-07-17 09:03 UTC)

<p>hi~I click OK and  I didn’t see any change?Is something wrong with me?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5223dbd1decb06c45d348a9c8051c29b398c7456.png" data-download-href="/uploads/short-url/bIDYIUujMuc18WNgHW1AnNQagzc.png?dl=1" title="微信图片_20200717165950" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/5223dbd1decb06c45d348a9c8051c29b398c7456_2_690x427.png" alt="微信图片_20200717165950" data-base62-sha1="bIDYIUujMuc18WNgHW1AnNQagzc" width="690" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/5223dbd1decb06c45d348a9c8051c29b398c7456_2_690x427.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5223dbd1decb06c45d348a9c8051c29b398c7456.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5223dbd1decb06c45d348a9c8051c29b398c7456.png 2x" data-dominant-color="CCCED0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信图片_20200717165950</span><span class="informations">726×450 58.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @wwx992881 (2020-07-17 09:18 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="12571">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Yes, oversampling is a good idea (if you need to segment thinner vessels and they are breaking up), and vesselness filtering can be useful too (to improve contrast of tubular structures in images). VMTK’s vessel segmentation methods only worked for me for very simple geometries (up to a few branches).</p>
<p>It seems that you get decent results with simple global thresholding and islands, which means that you would probably get even better results and faster by using “Local Threshold” effect (provided by SegmentEditorExtraEffects extension):</p>
</blockquote>
</aside>
<p>Hi,andras,Yes,I  tried it  follow the tutorial step by step,but I don’t see 3d segmentation,why?(I have clicked ‘show 3d’ button) <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4320920b919220dbc805e1c4cb0908966a00af4f.png" data-download-href="/uploads/short-url/9zPLTnsS4Nqo9U78aPXdz2DbwQv.png?dl=1" title="微信图片_20200717171003" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4320920b919220dbc805e1c4cb0908966a00af4f_2_690x387.png" alt="微信图片_20200717171003" data-base62-sha1="9zPLTnsS4Nqo9U78aPXdz2DbwQv" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4320920b919220dbc805e1c4cb0908966a00af4f_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4320920b919220dbc805e1c4cb0908966a00af4f_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4320920b919220dbc805e1c4cb0908966a00af4f.png 2x" data-dominant-color="A6A6AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信图片_20200717171003</span><span class="informations">1366×768 236 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2020-07-17 16:34 UTC)

<aside class="quote no-group" data-username="wwx992881" data-post="5" data-topic="12571">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/ebca7d/48.png" class="avatar"> wwx992881:</div>
<blockquote>
<p>hi~I click OK and I didn’t see any change?Is something wrong with me?</p>
</blockquote>
</aside>
<p>This is normal. Changing resolution does not change what you have already segmented, but if you apply smoothing or make further edits then you will see the effect of increased resolution.</p>
<aside class="quote no-group" data-username="wwx992881" data-post="6" data-topic="12571">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/ebca7d/48.png" class="avatar"> wwx992881:</div>
<blockquote>
<p>Hi,andras,Yes,I tried it follow the tutorial step by step,but I don’t see 3d segmentation,why?(I have clicked ‘show 3d’ button)</p>
</blockquote>
</aside>
<p>You will not see any structures that are smaller than the minimum diameter. Decrease that value to 1-2mm or less.</p>

---

## Post #8 by @wwx992881 (2020-07-20 13:45 UTC)

<p>okok~thanks! <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=9" title=":blush:" class="emoji" alt=":blush:"></p>

---
