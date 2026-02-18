# Annotation Ruler 

**Topic ID**: 1550
**Date**: 2017-11-28
**URL**: https://discourse.slicer.org/t/annotation-ruler/1550

---

## Post #1 by @pkharris (2017-11-28 21:22 UTC)

<p>Hello!</p>
<p>I am using 3D Slicer in order to measure certain vertical measurements and angular measurements of the mandible. I am noticing that the millimeter measurements are not giving me the correct measurement. For example, a measurement that should be reading 65mm (vertical height of the ramus), is giving me 185mm in 3D Slicer. Is there a solution to this problem? Is there some sort of way to calibrate the 3D Slicer ruler based on the original CBCT scan information?</p>

---

## Post #2 by @cpinter (2017-11-28 21:41 UTC)

<p>If you go to the Volumes module and open Volume Information you can check the spacing values. Are they as expected?</p>

---

## Post #3 by @pkharris (2017-11-28 22:38 UTC)

<p>Thank you for your prompt response!</p>
<p>My initial CBCT scan files were exported from Dolphin 3D. I first sculpted<br>
the body of the mandible out, in order to obtain more accurate<br>
measurements. Then I exported the DICOM file of the sculpted mandible, from<br>
Dolphin 3D, and opened the file in 3D Slicer.<br>
After this was done, I went into the Volumes module of 3D Slicer, to adjust<br>
the spacing values and origin values.</p>
<p>For more clarification, I have attached a screenshot to this email. On the<br>
right, is 3D Slicer with the Volume Information available to be adjusted.<br>
On the left, is Dolphin 3D with the original values of the CBCT scan.</p>
<p>Do the numbers listed for ‘Image Spacing’ and ‘Image Origin’ in 3D Slicer<br>
make sense, given the original values in Dolphin 3D?</p>
<p>Peyton</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/4237be72c992080ff309e89598feffeac7f7af4e.jpg" data-download-href="/uploads/short-url/9rMWwiYLmViYPuARMEhBKYvs0vY.jpg?dl=1" title="Ruler Calibration Issue.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/4237be72c992080ff309e89598feffeac7f7af4e_2_690x431.jpg" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/4237be72c992080ff309e89598feffeac7f7af4e_2_690x431.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/4237be72c992080ff309e89598feffeac7f7af4e_2_1035x646.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/4237be72c992080ff309e89598feffeac7f7af4e_2_1380x862.jpg 2x" data-dominant-color="91A0BB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ruler Calibration Issue.jpg</span><span class="informations">2560×1600 539 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2017-11-29 00:24 UTC)

<p>Volume Size (Voxels) = Image Dimensions in Slicer<br>
Voxel Size (mm^3) = Image Spacing in Slicer</p>
<p>Dolphin 3D does not show position of image origin.</p>
<p>How did you export the volume from Dolphin 3D? What file format did you export to? Were there any options for the export?</p>

---

## Post #5 by @pkharris (2017-11-29 20:03 UTC)

<p>Thank you for your prompt response, and your help! My apologies for the<br>
delay.</p>
<p>I have attached a screen shot of the method I use to export the file. I<br>
choose to export the file at ‘1:1 No Loss/Uncompressed’, and I export it as<br>
a single DICOM file. I save the file to a local folder, and then upload<br>
that file directly to the 3D Slicer software. There are various options to<br>
save the file, which can be seen in the attachment. There are also other<br>
options for compression, which I do not choose.</p>
<p>Peyton</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/a464a7d2416e50683ab0fc15bf211ed66447caf4.jpg" data-download-href="/uploads/short-url/nshXra69vMQg65FABFF72LyUwgk.jpg?dl=1" title="Ruler Calibration Issue-2.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/a464a7d2416e50683ab0fc15bf211ed66447caf4_2_690x431.jpg" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/a464a7d2416e50683ab0fc15bf211ed66447caf4_2_690x431.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/a464a7d2416e50683ab0fc15bf211ed66447caf4_2_1035x646.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/a464a7d2416e50683ab0fc15bf211ed66447caf4_2_1380x862.jpg 2x" data-dominant-color="5A7897"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ruler Calibration Issue-2.jpg</span><span class="informations">2560×1600 419 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2017-11-29 20:23 UTC)

<p>Could you please send us the DICOM metadata of the image? See instructions here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#How_to_obtain_DICOM_metadata">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#How_to_obtain_DICOM_metadata</a></p>

---

## Post #7 by @pkharris (2017-11-29 23:08 UTC)

<p>For some reason, the “Copy Metadata” button was not listed.<br>
I have taken a screenshot of the window that appears in order for me to<br>
obtain the Metadata for the scan.<br>
Is there a way for me to copy the metadata, that I am not seeing?</p>
<p>[image deleted]</p>

---

## Post #8 by @pkharris (2017-11-29 23:15 UTC)

