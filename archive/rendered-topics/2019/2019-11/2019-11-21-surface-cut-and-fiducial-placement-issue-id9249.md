# Surface Cut and Fiducial Placement Issue

**Topic ID**: 9249
**Date**: 2019-11-21
**URL**: https://discourse.slicer.org/t/surface-cut-and-fiducial-placement-issue/9249

---

## Post #1 by @Marjorie (2019-11-21 13:49 UTC)

<p>Hello,<br>
My apologies if it was asked or discussed elsewhere: I went through the documentation but I did not see anything.<br>
I discovered the software very recently (i’m working with Slicer 4.10.2 on Mac Catalina), I have already followed some tutorials, but I am currently facing a problem in “segment editor”, with the extension “segment editor extra effects”.<br>
Indeed, trying to apply this video (<a href="https://www.youtube.com/watch?v=xZwyW6SaoM4" class="inline-onebox" rel="noopener nofollow ugc">New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor - YouTube</a>) to one of my projects, it turns out that when I go on “surface cut” I can not then access “Fiducial Placement” (which remains grayed out).<br>
I can not understand why …<br>
Is it possible that this is Mac compatibility?<br>
Anyone know how to enlighten me?<br>
Thank you in advance and good day.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bcbe5fa871794ef98725163806fee2b6a7f648d5.jpeg" data-download-href="/uploads/short-url/qVHDz0fONwcxE2WI47JVjJ5pLZH.jpeg?dl=1" title="surfaceCutIssue" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bcbe5fa871794ef98725163806fee2b6a7f648d5_2_690x300.jpeg" alt="surfaceCutIssue" data-base62-sha1="qVHDz0fONwcxE2WI47JVjJ5pLZH" width="690" height="300" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bcbe5fa871794ef98725163806fee2b6a7f648d5_2_690x300.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bcbe5fa871794ef98725163806fee2b6a7f648d5_2_1035x450.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bcbe5fa871794ef98725163806fee2b6a7f648d5_2_1380x600.jpeg 2x" data-dominant-color="BBB7C0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">surfaceCutIssue</span><span class="informations">6620×2880 1.17 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-11-21 13:55 UTC)

<p>When you installed SegmentEditorExtraEffects extension, did you accept installing MarkupsToModel extension (which is required by Surface cut effect)?</p>
<p>If not, then install MarkupsToModel extension from the extension manager and retry.</p>
<p>If it still does not work then let us know if any error is logged (in menu: Help / Report a bug).</p>

---

## Post #3 by @Marjorie (2019-11-21 14:33 UTC)

<p>Thank you for your very quick answer.<br>
I had the extension “MarkupsToModel” so unfortunately it does not come from there.<br>
Do you want me to past the bug in this topic?</p>

---

## Post #4 by @lassoan (2019-11-21 14:49 UTC)

<p>Yes, you can copy-paste the log here.</p>

---

## Post #5 by @Marjorie (2019-11-21 14:53 UTC)

