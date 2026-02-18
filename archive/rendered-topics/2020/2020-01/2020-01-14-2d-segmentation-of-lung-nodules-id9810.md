# 2D Segmentation of lung nodules

**Topic ID**: 9810
**Date**: 2020-01-14
**URL**: https://discourse.slicer.org/t/2d-segmentation-of-lung-nodules/9810

---

## Post #1 by @ayat_karrar (2020-01-14 15:50 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ececc413e019516e27c7bf78060176c496e3977.png" alt="image" data-base62-sha1="26ZKjomFOSeruI97uoUpl0YfSU7" width="226" height="184"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a1bd38316e343a4aa885779cc584d29277ea2d8.png" alt="image" data-base62-sha1="jHLvvZbHn0737lj1TywxJsTUyKY" width="170" height="173"><br>
Can 3D Slicer make 2D Segmentation as shown in the previous images?</p>

---

## Post #2 by @muratmaga (2020-01-14 16:44 UTC)

<p>Sure you can import a single image and run the segmentation tool, but that’s not really what Slicer is intended for…</p>

---

## Post #3 by @lassoan (2020-01-14 22:10 UTC)

<p>Yes, as <a class="mention" href="/u/muratmaga">@muratmaga</a> suggests, you can segment single-slice volumes in Segment Editor module.</p>
<p>Why are you considering loading and segmenting only a single CT slice?</p>

---

## Post #4 by @ayat_karrar (2020-01-15 03:57 UTC)

<p>Thanks for your reply, i’ve already done my 2d  segmentation manually by using matlab algorithm, and just need to compare my results with an automated tool such as slicer.</p>

---

## Post #5 by @ayat_karrar (2020-01-15 04:04 UTC)

<p>i tried to use segment editor many times for 2d segmentation (my target) but i couldn’t. so do you have any file explains this target?<br>
thanks in advance</p>

---

## Post #6 by @ayat_karrar (2020-01-15 04:07 UTC)

<p>i appreciate your reply.<br>
yes i know, but i need to do 2d segmentation on slicer to evaluate my algorithm results.</p>

---

## Post #7 by @lassoan (2020-01-15 04:17 UTC)

<aside class="quote no-group" data-username="ayat_karrar" data-post="5" data-topic="9810">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ayat_karrar/48/5656_2.png" class="avatar"> ayat_karrar:</div>
<blockquote>
<p>i tried to use segment editor many times for 2d segmentation (my target) but i couldn’t</p>
</blockquote>
</aside>
<p>Many tools are not applicable to single-slice volumes, but otherwise there should be no problems. Let us know if you have any specific issue.</p>
<aside class="quote no-group" data-username="ayat_karrar" data-post="6" data-topic="9810">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ayat_karrar/48/5656_2.png" class="avatar"> ayat_karrar:</div>
<blockquote>
<p>yes i know, but i need to do 2d segmentation on slicer to evaluate my algorithm results.</p>
</blockquote>
</aside>
<p>CT images are natively 3D (except a very few special cases), so I would suggest to do the segmentation in Slicer on the original 3D volume and compared it with the 3D volume that you save in Matlab using <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m">nrrdwrite.m (available in Slicer’s MatlabBridge extension)</a>.</p>

---
