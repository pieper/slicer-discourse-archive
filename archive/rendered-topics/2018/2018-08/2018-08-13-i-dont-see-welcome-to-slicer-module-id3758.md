---
topic_id: 3758
title: "I Dont See Welcome To Slicer Module"
date: 2018-08-13
url: https://discourse.slicer.org/t/3758
---

# I don't see Welcome to Slicer module

**Topic ID**: 3758
**Date**: 2018-08-13
**URL**: https://discourse.slicer.org/t/i-dont-see-welcome-to-slicer-module/3758

---

## Post #1 by @kadohisa (2018-08-13 13:50 UTC)

<p>Problem report for Slicer 4.9.0-2018-08-10 win-amd64: [please describe expected and actual behavior]</p>
<p>Dear Sir/Madam,<br>
I downloaded version 4.8.1 for Windows onto my computer yesterday, then I saw one of modules, Welcome to Slicer, then I could uploaded my DICOM files. However, I could not get .mrml files. Once I closed the application, then opened again. But I neither saw the module, ‘Welcome to Slicer’  or uploaded DICOM files.<br>
Therefor I’ve tried to uninstall the version to replace with the latest version 4.9.0. However, again, I neither see Welcom to Slicer or can upload DICOM files.<br>
I’d appreciate it if you’d let me know what I should do.</p>
<p>Best wishes,</p>
<p>Miki</p>

---

## Post #2 by @ezproxy (2018-08-13 14:17 UTC)

<p>U can load Dicom Data from here.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72f37d6d8631a76b2943b62dc7559206fae176bc.png" data-download-href="/uploads/short-url/goU6BbDcFO0zdkRN7T10NnptRZq.png?dl=1" title="Load%20Dicom%20Data" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72f37d6d8631a76b2943b62dc7559206fae176bc_2_690x488.png" alt="Load%20Dicom%20Data" data-base62-sha1="goU6BbDcFO0zdkRN7T10NnptRZq" width="690" height="488" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72f37d6d8631a76b2943b62dc7559206fae176bc_2_690x488.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72f37d6d8631a76b2943b62dc7559206fae176bc.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72f37d6d8631a76b2943b62dc7559206fae176bc.png 2x" data-dominant-color="EFEEF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Load%20Dicom%20Data</span><span class="informations">802×568 43.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @kadohisa (2018-08-13 14:47 UTC)

