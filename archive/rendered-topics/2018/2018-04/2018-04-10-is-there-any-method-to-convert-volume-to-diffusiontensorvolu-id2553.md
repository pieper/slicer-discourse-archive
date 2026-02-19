---
topic_id: 2553
title: "Is There Any Method To Convert Volume To Diffusiontensorvolu"
date: 2018-04-10
url: https://discourse.slicer.org/t/2553
---

# Is there any method to convert volume to DiffusionTensorvolume?

**Topic ID**: 2553
**Date**: 2018-04-10
**URL**: https://discourse.slicer.org/t/is-there-any-method-to-convert-volume-to-diffusiontensorvolume/2553

---

## Post #1 by @ElonKou (2018-04-10 07:23 UTC)

<p>I am using dti to reconstruct Neurological plexus.<br>
and I load the data from dicom, the type of  “node” is volume ,it 's not what  I need(DiffusionTensorVolume).<br>
how could I convert this type ?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa363340d36636fa6828cb34e23a0a61c6e0b63f.png" data-download-href="/uploads/short-url/ohLibM9C5AEEwRPpKgorGMdWqMT.png?dl=1" title="Screenshot%20from%202018-04-10%2015-17-56" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa363340d36636fa6828cb34e23a0a61c6e0b63f_2_689x413.png" alt="Screenshot%20from%202018-04-10%2015-17-56" data-base62-sha1="ohLibM9C5AEEwRPpKgorGMdWqMT" width="689" height="413" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa363340d36636fa6828cb34e23a0a61c6e0b63f_2_689x413.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa363340d36636fa6828cb34e23a0a61c6e0b63f_2_1033x619.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa363340d36636fa6828cb34e23a0a61c6e0b63f.png 2x" data-dominant-color="B0B0B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-04-10%2015-17-56</span><span class="informations">1195×717 214 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The dti folder was loaded when I chose examine, but there was no option for diffusion tensor volume, and the slicer gave me a warning.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b5a92aac93e4e1aedc515075657dd02ecad2d81.png" data-download-href="/uploads/short-url/d29v5maOZwQvl3n9Ui88mtKDE1r.png?dl=1" title="Screenshot%20from%202018-04-10%2015-27-41" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b5a92aac93e4e1aedc515075657dd02ecad2d81_2_690x98.png" alt="Screenshot%20from%202018-04-10%2015-27-41" data-base62-sha1="d29v5maOZwQvl3n9Ui88mtKDE1r" width="690" height="98" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b5a92aac93e4e1aedc515075657dd02ecad2d81_2_690x98.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b5a92aac93e4e1aedc515075657dd02ecad2d81_2_1035x147.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b5a92aac93e4e1aedc515075657dd02ecad2d81_2_1380x196.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-04-10%2015-27-41</span><span class="informations">1900×270 52.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
warning:<br>
Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.  Reference image in series does not contain geometry information.  Please use caution.</p>
<p>how can I load this dti files or convert it to diffusiontensorvolume nodes?</p>

---

## Post #2 by @ihnorton (2018-04-10 15:29 UTC)

<p>Hi <a class="mention" href="/u/elonkou">@ElonKou</a>, please try loading directly using the DWIConvert, which will create a diffusion <em>weighted</em> volume node (then use the “tensor estimation” module to calculate a DTI node).</p>
<p>Module page: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DWIConverter">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DWIConverter</a><br>
Tutorial: <a href="http://slicerdmri.github.io/docs/tutorials/DWIConverterTutorial.pdf">http://slicerdmri.github.io/docs/tutorials/DWIConverterTutorial.pdf</a></p>

---

## Post #3 by @ElonKou (2018-04-09 16:02 UTC)

