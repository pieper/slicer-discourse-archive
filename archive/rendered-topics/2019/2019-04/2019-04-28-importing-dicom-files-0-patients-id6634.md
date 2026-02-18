# Importing DICOM files- 0 Patients

**Topic ID**: 6634
**Date**: 2019-04-28
**URL**: https://discourse.slicer.org/t/importing-dicom-files-0-patients/6634

---

## Post #1 by @zamanmd (2019-04-28 14:43 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.0<br>
Expected behavior: Succesfully importing 4 dicom files.<br>
Actual behavior: Imported 0 dicom files.</p>
<p>Greetings!</p>
<p>I hope that someone will be able to help me import four dicom files I have so that I can use it in 3d slicer. This is my first time using such software so please bear with me. Everytime I try importing the dicom files, it says 0 files imported. I also tried the dicom patching module but the result is the same. Any help would be appreciated.</p>
<p>Here is the log that I get:</p>
<blockquote>
<p>Blockquote vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open D:/Medicine/Clinical Research/Hopkins/Pediatric Urology/Pelvic Floor Volumes/Data/Data Analysis/3D Reconstructions/patcheddicom/pa000/st000/se000/000.dcm. ITK exception info: error in unknown:  Could not create IO object for reading file D:/Medicine/Clinical Research/Hopkins/Pediatric Urology/Pelvic Floor Volumes/Data/Data Analysis/3D Reconstructions/patcheddicom/pa000/st000/se000/000.dcm<br>
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
set the suffix to an unsupported type.</p>
</blockquote>
<p>Algorithm vtkITKArchetypeImageSeriesScalarReader(00000152EDB2A630) returned failure for request: vtkInformation (00000152F134E830)<br>
Debug: Off<br>
Modified Time: 299126<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1</p>
<p>ReadData: This is not a nrrd file</p>
<p>ReadData: Cannot read file as a volume of type DiffusionTensorVolume[fullName = D:/Medicine/Clinical Research/Hopkins/Pediatric Urology/Pelvic Floor Volumes/Data/Data Analysis/3D Reconstructions/patcheddicom/pa000/st000/se000/000.dcm]<br>
Number of files listed in the node = 0.<br>
File reader says it was able to read 0 files.<br>
File reader used the archetype file name of D:/Medicine/Clinical Research/Hopkins/Pediatric Urology/Pelvic Floor Volumes/Data/Data Analysis/3D Reconstructions/patcheddicom/pa000/st000/se000/000.dcm <span class="chcklst-box fa fa-square-o fa-fw"></span><br>
FileFormatError</p>
<p>ReadData: This is not a nrrd file</p>
<p>ReadData: Failed to instantiate a file reader</p>
<p>ReadData: Cannot read file as a volume of type Volume[fullName = D:/Medicine/Clinical Research/Hopkins/Pediatric Urology/Pelvic Floor Volumes/Data/Data Analysis/3D Reconstructions/patcheddicom/pa000/st000/se000/000.dcm]<br>
Number of files listed in the node = 0.<br>
File reader says it was able to read 0 files.<br>
File reader used the archetype file name of D:/Medicine/Clinical Research/Hopkins/Pediatric Urology/Pelvic Floor Volumes/Data/Data Analysis/3D Reconstructions/patcheddicom/pa000/st000/se000/000.dcm <span class="chcklst-box fa fa-square-o fa-fw"></span><br>
FileFormatError</p>
<blockquote>
<p>Blockquote</p>
</blockquote>

---

## Post #2 by @lassoan (2019-04-28 19:27 UTC)

<p>Are the DICOM files created by a clinical system or by some custom application?</p>
<p>All the files that are already imported are ignored if you attempt to import them again, so if you apply DICOM patcher on them then you need to clean the database before importing again.</p>
<p>After you import, select the series you want to load and click “Load”. If it fails then check the application log for errors. Also check the <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM" rel="nofollow noopener">DICOM FAQ</a>.</p>

---
