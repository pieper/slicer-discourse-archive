---
topic_id: 11976
title: "Bad Alloc Error While Using Margin Effect In Segment Editor"
date: 2020-06-10
url: https://discourse.slicer.org/t/11976
---

# Bad_alloc error while using margin effect in Segment editor module

**Topic ID**: 11976
**Date**: 2020-06-10
**URL**: https://discourse.slicer.org/t/bad-alloc-error-while-using-margin-effect-in-segment-editor-module/11976

---

## Post #1 by @Deepa (2020-06-10 07:47 UTC)

<p>Hello Everyone,</p>
<p>I’ve a 3D  volume like <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/d/d2474d5bf4d66d4459c50e8a31589bf2670791fb.jpeg" rel="noopener nofollow ugc">this</a>.<br>
For the suggestions offered <a href="https://discourse.slicer.org/t/using-crop-volume-module-to-extract-subvolume-from-a-3d-volume/11926/2">here</a>, I’m trying to use <code>Scissors</code> option in <code>Segment Editor </code> to extract a subvolume.</p>
<p>I used the circular option in “Scissors” tab to cut the segment. After obtaining the circular volume, I used the “islands” effect to retain the largest island. Using “Islands” effect on the whole volume worked fine, but I am not sure why memory issues (“bad_alloc”) occurs for this small volume.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d62925fb161b3605b1d307cfd79337ed69e403d7.png" alt="image" data-base62-sha1="uyykZIuuCsw2euCiTNg90OrcHDF" width="172" height="97"></p>
<p>Unable to allocate 705421132 elements of size 4 bytes.</p>
<p>Second try:</p>
<blockquote>
<pre><code>QXcbConnection: XCB error: 8 (BadMatch), sequence: 24430, resource id: 2622306, major code: 42 (SetInputFocus), minor code: 0
10 islands created (566 ignored)
Unable to allocate 705421132 elements of size 1 bytes.
</code></pre>
</blockquote>
<pre><code>Traceback (most recent call last):
  File "/folder/Slicer-4.11.0-2020-05-19-linux-amd64/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorEffects/SegmentEditorIslandsEffect.py", line 115, in onApply
    self.splitSegments(minimumSize = minimumSize, maxNumberOfSegments = 1)
  File "/folder/Slicer-4.11.0-2020-05-19-linux-amd64/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorEffects/SegmentEditorIslandsEffect.py", line 223, in splitSe
    self.scriptedEffect.modifySegmentByLabelmap(segmentationNode, segmentID, modifierImage, modificationMode)
MemoryError: std::bad_alloc: std::bad_alloc
</code></pre>
<p>I’d like to ask for inputs on what can be done to overcome this error</p>

---

## Post #2 by @lassoan (2020-06-10 13:17 UTC)

<p>Scissors effect just blanks out voxels, does not crop the volume. If you cannot add a few 10GB physical RAM and you find that configuring more virtual memory (swap space) results in too slow computation then you can reduce your image size before you start segmentation by cropping and/or resampling your input volume using “Crop volume” module.</p>

---