<p>Operating system : ubuntu 16.04<br>
Slicer version:4.8.1<br>
Expected behavior:Load DTI data from dicom files.<br>
Actual behavior:</p>
<p>Hi,I am new to 3dSlicer , and  I failed to load DTI files which from Hospital’s DVD(from Manufacturer SIEMENS).</p>
<p>the file structure is like this:</p>
<pre><code class="lang-auto">dicom
     |-----18032098/
             |------58020000
             |         |----dcm1
             |         |----dcm2
             |         |----dcm...
             |------58020001
             |         |----dcm1
             |         |----dcm2
             |         |----dcm...
</code></pre>
<p>I install slicerDMRI module and i want to load dti files to reconstruct Neural.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34c6d161d507706755bf537a0c0c70853ee33fae.png" data-download-href="/uploads/short-url/7wSNdy5TIhDTNxA5fsUmhlNs7Ei.png?dl=1" title="Screenshot%20from%202018-04-09%2018-31-29" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34c6d161d507706755bf537a0c0c70853ee33fae_2_690x170.png" alt="Screenshot%20from%202018-04-09%2018-31-29" data-base62-sha1="7wSNdy5TIhDTNxA5fsUmhlNs7Ei" width="690" height="170" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34c6d161d507706755bf537a0c0c70853ee33fae_2_690x170.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34c6d161d507706755bf537a0c0c70853ee33fae_2_1035x255.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34c6d161d507706755bf537a0c0c70853ee33fae_2_1380x340.png 2x" data-dominant-color="9BB4CC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-04-09%2018-31-29</span><span class="informations">1472×364 94 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I select the checkbox named “DICOMScalarVolumePlugin” + “MultiVolumeImportedPlugin” + “DicomRtimportPlugin”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/4969c1fa7c8bcafadff21f7bcd4ca4adecd268e5.png" data-download-href="/uploads/short-url/atrrifkt6b7tE1DSLevfYIMxu1T.png?dl=1" title="Screenshot%20from%202018-04-09%2018-30-02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4969c1fa7c8bcafadff21f7bcd4ca4adecd268e5_2_690x97.png" alt="Screenshot%20from%202018-04-09%2018-30-02" data-base62-sha1="atrrifkt6b7tE1DSLevfYIMxu1T" width="690" height="97" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4969c1fa7c8bcafadff21f7bcd4ca4adecd268e5_2_690x97.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4969c1fa7c8bcafadff21f7bcd4ca4adecd268e5_2_1035x145.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4969c1fa7c8bcafadff21f7bcd4ca4adecd268e5_2_1380x194.png 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-04-09%2018-30-02</span><span class="informations">1919×272 63.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>when I Click the examine button to check all the files.It  shows some warning: <code>"Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.  Reference image in series does not contain geometry information.  Please use caution. "</code></p>
<p>------------------------------------------------error---------------------------------<br>
all info about error in python interactor:</p>
<pre><code class="lang-auto"> reg inside examine
Warning in DICOM plugin Scalar Volume when examining loadable 17: ep2d_diff_mddw_64_cor_TENSOR_TRACEW_MAP_BValue_700: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.  Reference image in series does not contain geometry information.  Please use caution.  
Warning in DICOM plugin Scalar Volume when examining loadable 16: ep2d_diff_mddw_64_cor_TENSOR_ADC_MAP: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.  Reference image in series does not contain geometry information.  Please use caution.  
Warning in DICOM plugin Scalar Volume when examining loadable 15: ep2d_diff_mddw_64_cor_TENSOR_FA_MAP: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.  Reference image in series does not contain geometry information.  Please use caution.  
Warning in DICOM plugin Scalar Volume when examining loadable 14: ep2d_diff_mddw_64_cor_TENSOR: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.  Reference image in series does not contain geometry information.  Please use caution.  
Warning in DICOM plugin Scalar Volume when examining loadable 9: ep2d_diff_mddw_64_cor: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.  Reference image in series does not contain geometry information.  Please use caution.  
Loading with imageIOName: GDCM
No geomtry information available for DICOM data, skipping corner calculations
Loading with imageIOName: GDCM
Window/level found in DICOM tags (center=636.0, width=1275.0) has been applied to volume 5: t1_vibe_cor_1.8mm
Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 1.1314e-05 mm, tolerance threshold is 0.001 mm).
Loading with imageIOName: GDCM
No geomtry information available for DICOM data, skipping corner calculations
Loading with imageIOName: GDCM
Window/level found in DICOM tags (center=55.0, width=145.0) has been applied to volume 11: ep2d_diff_mddw_64_cor_TRACEW
Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 3.94772e-05 mm, tolerance threshold is 0.001 mm).
Loading with imageIOName: GDCM
Could not read scalar volume using GDCM approach.  Error is: FileFormatError
Loading with imageIOName: DCMTK
Could not read scalar volume using DCMTK approach.  Error is: FileFormatError
DICOM plugin failed to load '9: ep2d_diff_mddw_64_cor' as a 'Scalar Volume'.
Traceback (most recent call last):
  File "/home/elonkou/MyProjects/Slicer-4.8.1-linux-amd64/lib/Slicer-4.8/qt-scripted-modules/DICOMLib/DICOMWidgets.py", line 856, in proceedWithReferencedLoadablesSelection
    loadSuccess = plugin.load(loadable)
  File "/home/elonkou/MyProjects/Slicer-4.8.1-linux-amd64/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 547, in load
    addAcquisitionTransformIfNeeded=self.acquisitionGeometryRegularizationEnabled())
  File "/home/elonkou/MyProjects/Slicer-4.8.1-linux-amd64/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 780, in createAcquisitionTransform
    self.originalCorners = self.sliceCornersFromIJKToRAS(volumeNode)
  File "/home/elonkou/MyProjects/Slicer-4.8.1-linux-amd64/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 754, in sliceCornersFromIJKToRAS
    volumeNode.GetIJKToRASMatrix(ijkToRAS)
