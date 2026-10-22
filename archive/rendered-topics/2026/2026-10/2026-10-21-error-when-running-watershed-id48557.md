---
topic_id: 48557
title: "Error when running watershed"
date: 2026-10-21
url: https://discourse.slicer.org/t/48557
last_bumped: 2026-10-21T14:38:57.461Z
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
