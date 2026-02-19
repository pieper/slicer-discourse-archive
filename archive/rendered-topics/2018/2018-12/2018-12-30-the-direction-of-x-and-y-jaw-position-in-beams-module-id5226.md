---
topic_id: 5226
title: "The Direction Of X And Y Jaw Position In Beams Module"
date: 2018-12-30
url: https://discourse.slicer.org/t/5226
---

# The direction of x and y jaw position in Beams Module

**Topic ID**: 5226
**Date**: 2018-12-30
**URL**: https://discourse.slicer.org/t/the-direction-of-x-and-y-jaw-position-in-beams-module/5226

---

## Post #1 by @aseman (2018-12-30 08:08 UTC)

<p>Slicer version:4.8.1<br>
Hi 3D slicer experts and all<br>
In Beams module for Geometry Tab, the x jaw position and y jaw position are in the direction of which axes respectively? In the other words SI or AP or RL axes?<br>
Thanks a lot</p>

---

## Post #2 by @lassoan (2018-12-30 14:51 UTC)

<p>In general, in Slicer, first (x) axis is L-R, second (y) axis is A-P direction. <a class="mention" href="/u/cpinter">@cpinter</a> or <a class="mention" href="/u/gcsharp">@gcsharp</a> may comment on the axes directions in this specific case.</p>
<p>Use latest stable version (Slicer-4.10).</p>

---

## Post #3 by @gcsharp (2018-12-31 14:04 UTC)

<p>Hm, it looks like the beams module does not follow IEC conventions.  Thank you for the alert.</p>

---

## Post #4 by @cpinter (2018-12-31 17:23 UTC)

<p>I fixed the issue as discussed with <a class="mention" href="/u/gcsharp">@gcsharp</a>, see <a href="https://github.com/SlicerRt/SlicerRT/issues/100" rel="nofollow noopener">https://github.com/SlicerRt/SlicerRT/issues/100</a>.<br>
It should be fine in tomorrow’s nightly or later (but NOT in 4.10, only in 4.10.1 when released).</p>

---

## Post #5 by @aseman (2019-01-03 06:13 UTC)

<p>Hi<br>
Thank you for your guidelines.I have another question ! I import the RT Plans from Treatment Planning System (TPS). In TPS, the x is in L-R and y is in S-I directions. Is it possible to match the x and y directions in these two systems (i.e TPS and 3D Slicer)?<br>
Thanks a lot</p>

---

## Post #6 by @cpinter (2019-01-03 16:01 UTC)

<p>We talked with <a class="mention" href="/u/gcsharp">@gcsharp</a> and although the axes were right after my fix, the directions weren’t. I fixed them now.</p>
<p>To use this fixed version, please install the “Nightly Build” tomorrow or any day after: <a href="https://download.slicer.org/" rel="nofollow noopener">https://download.slicer.org/</a></p>

---

## Post #7 by @gcsharp (2019-01-03 17:00 UTC)

<p>Hi Azam,</p>
<p>Now everything should match between Slicer and your TPS after Csaba’s fix (tomorrow or next day nightly build).  For gantry 0, couch 0, and HFS treatment position, you should see x increase from R to L, and y increase from I to S. Please let us know if you have any more problem and thank you for your report.</p>

---

## Post #8 by @aseman (2019-02-09 05:25 UTC)

<p>Hi 3D Slicer experts and all<br>
I’ m sorry for my question .but can you tell me that for gantry 0 and  collimator 0 ,  what is the direction of x and y jaw respectively for slicer 4.10.1 (Linux)?<br>
Thanks a lot</p>

---

## Post #9 by @cpinter (2019-02-09 15:37 UTC)

<p>After our recent fixes, which are included in 4.10.1, everything should conform to the DICOM standard:</p>
<ol>
<li>IEC: <a href="http://dicom.nema.org/medical/DICOM/current/output/chtml/part03/sect_C.8.8.25.6.html" rel="nofollow noopener">http://dicom.nema.org/medical/DICOM/current/output/chtml/part03/sect_C.8.8.25.6.html</a>
</li>
<li>Beams (see jaws at ‘beam limiting device’): <a href="http://dicom.nema.org/medical/DICOM/current/output/chtml/part03/sect_C.8.8.14.html" rel="nofollow noopener">http://dicom.nema.org/medical/DICOM/current/output/chtml/part03/sect_C.8.8.14.html</a>
</li>
</ol>

---

## Post #10 by @aseman (2019-02-15 13:09 UTC)

<p>Hi<br>
Thank you very much for your guidelines. Briefly , by considering the 3D view and slice viewers , for Gantry 0 and collimator 0 ,  the x jaw position increases in S-I direction and y jaw position increases in L-R direction. also, both the  Gantry and collimator  rotation are counter clockwise. is this statement true ?<br>
Thanks a lot</p>

---