<p>I’m afraid it is not an answer to my question. My problem is that I don’t see this ‘Welcome to Slicer’ view at first.<br>
Then I’ve got the following bug reports.</p>
<pre><code class="lang-auto">[DEBUG][Qt] 13.08.2018 14:08:24 [] (unknown:0) - Session start time .......: 2018-08-13 14:08:24
[DEBUG][Qt] 13.08.2018 14:08:24 [] (unknown:0) - Slicer version ...........: 4.9.0-2018-08-10 (revision 27345) win-amd64 - installed release
[DEBUG][Qt] 13.08.2018 14:08:24 [] (unknown:0) - Operating system .........: Windows / 7 /  (Build 7600) - 64-bit
[DEBUG][Qt] 13.08.2018 14:08:24 [] (unknown:0) - Memory ...................: 32652 MB physical, 65303 MB virtual
[DEBUG][Qt] 13.08.2018 14:08:24 [] (unknown:0) - CPU ......................: GenuineIntel , 8 cores, 8 logical processors
[DEBUG][Qt] 13.08.2018 14:08:24 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 13.08.2018 14:08:24 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 13.08.2018 14:08:24 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 13.08.2018 14:08:24 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 13.08.2018 14:08:25 [Python] (C:\Program Files\Slicer 4.9.0-2018-08-10\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(['git', 'version'], cwd=C:\Program Files\Slicer 4.9.0-2018-08-10, universal_newlines=False, shell=None)
[DEBUG][Python] 13.08.2018 14:08:25 [Python] (C:\Program Files\Slicer 4.9.0-2018-08-10\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(['git', 'version'], cwd=C:\Program Files\Slicer 4.9.0-2018-08-10, universal_newlines=False, shell=None)
[WARNING][Qt] 13.08.2018 14:08:27 [] (unknown:0) - When loading module  "DICOM" , the dependency "SubjectHierarchy" failed to be loaded.
[WARNING][Qt] 13.08.2018 14:08:28 [] (unknown:0) - When loading module  "DICOM" , the dependency "SubjectHierarchy" failed to be loaded.
[WARNING][Qt] 13.08.2018 14:08:28 [] (unknown:0) - When loading module  "DICOMPatcher" , the dependency "DICOM" failed to be loaded.
[WARNING][Qt] 13.08.2018 14:08:29 [] (unknown:0) - When loading module  "MarkupsWidgetsSelfTest" , the dependency "Markups" failed to be loaded.
[WARNING][Qt] 13.08.2018 14:08:29 [] (unknown:0) - When loading module  "MultiVolumeImporter" , the dependency "MultiVolumeExplorer" failed to be loaded.
[WARNING][Qt] 13.08.2018 14:08:29 [] (unknown:0) - When loading module  "NeurosurgicalPlanningTutorialMarkupsSelfTest" , the dependency "Segmentations" failed to be loaded.
[WARNING][Qt] 13.08.2018 14:08:29 [] (unknown:0) - When loading module  "PlotsSelfTest" , the dependency "Plots" failed to be loaded.
[WARNING][Qt] 13.08.2018 14:08:29 [] (unknown:0) - When loading module  "SegmentEditor" , the dependency "Segmentations" failed to be loaded.
[WARNING][Qt] 13.08.2018 14:08:29 [] (unknown:0) - When loading module  "SegmentStatistics" , the dependency "SubjectHierarchy" failed to be loaded.
[WARNING][Qt] 13.08.2018 14:08:29 [] (unknown:0) - When loading module  "SubjectHierarchyCorePluginsSelfTest" , the dependency "SubjectHierarchy" failed to be loaded.
[WARNING][Qt] 13.08.2018 14:08:29 [] (unknown:0) - When loading module  "SubjectHierarchyGenericSelfTest" , the dependency "SubjectHierarchy" failed to be loaded.
[WARNING][Qt] 13.08.2018 14:08:29 [] (unknown:0) - When loading module  "TablesSelfTest" , the dependency "Tables" failed to be loaded.
[WARNING][Python] 13.08.2018 14:08:30 [Python] (C:\Program Files\Slicer 4.9.0-2018-08-10\lib\Slicer-4.9\qt-scripted-modules\DataProbeLib\SliceViewAnnotations.py:26) - SliceAnnotations: Disable features relying on vtkPVScalarBarActor
[INFO][Stream] 13.08.2018 14:08:30 [] (unknown:0) - starting storescp process
[INFO][Stream] 13.08.2018 14:08:30 [] (unknown:0) - (u'Starting C:/Program Files/Slicer 4.9.0-2018-08-10/bin/../bin\\storescp.exe with ', ['11112', '--accept-all', '--output-directory', u'C:\\Users\\mk02\\Documents\\SlicerDICOMDatabase/incoming', '--exec-sync', '--exec-on-reception', u'C:/Program Files/Slicer 4.9.0-2018-08-10/bin/../bin\\dcmdump.exe --load-short --print-short --print-filename --search PatientName "C:\\Users\\mk02\\Documents\\SlicerDICOMDatabase/incoming/#f"'])
[INFO][Stream] 13.08.2018 14:08:30 [] (unknown:0) - process C:/Program Files/Slicer 4.9.0-2018-08-10/bin/../bin\storescp.exe now in state Starting
[INFO][Stream] 13.08.2018 14:08:30 [] (unknown:0) - process C:/Program Files/Slicer 4.9.0-2018-08-10/bin/../bin\storescp.exe now in state Running
[CRITICAL][Stream] 13.08.2018 14:08:30 [] (unknown:0) - SliceAnnotations: Disable features relying on vtkPVScalarBarActor
</code></pre>
<p>Best wishes,<br>
Miki</p>

---

## Post #4 by @cpinter (2018-08-13 14:57 UTC)

<p>Can you please try a recent nightly version? 4.8.1 is quite old now and there have been profound changes in the new version you might like. We’re very close to releasing 4.10, so it should be pretty stable.</p>

---

## Post #5 by @kadohisa (2018-08-13 15:06 UTC)

<p>Thank you for your suggestion.</p>
<p>I’ll wait for the new version, then I may contact you if the current problem is not sorted out.</p>
<p>Best wishes,</p>
<p>Miki</p>

---

## Post #6 by @cpinter (2018-08-13 15:18 UTC)

<p>Please note that most people already use the nightly. It is generally safe to do so anyway, but now especially before the release.</p>

---

## Post #7 by @pieper (2018-08-13 15:21 UTC)

<p><a class="mention" href="/u/kadohisa">@kadohisa</a> based on the log file you posted it looks like your installation has gotten corrupted somehow - you could try re-installing 4.8.1 if you want to stick with that version.  But as <a class="mention" href="/u/cpinter">@cpinter</a> says, the nightly version is improved and is pretty stable these days.</p>

---

## Post #8 by @lassoan (2018-08-14 07:30 UTC)

<p>Also make sure you don’t have any contamination in your system or user environment (such as path of Python.exe added to system PATH), or Python or other applications installed in your system folders. See detailed instructions here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Troubleshooting#Debugging_Slicer_application_startup_issues">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Troubleshooting#Debugging_Slicer_application_startup_issues</a></p>

---

## Post #9 by @kadohisa (2018-08-14 12:27 UTC)

<p>Thank you very much for your information.</p>
<p>My Slicer settings were corrupted as you’ve thought.<br>
Now, I have a module, ‘Welcome to Slicer’, and upload DICOM data.</p>
<p>I’m a very beginner to learn to use Slicer.<br>
What I’d like to do with Slicer is reconstruct the skull surface with<br>
MRI data.<br>
However, I’m not sure what data actually I need for it.<br>
Once DICOM files (structure &amp; bone) are uploaded in Slicer, the data<br>
files which are required to produce skull surface are automatically<br>
produced?</p>
<p>I’d appreciate it if you’d let me know what I should do to get skulls of<br>
my subjects.</p>
<p>Best wishes,</p>
<p>Miki</p>

---

## Post #10 by @pieper (2018-08-14 12:54 UTC)

<p>Glad you got the installation working <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=5" title=":smile:" class="emoji" alt=":smile:"></p>
<p>As you probably know, bones in general and the skull in particular don’t show up well in typical MR sequences.  If you google for synthetic CT from MR you will find a lot of literature about how to estimate the bone from just the MR (it’s used for RT planning for example). I don’t know if anyone has slicer-compatible tools available.</p>

---

## Post #11 by @kadohisa (2018-08-14 13:26 UTC)

<p>I’ve seen MR Head in Sample Data.<br>
That is why I’ve thought skull would be able to be reconstructed in Slicer.</p>
<p>I’ve just simply thought it would be great if DICOM data uploded in Slicer are automatically converted to the files whice are required to reconstruct the skull.<br>
If not, I wonder if there are someone know how to produce those files.</p>
<p>Best wishes,</p>
<p>Miki</p>

---

## Post #12 by @saba.rn (2021-10-06 00:29 UTC)

<p>Hi Dear,<br>
Can you please mention how you solved this problem? I cannot see the welcome module anymore in any version I install.<br>
Thank you!</p>

---

## Post #13 by @lassoan (2021-10-06 12:27 UTC)

<p>What module do your see when you start Slicer?</p>

---
