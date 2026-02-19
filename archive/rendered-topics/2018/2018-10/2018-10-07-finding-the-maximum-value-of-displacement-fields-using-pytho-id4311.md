---
topic_id: 4311
title: "Finding The Maximum Value Of Displacement Fields Using Pytho"
date: 2018-10-07
url: https://discourse.slicer.org/t/4311
---

# Finding the maximum value of displacement fields using python

**Topic ID**: 4311
**Date**: 2018-10-07
**URL**: https://discourse.slicer.org/t/finding-the-maximum-value-of-displacement-fields-using-python/4311

---

## Post #1 by @aseman (2018-10-07 06:20 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.8.1<br>
Hi 3D slicer experts and all users<br>
I work with 3D slicer, but I am unfamiliar with python, and now I am learning it. I calculated the displacement fields for a specific segment (eg, lung), and as we know these vectors include components in 3 directions (RAS).<br>
1- I want to find the value of these vectors  ( Di =  (  Ri2 + Ai2 + Si2 )0.5  )<br>
, then find the maximum  among these values Di (Di max) .<br>
2- If we consider for each components of R, A, S  ;3 variables  P, Q, N ;  then what is the maximum value of each variables (eg, Pi max , Qi max , Ni max)?</p>

---

## Post #2 by @lassoan (2018-10-07 16:25 UTC)

<p>You can use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromGridTransform">arrayFromGridTransform</a> to get displacement values as a numpy array and you can use basic numpy functions to compute magnitude (norm) of the vectors and find maxima.</p>
<p>You can also convert any transform to a volume node containing displacement field vectors or magnitudes and use arrayFromVolume to get numpy array.</p>

---