AttributeError: 'NoneType' object has no attribute 'GetIJKToRASMatrix'

Loading with imageIOName: GDCM
No geomtry information available for DICOM data, skipping corner calculations
Loading with imageIOName: GDCM
No geomtry information available for DICOM data, skipping corner calculations
Loading with imageIOName: GDCM
Window/level found in DICOM tags (center=127.0, width=328.0) has been applied to volume 6: t2_spc_stir_cor_p2_iso
Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 0.000195456 mm, tolerance threshold is 0.001 mm).
Loading with imageIOName: GDCM
Window/level found in DICOM tags (center=632.0, width=1288.0) has been applied to volume 2: t2_tse_sag_384
Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 3.84523e-05 mm, tolerance threshold is 0.001 mm).
Loading with imageIOName: GDCM
Window/level found in DICOM tags (center=315.0, width=814.0) has been applied to volume 8: t2_haste3d_fs_cor_iso_myelo_MIP_COR
Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.35083e-06 mm, tolerance threshold is 0.001 mm).
Loading with imageIOName: GDCM
Window/level found in DICOM tags (center=819.0, width=1643.0) has been applied to volume 3: t2_tse_cor_384
Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 2.52064e-05 mm, tolerance threshold is 0.001 mm).
Loading with imageIOName: GDCM
Could not read scalar volume using GDCM approach.  Error is: FileFormatError
Loading with imageIOName: DCMTK
Could not read scalar volume using DCMTK approach.  Error is: FileFormatError
Failed to read a multivolume: 'NoneType' object has no attribute 'GetIJKToRASMatrix'
Traceback (most recent call last):
  File "/home/elonkou/MyProjects/Slicer-4.8.1-linux-amd64/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py", line 606, in load
    frame = scalarVolumePlugin.load(svLoadables[0])
  File "/home/elonkou/MyProjects/Slicer-4.8.1-linux-amd64/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 547, in load
    addAcquisitionTransformIfNeeded=self.acquisitionGeometryRegularizationEnabled())
  File "/home/elonkou/MyProjects/Slicer-4.8.1-linux-amd64/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 780, in createAcquisitionTransform
    self.originalCorners = self.sliceCornersFromIJKToRAS(volumeNode)
  File "/home/elonkou/MyProjects/Slicer-4.8.1-linux-amd64/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 754, in sliceCornersFromIJKToRAS
    volumeNode.GetIJKToRASMatrix(ijkToRAS)
