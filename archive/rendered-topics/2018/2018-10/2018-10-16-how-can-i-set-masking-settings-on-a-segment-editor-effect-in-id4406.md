---
topic_id: 4406
title: "How Can I Set Masking Settings On A Segment Editor Effect In"
date: 2018-10-16
url: https://discourse.slicer.org/t/4406
---

# How can I set masking settings on a segment editor effect in python?

**Topic ID**: 4406
**Date**: 2018-10-16
**URL**: https://discourse.slicer.org/t/how-can-i-set-masking-settings-on-a-segment-editor-effect-in-python/4406

---

## Post #1 by @mikebind (2018-10-16 05:37 UTC)

<p>I am trying to write an extension which automates use of some segment editor effects.  Right now, I am trying to use the “Smoothing” effect on several segments, but I want to change the masking settings programmatically for different segments. How can I control, for example, the “Editable intensity range” or which segments are allowed to be overwritten?  I’ve gotten far enough that I understand how to set the smoothing method and kernel size, but the masking settings appear to be handled differently.   Thanks!</p>

---

## Post #2 by @mikebind (2018-10-16 06:31 UTC)

<p>I think I may have figured this out.<br>
I believe the masking settings are accessed through the SegmentationNode (I’ll call mine ‘segNode’ below) for the segmentation being modified.  Specifically, to control the checkmark for “Editable intensity range”, use segNode.MasterVolumeIntensityMaskOn() to check or segNode.MasterVolumeIntensityMaskOff() to uncheck.  To set the range, use segNode.SetMasterVolumeIntensityMaskRange(minVal, maxVal).</p>
<p>To control the “Overwrite other segments” part, use segNode.SetOverwriteMode(N) where N is 0, 1, or 2.  0 means overwrite all, 1 means overwrite visible, and 2 means overwrite none.</p>
<p>The most complex one is to control the “Editable Area”.  It is segNode.SetMaskMode(N) where N is 0, 1, 2, 3, 4, or 5. 0 means paint allowed everywhere, 1 means paint allowed only inside all segments, 2 means paint allowed only inside visible segments, 3 means paint only allowed outside all segments, 4 means paint only allowed outside all visible segments, and 5 means paint only allowed inside one segment.  To specify which segment paint is allowed in one must specify segNode.SetMaskSegmentID(segID), where segID is the segment ID for the editable segment.</p>
<p>If someone reads this and I’ve gotten something wrong or there are nuances I’m missing, please let me know, I’m quite a novice at this.</p>

---

## Post #3 by @pieper (2018-10-16 12:51 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="2" data-topic="4406">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>SetOverwriteMode</p>
</blockquote>
</aside>
<p>Looks like you are on the right track.  For reference, you can use the enums defined here:</p>
<p><a href="https://github.com/Slicer/Slicer/blob/4c0b0b15276aedc0e12d77e2227536426979d773/Modules/Loadable/Segmentations/MRML/vtkMRMLSegmentEditorNode.h#L46-L85" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/4c0b0b15276aedc0e12d77e2227536426979d773/Modules/Loadable/Segmentations/MRML/vtkMRMLSegmentEditorNode.h#L46-L85</a></p>
<p>Then for clarity in the pythoncode  you can use:</p>
<pre><code class="lang-auto">slicer.vtkMRMLSegmentEditorNode.PaintAllowedInsideSingleSegment
</code></pre>

---

## Post #4 by @lassoan (2018-10-16 13:58 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="2" data-topic="4406">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I believe the masking settings are accessed through the SegmentationNode</p>
</blockquote>
</aside>
<p>Segmentation node (<a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentationNode.html">vtkMRMLSegmentationNode</a>) stores segmentation. Editing options are stored in segment editor node (<a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentEditorNode.html">vtkMRMLSegmentEditorNode</a>). For the built-in Segment Editor module, you can get segment editor node like this:</p>
<pre><code>segmentEditorNode = slicer.modules.segmenteditor.widgetRepresentation().self().editor.mrmlSegmentEditorNode()
</code></pre>
<p>See several examples of how to use segment editor effects from Python in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">script repository</a>.</p>

---

## Post #5 by @mikebind (2018-10-16 16:07 UTC)

<p>Thanks for the clarification about which node type is the right one.  I have looked at the examples in the script repository, which are very helpful, but I didn’t see any examples controlling the masking settings.</p>

---

## Post #6 by @mikebind (2018-10-16 16:09 UTC)

<p>Thank you very much for the clarification.  I found the enum definition, but am unfamiliar with C++ and interacting with it from python, so I couldn’t figure out how to access the enum values in the call to SetOverwriteMode.  I agree, this will be much clearer than just using an integer.</p>

---

## Post #7 by @lassoan (2020-02-10 00:58 UTC)

<p>The enums are available like this: <code>slicer.vtkMRMLSegmentEditorNode.PaintAllowedEverywhere</code>, <code>slicer.vtkMRMLSegmentEditorNode.OverwriteAllSegments</code>, etc.</p>

---
