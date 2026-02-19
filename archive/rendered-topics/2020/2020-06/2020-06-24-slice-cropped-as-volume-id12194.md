---
topic_id: 12194
title: "Slice Cropped As Volume"
date: 2020-06-24
url: https://discourse.slicer.org/t/12194
---

# Slice cropped as volume

**Topic ID**: 12194
**Date**: 2020-06-24
**URL**: https://discourse.slicer.org/t/slice-cropped-as-volume/12194

---

## Post #1 by @ada (2020-06-24 09:40 UTC)

<p>Hi all,</p>
<p>I have a 3D volume and I would like to display the ‘Red’ slice view.<br>
In python, it is working using :<br>
red = slicer.util.getNode(‘vtkMRMLSliceNodeRed’)<br>
red.SetSliceVisible(1)</p>
<p>Nevertheless the slice is extended to the all volume FOV. How can I display the slice inside the roi node defined by the user ?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2020-06-25 21:22 UTC)

<p>After you cropped the volume, select the cropped volume as background in the slice view. You can use <code>slicer.util.setSliceViewerLayers</code> for this.</p>

---