AttributeError: 'NoneType' object has no attribute 'GetIJKToRASMatrix'
Loading with imageIOName: GDCM
Window/level found in DICOM tags (center=1528.0, width=3140.0) has been applied to volume 10: ep2d_diff_mddw_64_cor_ADC
Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 3.94772e-05 mm, tolerance threshold is 0.001 mm).
Loading with imageIOName: GDCM
Window/level found in DICOM tags (center=111.0, width=300.0) has been applied to volume 7: t2_haste3d_fs_cor_iso_myelo
Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 0.000243026 mm, tolerance threshold is 0.001 mm).
Loading with imageIOName: GDCM
Window/level found in DICOM tags (center=500.0, width=1000.0) has been applied to volume 12: ep2d_diff_mddw_64_cor_FA
Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 3.94772e-05 mm, tolerance threshold is 0.001 mm).
Loading with imageIOName: GDCM
Window/level found in DICOM tags (center=636.0, width=1340.0) has been applied to volume 4: t2_tse_tra
Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 8.01715e-05 mm, tolerance threshold is 0.001 mm).

Could not load: 9: ep2d_diff_mddw_64_cor as a Scalar Volume
Could not load: ep2d_diff_mddw_64_cor_ColFA - as a 26 frames MultiVolume by ImagePositionPatient+AcquisitionTime as a MultiVolume
</code></pre>
<hr>
<p>it seems that  the data is multi-frame image, so I check ed the file and found some DICOM file is a 3d-data (128 × 128 × 26)，what should i do to load these data?</p>
<p>and , I need  the file of type nrrd, and I also failed to convert it to nrrd in  DWIconveter  moudule, it tells me</p>
<pre><code class="lang-auto">===================================================
Diffusion-weighted DICOM Import (DWIConvert) standard error:

Exception thrown while reading DICOM volume

itk::ExceptionObject (0x10e3c4c0)
Location: "unknown" 
File: /home/kitware/Dashboards/Package/Slicer-481-package/ITKv4/Modules/IO/ImageBase/include/itkImageSeriesReader.hxx
Line: 370
Description: itk::ERROR: ImageSeriesReader(0x10e27750): Size mismatch! The size of  /home/elonkou/Desktop/DTI/dicom/18032908/58020000/69462439 is [384, 384, 1] and does not match the required size [256, 256, 1] from file /home/elonkou/Desktop/DTI/dicom/18032908/58020000/69463693


Exception creating converter 
itk::ExceptionObject (0x10e3c4c0)
Location: "unknown" 
File: /home/kitware/Dashboards/Package/Slicer-481-package/ITKv4/Modules/IO/ImageBase/include/itkImageSeriesReader.hxx
Line: 370
Description: itk::ERROR: ImageSeriesReader(0x10e27750): Size mismatch! The size of  /home/elonkou/Desktop/DTI/dicom/18032908/58020000/69462439 is [384, 384, 1] and does not match the required size [256, 256, 1] from file /home/elonkou/Desktop/DTI/dicom/18032908/58020000/69463693



Diffusion-weighted DICOM Import (DWIConvert) standard output:

======= DWI Convert Public Lib Ctest =========
===================================================
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7164d8edf462fd885c496d62908da05d743fc3a2.png" data-download-href="/uploads/short-url/gb819Ns3Ouzh7qhW5jtYU6yH4eC.png?dl=1" title="Screenshot%20from%202018-04-09%2018-35-23" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7164d8edf462fd885c496d62908da05d743fc3a2_2_690x353.png" alt="Screenshot%20from%202018-04-09%2018-35-23" data-base62-sha1="gb819Ns3Ouzh7qhW5jtYU6yH4eC" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7164d8edf462fd885c496d62908da05d743fc3a2_2_690x353.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7164d8edf462fd885c496d62908da05d743fc3a2_2_1035x529.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7164d8edf462fd885c496d62908da05d743fc3a2_2_1380x706.png 2x" data-dominant-color="98979B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-04-09%2018-35-23</span><span class="informations">1916×981 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>so , what should i do ,anyone who can help me ?</p>

