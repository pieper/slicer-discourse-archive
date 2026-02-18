# Failure to load RTSTRUCT dicom file

**Topic ID**: 33504
**Date**: 2023-12-22
**URL**: https://discourse.slicer.org/t/failure-to-load-rtstruct-dicom-file/33504

---

## Post #1 by @Michele_R (2023-12-22 22:30 UTC)

<p>Operating system: MacOS Ventura<br>
Slicer version: 5.7.0</p>
<p>Hello,<br>
I am trying to load an image set including a 3D MRI with RT files containing volumetric and dosimetric information that have been exported from a DICOM viewer. I want to view the volume segmentations on the images in Slicer. I have installed SlicerRT, QuantitativeReporting and Sandbox extensions.</p>
<p>When I import the dicom files through the dicom import button, I get an error message saying that some files failed to load. the volumetric MRI appears correctly and the RT files do not load correctly. the RT files have a .dcm extension.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/beea27e980bdddf847698b95f6049d14bc82b9d3.jpeg" data-download-href="/uploads/short-url/reUoyC8JveuIlnwFQBWp6xuFAjN.jpeg?dl=1" title="Capture d’écran 2023-12-22 à 16.41.44" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/beea27e980bdddf847698b95f6049d14bc82b9d3_2_690x334.jpeg" alt="Capture d’écran 2023-12-22 à 16.41.44" data-base62-sha1="reUoyC8JveuIlnwFQBWp6xuFAjN" width="690" height="334" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/beea27e980bdddf847698b95f6049d14bc82b9d3_2_690x334.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/beea27e980bdddf847698b95f6049d14bc82b9d3_2_1035x501.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/beea27e980bdddf847698b95f6049d14bc82b9d3_2_1380x668.jpeg 2x" data-dominant-color="949498"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2023-12-22 à 16.41.44</span><span class="informations">1920×932 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d289428a013eaf0aca7760b8c1809a552b40c83.jpeg" data-download-href="/uploads/short-url/49WMKabC4InY6M04uY7pMoJQaUr.jpeg?dl=1" title="Capture d’écran 2023-12-22 à 16.41.52" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d289428a013eaf0aca7760b8c1809a552b40c83_2_690x340.jpeg" alt="Capture d’écran 2023-12-22 à 16.41.52" data-base62-sha1="49WMKabC4InY6M04uY7pMoJQaUr" width="690" height="340" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d289428a013eaf0aca7760b8c1809a552b40c83_2_690x340.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d289428a013eaf0aca7760b8c1809a552b40c83_2_1035x510.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d289428a013eaf0aca7760b8c1809a552b40c83_2_1380x680.jpeg 2x" data-dominant-color="9B9A9F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2023-12-22 à 16.41.52</span><span class="informations">1920×947 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>here is the Python error log:<br>
AttributeError: module ‘modules’ has no attribute ‘dicomsroimportexport’<br>
[Python] DICOM Plugin failed: module ‘modules’ has no attribute ‘dicomsroimportexport’<br>
[Python] Warning in DICOM plugin Scalar Volume when examining loadable Unnamed Series: Reference image in series does not contain geometry information. Please use caution.<br>
[VTK] vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /Volumes/Crucial X8/SLICER/SLICER test AVM case 2/Avm_Case_02_Gp/Rm_Stereotassica_Cmc - 330253576/unnamed_0/IM-0001-10000-0001.dcm. ITK exception info: error in unknown:  Could not create IO object for reading file /Volumes/Crucial X8/SLICER/SLICER test AVM case 2/Avm_Case_02_Gp/Rm_Stereotassica_Cmc - 330253576/unnamed_0/IM-0001-10000-0001.dcm<br>
[VTK]   Tried to create one of the following:<br>
[VTK]     BMPImageIO<br>
[VTK]     BioRadImageIO<br>
[VTK]     DCMTKImageIO<br>
[VTK]     GDCMImageIO<br>
[VTK]     GiplImageIO<br>
[VTK]     JPEGImageIO<br>
[VTK]     LSMImageIO<br>
[VTK]     MGHImageIO<br>
[VTK]     MINCImageIO<br>
[VTK]     MRCImageIO<br>
[VTK]     MetaImageIO<br>
[VTK]     NiftiImageIO<br>
[VTK]     NrrdImageIO<br>
[VTK]     PNGImageIO<br>
[VTK]     ScancoImageIO<br>
[VTK]     StimulateImageIO<br>
[VTK]     TIFFImageIO<br>
[VTK]     VTKImageIO<br>
[VTK]     MRMLIDImageIO<br>
[VTK]     Bruker2dseqImageIO<br>
[VTK]     GE4ImageIO<br>
[VTK]     GE5ImageIO<br>
[VTK]     HDF5ImageIO<br>
[VTK]     JPEG2000ImageIO<br>
[VTK]   You probably failed to set a file suffix, or<br>
[VTK]     set the suffix to an unsupported type.<br>
[VTK] Algorithm vtkITKArchetypeImageSeriesVectorReaderFile (0x7fe46d86f670) returned failure for request: vtkInformation (0x600008bd2940)<br>
[VTK]   Debug: Off<br>
[VTK]   Modified Time: 630465<br>
[VTK]   Reference Count: 1<br>
[VTK]   Registered Events: (none)<br>
[VTK]   Request: REQUEST_INFORMATION<br>
[VTK]   ALGORITHM_AFTER_FORWARD: 1<br>
[VTK]   FORWARD_DIRECTION: 0<br>
[Python] Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[VTK] vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /Volumes/Crucial X8/SLICER/SLICER test AVM case 2/Avm_Case_02_Gp/Rm_Stereotassica_Cmc - 330253576/unnamed_0/IM-0001-10000-0001.dcm. ITK exception info: error in unknown:  Could not create IO object for reading file /Volumes/Crucial X8/SLICER/SLICER test AVM case 2/Avm_Case_02_Gp/Rm_Stereotassica_Cmc - 330253576/unnamed_0/IM-0001-10000-0001.dcm<br>
[VTK]   Tried to create one of the following:<br>
[VTK]     BMPImageIO<br>
[VTK]     BioRadImageIO<br>
[VTK]     DCMTKImageIO<br>
[VTK]     GDCMImageIO<br>
[VTK]     GiplImageIO<br>
[VTK]     JPEGImageIO<br>
[VTK]     LSMImageIO<br>
[VTK]     MGHImageIO<br>
[VTK]     MINCImageIO<br>
[VTK]     MRCImageIO<br>
[VTK]     MetaImageIO<br>
[VTK]     NiftiImageIO<br>
[VTK]     NrrdImageIO<br>
[VTK]     PNGImageIO<br>
[VTK]     ScancoImageIO<br>
[VTK]     StimulateImageIO<br>
[VTK]     TIFFImageIO<br>
[VTK]     VTKImageIO<br>
[VTK]     MRMLIDImageIO<br>
[VTK]     Bruker2dseqImageIO<br>
[VTK]     GE4ImageIO<br>
[VTK]     GE5ImageIO<br>
[VTK]     HDF5ImageIO<br>
[VTK]     JPEG2000ImageIO<br>
[VTK]   You probably failed to set a file suffix, or<br>
[VTK]     set the suffix to an unsupported type.<br>
[VTK] Algorithm vtkITKArchetypeImageSeriesVectorReaderFile (0x7fe46d9a0450) returned failure for request: vtkInformation (0x600004b85080)<br>
[VTK]   Debug: Off<br>
[VTK]   Modified Time: 630560<br>
[VTK]   Reference Count: 1<br>
[VTK]   Registered Events: (none)<br>
[VTK]   Request: REQUEST_INFORMATION<br>
[VTK]   ALGORITHM_AFTER_FORWARD: 1<br>
[VTK]   FORWARD_DIRECTION: 0<br>
[Python] Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[Python] Could not load: Unnamed Series as a Scalar Volume<br>
[FD] [49433:149507:1222/162444.029558:ERROR:gl_context_cgl.cc(118)] Error creating context.</p>
<p>I tried to export the ROIs from Horos to <em>Osirix ROI</em> format and <em>.xml</em> but cannot load these either.</p>
<p>Could the issue lie with the file metadata (they could be corrupted when exported from the Dicom viewer)? or rather the Slicer program itself?</p>
<p>sidenote: the same cases have been segmented in Brainlab’s Elements software and exported, and these load correctly on Slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3704d46e21f84a9dee028d205b05f0660eccd93.jpeg" data-download-href="/uploads/short-url/njQqRF1feldov27ZHir4rwAfyiD.jpeg?dl=1" title="Capture d’écran 2023-12-22 à 16.44.20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3704d46e21f84a9dee028d205b05f0660eccd93_2_690x335.jpeg" alt="Capture d’écran 2023-12-22 à 16.44.20" data-base62-sha1="njQqRF1feldov27ZHir4rwAfyiD" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3704d46e21f84a9dee028d205b05f0660eccd93_2_690x335.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3704d46e21f84a9dee028d205b05f0660eccd93_2_1035x502.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3704d46e21f84a9dee028d205b05f0660eccd93_2_1380x670.jpeg 2x" data-dominant-color="969898"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2023-12-22 à 16.44.20</span><span class="informations">1920×933 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Michele_R (2023-12-27 17:53 UTC)

