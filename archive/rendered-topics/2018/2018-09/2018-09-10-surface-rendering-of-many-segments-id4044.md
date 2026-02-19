---
topic_id: 4044
title: "Surface Rendering Of Many Segments"
date: 2018-09-10
url: https://discourse.slicer.org/t/4044
---

# surface rendering of many segments

**Topic ID**: 4044
**Date**: 2018-09-10
**URL**: https://discourse.slicer.org/t/surface-rendering-of-many-segments/4044

---

## Post #1 by @Adriana_Zlahoda (2018-09-10 13:32 UTC)

<p>Slicer version:4.9.0<br>
Hi,<br>
I performed all heart segmentation from CT data. Now I want to render all segments in 3D assuming that all bordering segments have a common contact surface. Although during segmentation my segments are perfectly matched in slicer, during surface rendering I get separated surfaces…</p>
<p>Is it possible in slicer / any other software package?</p>

---

## Post #2 by @cpinter (2018-09-10 15:09 UTC)

<p>If you disable smoothing then the forced contact won’t be lost when converting to surfaces. Please note that this phenomenon only happens for visualization, and the underlying labelmap data is still contiguous. You can disable smoothing in the Segment Editor by clicking the small arrow next to Show 3D, or in the Segmentations module by changing the conversion parameter if you click Update on the Closed surface representation.</p>

---

## Post #3 by @pieper (2018-09-10 21:45 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> wouldn’t it be better to use <a href="https://www.vtk.org/pipermail/vtkusers/2017-December/100502.html">joint smoothing?</a></p>

---

## Post #4 by @lassoan (2018-09-11 04:42 UTC)

<p>We have that option in Smoothing effect but not in the automatic conversion between segment representations. The assumption is that smoothing operation in “binary labelmap to closed surface” conversion is only used for removing staircase artifacts and so it does not require adjustment of the geometry.</p>
<p>We would need to implement some new mechanism in segmentation infrastructure to allow joint conversion of multiple segments, because right now conversion happens segment by segment.</p>

---

## Post #5 by @cpinter (2018-09-11 12:45 UTC)

<p>Joint smoothing works on labelmaps. The user’s problem is about the surfaces shown in 3D which are converted from the labelmaps. This conversion is temporary and is only for visualization.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I don’t think we need to implement a new converter for this. It would basically mean a new representation type, some “topologically correct surface”, but it would mean the same or more interaction from the user than simply disabling smoothing. I assume that if the user needs to preserve this property on the segments then they won’t care about staircase artifacts.</p>

---

## Post #6 by @pieper (2018-09-11 13:09 UTC)

<p>The joint smoothing results are very useful in my opinion because they look more like real anatomy with smooth surfaces and no gaps between the structures.  This is useful even if the conversion is only temporary.</p>

---

## Post #7 by @cpinter (2018-09-11 13:22 UTC)

<p>If there is a converter in VTK that converts labelmaps to a set of surfaces preserving the joint edges, then it should not be hard to add. On a second thought, we probably wouldn’t need a new representation, but an option in the converter would be enough and we could expose it in segment editor the same way as smoothing. If there is no such converter though, then this would be a major project.</p>

---

## Post #8 by @pieper (2018-09-11 13:58 UTC)

<p>It would the same pipeline as the JointSmoothing option of <a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/ModelMaker">the ModelMaker</a>.  <a href="https://github.com/Slicer/Slicer/blob/master/Modules/CLI/ModelMaker/ModelMaker.cxx">The code</a> is pretty hard to follow but I’d think it could be ported.</p>

---

## Post #9 by @cpinter (2018-09-11 14:04 UTC)

<p>I added a Mantis issue for this: <a href="https://issues.slicer.org/view.php?id=4604">https://issues.slicer.org/view.php?id=4604</a></p>
<p>I think we have a good plan, so implementing it is now a matter of priorities.</p>

---

## Post #10 by @sarvpriya1985 (2018-12-27 15:57 UTC)

<p>Hi,<br>
How is 3D surface rendering different from 3D segmentation of heart and how is it used.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #11 by @lassoan (2018-12-27 16:35 UTC)

<p>When you segment structures then they are displayed in 3D views using surface rendering.</p>

---
