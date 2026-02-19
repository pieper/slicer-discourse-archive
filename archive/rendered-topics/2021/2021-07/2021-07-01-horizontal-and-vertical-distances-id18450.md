---
topic_id: 18450
title: "Horizontal And Vertical Distances"
date: 2021-07-01
url: https://discourse.slicer.org/t/18450
---

# Horizontal and vertical distances

**Topic ID**: 18450
**Date**: 2021-07-01
**URL**: https://discourse.slicer.org/t/horizontal-and-vertical-distances/18450

---

## Post #1 by @smm9886 (2021-07-01 06:53 UTC)

<p>Hi all,</p>
<p>I could utilize 3D Slicer to extract aortic root and coronary from a thorax-heart DICOM file. Now, I need to set rulers on the 3D view to show the horizontal and vertical distances on my model. However:<br>
1- How I can make sure my ending points of the ruler are snapped exactly to my model points (say at the end of the coronary arteries) but not in some random points close to the model points?<br>
2- I cannot force the ruler to stay in horizontal (0-degree) or vertical (90-degree) planes and it always has some sort of other angles.<br>
2- I cannot transfer or move the location of the ruler after I set the ending points of the ruler (please see the attached photo).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93530c786b53ce64c6f3081c3fd93f56925ad370.png" alt="Picture1" data-base62-sha1="l1i7od8hTJKDOY19kodSWwqRlja" width="454" height="448"></p>
<p>Anyone can please suggest some solutions?<br>
I can tell more detail if necessary.</p>
<p>Bests<br>
Mahmoud</p>

---

## Post #2 by @lassoan (2021-07-02 04:09 UTC)

<p>If you want to measure within a particular plane then you can place the line endpoints in a slice view instead of a 3D view. Or just display an axial slice view in the 3D view (click the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">Show in 3D view</a> button) to guide the point placement.</p>
<p>If you use markups line (instead of annotation ruler) in a recent Slicer Preview Release then you can adjust the point positions after placement (they stick to the visible surface by default).</p>

---

## Post #3 by @smm9886 (2021-07-02 05:49 UTC)

<p>Grazie <a class="mention" href="/u/lassoan">@lassoan</a> from Italia. I want to use the ruler annotation in 3D view to use the plot for my report files. When I am using markup lines, they are not clear in the plot (barely I can see their ending points). The good thing about the annotation rulers is that they are better visualized on the plot. However, once I fix the ending points of the ruler, I cannot move it, or also I would like to change the font size of the dimensions. I need to modify the 3D view plot and the ruler before I can use them in my report file. I will be happy if you could tell us some suggestions.</p>
<p>Best wishes,<br>
Mahmoud</p>

---

## Post #4 by @lassoan (2021-07-08 17:36 UTC)

<p>Markup lines have dozens of parameters that you can set so that they appear the way you want. For example, if you find the endpoints to be too small then you can adjust the “Glyph size” slider. I would recommend to go to Markups module and play with all the settings in “Display” section.</p>

---
