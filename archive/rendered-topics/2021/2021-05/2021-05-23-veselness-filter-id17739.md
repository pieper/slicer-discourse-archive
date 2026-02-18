# Veselness filter

**Topic ID**: 17739
**Date**: 2021-05-23
**URL**: https://discourse.slicer.org/t/veselness-filter/17739

---

## Post #1 by @Winet_Azer (2021-05-23 04:00 UTC)

<p>Operating system: windows<br>
Slicer version: 4.11.20200930</p>
<p>Hello,<br>
In my project I use the VMTK plug in for segmentation. When creating the centerline I wonder if there is a possibility to export the data concerning the diameter and the distance as well as their coordinates at the same time. I explain  with VMTK we can have either a table of the centerline concerning the diameters according to the distance or another table with the coordinates of some points of this centerline, but the two tables are not of the same dimension and so we can’t just add them to have all the information. is there another way to generate directly a table with all the information (x, y, z, diameter, distance)</p>
<p>Thank you very much</p>

---

## Post #2 by @chir.set (2021-05-23 09:59 UTC)

<aside class="quote no-group" data-username="Winet_Azer" data-post="1" data-topic="17739">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/winet_azer/48/11025_2.png" class="avatar"> Winet_Azer:</div>
<blockquote>
<p>or another table with the coordinates of some points of this centerline</p>
</blockquote>
</aside>
<p>Which module gives you the point coordinates of a centerline ? Is it a centerline model or a centerline curve ? The distance from the start of the centerline is available in ‘Centerline metrics’ module. Is it the module you’re referencing ? You title hints at ‘Vesselness Filtering’ module : can you precise your request ?</p>

---

## Post #4 by @Winet_Azer (2021-05-23 22:21 UTC)

<p>Thank you for your feedback, yes indeed the module CENTERLINE METRICS gives me distances and diameters, and the center line curve gives me the coordinates of the points. My question is to know if there is a way to have all this information in a single file.<br>
I thought of exporting both types of information but the problem is that for a given centerline the dimensions of the two information tables are not the same.</p>

---

## Post #5 by @chir.set (2021-05-24 08:48 UTC)

<p>The RAS coordinates can be added to the table provided by ‘Centerline metrics’, as in the picture below.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cce98be64028c1761dbed62deec8bdb7826f2d23.png" alt="Screenshot_20210524_091054" data-base62-sha1="teJM36D9iUpQxA7pJ0kAs3pTqCf" width="522" height="358"></p>
<p>If that’s what you expect, I’ll send a pull request to update the ‘Centerline metrics’ module.</p>
<p>Please note that this module can work with centerline models created by the ‘Extract centerline’ module only. These models have an associated ‘Radius’ array, that is actually used by ‘Centerline metrics’. The latter module cannot work with centerline curves produced by ‘Extract centerline’ because these do not have an associated ‘Radius’ array for each constituting point. Besides, a markups curve can be modified in the UI, which would require recomputing all metrics. This computation is done in ‘Extract centerline’, and is quite a tough procedure.</p>

---

## Post #6 by @Winet_Azer (2021-05-24 09:03 UTC)

<p>hello, this is exactly what i am looking for. please send the pull request to update. Thank you very much</p>

---

## Post #7 by @chir.set (2021-06-05 09:51 UTC)

<p>Unfortunately, the <a href="https://github.com/vmtk/SlicerExtension-VMTK/pull/27" rel="noopener nofollow ugc">pull request</a> didn’t gain interest. If you can apply patches to a file, I’ll send you the corresponding patch. You could then update your local copy of Centerlinemetrics.py.</p>

---

## Post #8 by @lassoan (2021-06-06 01:48 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="7" data-topic="17739">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Unfortunately, the <a href="https://github.com/vmtk/SlicerExtension-VMTK/pull/27">pull request </a> didn’t gain interest. I</p>
</blockquote>
</aside>
<p>Thank you for your contributions! The interest is absolutely there, but we need to juggle with many things and very hard to respond to all requests in as quickly as they would deserve.</p>
<p>Next time if you don’t get a timely response then the best is to add a comment every 2-3 days. You can also <span class="mention">@mention</span> the name of the people that you think could help.</p>

---

## Post #9 by @Winet_Azer (2021-06-08 10:29 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> thanks for the answer, yes I can apply patch to my files. please send me the corresponding patch.</p>

---

## Post #10 by @chir.set (2021-06-08 11:11 UTC)

<p>This feature has been merged in the repository, please update your SlicerVMTK extension.</p>
<p>However, choosing between ‘Cumulative’ and ‘Projected’ distance will generate a runtime error. A new pull request in awaiting attention. Everything else is OK.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #11 by @chir.set (2021-06-08 16:23 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="10" data-topic="17739">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>generate a runtime error</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/winet_azer">@Winet_Azer</a><br>
This has been fixed and merged, thanks <a class="mention" href="/u/lassoan">@lassoan</a>. Next SlicerVMTK extension build will be flawless regarding this module.</p>

---
