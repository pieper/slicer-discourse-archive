---
topic_id: 17037
title: "Automatic Endpoint Selection Outside Of Surface Module"
date: 2021-04-12
url: https://discourse.slicer.org/t/17037
---

# Automatic endpoint selection outside of surface module

**Topic ID**: 17037
**Date**: 2021-04-12
**URL**: https://discourse.slicer.org/t/automatic-endpoint-selection-outside-of-surface-module/17037

---

## Post #1 by @perecanals (2021-04-12 10:40 UTC)

<p>Hi,</p>
<p>I am trying to extract centerlines from vascular models using the automatic endpoint selection from the VMTK module in Slicer, and in some cases (I’d say in about 10-20% of cases) I come across an error which gets the centerline computation stuck:</p>
<pre><code>Warning: In /Volumes/D/S/S-0-build/VTK/Common/DataModel/vtkPolyData.cxx, line 993 
vtkPolyData (0x7fe922612940): Building VTK_LINE 15 with only one point, but VTK_LINE needs at 
least two points. Check the input.
</code></pre>
<p>Investigating this issue, I found that this happens when at least one of the endpoints is placed outside of the volume closed by the surface model of the vascular structure in a given case, and I can avoid the issue by manually placing the problematic endpoint/s inside of the model. However, I want to keep the whole process automatic. Is there a way to fix that?</p>
<p>Thank you,</p>

---

## Post #2 by @perecanals (2021-04-12 16:41 UTC)

<p>Of course, I meant surface model* in the topic. Sorry about that.</p>

---
