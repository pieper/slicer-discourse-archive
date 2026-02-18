# RTSTRUCT segmentation discrepancy

**Topic ID**: 10662
**Date**: 2020-03-12
**URL**: https://discourse.slicer.org/t/rtstruct-segmentation-discrepancy/10662

---

## Post #1 by @athanell (2020-03-12 16:35 UTC)

<p>Operating system: Windows 7<br>
Slicer version:4.11.0-2020-02-19<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello,<br>
After exporting a segmentation to an RTStruct I noticed that there are discrepancies with respect to the original segmentation in many slices of the volume. See for example the differences of 1 slice in the following screenshots.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/395aac7b16d79e5b94a914daedfbe3d2a966c055.jpeg" data-download-href="/uploads/short-url/8bntYkiG48rLnDXZjVMkUjVwX0V.jpeg?dl=1" title="OrigSeg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/395aac7b16d79e5b94a914daedfbe3d2a966c055_2_690x417.jpeg" alt="OrigSeg" data-base62-sha1="8bntYkiG48rLnDXZjVMkUjVwX0V" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/395aac7b16d79e5b94a914daedfbe3d2a966c055_2_690x417.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/395aac7b16d79e5b94a914daedfbe3d2a966c055_2_1035x625.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/395aac7b16d79e5b94a914daedfbe3d2a966c055_2_1380x834.jpeg 2x" data-dominant-color="242524"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">OrigSeg</span><span class="informations">1942×1175 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d8a0cc577d75915adf8f59f47ef9e4258d0eed4.jpeg" data-download-href="/uploads/short-url/dluaRKsAslruVYfAgIdGORGN7w0.jpeg?dl=1" title="RTSTructSeg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d8a0cc577d75915adf8f59f47ef9e4258d0eed4_2_690x399.jpeg" alt="RTSTructSeg" data-base62-sha1="dluaRKsAslruVYfAgIdGORGN7w0" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d8a0cc577d75915adf8f59f47ef9e4258d0eed4_2_690x399.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d8a0cc577d75915adf8f59f47ef9e4258d0eed4_2_1035x598.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d8a0cc577d75915adf8f59f47ef9e4258d0eed4_2_1380x798.jpeg 2x" data-dominant-color="232323"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">RTSTructSeg</span><span class="informations">2097×1215 225 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The image used is the head CT from Slicer’s sample data.<br>
Is this a normal behaviour?</p>
<p>Thank you<br>
Antonios</p>

---

## Post #2 by @gcsharp (2020-03-12 16:52 UTC)

<p>MIght be a keyholizing issue.  Is the screenshot from 3D Slicer?  Can you clarify what workflow steps you used?</p>

---

## Post #3 by @cpinter (2020-03-12 17:24 UTC)

<p>RTSTRUCT is saved in form of closed contours on each axial slice. If you have such a fragmented segmentation, you will probably encounter similar issues. I suggest cleaning your segmentation before saving to structure set.</p>
<p>A lot of the issues I’m referring to are related to polydata visualization. So it is possible that the underlying data itself is perfectly fine. Go to the Segmentations module, and in the advanced display section switch 2D visualization to binary labelmap. You will probably see healthier slice intersections.</p>

---

## Post #4 by @lassoan (2020-03-12 17:46 UTC)

<p>I would recommend to stay away from RT structure sets. This format was developed more than 20 years ago, specifically for radiation therapy. It is not suitable as a general-purpose segmentation storage format. The main issue is that in RT structure sets, segmentation is stored as a set of parallel planar contours, and so complex geometries (such as the one you show in your screenshots) practically cannot be represented without risk of data loss or corruption.</p>
<p>If you must use RT structure set (e.g., you export data to be imported by a TPS) then keep in mind these limitations. For all other purposes, follow what modern medical imaging software do: store segmentation in DICOM segmentation object. Slicer can read/write these DICOM files if you install QuantitativeReporting extension.</p>

---

## Post #5 by @athanell (2020-03-12 22:21 UTC)

<p>When I toggle in Segmentations&gt;Display&gt;Advanced&gt;Representation in 2D views from binary label map to closed surface the segmentation in some slices becomes better (even though not exactly the same as the original segmentation), while in some others kind of worse.</p>

