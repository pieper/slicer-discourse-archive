# Disapearing segment information after using importlabelmaptosegmentation

**Topic ID**: 9291
**Date**: 2019-11-25
**URL**: https://discourse.slicer.org/t/disapearing-segment-information-after-using-importlabelmaptosegmentation/9291

---

## Post #1 by @dominicrushforth (2019-11-25 13:08 UTC)

<p>Hi,</p>
<p>I am really loving 4.11 as I can now use scipy and pdflatex with ease. However ever since I started using 4.11 I have been having problems with my GUI for performing localised thresholing using simpleitk…</p>
<p>The first segment loses all it’s segment information as soon as another is created. The segment still exists in the list of segments and the segmentation node (when printed in the interactor) but it cannot be visualised - as if it were a newly created ‘blank’ segment.</p>
<p>I have tracked the issue down to this command:</p>
<p>slicer.vtkSlicerSegmentationsModuleLogic.ImportLabelmapToSegmentationNode(labelmap, segmentationNode, segmentVtkString)</p>
<p>Whenever this is run for a different segment, the first segment in the segmentation node is ‘cleared’ as described above. When creating multiple segments none of the subsequent segments are affected in the same way and it is possible to work around this problem by redefining the first segment after having completed all the others.</p>
<p>I am currently using the nightly from the 21st.</p>

---

## Post #2 by @lassoan (2019-11-25 13:53 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@sunderlandkyl</a> could you please check if you can reproduce this issue?</p>

---

## Post #3 by @Sunderlandkyl (2019-11-25 13:56 UTC)

<p>Sure, I’ll take a look.</p>

---

## Post #4 by @Sunderlandkyl (2019-11-25 14:58 UTC)

<p><a class="mention" href="/u/dominicrushforth">@dominicrushforth</a> I’ve tried importing lablemaps one after the other into the same segmentation, but I haven’t been able to reproduce this issue so far.</p>
<p>Could you provide mode information on when this occurs?<br>
How many segments are in the labelmaps that you import?</p>

---

## Post #5 by @dominicrushforth (2019-11-25 16:30 UTC)

<p>I’m not entirely sure what is relevant,</p>
<p>I get a vtkMRMLSegmentEditorNode…</p>
<pre><code class="lang-python">try:
  self.segmentEditorNode = slicer.util.getNode('Dose Segment Editor')
except:
  self.segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
self.segmentEditorNode.SetName('Dose Segment Editor')
# create a vtkMRMLSegmentationNode…
try:
  self.segmentationNode = slicer.util.getNode('Dose Segmentation')
except:
  self.segmentationNode = slicer.vtkMRMLSegmentationNode()
self.segmentationNode.SetName('Dose Segmentation')
</code></pre>
<p>I run the simple itk ConnectedThresholdImageFilter then use this function to put the resulting labelmap into a segment</p>
<pre><code class="lang-python"># names of relevant nodes are looked up
currentSegmentText = self.segmentationSelector.currentText
# looks for segment
segmentID = self.segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(currentSegmentText)
segment = self.segmentationNode.GetSegmentation().GetSegment(segmentID)
# if the mask segment has not already been created, this is done (it should have been but just in case!)
if segment is None:
  segmentID = self.segmentationNode.GetSegmentation().AddEmptySegment(currentSegmentText)
# convert resulting label map into a segment
segmentVtkString = vtk.vtkStringArray()
segmentVtkString.SetNumberOfValues(1)
segmentVtkString.SetValue(0,currentSegmentText)
slicer.vtkSlicerSegmentationsModuleLogic.ImportLabelmapToSegmentationNode(labelmap, self.segmentationNode, segmentVtkString)
</code></pre>
<p>The problem occurs when creating the second segment. The original segment can still be seen if the function is ended before the last<br>
line is run. Running the last line in the interactor then makes the first segment vanish (even if all the eyes are open). Creating a third segment has no effect on the second segment and so on… However if the first segment is removed the segment that is<br>
now at the top of the list is affected in the same way if any new segments are created using this method.  The problem doesn’t occur with other of creating or defining segments.</p>
<p>I am using<br>
r28644 on windows. I can install the latest nightly if that might help?</p>
<p>Dom</p>

---

## Post #6 by @Sunderlandkyl (2019-11-25 20:42 UTC)

<p>Thanks for your help, I think I’ve found the cause of the issue.<br>
I’ll let you know when it’s fixed.</p>

---

## Post #7 by @Sunderlandkyl (2019-11-25 22:06 UTC)

<p>Found the problem and made a fix (can be found here: <a href="https://github.com/Slicer/Slicer/pull/1268" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/1268</a>).</p>

---

## Post #8 by @Sunderlandkyl (2019-11-26 14:24 UTC)

<p>The fix should be found in the latest 4.11 nightly.</p>

---

## Post #9 by @dominicrushforth (2019-11-26 15:16 UTC)

<p>I’ve installed the latest nightly and it’s working great. Thanks so much <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
