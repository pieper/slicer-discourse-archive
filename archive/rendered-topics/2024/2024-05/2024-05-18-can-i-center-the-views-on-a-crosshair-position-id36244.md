---
topic_id: 36244
title: "Can I Center The Views On A Crosshair Position"
date: 2024-05-18
url: https://discourse.slicer.org/t/36244
---

# Can I center the views on a crosshair position?

**Topic ID**: 36244
**Date**: 2024-05-18
**URL**: https://discourse.slicer.org/t/can-i-center-the-views-on-a-crosshair-position/36244

---

## Post #1 by @sullivak (2024-05-18 03:03 UTC)

<p>Hi. I can set the location of crosshairs, e.g.<br>
slicer.mrmlScene.GetNodesByClass(‘vtkMRMLCrosshairNode’).GetItemAsObject(0).SetCrosshairRAS(point)</p>
<p>but is there a way to re-center the views on that location?</p>

---

## Post #2 by @cpinter (2024-05-20 12:20 UTC)

<p>You can use this API:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLSliceNode.h#L373-L387">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLSliceNode.h#L373-L387" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLSliceNode.h#L373-L387" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLSliceNode.h#L373-L387</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="373" style="counter-reset: li-counter 372 ;">
          <li>/// Set the RAS offset of the Slice to the passed values. JumpSlice</li>
          <li>/// and JumpAllSlices use the JumpMode to determine how to jump.</li>
          <li>void JumpSlice(double r, double a, double s);</li>
          <li>void JumpAllSlices(double r, double a, double s);</li>
          <li>/// Jump all slices in the scene.</li>
          <li>/// viewGroup can be used to jump only slice views that are in a specific group.</li>
          <li>/// By default viewGroup is set to -1, which means that all slice views are jumped.</li>
          <li>/// If a non-nullptr exclude pointer is specified then position of that slice node will not be changed.</li>
          <li>/// If jumpMode is set to vtkMRMLSliceNode::DefaultJumpSlice then jump mode set in the slice node will be used.</li>
          <li>/// specified in the slice node will be used.</li>
          <li>static void JumpAllSlices(vtkMRMLScene* scene, double r, double a, double s,</li>
          <li>  int jumpMode = vtkMRMLSliceNode::DefaultJumpSlice, int viewGroup = -1, vtkMRMLSliceNode* exclude = nullptr);</li>
          <li>void JumpSliceByOffsetting(double r, double a, double s);</li>
          <li>void JumpSliceByOffsetting(int k, double r, double a, double s);</li>
          <li>void JumpSliceByCentering(double r, double a, double s);</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @sullivak (2024-05-20 21:23 UTC)

<p>Thanks, that did the trick!</p>
<p>Not sure if this is the exact right way, but it worked:</p>
<pre><code class="lang-auto">def set_ras_coords(point: list[float]):
    slicer.mrmlScene.GetNodesByClass('vtkMRMLCrosshairNode').GetItemAsObject(0).SetCrosshairRAS(point)
    sliceNodes = list(slicer.mrmlScene.GetNodesByClass('vtkMRMLSliceNode'))
    for sliceNode in sliceNodes:
        sliceNode.JumpAllSlices(point[0], point[1], point[2])
</code></pre>

---
