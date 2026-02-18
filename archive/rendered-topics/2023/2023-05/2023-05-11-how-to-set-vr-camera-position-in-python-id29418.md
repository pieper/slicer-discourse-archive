# How to set VR camera position in Python?

**Topic ID**: 29418
**Date**: 2023-05-11
**URL**: https://discourse.slicer.org/t/how-to-set-vr-camera-position-in-python/29418

---

## Post #1 by @Gianluca_De_Lucia (2023-05-11 21:25 UTC)

<p>Hi,<br>
I am trying to develop a Python script for viewing an STL file through your VR module for 3DSlicer.<br>
I need to set up the camera position, but as far I didn’t succeed.<br>
I tried with:</p>
<blockquote>
<p>slicer.modules.virtualreality.viewWidget().renderWindow().GetRenderers().GetItemAsObject(0).SetViewPoint(position)</p>
</blockquote>
<p>but it has no effect in the viewer.</p>
<p>Can you help me with this?</p>

---

## Post #2 by @cpinter (2023-05-12 10:02 UTC)

<p>Based on the information you gave I’m not sure what it is exactly that you want, but I think this function may help <a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/VirtualReality/Widgets/qMRMLVirtualRealityView.h#L98" class="inline-onebox">SlicerVirtualReality/qMRMLVirtualRealityView.h at master · KitwareMedical/SlicerVirtualReality · GitHub</a></p>

---
