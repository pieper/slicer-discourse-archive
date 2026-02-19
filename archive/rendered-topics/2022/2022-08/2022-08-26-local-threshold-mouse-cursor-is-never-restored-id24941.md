---
topic_id: 24941
title: "Local Threshold Mouse Cursor Is Never Restored"
date: 2022-08-26
url: https://discourse.slicer.org/t/24941
---

# Local threshold : mouse cursor is never restored

**Topic ID**: 24941
**Date**: 2022-08-26
**URL**: https://discourse.slicer.org/t/local-threshold-mouse-cursor-is-never-restored/24941

---

## Post #1 by @chir.set (2022-08-26 19:39 UTC)

<p>‘Local threshold’ segment editor effect outputs the following in Python console :</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/home/user/programs/Slicer/bin/../lib/Slicer-5.1/qt-scripted-modules/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py", line 242, in processInteractionEvents
    self.apply(ijkPoints)
  File "/home/user/programs/Slicer/bin/../lib/Slicer-5.1/qt-scripted-modules/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py", line 481, in apply
    parameterSetNode.SetMasterVolumeIntensityMask(oldMasterVolumeIntensityMask)
AttributeError: 'vtkSlicerSegmentationsModuleMRML.vtkMRMLSegmentEdi' object has no attribute 'SetMasterVolumeIntensityMask'
</code></pre>
<p>It seems ‘SetMasterVolumeIntensityMask’ has been removed or renamed. The segmentation completes, but the mouse cursor is never restored.</p>
<p>FYI, hoping for a fix.</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2022-08-26 20:35 UTC)

<p>Thank you, good catch, that’s due that we missed adding a backward-compatibility method when we changed <code>master</code> to <code>source</code> for DEI reasons in Slicer-5.1. I’ve <a href="https://github.com/Slicer/Slicer/commit/b4fca2f83af7790c094b877f302c0578b5513298">fixed it now</a>, so the latest Slicer Preview Release (Slicer-5.1) will work well from tomorrow.</p>

---
