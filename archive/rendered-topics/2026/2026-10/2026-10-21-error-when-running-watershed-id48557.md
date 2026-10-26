---
topic_id: 48557
title: "Error when running watershed"
date: 2026-10-21
url: https://discourse.slicer.org/t/48557
last_bumped: 2026-10-26T00:39:11.100Z
---

# Error when running watershed

**Topic ID**: 48557
**Date**: 2026-10-21
**URL**: https://discourse.slicer.org/t/error-when-running-watershed/48557

---

## Post #1 by @jsguerra (2026-10-21 14:38 UTC)

<p>I’m trying to use watershed segmentation (5.12.4 on Win10) and I get a segmentation fail message. This is what I get on detials:</p>
<blockquote>
<p>Traceback (most recent call last):</p>
<p>File “C:\Users/JSG/AppData/Local/slicer.org/3D Slicer 5.12.4/bin/Python\slicer\util.py”, line 3614, in tryWithErrorDisplay</p>
<pre><code>yield
</code></pre>
<p>File “C:\Users\JSG\AppData\Local\slicer.org\3D Slicer 5.12.4\lib\Slicer-5.12\qt-scripted-modules\SegmentEditorEffects\AbstractScriptedSegmentEditorAutoCompleteEffect.py”, line 303, in onPreview</p>
<pre><code>self.preview()
</code></pre>
<p>File “C:\Users\JSG\AppData\Local\slicer.org\3D Slicer 5.12.4\lib\Slicer-5.12\qt-scripted-modules\SegmentEditorEffects\AbstractScriptedSegmentEditorAutoCompleteEffect.py”, line 567, in preview</p>
<pre><code>self.computePreviewLabelmap(mergedImage, outputLabelmap)
</code></pre>
<p>File “C:/Users/JSG/AppData/Local/slicer.org/3D Slicer 5.12.4/slicer.org/Extensions-34645/SegmentEditorExtraEffects/lib/Slicer-5.12/qt-scripted-modules/SegmentEditorWatershedLib/SegmentEditorEffect.py”, line 111, in computePreviewLabelmap</p>
<pre><code>labelImage = sitk.ReadImage(sitkUtils.GetSlicerITKReadWriteAddress(mergedLabelmapNode.GetName()))

             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “C:\Users\JSG\AppData\Local\slicer.org\3D Slicer 5.12.4\lib\Python\Lib\site-packages\SimpleITK\extra.py”, line 384, in ReadImage</p>
<pre><code>return reader.Execute()

       ^^^^^^^^^^^^^^^^
</code></pre>
<p>File “C:\Users\JSG\AppData\Local\slicer.org\3D Slicer 5.12.4\lib\Python\Lib\site-packages\SimpleITK\SimpleITK.py”, line 8534, in Execute</p>
<pre><code>return \_SimpleITK.ImageFileReader_Execute(self)

       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>RuntimeError: Exception thrown in SimpleITK ImageFileReader_Execute: D:\a\SimpleITK\SimpleITK\Code\IO\src\sitkImageReaderBase.cxx:91:</p>
<p>sitk::ERROR: The file “slicer:0000023F71755F30#vtkMRMLLabelMapVolumeNode1” does not exist.</p>
</blockquote>
<p>I created two segments and placed seeds in them. I am doing something wrong?</p>

---

## Post #2 by @Rei_Kurosawa (2026-10-23 07:06 UTC)

<p>You are not doing anything wrong, this is a known bug in the extension, not a workflow issue. The exact same traceback (SimpleITK ReadImage failing on the slicer: pseudo file path) is filed in the SegmentEditorExtraEffects issue tracker as issue 71, reported against 5.12 and still open. Painting seeds in two segments is exactly how the effect is meant to be used. Until it gets fixed, the built-in Grow from seeds effect in Segment Editor covers the same seed-based workflow without using the extension’s code. You can subscribe to the issue on GitHub to get notified when a fix lands.</p>

---

## Post #3 by @jsguerra (2026-10-26 00:39 UTC)

<p>Thank you for letting me know about the bug and for the suggestion!</p>

---
