# How load diffusionTensorImages from Dicom? 

**Topic ID**: 2544
**Date**: 2018-04-09
**URL**: https://discourse.slicer.org/t/how-load-diffusiontensorimages-from-dicom/2544

---

## Post #1 by @ElonKou (2018-04-09 16:02 UTC)

<p>Operating system : ubuntu 16.04<br>
Slicer version:4.8.1<br>
Expected behavior:Load DTI data from dicom files.<br>
Actual behavior:</p>
<p>Hi,I am new to 3dSlicer , and  I failed to load DTI files which from Hospital’s DVD(from Manufacturer SIEMENS).</p>
<p>the file structure is like this:<br>
dicom<br>
|-----18032098/<br>
|------58020000<br>
|         |----dcm1<br>
|         |----dcm2<br>
|         |----dcm…<br>
|------58020001<br>
|         |----dcm1<br>
|         |----dcm2<br>
|         |----dcm…<br>
I install slicerDMRI module and i want to load dti files to reconstruct Neural.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34c6d161d507706755bf537a0c0c70853ee33fae.png" data-download-href="/uploads/short-url/7wSNdy5TIhDTNxA5fsUmhlNs7Ei.png?dl=1" title="Screenshot%20from%202018-04-09%2018-31-29" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34c6d161d507706755bf537a0c0c70853ee33fae_2_690x170.png" alt="Screenshot%20from%202018-04-09%2018-31-29" data-base62-sha1="7wSNdy5TIhDTNxA5fsUmhlNs7Ei" width="690" height="170" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34c6d161d507706755bf537a0c0c70853ee33fae_2_690x170.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34c6d161d507706755bf537a0c0c70853ee33fae_2_1035x255.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34c6d161d507706755bf537a0c0c70853ee33fae_2_1380x340.png 2x" data-dominant-color="9BB4CC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-04-09%2018-31-29</span><span class="informations">1472×364 94 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I select the checkbox named “DICOMScalarVolumePlugin” + “MultiVolumeImportedPlugin” + “DicomRtimportPlugin”.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/4969c1fa7c8bcafadff21f7bcd4ca4adecd268e5.png" data-download-href="/uploads/short-url/atrrifkt6b7tE1DSLevfYIMxu1T.png?dl=1" title="Screenshot%20from%202018-04-09%2018-30-02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4969c1fa7c8bcafadff21f7bcd4ca4adecd268e5_2_690x97.png" alt="Screenshot%20from%202018-04-09%2018-30-02" data-base62-sha1="atrrifkt6b7tE1DSLevfYIMxu1T" width="690" height="97" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4969c1fa7c8bcafadff21f7bcd4ca4adecd268e5_2_690x97.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4969c1fa7c8bcafadff21f7bcd4ca4adecd268e5_2_1035x145.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4969c1fa7c8bcafadff21f7bcd4ca4adecd268e5_2_1380x194.png 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-04-09%2018-30-02</span><span class="informations">1919×272 63.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
when I Click the examine button to check all the files.It  shows some warning :"Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.  Reference image in series does not contain geometry information.  Please use caution. "</p>
<p>------------------------------------------------error---------------------------------<br>
all info about error in python interactor:<br>
reg inside examine<br>
Warning in DICOM plugin Scalar Volume when examining loadable 17: ep2d_diff_mddw_64_cor_TENSOR_TRACEW_MAP_BValue_700: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.  Reference image in series does not contain geometry information.  Please use caution.<br>
Warning in DICOM plugin Scalar Volume when examining loadable 16: ep2d_diff_mddw_64_cor_TENSOR_ADC_MAP: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.  Reference image in series does not contain geometry information.  Please use caution.<br>
Warning in DICOM plugin Scalar Volume when examining loadable 15: ep2d_diff_mddw_64_cor_TENSOR_FA_MAP: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.  Reference image in series does not contain geometry information.  Please use caution.<br>
Warning in DICOM plugin Scalar Volume when examining loadable 14: ep2d_diff_mddw_64_cor_TENSOR: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.  Reference image in series does not contain geometry information.  Please use caution.<br>
Warning in DICOM plugin Scalar Volume when examining loadable 9: ep2d_diff_mddw_64_cor: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.  Reference image in series does not contain geometry information.  Please use caution.<br>
Loading with imageIOName: GDCM<br>
No geomtry information available for DICOM data, skipping corner calculations<br>
Loading with imageIOName: GDCM<br>
Window/level found in DICOM tags (center=636.0, width=1275.0) has been applied to volume 5: t1_vibe_cor_1.8mm<br>
Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 1.1314e-05 mm, tolerance threshold is 0.001 mm).<br>
Loading with imageIOName: GDCM<br>
No geomtry information available for DICOM data, skipping corner calculations<br>
Loading with imageIOName: GDCM<br>
Window/level found in DICOM tags (center=55.0, width=145.0) has been applied to volume 11: ep2d_diff_mddw_64_cor_TRACEW<br>
Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 3.94772e-05 mm, tolerance threshold is 0.001 mm).<br>
Loading with imageIOName: GDCM<br>
Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
Loading with imageIOName: DCMTK<br>
Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
DICOM plugin failed to load ‘9: ep2d_diff_mddw_64_cor’ as a ‘Scalar Volume’.<br>
Traceback (most recent call last):<br>
File “/home/elonkou/MyProjects/Slicer-4.8.1-linux-amd64/lib/Slicer-4.8/qt-scripted-modules/DICOMLib/DICOMWidgets.py”, line 856, in proceedWithReferencedLoadablesSelection<br>
loadSuccess = plugin.load(loadable)<br>
File “/home/elonkou/MyProjects/Slicer-4.8.1-linux-amd64/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 547, in load<br>
addAcquisitionTransformIfNeeded=self.acquisitionGeometryRegularizationEnabled())<br>
File “/home/elonkou/MyProjects/Slicer-4.8.1-linux-amd64/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 780, in createAcquisitionTransform<br>
self.originalCorners = self.sliceCornersFromIJKToRAS(volumeNode)<br>
File “/home/elonkou/MyProjects/Slicer-4.8.1-linux-amd64/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 754, in sliceCornersFromIJKToRAS<br>
volumeNode.GetIJKToRASMatrix(ijkToRAS)<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetIJKToRASMatrix’</p>
<p>Loading with imageIOName: GDCM<br>
No geomtry information available for DICOM data, skipping corner calculations<br>
Loading with imageIOName: GDCM<br>
No geomtry information available for DICOM data, skipping corner calculations<br>
Loading with imageIOName: GDCM<br>
Window/level found in DICOM tags (center=127.0, width=328.0) has been applied to volume 6: t2_spc_stir_cor_p2_iso<br>
Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 0.000195456 mm, tolerance threshold is 0.001 mm).<br>
Loading with imageIOName: GDCM<br>
Window/level found in DICOM tags (center=632.0, width=1288.0) has been applied to volume 2: t2_tse_sag_384<br>
Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 3.84523e-05 mm, tolerance threshold is 0.001 mm).<br>
Loading with imageIOName: GDCM<br>
Window/level found in DICOM tags (center=315.0, width=814.0) has been applied to volume 8: t2_haste3d_fs_cor_iso_myelo_MIP_COR<br>
Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.35083e-06 mm, tolerance threshold is 0.001 mm).<br>
Loading with imageIOName: GDCM<br>
Window/level found in DICOM tags (center=819.0, width=1643.0) has been applied to volume 3: t2_tse_cor_384<br>
Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 2.52064e-05 mm, tolerance threshold is 0.001 mm).<br>
Loading with imageIOName: GDCM<br>
Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
Loading with imageIOName: DCMTK<br>
Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
Failed to read a multivolume: ‘NoneType’ object has no attribute ‘GetIJKToRASMatrix’<br>
Traceback (most recent call last):<br>
File “/home/elonkou/MyProjects/Slicer-4.8.1-linux-amd64/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 606, in load<br>
frame = scalarVolumePlugin.load(svLoadables[0])<br>
File “/home/elonkou/MyProjects/Slicer-4.8.1-linux-amd64/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 547, in load<br>
addAcquisitionTransformIfNeeded=self.acquisitionGeometryRegularizationEnabled())<br>
File “/home/elonkou/MyProjects/Slicer-4.8.1-linux-amd64/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 780, in createAcquisitionTransform<br>
self.originalCorners = self.sliceCornersFromIJKToRAS(volumeNode)<br>
File “/home/elonkou/MyProjects/Slicer-4.8.1-linux-amd64/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 754, in sliceCornersFromIJKToRAS<br>
volumeNode.GetIJKToRASMatrix(ijkToRAS)<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetIJKToRASMatrix’<br>
Loading with imageIOName: GDCM<br>
Window/level found in DICOM tags (center=1528.0, width=3140.0) has been applied to volume 10: ep2d_diff_mddw_64_cor_ADC<br>
Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 3.94772e-05 mm, tolerance threshold is 0.001 mm).<br>
Loading with imageIOName: GDCM<br>
Window/level found in DICOM tags (center=111.0, width=300.0) has been applied to volume 7: t2_haste3d_fs_cor_iso_myelo<br>
Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 0.000243026 mm, tolerance threshold is 0.001 mm).<br>
Loading with imageIOName: GDCM<br>
Window/level found in DICOM tags (center=500.0, width=1000.0) has been applied to volume 12: ep2d_diff_mddw_64_cor_FA<br>
Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 3.94772e-05 mm, tolerance threshold is 0.001 mm).<br>
Loading with imageIOName: GDCM<br>
Window/level found in DICOM tags (center=636.0, width=1340.0) has been applied to volume 4: t2_tse_tra<br>
Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 8.01715e-05 mm, tolerance threshold is 0.001 mm).</p>
<h2><a name="p-10327-could-not-load-9-ep2d_diff_mddw_64_cor-as-a-scalar-volume-could-not-load-ep2d_diff_mddw_64_cor_colfa-as-a-26-frames-multivolume-by-imagepositionpatientacquisitiontime-as-a-multivolume-1" class="anchor" href="#p-10327-could-not-load-9-ep2d_diff_mddw_64_cor-as-a-scalar-volume-could-not-load-ep2d_diff_mddw_64_cor_colfa-as-a-26-frames-multivolume-by-imagepositionpatientacquisitiontime-as-a-multivolume-1" aria-label="Heading link"></a>Could not load: 9: ep2d_diff_mddw_64_cor as a Scalar Volume<br>
Could not load: ep2d_diff_mddw_64_cor_ColFA - as a 26 frames MultiVolume by ImagePositionPatient+AcquisitionTime as a MultiVolume</h2>
<p>it seems that  the data is multi-frame image, so I check ed the file and found some DICOM file is a 3d-data (128 × 128 × 26)，what should i do to load these data?</p>
<h1><a name="p-10327-and-i-need-the-file-of-type-nrrd-and-i-also-failed-to-convert-it-to-nrrd-in-dwiconveter-moudule-it-tells-me-2" class="anchor" href="#p-10327-and-i-need-the-file-of-type-nrrd-and-i-also-failed-to-convert-it-to-nrrd-in-dwiconveter-moudule-it-tells-me-2" aria-label="Heading link"></a>and , I need  the file of type nrrd, and I also failed to convert it to nrrd in  DWIconveter  moudule, it tells me</h1>
<p>Diffusion-weighted DICOM Import (DWIConvert) standard error:</p>
<p>Exception thrown while reading DICOM volume</p>
<p>itk::ExceptionObject (0x10e3c4c0)<br>
Location: “unknown”<br>
File: /home/kitware/Dashboards/Package/Slicer-481-package/ITKv4/Modules/IO/ImageBase/include/itkImageSeriesReader.hxx<br>
Line: 370<br>
Description: itk::ERROR: ImageSeriesReader(0x10e27750): Size mismatch! The size of  /home/elonkou/Desktop/DTI/dicom/18032908/58020000/69462439 is [384, 384, 1] and does not match the required size [256, 256, 1] from file /home/elonkou/Desktop/DTI/dicom/18032908/58020000/69463693</p>
<p>Exception creating converter<br>
itk::ExceptionObject (0x10e3c4c0)<br>
Location: “unknown”<br>
File: /home/kitware/Dashboards/Package/Slicer-481-package/ITKv4/Modules/IO/ImageBase/include/itkImageSeriesReader.hxx<br>
Line: 370<br>
Description: itk::ERROR: ImageSeriesReader(0x10e27750): Size mismatch! The size of  /home/elonkou/Desktop/DTI/dicom/18032908/58020000/69462439 is [384, 384, 1] and does not match the required size [256, 256, 1] from file /home/elonkou/Desktop/DTI/dicom/18032908/58020000/69463693</p>
<p>Diffusion-weighted DICOM Import (DWIConvert) standard output:</p>
<h1><a name="p-10327-dwi-convert-public-lib-ctest-3" class="anchor" href="#p-10327-dwi-convert-public-lib-ctest-3" aria-label="Heading link"></a>======= DWI Convert Public Lib Ctest =========</h1>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7164d8edf462fd885c496d62908da05d743fc3a2.png" data-download-href="/uploads/short-url/gb819Ns3Ouzh7qhW5jtYU6yH4eC.png?dl=1" title="Screenshot%20from%202018-04-09%2018-35-23" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7164d8edf462fd885c496d62908da05d743fc3a2_2_690x353.png" alt="Screenshot%20from%202018-04-09%2018-35-23" data-base62-sha1="gb819Ns3Ouzh7qhW5jtYU6yH4eC" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7164d8edf462fd885c496d62908da05d743fc3a2_2_690x353.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7164d8edf462fd885c496d62908da05d743fc3a2_2_1035x529.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7164d8edf462fd885c496d62908da05d743fc3a2_2_1380x706.png 2x" data-dominant-color="98979B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-04-09%2018-35-23</span><span class="informations">1916×981 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>so , what should i do ,anyone who can help me ?</p>

---

## Post #2 by @ihnorton (2018-04-10 16:33 UTC)

<p>A post was merged into an existing topic: <a href="/t/is-there-any-method-to-convert-volume-to-diffusiontensorvolume/2553">Is there any method to convert volume to DiffusionTensorvolume?</a></p>

---

## Post #3 by @ihnorton (2018-04-10 16:33 UTC)



---
