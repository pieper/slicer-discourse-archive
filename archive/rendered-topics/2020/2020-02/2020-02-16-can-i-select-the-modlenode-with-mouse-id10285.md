# Can I select the modleNode with mouse?

**Topic ID**: 10285
**Date**: 2020-02-16
**URL**: https://discourse.slicer.org/t/can-i-select-the-modlenode-with-mouse/10285

---

## Post #1 by @timeanddoctor (2020-02-16 00:22 UTC)

<p>The slicer can select the markupFiducials with mouse but I donnot know can I use the mouse select the modelNode?</p>

---

## Post #2 by @Davide_Punzo (2020-02-20 08:02 UTC)

<p>I think there is no “ready-to-use” infrastructure for this, but you can:</p>
<ol>
<li>Use a callback to observe the mouse clicks in the 3d view (see <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.cxx#L2565" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.cxx#L2565</a>);</li>
<li>when you process the events, you get the model display manager from the view ;</li>
<li>you get the mouse event position from the interactor;</li>
<li>you call the display manager Pick method (this will return the cellID, the modelNodeId and the RAS coordinates of the picking).</li>
</ol>
<p>Another option, it would also to write a custom model display manager, or you can have a look at <a href="https://discourse.slicer.org/t/select-cells-of-a-3d-model/7753" class="inline-onebox">Select cells of a 3D model</a> (where you can use the crosshair or a markup point, which involves much less coding).</p>

---
