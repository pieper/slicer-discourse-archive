---
topic_id: 29428
title: "Totalsegmentator Practise Data"
date: 2023-05-12
url: https://discourse.slicer.org/t/29428
---

# Totalsegmentator --- practise data

**Topic ID**: 29428
**Date**: 2023-05-12
**URL**: https://discourse.slicer.org/t/totalsegmentator-practise-data/29428

---

## Post #1 by @whu (2023-05-12 12:52 UTC)

<p>After installing the Totalsegmentator extensions successfully.<br>
I found little problem in the visualization.<br>
Firstly, when using the example CTA data, when “Show 3D”, the result is:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22d4e33d00396f253ee98bf71d28fb177ff35a77.jpeg" alt="image" data-base62-sha1="4Y8lj6M2RkdJvUkhVIlQOE4yLRR" width="488" height="430"><br>
and the local detail is like this,seemed not so smooth as it should be.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/529887822ae86d8455f1ac63730161e54a16d067.jpeg" alt="image" data-base62-sha1="bMFWBbSh48MalDcyXYsARWR16NF" width="313" height="320"><br>
Second, when using the whole heart ct data (the famous segmentation dataset:<a href="https://zmiclab.github.io/zxh/0/mmwhs/data.html" class="inline-onebox" rel="noopener nofollow ugc">Multi-Modality Whole Heart Segmentation 2017</a>),one of the dataset:<br>
the process is good,but the visualization result is the same:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7ada4380db8d14819c790402c0b4e9e5dcebb1fc.jpeg" alt="image" data-base62-sha1="hwNSvzXrPlP7auHzjyr4GbR40Qk" width="362" height="367"><br>
If anyone want to practice it ,  I would like to share one of the dataset.</p>

---

## Post #2 by @rbumm (2023-05-12 16:30 UTC)

<p>You are probably using the FAST option automatically, in which the dataset gets downsampled?<br>
What are you system specs (GPU)?</p>

---

## Post #3 by @whu (2023-05-14 12:46 UTC)

<p>thanks.<br>
Win10 64bits，i7 12cores, NVIDIA Quadro P620（2G graphics memory）。<br>
So the totalsegmentator force to use fast mode, it seemed that the graphics memory should be more then 7G.</p>

---

## Post #4 by @rbumm (2023-05-14 15:05 UTC)

<p>You could install Pytorch in cpu mode, I guess you would get better segmentation results but would have a longer waiting time.</p>

---

## Post #5 by @whu (2023-05-15 10:45 UTC)

<p>the console version in Aconda virtual enviroment,Totalsegment seemed can not support “Show 3D”, just the slice by slice UNet segmentation. <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @whu (2023-05-15 11:23 UTC)

<p>the heart_myocardium segmentation result is like this<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/137422a5f510e0dcacad34fda97898885a6e48af.png" alt="image" data-base62-sha1="2M5Te6M3yrYQPp6zr0R1NmWxHe7" width="312" height="309"><br>
~</p>

---