---

## Post #6 by @athanell (2020-03-12 22:42 UTC)

<p>That explains why I see these differences. I will use the DICOM segmentation IOD from now on.</p>
<p>I have some trouble though exporting to the Segmentation IOD using Slicer, since I get some errors .After installing the QuantitativeReporting ,the current version of Slicer I am using complains that  the DCMQI is not compatible and the QuantitativeReporting might not work properly.  When tried to export the segmentation as seen in the following  screenshot I got the following errors: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9136d1435c43415cbd495e2d4b19e0622bab1c9.png" data-download-href="/uploads/short-url/zxqvDLXeeHnchaX82sCWTVlI09b.png?dl=1" title="DICOMSEGerror" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9136d1435c43415cbd495e2d4b19e0622bab1c9_2_690x375.png" alt="DICOMSEGerror" data-base62-sha1="zxqvDLXeeHnchaX82sCWTVlI09b" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9136d1435c43415cbd495e2d4b19e0622bab1c9_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9136d1435c43415cbd495e2d4b19e0622bab1c9_2_1035x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9136d1435c43415cbd495e2d4b19e0622bab1c9_2_1380x750.png 2x" data-dominant-color="989797"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">DICOMSEGerror</span><span class="informations">2559×1391 521 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> )</p>
<p>I also tried to export the study as a DICOM segmentation object using an older Slicer version (4.11.0-2019-04-06)where the DCMQI was compatible but I got  another error there during the export.</p>
<p>I will try to use the binary dcmqi and see if the export will be succesful.</p>
<p>Thanks again to all of you for your assistance and valuable suggestions</p>

---

## Post #7 by @lassoan (2020-03-13 15:04 UTC)

<p>Please also try the latest Slicer Preview Release and let us know if you experience any issues. Thank you!</p>

---

## Post #8 by @athanell (2020-03-16 08:01 UTC)

<p>I have used the latest preview release (4.11.0-2020-03-10 r28818) but I still get the same error as above.</p>

---

## Post #9 by @lassoan (2020-03-18 03:59 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> are you aware of this issue?</p>

---

## Post #10 by @fedorov (2020-03-18 13:29 UTC)

<p>I will investigate later today, thank you for mentioning.</p>

---

## Post #11 by @fedorov (2020-03-18 16:01 UTC)

<p><a class="mention" href="/u/athanell">@athanell</a> how did you load the image you are segmenting?</p>
<p>It looks like it was not loaded from DICOM. If that is the case, with the current capabilities, it is not possible to export DICOM segmentation. The plugin should not crash, but other than the crash, it expects the reference image has the accompanying DICOM series.</p>

---

## Post #12 by @lassoan (2020-03-18 16:16 UTC)

<p>If your input images are not DICOM: You can load the images from non-DICOM format into Slicer and export to DICOM format. You can then import/load them to Slicer, specify segmentation, and export the segmentation to DICOM.</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> Probably we should simplify this process (we can export the referenced volume to DICOM, too, and generate all the necessary UIDs).</p>

---

## Post #13 by @fedorov (2020-03-18 17:26 UTC)

<p>I created an issue here <a href="https://github.com/QIICR/QuantitativeReporting/issues/247">https://github.com/QIICR/QuantitativeReporting/issues/247</a>.</p>
<p>Does it make sense to automatically export the referenced volume? I think that process should be interactive. Maybe it is better to give error to the user and ask to export the referenced volume as DICOM first?</p>

---

## Post #14 by @lassoan (2020-03-19 00:16 UTC)

<p>It would be nice to offer exporting the referenced volume, so that users can just click OK (export with volume) or Cancel (abort exporting so that the user can export the volume manually).</p>

---

## Post #15 by @athanell (2020-04-15 09:05 UTC)

<p>I apologize for the very late response Andrey. You are correct I didn’t load the volume in a DICOM format. After converting the volume to a DICOM I could export the segmentation correctly.<br>
Thank you for your assistance.</p>

---

## Post #16 by @athanell (2020-04-15 09:06 UTC)

<p>I apologize for the very late response Andras. Indeed as you mentioned after converting the volume to a DICOM I could export the segmentation correctly.<br>
Thank you again for your assistance.</p>

---
