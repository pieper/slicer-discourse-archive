---
topic_id: 16611
title: "Vmtk Networkextraction Algorithm"
date: 2021-03-18
url: https://discourse.slicer.org/t/16611
---

# Vmtk networkextraction algorithm

**Topic ID**: 16611
**Date**: 2021-03-18
**URL**: https://discourse.slicer.org/t/vmtk-networkextraction-algorithm/16611

---

## Post #1 by @Deepa (2021-03-18 11:04 UTC)

<p>Hi All, Could someone please let me know the name of the network extraction algorithm available in VMTK?</p>

---

## Post #2 by @lassoan (2021-03-26 02:58 UTC)

<p>As far as I know, it is a new algorithm invented in VMTK. You can refer to it as “network extraction algorithm in VMTK” and cite the <a href="https://github.com/vmtk/vmtk/blob/master/doc/joss-paper/paper.md">VMTK paper</a>.</p>

---

## Post #3 by @Deepa (2021-03-26 05:07 UTC)

<p>Thank you! I did the same <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #5 by @KaryLiang (2021-04-06 01:59 UTC)

<p>Hi,<br>
I’ve got the ‘Radius’ array from network extraction algorithm <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py#L605" rel="noopener nofollow ugc">here</a>, can i think of this array as the true radius of the blood vessel?</p>

---

## Post #6 by @Carlos_Alberto_Bulan (2021-04-06 11:54 UTC)

<p>Hi,<br>
The radius computed by the filter is actually the “Maximum Sirunscrive Sphere Radius”, which is equal to the “real” cross-sectional radius in the case of a straight cylindrical pipe shape.<br>
The MSSRadius deviates from the real cross-sectional Radius when the shape of your artery deviates from the pipe. Usually overestimates at junctions and underestimates elsewhere.<br>
Depending on your application, the MSSRadius can be a good estimation of the real Radius.<br>
If you want more precision you could try vmtkcenterlinesections, which outputs the cross-sectional area at each centerline point (among other, potentially, useful data).<br>
Regards,<br>
Carlos</p>

---

## Post #7 by @KaryLiang (2021-04-07 08:12 UTC)

<p>Thanks Carlos. As you know, i want the cross-sectional radius actually. it’s so great that radius can compute using networkextraction. It help me a lot.<br>
I have one more question, the radius’s array, N*1, what does N represent? network points number? if yes, what is the distance between the points?<br>
If vmtkcenterlinesections can get more accurate radius, i’ll try it later.</p>

---

## Post #8 by @Carlos_Alberto_Bulan (2021-04-08 00:17 UTC)

<p>You can use vmtkcenterlineresampling filter to resample the centerline spacing.</p>

---

## Post #9 by @KaryLiang (2021-04-12 08:54 UTC)

<p>I am trying to use vmtkcenterlines<a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py#L691" rel="noopener nofollow ugc">(here)</a>  to get vessel center lines and MSSRadius. Before that, i already get endpoints from network algorithm.<br>
This is a detail of vmtkcenterlines input:</p>
<ul>
<li>
<p>tubePolyData = surfaceCapper.GetOutput().</p>
</li>
<li>
<p>sourceIdLIst: the first point of the endpoints array (i not sure does this make sense).</p>
</li>
<li>
<p>targetIdList: all point of endpoints expect the first one.</p>
</li>
</ul>
<p>i meet some problem:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa03ca6ae288110f4a26aa5716b1755fee80144b.png" alt="image" data-base62-sha1="zFJukeGlamLlsQdDUdOXHCou4Sn" width="294" height="34"></p>
<p>Please help or try to give some ideas to fix this.</p>

---
