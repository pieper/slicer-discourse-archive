---
topic_id: 44453
title: "Detecting Which Segments Have Been Modified"
date: 2025-09-11
url: https://discourse.slicer.org/t/44453
---

# Detecting which segments have been modified

**Topic ID**: 44453
**Date**: 2025-09-11
**URL**: https://discourse.slicer.org/t/detecting-which-segments-have-been-modified/44453

---

## Post #1 by @pieper (2025-09-11 21:28 UTC)

<p>I’m observing <code>vtkSegmentation.SourceRepresentationModified</code> and in the callback method I want to figure out which of the segments have been modified.  Does anyone know a good way to do this?</p>
<p>I tried checking the MTimes of the <code>vtkSegment</code>s but they don’t change when I edit.  If I call</p>
<pre><code class="lang-auto">representation = segmentation.GetSourceRepresentationName()
segmentation.GetSegment(segmentID).GetRepresentation(representation).GetMTime())
</code></pre>
<p>then the MTime changes, but since all the segments share the same representation I can’t tell which one changed.</p>
<p>I’d rather not have to look into the representation and compare the data.</p>

---

## Post #2 by @jcfr (2025-09-11 21:47 UTC)

<p>The event <code>vtkSegmentation::SegmentModified</code> is probably what you are looking for, the call data will be segment identifier.</p>

---

## Post #3 by @pieper (2025-09-11 23:43 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a>, I did look at that. From <a href="https://discourse.slicer.org/t/observe-modified-segment/7528/2">what is posted here</a> that is only fired when the segment metadata is modified, not the contents.  For now I’ve just disable the feature I was hoping to use.</p>

---

## Post #4 by @lassoan (2025-09-12 00:13 UTC)

<p>The easiest way to check if a segment was modified is to use the segment status. It is changed from the default <code>NotStarted</code> to <code>InProgress</code> whenever the user modifies a segment.</p>
<p>I used this to speed up saving of <del>nnUnet</del>TotalSegmentator-training-data-style (single segment per file) segmentations after manual editing. I submitted a <a href="https://github.com/JoostJM/SlicerCaseIterator/pull/22">pull request that implements the complete workflow of iterating through TotalSegmentator datasets and allows the user to fix up the segmentations using nnInteractive and save the modified segments</a>. This would have revitalized the CaseIterator a bit (and the changes to existing code were quite minimal) but the PR was not merged. This triggered the whole discussion about transferring the ownership of CaseIterator.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> It would be great if you could make use of this code in your new AI training data editor extension.</p>

---

## Post #5 by @muratmaga (2025-09-12 00:37 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="44453">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The easiest way to check if a segment was modified is to use the segment status. It is changed from the default <code>NotStarted</code> to <code>InProgress</code> whenever the user modifies a segment.</p>
</blockquote>
</aside>
<p>But this would not recognize a case when a segment is not modified since it is last saved (because it would be still <code>InProgess</code> unless the user chooses another state)?</p>

---

## Post #6 by @lassoan (2025-09-12 00:52 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="44453">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>this would not recognize a case when a segment is not modified since it is last saved (because it would be still <code>InProgess</code> unless the user chooses another state)?</p>
</blockquote>
</aside>
<p>When a segment is not modified then it does not have to be saved. It is useful for editing TotalSegmentator training data, in which each segment is stored in a separate file. Skipping saving of unchanged segments saves a lot of time when iterating through images.</p>
<p>If all the segments are stored in a single file then the segment state does not matter much, because then all the segments are saved into the file anyway.</p>

---

## Post #7 by @mau_igna_06 (2025-09-12 01:24 UTC)

<p>Maybe this is what you want Steve:</p>
<pre data-code-wrap="python"><code class="lang-python"># add a sample CT and open the segment editor 
#  and add a few segments

@vtk.calldata_type(vtk.VTK_LONG)
def myfunc(caller, eventId, callData):
  print('segment modified: ', callData)

seg = getNode('Segmentation')
seg.AddObserver(slicer.vtkSegmentation.SourceRepresentationModified, myfunc)

# modify segments and check out the printed number by myfunc
</code></pre>
<p>Tested on Slicer Preview</p>

---

## Post #8 by @pieper (2025-09-12 20:24 UTC)

<p>Thanks for all the help everyone.</p>
<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> that looks pretty good, and I get a unique value for each segment I tried but the call data seems to be a pointer like <code>4048792338560069170</code> or <code>3834588781771632178</code> and it’s not clear now to map that to segment IDs.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> thanks for the pointer to the iterator code.  It helped to see how the <code>Status</code> is used.</p>
<p>For my use case I am loading segmentations that already exist, so the <code>Status</code> may already be something other than <code>NotStarted</code> but since we aren’t using the status for anything else at this point I can set them all to <code>NotStarted</code> with <code>segmentationLogic.SetSegmentStatus(segment, segmentationLogic.NotStarted)</code> and then check the status later.</p>
<p>As a side note, before I learned about <code>GetSegmentStatus</code> I thought I would need to access the <code>vtkSegment</code> tags directly but I didn’t see a way to access them directly through python.  It would be nice to have a method signature that wraps.  Or is there another way to call it?</p>
<pre><code class="lang-auto">&gt;&gt;&gt; status = ""
&gt;&gt;&gt; seg.GetTag('Segmentation.Status', status)
Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
TypeError: GetTag argument 2:
</code></pre>

---

## Post #9 by @lassoan (2025-09-12 21:03 UTC)

