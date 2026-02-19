---
topic_id: 31083
title: "An Error Occurred While Adding Nii Format Data"
date: 2023-08-10
url: https://discourse.slicer.org/t/31083
---

# An error occurred while adding nii format data

**Topic ID**: 31083
**Date**: 2023-08-10
**URL**: https://discourse.slicer.org/t/an-error-occurred-while-adding-nii-format-data/31083

---

## Post #1 by @ThreeStones1029 (2023-08-10 08:42 UTC)

<p>Problem report for Slicer 5.2.2 linux-amd64: [please describe expected and actual behavior]<br>
Hello:</p>
<p>I met a problem, the thing is like this, I did not close the software after adding two nii.gz data, and later I wanted to add another nii.gz file, but when I clicked add data in File, the pop-up window was black (the pop-up window is as follows), so I immediately checked the log file. The uploaded attachment is the bug log. I checked the log and guessed it was a QT problem, but I didn’t know how to fix it.</p>
<p>I’ve tried turning it back on, but it only seems to last a while, and the problem keeps recurring.<br>
If anyone has encountered the same problem, can you tell me how to solve it? Thank you very much.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e427fadd38b034b8497c817e6e0b3b13a4935bc5.png" data-download-href="/uploads/short-url/wymwer4nIFm5v44bHyZlEg5uSkR.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e427fadd38b034b8497c817e6e0b3b13a4935bc5_2_690x419.png" alt="图片" data-base62-sha1="wymwer4nIFm5v44bHyZlEg5uSkR" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e427fadd38b034b8497c817e6e0b3b13a4935bc5_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e427fadd38b034b8497c817e6e0b3b13a4935bc5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e427fadd38b034b8497c817e6e0b3b13a4935bc5.png 2x" data-dominant-color="060606"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">767×466 17.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<details>
<summary>
bug log:</summary>
<pre><code class="lang-txt">[DEBUG][Qt] 10.08.2023 08:47:18 [] (unknown:0) - Session start time .......: 2023-08-10 08:47:18
[DEBUG][Qt] 10.08.2023 08:47:18 [] (unknown:0) - Slicer version ...........: 5.2.2 (revision 31382 / fb46bd1) linux-amd64 - installed release
[DEBUG][Qt] 10.08.2023 08:47:18 [] (unknown:0) - Operating system .........: Linux / 5.15.0-78-generic / #85~20.04.1-Ubuntu SMP Mon Jul 17 09:42:39 UTC 2023 / UTF-8 - 64-bit
[DEBUG][Qt] 10.08.2023 08:47:18 [] (unknown:0) - Memory ...................: 32011 MB physical, 31249 MB virtual
[DEBUG][Qt] 10.08.2023 08:47:18 [] (unknown:0) - CPU ......................: GenuineIntel Intel(R) Xeon(R) CPU E5-2640 v4 @ 2.40GHz, 10 cores, 20 logical processors
[DEBUG][Qt] 10.08.2023 08:47:18 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, Sequential threading
[DEBUG][Qt] 10.08.2023 08:47:18 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)
[DEBUG][Qt] 10.08.2023 08:47:18 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 10.08.2023 08:47:18 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 10.08.2023 08:47:18 [] (unknown:0) - Application path .........: /home/***/Slicer-5.2.2-linux-amd64/bin
[DEBUG][Qt] 10.08.2023 08:47:18 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 10.08.2023 08:47:24 [Python] (/home/***/Slicer-5.2.2-linux-amd64/lib/Slicer-5.2/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 10.08.2023 08:47:25 [Python] (/home/***/Slicer-5.2.2-linux-amd64/lib/Slicer-5.2/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 10.08.2023 08:47:25 [Python] (/home/***/Slicer-5.2.2-linux-amd64/lib/Slicer-5.2/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 10.08.2023 08:47:25 [] (unknown:0) - Switch to module:  "Welcome"
[INFO][VTK] 10.08.2023 08:47:49 [vtkMRMLVolumeArchetypeStorageNode (0x8045660)] (/work/Stable/Slicer-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:513) - Loaded volume from file: /home/***/Desktop/ITK_3D/data/***.nii.gz. Dimensions: 512x512x464. Number of components: 1. Pixel type: int.
[DEBUG][Qt] 10.08.2023 08:47:49 [] (unknown:0) - "Volume" Reader has successfully read the file "/home/jjf/Desktop/ITK_3D/data/***.nii.gz" "[3.52s]"
[INFO][VTK] 10.08.2023 08:51:33 [vtkMRMLVolumeArchetypeStorageNode (0xc44c980)] (/work/Stable/Slicer-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:513) - Loaded volume from file: /home/***/Desktop/ITK_3D/data/***.nii.gz. Dimensions: 512x512x420. Number of components: 1. Pixel type: int.
[DEBUG][Qt] 10.08.2023 08:51:33 [] (unknown:0) - "Volume" Reader has successfully read the file "/home/jjf/Desktop/ITK_3D/data/***.nii.gz" "[3.13s]"
[WARNING][Qt] 10.08.2023 09:02:03 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 9348, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:03 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 9351, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:03 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 9367, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:03 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 9368, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:03 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 9380, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:03 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 9384, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:03 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 9385, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:03 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 9389, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:04 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 9392, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:04 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 9396, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:04 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 9400, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[DEBUG][Qt] 10.08.2023 09:02:14 [] (unknown:0) - Switch to module:  "DICOM"
[CRITICAL][Stream] 10.08.2023 09:02:14 [] (unknown:0) - Database folder does not contain ctkDICOM.sql file: /home/***/Documents/SlicerDICOMDatabase
[WARNING][Qt] 10.08.2023 09:02:18 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10053, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:18 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10056, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:18 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10060, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:18 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10061, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:22 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10094, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:22 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10095, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:24 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10106, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:24 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10107, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:25 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10125, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:25 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10136, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:25 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10137, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:25 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10148, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:30 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10296, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:30 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10299, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:30 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10303, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:30 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10304, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[DEBUG][Qt] 10.08.2023 09:02:36 [] (unknown:0) - Switch to module:  "Data"
[WARNING][Qt] 10.08.2023 09:02:39 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10689, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:39 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10692, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:39 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10708, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:39 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10709, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:41 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10724, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:41 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10725, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:41 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10726, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:41 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10727, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:41 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10728, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:02:43 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10737, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:06:38 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10757, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:06:40 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10774, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:06:40 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10778, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:06:40 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10782, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:06:40 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10786, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:06:43 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10978, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:06:43 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10981, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:06:43 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10997, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:06:43 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 10998, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:06:44 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 11011, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:06:44 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 11015, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:06:44 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 11019, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:06:44 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 11020, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:06:44 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 11021, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:06:44 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 11022, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:06:44 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 11023, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:06:49 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 11045, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:06:49 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 11049, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[DEBUG][Qt] 10.08.2023 09:07:31 [] (unknown:0) - Switch to module:  "Welcome"
[WARNING][Qt] 10.08.2023 09:07:40 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 11988, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:07:40 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 11991, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:07:40 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 12007, resource id: 121634877, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 10.08.2023 09:07:40 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 12008, resource id: 121634877, major code: 130 (Unknown), minor code: 3
</code></pre>
</details>

---

## Post #2 by @lassoan (2023-08-10 08:59 UTC)

<p>Thanks for reporting, it seems like the same or very similar issue as this one:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7153">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7153" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7153" target="_blank" rel="noopener">Switching workspaces in Ubuntu causes multiple UI failures</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-08-04" data-time="21:09:52" data-timezone="UTC">09:09PM - 04 Aug 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/tao558" target="_blank" rel="noopener">
          <img alt="tao558" src="https://avatars.githubusercontent.com/u/26352734?v=4" class="onebox-avatar-inline" width="20" height="20">
          tao558
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary
Switching workspaces in Ubuntu can be done with the `ctrl` + `alt` +<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> `down` / `up` arrow keys. If a user opens slicer, loads two volumes into the foreground / background, switches workspaces, then returns to the workspace with slicer open, two UI failures happen:

1. Clicking the "add data" button opens a completely black menu box
2. The foreground / background volumes can no longer be changed (the dropdown menu doesn't appear)

See the attached video for an example of both of these errors.

## Steps to reproduce
1. Load a volume into the background and foreground for a given slice view
2. Change to a different workspace (`ctrl` + `alt` + `down` / `up`)
3. Change back to the original workspace with slicer open
4. Try clicking the "add data" button and observe that the menu is completely black
5. Try changing the foreground / background volumes and observe that the drop down menu doesn't appear

## Environment
- Slicer version: Slicer-5.3.0-2023-08-03
- Operating system: Ubuntu 20.04

The following debug output from the error log might be helpful:

```
QXcbConnection: XC

https://github.com/Slicer/Slicer/assets/26352734/7fc4027d-c515-4c30-aa5a-14adc4571b63

B error: 8 (BadMatch), sequence: 3577, resource id: 41943173, major code: 130 (Unknown), minor code: 3
QXcbConnection: XCB error: 8 (BadMatch), sequence: 3580, resource id: 41943173, major code: 130 (Unknown), minor code: 3
QXcbConnection: XCB error: 8 (BadMatch), sequence: 3593, resource id: 41943173, major code: 130 (Unknown), minor code: 3
QXcbConnection: XCB error: 8 (BadMatch), sequence: 3594, resource id: 41943173, major code: 130 (Unknown), minor code: 3
```

https://github.com/Slicer/Slicer/assets/26352734/c8829dd9-b543-4697-bb2e-4f8e1d63e02f</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
