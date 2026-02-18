# Multi volume rendering

**Topic ID**: 760
**Date**: 2017-07-25
**URL**: https://discourse.slicer.org/t/multi-volume-rendering/760

---

## Post #1 by @nih (2017-07-25 12:42 UTC)

<p>Hello world,</p>
<p>I recently wrote an extension to import GE 3D/4D ultrasound (US) data into 3DSlicer. Right now, my colleagues and me want to visualise the 3D US volume along with (registered) preop. digital substraction angiography data. However, we found that there used to be a multi volume rendering feature which is not supported anymore. Can someone remember the reasons for this?</p>
<p>Are there any recent developments towards multi volume rendering? Actually, there even seems to be a pretty nice VTK extension enabling this functionality using raycasting [1]. Therefore, we were thinking about extending Slicer rendering engine by this approach. Would that make sense?</p>
<p>Best,<br>
Nico</p>
<p>[1] (Bozorgi, 2015) / <a href="https://github.com/bozorgi/VTKMultiVolumeRayCaster" rel="nofollow noopener">https://github.com/bozorgi/VTKMultiVolumeRayCaster</a></p>

---

## Post #2 by @lassoan (2017-07-25 12:47 UTC)

<p>Multi-volume rendering is being added to VTK8, so in Slicer we won’t specifically work on developing this feature in Slicer. Once the feature is available in VTK, we’ll update Slicer GUI accordingly.</p>
<p>Till then, probably your best bet is to create 3D actors from your DSA volume using Segment editor (there are lots of semi-automatic tools that can provide nice visualization of bones and soft tissues with a couple of minutes of manual work). You can use VMTK to create nice vessel tree (vesselness filtering, level set filtering, centerline extraction).</p>

---

## Post #3 by @pieper (2017-07-25 20:28 UTC)

<p>If you want to try some experiments with the bozorgi multivolume code it would be interesting to know how they work out.  Slicer’s VolumeRendering module should be fairly easy to extend, and the MRML level already supports associating independent rendering parameters per-volume.</p>
<p>Regarding your question about why the older multivolume renderer was removed, it was a support issue.  GPU code can be somewhat fragile and hard to debug across devices, so it helps to have a actively maintained and widely used code base.  Driver issues, memory limitations, device-specific rendering artifacts, etc can all eat up a lot of debugging time.</p>

---
