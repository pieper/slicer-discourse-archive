---
topic_id: 851
title: "Set Segmentation Master Volume From Python"
date: 2017-08-09
url: https://discourse.slicer.org/t/851
---

# Set segmentation master volume from Python

**Topic ID**: 851
**Date**: 2017-08-09
**URL**: https://discourse.slicer.org/t/set-segmentation-master-volume-from-python/851

---

## Post #1 by @Colin_McCurdy (2017-08-09 21:04 UTC)

<p>I have a question related to this topic (sorry if I should have posted a new topic!)</p>
<p>I am trying to auto-create segmentations from multiple master volumes using python, but when trying to do the second segmentation it has trouble setting the active segmentation with this code:</p>
<p><code>segmentEditorWidget.setSegmentationNode(segmentationNode) 	segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)</code></p>
<p>Interestingly, calling <code>setSegmentationNode(segmentationNode)</code> twice sets the node properly, but the master volume node setting is for some reason disabled, as shown:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c21e2d4b8f7515b1d5d5cc132af4c0a4865c24d8.png" data-download-href="/uploads/short-url/rHfhy2R0GOOoZzENRSlFjhbrUNy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c21e2d4b8f7515b1d5d5cc132af4c0a4865c24d8.png" alt="image" data-base62-sha1="rHfhy2R0GOOoZzENRSlFjhbrUNy" width="690" height="148" data-dominant-color="F6F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">757×163 6.54 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’m not sure if I can simply enable that menu (or how to do that) or if I’m missing some sort of ‘reset’ I need to do to access this menu.</p>
<p>Thanks,</p>
<p>Colin</p>

---

## Post #2 by @lassoan (2017-08-09 21:22 UTC)

<p>After setting segmentation node, you should be able to set the master node by simply calling setMasterVolumeNode. Are you using the latest nightly version of Slicer?</p>

---

## Post #3 by @Colin_McCurdy (2017-08-10 15:15 UTC)

<p>Nope, I’ll try it out.<br>
I agree and for the first iteration of my code that method works perfectly. I’ll update after I try in the newest nightly…</p>
<p><strong>Update</strong>: still not working. I’m wondering if I’m not setting up the widget properly as I do a few things within the loop.</p>
<p>I set this up outside of the loop:<br>
<code>segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()</code></p>
<p>then within<br>
<code>for volNum, vol in enumerate(vols):</code></p>
<p><code># ... code for setup of segmentation...</code></p>
<p><code>segmentEditorWidget.setMRMLScene(slicer.mrmlScene)</code><br>
<code>segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()</code><br>
<code>slicer.mrmlScene.AddNode(segmentEditorNode)</code><br>
<code>segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)</code><br>
<code>segmentEditorWidget.setSegmentationNode(segmentationNode)</code><br>
<code>segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)</code></p>
<p><code># ... after seed growth and at end of loop...</code><br>
<code>slicer.mrmlScene.RemoveNode(segmentEditorNode)</code></p>
<p>Then the error results when I attempt to grow from seeds during the second iteration of the loop.</p>

---

## Post #4 by @fedorov (2017-08-10 16:20 UTC)

<p><a class="mention" href="/u/che85">@che85</a> did this in another module - can you point <a class="mention" href="/u/colin_mccurdy">@Colin_McCurdy</a> to the relevant part in QuantitativeReporting Christian?</p>

---

## Post #5 by @lassoan (2017-08-10 16:51 UTC)

<p>Also, have a look at the simple <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">example script repository</a>. Does that work correctly?</p>

---

## Post #6 by @Colin_McCurdy (2017-08-10 17:20 UTC)

<p>My code is based off of the SegmentGrowCutSimple code.</p>
<p>It’s moreso using the segmentEditorWidget within a loop that seems to be the issue.</p>

---

## Post #7 by @lassoan (2017-08-10 17:35 UTC)

<p>If you don’t let events to be processed (because you don’t return from your loop) then it might be an issue. Try if adding <code>slicer.app.processEvents()</code> in your loop fixes the problems.</p>
<p>Is your module on GitHub? If you send the repository URL then I can have a look.</p>

---

## Post #8 by @Colin_McCurdy (2017-08-10 17:54 UTC)

<p>not quite a module, just a script for now.<br>
But you can view it here:<br>
<a href="https://github.com/colinmccurdy/dtiAnalysis/blob/master/dtiAnalysisNrrd.py" class="inline-onebox" rel="noopener nofollow ugc">dtiAnalysis/dtiAnalysisNrrd.py at master · colinmccurdy/dtiAnalysis · GitHub</a> , let me know if you see any glaring issues !</p>
<p>also, I tried processEvents in a few locations and it did not make a difference.</p>
<p>Another note: even when I run a single iteration I get the following errors:</p>
<blockquote>
<p>void __cdecl qMRMLSegmentEditorWidget::onSegmentSelectionChanged(const class QItemSelection &amp;,const class QItemSelection &amp;) : Invalid segment editor parameter set node<br>
void __cdecl qMRMLSegmentEditorWidget::onSegmentationNodeChanged(class vtkMRMLNode *) : Invalid segment editor parameter set node<br>
void __cdecl qMRMLSegmentEditorWidget::onSegmentSelectionChanged(const class QItemSelection &amp;,const class QItemSelection &amp;) : Invalid segment editor parameter set node<br>
void __cdecl qMRMLSegmentEditorWidget::onSegmentationNodeChanged(class vtkMRMLNode *) : Invalid segment editor parameter set node<br>
void __cdecl qMRMLSegmentEditorWidget::onMasterVolumeNodeChanged(class vtkMRMLNode *) : Invalid segment editor parameter set node<br>
void __cdecl qMRMLSegmentEditorWidget::onMasterVolumeNodeChanged(class vtkMRMLNode *) : Invalid segment editor parameter set node<br>
void __cdecl qMRMLSegmentEditorWidget::onMasterVolumeNodeChanged(class vtkMRMLNode *) : Invalid segment editor parameter set node<br>
void __cdecl qMRMLSegmentEditorWidget::updateWidgetFromMRML(void) : Invalid segment editor parameter set node<br>
vtkSlicerSegmentationsModuleLogic::GetSegmentForSegmentSubjectHierarchyItem: Segmentation does not contain segment with given ID: PhantomVolume<br>
vtkSlicerSegmentationsModuleLogic::GetSegmentForSegmentSubjectHierarchyItem: Segmentation does not contain segment with given ID: Background<br>
vtkSlicerSegmentationsModuleLogic::GetSegmentForSegmentSubjectHierarchyItem: Segmentation does not contain segment with given ID: Feature</p>
</blockquote>
<p>The code seems to still execute though with a single one.</p>

---
