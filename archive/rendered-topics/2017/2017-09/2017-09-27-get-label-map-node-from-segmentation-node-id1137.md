# Get label map node from segmentation node

**Topic ID**: 1137
**Date**: 2017-09-27
**URL**: https://discourse.slicer.org/t/get-label-map-node-from-segmentation-node/1137

---

## Post #1 by @snvl (2017-09-27 19:49 UTC)

<p>Hello!</p>
<p>Is there a way to create a label map node from a segmentation node? I know I can go the other way (from a label map to a segmentation), but I can’t seem to find a way to do the opposite. If this is not possible is there a way to at least get the array underlying the segmentation node? I know I can get an oriented image data, but if I do slicer.util.array on the oriented image data, nothing is returned.</p>
<p>Thanks!</p>

---

## Post #2 by @cpinter (2017-09-27 20:15 UTC)

<p>Answered in</p><aside class="quote" data-post="1" data-topic="603">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/export-volume-data-in-segment/603">Export volume data in segment?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Is it possible to export the volume data in a segment? Meaning, using the Segment Editor, you create a segment, then export a TIFF stack or NRRD with the same volume size as your original data set, but with just the data in your segment, all other voxels at 0? 
Thanks! 
-Hollister
  </blockquote>
</aside>

<p>You can also reach this function (i.e. Segmentations module import/export) from the Data module (right-click the segmentation), and in Segment Editor as an option for the Segmentations button.</p>

---

## Post #3 by @snvl (2017-09-27 20:20 UTC)

<p>Awesome! Do you know how I might do this through the python code?</p>
<p>Found it:<br>
<code><br>
slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode()<br>
</code></p>

---

## Post #4 by @snvl (2017-09-27 20:31 UTC)

<p>Do you know what the inputs for this function is or where the documentation is for the segments?</p>
<p>slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode()</p>

---

## Post #5 by @cpinter (2017-09-27 20:35 UTC)

<p>These are the available signatures<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L166-L192" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L166-L192" target="_blank">Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L166-L192</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="166" style="counter-reset: li-counter 165 ;">
<li>static bool ExportAllSegmentsToModels(vtkMRMLSegmentationNode* segmentationNode, vtkIdType folderItemId);</li>
<li>
</li><li>/// Export multiple segments into a multi-label labelmap volume node</li>
<li>/// \param segmentationNode Segmentation node from which the the segments are exported</li>
<li>/// \param segmentIds List of segment IDs to export</li>
<li>/// \param labelmapNode Labelmap node to export the segments to</li>
<li>/// \param referenceVolumeNode If specified, then the merged labelmap node will match the geometry of referenceVolumeNode</li>
<li>static bool ExportSegmentsToLabelmapNode(vtkMRMLSegmentationNode* segmentationNode, std::vector&lt;std::string&gt;&amp; segmentIDs,</li>
<li>  vtkMRMLLabelMapVolumeNode* labelmapNode, vtkMRMLVolumeNode* referenceVolumeNode = nullptr);</li>
<li>
</li><li>/// Export multiple segments into a multi-label labelmap volume node</li>
<li>/// \param segmentationNode Segmentation node from which the the segments are exported</li>
<li>/// \param segmentIds List of segment IDs to export</li>
<li>/// \param labelmapNode Labelmap node to export the segments to</li>
<li>/// \param referenceVolumeNode If specified, then the merged labelmap node will match the geometry of referenceVolumeNode</li>
<li>static bool ExportSegmentsToLabelmapNode(vtkMRMLSegmentationNode* segmentationNode, vtkStringArray* segmentIDs,</li>
<li>  vtkMRMLLabelMapVolumeNode* labelmapNode, vtkMRMLVolumeNode* referenceVolumeNode = nullptr);</li>
<li>
</li><li>/// Export visible segments into a multi-label labelmap volume node</li>
<li>/// \param segmentationNode Segmentation node from which the the visible segments are exported</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L166-L192" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>A few examples of usage<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/Slicer/Slicer/search?utf8=%E2%9C%93&amp;q=ExportSegmentsToLabelmapNode&amp;type=" target="_blank">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars3.githubusercontent.com/u/324362?s=400&amp;v=4" class="thumbnail onebox-avatar" width="400" height="400">

<h3><a href="https://github.com/Slicer/Slicer/search?utf8=%E2%9C%93&amp;q=ExportSegmentsToLabelmapNode&amp;type=" target="_blank">Slicer/Slicer</a></h3>

<p>Multi-platform, free open source software for visualization and image computing. - Slicer/Slicer</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #6 by @snvl (2017-09-27 20:38 UTC)

<p>Are there examples in python?</p>

---

## Post #7 by @lassoan (2017-09-27 20:39 UTC)

