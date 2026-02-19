---
topic_id: 11710
title: "Pt Beam Data Not Loading"
date: 2020-05-26
url: https://discourse.slicer.org/t/11710
---

# PT Beam Data not loading

**Topic ID**: 11710
**Date**: 2020-05-26
**URL**: https://discourse.slicer.org/t/pt-beam-data-not-loading/11710

---

## Post #1 by @mdsainth (2020-05-26 14:26 UTC)

<p>I am loading a DICOM dataset from a proton therapy treatment plan from a RaySearch TPS. This inclused the DICOM-CT, DICOM-RTDOSE, DICOM-RTPLAN and DICOM-STRUCT files, However I have problems with the beam data and receive the following error (underneath).<br>
Could it be that this type of plan is not supported?</p>
<p>Regards<br>
Marijke<br>
Warning in DICOM plugin Scalar Volume when examining loadable 1: CBLXxCT1PTV1_1_1: Reference image in series does not contain geometry information. Please use caution.</p>
<p>Loading with imageIOName: GDCM<br>
Window/level found in DICOM tags (center=40.0, width=300.0) has been applied to volume 5: Anonymized<br>
/Slicer-4.10/qt-scripted-modules/SegmentEditorDrawTubeLib/SegmentEditorEffect.py", line 14, in <strong>init</strong><br>
self.logic = DrawTubeLogic(scriptedEffect)<br>
File “C:/Users/mdsainth/AppData/Roaming/NA-MIC/Extensions-28257/SegmentEditorExtraEffects/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorDrawTubeLib/SegmentEditorEffect.py”, line 428, in <strong>init</strong><br>
self.curveGenerator = slicer.vtkCurveGenerator()Loading with imageIOName: GDCM<br>
Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
Loading with imageIOName: DCMTK<br>
Could not read scalar volume using DCMTK approach.  Error is: FileFormatError</p>
<p>Could not load: 1: CBLXxCT1PTV1_1_1 as a Scalar Volume</p>
<p>AttributeError: ‘module’ object has no attribute ‘vtkCurveGenerator’<br>
Traceback (most recent call last):<br>
File “C:/Users/mdsainth/AppData/Roaming/NA-MIC/Extensions-28257/SegmentEditorExtraEffects/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorDrawTube.py”, line 27, in registerEditorEffect<br>
instance.self().register()<br>
AttributeError: ‘NoneType’ object has no attribute ‘register’<br>
reg inside examine<br>
Loading with imageIOName: GDCM<br>
Window/level found in DICOM tags (center=40.0, width=300.0) has been applied to volume 5: Cranio-Spinaal  2.0  B30s<br>
Imported a DICOM directory, checking for extensions<br>
reg inImported a DICOM directory, checking for extensions<br>
reg inside examine<br>
Loading with imageIOName: GDCM<br>
Window/level found in DICOM tags (center=40.0, width=300.0) has been applied to volume 5: Cranio-Spinaal  2.0  B30s_1<br>
side examine</p>

---
