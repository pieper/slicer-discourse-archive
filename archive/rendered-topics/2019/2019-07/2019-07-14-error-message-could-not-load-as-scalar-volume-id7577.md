---
topic_id: 7577
title: "Error Message Could Not Load As Scalar Volume"
date: 2019-07-14
url: https://discourse.slicer.org/t/7577
---

# Error message: Could not load as Scalar Volume

**Topic ID**: 7577
**Date**: 2019-07-14
**URL**: https://discourse.slicer.org/t/error-message-could-not-load-as-scalar-volume/7577

---

## Post #1 by @J_C (2019-07-14 21:23 UTC)

<p>Hi,<br>
Recently I started using Slicer (4.10.2) to extract some radiomics features from MRI images using the radiomics module, but every time I try to import some DICOMs through the DICOM manager, I get a lot of warnings; then if I load the exam, a list of “could not load as scalar volume” comes out. I already tried DICOM patcher and nothing changed. I tried GDCM, DCMTK and Archetype. Files aren’t anonymized, since I read it was another possible issue. I know that another things is that they could be corrupted, but if that’s the case, that would mean that every exported exam is the same.</p>
<p>Am I getting something wrong?</p>

---

## Post #2 by @lassoan (2019-07-14 21:59 UTC)

<p>Could you copy-paste here your application log (menu: Help / Report a bug) and/or share an anonymized series?</p>

---

## Post #3 by @J_C (2019-07-21 11:11 UTC)

