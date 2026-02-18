# Distance measurement

**Topic ID**: 8495
**Date**: 2019-09-19
**URL**: https://discourse.slicer.org/t/distance-measurement/8495

---

## Post #1 by @RadioQuest (2019-09-19 10:17 UTC)

<p>Hi…<br>
Is there a tool to measure the distance between 2 points. (ruler annotation is not useful).<br>
I need some kind of ruler or scale to measure the size/ distance.<br>
Thanks.</p>

---

## Post #2 by @lassoan (2019-09-19 12:22 UTC)

<aside class="quote no-group" data-username="RadioQuest" data-post="1" data-topic="8495">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/85f322/48.png" class="avatar"> RadioQuest:</div>
<blockquote>
<p>ruler annotation is not useful</p>
</blockquote>
</aside>
<p>Annotation ruler can measure distance between two points. Why it is not suitable for what you want to do?</p>
<p>You can drop two markup fiducial points and get the distance between them by going to Markups module, selecting both fiducial points in the list, and right-click in the list.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5e35e25920514647975f597b18ee749656b42f5.png" data-download-href="/uploads/short-url/nFvUMlXk8b5GALanHjWLsfLr1tP.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5e35e25920514647975f597b18ee749656b42f5_2_690x498.png" alt="image" data-base62-sha1="nFvUMlXk8b5GALanHjWLsfLr1tP" width="690" height="498" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5e35e25920514647975f597b18ee749656b42f5_2_690x498.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5e35e25920514647975f597b18ee749656b42f5_2_1035x747.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5e35e25920514647975f597b18ee749656b42f5_2_1380x996.png 2x" data-dominant-color="D5D7E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1644×1188 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>We are improving markups on recent Slicer Preview versions, adding a line tool, which is somewhat more convenient (but it does not display the distance value yet, so for now you have to compute it from the point coordinates yourself).</p>

---

## Post #3 by @RadioQuest (2019-09-19 12:59 UTC)

<p>Yes this works.<br>
Thanks a lot!</p>

---

## Post #4 by @lassoan (2019-09-19 13:14 UTC)

<p>Great! Why ruler was not suitable? (just asking so that we can take it into consideration when improving markups lines)</p>

---

## Post #5 by @RadioQuest (2019-09-19 13:43 UTC)

<p>Hi…<br>
I am trying to measure the distance - for example 2 cm lateral from midline , etc. So I needed a tool that will help me to select my region easily anywhere. Also it would be useful to measure the distance between any two points. This present ruler does not seem to be that useful if I know the distance and place point accordingly.<br>
please correct me if I am wrong.<br>
Thanks.</p>

---

## Post #6 by @anilpawar (2022-05-13 11:26 UTC)

<p>Hi, thanks for clear steps to measure the length. Still I am a small query. I am using it for CT images where pixel spacing is in mm. So this measured length will be in mm or pixels unit?</p>
<p>Thanks in advance.</p>

---

## Post #7 by @lassoan (2022-05-14 20:08 UTC)

<p>Measurement is always in physical units (you may not even load an image, but you may measure distances on surface meshes, etc).</p>
<p>Unless you change the default unit in the application settings, the physical length unit is millimeters.</p>

---

## Post #8 by @anilpawar (2022-05-17 03:42 UTC)

<p>Thanks a lot for quick reply and confirmation <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @lassoan (2023-03-21 02:03 UTC)



---
