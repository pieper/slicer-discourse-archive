---
topic_id: 4809
title: "Threshold Fail For Segment Editor"
date: 2018-11-20
url: https://discourse.slicer.org/t/4809
---

# Threshold fail for Segment Editor

**Topic ID**: 4809
**Date**: 2018-11-20
**URL**: https://discourse.slicer.org/t/threshold-fail-for-segment-editor/4809

---

## Post #1 by @cyufu (2018-11-20 04:33 UTC)

<p>Operating system: windows 10  64<br>
Slicer version:4.11.0 2018-11-17</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65e0aa009508cf016a897cea1352d21aa58b0c02.png" data-download-href="/uploads/short-url/exfz27C9FuifOE97hiuyjjgHV0m.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65e0aa009508cf016a897cea1352d21aa58b0c02_2_690x481.png" alt="image" data-base62-sha1="exfz27C9FuifOE97hiuyjjgHV0m" width="690" height="481" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65e0aa009508cf016a897cea1352d21aa58b0c02_2_690x481.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65e0aa009508cf016a897cea1352d21aa58b0c02_2_1035x721.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65e0aa009508cf016a897cea1352d21aa58b0c02_2_1380x962.png 2x" data-dominant-color="CECED3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1391×970 85 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Apply  fail</p>
<p>Use for masking→Paint or Scissors（fill inside）fail</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c76879494ecee548f043ea895ee845b2182f26c4.gif" data-download-href="/uploads/short-url/ss2QJTCVZHEunfbFq4qNMQoIK3O.gif?dl=1" title="GIF" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c76879494ecee548f043ea895ee845b2182f26c4_2_690x481.gif" alt="GIF" data-base62-sha1="ss2QJTCVZHEunfbFq4qNMQoIK3O" width="690" height="481" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c76879494ecee548f043ea895ee845b2182f26c4_2_690x481.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c76879494ecee548f043ea895ee845b2182f26c4_2_1035x721.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c76879494ecee548f043ea895ee845b2182f26c4_2_1380x962.gif 2x" data-dominant-color="B6B7BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">GIF</span><span class="informations">1391×970 562 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks<br>
Cyufu</p>

---

## Post #2 by @cpinter (2018-11-20 13:39 UTC)

<p>It is hard to know exactly what happens without more information such as the voxel values in the image, but here’s what I think:</p>
<ul>
<li>Threshold limits seem to be off, because even before you press apply, we don’t see anything in the preview. There should be a pink “pulsing” in the “in” area of the threshold</li>
<li>Scissors don’t work for the same reason, because you apply the threshold as mask, and as threshold excludes everything, scissors do not fill anything</li>
</ul>
<p>What are the scalar values in your image? Is there anything in the log that may help? (About / Report a problem)</p>

---

## Post #3 by @lassoan (2018-11-20 15:45 UTC)

<p>Also, could you go to Volumes module, select the master volume is selected as “Active volume” and take a screenshot of <em>Volume information</em> section and <em>Histogram</em> section?</p>

---

## Post #4 by @cyufu (2018-11-20 23:44 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="4809">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>go to Volumes module, select the master volume is selected as “Active volume” and take a screenshot of <em>Volume information</em> section and <em>Histogram</em> section?</p>
</blockquote>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a31c49507e5964ba0310614f1807e5540df3ac3.png" data-download-href="/uploads/short-url/f9reP66Jr9bQrrQoPaizvzOEgAb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a31c49507e5964ba0310614f1807e5540df3ac3_2_655x500.png" alt="image" data-base62-sha1="f9reP66Jr9bQrrQoPaizvzOEgAb" width="655" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a31c49507e5964ba0310614f1807e5540df3ac3_2_655x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a31c49507e5964ba0310614f1807e5540df3ac3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a31c49507e5964ba0310614f1807e5540df3ac3.png 2x" data-dominant-color="DCDCDB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">822×653 50.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/2774719a8285cd1f742949a3a7dd758467b98f99.png" data-download-href="/uploads/short-url/5D26g5QkoiaExaq2tvM7JFKg4iJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/2774719a8285cd1f742949a3a7dd758467b98f99.png" alt="image" data-base62-sha1="5D26g5QkoiaExaq2tvM7JFKg4iJ" width="655" height="500" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">863×658 31 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks</p>

---

## Post #6 by @lassoan (2018-11-20 23:52 UTC)

<p>There are two unusual properties of this volume:</p>
<ol>
<li>It is very large. Try resample by a spacing factor of 4 in Crop volume module and see if you still have issues.</li>
<li>This is a binary volume, i.e., it is already segmented. Instead of segmenting it again, load the volume as a labelmap volume and then import it into segmentation (using Segmentations module Import/Export section).</li>
</ol>

---