---

## Post #4 by @ihnorton (2018-04-10 16:40 UTC)

<p>(Hi <a class="mention" href="/u/elonkou">@ElonKou</a>, I combined both of your messages in one thread)</p>
<p>Based on the screenshot in <a href="https://discourse.slicer.org/t/is-there-any-method-to-convert-volume-to-diffusiontensorvolume/2553/3?u=ihnorton">this message</a>, please try loading the following series <em>only</em>:</p>
<p><code>ep2d diff mddw 64 cor</code> (series 9)</p>
<p>All of the other ones with a longer name (like <code>ep2d diff mddw 64 cor TENSOR</code>) are derived sequences calculated on the scanner, and are not supported by DWIConvert. You could load some of the caculated ones like ADC or FA as scalar volumes, but for DTI analysis please start with the sequence identified above and use the calculation tools within Slicer.</p>
<p>Hope that helps.</p>

---

## Post #5 by @ElonKou (2018-04-11 05:05 UTC)

<p>Thanks for your reply, because I’m in China (bad network and opposite time zone), so it may not be timely.</p>
<p>I got a new set of data, the same type as the previous data. The data I got was in an entire folder, so I couldn’t tell which one was <code>ep2d_diff_mrrw_20_cor</code>. I used a python script to classify all files according to the series number of each dicom file, where series 4 is <code>ep2d_diff_mrrw_20_cor</code>, and then I used module DWIconvert to convert a series 4 folder to dwi, there is a problem here and the module shows that the size does not match.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67ae715ddbcdb5859f187dbea9cba921b6e9b25d.png" data-download-href="/uploads/short-url/eNcV8iyMQMMfS5gxZ4TB7BrkRwp.png?dl=1" title="Screenshot%20from%202018-04-11%2012-50-16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/67ae715ddbcdb5859f187dbea9cba921b6e9b25d_2_690x388.png" alt="Screenshot%20from%202018-04-11%2012-50-16" data-base62-sha1="eNcV8iyMQMMfS5gxZ4TB7BrkRwp" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/67ae715ddbcdb5859f187dbea9cba921b6e9b25d_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/67ae715ddbcdb5859f187dbea9cba921b6e9b25d_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/67ae715ddbcdb5859f187dbea9cba921b6e9b25d_2_1380x776.png 2x" data-dominant-color="EEEEED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-04-11%2012-50-16</span><span class="informations">1917×1079 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/1853749d5249d0dfe20349017b3c145bca238926.png" data-download-href="/uploads/short-url/3tcgeR9S2knpggBV0arVorrGAl0.png?dl=1" title="Screenshot%20from%202018-04-11%2012-59-15" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/1853749d5249d0dfe20349017b3c145bca238926_2_690x452.png" alt="Screenshot%20from%202018-04-11%2012-59-15" data-base62-sha1="3tcgeR9S2knpggBV0arVorrGAl0" width="690" height="452" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/1853749d5249d0dfe20349017b3c145bca238926_2_690x452.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/1853749d5249d0dfe20349017b3c145bca238926_2_1035x678.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/1853749d5249d0dfe20349017b3c145bca238926_2_1380x904.png 2x" data-dominant-color="F0F0F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-04-11%2012-59-15</span><span class="informations">1645×1079 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>the whole error info when use DWIconvert is:</p>
<blockquote>
<p>Diffusion-weighted DICOM Import (DWIConvert) standard error:<br>
Exception thrown while reading DICOM volume<br>
itk::ExceptionObject (0x58703e0)<br>
Location: “unknown”<br>
File: /home/kitware/Dashboards/Package/Slicer-481-&gt; package/ITKv4/Modules/IO/ImageBase/include/itkImageSeriesReader.hxx<br>
Line: 370<br>
Description: itk::ERROR: ImageSeriesReader(0x56fe370): Size mismatch! The size of<br>
/home/elonkou/Desktop/NEW_PATIENT/dicom4/54359274 is [128, 128, 27] and does not match the required size [128, 128, 1] from file /home/elonkou/Desktop/NEW_PATIENT/dicom4/54359274</p>
<p>Exception creating converter<br>
itk::ExceptionObject (0x58703e0)<br>
Location: “unknown”<br>
File: /home/kitware/Dashboards/Package/Slicer-481-package/ITKv4/Modules/IO/ImageBase/include/itkImageSeriesReader.hxx<br>
Line: 370<br>
Description: itk::ERROR: ImageSeriesReader(0x56fe370): Size mismatch! The size of  /home/elonkou/Desktop/NEW_PATIENT/dicom4/54359274 is [128, 128, 27] and does not match the required size [128, 128, 1] from file /home/elonkou/Desktop/NEW_PATIENT/dicom4/54359274</p>
<p>Diffusion-weighted DICOM Import (DWIConvert) standard output:</p>
<p>======= DWI Convert Public Lib Ctest =========</p>
</blockquote>
<p>I checked the unmatched files in python. All the files in the series 9 are 128 * 128 * 27. It seems that dwiconvert only supports 128 * 128 * 1 dicom files.</p>

