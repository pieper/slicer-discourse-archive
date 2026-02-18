# How to fix loading error: Could not load as DWI Volume as a Diffusion Volume

**Topic ID**: 281
**Date**: 2017-05-08
**URL**: https://discourse.slicer.org/t/how-to-fix-loading-error-could-not-load-as-dwi-volume-as-a-diffusion-volume/281

---

## Post #1 by @broccoli (2017-05-08 12:50 UTC)

<p>I am trying to load .dcm data. Sadly it failed, the error message displayed was Could not load as DWI Volume as a Diffusion Volume. However, I am not trying to load as DWI volume.</p>
<p>As an alternative I tried adding the data into the scene with the DATA button and converting to a multivolume with the MultiVolumeImporter module. This wasn’t a satisfactory solution, because I couldn’t select the created multivolume as input ct volume in other modules.</p>
<p>How this issue be fixed?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2017-05-08 12:53 UTC)

<p>Use the latest nightly version, probably your problem is fixed there already.</p>
<p>If you still have problems with loading your DICOM data then copy-paste here the application log (menu: Help/Report a bug) of a failed loading. Make sure you remove patient information from the log. What kind of data you would like to load?</p>

---

## Post #3 by @broccoli (2017-05-08 13:36 UTC)

<p>In the latest nightly version I get the same error.<br>
I am trying to load ct data with .dcm file type.<br>
Here is a copy of the error log with repetitions removed where possilble:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 08.05.2017 15:00:23 [] (unknown:0) - Session start time .......: 2017-05-08 15:00:23
[DEBUG][Qt] 08.05.2017 15:00:23 [] (unknown:0) - Slicer version ...........: 4.7.0-2017-05-06 (revision 26007) win-amd64 - installed
[DEBUG][Qt] 08.05.2017 15:00:23 [] (unknown:0) - Operating system .........: Windows / 7 / Service Pack 1 (Build 7601) - 64-bit
[DEBUG][Qt] 08.05.2017 15:00:23 [] (unknown:0) - Memory ...................: 4040 MB physical, 8079 MB virtual
[DEBUG][Qt] 08.05.2017 15:00:23 [] (unknown:0) - CPU ......................: GenuineIntel , 4 cores, 16 logical processors
[DEBUG][Qt] 08.05.2017 15:00:23 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 08.05.2017 15:00:23 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 08.05.2017 15:00:23 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 08.05.2017 15:00:26 [Python] (C:\Program Files\Slicer 4.7.0-2017-05-06\lib\Slicer-4.7\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 08.05.2017 15:00:27 [Python] (C:\Program Files\Slicer 4.7.0-2017-05-06\lib\Slicer-4.7\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 08.05.2017 15:00:27 [Python] (C:\Program Files\Slicer 4.7.0-2017-05-06\lib\Slicer-4.7\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 08.05.2017 15:00:23 [] (unknown:0) - Number of registered modules: 140
[DEBUG][Qt] 08.05.2017 15:00:26 [] (unknown:0) - Number of instantiated modules: 140
[WARNING][Qt] 08.05.2017 15:00:26 [] (unknown:0) - When loading module  "CLIEventTest" , the dependency "CLI4Test" failed to be loaded.
[INFO][Stream] 08.05.2017 15:00:27 [] (unknown:0) - Initializing terminology mapping for map file C:/Program Files/Slicer 4.7.0-2017-05-06/share/Slicer-4.7/ColorFiles/Terminology//GenericAnatomyColors-SNOMED.csv
[INFO][Stream] 08.05.2017 15:00:27 [] (unknown:0) - 288 terms were read for Slicer LUT GenericAnatomyColors
[WARNING][Qt] 08.05.2017 15:00:27 [] (unknown:0) - When loading module  "TwoCLIsInARowTest" , the dependency "CLI4Test" failed to be loaded.
[WARNING][Qt] 08.05.2017 15:00:27 [] (unknown:0) - When loading module  "TwoCLIsInParallelTest" , the dependency "CLI4Test" failed to be loaded.
[DEBUG][Qt] 08.05.2017 15:00:27 [] (unknown:0) - Number of loaded modules: 137
[DEBUG][Qt] 08.05.2017 15:00:27 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 08.05.2017 15:00:32 [] (unknown:0) - Switch to module:  "DICOM"
[WARNING][Python] 08.05.2017 15:00:53 [Python] (C:/Program Files/Slicer 4.7.0-2017-05-06/lib/Slicer-4.7/qt-scripted-modules/DICOMScalarVolumePlugin.py:253) - Geometric issues were found with 1 of the series.  Please use caution.
[WARNING][Python] 08.05.2017 15:00:54 [Python] (C:/Program Files/Slicer 4.7.0-2017-05-06/lib/Slicer-4.7/qt-scripted-modules/DICOMScalarVolumePlugin.py:253) - Geometric issues were found with 1 of the series.  Please use caution.
[CRITICAL][Stream] 08.05.2017 15:00:53 [] (unknown:0) - Geometric issues were found with 1 of the series.  Please use caution.
[CRITICAL][Stream] 08.05.2017 15:00:54 [] (unknown:0) - Geometric issues were found with 1 of the series.  Please use caution.
[DEBUG][Python] 08.05.2017 15:00:54 [Python] (C:/Program Files/Slicer 4.7.0-2017-05-06/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py:392) - MultiVolumeImportPlugin::examine
[DEBUG][Python] 08.05.2017 15:00:54 [Python] (C:/Program Files/Slicer 4.7.0-2017-05-06/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py:432) - DICOMMultiVolumePlugin found 0 multivolumes!
[DEBUG][Python] 08.05.2017 15:00:54 [Python] (C:/Program Files/Slicer 4.7.0-2017-05-06/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py:105) - MultiVolumeImportPlugin:examineMultiseries
[DEBUG][Python] 08.05.2017 15:00:55 [Python] (C:/Program Files/Slicer 4.7.0-2017-05-06/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py:110) - DICOMMultiVolumePlugin found 0 multivolumes!
[WARNING][Python] 08.05.2017 15:00:55 [Python] (C:\Program Files\Slicer 4.7.0-2017-05-06\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\DICOMWidgets.py:857) - Warning in DICOM plugin Scalar Volume when examining loadable 10003: file: There is no pixel data attribute for the DICOM objects, but they might be readable as secondary capture images.  Images are not equally spaced (a difference of 0.7 in spacings was detected).  Slicer will load this series as if it had a spacing of 0.  Please use caution.
[WARNING][Python] 08.05.2017 15:00:55 [Python] (C:\Program Files\Slicer 4.7.0-2017-05-06\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\DICOMWidgets.py:857) - Warning in DICOM plugin Scalar Volume when examining loadable 10003: file for contentTime of 174244.497000: There is no pixel data attribute for the DICOM objects, but they might be readable as secondary capture images.
[WARNING][Python] 08.05.2017 15:00:55 [Python] (C:\Program Files\Slicer 4.7.0-2017-05-06\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\DICOMWidgets.py:857) - Warning in DICOM plugin Scalar Volume when examining loadable 10003: file for contentTime of 174244.487000: There is no pixel data attribute for the DICOM objects, but they might be readable as secondary capture images.
[WARNING][Python] 08.05.2017 15:00:55 [Python] (C:\Program Files\Slicer 4.7.0-2017-05-06\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\DICOMWidgets.py:857) - Warning in DICOM plugin Scalar Volume when examining loadable 10003: file for contentTime of 174244.481000: There is no pixel data attribute for the DICOM objects, but they might be readable as secondary capture images.
 Images are not equally spaced (a difference of 0.7 in spacings was detected).  Slicer will load this series as if it had a spacing of 0.  Please use caution.
[CRITICAL][Stream] 08.05.2017 15:00:55 [] (unknown:0) - Warning in DICOM plugin Scalar Volume when examining loadable 10003: file: There is no pixel data attribute for the DICOM objects, but they might be readable as secondary capture images.  Images are not equally spaced (a difference of 0.7 in spacings was detected).  Slicer will load this series as if it had a spacing of 0.  Please use caution.
[CRITICAL][Stream] 08.05.2017 15:00:55 [] (unknown:0) - Warning in DICOM plugin Scalar Volume when examining loadable 10003: file for contentTime of 174244.497000: There is no pixel data attribute for the DICOM objects, but they might be readable as secondary capture images.
Images are not equally spaced (a difference of 0.7 in spacings was detected).  Slicer will load this series as if it had a spacing of 0.  Please use caution.
[WARNING][Python] 08.05.2017 15:01:25 [Python] (C:\Program Files\Slicer 4.7.0-2017-05-06\bin\Python\slicer\util.py:810) - 
Could not load: file - as DWI Volume as a Diffusion Volume
[DEBUG][Qt] 08.05.2017 15:01:04 [] (unknown:0) - Found CommandLine Module, target is  C:/Program Files/Slicer 4.7.0-2017-05-06/lib/Slicer-4.7/cli-modules/DWIConvert.exe
[DEBUG][Qt] 08.05.2017 15:01:04 [] (unknown:0) - ModuleType: CommandLineModule
[DEBUG][Qt] 08.05.2017 15:01:04 [] (unknown:0) - Diffusion-weighted DICOM Import (DWIConvert) command line: 

C:/Program Files/Slicer 4.7.0-2017-05-06/lib/Slicer-4.7/cli-modules/DWIConvert.exe --conversionMode DicomToNrrd --outputVolume C:/Users/_/AppData/Local/Temp/Slicer/HDJG_vtkMRMLDiffusionWeightedVolumeNodeB.nrrd --inputDicomDirectory C:/Users/_/AppData/Local/Temp/Slicer/__SlicerTemp__ --outputDirectory C:/Users/_/AppData/Local/Temp/Slicer --smallGradientThreshold 0.2 --transposeInputBVectors
[ERROR][VTK] 08.05.2017 15:01:25 [vtkSlicerCLIModuleLogic (000000000CCA5920)] (C:\D\N\Slicer-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2159) - Diffusion-weighted DICOM Import (DWIConvert) standard error:

E: can't change to unencapsulated representation for pixel data
E: can't determine 'PhotometricInterpretation' of decompressed image
E: mandatory attribute 'PhotometricInterpretation' is missing or can't be determined
E: can't change to unencapsulated representation for pixel data

Error: no DICOMfiles found in inputDirectory: C:/Users/_/AppData/Local/Temp/Slicer/__SlicerTemp__
[ERROR][VTK] 08.05.2017 15:01:25 [vtkSlicerCLIModuleLogic (000000000CCA5920)] (C:\D\N\Slicer-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2243) - Diffusion-weighted DICOM Import (DWIConvert) terminated with a fault.
[CRITICAL][Stream] 08.05.2017 15:01:25 [] (unknown:0) -
[CRITICAL][Stream] 08.05.2017 15:01:25 [] (unknown:0) - Could not load: file - as DWI Volume as a Diffusion Volume
[DEBUG][Python] 08.05.2017 15:03:02 [Python] (C:/Program Files/Slicer 4.7.0-2017-05-06/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py:392) - MultiVolumeImportPlugin::examine
[DEBUG][Python] 08.05.2017 15:03:03 [Python] (C:/Program Files/Slicer 4.7.0-2017-05-06/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py:432) - DICOMMultiVolumePlugin found 0 multivolumes!
[DEBUG][Python] 08.05.2017 15:03:03 [Python] (C:/Program Files/Slicer 4.7.0-2017-05-06/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py:105) - MultiVolumeImportPlugin:examineMultiseries
[DEBUG][Python] 08.05.2017 15:03:03 [Python] (C:/Program Files/Slicer 4.7.0-2017-05-06/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py:110) - DICOMMultiVolumePlugin found 0 multivolumes!
[WARNING][Python] 08.05.2017 15:03:03 [Python] (C:\Program Files\Slicer 4.7.0-2017-05-06\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\DICOMWidgets.py:857) - Warning in DICOM plugin Scalar Volume when examining loadable 10003: file: There is no pixel data attribute for the DICOM objects, but they might be readable as secondary capture images.  Images are not equally spaced (a difference of 0.7 in spacings was detected).  Slicer will load this series as if it had a spacing of 0.  Please use caution.
[WARNING][Python] 08.05.2017 15:03:03 [Python] (C:\Program Files\Slicer 4.7.0-2017-05-06\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\DICOMWidgets.py:857) - Warning in DICOM plugin Scalar Volume when examining loadable 10003: file for contentTime of 174244.497000: There is no pixel data attribute for the DICOM objects, but they might be readable as secondary capture images.
[WARNING][Python] 08.05.2017 15:03:03 [Python] (C:\Program Files\Slicer 4.7.0-2017-05-06\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\DICOMWidgets.py:857) - Warning in DICOM plugin Scalar Volume when examining loadable 10003: file for contentTime of 174244.487000: There is no pixel data attribute for the DICOM objects, but they might be readable as secondary capture images.
Images are not equally spaced (a difference of 0.7 in spacings was detected).  Slicer will load this series as if it had a spacing of 0.  Please use caution.
[CRITICAL][Stream] 08.05.2017 15:03:03 [] (unknown:0) - Warning in DICOM plugin Scalar Volume when examining loadable 10003: file: There is no pixel data attribute for the DICOM objects, but they might be readable as secondary capture images.  Images are not equally spaced (a difference of 0.7 in spacings was detected).  Slicer will load this series as if it had a spacing of 0.  Please use caution.
[CRITICAL][Stream] 08.05.2017 15:03:03 [] (unknown:0) - Warning in DICOM plugin Scalar Volume when examining loadable 10003: file for contentTime of 174244.497000: There is no pixel data attribute for the DICOM objects, but they might be readable as secondary capture images.
Images are not equally spaced (a difference of 0.7 in spacings was detected).  Slicer will load this series as if it had a spacing of 0.  Please use caution.
[WARNING][Python] 08.05.2017 15:03:11 [Python] (C:\Program Files\Slicer 4.7.0-2017-05-06\bin\Python\slicer\util.py:810) - 
Could not load: file - as DWI Volume as a Diffusion Volume
[DEBUG][Qt] 08.05.2017 15:03:04 [] (unknown:0) - Found CommandLine Module, target is  C:/Program Files/Slicer 4.7.0-2017-05-06/lib/Slicer-4.7/cli-modules/DWIConvert.exe
[DEBUG][Qt] 08.05.2017 15:03:04 [] (unknown:0) - ModuleType: CommandLineModule
[DEBUG][Qt] 08.05.2017 15:03:04 [] (unknown:0) - Diffusion-weighted DICOM Import (DWIConvert) command line: 

C:/Program Files/Slicer 4.7.0-2017-05-06/lib/Slicer-4.7/cli-modules/DWIConvert.exe --conversionMode DicomToNrrd --outputVolume C:/Users/_/AppData/Local/Temp/Slicer/HDJG_vtkMRMLDiffusionWeightedVolumeNodeC.nrrd --inputDicomDirectory C:/Users/_/AppData/Local/Temp/Slicer/__SlicerTemp__ --outputDirectory C:/Users/_/AppData/Local/Temp/Slicer --smallGradientThreshold 0.2 --transposeInputBVectors
[ERROR][VTK] 08.05.2017 15:03:11 [vtkSlicerCLIModuleLogic (000000000CCA5920)] (C:\D\N\Slicer-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2159) - Diffusion-weighted DICOM Import (DWIConvert) standard error:

E: can't change to unencapsulated representation for pixel data
E: can't determine 'PhotometricInterpretation' of decompressed image
E: mandatory attribute 'PhotometricInterpretation' is missing or can't be determined
E: can't change to unencapsulated representation for pixel data


Error: no DICOMfiles found in inputDirectory: C:/Users/_/AppData/Local/Temp/Slicer/__SlicerTemp__
[ERROR][VTK] 08.05.2017 15:03:11 [vtkSlicerCLIModuleLogic (000000000CCA5920)] (C:\D\N\Slicer-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2243) - Diffusion-weighted DICOM Import (DWIConvert) terminated with a fault.
[CRITICAL][Stream] 08.05.2017 15:03:11 [] (unknown:0) -
[CRITICAL][Stream] 08.05.2017 15:03:11 [] (unknown:0) - Could not load: file - as DWI Volume as a Diffusion Volume
</code></pre>

---

## Post #4 by @fedorov (2017-05-08 13:49 UTC)

<aside class="quote no-group quote-modified" data-username="broccoli" data-post="3" data-topic="281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/a183cd/48.png" class="avatar"> broccoli:</div>
<blockquote>
<p>[DEBUG][Qt] 08.05.2017 15:03:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Diffusion-weighted DICOM Import (DWIConvert) command line:</p>
<p>C:/Program Files/Slicer 4.7.0-2017-05-06/lib/Slicer-4.7/cli-modules/DWIConvert.exe --conversionMode DicomToNrrd --outputVolume</p>
</blockquote>
</aside>
<p>If you are getting this for a CT volume, it means there is a problem with DWI plugin. It should not be triggered for a CT volume.</p>
<p>Please confirm that you included the correct log file.</p>

---

## Post #5 by @broccoli (2017-05-08 13:54 UTC)

<p>The log file was copied after the attempt at loading the ct data. This was the first thing I tried after installing the newest nightly version.</p>

---

## Post #6 by @lassoan (2017-05-08 14:05 UTC)

<p>Could you please try loading with DWI plugin disabled?</p>
<p>How to disable DWI plugin:</p>
<ul>
<li>check the “Advanced” checkbox in the lower right corner of DICOM browser</li>
<li>uncheck “DICOMDiffusionVolumePlugin” at the left side of the window</li>
<li>uncheck the “Advanced” checkbox</li>
</ul>

---

## Post #7 by @lassoan (2017-05-08 14:10 UTC)

<aside class="quote no-group" data-username="broccoli" data-post="3" data-topic="281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/a183cd/48.png" class="avatar"> broccoli:</div>
<blockquote>
<p>DICOM objects, but they might be readable as secondary capture images.<br>
Images are not equally spaced (a difference of 0.7 in spacings was detected).  Slicer will load this series as if it had a spacing of 0.  Please use caution.<br>
[WARNING][Python] 08.05.2017 15:01:25 [Python] (C:\Program Files\Slicer 4.7.0-2017-05-06\bin\Python\slicer\util.py:810) -</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/ihnorton">@ihnorton</a> Could you please check if you can tune the DWI volume detection code based on this log? If it’s difficult to write a sensitive but robust detection mechanism for DWI volumes then probably the best is to move the DWI DICOM plugin to the Diffusion extension.</p>

---

## Post #8 by @fedorov (2017-05-08 14:15 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>DICOM objects, but they might be readable as secondary capture images.<br>
Images are not equally spaced (a difference of 0.7 in spacings was detected).  Slicer will load this series as if it had a spacing of 0.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> it looks like there may be other issues with the data. This specific error comes from the ScalarVolume plugin.</p>
<p>I agree that certainly CT should not be called out by the DWI plugin. We’ve seen this kind of behavior earlier in other situations, and it is quite confusing.</p>
<aside class="quote no-group quote-modified" data-username="broccoli" data-post="3" data-topic="281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/a183cd/48.png" class="avatar"> broccoli:</div>
<blockquote>
<p>[CRITICAL][Stream] 08.05.2017 15:00:55 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Warning in DICOM plugin Scalar Volume when examining loadable 10003: file: There is no pixel data attribute for the DICOM objects, but they might be readable as secondary capture images.  Images are not equally spaced (a difference of 0.7 in spacings was detected).  Slicer will load this series as if it had a spacing of 0.  Please use caution.</p>
</blockquote>
</aside>

---

## Post #9 by @broccoli (2017-05-08 14:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="281" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Could you please try loading with DWI plugin disabled?</p>
<p>How to disable DWI plugin:</p>
<ul>
<li>check the “Advanced” checkbox in the lower right corner of DICOM browser</li>
<li>uncheck “DICOMDiffusionVolumePlugin” at the left side of the window</li>
<li>uncheck the “Advanced” checkbox</li>
</ul>
</blockquote>
</aside>
<p>With the DWI plugin disabled the data could be loaded <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
Thank you and <a class="mention" href="/u/fedorov">@fedorov</a> for the help!</p>

---

## Post #10 by @fedorov (2017-05-08 14:24 UTC)

<aside class="quote no-group" data-username="broccoli" data-post="9" data-topic="281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/a183cd/48.png" class="avatar"> broccoli:</div>
<blockquote>
<p>With the DWI plugin disabled the data could be loaded <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
</blockquote>
</aside>
<p>Wow, I can’t explain the error messages then… I have to admit I have no idea what is going on on your side! Glad it works, anyway.</p>

---

## Post #11 by @lassoan (2017-05-08 14:43 UTC)

<p>Often there are a couple of DICOM objects that none of the plugins recognize or can load properly (scout scans, dose reports, etc). For those the scalar volume plugin prints error messages like this. I agree that it is confusing and not specific enough. Probably the scalar volume reader should reject those items, too. I’ve added a ticket to track the improvement of these error messages: <a href="http://na-mic.org/Mantis/view.php?id=4371">http://na-mic.org/Mantis/view.php?id=4371</a>.</p>

---

## Post #12 by @fedorov (2017-05-08 14:53 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> only if the user parses at the study level, right? It seems that only one loadable is being examined, from the messages in the log.</p>
<p><a class="mention" href="/u/broccoli">@broccoli</a>, if you can, please let us know for the error below:</p>
<ol>
<li>does the ScalarVolume plugin error happen in the earlier release of Slicer for the same dataset, or it is something new?</li>
<li>are you trying to load the whole study, or just a single CT series when this error shows up?</li>
</ol>
<aside class="quote no-group" data-username="broccoli" data-post="3" data-topic="281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/a183cd/48.png" class="avatar"> broccoli:</div>
<blockquote>
<p>[WARNING][Python] 08.05.2017 15:03:03 [Python] (C:\Program Files\Slicer 4.7.0-2017-05-06\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\DICOMWidgets.py:857) - Warning in DICOM plugin Scalar Volume when examining loadable 10003: file: There is no pixel data attribute for the DICOM objects, but they might be readable as secondary capture images.  Images are not equally spaced (a difference of 0.7 in spacings was detected).  Slicer will load this series as if it had a spacing of 0.  Please use caution.</p>
</blockquote>
</aside>

---

## Post #13 by @broccoli (2017-05-08 15:28 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="12" data-topic="281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p><a class="mention" href="/u/broccoli">@broccoli</a>, if you can, please let us know for the error below:</p>
<ol>
<li>does the ScalarVolume plugin error happen in the earlier release of Slicer for the same dataset, or it is something new?</li>
<li>are you trying to load the whole study, or just a single CT series when this error shows up?</li>
</ol>
</blockquote>
</aside>
<p>Using version 4.7.0-2017-04-04 the error still shows up:</p>
<pre><code class="lang-auto">[WARNING][Python] 08.05.2017 17:19:11 [Python] (C:\Program Files\Slicer 4.7.0-2017-04-04\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\DICOMWidgets.py:827) - Warning in DICOM plugin Scalar Volume when examining loadable 10003: file: There is no pixel data attribute for the DICOM objects, but they might be readable as secondary capture images.  Images are not equally spaced (a difference of 0.7 in spacings was detected).  Slicer will load this series as if it had a spacing of 0.  Please use caution.
</code></pre>
<p>I also get the following popup message in this version: <code>Warning: 92 of 184 selected files listed in the database cannot be found on disk.</code><br>
This seems odd to me, as the folder with the ct series is supposed to contain 92 files.</p>

---

## Post #14 by @lassoan (2017-05-08 15:32 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="12" data-topic="281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p><a class="mention" href="/u/lassoan">@lassoan</a> only if the user parses at the study level, right? It seems that only one loadable is being examined, from the messages in the log.</p>
</blockquote>
</aside>
<p>Yes. The error should not show up if the user explicitly selects only the items that can be loaded.</p>

---
