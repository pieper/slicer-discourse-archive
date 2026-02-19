---
topic_id: 5970
title: "Determining Diameter And Lengths Of Blood Vessel"
date: 2019-02-28
url: https://discourse.slicer.org/t/5970
---

# Determining diameter and lengths of blood vessel

**Topic ID**: 5970
**Date**: 2019-02-28
**URL**: https://discourse.slicer.org/t/determining-diameter-and-lengths-of-blood-vessel/5970

---

## Post #1 by @elahe_heydari (2019-02-28 15:19 UTC)

<p>Hi everybody<br>
In my project, I need to determined diameter and lengths of vessel. In slicer, How can I do it?<br>
I would be really grateful if you let me know your comments.<br>
Thanks</p>

---

## Post #2 by @Amine (2019-03-04 08:42 UTC)

<p>For the lenght you could use the “curve maker” module (via extensions), there is a lenght value once you make the curve. and for diameter, use reformat module to get a clean slice of the vessel (use shift and crosshairs+click to find it quickly) then use the ruler to measure the distance</p>

---

## Post #3 by @elahe_heydari (2019-03-04 10:58 UTC)

<p>thanks for your reply, I did what you said,but for measurment of diameter, it is not accurate beacuse the shape of vessel is not exactly circle and i need to average all of angles of diameter or find maximume distance.</p>

---

## Post #4 by @Amine (2019-03-04 11:35 UTC)

<p>i guess you want an average diameter then, so what you could do is measure the surface of the vessel section then use it to calculate diameter by (Surface=pi x radius^2). To do so you can do the reformat module to get the vessel section and make a flat segment of it using the paint tool in segment editor, then activate “show 3d” and go to segment statistics module to get the surface (divide it by two since the flat segment is two sided)</p>

---

## Post #5 by @Frederic (2019-03-04 16:43 UTC)

<p>Hi,<br>
Another alternative could be to use the <em><a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/GeodesicSlicer" rel="nofollow noopener">GeodesicSlicer</a></em> module (extension), if your vessel is in 3D.<br>
For the length: Just create the shortest path by add fiducial points<br>
For diameter: Same explanation given by <a class="mention" href="/u/amine">@Amine</a>, Get a slice of the vessel and use the ruler or a little modification of the ’ rTMS resting motor threshold- Correction factor’ option of the GeodesicSlicer module.</p>

---
