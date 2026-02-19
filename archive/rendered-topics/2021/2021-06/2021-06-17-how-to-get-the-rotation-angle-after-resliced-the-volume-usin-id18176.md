---
topic_id: 18176
title: "How To Get The Rotation Angle After Resliced The Volume Usin"
date: 2021-06-17
url: https://discourse.slicer.org/t/18176
---

# How to get the rotation angle after resliced the volume using two rotating orthogonal planes?

**Topic ID**: 18176
**Date**: 2021-06-17
**URL**: https://discourse.slicer.org/t/how-to-get-the-rotation-angle-after-resliced-the-volume-using-two-rotating-orthogonal-planes/18176

---

## Post #1 by @jumbojing (2021-06-17 01:13 UTC)

<p>In <a href="https://github.com/SlicerHeart/SlicerHeart" rel="noopener nofollow ugc">SlicerHeart/SlicerHeart</a>, I learned the reslicing the volume using two rotating orthogonal planes. That’s great!<br>
I want to know how to get the rotation angle after  resliced the volume using two rotating orthogonal planes in each slice.<br>
<a class="mention" href="/u/lassoan">@lassoan</a> , can you tell me?<br>
Ask grant instruction. Thank!</p>

---

## Post #2 by @lassoan (2021-06-17 13:46 UTC)

<p>What would you like to achieve?</p>
<p>For example, you can get angle between two slices as described in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#measure-angle-between-two-slice-planes">this example</a>.</p>

---

## Post #3 by @jumbojing (2021-06-17 13:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="18176">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>this example</p>
</blockquote>
</aside>
<p>I use this example in  the reslicing the volume using two rotating orthogonal planes.but always 90</p>

---

## Post #4 by @lassoan (2021-06-17 14:00 UTC)

<p>You can change the script to compute anything you need. If you are not interested in angle between two planes then compute angle between one plane and a fixed direction.</p>

---

## Post #5 by @jumbojing (2021-06-17 14:01 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I want to the rotation angle of that two rotating orthogonal planes…or said it Is absolutely not relative, or compared with the original axis…</p>

---

## Post #6 by @jumbojing (2021-06-17 14:16 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> in <a href="https://github.com/smclach/PedicleScrewSimulator/blob/master/PedicleScrewSimulator/PedicleScrewSimulatorWizard/MeasurementsStep.py" rel="noopener nofollow ugc">PedicleScrewSimulator/MeasurementsStep.py at master · smclach/PedicleScrewSimulator</a>,  the def sliderValueChanged,<br>
green slicer rotate is different from Red and Yellow slice…How to correct that…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6552ba492b6c887b981971b16fd285b2a97ca67.jpeg" data-download-href="/uploads/short-url/q0ZnloshemL5ArzyXyo3CLpWugL.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b6552ba492b6c887b981971b16fd285b2a97ca67_2_690x316.jpeg" alt="image" data-base62-sha1="q0ZnloshemL5ArzyXyo3CLpWugL" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b6552ba492b6c887b981971b16fd285b2a97ca67_2_690x316.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b6552ba492b6c887b981971b16fd285b2a97ca67_2_1035x474.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b6552ba492b6c887b981971b16fd285b2a97ca67_2_1380x632.jpeg 2x" data-dominant-color="46474E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2814×1292 336 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2021-06-17 14:38 UTC)

<aside class="quote no-group" data-username="jumbojing" data-post="5" data-topic="18176">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jumbojing/48/10811_2.png" class="avatar"> jumbojing:</div>
<blockquote>
<p>I want to the rotation angle of that two rotating orthogonal planes…or said it Is absolutely not relative, or compared with the original axis…</p>
</blockquote>
</aside>
<p>If you want to compute angle compared to a fixed axis direction then set <code>sliceNormalVector[1]=[1,0,0]</code> instead of setting it from another slice’s normal vector.</p>
<aside class="quote no-group" data-username="jumbojing" data-post="6" data-topic="18176">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jumbojing/48/10811_2.png" class="avatar"> jumbojing:</div>
<blockquote>
<p>he def sliderValueChanged,<br>
green slicer rotate is different from Red and Yellow slice…</p>
</blockquote>
</aside>
<p>You can use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-slice-position-and-orientation-from-a-normal-vector-and-position">this script</a> if you want to rotate slice <em>normal direction</em> but keep the <em>up direction</em> aligned with anatomical axes.</p>

---

## Post #8 by @jumbojing (2021-06-17 14:50 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks​:ox:<img src="https://emoji.discourse-cdn.com/twitter/beer.png?v=9" title=":beer:" class="emoji" alt=":beer:"><img src="https://emoji.discourse-cdn.com/twitter/ox.png?v=9" title=":ox:" class="emoji" alt=":ox:"><img src="https://emoji.discourse-cdn.com/twitter/beer.png?v=9" title=":beer:" class="emoji" alt=":beer:"><img src="https://emoji.discourse-cdn.com/twitter/ox.png?v=9" title=":ox:" class="emoji" alt=":ox:"><img src="https://emoji.discourse-cdn.com/twitter/beer.png?v=9" title=":beer:" class="emoji" alt=":beer:"><img src="https://emoji.discourse-cdn.com/twitter/ox.png?v=9" title=":ox:" class="emoji" alt=":ox:"><img src="https://emoji.discourse-cdn.com/twitter/beer.png?v=9" title=":beer:" class="emoji" alt=":beer:"><img src="https://emoji.discourse-cdn.com/twitter/ox.png?v=9" title=":ox:" class="emoji" alt=":ox:"><img src="https://emoji.discourse-cdn.com/twitter/beer.png?v=9" title=":beer:" class="emoji" alt=":beer:"><img src="https://emoji.discourse-cdn.com/twitter/ox.png?v=9" title=":ox:" class="emoji" alt=":ox:"><img src="https://emoji.discourse-cdn.com/twitter/beer.png?v=9" title=":beer:" class="emoji" alt=":beer:"><img src="https://emoji.discourse-cdn.com/twitter/ox.png?v=9" title=":ox:" class="emoji" alt=":ox:"><img src="https://emoji.discourse-cdn.com/twitter/beer.png?v=9" title=":beer:" class="emoji" alt=":beer:"></p>

---
