# Cannot get label layer and foreground layer volumes

**Topic ID**: 20588
**Date**: 2021-11-11
**URL**: https://discourse.slicer.org/t/cannot-get-label-layer-and-foreground-layer-volumes/20588

---

## Post #1 by @Shazam_L (2021-11-11 21:20 UTC)

<p>Hello,</p>
<p>I seem to get background layer volume but everything else is nullptr.<br>
I can visually see segmentations and there is a labellayer present<br>
This is my setup</p>
<pre><code class="lang-auto">vtkSlicerApplicationLogic* appLogic = vtkSlicerApplicationLogic::SafeDownCast(
    qSlicerApplication::application()-&gt;applicationLogic()
  );
  if (!appLogic) return theList;
  d-&gt;sliceLogic = vtkMRMLSliceLogic::SafeDownCast(
    appLogic-&gt;GetSliceLogic(sliceNode)
  );
  if (!d-&gt;sliceLogic) return theList;

  layerLogic["B"] = vtkMRMLSliceLayerLogic::SafeDownCast(d-&gt;sliceLogic-&gt;GetBackgroundLayer());
  layerLogic["F"] = vtkMRMLSliceLayerLogic::SafeDownCast(d-&gt;sliceLogic-&gt;GetForegroundLayer());
  layerLogic["L"] = vtkMRMLSliceLayerLogic::SafeDownCast(d-&gt;sliceLogic-&gt;GetLabelLayer());
 // Some loop
      volumeNode = vtkMRMLVolumeNode::SafeDownCast(
           d-&gt;sliceLogic-&gt;GetLayerVolumeNode(i)
       );
</code></pre>

---

## Post #2 by @lassoan (2021-11-12 05:55 UTC)

<p>Segmentations are not displayed using slice layers, but by they have their own displayable manager. You can change a segmentation node’s display properties via its display node.</p>

---
