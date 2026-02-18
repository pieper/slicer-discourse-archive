# Beam Data in Slicer RT not loading

**Topic ID**: 5718
**Date**: 2019-02-10
**URL**: https://discourse.slicer.org/t/beam-data-in-slicer-rt-not-loading/5718

---

## Post #1 by @samShy (2019-02-10 08:43 UTC)

<p>Hello,</p>
<p>I am currently investigating the possibility of implementing Slicer RT as part of a Clinical protocol for the comparison of Proton and Cyberkinife treatment plans for liver cancer.</p>
<p>Part of the analysis process is to perform robost evaluation, whereby certiain aspect of the beams for the plan are adjusted and the dose is recalculated to simulate  a number of worst case scenarios.</p>
<p>I believe such an analysis should be possible with slicer however when I load the DICOM files the beam data does not appear to be available for manipulation.</p>
<p>I have attached a screen shot of the warnings reported by Slicer when using the advance view of the DICOM load module. Im not exactly sure what the message means and if it could be related to the beam data being unavailable.</p>
<p>any assistance on this issue will be greatly appreciated,</p>
<p>thanks,<br>
Samuel</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c543d6c9fe6adde00c6a6e7052a10139e8bd06e.jpeg" data-download-href="/uploads/short-url/hJRGKIk2vY9jxJoxPxGTY4grXGK.jpeg?dl=1" title="Dicom%20load" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c543d6c9fe6adde00c6a6e7052a10139e8bd06e_2_690x379.jpeg" alt="Dicom%20load" data-base62-sha1="hJRGKIk2vY9jxJoxPxGTY4grXGK" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c543d6c9fe6adde00c6a6e7052a10139e8bd06e_2_690x379.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c543d6c9fe6adde00c6a6e7052a10139e8bd06e_2_1035x568.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c543d6c9fe6adde00c6a6e7052a10139e8bd06e_2_1380x758.jpeg 2x" data-dominant-color="DBE8F0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Dicom%20load</span><span class="informations">1980×1088 203 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7ca70d20ad4aad8d33346f6754689d4263a497f.jpeg" data-download-href="/uploads/short-url/x4w1pXRpafoWLwImrrdSJyZDCyj.jpeg?dl=1" title="Absent%20Beam%20Data" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7ca70d20ad4aad8d33346f6754689d4263a497f_2_347x500.jpeg" alt="Absent%20Beam%20Data" data-base62-sha1="x4w1pXRpafoWLwImrrdSJyZDCyj" width="347" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7ca70d20ad4aad8d33346f6754689d4263a497f_2_347x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7ca70d20ad4aad8d33346f6754689d4263a497f_2_520x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7ca70d20ad4aad8d33346f6754689d4263a497f_2_694x1000.jpeg 2x" data-dominant-color="F6F6F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Absent%20Beam%20Data</span><span class="informations">696×1001 66.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @cpinter (2019-02-10 14:10 UTC)

<p>The first screenshot contains all the loadables offered by <em>all</em> the DICOM plugins, most of which are not selected for loading. If you scroll up, then you’ll see the selected ones checked. Those are the ones that are loaded.</p>
<p>Can you please post a screenshot about the contents of the Subject hierarchy tree in the Data module after loading?<br>
And if you could look at the log (About / Report a problem) after loading and find any errors, those would be interesting to see as well. Thanks.</p>

---

## Post #3 by @cpinter (2019-02-10 14:11 UTC)

<p>Also please note that SlicerRT currently cannot handle MLCs or arcs, only simple square beams. The infrastructure for MLCs is there, but never worked properly so it would need some work.</p>

---

## Post #4 by @samShy (2019-02-10 15:12 UTC)

