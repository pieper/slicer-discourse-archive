---
topic_id: 26162
title: "Segment Geometry Transformation Using Python Interactor"
date: 2022-11-09
url: https://discourse.slicer.org/t/26162
---

# Segment Geometry Transformation using python interactor

**Topic ID**: 26162
**Date**: 2022-11-09
**URL**: https://discourse.slicer.org/t/segment-geometry-transformation-using-python-interactor/26162

---

## Post #1 by @hourglassnam (2022-11-09 15:09 UTC)

<p>Hello~!<br>
I was trying to use Segment Geometry using python interactor.<br>
I figure out how to get the statistic data but could not make the transformation to work.</p>
<p>I tried below script and got following error message.</p>
<pre><code class="lang-auto">import SegmentGeometry
SegGeoLogic = SegmentGeometry.SegmentGeometryLogic()
SegGeoLogic.getParameterNode().SetParameter(volumeName, sourceNode.GetID())
slicer.modules.SegmentGeometryWidget.onPrincipalAxes()
</code></pre>
<blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:/Users/njy95/AppData/Local/NA-MIC/Slicer 5.1.0-2022-09-27/NA-MIC/Extensions-31161/SegmentGeometry/lib/Slicer-5.1/qt-scripted-modules/SegmentGeometry.py”, line 395, in onPrincipalAxes<br>
segName = segmentationNode.GetName()<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetName’</p>
</blockquote>
<p>I thought I did setup Segmentation node for the transformation, so I cannot figure out what went wrong!</p>
<p>I will be glad to hear any advice on how to use the onPrincipalAxes for the Segment Geometry Transformation.<br>
Thank you in advance!</p>

---

## Post #2 by @lassoan (2022-12-01 07:32 UTC)

<p>If <a class="mention" href="/u/jmhuie">@jmhuie</a> does not respond here soon then you can submit a question as an issue in the <a href="https://github.com/jmhuie/Slicer-SegmentGeometry">extension’s repository</a>.</p>

---

## Post #3 by @jmhuie (2022-12-01 20:51 UTC)

<p>I’ll admit that I have not tested how well SegmentGeometry works using the python terminal. I will see if I can get to the root of the problem and get back to you <a class="mention" href="/u/hourglassnam">@hourglassnam</a>.</p>

---

## Post #4 by @jmhuie (2022-12-09 14:45 UTC)

<p>Hi <a class="mention" href="/u/hourglassnam">@hourglassnam</a></p>
<p>When using the sample data for SegmentGeometry, this chunk of code worked for me. Give this ago and let me know if it doesn’t work. You’ll need to define the volumenode, the segmentation node, and the segment you want to use.</p>
<pre><code class="lang-auto">volumeNode = getNode("DemoForelimb")
segmentationNode = getNode("DemoSegment")

slicer.modules.segmentgeometry.widgetRepresentation()
slicer.modules.SegmentGeometryWidget.ui.segmentationSelector.setCurrentNode(segmentationNode)
slicer.modules.SegmentGeometryWidget.ui.regionSegmentSelector.setCurrentSegmentID("Humerus")
slicer.modules.SegmentGeometryWidget.ui.volumeSelector.setCurrentNode(volumeNode)
slicer.modules.SegmentGeometryWidget.onPrincipalAxes()
</code></pre>

---
