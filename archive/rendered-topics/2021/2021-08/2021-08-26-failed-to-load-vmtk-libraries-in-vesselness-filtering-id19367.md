# Failed to load VMTK libraries in Vesselness Filtering

**Topic ID**: 19367
**Date**: 2021-08-26
**URL**: https://discourse.slicer.org/t/failed-to-load-vmtk-libraries-in-vesselness-filtering/19367

---

## Post #1 by @simone (2021-08-26 15:20 UTC)

<p>Hi, I am using Slicer 4.11.20210226 on macOS 11.5. I am trying to use Vesselness Filtering but I get the error above. This is the full log:</p>
<p>[DEBUG][Qt] 26.08.2021 11:07:13 [] (unknown:0) - Session start time …: 2021-08-26 11:07:13<br>
[DEBUG][Qt] 26.08.2021 11:07:13 [] (unknown:0) - Slicer version …: 4.11.20210226 (revision 29738 / 7a593c8) macosx-amd64 - installed release<br>
[DEBUG][Qt] 26.08.2021 11:07:13 [] (unknown:0) - Operating system …: macOS / 11.5 / 20G71 / UTF-8 - 64-bit<br>
[DEBUG][Qt] 26.08.2021 11:07:13 [] (unknown:0) - Memory …: 8192 MB physical, 1024 MB virtual<br>
[DEBUG][Qt] 26.08.2021 11:07:13 [] (unknown:0) - CPU …: GenuineIntel Intel(R) Core™ i5-8259U CPU @ 2.30GHz, 4 cores, 8 logical processors<br>
[DEBUG][Qt] 26.08.2021 11:07:13 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 26.08.2021 11:07:13 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 26.08.2021 11:07:13 [] (unknown:0) - Developer mode enabled …: yes<br>
[DEBUG][Qt] 26.08.2021 11:07:13 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 26.08.2021 11:07:13 [] (unknown:0) - Application path …: /Applications/Slicer.app/Contents/MacOS<br>
[DEBUG][Qt] 26.08.2021 11:07:13 [] (unknown:0) - Additional module paths …: Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules, Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules<br>
[DEBUG][Python] 26.08.2021 11:07:14 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pydicom/datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[CRITICAL][Qt] 26.08.2021 11:07:14 [] (unknown:0) -   Error(s):<br>
CLI executable: /Applications/Slicer.app/Contents/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules/vtkvmtk.py<br>
The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.<br>
[CRITICAL][Qt] 26.08.2021 11:07:14 [] (unknown:0) - Fail to instantiate module  “vtkvmtk”<br>
[CRITICAL][Qt] 26.08.2021 11:07:14 [] (unknown:0) - The following modules failed to be instantiated:<br>
[CRITICAL][Qt] 26.08.2021 11:07:14 [] (unknown:0) -    vtkvmtk<br>
[DEBUG][Python] 26.08.2021 11:07:15 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 26.08.2021 11:07:15 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 26.08.2021 11:07:15 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 26.08.2021 11:07:15 [] (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][VTK] 26.08.2021 11:07:16 [vtkMRMLVolumeArchetypeStorageNode (0x7fb98de31330)] (/Volumes/D/S/S-1/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:509) - Loaded volume from file: /Applications/Slicer.app/Contents/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/Resources/Vesselness.png. Dimensions: 65x50x1. Number of components: 3. Pixel type: unsigned char.<br>
[DEBUG][Python] 26.08.2021 11:07:36 [Python] (/Applications/Slicer.app/Contents/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/VesselnessFiltering.py:260) - onMRMLSceneChanged<br>
[DEBUG][Python] 26.08.2021 11:07:36 [Python] (/Applications/Slicer.app/Contents/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/VesselnessFiltering.py:337) - restoreDefaults<br>
[DEBUG][Qt] 26.08.2021 11:07:36 [] (unknown:0) - Switch to module:  “VesselnessFiltering”<br>
[CRITICAL][Stream] 26.08.2021 11:07:36 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 26.08.2021 11:07:36 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/VesselnessFiltering.py”, line 261, in onMRMLSceneChanged<br>
[CRITICAL][Stream] 26.08.2021 11:07:36 [] (unknown:0) -     self.restoreDefaults()<br>
[CRITICAL][Stream] 26.08.2021 11:07:36 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/VesselnessFiltering.py”, line 339, in restoreDefaults<br>
[CRITICAL][Stream] 26.08.2021 11:07:36 [] (unknown:0) -     self.detectPushButton.checked = True<br>
[CRITICAL][Stream] 26.08.2021 11:07:36 [] (unknown:0) - AttributeError: ‘VesselnessFilteringWidget’ object has no attribute ‘detectPushButton’</p>
<p>I already tried to use the nightly version without success. Can you please help me to fix this? Thanks in advance.</p>

---

## Post #2 by @lassoan (2021-08-27 01:36 UTC)

<p>This is a known regression, we hope that it will be fixed early next week. You can monitor the status (sign up for update notifications) of this issue here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/issues/37">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/37" target="_blank" rel="noopener">github.com/vmtk/SlicerExtension-VMTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/37" target="_blank" rel="noopener">VMTK gone missing recently in Slicer-4.11.20210226 and latest Slicer-4.13</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-08-09" data-time="19:08:54" data-timezone="UTC">07:08PM - 09 Aug 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The extension installation package does not contain VMTK binaries, only the Slic<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">er module .py files, for both latest Slicer Stable Release and Slicer Preview Release on macOS.

It seems that the recent upgrade to VTK9 broke packaging for VTK-8.2.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
