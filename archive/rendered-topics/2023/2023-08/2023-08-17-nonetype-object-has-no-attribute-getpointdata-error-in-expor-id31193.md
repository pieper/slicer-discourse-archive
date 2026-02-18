# 'NoneType' object has no attribute 'GetPointData' error in exporting RTSTRUCT object into DICOM-SEG

**Topic ID**: 31193
**Date**: 2023-08-17
**URL**: https://discourse.slicer.org/t/nonetype-object-has-no-attribute-getpointdata-error-in-exporting-rtstruct-object-into-dicom-seg/31193

---

## Post #1 by @HJY (2023-08-17 07:56 UTC)

<p>Hi everyone,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a97531ad34b120ee901f82790fcd9b5998a4d089.png" data-download-href="/uploads/short-url/ob5MkM5bWpcMkoXIxbE4C5wisfD.png?dl=1" title="Screen-shot of 3D Slicer (DICOM Export-1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a97531ad34b120ee901f82790fcd9b5998a4d089_2_533x500.png" alt="Screen-shot of 3D Slicer (DICOM Export-1)" data-base62-sha1="ob5MkM5bWpcMkoXIxbE4C5wisfD" width="533" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a97531ad34b120ee901f82790fcd9b5998a4d089_2_533x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a97531ad34b120ee901f82790fcd9b5998a4d089_2_799x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a97531ad34b120ee901f82790fcd9b5998a4d089_2_1066x1000.png 2x" data-dominant-color="353737"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen-shot of 3D Slicer (DICOM Export-1)</span><span class="informations">1980×1857 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afe8d1a79655725fd006078c25cda11d736e2eec.jpeg" data-download-href="/uploads/short-url/p6amUXFsALSTSvOH2GzRXYlxmTW.jpeg?dl=1" title="Screen-shot of 3D Slicer (display)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afe8d1a79655725fd006078c25cda11d736e2eec_2_690x395.jpeg" alt="Screen-shot of 3D Slicer (display)" data-base62-sha1="p6amUXFsALSTSvOH2GzRXYlxmTW" width="690" height="395" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afe8d1a79655725fd006078c25cda11d736e2eec_2_690x395.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afe8d1a79655725fd006078c25cda11d736e2eec_2_1035x592.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afe8d1a79655725fd006078c25cda11d736e2eec_2_1380x790.jpeg 2x" data-dominant-color="454549"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen-shot of 3D Slicer (display)</span><span class="informations">1920×1100 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
![Screen-shot of 3D Slicer (DICOM Export-2)|533x499]<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afe8d1a79655725fd006078c25cda11d736e2eec.jpeg" data-download-href="/uploads/short-url/p6amUXFsALSTSvOH2GzRXYlxmTW.jpeg?dl=1" title="Screen-shot of 3D Slicer (display)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afe8d1a79655725fd006078c25cda11d736e2eec_2_690x395.jpeg" alt="Screen-shot of 3D Slicer (display)" data-base62-sha1="p6amUXFsALSTSvOH2GzRXYlxmTW" width="690" height="395" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afe8d1a79655725fd006078c25cda11d736e2eec_2_690x395.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afe8d1a79655725fd006078c25cda11d736e2eec_2_1035x592.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afe8d1a79655725fd006078c25cda11d736e2eec_2_1380x790.jpeg 2x" data-dominant-color="454549"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen-shot of 3D Slicer (display)</span><span class="informations">1920×1100 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
(upload://nUHM4oyIkkUDF76n6Fw9f15xgfA.png)</p>
<p>I am having trouble saving/exporting RTSTRUCT object into DICOM-SEG format. The RTSTRUCT loads up and displays correctly in Slicer (attached ‘display’) and also is properly associated w/ the CT series in which the segmentation was performed.</p>
<p>I have both DCMQI and QuantitativeReporting extensions installed and see the option for ‘DICOMSegmentation’ under ‘Select export type’ menu available when I click on the study or RTSTRUCT node (attached ‘DICOM Export’). However, I get a segmentation object export failure error message that says ‘NoneType’ object has no attribute ‘GetPointData’.</p>
<p>I have tried both the stable version of Slicer 5.2.2 as well as 5.3.0 to no avail. This particular RTSTRUCT can be correctly open/displayed in platform other than Slicer (i.e., MiM). Any ideas as to what could be causing this error?</p>

---

## Post #2 by @cpinter (2023-08-17 11:54 UTC)

<p>When you get the error you mentioned you get a complete call stack. It starts with ‘Traceback:’. Can you please paste the whole thing?</p>

---

## Post #3 by @HJY (2023-08-17 17:10 UTC)

<p>Here it is:</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/hjyu2/Downloads/3D Slicer/Slicer 5.3.0-2023-08-12/slicer.org/Extensions-31925/QuantitativeReporting/lib/Slicer-5.3/qt-scripted-modules/DICOMSegmentationPlugin.py”, line 367, in export<br>
exporter.export(exportable.directory, segFileName, metadata)<br>
File “C:/Users/hjyu2/Downloads/3D Slicer/Slicer 5.3.0-2023-08-12/slicer.org/Extensions-31925/QuantitativeReporting/lib/Slicer-5.3/qt-scripted-modules/DICOMSegmentationPlugin.py”, line 504, in export<br>
nonEmptySegmentIDs = self.getNonEmptySegmentIDs(segmentIDs)<br>
File “C:/Users/hjyu2/Downloads/3D Slicer/Slicer 5.3.0-2023-08-12/slicer.org/Extensions-31925/QuantitativeReporting/lib/Slicer-5.3/qt-scripted-modules/DICOMSegmentationPlugin.py”, line 582, in getNonEmptySegmentIDs<br>
return [segmentID for segmentID in segmentIDs if not self.isSegmentEmpty(segmentation.GetSegment(segmentID))]<br>
File “C:/Users/hjyu2/Downloads/3D Slicer/Slicer 5.3.0-2023-08-12/slicer.org/Extensions-31925/QuantitativeReporting/lib/Slicer-5.3/qt-scripted-modules/DICOMSegmentationPlugin.py”, line 582, in <br>
return [segmentID for segmentID in segmentIDs if not self.isSegmentEmpty(segmentation.GetSegment(segmentID))]<br>
File “C:/Users/hjyu2/Downloads/3D Slicer/Slicer 5.3.0-2023-08-12/slicer.org/Extensions-31925/QuantitativeReporting/lib/Slicer-5.3/qt-scripted-modules/DICOMSegmentationPlugin.py”, line 588, in isSegmentEmpty<br>
imagescalars = r.GetPointData().GetArray(“ImageScalars”)<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetPointData’</p>

---
