# Segment statistics

**Topic ID**: 7303
**Date**: 2019-06-25
**URL**: https://discourse.slicer.org/t/segment-statistics/7303

---

## Post #1 by @persst (2019-06-25 12:08 UTC)

<p>Hi!</p>
<p>I have a question regarding the module Segment Statistics. After applying Segement Statistics in 3DSlicer 4.9, 3DSlicer displays two different volumes, volume (1) and (2).</p>
<p>Please find the attached table here:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05652fc5faf9880b496789931708c7ece1cf41f8.png" alt="image" data-base62-sha1="LJb4P6OelD2OsX1DGZc2LYDR44" width="654" height="79"></p>
<p>What is the difference between these volumes?</p>
<p>Thanks!</p>

---

## Post #2 by @jamesobutler (2019-06-25 14:02 UTC)

<p>See some information from the following thread:</p><aside class="quote quote-modified" data-post="8" data-topic="1170">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-measure-3d-volumes-dimensions/1170/8">How to measure 3D volume's dimensions?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    There are several ways of computing these metrics. The main difference is what is the representation used (surface or volumetric) and if the entire segment is used or only the part that overlaps with the selected scalar volume. 

Also, is there a way to compute maximum/minimum 3D diameter with any of the statistics modules? 

Currently diameter computation is not offered by any of the Segment Statistics plugins. 
SimpleITK’s LabelShapeStatisticsImageFilter can compute many kind of diameters and…
  </blockquote>
</aside>

<blockquote>
<p>It does not matter which method you use (the difference is less than 1%), just choose one and use always that. If you primarily work with labelmaps (and use 3D surface for visualization only) then you may prefer labelmap based method; if you mainly work with surfaces then you may choose the volume computed from the generated surface.</p>
</blockquote>

---

## Post #3 by @doc-xie (2019-06-26 13:49 UTC)

<p>Hi James Butler,<br>
The difference between the two volumes is 30% and more than 1%. So which one is the actual volume of the infarction?<br>
Thanks,<br>
Xie</p>

---

## Post #4 by @lassoan (2019-06-26 14:44 UTC)

<p>There is also a difference in what volume the statistics is computed on. For example, closed surface statistics plugin reports the entire segment volume; Scalar volume statistics reports only the part that overlaps with the selected “Scalar volume”.</p>

---

## Post #5 by @manjula (2020-01-23 18:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="7303">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>atistics plugin reports the entire segment volu</p>
</blockquote>
</aside>
<p>Dear Prof Lasso,</p>
<p>To calculate the volume of bone and lacuna space percentage,</p>
<p>for example if segment 1st  segment with 700 - 1000 HU and the next segment on the exact same region with 300-500 HU and if i want to measure the volume of 1st and 2nd segment in a CT which volume should i use ?</p>
<p>Label map or the closed surface statistics  volume would be better ?</p>

---

## Post #6 by @lassoan (2020-01-30 15:54 UTC)

<p>It should not matter much as long as you consistently use the same method. If your workflow is primarily uses labelmaps then use labelmap-based metrics, if you mainly work with surface meshes then it may make more sense to use metrics computed from closed surface representation.</p>

---

## Post #7 by @manjula (2020-01-30 21:17 UTC)

<p>Thank you much appreciated !</p>

---