---

## Post #6 by @ihnorton (2018-04-11 14:52 UTC)

<p>I think the most likely issue is still mis-sorting: DWIConvert requires that all files to be converted are from the same series (or at least identical acquisition parameters) and alone in one folder. You could try this script to do the sorting first:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pieper/dicomsort">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pieper/dicomsort" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/0b8354de26354339d858c8e2f17085c156454cc3fe3164ea74959fd6d1d404d8/pieper/dicomsort" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/pieper/dicomsort" target="_blank" rel="noopener">GitHub - pieper/dicomsort: A project to provide custom sorting and renaming...</a></h3>

  <p>A project to provide custom sorting and renaming of dicom files - GitHub - pieper/dicomsort: A project to provide custom sorting and renaming of dicom files</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>That said, if the data is from a Prisma or newer scanner, then I’m not sure if DWIConvert fully supports it yet. Please let us know the following tag information: (0008,0070) (0008,1090) (0018,1020)</p>
<p>e.g.:</p>
<p>(0008,0070) LO [SIEMENS]                                #   8, 1 Manufacturer<br>
(0008,1090) LO [Verio]                                  #   6, 1 ManufacturerModelName<br>
(0018,1020) LO [syngo MR B17]                           #  12, 1 SoftwareVersions</p>
<p>If you are using a Prisma or newer scanner version, then it would be very helpful if you are able to share phantom data – that’s the fastest way for me and <code>@hjmjohnson</code> to be able to fix problems and update supported versions.</p>

---

## Post #7 by @ElonKou (2018-04-12 02:55 UTC)

<p>The Tag of data is:</p>
<blockquote>
<p>(0008,0070) Manufacturer [SEMENS]<br>
(0008,1090) ManufacturerModelName [Skyra]<br>
(0018,1020) SoftwareVersions [Syngo MR D13]</p>
</blockquote>
<p>I used the dicomsort to classify the result and the program got an error. The error message was：</p>
<blockquote>
<p>Source file: /home/elonkou/Desktop/NEW_PATIENT/dicom/18041007/32070000/54361386<br>
Target file: /home/elonkou/Desktop/NEW_PATIENT_SORT/ServicePatient-MR00480109-SZ_hospital_l-spine-20171011/9_ep2d_diff_mddw_20_cor_TENSOR-1.dcm</p>
<p>Target file already exists - pattern is probably not unique<br>
Aborting to avoid data loss.</p>
</blockquote>
<p>In the 9th series, there were two files. There was an error. I modified the source code of dicomsort to skip the error, and finally got a folder. The classification in this folder is the same as my previous classification. (My classification is based on the dicom’s file seriesNumber or SeriesInstanceUID)</p>
<p>Since I have not yet been able to shield the patient’s information, I cannot send it out yet.</p>
<p>According to the categorized file information, it seems that the number of DWI source files is a little bit larger. Series 4 is a dicom file, and there are 83 in total. The size of each dicom file is 128 * 128 * 27</p>