<p>[DEBUG][Qt] 21.11.2019 15:51:38 [] (unknown:0) - Session start time …: 2019-11-21 15:51:38<br>
[DEBUG][Qt] 21.11.2019 15:51:38 [] (unknown:0) - Slicer version …: 4.10.2 (revision 28257) macosx-amd64 - installed release<br>
[DEBUG][Qt] 21.11.2019 15:51:38 [] (unknown:0) - Operating system …: Mac OS X / 10.15 / 19A583 - 64-bit<br>
[DEBUG][Qt] 21.11.2019 15:51:38 [] (unknown:0) - Memory …: 16384 MB physical, 2048 MB virtual<br>
[DEBUG][Qt] 21.11.2019 15:51:38 [] (unknown:0) - CPU …: GenuineIntel Intel® Core™ i5-7500 CPU @ 3.40GHz, 4 cores, 4 logical processors<br>
[DEBUG][Qt] 21.11.2019 15:51:38 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 21.11.2019 15:51:38 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 21.11.2019 15:51:38 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 21.11.2019 15:51:38 [] (unknown:0) - Additional module paths …: /Volumes/Disque dur externe/marjorie champarou/Applications/Slicer.app/Contents/Extensions-28257/SegmentEditorExtraEffects/lib/Slicer-4.10/qt-scripted-modules<br>
[DEBUG][Python] 21.11.2019 15:51:39 [Python] (/Volumes/Disque dur externe/marjorie champarou/Applications/Slicer.app/Contents/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 21.11.2019 15:51:41 [Python] (/Volumes/Disque dur externe/marjorie champarou/Applications/Slicer.app/Contents/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 21.11.2019 15:51:41 [Python] (/Volumes/Disque dur externe/marjorie champarou/Applications/Slicer.app/Contents/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 21.11.2019 15:51:41 [] (unknown:0) - Switch to module:  “Welcome”<br>
[CRITICAL][Stream] 21.11.2019 15:51:42 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 21.11.2019 15:51:42 [] (unknown:0) -   File “/Volumes/Disque dur externe/marjorie champarou/Applications/Slicer.app/Contents/Extensions-28257/SegmentEditorExtraEffects/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorDrawTubeLib/SegmentEditorEffect.py”, line 14, in <strong>init</strong><br>
[CRITICAL][Stream] 21.11.2019 15:51:42 [] (unknown:0) -     self.logic = DrawTubeLogic(scriptedEffect)<br>
[CRITICAL][Stream] 21.11.2019 15:51:42 [] (unknown:0) -   File “/Volumes/Disque dur externe/marjorie champarou/Applications/Slicer.app/Contents/Extensions-28257/SegmentEditorExtraEffects/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorDrawTubeLib/SegmentEditorEffect.py”, line 407, in <strong>init</strong><br>
[CRITICAL][Stream] 21.11.2019 15:51:42 [] (unknown:0) -     self.curveGenerator = slicer.vtkCurveGenerator()<br>
[CRITICAL][Stream] 21.11.2019 15:51:42 [] (unknown:0) - AttributeError: ‘module’ object has no attribute ‘vtkCurveGenerator’<br>
[CRITICAL][Qt] 21.11.2019 15:51:42 [] (unknown:0) - qSlicerPythonCppAPI::instantiateClass  - [ “SegmentEditorEffect” ] - Failed to instantiate scripted pythonqt class “SegmentEditorEffect” 0x12e934c18<br>
[CRITICAL][Stream] 21.11.2019 15:51:42 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 21.11.2019 15:51:42 [] (unknown:0) -   File “/Volumes/Disque dur externe/marjorie champarou/Applications/Slicer.app/Contents/Extensions-28257/SegmentEditorExtraEffects/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorDrawTube.py”, line 27, in registerEditorEffect<br>
[CRITICAL][Stream] 21.11.2019 15:51:42 [] (unknown:0) -     instance.self().register()<br>
[CRITICAL][Stream] 21.11.2019 15:51:42 [] (unknown:0) - AttributeError: ‘NoneType’ object has no attribute ‘register’<br>
[INFO][Stream] 21.11.2019 15:51:47 [] (unknown:0) - Loading Slicer RC file [/Volumes/Disque dur externe/marjorie champarou/.slicerrc.py]<br>
[DEBUG][Qt] 21.11.2019 15:51:59 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[WARNING][Qt] 21.11.2019 15:51:59 [] (unknown:0) - QLayout::addChildLayout: layout “” already has a parent<br>
[DEBUG][Qt] 21.11.2019 15:52:10 [] (unknown:0) - Switch to module:  “DICOM”<br>
[DEBUG][Python] 21.11.2019 15:52:19 [Python] (/Volumes/Disque dur externe/marjorie champarou/Applications/Slicer.app/Contents/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 21.11.2019 15:52:19 [Python] (/Volumes/Disque dur externe/marjorie champarou/Applications/Slicer.app/Contents/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 2 multivolumes!<br>
[DEBUG][Python] 21.11.2019 15:52:20 [Python] (/Volumes/Disque dur externe/marjorie champarou/Applications/Slicer.app/Contents/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:165) - MultiVolumeImportPlugin:examineMultiseries<br>
[DEBUG][Python] 21.11.2019 15:52:20 [Python] (/Volumes/Disque dur externe/marjorie champarou/Applications/Slicer.app/Contents/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:170) - DICOMMultiVolumePlugin found 1 multivolumes!<br>
[INFO][Python] 21.11.2019 15:52:20 [Python] (/Volumes/Disque dur externe/marjorie champarou/Applications/Slicer.app/Contents/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: GDCM<br>
[WARNING][Python] 21.11.2019 15:52:22 [Python] (/Volumes/Disque dur externe/marjorie champarou/Applications/Slicer.app/Contents/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:706) - Irregular volume geometry detected, but maximum error non-zero but is within tolerance (maximum error of 0.000662231 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 21.11.2019 15:52:20 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[CRITICAL][Stream] 21.11.2019 15:52:22 [] (unknown:0) - Irregular volume geometry detected, but maximum error non-zero but is within tolerance (maximum error of 0.000662231 mm, tolerance threshold is 0.001 mm).<br>
[DEBUG][Qt] 21.11.2019 15:52:27 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[WARNING][Qt] 21.11.2019 15:52:34 [] (unknown:0) - ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1<br>
[CRITICAL][Stream] 21.11.2019 15:52:37 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 21.11.2019 15:52:37 [] (unknown:0) -   File “/Volumes/Disque dur externe/marjorie champarou/Applications/Slicer.app/Contents/Extensions-28257/SegmentEditorExtraEffects/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorSurfaceCutLib/SegmentEditorEffect.py”, line 130, in activate<br>
[CRITICAL][Stream] 21.11.2019 15:52:37 [] (unknown:0) -     self.createNewMarkupNode()<br>
[CRITICAL][Stream] 21.11.2019 15:52:37 [] (unknown:0) -   File “/Volumes/Disque dur externe/marjorie champarou/Applications/Slicer.app/Contents/Extensions-28257/SegmentEditorExtraEffects/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorSurfaceCutLib/SegmentEditorEffect.py”, line 308, in createNewMarkupNode<br>
[CRITICAL][Stream] 21.11.2019 15:52:37 [] (unknown:0) -     self.setAndObserveSegmentMarkupNode(self.segmentMarkupNode)<br>
[CRITICAL][Stream] 21.11.2019 15:52:37 [] (unknown:0) -   File “/Volumes/Disque dur externe/marjorie champarou/Applications/Slicer.app/Contents/Extensions-28257/SegmentEditorExtraEffects/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorSurfaceCutLib/SegmentEditorEffect.py”, line 333, in setAndObserveSegmentMarkupNode<br>
[CRITICAL][Stream] 21.11.2019 15:52:37 [] (unknown:0) -     self.updateModelFromSegmentMarkupNode()<br>
[CRITICAL][Stream] 21.11.2019 15:52:37 [] (unknown:0) -   File “/Volumes/Disque dur externe/marjorie champarou/Applications/Slicer.app/Contents/Extensions-28257/SegmentEditorExtraEffects/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorSurfaceCutLib/SegmentEditorEffect.py”, line 368, in updateModelFromSegmentMarkupNode<br>
[CRITICAL][Stream] 21.11.2019 15:52:37 [] (unknown:0) -     self.logic.updateModelFromMarkup(self.segmentMarkupNode, self.segmentModel)<br>
[CRITICAL][Stream] 21.11.2019 15:52:37 [] (unknown:0) -   File “/Volumes/Disque dur externe/marjorie champarou/Applications/Slicer.app/Contents/Extensions-28257/SegmentEditorExtraEffects/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorSurfaceCutLib/SegmentEditorEffect.py”, line 398, in updateModelFromMarkup<br>
[CRITICAL][Stream] 21.11.2019 15:52:37 [] (unknown:0) -     markupsToModel = slicer.modules.markupstomodel.logic()<br>
[CRITICAL][Stream] 21.11.2019 15:52:37 [] (unknown:0) - AttributeError: ‘module’ object has no attribute ‘markupstomodel’</p>

---

## Post #6 by @lassoan (2019-11-21 14:56 UTC)

<p>The log confirms that MarkupsToModel extension is not installed. If it shows up in the extension manager then uninstall it, then install it again.</p>

---

## Post #7 by @Marjorie (2019-11-21 15:02 UTC)

<p>Thank you very much!<br>
Indeed “markupsToModel” was noted as installed but after uninstalling and reinstalling it, it works! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
Have a nice day !</p>

---

## Post #8 by @lassoan (2019-11-21 15:04 UTC)

<p>I’m glad it works.</p>
<p>Probably installation was incomplete (you might have closed the application before installation was completed).</p>

---

## Post #9 by @Marjorie (2019-11-21 15:10 UTC)

<p>Ok it’s good to know.<br>
Thank you !</p>

---

## Post #10 by @lassoan (2023-09-18 13:14 UTC)

<p>A post was merged into an existing topic: <a href="/t/new-extensions-can-not-work-on-slicer-5-4-0-on-macos/31535/8">New extensions can not work on Slicer 5.4.0 on MacOS</a></p>

---