<p>I have attached a better screenshot to this email.</p>
<p>My apologies!<br>
Peyton</p>
<p>[Image deleted]</p>

---

## Post #9 by @pieper (2017-11-30 13:52 UTC)

<p>Hi - could you use the anonymize option when exporting from Dolphin and the latest version of Slicer (4.8) to get access to the option for copying metadata.</p>
<p>Thanks</p>

---

## Post #10 by @pkharris (2017-11-30 18:06 UTC)

<p>Thank you again for those specific instructions! I was able to get access<br>
to copying the metadata.</p>
<p>Hope to hear from you all soon!</p>
<p>[0008,0005] SpecificCharacterSet ISO_IR 100 CS 10<br>
[0008,0008] ImageType [2] DERIVED, PRIMARY CS 16<br>
[0008,0012] InstanceCreationDate 20171130 DA 8<br>
[0008,0013] InstanceCreationTime 120140.0 TM 8<br>
[0008,0014] InstanceCreatorUID 99999 UI 6<br>
[0008,0016] SOPClassUID 1.2.840.10008.5.1.4.1.1.2 UI 26<br>
[0008,0018] SOPInstanceUID<br>
2.16.840.1.114363.0999.000.1.1.1512064900.0.123380.23376.28.1 UI 62<br>
[0008,0020] StudyDate 20171130 DA 8<br>
[0008,0021] SeriesDate 20171130 DA 8<br>
[0008,0022] AcquisitionDate 20171130 DA 8<br>
[0008,0023] ContentDate 20171130 DA 8<br>
[0008,0030] StudyTime 120140.0 TM 8<br>
[0008,0031] SeriesTime 120140.0 TM 8<br>
[0008,0032] AcquisitionTime 175436 TM 6<br>
[0008,0033] ContentTime 120140.0 TM 8<br>
[0008,0050] AccessionNumber  SH 0<br>
[0008,0060] Modality CT CS 2<br>
[0008,0070] Manufacturer Imaging Sciences International LO 30<br>
[0008,0080] InstitutionName Sellke and Reily Ortho LO 22<br>
[0008,0081] InstitutionAddress 30 North Slusser Street<br>
Suite 1<br>
Grayslake, IL 60030 ST 52<br>
[0008,0090] ReferringPhysicianName  PN 0<br>
[0008,1010] StationName I-CAT SH 6<br>
[0008,103e] SeriesDescription Dolphin3D Internal LO 18<br>
[0008,1050] PerformingPhysicianName  PN 0<br>
[0008,1070] OperatorsName ortho PN 6<br>
[0008,1090] ManufacturerModelName 17-19 LO 6<br>
[0009,0100] Unknown Tag &amp; Data 11753 LO 6<br>
[0009,0101] Unknown Tag &amp; Data 1 IS 2<br>
[0010,0010] PatientName Anonymous Anonymous PN 20<br>
[0010,0020] PatientID Anonymous LO 10<br>
[0010,0030] PatientBirthDate 20000101 DA 8<br>
[0010,0040] PatientSex M CS 2<br>
[0010,2160] EthnicGroup  SH 0<br>
[0010,4000] PatientComments  LT 0<br>
[0018,0022] ScanOptions LANDSCAPE CS 10<br>
[0018,0050] SliceThickness 0.399998009204865 DS 18<br>
[0018,0060] KVP 120 DS 4<br>
[0018,0090] DataCollectionDiameter 130.00 DS 6<br>
[0018,1000] DeviceSerialNumber ICU-080677 LO 10<br>
[0018,1020] SoftwareVersions 1.9.3.13 LO 8<br>
[0018,1150] ExposureTime 4 IS 2<br>
[0018,1151] XRayTubeCurrent 5 IS 2<br>
[0018,5100] PatientPosition  CS 0<br>
[0019,1000] Unknown Tag &amp; Data ISI_ACQU_1 LO 10<br>
[0019,1043] Unknown Tag &amp; Data 1 IS 2<br>
[0019,1050] Unknown Tag &amp; Data 55.4864848409 DS 14<br>
[0019,1051] Unknown Tag &amp; Data 42.0000000000 DS 14<br>
[0019,2000] Unknown Tag &amp; Data  LO 0<br>
[0019,2001] Unknown Tag &amp; Data lVCVRGUmP71OnVPQKhMWnTlcQQ0 LO 28<br>
[0020,000d] StudyInstanceUID<br>
2.16.840.1.114363.0999.000.1.1.1512064900.0.123548.25381.13260.2 UI 64<br>
[0020,000e] SeriesInstanceUID<br>
2.16.840.1.114363.0999.000.1.1.1512064900.0.123548.1950.21266.29 UI 64<br>
[0020,0010] StudyID 1 SH 2<br>
[0020,0011] SeriesNumber 1 IS 2<br>
[0020,0012] AcquisitionNumber 164 IS 4<br>
[0020,0013] InstanceNumber 1 IS 2<br>
[0020,0032] ImagePositionPatient [3] -200, -200, -30.7999992370605 DS 28<br>
[0020,0037] ImageOrientationPatient [6] 1.000000, 0.000000, 0.000000,<br>
0.000000, 1.000000, 0.000000 DS 54<br>
[0020,0052] FrameOfReferenceUID<br>
2.16.840.114421.80677.9451500894.9483036894 UI 44<br>
[0020,1040] PositionReferenceIndicator  LO 0<br>
[0020,1041] SliceLocation -30.7999992370605 DS 18<br>
[0021,1032] Unknown Tag &amp; Data 18.537371 DS 10<br>
[0021,1034] Unknown Tag &amp; Data 8.883619 DS 8<br>
[0028,0002] SamplesPerPixel 1 US 2<br>
[0028,0004] PhotometricInterpretation MONOCHROME2 CS 12<br>
[0028,0008] NumberOfFrames 256 IS 4<br>
[0028,0010] Rows 291 US 2<br>
[0028,0011] Columns 387 US 2<br>
[0028,0030] PixelSpacing [2] 0.400000005960464, 0.400000005960464 DS 36<br>
[0028,0100] BitsAllocated 16 US 2<br>
[0028,0101] BitsStored 16 US 2<br>
[0028,0102] HighBit 15 US 2<br>
[0028,0103] PixelRepresentation 0 US 2<br>
[0028,0106] SmallestImagePixelValue 0 US 2<br>
[0028,0107] LargestImagePixelValue 65535 US 2<br>
[0028,1050] WindowCenter 600 DS 4<br>
[0028,1051] WindowWidth 3200 DS 4<br>
[0028,1052] RescaleIntercept -1000 DS 6<br>
[0028,1053] RescaleSlope 1 DS 2<br>
[0032,4000] RETIRED_StudyComments  LT 0<br>
[7fe0,0010] PixelData 0000 OW 57659904<br>
[aaa1,2020] Unknown Tag &amp; Data 0 0 0 0 30 72 SH 14</p>