<p>update: after trying to load sample files with RT data unsuccessfully and reinstalling 3D SLICER (latest stable version 5.6.1 and preview release 5.7.0) with SlicerRT extension also without any better results I <strong>downloaded a previous release of 3D SLICER (5.2.2) and it works seamlessly.</strong></p>
<p>the RTSTRUCT files seem to be intact and the issue might have been related to the location/path to retrieve the extensions/modules (dicomimportexport error).</p>
<p>PS: the latest stable Windows release, with SlicerRT did not function either.</p>

---

## Post #3 by @cpinter (2024-01-02 10:50 UTC)

<p>Yes, unfortunately there is a problem with certain extensions on MacOS.</p>
<p>Thanks for posting the outcome as well.</p>

---

## Post #4 by @fedorov (2024-03-06 17:23 UTC)

<p>I have the same problem on Mac. Current preview fails the same way as the preview release I had from January in this line <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomSroImportExport/DicomSroImportExportPlugin.py#L40:" class="inline-onebox">SlicerRT/DicomSroImportExport/DicomSroImportExportPlugin.py at master · SlicerRt/SlicerRT · GitHub</a></p>
<pre><code class="lang-auto">AttributeError: module 'modules' has no attribute 'dicomrtimportexport'
[Python] DICOM Plugin failed: module 'modules' has no attribute 'dicomrtimportexport'
Traceback (most recent call last):
  File "/Applications/Slicer-5.7.0-20240306.app/Contents/lib/Slicer-5.7/qt-scripted-modules/DICOMLib/DICOMUtils.py", line 765, in getLoadablesFromFileLists
    loadablesByPlugin[plugin] = plugin.examineForImport(fileLists)
  File "/Applications/Slicer-5.7.0-20240306.app/Contents/Extensions-32750/SlicerRT/lib/Slicer-5.7/qt-scripted-modules/DicomSroImportExportPlugin.py", line 40, in examineForImport
    slicer.modules.dicomsroimportexport.logic().ExamineForLoad(vtkFileList, loadablesCollection)