<p>You can always use help() function in Python to get documentation, for example:<br>
help(slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode)</p>
<p>Example where it is used: <a href="https://github.com/Slicer/Slicer/blob/master/Utilities/Templates/Modules/ScriptedSegmentEditorEffect/SegmentEditorTemplateKeyLib/SegmentEditorEffect.py#L97">https://github.com/Slicer/Slicer/blob/master/Utilities/Templates/Modules/ScriptedSegmentEditorEffect/SegmentEditorTemplateKeyLib/SegmentEditorEffect.py#L97</a></p>
<p>To create a custom Segment Editor effect, use ExtensionWizard module and choose ScriptedSegmentEditorEffect module template. It creates a fully functional effect that uses SimpleITK and you just have to replace the core of it to do what you need.</p>

---

## Post #8 by @cpinter (2017-09-28 07:01 UTC)

<p><a class="mention" href="/u/snvl">@snvl</a> The first two results in the search that was the second link in my post above are python examples.</p>

---

## Post #10 by @aiden.zhu (2019-08-29 19:37 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> Would you please help explain this to me?<br>
inside here:<br>
slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsToLabelmapNode(segmentationNode, segs, tmpLabelmapNode, masterVolumeNode)<br>
where segs has to be an vtk.vtkStringArray() and the segs may be obtained by:</p>
<p>segmentationNode = self.scriptedEffect.parameterSetNode().GetSegmentationNode()<br>
segs = vtk.vtkStringArray()<br>
segmentationNode.GetDisplayNode().GetVisibleSegmentIDs(segs)</p>
<p>But while I try to get the selected segment-ID through:</p>
<p>segmentationNode = self.scriptedEffect.parameterSetNode().GetSegmentationNode()<br>
selectedSegmentID = self.scriptedEffect.parameterSetNode().GetSelectedSegmentID()<br>
where I just got a simple string for selectedSegmentID</p>
<p>How can I get a vtk.vtkStringArray for this selectedSegmentID or any easy conversion?</p>
<p>Thanks a lot.</p>

---

## Post #11 by @cpinter (2019-08-29 19:51 UTC)

<pre><code>sa = vtk.vtkStringArray()
sa.InsertNextValue(selectedSegmentID)
</code></pre>
<p>FYI the documentation tells you everything<br>
<a href="https://vtk.org/doc/nightly/html/classvtkStringArray.html" class="onebox" target="_blank" rel="nofollow noopener">https://vtk.org/doc/nightly/html/classvtkStringArray.html</a></p>

---

## Post #12 by @aiden.zhu (2019-08-29 20:13 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a>  Thank you so much for the quick reply. Sorry I am kind of new to vtk.<br>
<img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"><br>
Best,<br>
Aiden</p>

---

## Post #13 by @fedorov (2019-11-22 14:48 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a> is it possible to get the reference volume?</p>
<p>I searched, but could not find the answer. I was confused by the comment for the method below, it just returns a constant string.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLSegmentationNode.h#L181-L182" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLSegmentationNode.h#L181-L182" target="_blank">Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLSegmentationNode.h#L181-L182</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="181" style="counter-reset: li-counter 180 ;">
<li>/// Expose reference identifier to get the volume node defining the reference image geometry if any</li>
<li>static std::string GetReferenceImageGeometryReferenceRole() { return "referenceImageGeometryRef"; };</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #14 by @lassoan (2019-11-22 15:05 UTC)

<p>The constant string is the name of the node reference role. You can get the reference volume node like this: <code>segmentationNode.GetNodeReference(slicer.vtkMRMLSegmentationNode.GetReferenceImageGeometryReferenceRole()) </code></p>

---

## Post #15 by @fedorov (2019-11-23 01:08 UTC)

<p>Thank you Andras, this resolved the latest issue I had!</p>

---

## Post #16 by @fedorov (2019-11-26 23:43 UTC)

<p>Related to this issue, I wanted to mention that I used this approach without reading documentation (my usual mode of operation <img src="https://emoji.discourse-cdn.com/twitter/roll_eyes.png?v=9" title=":roll_eyes:" class="emoji" alt=":roll_eyes:">) as follows:</p>
<pre><code class="lang-python">segmentLabelmapNode = slicer.vtkMRMLLabelMapVolumeNode()
slicer.mrmlScene.AddNode(segmentLabelmapNode)
segmentIDs = vtk.vtkStringArray()
segmentIDs.InsertNextValue(0)
referenceNode = segmentationNode.GetNodeReference(slicer.vtkMRMLSegmentationNode.GetReferenceImageGeometryReferenceRole())
slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(segmentationNode, segmentIDs, segmentLabelmapNode, referenceNode)
</code></pre>
<p>Somehow this code works in the nightly, but when I do this in 4.10.2 I get error (<code>InsertNextValue</code> expects a string). If I do pass 0 as a string, I get a crash. The correct way to initialize that array, as I understand it, is the following:</p>
<pre><code class="lang-python">segmentationNode.GetSegmentation().GetSegmentIDs(segmentIDs)
</code></pre>
<p>Just in case this can help someone else.</p>

---