---

## Post #11 by @lassoan (2017-11-30 20:51 UTC)

<p>I just remember that we have added a some rules to the DICOM Patcher module that fixes these Dolphin3D-exported files (they are not conform to the DICOM standard). Please run the DICOM Patcher module on your data set and then import it into Slicer. Voxel sizes in these patched DICOM files should be correct.</p>
<p>If you have a support contract with Dolphin3D manufacturer then you may let them know that their DICOM-exported files are invalid and they may contact us for details on how to fix their exporter.</p>

---

## Post #12 by @pkharris (2017-11-30 22:43 UTC)

<p>Thank you so much for the suggestion!</p>
<p>I did run the DICOM Patcher Module for the scan, which did correct the<br>
voxel discrepancy.</p>
<p>I’m still having the issue with the ruler calibration though.</p>
<p>I have attached screenshots of the issue, and the metadata.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/d141195c467e0a6d3bdcbaf43f1d25361a8a26b7.jpg" data-download-href="/uploads/short-url/tR9gsioxmgWrHs6tYN4slJAJLTN.jpg?dl=1" title="Ruler Calibration Issue-4.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d141195c467e0a6d3bdcbaf43f1d25361a8a26b7_2_690x431.jpg" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d141195c467e0a6d3bdcbaf43f1d25361a8a26b7_2_690x431.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d141195c467e0a6d3bdcbaf43f1d25361a8a26b7_2_1035x646.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d141195c467e0a6d3bdcbaf43f1d25361a8a26b7_2_1380x862.jpg 2x" data-dominant-color="96A7C0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ruler Calibration Issue-4.jpg</span><span class="informations">2560×1600 443 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #13 by @lassoan (2017-12-01 02:20 UTC)

<p>These fields specify voxel size (image spacing):</p>
<pre><code>[0018,0050] SliceThickness 0.399998009204865 DS 18
[0028,0030] PixelSpacing [2] 0.400000005960464, 0.400000005960464 DS 36
</code></pre>
<p>Can you check what image spacing values do you see in Volumes module? (they should be 0.4 0.4 0.4)</p>

---

## Post #14 by @haylea.b (2018-07-20 10:15 UTC)

<p>Hi I am wanting to calibrate the ruler for measurements of teeth as it is incorrect, is there a way I can do this? thank you in advance <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=5" title=":smile:" class="emoji" alt=":smile:"></p>

---

## Post #15 by @muratmaga (2018-07-21 05:07 UTC)

<p>As the prior discussion indicates, Slicer simply uses the image spacing provided by your dataset. Did you import the data from DICOM series? If so, try running the dicom patcher as indicated.</p>

---
