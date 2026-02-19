---
topic_id: 41102
title: "Creating And Exporting 2D Bounding Boxes For Each Slice For"
date: 2025-01-15
url: https://discourse.slicer.org/t/41102
---

# Creating and Exporting 2D Bounding Boxes for Each Slice for Deep Learning Training

**Topic ID**: 41102
**Date**: 2025-01-15
**URL**: https://discourse.slicer.org/t/creating-and-exporting-2d-bounding-boxes-for-each-slice-for-deep-learning-training/41102

---

## Post #1 by @zupl1234 (2025-01-15 23:26 UTC)

<p>Hi,</p>
<p>I am working on annotating medical images (CT &amp; MRI) using 3D Slicer, and I have the following use case:</p>
<p>I need to:</p>
<ol>
<li>Annotate specific regions of interest by creating <strong>2D bounding boxes</strong> on <strong>each slice</strong> individually.</li>
<li>Extract the <strong>2D coordinates</strong> (X, Y) of the 4 corners of each bounding box for future use in training a deep learning model.</li>
</ol>
<p>Could you please clarify:</p>
<ul>
<li>Is it possible to create 2D bounding boxes per slice in 3D Slicer?</li>
<li>How can I extract the 2D coordinates of each bounding box?</li>
<li>In what format can these annotations be exported (e.g., JSON, CSV, etc.) to facilitate their use in deep learning pipelines?</li>
</ul>
<p>Thank you</p>

---

## Post #2 by @pieper (2025-01-15 23:33 UTC)

<p>Yes, that should be quite easy if you are willing to do some python scripting.  Otherwise not really.</p>

---
