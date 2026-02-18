# Module 'slicer.util' has no attribute 'updateSegmentBinaryLabelmapFromArray'

**Topic ID**: 21949
**Date**: 2022-02-13
**URL**: https://discourse.slicer.org/t/module-slicer-util-has-no-attribute-updatesegmentbinarylabelmapfromarray/21949

---

## Post #1 by @Saebiryx (2022-02-13 13:23 UTC)

<p><strong>Operating system:</strong> Windows 10<br>
<strong>Slicer version:</strong> 4.11.20210226<br>
<strong>Behavior:</strong><br>
Using the python interactor, i’m unable to change a labelmap.</p>
<blockquote>
<blockquote>
<blockquote>
<p>slicer.util.updateSegmentBinaryLabelmapFromArray(segmentArray, segmentationNode, segmentId)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
AttributeError: module ‘slicer.util’ has no attribute ‘updateSegmentBinaryLabelmapFromArray’</p>
</blockquote>
</blockquote>
</blockquote>
<p>or</p>
<blockquote>
<blockquote>
<blockquote>
<p>updateSegmentBinaryLabelmapFromArray(segmentArray, segmentationNode, segmentId)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
NameError: name ‘updateSegmentBinaryLabelmapFromArray’ is not defined</p>
</blockquote>
</blockquote>
</blockquote>
<p>Although ‘updateSegmentBinaryLabelmapFromArray’ is mentioned in the docs, it doesn’t seem to work. Am I missing something? import slicer and import vtk didn’t solve the issue.</p>
<p>Example (marking all pixels in a specific slice):</p>
<blockquote>
<blockquote>
<blockquote>
<p>volumeNode = getNode(‘AB’)<br>
segmentationNode = getNode(‘test’)<br>
segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(‘Segment_1’)<br>
segment = segmentationNode.GetSegmentation().GetSegment(segmentId)<br>
segmentArray = slicer.util.arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId)<br>
segmentArray[61,:,:] = 1<br>
slicer.util.updateSegmentBinaryLabelmapFromArray(segmentArray, segmentationNode, segmentId)</p>
</blockquote>
</blockquote>
</blockquote>

---

## Post #2 by @lassoan (2022-02-13 13:31 UTC)

<p>Currently on readthedocs the only documentation version is <a href="https://slicer.readthedocs.io/en/latest/">https://slicer.readthedocs.io/en/latest/</a></p>
<p>“latest” refers to the very latest Slicer Preview Release that is updated every day. Older versions are documented on the old Slicer wiki, for example <a href="https://www.slicer.org/wiki/Documentation/4.10/ScriptRepository">https://www.slicer.org/wiki/Documentation/4.10/ScriptRepository</a></p>
<p>Since we plan to release the current Slicer Preview Release as the new stable version very soon, I would recommend you to switch to the latest Slicer Preview Release now.</p>

---
