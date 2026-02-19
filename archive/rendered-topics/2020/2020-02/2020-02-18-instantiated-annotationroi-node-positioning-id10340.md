---
topic_id: 10340
title: "Instantiated Annotationroi Node Positioning"
date: 2020-02-18
url: https://discourse.slicer.org/t/10340
---

# Instantiated AnnotationROI node positioning

**Topic ID**: 10340
**Date**: 2020-02-18
**URL**: https://discourse.slicer.org/t/instantiated-annotationroi-node-positioning/10340

---

## Post #1 by @adelmo (2020-02-18 17:32 UTC)

<p>Hello,</p>
<p>I would like to instantiate, via Python code, an AnnotationROI node and I would like to automatically position the generated bounding box to enclose exactly a volume node.<br>
I am sure it is a super simple operation but I can’t manage to do it using the SetXYZ and the SetRadiusXYZ methods.<br>
Could somebody help me?</p>
<p>Thank you,<br>
AD</p>

---

## Post #2 by @lassoan (2020-02-18 17:44 UTC)

<p>You can use <code>slicer.modules.cropvolume.logic().FitROIToInputVolume()</code> method to fit a ROI node to a volume.</p>

---
