# tempDICOMDatabase crashes slicer

**Topic ID**: 25515
**Date**: 2022-10-03
**URL**: https://discourse.slicer.org/t/tempdicomdatabase-crashes-slicer/25515

---

## Post #1 by @talmazov (2022-10-03 00:21 UTC)

<p>Hey all,<br>
I am experiencing a peculiar issue and I was hoping for some help to help me narrow down the problem.<br>
I have the following piece of code</p>
<pre><code class="lang-auto">dicomDataDir = os.path.dirname(context.scene.DICOM_dir).replace(os.sep, '/'),
loadedNodeIDs = []
from DICOMLib import DICOMUtils
with DICOMUtils.TemporaryDICOMDatabase() as db:
    DICOMUtils.importDicom(dicomDataDir, db)
    patientUIDs = db.patients()
    for patientUID in patientUIDs:
        loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
    DICOMUtils.deleteTemporaryDatabase(db, True)
</code></pre>
<p>where dicomDataDir points to a dicom folder.<br>
this code logic is in a function i call on slicer startup.</p>
<p>For some DICOM series it works, for others it causes slicer to crash and exit unexpectedly during startup. the peculiar part is that the same DICOM series may load and allow slicer to work fine while other times it causes it to crash - so perhaps it is not an issue with the DICOM files?</p>
<p>below is the log output when a crash occurs:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 02.10.2022 19:58:55 [] (unknown:0) - Session start time .......: 2022-10-02 19:58:55
[DEBUG][Qt] 02.10.2022 19:58:55 [] (unknown:0) - Slicer version ...........: 5.0.2 (revision 30822 / a4420c3) win-amd64 - installed release
[DEBUG][Qt] 02.10.2022 19:58:55 [] (unknown:0) - Operating system .........: Windows /  Personal / (Build 19043, Code Page 65001) - 64-bit
[DEBUG][Qt] 02.10.2022 19:58:55 [] (unknown:0) - Memory ...................: 32702 MB physical, 37566 MB virtual
[DEBUG][Qt] 02.10.2022 19:58:55 [] (unknown:0) - CPU ......................: GenuineIntel , 8 cores, 8 logical processors
[DEBUG][Qt] 02.10.2022 19:58:55 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 02.10.2022 19:58:55 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 02.10.2022 19:58:55 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 02.10.2022 19:58:55 [] (unknown:0) - Developer mode ...........: enabled
[DEBUG][Qt] 02.10.2022 19:58:55 [] (unknown:0) - Application path .........: C:/ProgramData/NA-MIC/Slicer 5.0.2/bin
[DEBUG][Qt] 02.10.2022 19:58:55 [] (unknown:0) - Additional module paths ..: C:/Users/Mayotic/AppData/Roaming/Blender Foundation/Blender/3.2/scripts/addons/openPlan/slicer_module
[DEBUG][Python] 02.10.2022 19:58:56 [Python] (C:\ProgramData\NA-MIC\Slicer 5.0.2\lib\Slicer-5.0\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 02.10.2022 19:58:57 [Python] (C:\ProgramData\NA-MIC\Slicer 5.0.2\lib\Slicer-5.0\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 02.10.2022 19:58:57 [Python] (C:\ProgramData\NA-MIC\Slicer 5.0.2\lib\Slicer-5.0\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 02.10.2022 19:58:57 [] (unknown:0) - Switch to module:  "Welcome"
[INFO][Python] 02.10.2022 19:58:58 [Python] (C:\ProgramData\NA-MIC\Slicer 5.0.2\lib\Slicer-5.0\qt-scripted-modules\DICOMLib\DICOMUtils.py:318) - Switching to temporary DICOM database: C:/Users/Mayotic/AppData/Local/Temp/Slicer/20221002_235858_TempDICOMDatabase
[INFO][Stream] 02.10.2022 19:58:58 [] (unknown:0) - Switching to temporary DICOM database: C:/Users/Mayotic/AppData/Local/Temp/Slicer/20221002_235858_TempDICOMDatabase
[DEBUG][Qt] 02.10.2022 19:58:58 [] (unknown:0) - TagCacheDatabase adding table
[DEBUG][Qt] 02.10.2022 19:58:59 [] (unknown:0) - "DICOM indexer has successfully inserted 500 files [0.20s]"
[DEBUG][Qt] 02.10.2022 19:58:59 [] (unknown:0) - "DICOM indexer has successfully processed 500 files [1.80s]"
[DEBUG][Qt] 02.10.2022 19:59:00 [] (unknown:0) - "DICOM indexer has updated display fields for 500 files [0.10s]"
[INFO][Python] 02.10.2022 19:59:01 [Python] (C:/ProgramData/NA-MIC/Slicer 5.0.2/bin/../lib/Slicer-5.0/qt-scripted-modules/DICOMScalarVolumePlugin.py:391) - Loading with imageIOName: GDCM
</code></pre>
<p>and below is the log output when everything loads perfect and slicer works (this one failed to open properly second time around):</p>
<pre><code class="lang-auto">[DEBUG][Qt] 02.10.2022 20:06:47 [] (unknown:0) - Session start time .......: 2022-10-02 20:06:47
[DEBUG][Qt] 02.10.2022 20:06:47 [] (unknown:0) - Slicer version ...........: 5.0.2 (revision 30822 / a4420c3) win-amd64 - installed release
[DEBUG][Qt] 02.10.2022 20:06:47 [] (unknown:0) - Operating system .........: Windows /  Personal / (Build 19043, Code Page 65001) - 64-bit
[DEBUG][Qt] 02.10.2022 20:06:47 [] (unknown:0) - Memory ...................: 32702 MB physical, 37566 MB virtual
[DEBUG][Qt] 02.10.2022 20:06:47 [] (unknown:0) - CPU ......................: GenuineIntel , 8 cores, 8 logical processors
[DEBUG][Qt] 02.10.2022 20:06:47 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 02.10.2022 20:06:47 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 02.10.2022 20:06:47 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 02.10.2022 20:06:47 [] (unknown:0) - Developer mode ...........: enabled
[DEBUG][Qt] 02.10.2022 20:06:47 [] (unknown:0) - Application path .........: C:/ProgramData/NA-MIC/Slicer 5.0.2/bin
[DEBUG][Qt] 02.10.2022 20:06:47 [] (unknown:0) - Additional module paths ..: C:/Users/Mayotic/AppData/Roaming/Blender Foundation/Blender/3.2/scripts/addons/openPlan/slicer_module
[DEBUG][Python] 02.10.2022 20:06:48 [Python] (C:\ProgramData\NA-MIC\Slicer 5.0.2\lib\Slicer-5.0\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 02.10.2022 20:06:49 [Python] (C:\ProgramData\NA-MIC\Slicer 5.0.2\lib\Slicer-5.0\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 02.10.2022 20:06:49 [Python] (C:\ProgramData\NA-MIC\Slicer 5.0.2\lib\Slicer-5.0\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 02.10.2022 20:06:49 [] (unknown:0) - Switch to module:  "Welcome"
[INFO][Python] 02.10.2022 20:06:50 [Python] (C:\ProgramData\NA-MIC\Slicer 5.0.2\lib\Slicer-5.0\qt-scripted-modules\DICOMLib\DICOMUtils.py:318) - Switching to temporary DICOM database: C:/Users/Mayotic/AppData/Local/Temp/Slicer/20221003_000650_TempDICOMDatabase
[INFO][Stream] 02.10.2022 20:06:50 [] (unknown:0) - Switching to temporary DICOM database: C:/Users/Mayotic/AppData/Local/Temp/Slicer/20221003_000650_TempDICOMDatabase
[DEBUG][Qt] 02.10.2022 20:06:50 [] (unknown:0) - TagCacheDatabase adding table
[CRITICAL][Stream] 02.10.2022 20:06:52 [] (unknown:0) - E: DcmElement: Unknown Tag &amp; Data (3f3c,6d78) larger (1702240364) than remaining bytes in file
[DEBUG][Qt] 02.10.2022 20:06:52 [] (unknown:0) - Could not load  "C:/Users/Mayotic/Downloads/CBCT/Analyses/1.2.250.1.90.3.4061631600.20210308165901.9728.34.xml" 
DCMTK says:  I/O suspension or premature end of stream
[WARNING][Qt] 02.10.2022 20:06:52 [] (unknown:0) - Could not read DICOM file:C:/Users/Mayotic/Downloads/CBCT/Analyses/1.2.250.1.90.3.4061631600.20210308165901.9728.34.xml
[CRITICAL][Stream] 02.10.2022 20:06:52 [] (unknown:0) - E: DcmElement: Unknown Tag &amp; Data (3f3c,6d78) larger (1702240364) than remaining bytes in file
[DEBUG][Qt] 02.10.2022 20:06:52 [] (unknown:0) - Could not load  "C:/Users/Mayotic/Downloads/CBCT/FilesManager.xml" 
DCMTK says:  I/O suspension or premature end of stream
[WARNING][Qt] 02.10.2022 20:06:52 [] (unknown:0) - Could not read DICOM file:C:/Users/Mayotic/Downloads/CBCT/FilesManager.xml
[DEBUG][Qt] 02.10.2022 20:06:53 [] (unknown:0) - "DICOM indexer has successfully inserted 651 files [0.26s]"
[DEBUG][Qt] 02.10.2022 20:06:53 [] (unknown:0) - "DICOM indexer has successfully processed 653 files [2.93s]"
[DEBUG][Qt] 02.10.2022 20:06:53 [] (unknown:0) - "DICOM indexer has updated display fields for 651 files [0.13s]"
[INFO][Python] 02.10.2022 20:07:02 [Python] (C:/ProgramData/NA-MIC/Slicer 5.0.2/bin/../lib/Slicer-5.0/qt-scripted-modules/DICOMScalarVolumePlugin.py:391) - Loading with imageIOName: GDCM
[INFO][Python] 02.10.2022 20:07:06 [Python] (C:/ProgramData/NA-MIC/Slicer 5.0.2/bin/../lib/Slicer-5.0/qt-scripted-modules/DICOMScalarVolumePlugin.py:470) - Window/level found in DICOM tags (center=1048.0, width=4096.0) has been applied to volume 1: 3D CBCT Image Set
[ERROR][Python] 02.10.2022 20:07:07 [Python] (C:\ProgramData\NA-MIC\Slicer 5.0.2\lib\Slicer-5.0\qt-scripted-modules\DICOMLib\DICOMUtils.py:351) - Unable to close DICOM database C:/Users/Mayotic/AppData/Local/Temp/Slicer/20221003_000650_TempDICOMDatabase/ctkDICOM.sql
[INFO][Stream] 02.10.2022 20:07:02 [] (unknown:0) - Loading with imageIOName: GDCM
[ERROR][VTK] 02.10.2022 20:07:06 [vtkCompositeDataPipeline (00000205552D6390)] (D:\D\S\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkImageMapToWindowLevelColors(000002055600F5B0) has 0 connections but is not optional.
[ERROR][VTK] 02.10.2022 20:07:06 [vtkCompositeDataPipeline (00000205552D6590)] (D:\D\S\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkImageThreshold(000002055600F170) has 0 connections but is not optional.
[ERROR][VTK] 02.10.2022 20:07:06 [vtkCompositeDataPipeline (00000205552D6390)] (D:\D\S\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkImageMapToWindowLevelColors(000002055600F5B0) has 0 connections but is not optional.
[ERROR][VTK] 02.10.2022 20:07:06 [vtkCompositeDataPipeline (0000020542DCA8C0)] (D:\D\S\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkImageMapToWindowLevelColors(000002055600F6C0) has 0 connections but is not optional.
[ERROR][VTK] 02.10.2022 20:07:06 [vtkCompositeDataPipeline (0000020542DC9DC0)] (D:\D\S\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkImageThreshold(000002055600F280) has 0 connections but is not optional.
[ERROR][VTK] 02.10.2022 20:07:06 [vtkCompositeDataPipeline (0000020542DCA8C0)] (D:\D\S\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkImageMapToWindowLevelColors(000002055600F6C0) has 0 connections but is not optional.
[INFO][Stream] 02.10.2022 20:07:06 [] (unknown:0) - Window/level found in DICOM tags (center=1048.0, width=4096.0) has been applied to volume 1: 3D CBCT Image Set
[CRITICAL][Stream] 02.10.2022 20:07:07 [] (unknown:0) - Unable to close DICOM database C:/Users/Mayotic/AppData/Local/Temp/Slicer/20221003_000650_TempDICOMDatabase/ctkDICOM.sql
[DEBUG][Qt] 02.10.2022 20:07:07 [] (unknown:0) - Switch to module:  "BlenderMonitor"
[INFO][Stream] 02.10.2022 20:07:21 [] (unknown:0) - DISCONNECTED
[DEBUG][Qt] 02.10.2022 20:07:23 [] (unknown:0) - Switch to module:  ""

</code></pre>
<p>any thoughts? has anyone experienced issues with the temporary DICOM database?<br>
alternatively i could use the normal DICOM database and then remove the loaded data? any examples of removing patients from the DICOM browser using python?<br>
I thought using loadVolume would be a good work-around but the DICOM volume data sometimes is loaded with flipped coordinates</p>
<p>Best,<br>
Georgi</p>

---

## Post #2 by @talmazov (2022-10-04 22:50 UTC)

<p>I’ve been messing around trying to debug and I was able to narrow it down to this.<br>
Using</p>
<pre><code class="lang-auto">DICOMUtils.importDicom(dicomDataDir, slicer.dicomDatabase)
</code></pre>
<p>on startup work just fine, but the moment I call</p>
<pre><code class="lang-auto">DICOMUtils.loadPatientByUID(slicer.dicomDatabase.patients()[0])
</code></pre>
<p>slicer crashes.<br>
I will try to see if using</p>
<pre><code class="lang-auto">scalarVolumeReader = DICOMScalarVolumePlugin.DICOMScalarVolumePluginClass()
</code></pre>
<p>method from <a href="https://discourse.slicer.org/t/loading-dicom-files-with-python-script-for-mac/12855/4" class="inline-onebox">Loading DICOM files with python script for Mac - #4 by epearlstone</a><br>
would provide a viable solution</p>
<p>~Georgi</p>

---

## Post #3 by @pieper (2022-10-04 22:54 UTC)

<p>Narrowing this down should really help.  If you have a debug build you should be able to figure out what is crashing.  In any case if you could provide a way to reproduce the issue with public data then others can investigate.</p>

---
