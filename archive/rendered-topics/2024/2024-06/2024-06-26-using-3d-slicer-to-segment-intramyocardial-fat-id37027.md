---
topic_id: 37027
title: "Using 3D Slicer To Segment Intramyocardial Fat"
date: 2024-06-26
url: https://discourse.slicer.org/t/37027
---

# Using 3D slicer to segment intramyocardial fat

**Topic ID**: 37027
**Date**: 2024-06-26
**URL**: https://discourse.slicer.org/t/using-3d-slicer-to-segment-intramyocardial-fat/37027

---

## Post #1 by @kasun (2024-06-26 02:54 UTC)

<p>Hello all,</p>
<p>I was hoping to get some help with a project I’m working on.</p>
<p>I have a series of cardiac gated CTs and I would like to segment out the intramyocardial fat (lipomatous metaplasia) as a 3d shell vtk file.</p>
<p>This lipmatous metaplasia (LM) would be defined as “a continuous minimal area (eg, &gt;1 mm2) … with attenuation between −180 and 0 Hounsefield Units HU”<br>
<a href="https://doi.org/10.1161/CIRCIMAGING.123.014399" class="onebox" target="_blank" rel="noopener nofollow ugc">https://doi.org/10.1161/CIRCIMAGING.123.014399</a></p>
<p>My plan would be to use TotalSegmentator Heart Chambers model to segment the endo and epicardial borders of the LV and RV.</p>
<p>Would be it possible to automatically segment out this range of Hounsfield Units from only within the myocardium i.e. exclude epicardial adipose tissue (and ideally include them if there is &gt;1mm2 of contiguous fat)? And create a 3D model that can be exported as a VTK. How could I do this?</p>

---

## Post #2 by @pieper (2024-06-27 12:08 UTC)

<p>That sounds quite doable, either interactively using various tools in the Segment Editor or if you want by writing a script to automate parts if you have a lot of cases to do.  I’m not sure there’s any specific recipe other than practice with the tools and review examples.</p>

---

## Post #3 by @kasun (2024-07-11 01:03 UTC)

<p>Hi Steve</p>
<p>Thanks for this. Is there a particular tool that I can use to select pixels with a particular hounsfield unit? What is the name of that tool / is there a video/written guide of using this?</p>

---

## Post #4 by @pieper (2024-07-11 11:53 UTC)

<p>The Threshold tool in the SegmentEditor can be used to set high/low masking thresholds for other tools (paint, draw, scissors…).  You can find lots of videos and examples online - these features have been stable for many years, so even old videos about older versions work basically the same.</p>

---
