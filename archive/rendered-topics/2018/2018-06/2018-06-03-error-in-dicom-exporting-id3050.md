# Error in DICOM Exporting

**Topic ID**: 3050
**Date**: 2018-06-03
**URL**: https://discourse.slicer.org/t/error-in-dicom-exporting/3050

---

## Post #1 by @Stefania_Julian (2018-06-03 00:53 UTC)

<p>Operating system: Mac IOS<br>
Slicer version: 4.8.1 r26813<br>
Expected behavior:<br>
Actual behavior: Error occured in exporter.<br>
Hello Im new in Slicer. Im trying to export TAC images I modified in Slicer. I need them in DICOM extension for another planning software. When I try to export them, the sign “Error occured in exporter.” If you could help me I would be very glad.</p>

---

## Post #2 by @lassoan (2018-06-03 00:54 UTC)

<p>Could you please send the application log (menu: Help / Report a bug) of a session where you attempted the export?</p>

---

## Post #3 by @Stefania_Julian (2018-06-03 15:33 UTC)

<p>Is this what you refer to?</p>
<p>[DEBUG][Qt] 03.06.2018 12:20:25 [] (unknown:0) - Session start time …: 2018-06-03 12:20:25<br>
[DEBUG][Qt] 03.06.2018 12:20:25 [] (unknown:0) - Slicer version …: 4.8.1 (revision 26813) macosx-amd64 - installed<br>
[DEBUG][Qt] 03.06.2018 12:20:25 [] (unknown:0) - Operating system …: Mac OS X / 10.13.4 / 17E199 - 64-bit<br>
[DEBUG][Qt] 03.06.2018 12:20:25 [] (unknown:0) - Memory …: 4096 MB physical, 1024 MB virtual<br>
[DEBUG][Qt] 03.06.2018 12:20:25 [] (unknown:0) - CPU …: GenuineIntel Intel® Core™ i5-5250U CPU @ 1.60GHz, 2 cores, 4 logical processors<br>
[DEBUG][Qt] 03.06.2018 12:20:25 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 03.06.2018 12:20:25 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 03.06.2018 12:20:25 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 03.06.2018 12:20:32 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
[DEBUG][Python] 03.06.2018 12:20:40 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 03.06.2018 12:20:41 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 03.06.2018 12:20:41 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 03.06.2018 12:20:30 [] (unknown:0) - Number of registered modules: 135<br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -   File “”, line 1, in <br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/ExtensionWizard.py”, line 7, in <br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -     import SlicerWizard.ExtensionDescription<br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/SlicerWizard/<strong>init</strong>.py”, line 42, in <br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -     from .ExtensionDescription import ExtensionDescription<br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/SlicerWizard/ExtensionDescription.py”, line 6, in <br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -     from .ExtensionProject import ExtensionProject<br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/SlicerWizard/ExtensionProject.py”, line 6, in <br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -     from .Utilities import detectEncoding<br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/SlicerWizard/Utilities.py”, line 10, in <br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -     import git<br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/<strong>init</strong>.py”, line 82, in <br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -     refresh()<br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/<strong>init</strong>.py”, line 73, in refresh<br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -     if not Git.refresh(path=path):<br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/cmd.py”, line 230, in refresh<br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -     cls().version()<br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/cmd.py”, line 551, in <br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -     return lambda *args, **kwargs: self._call_process(name, *args, **kwargs)<br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/cmd.py”, line 1010, in _call_process<br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -     return self.execute(call, **exec_kwargs)<br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/cmd.py”, line 821, in execute<br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -     raise GitCommandError(command, status, stderr_value, stdout_value)<br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) - git.exc.GitCommandError: Cmd(‘git’) failed due to: exit code(1)<br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -   cmdline: git version<br>
[CRITICAL][Stream] 03.06.2018 12:20:32 [] (unknown:0) -   stderr: ‘xcode-select: note: no developer tools were found at ‘/Applications/Xcode.app’, requesting install. Choose an option in the dialog to download the command line developer tools.’<br>
[CRITICAL][Qt] 03.06.2018 12:20:32 [] (unknown:0) - loadSourceAsModule - Failed to load file “/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/ExtensionWizard.py”  as module “ExtensionWizard” !<br>
[CRITICAL][Qt] 03.06.2018 12:20:32 [] (unknown:0) - Fail to instantiate module  “ExtensionWizard”<br>
[DEBUG][Qt] 03.06.2018 12:20:33 [] (unknown:0) - Number of instantiated modules: 134<br>
[DEBUG][Qt] 03.06.2018 12:20:41 [] (unknown:0) - Number of loaded modules: 134<br>
[DEBUG][Qt] 03.06.2018 12:20:41 [] (unknown:0) - Switch to module:  “Welcome”<br>
[CRITICAL][FD] 03.06.2018 12:20:52 [] (unknown:0) - 2018-06-03 12:20:52.076 Slicer[657:11674] modalSession has been exited prematurely - check for a reentrant call to endModalSession:<br>
[DEBUG][Qt] 03.06.2018 12:20:55 [] (unknown:0) - Switch to module:  “DICOM”<br>
[DEBUG][Python] 03.06.2018 12:21:05 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py:449) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 03.06.2018 12:21:06 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py:489) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[DEBUG][Python] 03.06.2018 12:21:06 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py:162) - MultiVolumeImportPlugin:examineMultiseries<br>
[DEBUG][Python] 03.06.2018 12:21:06 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py:167) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[INFO][Python] 03.06.2018 12:21:06 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:422) - Loading with imageIOName: GDCM<br>
[INFO][Python] 03.06.2018 12:21:20 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:494) - Window/level found in DICOM tags (center=350.0, width=2700.0) has been applied to volume 4: TAC Altamirano1<br>
[WARNING][Python] 03.06.2018 12:21:21 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:799) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 0.000404771 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 03.06.2018 12:21:06 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 03.06.2018 12:21:20 [] (unknown:0) - Window/level found in DICOM tags (center=350.0, width=2700.0) has been applied to volume 4: TAC Altamirano1<br>
[CRITICAL][Stream] 03.06.2018 12:21:21 [] (unknown:0) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 0.000404771 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 03.06.2018 12:21:26 [] (unknown:0) - selected row 0<br>
[INFO][Stream] 03.06.2018 12:21:26 [] (unknown:0) - Today: TAC Altamirano1 for ALTAMIRANO ^DANIELA ANABEL<br>
[INFO][Stream] 03.06.2018 12:22:03 [] (unknown:0) - selected row 0<br>
[INFO][Stream] 03.06.2018 12:22:03 [] (unknown:0) - Today: TAC Altamirano1 for ALTAMIRANO ^DANIELA ANABEL<br>
[INFO][Stream] 03.06.2018 12:22:07 [] (unknown:0) - selected row 0<br>
[INFO][Stream] 03.06.2018 12:22:07 [] (unknown:0) - Today: TAC Altamirano1 for ALTAMIRANO ^DANIELA ANABEL<br>
[INFO][Stream] 03.06.2018 12:22:27 [] (unknown:0) - starting storescp process<br>
[INFO][Stream] 03.06.2018 12:22:27 [] (unknown:0) - (u’Starting /Applications/Slicer.app/Contents/bin/storescp with ‘, [‘11112’, ‘–accept-all’, ‘–output-directory’, u’/Users/stefania/Documents/SlicerDICOMDatabase/incoming’, ‘–exec-sync’, ‘–exec-on-reception’, u’/Applications/Slicer.app/Contents/bin/dcmdump --load-short --print-short --print-filename --search PatientName “/Users/stefania/Documents/SlicerDICOMDatabase/incoming/<span class="hashtag">#f</span>”’])<br>
[INFO][Stream] 03.06.2018 12:22:27 [] (unknown:0) - process /Applications/Slicer.app/Contents/bin/storescp now in state Starting<br>
[INFO][Stream] 03.06.2018 12:22:27 [] (unknown:0) - process /Applications/Slicer.app/Contents/bin/storescp now in state Running<br>
[INFO][Stream] 03.06.2018 12:22:28 [] (unknown:0) - stopping DICOM process<br>
[WARNING][Qt] 03.06.2018 12:22:28 [] (unknown:0) - QProcess: Destroyed while process is still running.<br>
[INFO][Stream] 03.06.2018 12:22:28 [] (unknown:0) - process /Applications/Slicer.app/Contents/bin/storescp now in state NotRunning<br>
[CRITICAL][Stream] 03.06.2018 12:22:28 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 03.06.2018 12:22:28 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOM.py”, line 395, in onToggleListener<br>
[CRITICAL][Stream] 03.06.2018 12:22:28 [] (unknown:0) -     del slicer.dicomListener<br>
[CRITICAL][Stream] 03.06.2018 12:22:28 [] (unknown:0) - AttributeError: dicomListener<br>
[INFO][Stream] 03.06.2018 12:22:38 [] (unknown:0) - selected row 0<br>
[INFO][Stream] 03.06.2018 12:22:38 [] (unknown:0) - Today: TAC Altamirano1 for ALTAMIRANO ^DANIELA ANABEL<br>
[INFO][Stream] 03.06.2018 12:22:44 [] (unknown:0) - selected row 0<br>
[INFO][Stream] 03.06.2018 12:22:44 [] (unknown:0) - Today: TAC Altamirano1 for ALTAMIRANO ^DANIELA ANABEL<br>
[INFO][Python] 03.06.2018 12:22:52 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:601) - Export scalar volume ‘4: TAC Altamirano1’ to directory /var/folders/02/xlz1btn17819djv59_ntjzqm0000gn/T/Slicer-stefania/DICOMExportTemp_20180603_122252/ScalarVolume_7<br>
[INFO][Stream] 03.06.2018 12:22:52 [] (unknown:0) - Export scalar volume ‘4: TAC Altamirano1’ to directory /var/folders/02/xlz1btn17819djv59_ntjzqm0000gn/T/Slicer-stefania/DICOMExportTemp_20180603_122252/ScalarVolume_7<br>
[CRITICAL][Stream] 03.06.2018 12:22:52 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 03.06.2018 12:22:52 [] (unknown:0) -   File “”, line 2, in <br>
[CRITICAL][Stream] 03.06.2018 12:22:52 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 638, in export<br>
[CRITICAL][Stream] 03.06.2018 12:22:52 [] (unknown:0) -     exporter.export()<br>
[CRITICAL][Stream] 03.06.2018 12:22:52 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMLib/DICOMExportScalarVolume.py”, line 128, in export<br>
[CRITICAL][Stream] 03.06.2018 12:22:52 [] (unknown:0) -     cliNode = slicer.cli.run(dicomWrite, None, cliparameters, wait_for_completion=True)<br>
[CRITICAL][Stream] 03.06.2018 12:22:52 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/slicer/cli.py”, line 71, in run<br>
[CRITICAL][Stream] 03.06.2018 12:22:52 [] (unknown:0) -     node = createNode(module, parameters)<br>
[CRITICAL][Stream] 03.06.2018 12:22:52 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/slicer/cli.py”, line 13, in createNode<br>
[CRITICAL][Stream] 03.06.2018 12:22:52 [] (unknown:0) -     setNodeParameters(node, parameters)<br>
[CRITICAL][Stream] 03.06.2018 12:22:52 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/slicer/cli.py”, line 31, in setNodeParameters<br>
[CRITICAL][Stream] 03.06.2018 12:22:52 [] (unknown:0) -     node.SetParameterAsString(key, value)<br>
[CRITICAL][Stream] 03.06.2018 12:22:52 [] (unknown:0) - TypeError: SetParameterAsString argument 2: (unicode conversion error)<br>
[INFO][Python] 03.06.2018 12:23:26 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMLib/DICOMExportScene.py:42) - Saving Image…<br>
[INFO][Python] 03.06.2018 12:23:26 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMLib/DICOMExportScene.py:42) - Saving Scene…<br>
[INFO][Python] 03.06.2018 12:25:31 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMLib/DICOMExportScene.py:42) - Making zip…<br>
[INFO][Python] 03.06.2018 12:25:33 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMLib/DICOMExportScene.py:42) - Making dicom reference file…<br>
[INFO][Stream] 03.06.2018 12:23:26 [] (unknown:0) - Saving Image…<br>
[WARNING][Qt] 03.06.2018 12:23:26 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile<br>
[INFO][Stream] 03.06.2018 12:23:26 [] (unknown:0) - 0<br>
[INFO][Stream] 03.06.2018 12:23:26 [] (unknown:0) - something is none<br>
[INFO][Stream] 03.06.2018 12:23:26 [] (unknown:0) - 1<br>
[INFO][Stream] 03.06.2018 12:23:26 [] (unknown:0) - something is none<br>
[INFO][Stream] 03.06.2018 12:23:26 [] (unknown:0) - 2<br>
[INFO][Stream] 03.06.2018 12:23:26 [] (unknown:0) - something is none<br>
[INFO][Stream] 03.06.2018 12:23:26 [] (unknown:0) - Saving Scene…<br>
[INFO][Stream] 03.06.2018 12:25:31 [] (unknown:0) - Making zip…<br>
[INFO][VTK] 03.06.2018 12:25:31 [] (unknown:0) - Info: In /Users/kitware/Dashboards/Package/Slicer-481/Libs/MRML/Logic/vtkArchive.cxx, line 35<br>
Zip: adding: /var/folders/02/xlz1btn17819djv59_ntjzqm0000gn/T/Slicer-stefania/dicomExportEnVKb8/scene/scene.mrml<br>
[INFO][VTK] 03.06.2018 12:25:31 [] (unknown:0) - Info: In /Users/kitware/Dashboards/Package/Slicer-481/Libs/MRML/Logic/vtkArchive.cxx, line 35<br>
Zip: adding rel: scene/scene.mrml<br>
[INFO][VTK] 03.06.2018 12:25:31 [] (unknown:0) - Info: In /Users/kitware/Dashboards/Package/Slicer-481/Libs/MRML/Logic/vtkArchive.cxx, line 35<br>
Zip: adding: /var/folders/02/xlz1btn17819djv59_ntjzqm0000gn/T/Slicer-stefania/dicomExportEnVKb8/scene/Data/4%3a%20TAC%20Altamirano1.nrrd<br>
[INFO][VTK] 03.06.2018 12:25:31 [] (unknown:0) - Info: In /Users/kitware/Dashboards/Package/Slicer-481/Libs/MRML/Logic/vtkArchive.cxx, line 35<br>
Zip: adding rel: scene/Data/4%3a%20TAC%20Altamirano1.nrrd<br>
[INFO][VTK] 03.06.2018 12:25:33 [] (unknown:0) - Info: In /Users/kitware/Dashboards/Package/Slicer-481/Libs/MRML/Logic/vtkArchive.cxx, line 35<br>
Zip: adding: /var/folders/02/xlz1btn17819djv59_ntjzqm0000gn/T/Slicer-stefania/dicomExportEnVKb8/scene/Slicer Data Bundle Scene View.png<br>
[INFO][VTK] 03.06.2018 12:25:33 [] (unknown:0) - Info: In /Users/kitware/Dashboards/Package/Slicer-481/Libs/MRML/Logic/vtkArchive.cxx, line 35<br>
Zip: adding rel: scene/Slicer Data Bundle Scene View.png<br>
[INFO][Stream] 03.06.2018 12:25:33 [] (unknown:0) - Making dicom reference file…<br>
[INFO][Stream] 03.06.2018 12:25:33 [] (unknown:0) - (‘running: ‘, u’/Applications/Slicer.app/Contents/bin/dcmdump’, [’–print-all’, ‘–write-pixel’, u’/var/folders/02/xlz1btn17819djv59_ntjzqm0000gn/T/Slicer-stefania/dicomExportEnVKb8’, u’/Users/stefania/Documents/OsiriX Data/DATABASE.noindex/20000/17349.dcm’])<br>
[INFO][Stream] 03.06.2018 12:25:33 [] (unknown:0) - stopping DICOM process<br>
[CRITICAL][Stream] 03.06.2018 12:25:33 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 03.06.2018 12:25:33 [] (unknown:0) -   File “”, line 3, in <br>
[CRITICAL][Stream] 03.06.2018 12:25:33 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMLib/DICOMExportScene.py”, line 46, in export<br>
[CRITICAL][Stream] 03.06.2018 12:25:33 [] (unknown:0) -     success = self.createDICOMFileForScene()<br>
[CRITICAL][Stream] 03.06.2018 12:25:33 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMLib/DICOMExportScene.py”, line 163, in createDICOMFileForScene<br>
[CRITICAL][Stream] 03.06.2018 12:25:33 [] (unknown:0) -     dump = str(dump) + candygram<br>
[CRITICAL][Stream] 03.06.2018 12:25:33 [] (unknown:0) - UnicodeDecodeError: ‘ascii’ codec can’t decode byte 0xc1 in position 2477: ordinal not in range(128)<br>
[CRITICAL][FD] 03.06.2018 12:31:42 [] (unknown:0) - 2018-06-03 12:31:42.452 Slicer[657:11674] modalSession has been exited prematurely - check for a reentrant call to endModalSession:</p>

