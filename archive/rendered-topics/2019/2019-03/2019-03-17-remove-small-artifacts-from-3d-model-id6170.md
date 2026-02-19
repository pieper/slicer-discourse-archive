---
topic_id: 6170
title: "Remove Small Artifacts From 3D Model"
date: 2019-03-17
url: https://discourse.slicer.org/t/6170
---

# Remove small artifacts from 3d model

**Topic ID**: 6170
**Date**: 2019-03-17
**URL**: https://discourse.slicer.org/t/remove-small-artifacts-from-3d-model/6170

---

## Post #1 by @Michael_Ef (2019-03-17 11:00 UTC)

<p>Hello,</p>
<p>I reconstructed a 3d model of prostate glands from histological slides by marching cubes algorithm. In my model I have a lot of small contours that i do not want to have in the model. Is there a way (e.g. a vtk filter) to extract these contours by setting a minimum size for these contours? Similar to the vtkConnectivityFilter where you can extract the largest region!?</p>
<p>Thanks a lot in advance.</p>
<p>Regards Michael</p>

---

## Post #2 by @cpinter (2019-03-17 12:40 UTC)

<p>The Islands effect in Segment Editor can do this, here’s the code:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorIslandsEffect.py#L121-L208" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorIslandsEffect.py#L121-L208" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorIslandsEffect.py#L121-L208</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="121" style="counter-reset: li-counter 120 ;">
<li>def splitSegments(self, minimumSize = 0, maxNumberOfSegments = 0, split = True):</li>
<li>  """</li>
<li>  minimumSize: if 0 then it means that all islands are kept, regardless of size</li>
<li>  maxNumberOfSegments: if 0 then it means that all islands are kept, regardless of how many</li>
<li>  """</li>
<li>  # This can be a long operation - indicate it to the user</li>
<li>  qt.QApplication.setOverrideCursor(qt.Qt.WaitCursor)</li>
<li>
</li>
<li>  self.scriptedEffect.saveStateForUndo()</li>
<li>
</li>
<li>  # Get modifier labelmap</li>
<li>  selectedSegmentLabelmap = self.scriptedEffect.selectedSegmentLabelmap()</li>
<li>
</li>
<li>  castIn = vtk.vtkImageCast()</li>
<li>  castIn.SetInputData(selectedSegmentLabelmap)</li>
<li>  castIn.SetOutputScalarTypeToUnsignedInt()</li>
<li>
</li>
<li>  # Identify the islands in the inverted volume and</li>
<li>  # find the pixel that corresponds to the background</li>
<li>  islandMath = vtkITK.vtkITKIslandMath()</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorIslandsEffect.py#L121-L208" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Is there a good reason for using low-level VTK functions instead of Segment Editor? You’re using Slicer I assume so why not use its features?</p>

---
