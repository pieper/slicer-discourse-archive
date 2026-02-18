# Convert RT structure to Nrrd

**Topic ID**: 16241
**Date**: 2021-02-26
**URL**: https://discourse.slicer.org/t/convert-rt-structure-to-nrrd/16241

---

## Post #1 by @xlucox (2021-02-26 15:02 UTC)

<p>Hi everyone,</p>
<p>I’m trying to convert the RT structure to nrrd using the script BatchStructureSetConversion.py from the SlicerRT module. I executed the script from terminal in this way:<br>
/path/to/Slicer/Slicer-4.11.0-2020-08-29-linux-amd64/Slicer --no-main-window --python-script /path/to/thescript/BatchStructureSetConversion.py -i /path/to/RTStructure/ -r /path/to/theDicom -o outputpath</p>
<p>The script freezes when it is creating the labelmaps. The output I get is:<br>
libpng warning: iCCP: known incorrect sRGB profile<br>
qSlicerSequencesModulePrivate::addToolBar: no main window is available, toolbar is not added<br>
This plugin dir: /home/luciano/.config/NA-MIC/Extensions-29335/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules<br>
Loading Slicer RC file [/home/luciano/.slicerrc.py]<br>
Import reference anatomy DICOM data from /mnt/Luco/Documents/AIQ/HandN/borrar/CT<br>
Switching to temporary DICOM database: /mnt/Luco/Programs/Slicer/TemporaryDirecotory/20210226_144833_TempDICOMDatabase<br>
TagCacheDatabase adding table</p>
<p>“DICOM indexer has successfully inserted 91 files [0.06s]”<br>
“DICOM indexer has successfully processed 91 files [0.10s]”<br>
“DICOM indexer has updated display fields for 91 files [0.02s]”<br>
Loading with imageIOName: GDCM<br>
Window/level found in DICOM tags (center=40.0, width=400.0) has been applied to volume 2: CT IMAGES<br>
Import DICOM data from /mnt/Luco/Documents/AIQ/HandN/borrar/RTStructure-CT/<br>
Switching to temporary DICOM database: /mnt/Luco/Programs/Slicer/TemporaryDirecotory/20210226_144836_TempDICOMDatabase<br>
TagCacheDatabase adding table</p>
<p>“DICOM indexer has successfully inserted 1 files [0.00s]”<br>
“DICOM indexer has successfully processed 1 files [0.01s]”<br>
“DICOM indexer has updated display fields for 1 files [0.00s]”<br>
Load first patient into Slicer<br>
Please install SlicerRT extension to enable loading of DICOM RT Structure Set objects<br>
Please install SlicerRT extension to enable loading of DICOM RT Structure Set objects<br>
W: OperatorsName (0008,1070) absent in RTSeriesModule (type 2)<br>
W: PositionReferenceIndicator (0020,1040) absent in FrameOfReferenceModule (type 2)<br>
W: OperatorsName (0008,1070) absent in RTSeriesModule (type 2)<br>
W: PositionReferenceIndicator (0020,1040) absent in FrameOfReferenceModule (type 2)<br>
Warning: In /work/Preview/S-0-E-b/SlicerRT/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.cxx, line 1244<br>
vtkPlanarContourToClosedSurfaceConversionRule (0x6f44a00): GetSpacingBetweenLines: Contour spacing is not consistent.</p>
<p>Warning: In /work/Preview/S-0-E-b/SlicerRT/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.cxx, line 1244<br>
vtkPlanarContourToClosedSurfaceConversionRule (0x6f44a00): GetSpacingBetweenLines: Contour spacing is not consistent.</p>
<p>Convert loaded structure set to labelmap volumes<br>
Converting structure set 1: RTSTRUCT: RTstruct</p>
<p>It freezes there, and nothing happen. I could load this RT structure within Slicer, so I assume I’m doing something wrong.</p>
<p>Does anyone could help me with this?<br>
I could create the nrrd for some samples but I can’t in others.</p>
<p>Thanks!!!</p>

---