---

## Post #4 by @pieper (2018-06-03 15:54 UTC)

<p>It looks like you are trying to export the entire scene, but it’s running into an error possibly related to a non-ascii character.</p>
<p>But in any case, you probably don’t want to export the full scene because that will create a Slicer-specific file (technically it’s a secondary capture object that can be moved around as DICOM, but only another Slicer instance will be able to open the data from the private tags).</p>
<p>Since your goal is to send the modified data to another system, you should export the volume as a new series.  Be sure it is associated with a subject and study in the subject hierarchy.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export</a></p>

---

## Post #5 by @Stefania_Julian (2018-06-03 16:05 UTC)

<p>I did that, but it is not working.<br>
[DEBUG][Qt] 03.06.2018 12:57:30 [] (unknown:0) - Session start time …: 2018-06-03 12:57:30<br>
[DEBUG][Qt] 03.06.2018 12:57:30 [] (unknown:0) - Slicer version …: 4.8.1 (revision 26813) macosx-amd64 - installed<br>
[DEBUG][Qt] 03.06.2018 12:57:30 [] (unknown:0) - Operating system …: Mac OS X / 10.13.4 / 17E199 - 64-bit<br>
[DEBUG][Qt] 03.06.2018 12:57:30 [] (unknown:0) - Memory …: 4096 MB physical, 1024 MB virtual<br>
[DEBUG][Qt] 03.06.2018 12:57:30 [] (unknown:0) - CPU …: GenuineIntel Intel® Core™ i5-5250U CPU @ 1.60GHz, 2 cores, 4 logical processors<br>
[DEBUG][Qt] 03.06.2018 12:57:30 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 03.06.2018 12:57:30 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 03.06.2018 12:57:30 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 03.06.2018 12:57:38 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
[DEBUG][Python] 03.06.2018 12:57:46 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 03.06.2018 12:57:47 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 03.06.2018 12:57:47 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 03.06.2018 12:57:36 [] (unknown:0) - Number of registered modules: 135<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “”, line 1, in <br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/ExtensionWizard.py”, line 7, in <br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     import SlicerWizard.ExtensionDescription<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/SlicerWizard/<strong>init</strong>.py”, line 42, in <br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     from .ExtensionDescription import ExtensionDescription<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/SlicerWizard/ExtensionDescription.py”, line 6, in <br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     from .ExtensionProject import ExtensionProject<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/SlicerWizard/ExtensionProject.py”, line 6, in <br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     from .Utilities import detectEncoding<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/SlicerWizard/Utilities.py”, line 10, in <br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     import git<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/<strong>init</strong>.py”, line 82, in <br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     refresh()<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/<strong>init</strong>.py”, line 73, in refresh<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     if not Git.refresh(path=path):<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/cmd.py”, line 230, in refresh<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     cls().version()<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/cmd.py”, line 551, in <br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     return lambda *args, **kwargs: self._call_process(name, *args, **kwargs)<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/cmd.py”, line 1010, in _call_process<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     return self.execute(call, **exec_kwargs)<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/cmd.py”, line 821, in execute<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     raise GitCommandError(command, status, stderr_value, stdout_value)<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) - git.exc.GitCommandError: Cmd(‘git’) failed due to: exit code(1)<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   cmdline: git version<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   stderr: ‘xcode-select: note: no developer tools were found at ‘/Applications/Xcode.app’, requesting install. Choose an option in the dialog to download the command line developer tools.’<br>
[CRITICAL][Qt] 03.06.2018 12:57:38 [] (unknown:0) - loadSourceAsModule - Failed to load file “/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/ExtensionWizard.py”  as module “ExtensionWizard” !<br>
[CRITICAL][Qt] 03.06.2018 12:57:38 [] (unknown:0) - Fail to instantiate module  “ExtensionWizard”<br>
[DEBUG][Qt] 03.06.2018 12:57:38 [] (unknown:0) - Number of instantiated modules: 134<br>
[DEBUG][Qt] 03.06.2018 12:57:47 [] (unknown:0) - Number of loaded modules: 134<br>
[DEBUG][Qt] 03.06.2018 12:57:47 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 03.06.2018 12:58:27 [] (unknown:0) - Switch to module:  “DICOM”<br>
[DEBUG][Python] 03.06.2018 12:58:36 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py:449) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 03.06.2018 12:58:37 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py:489) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[DEBUG][Python] 03.06.2018 12:58:38 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py:162) - MultiVolumeImportPlugin:examineMultiseries<br>
[DEBUG][Python] 03.06.2018 12:58:38 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py:167) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[INFO][Python] 03.06.2018 12:58:38 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:422) - Loading with imageIOName: GDCM<br>
[INFO][Python] 03.06.2018 12:58:57 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:494) - Window/level found in DICOM tags (center=350.0, width=2700.0) has been applied to volume 4: TAC Altamirano1<br>
[WARNING][Python] 03.06.2018 12:58:59 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:799) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 0.000404771 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 03.06.2018 12:58:38 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 03.06.2018 12:58:57 [] (unknown:0) - Window/level found in DICOM tags (center=350.0, width=2700.0) has been applied to volume 4: TAC Altamirano1<br>
[CRITICAL][Stream] 03.06.2018 12:58:59 [] (unknown:0) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 0.000404771 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 03.06.2018 12:59:30 [] (unknown:0) - selected row 0<br>
[INFO][Stream] 03.06.2018 12:59:30 [] (unknown:0) - Today: TAC Altamirano1 for ALTAMIRANO ^DANIELA ANABEL<br>
[INFO][Stream] 03.06.2018 13:00:12 [] (unknown:0) - starting storescp process<br>
[INFO][Stream] 03.06.2018 13:00:12 [] (unknown:0) - (u’Starting /Applications/Slicer.app/Contents/bin/storescp with ‘, [‘11112’, ‘–accept-all’, ‘–output-directory’, u’/Users/stefania/Documents/SlicerDICOMDatabase/incoming’, ‘–exec-sync’, ‘–exec-on-reception’, u’/Applications/Slicer.app/Contents/bin/dcmdump --load-short --print-short --print-filename --search PatientName “/Users/stefania/Documents/SlicerDICOMDatabase/incoming/<span class="hashtag">#f</span>”’])<br>
[INFO][Stream] 03.06.2018 13:00:12 [] (unknown:0) - process /Applications/Slicer.app/Contents/bin/storescp now in state Starting<br>
[INFO][Stream] 03.06.2018 13:00:12 [] (unknown:0) - process /Applications/Slicer.app/Contents/bin/storescp now in state Running<br>
[DEBUG][Python] 03.06.2018 13:00:23 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py:449) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 03.06.2018 13:00:26 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py:489) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[DEBUG][Python] 03.06.2018 13:00:26 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py:162) - MultiVolumeImportPlugin:examineMultiseries<br>
[DEBUG][Python] 03.06.2018 13:00:26 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py:167) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[INFO][Python] 03.06.2018 13:00:26 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:422) - Loading with imageIOName: GDCM<br>
[INFO][Python] 03.06.2018 13:00:43 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:494) - Window/level found in DICOM tags (center=350.0, width=2700.0) has been applied to volume 4: TAC Altamirano1_1<br>
[WARNING][Python] 03.06.2018 13:00:44 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:799) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 0.000404771 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 03.06.2018 13:00:26 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 03.06.2018 13:00:43 [] (unknown:0) - Window/level found in DICOM tags (center=350.0, width=2700.0) has been applied to volume 4: TAC Altamirano1_1<br>
[CRITICAL][Stream] 03.06.2018 13:00:44 [] (unknown:0) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 0.000404771 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 03.06.2018 13:01:00 [] (unknown:0) - stopping DICOM process<br>
[WARNING][Qt] 03.06.2018 13:01:00 [] (unknown:0) - QProcess: Destroyed while process is still running.<br>
[INFO][Stream] 03.06.2018 13:01:00 [] (unknown:0) - process /Applications/Slicer.app/Contents/bin/storescp now in state NotRunning<br>
[CRITICAL][Stream] 03.06.2018 13:01:00 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 03.06.2018 13:01:00 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOM.py”, line 395, in onToggleListener<br>
[CRITICAL][Stream] 03.06.2018 13:01:00 [] (unknown:0) -     del slicer.dicomListener<br>
[CRITICAL][Stream] 03.06.2018 13:01:00 [] (unknown:0) - AttributeError: dicomListener<br>
[CRITICAL][FD] 03.06.2018 13:01:15 [] (unknown:0) - 2018-06-03 13:01:15.433 Slicer[790:59302] modalSession has been exited prematurely - check for a reentrant call to endModalSession:<br>
[DEBUG][Qt] 03.06.2018 13:01:47 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[DEBUG][Qt] 03.06.2018 13:01:58 [] (unknown:0) - Switch to module:  “Models”<br>
[DEBUG][Qt] 03.06.2018 13:02:02 [] (unknown:0) - Switch to module:  “Volumes”<br>
[WARNING][Qt] 03.06.2018 13:02:02 [] (unknown:0) - ctkDoubleRangeSlider::setSingleStep( 100 ) is outside of valid bounds.<br>
[WARNING][Qt] 03.06.2018 13:02:02 [] (unknown:0) - ctkRangeWidget::setSingleStep( 100 ) is outside valid bounds<br>
[WARNING][Qt] 03.06.2018 13:02:07 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 03.06.2018 13:02:09 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 03.06.2018 13:02:09 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 03.06.2018 13:02:14 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 03.06.2018 13:02:14 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[DEBUG][Qt] 03.06.2018 13:02:21 [] (unknown:0) - Switch to module:  “Data”<br>
[WARNING][Qt] 03.06.2018 13:02:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[CRITICAL][FD] 03.06.2018 13:03:13 [] (unknown:0) - 2018-06-03 13:03:13.582 Slicer[790:59302] modalSession has been exited prematurely - check for a reentrant call to endModalSession:<br>
[CRITICAL][FD] 03.06.2018 13:03:35 [] (unknown:0) - 2018-06-03 13:03:35.289 Slicer[790:59302] modalSession has been exited prematurely - check for a reentrant call to endModalSession:<br>
[INFO][Python] 03.06.2018 13:04:10 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:601) - Export scalar volume ‘4: TAC Altamirano1’ to directory /var/folders/02/xlz1btn17819djv59_ntjzqm0000gn/T/Slicer-stefania/DICOMExportTemp_20180603_130410/ScalarVolume_7<br>
[INFO][Stream] 03.06.2018 13:04:10 [] (unknown:0) - Export scalar volume ‘4: TAC Altamirano1’ to directory /var/folders/02/xlz1btn17819djv59_ntjzqm0000gn/T/Slicer-stefania/DICOMExportTemp_20180603_130410/ScalarVolume_7<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -   File “”, line 2, in <br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 638, in export<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -     exporter.export()<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMLib/DICOMExportScalarVolume.py”, line 128, in export<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -     cliNode = slicer.cli.run(dicomWrite, None, cliparameters, wait_for_completion=True)<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/slicer/cli.py”, line 71, in run<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -     node = createNode(module, parameters)<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/slicer/cli.py”, line 13, in createNode<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -     setNodeParameters(node, parameters)<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/slicer/cli.py”, line 31, in setNodeParameters<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -     node.SetParameterAsString(key, value)<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) - TypeError: SetParameterAsString argument 2: (unicode conversion error)<br>
[CRITICAL][FD] 03.06.2018 13:04:17 [] (unknown:0) - 2018-06-03 13:04:17.102 Slicer[790:59302] modalSession has been exited prematurely - check for a reentrant call to endModalSession:</p>