## Post #7 by @cyufu (2018-11-21 01:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="4809">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>by a spacing factor of 4 in Crop volume module</p>
</blockquote>
</aside>
<p>by a spacing factor of 1 in Crop volume module,success.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20fffd4bd0b710cfd4e0ecaede015176f55e840a.jpeg" data-download-href="/uploads/short-url/4HVJv5YDZC6RxbNpG3O9cn3m6QW.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/20fffd4bd0b710cfd4e0ecaede015176f55e840a_2_445x500.jpeg" alt="image" data-base62-sha1="4HVJv5YDZC6RxbNpG3O9cn3m6QW" width="445" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/20fffd4bd0b710cfd4e0ecaede015176f55e840a_2_445x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/20fffd4bd0b710cfd4e0ecaede015176f55e840a_2_667x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20fffd4bd0b710cfd4e0ecaede015176f55e840a.jpeg 2x" data-dominant-color="A68590"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">861×966 452 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>thanks</p>

---

## Post #8 by @cpinter (2018-11-21 14:21 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="4809">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This is a binary volume, i.e., it is already segmented. Instead of segmenting it again, load the volume as a labelmap volume and then import it into segmentation (using Segmentations module Import/Export section)</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/cyufu">@cyufu</a> Have you tried this? I think it’s unnecessary extra work re-segmenting a segmentation. It’s much easier if you load it according to its data type to begin with.</p>

---

## Post #9 by @cyufu (2018-11-21 23:43 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="8" data-topic="4809">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>load the volume as a labelmap volume</p>
</blockquote>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27b1cba5c0d7c57de58feb542e1744f7c6b2a61c.png" data-download-href="/uploads/short-url/5F9xSx9GzwGA8uckjdnvmhw7HAg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27b1cba5c0d7c57de58feb542e1744f7c6b2a61c.png" alt="image" data-base62-sha1="5F9xSx9GzwGA8uckjdnvmhw7HAg" width="690" height="395" data-dominant-color="223840"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">777×445 4.74 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But it isn’t outline.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57e855b43dc03ad519ae5ecb5e85479901a0cab3.png" data-download-href="/uploads/short-url/cxFjwu8LxyzFchpE8IJOfHvLEpJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57e855b43dc03ad519ae5ecb5e85479901a0cab3_2_690x308.png" alt="image" data-base62-sha1="cxFjwu8LxyzFchpE8IJOfHvLEpJ" width="690" height="308" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57e855b43dc03ad519ae5ecb5e85479901a0cab3_2_690x308.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57e855b43dc03ad519ae5ecb5e85479901a0cab3_2_1035x462.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57e855b43dc03ad519ae5ecb5e85479901a0cab3.png 2x" data-dominant-color="2C2529"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1089×487 31.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>thanks</p>

---

## Post #10 by @cpinter (2018-11-22 00:17 UTC)

<aside class="quote no-group" data-username="cyufu" data-post="9" data-topic="4809">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cyufu/48/1779_2.png" class="avatar"> cyufu:</div>
<blockquote>
<p>But it isn’t outline</p>
</blockquote>
</aside>
<p>Because you loaded it as regular volume. If you open the options after drag&amp;drop in the Add data dialog, you can check a checkbox so that it’s loaded as labelmap. You can also convert it in the Volumes module to labelmap type.</p>
<p>Most data types can be displayed in many ways, so the way something is displayed is not a good indicator of what it is exactly. The Data module for example is a much better way to find these things out.</p>

---

## Post #11 by @cyufu (2018-11-22 00:55 UTC)

<p>I have opened it correctly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36876ad26bdf1ac0e4f0231e97d1db7750ee2d16.png" data-download-href="/uploads/short-url/7MnUDMiYsqi0zMFPOo9MJjr666G.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36876ad26bdf1ac0e4f0231e97d1db7750ee2d16.png" alt="image" data-base62-sha1="7MnUDMiYsqi0zMFPOo9MJjr666G" width="690" height="410" data-dominant-color="FAFAFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">744×443 7.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a62005d8f37a2dc733508134673f5cbfede94202.png" data-download-href="/uploads/short-url/nHBRRlr8MOfQVnzhC5Qu4yM6fOq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a62005d8f37a2dc733508134673f5cbfede94202_2_690x488.png" alt="image" data-base62-sha1="nHBRRlr8MOfQVnzhC5Qu4yM6fOq" width="690" height="488" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a62005d8f37a2dc733508134673f5cbfede94202_2_690x488.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a62005d8f37a2dc733508134673f5cbfede94202_2_1035x732.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a62005d8f37a2dc733508134673f5cbfede94202.png 2x" data-dominant-color="A0A6AC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1107×783 47.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>thanks.</p>

---

## Post #12 by @lassoan (2022-02-18 01:18 UTC)

<p>3 posts were split to a new topic: <a href="/t/segment-editor-threshold-effect-creates-large-blocks/22034">Segment Editor Threshold effect creates large blocks</a></p>

---
