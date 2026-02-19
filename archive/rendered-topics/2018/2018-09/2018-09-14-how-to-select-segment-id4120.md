---
topic_id: 4120
title: "How To Select Segment"
date: 2018-09-14
url: https://discourse.slicer.org/t/4120
---

# How to select segment

**Topic ID**: 4120
**Date**: 2018-09-14
**URL**: https://discourse.slicer.org/t/how-to-select-segment/4120

---

## Post #1 by @timeanddoctor (2018-09-14 16:00 UTC)

<p>I have two segment “skin1” and “skin2”. And when I apply threshold with CLI, I donot know how to select the second one. I don’t know how to set parameters for skin2<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c3f5fbd95bf06ae8d4cd0bdfcf7fe54a2dd3d51.jpeg" alt="360%E6%88%AA%E5%9B%BE-406308453" data-base62-sha1="8AYqqXc62lT0yu0uKzcqXdMHgyd" width="202" height="44"></p>
<pre><code># Thresholding
segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold","54")  
effect.setParameter("MaximumThreshold","78")
effect.self().onApply()
</code></pre>

---

## Post #2 by @cpinter (2018-09-14 16:20 UTC)

<p>This should do the trick<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.h#L212" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.h#L212" target="_blank">Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.h#L212</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="202" style="counter-reset: li-counter 201 ;">
<li>/// Set segmentation MRML node</li>
<li>void setSegmentationNode(vtkMRMLNode* node);</li>
<li>/// Set segmentation MRML node by its ID</li>
<li>void setSegmentationNodeID(const QString&amp; nodeID);</li>
<li>/// Set master volume MRML node</li>
<li>void setMasterVolumeNode(vtkMRMLNode* node);</li>
<li>/// Set master volume MRML node by its ID</li>
<li>void setMasterVolumeNodeID(const QString&amp; nodeID);</li>
<li>
</li>
<li>/// Set selected segment by its ID</li>
<li class="selected">void setCurrentSegmentID(const QString segmentID);</li>
<li>
</li>
<li>/// Set active effect by name</li>
<li>void setActiveEffectByName(QString effectName);</li>
<li>
</li>
<li>/// Save current segmentation before performing an edit operation</li>
<li>/// to allow reverting to the current state by using undo</li>
<li>void saveStateForUndo();</li>
<li>
</li>
<li>/// Update modifierLabelmap, maskLabelmap, or alignedMasterVolumeNode</li>
<li>void updateVolume(void* volumePtr, bool&amp; success);</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #3 by @timeanddoctor (2018-09-14 16:47 UTC)

<p>OK, Csaba Pinter, thank you very much.<br>
Another problem,  can I define the color of a segment<br>
<code>addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("skin11",*red*)</code></p>

---

## Post #4 by @cpinter (2018-09-14 17:25 UTC)

<p>To change the primary color of the segment (that is also saved to disk etc.)</p>
<pre><code>s=getNode('vtkMRMLSegmentationNode1')
se=s.GetSegmentation()
seg=se.GetSegment('Segment_1')
seg.SetColor(1,0,0)
</code></pre>
<p>To change the override color (only for display)</p>
<pre><code>d=s.GetDisplayNode()
d.SetSegmentOverrideColor('Segment_1', 0,1,0)</code></pre>

---

## Post #5 by @timeanddoctor (2018-09-15 08:51 UTC)

<p>Thank you very much.</p>

---