<p>The API is Python-wrapped, see how it is used here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/784997471e8e4dfede24ab9618519b95be5b4e4d/SegmentEditorDrawTube/SegmentEditorDrawTubeLib/SegmentEditorEffect.py#L297">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/784997471e8e4dfede24ab9618519b95be5b4e4d/SegmentEditorDrawTube/SegmentEditorDrawTubeLib/SegmentEditorEffect.py#L297" target="_blank" rel="noopener">github.com/lassoan/SlicerSegmentEditorExtraEffects</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/784997471e8e4dfede24ab9618519b95be5b4e4d/SegmentEditorDrawTube/SegmentEditorDrawTubeLib/SegmentEditorEffect.py#L297" target="_blank" rel="noopener">SegmentEditorDrawTube/SegmentEditorDrawTubeLib/SegmentEditorEffect.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/784997471e8e4dfede24ab9618519b95be5b4e4d/SegmentEditorDrawTube/SegmentEditorDrawTubeLib/SegmentEditorEffect.py#L297" rel="noopener"><code>784997471</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="287" style="counter-reset: li-counter 286 ;">
          <li>def onEdit(self):</li>
          <li>  # Create empty model node</li>
          <li>  if self.segmentModel is None:</li>
          <li>    self.createNewModelNode()</li>
          <li></li>
          <li>  segmentID = self.scriptedEffect.parameterSetNode().GetSelectedSegmentID()</li>
          <li>  segmentationNode = self.scriptedEffect.parameterSetNode().GetSegmentationNode()</li>
          <li>  segment = segmentationNode.GetSegmentation().GetSegment(segmentID)</li>
          <li></li>
          <li>  fPosStr = vtk.mutable("")</li>
          <li class="selected">  segment.GetTag("DrawTubeEffectMarkupPositions", fPosStr)</li>
          <li>  self.logic.setPointsFromString(self.segmentMarkupNode, fPosStr)</li>
          <li></li>
          <li>  self.editButton.setEnabled(False)</li>
          <li>  self.updateModelFromSegmentMarkupNode()</li>
          <li></li>
          <li>def onMarkupNodeSelectorChanged(self, node):</li>
          <li>  self.importButton.enabled = node is not None</li>
          <li></li>
          <li>def onImportMarkupNode(self):</li>
          <li>  selectedMarkupNode = self.markupNodeSelector.currentNode()</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>But this mutable variable is quite esoteric, so I agree it would be nice to have a simpler, more Pythonic API (and a method to get all the tag names).</p>

---

## Post #10 by @chir.set (2025-09-12 21:10 UTC)

<aside class="quote no-group" data-username="pieper" data-post="8" data-topic="44453">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>a way to access them directly through python</p>
</blockquote>
</aside>
<p>Using <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/6e787f8d7b6871c1bc450abca1283c3e36985e0c/GuidedVeinSegmentation/GuidedVeinSegmentation.py#L395" rel="noopener nofollow ugc">vtk.reference()</a> seems to do the trick too. I have no idea how it differs from <code>vtk.mutable()</code>.</p>
<p>There’s a nice <code>vtkSegment::GetTags()</code> in C++, it does not seem to be wrapped for Python indeed.</p>
<p>I’m also interested in detecting a change in a segment selectively and didn’t find a way for that. I’ll dig more about <a class="mention" href="/u/lassoan">@lassoan</a> 's solution above.</p>

---

## Post #11 by @pieper (2025-09-13 02:14 UTC)

<p>For the record, here’s what I ended up doing for now:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/MorphoCloud/SlicerMorphoDepot/blob/main/MorphoDepot/MorphoDepot.py#L451-L520">
  <header class="source">

      <a href="https://github.com/MorphoCloud/SlicerMorphoDepot/blob/main/MorphoDepot/MorphoDepot.py#L451-L520" target="_blank" rel="noopener">github.com/MorphoCloud/SlicerMorphoDepot</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/MorphoCloud/SlicerMorphoDepot/blob/main/MorphoDepot/MorphoDepot.py#L451-L520" target="_blank" rel="noopener">MorphoDepot/MorphoDepot.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/MorphoCloud/SlicerMorphoDepot/blob/main/MorphoDepot/MorphoDepot.py#L451-L520" rel="noopener"><code>main</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="451" style="counter-reset: li-counter 450 ;">
          <li>def onIssueDoubleClicked(self, item):</li>
          <li>    slicer.util.showStatusMessage(f"Loading {item.text()}")</li>
          <li>    repoDirectory = os.path.normpath(self.configureUI.repoDirectory.currentPath)</li>
          <li>    issue = self.issuesByItem[item]</li>
          <li>    if slicer.util.confirmOkCancelDisplay("Close scene and load issue?"):</li>
          <li>        self.removeObservers()</li>
          <li>        self.segmentNamesByID = {}</li>
          <li>        self.annotateUI.currentIssueLabel.text = f"Issue: {item.text()}"</li>
          <li>        slicer.mrmlScene.Clear()</li>
          <li>        try:</li>
          <li>            self.logic.loadIssue(issue, repoDirectory)</li>
          <li>            self.annotateUI.forkManagementCollapsibleButton.enabled = True</li>
          <li>            segmentation = self.logic.segmentationNode.GetSegmentation()</li>
          <li>            segmentationLogic = slicer.modules.segmentations.logic()</li>
          <li>            for segmentID in segmentation.GetSegmentIDs():</li>
          <li>                segment = segmentation.GetSegment(segmentID)</li>
          <li>                segmentationLogic.SetSegmentStatus(segment, segmentationLogic.NotStarted)</li>
          <li>                self.segmentNamesByID[segmentID] = segment.GetName()</li>
          <li>            segmentEvents = [segmentation.SourceRepresentationModified,</li>
          <li>                             segmentation.SegmentModified,</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/MorphoCloud/SlicerMorphoDepot/blob/main/MorphoDepot/MorphoDepot.py#L451-L520" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Thanks again everyone!</p>

---
