# NVIDIA AIAA error when using auto-segmentation (modle: clara_pt_liver_and_tumor_CT_segmentation)

**Topic ID**: 20197
**Date**: 2021-10-17
**URL**: https://discourse.slicer.org/t/nvidia-aiaa-error-when-using-auto-segmentation-modle-clara-pt-liver-and-tumor-ct-segmentation/20197

---

## Post #1 by @twsheng (2021-10-17 21:20 UTC)

<p>Hello everyone,</p>
<p>Could anyone help me with this error message when using the Nvidia Segmentation extension?</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/Extensions-30160/NvidiaAIAssistedAnnotation/lib/Slicer-4.13/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py", line 412, in onClickSegmentation
    if self.updateSegmentationMask(extreme_points, result_file, modelInfo):
  File "/Applications/Slicer.app/Contents/Extensions-30160/NvidiaAIAssistedAnnotation/lib/Slicer-4.13/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py", line 242, in updateSegmentationMask
    labelImage = sitk.ReadImage(in_file)
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/SimpleITK-2.1.0-py3.6-macosx-10.13-x86_64.egg/SimpleITK/extra.py", line 346, in ReadImage
    return reader.Execute()
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/SimpleITK-2.1.0-py3.6-macosx-10.13-x86_64.egg/SimpleITK/SimpleITK.py", line 8015, in Execute
    return _SimpleITK.ImageFileReader_Execute(self)
RuntimeError: Exception thrown in SimpleITK ImageFileReader_Execute: /Volumes/D/P/S-0-build/ITK/Modules/IO/NIFTI/src/itkNiftiImageIO.cxx:1980:
ITK ERROR: ITK only supports orthonormal direction cosines.  No orthonormal definition found!
</code></pre>
<p>Thank you</p>

---

## Post #2 by @lassoan (2021-10-17 21:31 UTC)

<p>As the error message tells, you need to have orthogonal image axes. You can use Crop volume module with resampling mode enabled to resample your volume on a grid with orthogonal axes.</p>

---

## Post #3 by @twsheng (2021-10-17 22:55 UTC)

<p>Thanks a lot. It’s work.</p>

---
