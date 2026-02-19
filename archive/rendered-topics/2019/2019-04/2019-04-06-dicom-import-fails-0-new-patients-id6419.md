---
topic_id: 6419
title: "Dicom Import Fails 0 New Patients"
date: 2019-04-06
url: https://discourse.slicer.org/t/6419
---

# DICOM import fails - 0 New Patients

**Topic ID**: 6419
**Date**: 2019-04-06
**URL**: https://discourse.slicer.org/t/dicom-import-fails-0-new-patients/6419

---

## Post #1 by @LizzyMedinaGtz (2019-04-06 03:32 UTC)

<p>Problem report for Slicer 4.10.1 macosx-amd64: [please describe expected and actual behavior]<br>
When I try to import to DICOM but it says that I have 0 New Patients, 0 New Studies<br>
This are my latest log messages</p>
<details>
<summary>
Application log</summary>
<pre><code>[DEBUG][Qt] 05.04.2019 18:37:28 [] (unknown:0) - Session start time .......: 2019-04-05 18:37:28
[DEBUG][Qt] 05.04.2019 18:37:28 [] (unknown:0) - Slicer version ...........: 4.10.1 (revision 27931) macosx-amd64 - installed release
[DEBUG][Qt] 05.04.2019 18:37:28 [] (unknown:0) - Operating system .........: Mac OS X / 10.12.6 / 16G29 - 64-bit
[DEBUG][Qt] 05.04.2019 18:37:28 [] (unknown:0) - Memory ...................: 8192 MB physical, 1024 MB virtual
[DEBUG][Qt] 05.04.2019 18:37:28 [] (unknown:0) - CPU ......................: GenuineIntel Intel(R) Core(TM) i5-4590 CPU @ 3.30GHz, 4 cores, 4 logical processors
[DEBUG][Qt] 05.04.2019 18:37:28 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, Sequential threading
[DEBUG][Qt] 05.04.2019 18:37:28 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 05.04.2019 18:37:28 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 05.04.2019 18:37:28 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 05.04.2019 18:37:35 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 05.04.2019 18:37:37 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 05.04.2019 18:37:37 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 05.04.2019 18:37:38 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 05.04.2019 18:43:39 [] (unknown:0) - Switch to module:  "DICOM"
[DEBUG][Qt] 05.04.2019 18:45:06 [] (unknown:0) - TagCacheDatabase adding table
[WARNING][Qt] 05.04.2019 18:45:06 [] (unknown:0) - QSqlDatabasePrivate::removeDatabase: connection 'SLICER' is still in use, all queries will cease to work.
[WARNING][Qt] 05.04.2019 18:45:06 [] (unknown:0) - QSqlDatabasePrivate::addDatabase: duplicate connection name 'SLICER', old connection removed.
[DEBUG][Qt] 05.04.2019 18:45:53 [] (unknown:0) - TagCacheDatabase adding table
[WARNING][Qt] 05.04.2019 18:45:53 [] (unknown:0) - QSqlDatabasePrivate::removeDatabase: connection 'SLICER' is still in use, all queries will cease to work.
[WARNING][Qt] 05.04.2019 18:45:53 [] (unknown:0) - QSqlDatabasePrivate::addDatabase: duplicate connection name 'SLICER', old connection removed.
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/.DS_Store" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/.DS_Store
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/DICOMDIR" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/DICOMDIR
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1000000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1000000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1000001" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1000001
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1000002" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1000002
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1010000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1010000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1020000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1020000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1030000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1030000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1040000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1040000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1050000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1050000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1060000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1060000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1070000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1070000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1080000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1080000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1090000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1090000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1100000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1100000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1100001" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1100001
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1110000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1110000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1120000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1120000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1130000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1130000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1140000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1140000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1150000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1150000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1160000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1160000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1170000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1170000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1180000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1180000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1190000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1190000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1200000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1200000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1200001" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1200001
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1210000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1210000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1220000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1220000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1230000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1230000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1240000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1240000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1250000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1250000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1260000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1260000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1270000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1270000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1280000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1280000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1290000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1290000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1300000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1300000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1300001" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1300001
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1310000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1310000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1320000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1320000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1330000" 
DCMTK says:  No such file or directory
[WARNING][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not read DICOM file:/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1330000
[DEBUG][Qt] 05.04.2019 18:46:10 [] (unknown:0) - Could not load  "/Users/medinnovationjc/Desktop/Anomalías cardiacas/Coartación de la aorta/TAC coartación/COARTACION/GHW4EJ0M/4JJ0WMJ0/I1340000" 
DCMTK says:  No such file or directory
</code></pre>
</details>

---

## Post #2 by @VincentYu (2019-04-06 12:36 UTC)

<aside class="quote no-group" data-username="LizzyMedinaGtz" data-post="1" data-topic="6419">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lizzymedinagtz/48/3398_2.png" class="avatar"> LizzyMedinaGtz:</div>
<blockquote>
<p>0 New Patients, 0 New Studies</p>
</blockquote>
</aside>
<p>I always receive this message if the path of DICOM includes any Chinese character. You may rename the folders using only English characters (ASCII code) and load the DICOM again.</p>

---

## Post #3 by @cpinter (2019-04-06 13:48 UTC)

<p>I agree, it’s probably the character ‘ó’ in the path. Unfortunately this is a limitation that is very hard to get rid of, see</p>
<aside class="quote quote-modified" data-post="10" data-topic="204">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/why-i-can-not-import-dicom/204/10">Why I can not import DICOM?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    This log message describes the problem and suggested solution: 

Please set an empty folder for DICOM database that you have write access to, try DICOM import again, and let us know if it fixed the DICOM importing.
  </blockquote>
</aside>
<aside class="quote" data-post="2" data-topic="5223">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/problem-with-loading-files/5223/2">Problem with loading files</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    See the <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#I_try_to_import_a_directory_of_DICOM_files.2C_but_nothing_shows_up_in_the_browser" rel="nofollow noopener">DICOM FAQ</a>: 

Try moving the data and the database directory to a path that includes only US English characters (ASCII) to avoid possible parsing errors. No special, international characters are allowed. 

You’ve tried to load the data set from the folder name C:/Users/P???czek typu gniazdko/Desktop/… folder, which contained a special character. Instead, move your DICOM data to c:\temp and import it from there.
  </blockquote>
</aside>
<aside class="quote" data-post="1" data-topic="5398">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/71e660/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/special-characters/5398">Special characters</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    It may sound a total stupid ask from a person who shouldn’t use any software:) 
Is it possible to develop a warning sign or message in a popping up window if Slicer has a problem with a special character in a folder or file name? I lost 2 days to find where the problem should be when I was not able to load or open any files since I mistyped (I typed a special hungarian characet accidentaly) a name of a complete folder.
  </blockquote>
</aside>
<aside class="quote" data-post="2" data-topic="2459">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/error-loading-dicom-files/2459/2">Error loading Dicom Files</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi - 
It looks like the accent character in your pathname is causing a problem.  When I open the data from a directory with a plain ascii path it loads with no problem.  (the unicode conversion error message is the clue). 
-Steve
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="1" data-topic="2839">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/977dab/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/load-dicom-import/2839">load DICOM import</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: windows7 
Slicer version: 4.9.0 
Expected behavior: DICOM load 
Actual behavior: 
There is no change after loading the DICOM file. 
[1] 
If you drag the DICOM folder to the Slicer window and click “Load directory into dicom database”, nothing happens. 
When I import to DICOM Browser, there is no dicom data information. 
[2] 
The DICOM file I use is probably not a problem. 
It is being used in other programs. 
I have tried to input and import to try the DICOM Patcher module, but…
  </blockquote>
</aside>
<aside class="quote" data-post="7" data-topic="4464">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/can-t-import-dicom-data/4464/7">Can`t import DICOM data</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    The problem is likely due to this: 
“C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase 
Sorry, we don’t handle non-English characters well.  Please set your directory to point to an ascii-only path. 
Hope that helps, 
Steve
  </blockquote>
</aside>


---

## Post #4 by @lassoan (2019-04-06 17:38 UTC)

<p>I’ve added a warning popup when somebody wants to import DICOM files from a folder that contains special characters using drag-and-drop (see <a href="https://github.com/Slicer/Slicer/commit/45e98d37f16375a620931c622656a16484cf1b3d" rel="nofollow noopener">here</a>), but I did not have time to implement this for the case when the Import button is pressed. It would be nice if somebody could add the warning popup there, too.</p>

---

## Post #5 by @pieper (2019-04-06 18:06 UTC)

<p>Nice Andras <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>If someone has time to really dig into this, another nice feature would be to add a link to the <a href="https://www.slicer.org/wiki/Documentation/4.10/FAQ/DICOM" rel="nofollow noopener">Slicer DICOM FAQ</a> or other help (e.g. as part of the dialog when zero instances are imported).  It’s a little tricky since that dialog is <a href="https://github.com/commontk/CTK/blob/cccef11c938cc946789ddb25ccc613287a33c56e/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L119" rel="nofollow noopener">implemented in CTK</a>.  I guess it could be extended to have a QString property to display as a label when zero instances are imported.</p>

---

## Post #6 by @LizzyMedinaGtz (2019-04-08 14:06 UTC)

<p>this was the solution!, thank you very much</p>

---

## Post #7 by @Marci (2019-08-18 15:36 UTC)

<p>Hi there,</p>
<p>I also have a problem. Could anyone help please? I cannot import any .dcm files to Slicer 3D. I have the latest nightly build for Mac. I only get a notification:</p>
<p>“Directory import completed.<br>
0 New Patients<br>
0 New Studies<br>
0 New Series<br>
0 New Instances”</p>
<p>Log:<br>
[DEBUG][Qt] 18.08.2019 17:32:25 [] (unknown:0) - Session start time …: 2019-08-18 17:32:25<br>
[DEBUG][Qt] 18.08.2019 17:32:25 [] (unknown:0) - Slicer version …: 4.11.0-2019-08-16 (revision 28446) macosx-amd64 - installed release<br>
[DEBUG][Qt] 18.08.2019 17:32:25 [] (unknown:0) - Operating system …: Mac OS X / 10.14.5 / 18F132 - 64-bit<br>
[DEBUG][Qt] 18.08.2019 17:32:25 [] (unknown:0) - Memory …: 8192 MB physical, 2048 MB virtual<br>
[DEBUG][Qt] 18.08.2019 17:32:25 [] (unknown:0) - CPU …: GenuineIntel Intel® Core™ i5-5257U CPU @ 2.70GHz, 2 cores, 4 logical processors<br>
[DEBUG][Qt] 18.08.2019 17:32:25 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 18.08.2019 17:32:25 [] (unknown:0) - Qt configuration …: version 5.10.0, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 18.08.2019 17:32:25 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 18.08.2019 17:32:25 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 18.08.2019 17:32:25 [] (unknown:0) - Application path …: /Applications/Slicer.app/Contents/MacOS<br>
[DEBUG][Qt] 18.08.2019 17:32:25 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 18.08.2019 17:32:29 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 18.08.2019 17:32:31 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 18.08.2019 17:32:31 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 18.08.2019 17:32:32 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 18.08.2019 17:32:41 [] (unknown:0) - Switch to module:  “DICOM”<br>
[DEBUG][Qt] 18.08.2019 17:32:50 [] (unknown:0) - Could not load  “/Volumes/Macintosh HD/Users/Marci/Desktop/3D Anatomy Basal Lamella/CBCT 14 fej/Implant Oktat¢ Kurzus AJ170411/Implant Oktat¢ Kurzus AJ170411/data/images/cbct/1.dcm”<br>
DCMTK says:  No such file or directory<br>
[WARNING][Qt] 18.08.2019 17:32:50 [] (unknown:0) - Could not read DICOM file:/Volumes/Macintosh HD/Users/Marci/Desktop/3D Anatomy Basal Lamella/CBCT 14 fej/Implant Oktat¢ Kurzus AJ170411/Implant Oktat¢ Kurzus AJ170411/data/images/cbct/1.dcm<br>
[DEBUG][Qt] 18.08.2019 17:32:50 [] (unknown:0) - Could not load  “/Volumes/Macintosh HD/Users/Marci/Desktop/3D Anatomy Basal Lamella/CBCT 14 fej/Implant Oktat¢ Kurzus AJ170411/Implant Oktat¢ Kurzus AJ170411/data/images/cbct/cbct.txt”<br>
DCMTK says:  No such file or directory<br>
[WARNING][Qt] 18.08.2019 17:32:50 [] (unknown:0) - Could not read DICOM file:/Volumes/Macintosh HD/Users/Marci/Desktop/3D Anatomy Basal Lamella/CBCT 14 fej/Implant Oktat¢ Kurzus AJ170411/Implant Oktat¢ Kurzus AJ170411/data/images/cbct/cbct.txt<br>
[DEBUG][Qt] 18.08.2019 17:32:51 [] (unknown:0) - Could not load  “/Volumes/Macintosh HD/Users/Marci/Desktop/3D Anatomy Basal Lamella/CBCT 14 fej/Implant Oktat¢ Kurzus AJ170411/Implant Oktat¢ Kurzus AJ170411/data/images/cbct/cbct.xml”<br>
DCMTK says:  No such file or directory<br>
[WARNING][Qt] 18.08.2019 17:32:51 [] (unknown:0) - Could not read DICOM file:/Volumes/Macintosh HD/Users/Marci/Desktop/3D Anatomy Basal Lamella/CBCT 14 fej/Implant Oktat¢ Kurzus AJ170411/Implant Oktat¢ Kurzus AJ170411/data/images/cbct/cbct.xml<br>
[DEBUG][Qt] 18.08.2019 17:32:51 [] (unknown:0) - “DICOM indexer has successfully processed 3 files [0.42s]”<br>
[INFO][Python] 18.08.2019 17:33:07 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMWidgets.py:474) - Imported a DICOM directory, checking for extensions<br>
[INFO][Stream] 18.08.2019 17:33:07 [] (unknown:0) - Imported a DICOM directory, checking for extensions</p>
<p>Thank you very much for your help in advance</p>
<p>Yours<br>
M. Eördögh</p>

---

## Post #8 by @pieper (2019-08-18 15:56 UTC)

<p>Hi -</p>
<p>Looks like you have the same problem as <a href="https://discourse.slicer.org/t/dicom-import-fails-0-new-patients/6419">the post you replied to</a>.  Can you try again with only ascii characters in the path?  (also see <a href="https://discourse.slicer.org/t/special-characters/5398">this post</a>).</p>

---

## Post #9 by @Marci (2019-08-18 16:19 UTC)

<p>Hello,</p>
<p>I thought the same as I sent the mail. It helped. Thank you!</p>

---
