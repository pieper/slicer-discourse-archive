---
topic_id: 36005
title: "Change Active Widget"
date: 2024-05-08
url: https://discourse.slicer.org/t/36005
---

# Change active widget

**Topic ID**: 36005
**Date**: 2024-05-08
**URL**: https://discourse.slicer.org/t/change-active-widget/36005

---

## Post #1 by @dfajtai (2024-05-08 20:22 UTC)

<p>I am curious if there is a way to jump from one module to another programmatically using Python.</p>
<p>I have a module in which several automatic segmentations were generated. I would like to give an easy option for the user to jump into the SegmentEditor widget - which was previously configured by certain parameters -  showing a certain segmentation over a given master volume.</p>
<p>So far I have tried this:</p>
<pre><code class="lang-auto">self.segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
self.segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
self.segmentEditorNode =slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
self.segmentEditorWidget.setMRMLSegmentEditorNode(self.segmentEditorNode)
</code></pre>
<p>then later on</p>
<pre><code class="lang-auto">self.segmentEditorWidget.show()
</code></pre>
<p>but this shows the widget inside a floating window.</p>
<p>So the question is, what is the right way, to show a docked version of the parametrized SegmentEditorWidget?</p>

---

## Post #2 by @rfenioux (2024-05-13 07:53 UTC)

<p>This is the expected behavior when creating a new widget, unless you integrate it into the layout of your module. I think what you want is to configure the existing segment editor widget instance, then jump to the segment editor module.</p>
<pre><code class="lang-auto">segmentEditorWidget = slicer.modules.SegmentEditorWidget.editor
# setup things ...
segmentEditorWidget.setActiveEffectByName("Threshold")
</code></pre>
<p>switch to module<br>
<code>slicer.util.selectModule("SegmentEditor")</code></p>

---

## Post #4 by @dfajtai (2024-05-17 07:53 UTC)

<p>As you said this needs an existing segment editor widget. But it is instantiated only if the user opens the segment editor module previously. By opening the segment editor, 3 nodes are generated: a vtkMRMLSegmentEditorNode, a vtkMRMLSegmentationNode, and a vtkMRMLSegmentationDisplayNode.</p>
<p>By calling</p>
<pre><code class="lang-auto">slicer.util.selectModule("SegmentEditor")
</code></pre>
<p>later on, will show this instance of the segment editor - not the one I have instantiated manually.</p>
<p>So the question still remains, but a bit altered:<br>
How can one create all these three nodes, without opening the segment editor?</p>
<p>Since then I have 2 solutions: switching back and forth between the segment editor and my module, or switching to the segment editor - which ensures that there is an instance I can parameterize - and then make the changes I want to.</p>

---