<p>Thanks for the promt reply</p>
<p>I have attached screen shots of the subject hierarchy and error log.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/993c2fdf29bd71545690dd8d05fda0e59dc16cbe.jpeg" data-download-href="/uploads/short-url/lRA0bDX3SnuowKtH0WNr2oeFqrQ.jpeg?dl=1" title="subject%20hierarchy%201" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/993c2fdf29bd71545690dd8d05fda0e59dc16cbe_2_690x358.jpeg" alt="subject%20hierarchy%201" data-base62-sha1="lRA0bDX3SnuowKtH0WNr2oeFqrQ" width="690" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/993c2fdf29bd71545690dd8d05fda0e59dc16cbe_2_690x358.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/993c2fdf29bd71545690dd8d05fda0e59dc16cbe_2_1035x537.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/993c2fdf29bd71545690dd8d05fda0e59dc16cbe_2_1380x716.jpeg 2x" data-dominant-color="7A837D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">subject%20hierarchy%201</span><span class="informations">1916×995 197 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c9edb37150cd0bbce8af2eba4038826c6060f15.jpeg" data-download-href="/uploads/short-url/6mJm7qUi8NFdpV5drXNMmtUhGn3.jpeg?dl=1" title="subject%20hierarchy%202" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c9edb37150cd0bbce8af2eba4038826c6060f15_2_690x359.jpeg" alt="subject%20hierarchy%202" data-base62-sha1="6mJm7qUi8NFdpV5drXNMmtUhGn3" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c9edb37150cd0bbce8af2eba4038826c6060f15_2_690x359.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c9edb37150cd0bbce8af2eba4038826c6060f15_2_1035x538.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c9edb37150cd0bbce8af2eba4038826c6060f15_2_1380x718.jpeg 2x" data-dominant-color="79827D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">subject%20hierarchy%202</span><span class="informations">1915×997 205 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bef10e131000aa0c1be7df4dfef7e5a6d65f6ceb.jpeg" data-download-href="/uploads/short-url/rf9aZwgB6BKnn93P8oQxHJIx1iP.jpeg?dl=1" title="error%20log%201" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bef10e131000aa0c1be7df4dfef7e5a6d65f6ceb_2_690x291.jpeg" alt="error%20log%201" data-base62-sha1="rf9aZwgB6BKnn93P8oQxHJIx1iP" width="690" height="291" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bef10e131000aa0c1be7df4dfef7e5a6d65f6ceb_2_690x291.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bef10e131000aa0c1be7df4dfef7e5a6d65f6ceb_2_1035x436.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bef10e131000aa0c1be7df4dfef7e5a6d65f6ceb_2_1380x582.jpeg 2x" data-dominant-color="E6E9F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error%20log%201</span><span class="informations">1913×809 240 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba0e9274103697b70c153b1985ab5edf4db71220.jpeg" data-download-href="/uploads/short-url/qxW1RvnkbzmwxqRLdXvP434I0tq.jpeg?dl=1" title="error%20log%202" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba0e9274103697b70c153b1985ab5edf4db71220_2_690x288.jpeg" alt="error%20log%202" data-base62-sha1="qxW1RvnkbzmwxqRLdXvP434I0tq" width="690" height="288" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba0e9274103697b70c153b1985ab5edf4db71220_2_690x288.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba0e9274103697b70c153b1985ab5edf4db71220_2_1035x432.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba0e9274103697b70c153b1985ab5edf4db71220_2_1380x576.jpeg 2x" data-dominant-color="E9ECF5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error%20log%202</span><span class="informations">1920×804 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8582ab50040bfb48dc8bf30b9ea5020f333f7ed.jpeg" data-download-href="/uploads/short-url/o1f6UVVYQIaVsDe6fg6BSWupP1b.jpeg?dl=1" title="error%20log%203" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8582ab50040bfb48dc8bf30b9ea5020f333f7ed_2_690x371.jpeg" alt="error%20log%203" data-base62-sha1="o1f6UVVYQIaVsDe6fg6BSWupP1b" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8582ab50040bfb48dc8bf30b9ea5020f333f7ed_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8582ab50040bfb48dc8bf30b9ea5020f333f7ed_2_1035x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8582ab50040bfb48dc8bf30b9ea5020f333f7ed_2_1380x742.jpeg 2x" data-dominant-color="EDF1F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error%20log%203</span><span class="informations">1920×1035 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I can also send a text of the log file is it helps?</p>
<p>Thanks,</p>

