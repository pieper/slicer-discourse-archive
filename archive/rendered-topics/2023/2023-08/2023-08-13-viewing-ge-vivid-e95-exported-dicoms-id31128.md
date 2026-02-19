---
topic_id: 31128
title: "Viewing Ge Vivid E95 Exported Dicoms"
date: 2023-08-13
url: https://discourse.slicer.org/t/31128
---

# Viewing GE vivid e95 exported dicoms

**Topic ID**: 31128
**Date**: 2023-08-13
**URL**: https://discourse.slicer.org/t/viewing-ge-vivid-e95-exported-dicoms/31128

---

## Post #1 by @thundertfive (2023-08-13 17:53 UTC)

<p>Hi there, I installed SlicerHeart extension and tried to import dicom files exported from the  GE vivid e95 machine.  It can’t import last volumes and gives the following error:</p>
<pre><code class="lang-auto">[Python] Traceback (most recent call last):
[Python]   File "C:\Users\PC\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Slicer-5.2\qt-scripted-modules\DICOMLib\DICOMUtils.py", line 790, in loadLoadables
[Python]     loadSuccess = plugin.load(loadable)
[Python]   File "C:/Users/PC/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/SlicerHeart/lib/Slicer-5.2/qt-scripted-modules/DicomUltrasoundPlugin.py", line 558, in load
[Python]     loadedNode = self.loadGeUsMovie(loadable)
[Python]   File "C:/Users/PC/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/SlicerHeart/lib/Slicer-5.2/qt-scripted-modules/DicomUltrasoundPlugin.py", line 791, in loadGeUsMovie
[Python]     if imageProxyVolumeNode:
[Python] UnboundLocalError: local variable 'imageProxyVolumeNode' referenced before assignment
</code></pre>
<p>Also, loaded volumes are seem wrong. Some of them looks like frames from the same video and the volume with multiple frames seems distorted too. My dicom files have “gems_ultrasound_moviegroup_001” private tags. I know there are topics about it but none of them solved my issue. I appreciate your help.</p>
<p>Finally, I want to mention that I split my DICOMDIR to the individual dicom files to open from the Slicer. Does Slicer supports DICOMDIR format or can it be the issue? Thank you in advance <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @lassoan (2023-08-13 18:02 UTC)

<p>The safest is to delete any DICOMDIR file to make sure it is not taken into account when indexing the DICOM files. DICOMDIR file just provides a summary of files in the folder. We tried to used them in the past but they caused a lot of problems, because often files that the DICOMDIR file referred to were no longer there, or some files in the folder were not mentioned in the DICOMDIR file.</p>
<p>I’ll check what could have caused the <code>UnboundLocalError</code> exception that you saw.</p>

---

## Post #3 by @thundertfive (2023-08-13 18:31 UTC)

<p>Thank you a lot.  I want to ask one more thing, do files in the DICOMDIR contain the whole metadata? They have no extension and when I directly import them it doesn’t differentiate 2 different patients or studies. I only see volumes with single frames instead of videos. I know I asked too much but I would really appreciate any help. I saw so many people have problems with the gems_ultrasound_moviegroup_001 tag and it seems there is no direct solution <img src="https://emoji.discourse-cdn.com/twitter/slightly_frowning_face.png?v=12" title=":slightly_frowning_face:" class="emoji" alt=":slightly_frowning_face:" loading="lazy" width="20" height="20"></p>
<p>By the way, I get different errors like this, I hope they may help:</p>
<pre><code class="lang-auto"> vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open ...  ITK exception info: error in unknown:  Could not create IO object for reading file .. [VTK]   Tried to create one of the following:
[VTK]     BMPImageIO
[VTK]     BioRadImageIO
[VTK]     DCMTKImageIO
[VTK]     GDCMImageIO
[VTK]     GiplImageIO
[VTK]     JPEGImageIO
[VTK]     LSMImageIO
[VTK]     MGHImageIO
[VTK]     MINCImageIO
[VTK]     MRCImageIO
[VTK]     MetaImageIO
[VTK]     NiftiImageIO
[VTK]     NrrdImageIO
[VTK]     PNGImageIO
[VTK]     ScancoImageIO
[VTK]     StimulateImageIO
[VTK]     TIFFImageIO
[VTK]     VTKImageIO
[VTK]     MRMLIDImageIO
[VTK]     Bruker2dseqImageIO
[VTK]     GE4ImageIO
[VTK]     GE5ImageIO
[VTK]     HDF5ImageIO
[VTK]     JPEG2000ImageIO
[VTK]   You probably failed to set a file suffix, or
[VTK]     set the suffix to an unsupported type.
[VTK] Algorithm vtkITKArchetypeDiffusionTensorImageReaderFile(0000024A6FD70C30) returned failure for request: vtkInformation (0000024A704F1B70)

</code></pre>
<p>Edit: I want to clarify that problems with the gems_ultrasound_moviegroup_001  tag are not special to the Slicer app. I searched the whole internet, used dozens of viewers/code, and couldn’t read the content properly yet.</p>

---

## Post #4 by @thundertfive (2023-08-20 14:03 UTC)

<p>Hi, I wrote very similar code as the Slicer’s Heart extension in Python. I realized that one of my Dicom files have a missing header and got the same error. Therefore I deleted that file and the error is solved. Moreover, I realized that stored videos are in a cartesian system, and converting them to the polar coordinates solved my issue and managed to view them as in the machine. I need to validate that their views are correct but I hope I won’t need to spend more time in those nested tags <img src="https://emoji.discourse-cdn.com/twitter/slightly_frowning_face.png?v=12" title=":slightly_frowning_face:" class="emoji" alt=":slightly_frowning_face:" loading="lazy" width="20" height="20"> . Thank you for your previous answer again. I think this issue is solved.</p>

---