AttributeError: module 'modules' has no attribute 'dicomsroimportexport'
[Python] DICOM Plugin failed: module 'modules' has no attribute 'dicomsroimportexport'
</code></pre>
<p>Full error log is here: <a href="https://gist.github.com/fedorov/365d782ffb9813b1a0f08c03857ab207" class="inline-onebox">SlicerRT error log - Slicer 5.7.0-2024-03-04 · GitHub</a></p>
<p>The impact of this error is that it is currently impossible to load DICOM RTSTRUCT at all, so this is a major regression. I have not been able to find a workaround. I also have the same error in the current stable 5.6.1.</p>
<p>Is there any plan/resources to fix this?</p>

---

## Post #5 by @pieper (2024-03-06 17:57 UTC)

<p>The errors at the top of the log point to a <code>libomp.dylib</code>.  Is that missing from the package but available in a local build?</p>
<pre><code class="lang-auto">Qt]   Error(s):
[Qt]     Cannot load library /Applications/Slicer-5.7.0-20240306.app/Contents/Extensions-32750/SlicerRT/lib/Slicer-5.7/qt-loadable-modules/libqSlicerBeamsModule.dylib: (dlopen(/Applications/Slicer-5.7.0-20240306.app/Contents/Extensions-32750/SlicerRT/lib/Slicer-5.7/qt-loadable-modules/libqSlicerBeamsModule.dylib, 0x0085): Library not loaded: @rpath/libomp.dylib
[Qt]   Referenced from: &lt;8CC410E5-7FE3-33F6-BC6E-A68391968FE8&gt; /Applications/Slicer-5.7.0-20240306.app/Contents/Extensions-32750/SlicerRT/lib/Slicer-5.7/qt-loadable-modules/libvtkSlicerBeamsModuleMRML.dylib
[Qt]   Reason: tried: '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../Extensions-32750/QuantitativeReporting/lib/Slicer-5.7/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../Extensions-32750/SlicerDevelopmentToolbox/lib/Slicer-5.7/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../Extensions-32750/IDCBrowser/lib/Slicer-5.7/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../Extensions-32750/DCMQI/lib/Slicer-5.7/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../Extensions-32750/DCMQI/lib/Slicer-5.7/cli-modules/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../Extensions-32750/PETDICOMExtension/lib/Slicer-5.7/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../Extensions-32750/PETDICOMExtension/lib/Slicer-5.7/cli-modules/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../Extensions-32750/SlicerRT/lib/Slicer-5.7/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../Extensions-32750/SlicerRT/lib/Slicer-5.7/cli-modules/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../Extensions-32750/SlicerRT/lib/Slicer-5.7/qt-loadable-modules/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../bin/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../lib/Slicer-5.7/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../lib/Slicer-5.7/cli-modules/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../lib/Slicer-5.7/qt-loadable-modules/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../../lib/Slicer-5.7/qt-loadable-modules/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../lib/Python/lib/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../lib/Python/lib/python3.9/site-packages/numpy/core/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../lib/Python/lib/python3.9/site-packages/numpy/lib/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/../lib/Slicer-5.7/qt-loadable-modules/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Users/svc-dashboard/D/Support/clang+llvm-14.0.6-x86_64-apple-darwin/lib/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/Support/clang+llvm-14.0.6-x86_64-apple-darwin/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/Frameworks/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/Frameworks/QtCore.framework/Versions/5/Frameworks/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/MacOS/../libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/CTK-build/CMakeExternals/Install/lib/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/CTK-build/CMakeExternals/Install/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/usr/local/lib/libomp.dylib' (no such file), '/usr/lib/libomp.dylib' (no such file, not in dyld cache))
</code></pre>

---

## Post #6 by @fedorov (2024-03-06 18:01 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="33504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>The errors at the top of the log point to a <code>libomp.dylib</code>. Is that missing from the package but available in a local build?</p>
</blockquote>
</aside>
<p>Indeed, <code>libomp.dylib</code> is missing from the package. I do not have a mac build.</p>

---

## Post #7 by @fedorov (2024-03-25 19:57 UTC)

<p>I created an issue in SlicerRT: <a href="https://github.com/SlicerRt/SlicerRT/issues/242" class="inline-onebox">SlicerRT Slicer extension is not working on mac · Issue #242 · SlicerRt/SlicerRT · GitHub</a></p>

---

## Post #8 by @Gaelle (2024-12-18 10:39 UTC)

<p>Thank you very much for sharing this information, I couldn’t import the RTStructu on the latest versions (5.6.2 neihter 5.7 for linux)<br>
I succeded in version 5.2.2 :))</p>

---