---

## Post #8 by @ihnorton (2018-04-16 18:16 UTC)

<p>Hi <a class="mention" href="/u/elonkou">@ElonKou</a>, thanks for sharing the data with me. It looks like Skyra (or at least this acquisition/protocol) uses a multiframe representation (edit: <em>for MOSAIC</em>), with gradient and b-value stored in frame metadata (normal tags, but they are embedded per frame). It is different than the other Skyra data I have seen so far – which is only a few datasets.</p>
<p>I don’t think DWIConvert supports this type of data yet. dcm2nii seems to somewhat support it, but for your data at least dcm2nii does not create a bvec/bval pair (because apparently it requires a baseline – the data you shared seems to only have b=700 for all frames).</p>
<p>cc <a class="mention" href="/u/hjmjohnson">@hjmjohnson</a> in case you have any experience/comments on Skyra support.</p>

---

## Post #9 by @ihnorton (2018-04-16 18:33 UTC)

<p>Actually, looking at this a bit more, I think this data <em>is</em> MOSAIC, but Siemens has changed how they store the data — now they use standard multi-frame DICOM, whereas on older scanner versions MOSAIC was stored in a Siemens-specific way (essentially tiled in the pixel data of a single frame).</p>

---

## Post #10 by @ElonKou (2018-04-20 06:21 UTC)

<p>Thank you for your reply. If there is any other way to read DWI data, please let me know. I’m also trying to read data directly from dicom and then converting it to NRRD so that I can skip the plug-in DWIconvert. If you have a way to merge the contents of a dicom file into an nrrd, please let me know, thanks very much!</p>

---

## Post #11 by @ihnorton (2018-04-20 14:01 UTC)

<p>I have started a patch to DWIConvert, but didn’t have a chance to finish it yet. Do you happen to know about any option on the scanner to write the DWI data as multiframe rather than MOSAIC? We don’t have any scanners running Syngo D13 here (I’ve been checking around to try to find some non-anonymous test data locally, but no one knows how to create such a dataset. Our scanners are on E11).</p>
<p>(as I mentioned, I tried another well-known converter called <code>dcm2nii</code> and it did not succeed either for your data)</p>

---

## Post #12 by @ElonKou (2018-04-23 08:14 UTC)

<p>I also tried the dcm2nii plugin and it did not succeed.<br>
I am very embarrassed that I do not have some options for generating DWI on Siemens equipment. My data is copied from the hospital CD.<br>
This data can be read out using MTIK, but there is an error, I can not confirm whether or not the MITK is read correctly, and the nrrd file exported by MITK cannot be opened in Slicer (Slicer does not report any error).<br>
In addition, DWIconvet seems to have a function to decode the mosaic (<a href="https://github.com/BRAINSia/BRAINSTools/blob/master/DWIConvert/SiemensDWIConverter.cxx#L423" rel="nofollow noopener">https://github.com/BRAINSia/BRAINSTools/blob/master/DWIConvert/SiemensDWIConverter.cxx#L423</a>)<br>
Thank you very much for your help. If you have any other solution to this problem, please let me know.</p>

---

## Post #13 by @ElonKou (2018-05-03 03:39 UTC)

<p>Thank you very much for your help. I have already solved this problem.<br>
I read all the pixel-data, gradients, bvalues from the dicom series and wrote them all to the dwi node. Then I get the dwi-node ,and can use it to continue my reconstruction of the DTI-neurons. Thank you again for your help.</p>

---