---

## Post #6 by @Stefania_Julian (2018-06-03 16:51 UTC)

<p>I tried to do that, but algo Error comes out.<br>
[DEBUG][Qt] 03.06.2018 12:57:30 [] (unknown:0) - Session start time …: 2018-06-03 12:57:30<br>
[DEBUG][Qt] 03.06.2018 12:57:30 [] (unknown:0) - Slicer version …: 4.8.1 (revision 26813) macosx-amd64 - installed<br>
[DEBUG][Qt] 03.06.2018 12:57:30 [] (unknown:0) - Operating system …: Mac OS X / 10.13.4 / 17E199 - 64-bit<br>
[DEBUG][Qt] 03.06.2018 12:57:30 [] (unknown:0) - Memory …: 4096 MB physical, 1024 MB virtual<br>
[DEBUG][Qt] 03.06.2018 12:57:30 [] (unknown:0) - CPU …: GenuineIntel Intel® Core™ i5-5250U CPU @ 1.60GHz, 2 cores, 4 logical processors<br>
[DEBUG][Qt] 03.06.2018 12:57:30 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 03.06.2018 12:57:30 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 03.06.2018 12:57:30 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 03.06.2018 12:57:38 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
[DEBUG][Python] 03.06.2018 12:57:46 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 03.06.2018 12:57:47 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 03.06.2018 12:57:47 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 03.06.2018 12:57:36 [] (unknown:0) - Number of registered modules: 135<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “”, line 1, in <br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/ExtensionWizard.py”, line 7, in <br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     import SlicerWizard.ExtensionDescription<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/SlicerWizard/<strong>init</strong>.py”, line 42, in <br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     from .ExtensionDescription import ExtensionDescription<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/SlicerWizard/ExtensionDescription.py”, line 6, in <br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     from .ExtensionProject import ExtensionProject<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/SlicerWizard/ExtensionProject.py”, line 6, in <br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     from .Utilities import detectEncoding<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/SlicerWizard/Utilities.py”, line 10, in <br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     import git<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/<strong>init</strong>.py”, line 82, in <br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     refresh()<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/<strong>init</strong>.py”, line 73, in refresh<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     if not Git.refresh(path=path):<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/cmd.py”, line 230, in refresh<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     cls().version()<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/cmd.py”, line 551, in <br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     return lambda *args, **kwargs: self._call_process(name, *args, **kwargs)<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/cmd.py”, line 1010, in _call_process<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     return self.execute(call, **exec_kwargs)<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/git/cmd.py”, line 821, in execute<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -     raise GitCommandError(command, status, stderr_value, stdout_value)<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) - git.exc.GitCommandError: Cmd(‘git’) failed due to: exit code(1)<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   cmdline: git version<br>
[CRITICAL][Stream] 03.06.2018 12:57:38 [] (unknown:0) -   stderr: ‘xcode-select: note: no developer tools were found at ‘/Applications/Xcode.app’, requesting install. Choose an option in the dialog to download the command line developer tools.’<br>
[CRITICAL][Qt] 03.06.2018 12:57:38 [] (unknown:0) - loadSourceAsModule - Failed to load file “/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/ExtensionWizard.py”  as module “ExtensionWizard” !<br>
[CRITICAL][Qt] 03.06.2018 12:57:38 [] (unknown:0) - Fail to instantiate module  “ExtensionWizard”<br>
[DEBUG][Qt] 03.06.2018 12:57:38 [] (unknown:0) - Number of instantiated modules: 134<br>
[DEBUG][Qt] 03.06.2018 12:57:47 [] (unknown:0) - Number of loaded modules: 134<br>
[DEBUG][Qt] 03.06.2018 12:57:47 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 03.06.2018 12:58:27 [] (unknown:0) - Switch to module:  “DICOM”<br>
[DEBUG][Python] 03.06.2018 12:58:36 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py:449) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 03.06.2018 12:58:37 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py:489) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[DEBUG][Python] 03.06.2018 12:58:38 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py:162) - MultiVolumeImportPlugin:examineMultiseries<br>
[DEBUG][Python] 03.06.2018 12:58:38 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py:167) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[INFO][Python] 03.06.2018 12:58:38 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:422) - Loading with imageIOName: GDCM<br>
[INFO][Python] 03.06.2018 12:58:57 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:494) - Window/level found in DICOM tags (center=350.0, width=2700.0) has been applied to volume 4: TAC Altamirano1<br>
[WARNING][Python] 03.06.2018 12:58:59 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:799) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 0.000404771 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 03.06.2018 12:58:38 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 03.06.2018 12:58:57 [] (unknown:0) - Window/level found in DICOM tags (center=350.0, width=2700.0) has been applied to volume 4: TAC Altamirano1<br>
[CRITICAL][Stream] 03.06.2018 12:58:59 [] (unknown:0) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 0.000404771 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 03.06.2018 12:59:30 [] (unknown:0) - selected row 0<br>
[INFO][Stream] 03.06.2018 12:59:30 [] (unknown:0) - Today: TAC Altamirano1 for ALTAMIRANO ^DANIELA ANABEL<br>
[INFO][Stream] 03.06.2018 13:00:12 [] (unknown:0) - starting storescp process<br>
[INFO][Stream] 03.06.2018 13:00:12 [] (unknown:0) - (u’Starting /Applications/Slicer.app/Contents/bin/storescp with ‘, [‘11112’, ‘–accept-all’, ‘–output-directory’, u’/Users/stefania/Documents/SlicerDICOMDatabase/incoming’, ‘–exec-sync’, ‘–exec-on-reception’, u’/Applications/Slicer.app/Contents/bin/dcmdump --load-short --print-short --print-filename --search PatientName “/Users/stefania/Documents/SlicerDICOMDatabase/incoming/<span class="hashtag">#f</span>”’])<br>
[INFO][Stream] 03.06.2018 13:00:12 [] (unknown:0) - process /Applications/Slicer.app/Contents/bin/storescp now in state Starting<br>
[INFO][Stream] 03.06.2018 13:00:12 [] (unknown:0) - process /Applications/Slicer.app/Contents/bin/storescp now in state Running<br>
[DEBUG][Python] 03.06.2018 13:00:23 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py:449) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 03.06.2018 13:00:26 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py:489) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[DEBUG][Python] 03.06.2018 13:00:26 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py:162) - MultiVolumeImportPlugin:examineMultiseries<br>
[DEBUG][Python] 03.06.2018 13:00:26 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/MultiVolumeImporterPlugin.py:167) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[INFO][Python] 03.06.2018 13:00:26 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:422) - Loading with imageIOName: GDCM<br>
[INFO][Python] 03.06.2018 13:00:43 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:494) - Window/level found in DICOM tags (center=350.0, width=2700.0) has been applied to volume 4: TAC Altamirano1_1<br>
[WARNING][Python] 03.06.2018 13:00:44 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:799) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 0.000404771 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 03.06.2018 13:00:26 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 03.06.2018 13:00:43 [] (unknown:0) - Window/level found in DICOM tags (center=350.0, width=2700.0) has been applied to volume 4: TAC Altamirano1_1<br>
[CRITICAL][Stream] 03.06.2018 13:00:44 [] (unknown:0) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 0.000404771 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 03.06.2018 13:01:00 [] (unknown:0) - stopping DICOM process<br>
[WARNING][Qt] 03.06.2018 13:01:00 [] (unknown:0) - QProcess: Destroyed while process is still running.<br>
[INFO][Stream] 03.06.2018 13:01:00 [] (unknown:0) - process /Applications/Slicer.app/Contents/bin/storescp now in state NotRunning<br>
[CRITICAL][Stream] 03.06.2018 13:01:00 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 03.06.2018 13:01:00 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOM.py”, line 395, in onToggleListener<br>
[CRITICAL][Stream] 03.06.2018 13:01:00 [] (unknown:0) -     del slicer.dicomListener<br>
[CRITICAL][Stream] 03.06.2018 13:01:00 [] (unknown:0) - AttributeError: dicomListener<br>
[CRITICAL][FD] 03.06.2018 13:01:15 [] (unknown:0) - 2018-06-03 13:01:15.433 Slicer[790:59302] modalSession has been exited prematurely - check for a reentrant call to endModalSession:<br>
[DEBUG][Qt] 03.06.2018 13:01:47 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[DEBUG][Qt] 03.06.2018 13:01:58 [] (unknown:0) - Switch to module:  “Models”<br>
[DEBUG][Qt] 03.06.2018 13:02:02 [] (unknown:0) - Switch to module:  “Volumes”<br>
[WARNING][Qt] 03.06.2018 13:02:02 [] (unknown:0) - ctkDoubleRangeSlider::setSingleStep( 100 ) is outside of valid bounds.<br>
[WARNING][Qt] 03.06.2018 13:02:02 [] (unknown:0) - ctkRangeWidget::setSingleStep( 100 ) is outside valid bounds<br>
[WARNING][Qt] 03.06.2018 13:02:07 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 03.06.2018 13:02:09 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 03.06.2018 13:02:09 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 03.06.2018 13:02:14 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 03.06.2018 13:02:14 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[DEBUG][Qt] 03.06.2018 13:02:21 [] (unknown:0) - Switch to module:  “Data”<br>
[WARNING][Qt] 03.06.2018 13:02:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[CRITICAL][FD] 03.06.2018 13:03:13 [] (unknown:0) - 2018-06-03 13:03:13.582 Slicer[790:59302] modalSession has been exited prematurely - check for a reentrant call to endModalSession:<br>
[CRITICAL][FD] 03.06.2018 13:03:35 [] (unknown:0) - 2018-06-03 13:03:35.289 Slicer[790:59302] modalSession has been exited prematurely - check for a reentrant call to endModalSession:<br>
[INFO][Python] 03.06.2018 13:04:10 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:601) - Export scalar volume ‘4: TAC Altamirano1’ to directory /var/folders/02/xlz1btn17819djv59_ntjzqm0000gn/T/Slicer-stefania/DICOMExportTemp_20180603_130410/ScalarVolume_7<br>
[INFO][Stream] 03.06.2018 13:04:10 [] (unknown:0) - Export scalar volume ‘4: TAC Altamirano1’ to directory /var/folders/02/xlz1btn17819djv59_ntjzqm0000gn/T/Slicer-stefania/DICOMExportTemp_20180603_130410/ScalarVolume_7<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -   File “”, line 2, in <br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 638, in export<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -     exporter.export()<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Slicer-4.8/qt-scripted-modules/DICOMLib/DICOMExportScalarVolume.py”, line 128, in export<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -     cliNode = slicer.cli.run(dicomWrite, None, cliparameters, wait_for_completion=True)<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/slicer/cli.py”, line 71, in run<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -     node = createNode(module, parameters)<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/slicer/cli.py”, line 13, in createNode<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -     setNodeParameters(node, parameters)<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/Python/slicer/cli.py”, line 31, in setNodeParameters<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) -     node.SetParameterAsString(key, value)<br>
[CRITICAL][Stream] 03.06.2018 13:04:10 [] (unknown:0) - TypeError: SetParameterAsString argument 2: (unicode conversion error)<br>
[CRITICAL][FD] 03.06.2018 13:04:17 [] (unknown:0) - 2018-06-03 13:04:17.102 Slicer[790:59302] modalSession has been exited prematurely - check for a reentrant call to endModalSession:</p>

---