<p>Hi, since I’m actually travelling back and forth for my work, I cannot always access to all my data, that’s the reason I was this late in answering.<br>
The error data log is the following, and it seems it repeats a lot, this is only part of it since the whole thing is exceeding the word limit of the post.</p>
<p>[ERROR][Python] 21.07.2019 12:52:39 [Python] (G:/3d Slicer/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[INFO][Stream] 21.07.2019 12:52:38 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[ERROR][VTK] 21.07.2019 12:52:39 [vtkITKArchetypeImageSeriesScalarReader (0000000010174DC0)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKArchetypeImageSeriesReader.cxx:408) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open G:/1 Pre-PT/Avila 29-10-2018/DICOMOBJ/00000406. ITK exception info: error in unknown:  Could not create IO object for reading file G:/1 Pre-PT/Avila 29-10-2018/DICOMOBJ/00000406<br>
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
You probably failed to set a file suffix, or<br>
set the suffix to an unsupported type.<br>
[ERROR][VTK] 21.07.2019 12:52:39 [vtkCompositeDataPipeline (000000001674DF90)] (D:\D\S\Slicer-4102-build\VTK\Common\ExecutionModel\vtkExecutive.cxx:782) - Algorithm vtkITKArchetypeImageSeriesScalarReader(0000000010174DC0) returned failure for request: vtkInformation (0000000015D7A750)<br>
Debug: Off<br>
Modified Time: 338830<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
[CRITICAL][Stream] 21.07.2019 12:52:39 [] (unknown:0) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[INFO][Stream] 21.07.2019 12:52:39 [] (unknown:0) - Loading with imageIOName: DCMTK<br>
[ERROR][VTK] 21.07.2019 12:52:39 [vtkITKArchetypeImageSeriesScalarReader (0000000010175170)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKArchetypeImageSeriesReader.cxx:408) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open G:/1 Pre-PT/Avila 29-10-2018/DICOMOBJ/00000406. ITK exception info: error in unknown:  Could not create IO object for reading file G:/1 Pre-PT/Avila 29-10-2018/DICOMOBJ/00000406<br>
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
You probably failed to set a file suffix, or<br>
set the suffix to an unsupported type.<br>
[ERROR][VTK] 21.07.2019 12:52:39 [vtkCompositeDataPipeline (0000000016749DF0)] (D:\D\S\Slicer-4102-build\VTK\Common\ExecutionModel\vtkExecutive.cxx:782) - Algorithm vtkITKArchetypeImageSeriesScalarReader(0000000010175170) returned failure for request: vtkInformation (0000000015D7DD60)<br>
Debug: Off<br>
Modified Time: 338913<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
[CRITICAL][Stream] 21.07.2019 12:52:39 [] (unknown:0) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[INFO][Python] 21.07.2019 12:52:39 [Python] (G:/3d Slicer/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: GDCM<br>
[ERROR][Python] 21.07.2019 12:52:39 [Python] (G:/3d Slicer/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[INFO][Python] 21.07.2019 12:52:39 [Python] (G:/3d Slicer/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: DCMTK<br>
[ERROR][Python] 21.07.2019 12:52:40 [Python] (G:/3d Slicer/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[INFO][Stream] 21.07.2019 12:52:39 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[ERROR][VTK] 21.07.2019 12:52:39 [vtkITKArchetypeImageSeriesScalarReader (0000000010174DC0): vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open G:/1 Pre-PT/Avila 29-10-2018/DICOMOBJ/000000D7. ITK exception info: error in unknown: itk::ERROR: GDCMImageIO(00000000107B4A60)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKArchetypeImageSeriesReader.cxx:408) - Cannot read requested file<br>
[ERROR][VTK] 21.07.2019 12:52:39 [vtkCompositeDataPipeline (0000000016750510)] (D:\D\S\Slicer-4102-build\VTK\Common\ExecutionModel\vtkExecutive.cxx:782) - Algorithm vtkITKArchetypeImageSeriesScalarReader(0000000010174DC0) returned failure for request: vtkInformation (0000000015D7E850)<br>
Debug: Off<br>
Modified Time: 340155<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
[CRITICAL][Stream] 21.07.2019 12:52:39 [] (unknown:0) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[INFO][Stream] 21.07.2019 12:52:39 [] (unknown:0) - Loading with imageIOName: DCMTK<br>
[ERROR][VTK] 21.07.2019 12:52:40 [vtkITKArchetypeImageSeriesScalarReader (0000000010175170): vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open G:/1 Pre-PT/Avila 29-10-2018/DICOMOBJ/000000D7. ITK exception info: error in unknown: itk::ERROR: GDCMImageIO(00000000107B4610)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKArchetypeImageSeriesReader.cxx:408) - Cannot read requested file<br>
[ERROR][VTK] 21.07.2019 12:52:40 [vtkCompositeDataPipeline (00000000167536C0)] (D:\D\S\Slicer-4102-build\VTK\Common\ExecutionModel\vtkExecutive.cxx:782) - Algorithm vtkITKArchetypeImageSeriesScalarReader(0000000010175170) returned failure for request: vtkInformation (0000000015D7D720)<br>
Debug: Off<br>
Modified Time: 340249<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
[CRITICAL][Stream] 21.07.2019 12:52:40 [] (unknown:0) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[INFO][Python] 21.07.2019 12:52:40 [Python] (G:/3d Slicer/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: GDCM<br>
[ERROR][Python] 21.07.2019 12:52:40 [Python] (G:/3d Slicer/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[INFO][Python] 21.07.2019 12:52:40 [Python] (G:/3d Slicer/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: DCMTK<br>
[ERROR][Python] 21.07.2019 12:52:40 [Python] (G:/3d Slicer/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[INFO][Stream] 21.07.2019 12:52:40 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[ERROR][VTK] 21.07.2019 12:52:40 [vtkITKArchetypeImageSeriesScalarReader (0000000010174DC0): vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open G:/1 Pre-PT/Avila 29-10-2018/DICOMOBJ/00000282. ITK exception info: error in unknown: itk::ERROR: GDCMImageIO(00000000107B4A60)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKArchetypeImageSeriesReader.cxx:408) - Cannot read requested file<br>
[ERROR][VTK] 21.07.2019 12:52:40 [vtkCompositeDataPipeline (00000000167538A0)] (D:\D\S\Slicer-4102-build\VTK\Common\ExecutionModel\vtkExecutive.cxx:782) - Algorithm vtkITKArchetypeImageSeriesScalarReader(0000000010174DC0) returned failure for request: vtkInformation (0000000015D7F020)<br>
Debug: Off<br>
Modified Time: 340342<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
[CRITICAL][Stream] 21.07.2019 12:52:40 [] (unknown:0) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[INFO][Stream] 21.07.2019 12:52:40 [] (unknown:0) - Loading with imageIOName: DCMTK<br>
[ERROR][VTK] 21.07.2019 12:52:40 [vtkITKArchetypeImageSeriesScalarReader (0000000010175170): vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open G:/1 Pre-PT/Avila 29-10-2018/DICOMOBJ/00000282. ITK exception info: error in unknown: itk::ERROR: GDCMImageIO(00000000107B4610)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKArchetypeImageSeriesReader.cxx:408) - Cannot read requested file<br>
[ERROR][VTK] 21.07.2019 12:52:40 [vtkCompositeDataPipeline (0000000016753A80)] (D:\D\S\Slicer-4102-build\VTK\Common\ExecutionModel\vtkExecutive.cxx:782) - Algorithm vtkITKArchetypeImageSeriesScalarReader(0000000010175170) returned failure for request: vtkInformation (0000000015D7D6D0)<br>
Debug: Off<br>
Modified Time: 340436<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
[CRITICAL][Stream] 21.07.2019 12:52:40 [] (unknown:0) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[INFO][Python] 21.07.2019 12:52:40 [Python] (G:/3d Slicer/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: GDCM<br>
[ERROR][Python] 21.07.2019 12:52:41 [Python] (G:/3d Slicer/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[INFO][Python] 21.07.2019 12:52:41 [Python] (G:/3d Slicer/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: DCMTK<br>
[ERROR][Python] 21.07.2019 12:52:41 [Python] (G:/3d Slicer/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[INFO][Stream] 21.07.2019 12:52:40 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[ERROR][VTK] 21.07.2019 12:52:41 [vtkITKArchetypeImageSeriesScalarReader (0000000010174DC0)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKArchetypeImageSeriesReader.cxx:408) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open G:/1 Pre-PT/Avila 29-10-2018/DICOMOBJ/00000408. ITK exception info: error in unknown:  Could not create IO object for reading file G:/1 Pre-PT/Avila 29-10-2018/DICOMOBJ/00000408</p>

---

## Post #4 by @cpinter (2019-07-21 19:34 UTC)

<p>This may be very trivial but could you try using a directory that does not have a space in the path? I see that there are a few like “1 Pre-PT” and “Avila 29-10-2018”, and space may be a problem, similarly to how special characters are a problem.</p>

---

## Post #5 by @J_C (2019-07-22 21:58 UTC)

<p>Thank you for the suggestion, but it doesn’t seems to work. I noticed (opening up the DICOMs in another reader) that some mri sequences folders (for example T2) are empty, but there other folders named differently which contains the data. If I look at advanced settings in Dicom importer in slicer, I can select these series (that are unselected by default) and this seems to solve the problem in some cases.</p>

---
