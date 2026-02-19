---
topic_id: 23070
title: "Artery Tumor Intersection Points"
date: 2022-04-21
url: https://discourse.slicer.org/t/23070
---

# Artery-tumor intersection points

**Topic ID**: 23070
**Date**: 2022-04-21
**URL**: https://discourse.slicer.org/t/artery-tumor-intersection-points/23070

---

## Post #1 by @gfurnari (2022-04-21 09:01 UTC)

<p>Hi everyone,<br>
i’m working on segmentation of kidney tumor and artery that feeds the tumor. I used logical operator intersect to get the parts where artery and tumor touch each other. I’d like to know if it’s possible to get ras coordinates of the contact points (without adding markups manually).<br>
Thank you very much for your time.</p>

---

## Post #2 by @gfurnari (2022-04-21 09:46 UTC)

<p>P.S.<br>
it would be even better if i could get intersection point between tumor segment and centerline curve of the artery, obtained through “extract centerline” (vmtk).<br>
thanks again</p>

---

## Post #3 by @mikebind (2022-04-21 17:26 UTC)

<p>If there are multiple intersection regions, you can split each into it’s own segment using Islands → Split islands to segments.  Then, you can find the centroid of each intersection segment using Segment Statistics module.  If there are only small regions of intersection, these centroids might be quite close to the vessel centerline.</p>

---

## Post #4 by @gfurnari (2022-04-22 13:13 UTC)

<p>Thank you for your quick response, mike.<br>
Though, is it possible to get the exact intersection point/points?</p>

---

## Post #5 by @mikebind (2022-04-22 16:09 UTC)

<p>I’m sure this is possible at the VTK level and I would not be surprised if this is possible somehow in Slicer or a current Slicer extension, but I personally do not know how to find intersection points of a markups curve with a surface model. In <a href="https://discourse.slicer.org/t/intersection-two-models-plane-and-centerlines-ct-mr/4130/3">this</a> forum thread (<a href="https://discourse.slicer.org/t/intersection-two-models-plane-and-centerlines-ct-mr/4130/3" class="inline-onebox">Intersection two models (Plane and centerlines CT/MR) - #3 by shahrokh</a>), I see someone has shared code for finding intersections of curves with a plane using vtkCutter, but I think this will not quite work for your purposes because it looks like vtkCutter uses an implicitly described surface (easy for a plane but maybe less so for your vessel segments).  I also found this link: <a href="https://kitware.github.io/vtk-examples/site/Cxx/ImageData/IntersectLine/">https://kitware.github.io/vtk-examples/site/Cxx/ImageData/IntersectLine/</a>, which seems closer to what you are trying to do, but again may not be exactly it.</p>
<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a>, do you have any suggestions?</p>

---

## Post #6 by @mau_igna_06 (2022-04-22 17:32 UTC)

<p>Hi.</p>
<p>To find the intersection of centerline (only one branch) and the tumor surface (created from the segment) I would recommend to get the internal polydata representacion of the simply displayed centerline curve (that’s a 3d model) and use the module CombineModels to get the intesection with the tumor model. Then extract the centerline of the resulting model.</p>
<p>Hope it helps</p>

---

## Post #7 by @lassoan (2022-04-23 05:47 UTC)

<p>Both CombineModels and vtkCutter should give you the intersection point coordinates. vtkCutter needs a implicit function as input, which you can get from the tumor polydata using vtkImplicitPolyDataDistance filter.</p>

---

## Post #8 by @gfurnari (2022-04-24 14:30 UTC)

<p>Thank you very much for your replies, <a class="mention" href="/u/mikebind">@mikebind</a>, <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> and <a class="mention" href="/u/lassoan">@lassoan</a> .<br>
Actually, I can’t find CombineModels module. where can i find it?<br>
Sorry, i’m quite new with 3d slicer.</p>

---

## Post #9 by @lassoan (2022-04-24 19:06 UTC)

<aside class="quote no-group" data-username="gfurnari" data-post="8" data-topic="23070">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/a4c791/48.png" class="avatar"> gfurnari:</div>
<blockquote>
<p>I can’t find CombineModels module. where can i find it?</p>
</blockquote>
</aside>
<p>It is provided by the <a href="https://github.com/PerkLab/SlicerSandbox#slicersandbox">Sandbox extension</a>.</p>

---

## Post #10 by @gfurnari (2022-04-25 14:09 UTC)

<p>is it available for 4.11.2 version?</p>

---

## Post #11 by @lassoan (2022-04-25 14:11 UTC)

<p>You need to use the latest Slicer Preview Release. It will become the new Slicer Stable Release very soon anyway.</p>

---

## Post #12 by @gfurnari (2022-04-26 11:55 UTC)

<p>Hi, i tried with CombineModules method but if i use 3d model of centerline polydata representation and tumor, it does create the intersection model but it is not displayed and if i use it to extract centerline, an error tells me that “valid input surface is required”</p>

---

## Post #13 by @gfurnari (2022-04-26 12:23 UTC)

<p>in fact, if i check properties of the model created, surface area, volume, number of points and number of cells are all to zero</p>

---

## Post #14 by @lassoan (2022-04-30 04:11 UTC)

<p>Artery is a polyline, tumor is a surface, therefore the intersection of the two is just a set of points.</p>
<p>What would you like to achieve?</p>

---

## Post #17 by @gfurnari (2022-04-27 12:57 UTC)

<p>Hi everyone,<br>
i’ve already asked something like this, but i want to explain better what i’m trying to find out.<br>
Basically i have artery and tumor segmentation and i extracted artery centerline curve (with hierachy).</p>
<ol>
<li>I would like to understand which of the branches of the centerline curve intersects with the tumor ;</li>
<li>once i found the branch(es), i want to go back up in the hierarchy to the main branch (‘Centerline curve(0)’ );</li>
<li>possibly doing all by code.</li>
</ol>
<p>Do you have any ideas on how to do to something like this?</p>
<p>Thank you very much, guys.</p>

---

## Post #19 by @lassoan (2022-05-02 12:21 UTC)

<aside class="quote no-group" data-username="gfurnari" data-post="17" data-topic="23070">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/a4c791/48.png" class="avatar"> gfurnari:</div>
<blockquote>
<ul>
<li>I would like to understand which of the branches of the centerline curve intersects with the tumor ;</li>
<li>once i found the branch(es), i want to go back up in the hierarchy to the main branch (‘Centerline curve(0)’ );</li>
</ul>
</blockquote>
</aside>
<p>This should not be a problem at all.</p>
<p>One option is to use <a href="https://vtk.org/doc/nightly/html/classvtkCutter.html">vtkCutter</a> on a polydata that contains all branches. This works if the cutter preserves cell data in the output, because then you can add cell IDs as a cell array (using <a href="https://vtk.org/doc/nightly/html/classvtkIdFilter.html">vtkIdFilter</a>) and in the output cell or point data you’ll have the IDs of all branches that had intersection point.</p>
<p>If vtkCutter does preserve cell data then you can use vtkCutter on one branch at a time. If the output is non-empty then you know that the branch intersects the surface. For this, you can use markup curves: iterate through the curves in the subject hierarchy and get the polydata of each curve using <code>curveNode.GetCurveWorld()</code>.</p>

---

## Post #20 by @gfurnari (2022-05-05 14:24 UTC)

<p>Thank you very, it was very helpful!</p>

---