---

## Post #5 by @cpinter (2019-02-10 15:34 UTC)

<p>Thanks for the screenshots. It seems that no plan or beam data is imported whatsoever.</p>
<p>Regarding the log, unfortunately only the info and warning messages are shown and not the errors which would be the interesting part.<br>
Yes please, go to About / Report an error in the menu after loading this dataset, and send us the log, or at least the parts that contain errors. Thanks</p>

---

## Post #6 by @samShy (2019-02-11 07:59 UTC)

<p>Heres the error log information:</p>
<p>[INFO][VTK] 10.02.2019 22:46:10 [vtkMRMLVolumeArchetypeStorageNode (000002680EA70890)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: D:/SLICER/CKLiver_Proton_Study_Plans/DATA SET 1/Data_set_1new/1.2.840.114358.14038002616494.20181216111455.1971345711270_rtdose.dcm. Dimensions: 512x512x197. Number of components: 1. Pixel type: unsigned short.<br>
[ERROR][VTK] 10.02.2019 22:46:10 [vtkSlicerDicomRtImportExportModuleLogic (000002680B12A770)] (D:\D\P\S-0-E-b\SlicerRT\DicomRtImportExport\Logic\vtkSlicerDicomRtImportExportModuleLogic.cxx:553) - LoadRtDose: RTDoseReferencedRTPlanSOPInstanceUID not found for dose volume 0: RTDOSE: Anonymized [0]<br>
[ERROR][VTK] 10.02.2019 22:46:10 [vtkTransformPolyDataFilter (000002680BCB7330)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[ERROR][VTK] 10.02.2019 22:46:10 [vtkTransformPolyDataFilter (0000026816BE1D40)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[ERROR][VTK] 10.02.2019 22:46:11 [vtkTransformPolyDataFilter (0000026816BF2A00)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[ERROR][VTK] 10.02.2019 22:46:11 [vtkTransformPolyDataFilter (0000026816BF2A00)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[ERROR][VTK] 10.02.2019 22:46:11 [vtkTransformPolyDataFilter (0000026816BE3460)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[ERROR][VTK] 10.02.2019 22:46:11 [vtkTransformPolyDataFilter (0000026816BE3460)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data</p>
<p>[INFO][VTK] 10.02.2019 22:46:13 [vtkMRMLVolumeArchetypeStorageNode (000002680EA71B50)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: D:/SLICER/CKLiver_Proton_Study_Plans/DATA SET 1/Data_set_1new/1.2.840.114358.14038002616494.20181216111501.1971495994140_RAW_DOSE_rtdose.dcm. Dimensions: 512x512x197. Number of components: 1. Pixel type: unsigned short.<br>
[ERROR][VTK] 10.02.2019 22:46:13 [vtkSlicerDicomRtImportExportModuleLogic (000002680B12A770)] (D:\D\P\S-0-E-b\SlicerRT\DicomRtImportExport\Logic\vtkSlicerDicomRtImportExportModuleLogic.cxx:553) - LoadRtDose: RTDoseReferencedRTPlanSOPInstanceUID not found for dose volume 0: RTDOSE: Anonymized [0]_1<br>
[INFO][Stream] 10.02.2019 22:46:13 [] (unknown:0) - Loading series ‘63: RTDOSE: RT Dose: GTV50 plan’ from file ‘D:/SLICER/CKLiver_Proton_Study_Plans/DATA SET 1/GTV50 plan-anon/rtdose.dcm’<br>
[CRITICAL][Stream] 10.02.2019 22:46:13 [] (unknown:0) - W: OperatorsName (0008,1070) absent in RTSeriesModule (type 2)<br>
[INFO][VTK] 10.02.2019 22:46:14 [vtkMRMLVolumeArchetypeStorageNode (000002680EA706B0)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: D:/SLICER/CKLiver_Proton_Study_Plans/DATA SET 1/GTV50 plan-anon/rtdose.dcm. Dimensions: 256x256x197. Number of components: 1. Pixel type: unsigned int.<br>
[ERROR][VTK] 10.02.2019 22:46:14 [vtkTransformPolyDataFilter (0000026816BF2A00)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[ERROR][VTK] 10.02.2019 22:46:14 [vtkTransformPolyDataFilter (0000026816BF2A00)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[ERROR][VTK] 10.02.2019 22:46:14 [vtkTransformPolyDataFilter (0000026816BE3460)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[ERROR][VTK] 10.02.2019 22:46:14 [vtkTransformPolyDataFilter (0000026816BE3460)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[INFO][Python] 10.02.2019 22:46:14 [Python] (C:/Program Files/Slicer 4.11.0-2019-02-01/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: GDCM<br>
[ERROR][Python] 10.02.2019 22:46:14 [Python] (C:/Program Files/Slicer 4.11.0-2019-02-01/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[INFO][Python] 10.02.2019 22:46:14 [Python] (C:/Program Files/Slicer 4.11.0-2019-02-01/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: DCMTK<br>
[ERROR][Python] 10.02.2019 22:46:14 [Python] (C:/Program Files/Slicer 4.11.0-2019-02-01/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[INFO][Stream] 10.02.2019 22:46:14 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[ERROR][VTK] 10.02.2019 22:46:14 [vtkITKArchetypeImageSeriesScalarReader (000002680E9506C0)] (D:\D\P\Slicer-0\Libs\vtkITK\vtkITKArchetypeImageSeriesReader.cxx:408) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open D:/SLICER/CKLiver_Proton_Study_Plans/DATA SET 1/GTV50 plan-anon/rtplan.dcm. ITK exception info: error in unknown:  Could not create IO object for reading file D:/SLICER/CKLiver_Proton_Study_Plans/DATA SET 1/GTV50 plan-anon/rtplan.dcm<br>
Tried to create one of the following:<br>
BMPImageIO<br>
BioRadImageIO<br>
DCMTKImageIO<br>
GDCMImageIO<br>
GiplImageIO<br>
JPEGImageIO<br>
LSMImageIO<br>
MGHImageIO<br>
MINCImageIO<br>
MRCImageIO<br>
MetaImageIO<br>
NiftiImageIO<br>
NrrdImageIO<br>
PNGImageIO<br>
StimulateImageIO<br>
TIFFImageIO<br>
VTKImageIO<br>
MRMLIDImageIO<br>
Bruker2dseqImageIO<br>
GE4ImageIO<br>
GE5ImageIO<br>
HDF5ImageIO<br>
You probably failed to set a file suffix, or<br>
set the suffix to an unsupported type.<br>
[ERROR][VTK] 10.02.2019 22:46:14 [vtkCompositeDataPipeline (00000268186DCE60)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkExecutive.cxx:782) - Algorithm vtkITKArchetypeImageSeriesScalarReader(000002680E9506C0) returned failure for request: vtkInformation (0000026817780490)<br>
Debug: Off<br>
Modified Time: 4184765<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
[CRITICAL][Stream] 10.02.2019 22:46:14 [] (unknown:0) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[INFO][Stream] 10.02.2019 22:46:14 [] (unknown:0) - Loading with imageIOName: DCMTK<br>
[ERROR][VTK] 10.02.2019 22:46:14 [vtkITKArchetypeImageSeriesScalarReader (000002680A8D25D0)] (D:\D\P\Slicer-0\Libs\vtkITK\vtkITKArchetypeImageSeriesReader.cxx:408) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open D:/SLICER/CKLiver_Proton_Study_Plans/DATA SET 1/GTV50 plan-anon/rtplan.dcm. ITK exception info: error in unknown:  Could not create IO object for reading file D:/SLICER/CKLiver_Proton_Study_Plans/DATA SET 1/GTV50 plan-anon/rtplan.dcm<br>
Tried to create one of the following:<br>
BMPImageIO<br>
BioRadImageIO<br>
DCMTKImageIO<br>
GDCMImageIO<br>
GiplImageIO<br>
JPEGImageIO<br>
LSMImageIO<br>
MGHImageIO<br>
MINCImageIO<br>
MRCImageIO<br>
MetaImageIO<br>
NiftiImageIO<br>
NrrdImageIO<br>
PNGImageIO<br>
StimulateImageIO<br>
TIFFImageIO<br>
VTKImageIO<br>
MRMLIDImageIO<br>
Bruker2dseqImageIO<br>
GE4ImageIO<br>
GE5ImageIO<br>
HDF5ImageIO<br>
You probably failed to set a file suffix, or<br>
set the suffix to an unsupported type.<br>
[ERROR][VTK] 10.02.2019 22:46:14 [vtkCompositeDataPipeline (00000268186DCC80)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkExecutive.cxx:782) - Algorithm vtkITKArchetypeImageSeriesScalarReader(000002680A8D25D0) returned failure for request: vtkInformation (0000026817782150)<br>
Debug: Off<br>
Modified Time: 4184848<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
[CRITICAL][Stream] 10.02.2019 22:46:14 [] (unknown:0) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[INFO][Stream] 10.02.2019 22:46:14 [] (unknown:0) - Loading series ‘26: RTDOSE: RT Dose’ from file ‘D:/SLICER/CKLiver_Proton_Study_Plans/DATA SET 1/ITV Plan-anon/rtdose.dcm’<br>
[INFO][VTK] 10.02.2019 22:46:15 [vtkMRMLVolumeArchetypeStorageNode (000002680EA71970)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: D:/SLICER/CKLiver_Proton_Study_Plans/DATA SET 1/ITV Plan-anon/rtdose.dcm. Dimensions: 256x256x197. Number of components: 1. Pixel type: unsigned int.<br>
[INFO][Python] 10.02.2019 22:46:15 [Python] (C:/Program Files/Slicer 4.11.0-2019-02-01/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: GDCM<br>
[INFO][Python] 10.02.2019 22:46:17 [Python] (C:/Program Files/Slicer 4.11.0-2019-02-01/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:375) - Window/level found in DICOM tags (center=40.0, width=400.0) has been applied to volume 2: Anonymized<br>
[WARNING][Python] 10.02.2019 22:46:18 [Python] (C:/Program Files/Slicer 4.11.0-2019-02-01/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:701) - Irregular volume geometry detected, but maximum error non-zero but is within tolerance (maximum error of 1.78223e-05 mm, tolerance threshold is 0.001 mm).<br>
[WARNING][Python] 10.02.2019 22:46:18 [Python] (C:\Program Files\Slicer 4.11.0-2019-02-01\bin\Python\slicer\util.py:1110) -<br>
Could not load: 1: Unnamed Series as a Scalar Volume<br>
[INFO][Stream] 10.02.2019 22:46:15 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[ERROR][VTK] 10.02.2019 22:46:17 [vtkCompositeDataPipeline (0000026813062C40)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:709) - Input port 0 of algorithm vtkCleanPolyData(0000026839675450) has 0 connections but is not optional.<br>
[ERROR][VTK] 10.02.2019 22:46:17 [vtkCompositeDataPipeline (00000268151E4B90)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:709) - Input port 0 of algorithm vtkCleanPolyData(00000268130ED500) has 0 connections but is not optional.<br>
[ERROR][VTK] 10.02.2019 22:46:17 [vtkTransformPolyDataFilter (0000026816BF2A00)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[ERROR][VTK] 10.02.2019 22:46:17 [vtkCompositeDataPipeline (00000268151E4B90)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:709) - Input port 0 of algorithm vtkCleanPolyData(00000268130ED500) has 0 connections but is not optional.<br>
[ERROR][VTK] 10.02.2019 22:46:17 [vtkTransformPolyDataFilter (0000026816BF2A00)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[ERROR][VTK] 10.02.2019 22:46:17 [vtkCompositeDataPipeline (00000268151E4B90)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:709) - Input port 0 of algorithm vtkCleanPolyData(00000268130ED500) has 0 connections but is not optional.<br>
[ERROR][VTK] 10.02.2019 22:46:17 [vtkTransformPolyDataFilter (0000026816BE3460)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[ERROR][VTK] 10.02.2019 22:46:17 [vtkTransformPolyDataFilter (0000026816BE3460)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[INFO][Stream] 10.02.2019 22:46:17 [] (unknown:0) - Window/level found in DICOM tags (center=40.0, width=400.0) has been applied to volume 2: Anonymized<br>
[CRITICAL][Stream] 10.02.2019 22:46:18 [] (unknown:0) - Irregular volume geometry detected, but maximum error non-zero but is within tolerance (maximum error of 1.78223e-05 mm, tolerance threshold is 0.001 mm).<br>
[CRITICAL][Stream] 10.02.2019 22:46:18 [] (unknown:0) -<br>
[CRITICAL][Stream] 10.02.2019 22:46:18 [] (unknown:0) - Could not load: 1: Unnamed Series as a Scalar Volume<br>
[DEBUG][Qt] 10.02.2019 22:46:41 [] (unknown:0) - Switch to module:  “Data”<br>
[ERROR][VTK] 10.02.2019 22:46:58 [vtkTransformPolyDataFilter (0000026816BE3460)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[ERROR][VTK] 10.02.2019 22:46:58 [vtkTransformPolyDataFilter (0000026816BE3460)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[ERROR][VTK] 10.02.2019 22:46:59 [vtkTransformPolyDataFilter (0000026816BF2A00)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[ERROR][VTK] 10.02.2019 22:46:59 [vtkTransformPolyDataFilter (0000026816BF2A00)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[ERROR][VTK] 10.02.2019 22:46:59 [vtkTransformPolyDataFilter (0000026816BE3460)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[ERROR][VTK] 10.02.2019 22:46:59 [vtkTransformPolyDataFilter (0000026816BE3460)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[ERROR][VTK] 10.02.2019 23:00:09 [vtkCompositeDataPipeline (0000026813062C40)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:709) - Input port 0 of algorithm vtkCleanPolyData(0000026839675450) has 0 connections but is not optional.<br>
[ERROR][VTK] 10.02.2019 23:00:09 [vtkCompositeDataPipeline (00000268151E4B90)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:709) - Input port 0 of algorithm vtkCleanPolyData(00000268130ED500) has 0 connections but is not optional.<br>
[ERROR][VTK] 10.02.2019 23:00:09 [vtkCompositeDataPipeline (0000026813062C40)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:709) - Input port 0 of algorithm vtkCleanPolyData(0000026839675450) has 0 connections but is not optional.<br>
[ERROR][VTK] 10.02.2019 23:00:09 [vtkCompositeDataPipeline (00000268151E4B90)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:709) - Input port 0 of algorithm vtkCleanPolyData(00000268130ED500) has 0 connections but is not optional.</p>

---

## Post #7 by @cpinter (2019-02-11 15:12 UTC)

<p>Thanks for the log! It does not say anything about failed beam data loading. Is it possible for you to share an anonymized dataset which you have this problem with? Then I’ll try to reproduce the issue.</p>

---

## Post #8 by @samShy (2019-02-12 03:53 UTC)

<p>I am happy to share the anonymized dataset,<br>
However could you please inform me as to the best means to share the data.</p>
<p>Cheers,<br>
Sam</p>

---

## Post #9 by @cpinter (2019-02-12 19:23 UTC)

<p>Whatever you normally prefer. Many times we use Dropbox/OneDrive/GDrive, but for some people a server hosted by their institution is easier. The data is for testing and bugfixing purposes only, so temporary storage is completely fine. Thanks!</p>

---

## Post #10 by @samShy (2019-02-15 02:55 UTC)

<p>here is the link to the Gdrive folder<br>
<a href="https://drive.google.com/drive/folders/1jnvyMppJfDm3IyCoI689rTTdx_H5pDiF?usp=sharing" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/drive/folders/1jnvyMppJfDm3IyCoI689rTTdx_H5pDiF?usp=sharing</a></p>

---

## Post #11 by @cpinter (2019-02-15 14:55 UTC)

<p>I got it, thank you. I just need some time ot get there. Please standby</p>

---

## Post #12 by @cpinter (2019-02-15 15:30 UTC)

<p>I did some digging and it turns out that my hunch was right: the type of plan simply isn’t supported yet, see<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx#L1689" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx#L1689" target="_blank" rel="nofollow noopener">SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx#L1689</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="1679" style="counter-reset: li-counter 1678 ;">
<li>{
</li>
<li>  this-&gt;Internal-&gt;ExamineRtStructureSetDataset(dataset, name, referencedSOPInstanceUIDs);
</li>
<li>}
</li>
<li>// RTImage
</li>
<li>else if (sopClass == UID_RTImageStorage)
</li>
<li>{
</li>
<li>  this-&gt;Internal-&gt;ExamineRtImageDataset(dataset, name, referencedSOPInstanceUIDs);
</li>
<li>}
</li>
<li>/* Not yet supported
</li>
<li>else if (sopClass == UID_RTTreatmentSummaryRecordStorage)
</li>
<li class="selected">else if (sopClass == UID_RTIonPlanStorage)
</li>
<li>else if (sopClass == UID_RTIonBeamsTreatmentRecordStorage)
</li>
<li>*/
</li>
<li>else
</li>
<li>{
</li>
<li>  continue; // Not an RT file
</li>
<li>}
</li>
<li>
</li>
<li>// The file is a loadable RT object, create and set up loadable
</li>
<li>vtkSmartPointer&lt;vtkSlicerDICOMLoadable&gt; loadable = vtkSmartPointer&lt;vtkSlicerDICOMLoadable&gt;::New();
</li>
<li>loadable-&gt;SetName(name.c_str());
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
(the plan in your dataset has the SOP class UID of ion plans).</p>
<p>If you have some time, adding it shouldn’t be too hard I think. Just follow the existing example (RTPlanStorage) and the corresponding section of the DICOM standard. <a class="mention" href="/u/gcsharp">@gcsharp</a> what do you think?<br>
If you decide to go for it, I’m happy to help!</p>

---

## Post #13 by @gcsharp (2019-02-15 19:10 UTC)

<p>RT Ion Plan shares some overlap with RT Plan, yes, I think it should not be too difficult.</p>

---

## Post #14 by @samShy (2019-02-16 10:39 UTC)

<p>Thanks for diagnosing the problem,</p>
<p>I would love to have a go at adding it, but i think will need a lot of help. My programing experience has been mainly limited to Matlab, but currently recieving training on Python programing . So any assistance will be much appreciated.</p>

---

## Post #15 by @cpinter (2019-02-16 14:44 UTC)

<p>Excellent! I think you can help a lot in the DICOM side of things.</p>
<p>I’ll create a branch on GitHub for this and add placeholders where the proton/ion part needs to go so that you just need to fill in some gaps in the code. I’ll also point to examples you can copy-paste-modify to get the ion part working.</p>
<p>Please follow <a href="https://github.com/SlicerRt/SlicerRT/issues/25" rel="nofollow noopener">this GitHub issue</a>. I’ll describe the steps there. Thanks a lot in advance!</p>

---

## Post #16 by @cpinter (2019-12-04 13:50 UTC)

<p>2 posts were split to a new topic: <a href="/t/hdr-brachytherapy-plan-loading/9383">HDR brachytherapy plan loading</a></p>

---
