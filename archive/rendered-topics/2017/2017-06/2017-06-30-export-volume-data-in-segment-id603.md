---
topic_id: 603
title: "Export Volume Data In Segment"
date: 2017-06-30
url: https://discourse.slicer.org/t/603
---

# Export volume data in segment?

**Topic ID**: 603
**Date**: 2017-06-30
**URL**: https://discourse.slicer.org/t/export-volume-data-in-segment/603

---

## Post #1 by @hherhold (2017-06-30 11:38 UTC)

<p>Is it possible to export the volume data in a segment? Meaning, using the Segment Editor, you create a segment, then export a TIFF stack or NRRD with the same volume size as your original data set, but with just the data in your segment, all other voxels at 0?</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @cpinter (2017-06-30 11:51 UTC)

<p>In Segmentations module open the Import/Export section and export the segments into labelmap. If you have overlapping structures you need to export each to a different labelmap. Then you can click Save in the toolbar or main menu and export the labelmap to nrrd</p>

---

## Post #3 by @hherhold (2017-06-30 12:07 UTC)

<p>Thanks for the reply Csaba.</p>
<p>This exports just the label map, with areas in the label as 1 and outside as zero. Is there a way to do the exact same thing, but exporting the volume data inside that label map? Meaning the greyscale values, not just the 1/0 inside/outside the label map.</p>
<p>Thanks!!!</p>
<p>-Hollister</p>

---

## Post #4 by @cpinter (2017-06-30 12:21 UTC)

<p>Ah I see. You can use the Mask Scalar Volume module</p>

---

## Post #5 by @hherhold (2017-06-30 13:44 UTC)

<p>Exactly what I was looking for. I <em>knew</em> there had to be a way!</p>
<p>Thanks!!</p>
<p>-Hollister</p>

---

## Post #6 by @fedorov (2019-11-21 23:51 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> is there an easy way to do this programmatically, is there a “recipe” somewhere?</p>
<p>If I understand correctly, this function is doing the export, but at this point I cannot quickly figure out how to get to it from python. I was also not sure if parameterizing the export through the widget is the only approach to do this.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/qSlicerSegmentationsModuleWidget.cxx#L821-L941" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/qSlicerSegmentationsModuleWidget.cxx#L821-L941" target="_blank">Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/qSlicerSegmentationsModuleWidget.cxx#L821-L941</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="821" style="counter-reset: li-counter 820 ;">
<li>bool qSlicerSegmentationsModuleWidget::exportFromCurrentSegmentation()</li>
<li>{</li>
<li>  Q_D(qSlicerSegmentationsModuleWidget);</li>
<li>
</li>
<li>  vtkMRMLSubjectHierarchyNode* shNode = vtkMRMLSubjectHierarchyNode::GetSubjectHierarchyNode(this-&gt;mrmlScene());</li>
<li>  if (!shNode)</li>
<li>    {</li>
<li>    qCritical() &lt;&lt; Q_FUNC_INFO &lt;&lt; ": Failed to access subject hierarchy node";</li>
<li>    return false;</li>
<li>    }</li>
<li>
</li>
<li>  vtkMRMLSegmentationNode* currentSegmentationNode =  vtkMRMLSegmentationNode::SafeDownCast(</li>
<li>    d-&gt;MRMLNodeComboBox_Segmentation-&gt;currentNode() );</li>
<li>  if (!currentSegmentationNode || !currentSegmentationNode-&gt;GetSegmentation())</li>
<li>    {</li>
<li>    qWarning() &lt;&lt; Q_FUNC_INFO &lt;&lt; ": No segmentation selected";</li>
<li>    return false;</li>
<li>    }</li>
<li>
</li>
<li>  // Get IDs of segments to be exported</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/qSlicerSegmentationsModuleWidget.cxx#L821-L941" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #7 by @fedorov (2019-11-21 23:53 UTC)

<p>Found this thread: <a href="https://discourse.slicer.org/t/get-label-map-node-from-segmentation-node/1137/3" class="inline-onebox">Get label map node from segmentation node</a> that also discusses programmatic use. Let me study that first!</p>

---

## Post #8 by @cpinter (2019-11-29 16:48 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> Sounds good. Sorry for not reacting, I’m still in the process of moving continents. However, now the move itself is done and I’m gradually getting back to normal. Let me know if you need any guidance!</p>

---

## Post #9 by @fedorov (2019-11-29 17:30 UTC)

<p>No worries Csaba, I figured it out - Discourse search was very handy to locate that thread, and <a class="mention" href="/u/lassoan">@lassoan</a> helped with the bits I was missing. Good luck with the move, and settling down at the new place!</p>

---
