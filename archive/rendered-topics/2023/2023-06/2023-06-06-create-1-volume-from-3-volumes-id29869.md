# Create 1 volume from 3 volumes

**Topic ID**: 29869
**Date**: 2023-06-06
**URL**: https://discourse.slicer.org/t/create-1-volume-from-3-volumes/29869

---

## Post #1 by @KarelPenicka (2023-06-06 15:39 UTC)

<p>Hi guys. I got from hospital Axial, Koronal and Sagital Series.Each of these series have resolution 0,15 x 0,1 5x 2 mm. I want to take from eaxh series only one view (one with higher resolution ) and create new serie.<br>
I tryed to convert it with Isotropic  spacing, but 3D result is horrible.How can I do it ?<br>
Thank you<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/349ed15da4e4f511c8e39116c12ad5ff9529b94e.png" alt="obrazek" data-base62-sha1="7vv5PK3QgdPoTdXHpJ4QKzhzfwW" width="220" height="92"></p>
<p>I can open all 3 series , and in each window display different serie. But it take me as source volume ony one volume. With series I mean volumes.</p>
<p>Thank you</p>

---

## Post #2 by @mikebind (2023-06-06 19:00 UTC)

<p>Reconstructing a nice 3D image volume from views which are high resolution in some directions but not others is a common desire because medical images are often acquired in this way and it seems intuitive to human brains that there should be an easy way to combine them all together.  However, each series is either missing or squishing together quite a bit of data in the low-resolution dimension, and it is not at all computationally trivial to guess how to use the available slice data to interpolate or resolve that into a single higher-resolution (in all dimensions) image volume which fills in all the space.  There are attempts out there which have tried to solve this problem, but there is no existing method which works really well and everyone just uses.  Here are links to a few times this has come up before with some more helpful discussion and some links to possible approaches:</p>
<ul>
<li><a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941" class="inline-onebox">Combining volumes - what am I missing?</a></li>
<li><a href="https://discourse.slicer.org/t/import-volume-by-projections/2871/4" class="inline-onebox">Import volume by projections - #4 by lassoan</a></li>
</ul>

---

## Post #3 by @KarelPenicka (2023-06-08 19:28 UTC)

<p>Hi Mike, thank you for your help …<br>
For now , I made it from bad resolution. But for next time , the have to prepair it properly from hospital. I will tell them it. One more time thank you for your time <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
