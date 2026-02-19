---
topic_id: 5797
title: "Export Dicom Rt Structure As Segmentation"
date: 2019-02-15
url: https://discourse.slicer.org/t/5797
---

# Export DICOM RT structure as segmentation

**Topic ID**: 5797
**Date**: 2019-02-15
**URL**: https://discourse.slicer.org/t/export-dicom-rt-structure-as-segmentation/5797

---

## Post #1 by @yliao (2019-02-15 20:35 UTC)

<p>Hi,<br>
I am trying to convert a DICOM RT structure file to STL file through exporting a segmentation from 3D Slicer 4.10.0. The segmentation was successfully loaded in Slicer by opening the DICOM RT Structure.<br>
I can view the structure and edit it as a segmentation just fine. However, I tried to export it using the “Segment Editor” module and selected “Export to files” under “Segmentations”. Nothing is showing up in the destination folder or anywhere else.<br>
Your help is greatly appreciated!</p>

---

## Post #2 by @cpinter (2019-02-15 20:51 UTC)

<p>What do you mean by “edit it as a segmentation just fine”? Loaded RT structure sets cannot directly be edited, so I suspect there is something strange going on here. Are you sure you are trying to edit and export the right dataset?</p>
<p>It would help if you’d either make a video of what you’re doing from the beginning, or describe each step in a very detailed manner. Thanks!</p>

---

## Post #3 by @yliao (2019-02-15 22:10 UTC)

<p>Thank you! You are right. I had to convert it to binary label map before editing, but that’s prompted properly and straightforward. The problem was exporting afterwards.</p>
<p>The problem is fixed now. I guess Slicer is having trouble dealing with the imported RT Structure as a segmentation. I created a new segmentation on the CT images and dragged that structure into the new segmentation and everything was fine. I am able to export.</p>

---

## Post #4 by @cpinter (2019-02-16 01:25 UTC)

<p>I’m glad it works for you. I’d still feel better if I understood what is going wrong with your original approach. If you’re content with this solution I understand, but it would help us if you made a video or explained why exactly the first try didn’t go well.</p>

---

## Post #5 by @yliao (2019-02-16 01:42 UTC)

<p>Sure. I’ll submit the pictures on Monday. Thank you for following up on this.</p>

---

## Post #6 by @yliao (2019-02-18 18:02 UTC)

<p>Hi Csaba,<br>
Here are the screenshots I took this morning regarding the export STL problem. I hope the pictures are self explanatory. Please let me know if you need additional information. Thank you for looking into this.</p>
<p>Yixiang<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90ef48da99849ed677ecf32ae942be4840dd9f2d.png" data-download-href="/uploads/short-url/kG9q4NUEF9d5gE14iN8n3E6gWFT.png?dl=1" title="Import1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90ef48da99849ed677ecf32ae942be4840dd9f2d_2_690x265.png" alt="Import1" data-base62-sha1="kG9q4NUEF9d5gE14iN8n3E6gWFT" width="690" height="265" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90ef48da99849ed677ecf32ae942be4840dd9f2d_2_690x265.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90ef48da99849ed677ecf32ae942be4840dd9f2d_2_1035x397.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90ef48da99849ed677ecf32ae942be4840dd9f2d_2_1380x530.png 2x" data-dominant-color="E6E6E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Import1</span><span class="informations">1648×635 33.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @yliao (2019-02-18 18:03 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0b9e859c6700826ceed45450da70466db811d04.png" data-download-href="/uploads/short-url/pdol56u7dMNRB9LZw83qOzZqRp2.png?dl=1" title="Edit2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0b9e859c6700826ceed45450da70466db811d04_2_690x388.png" alt="Edit2" data-base62-sha1="pdol56u7dMNRB9LZw83qOzZqRp2" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0b9e859c6700826ceed45450da70466db811d04_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0b9e859c6700826ceed45450da70466db811d04_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0b9e859c6700826ceed45450da70466db811d04_2_1380x776.png 2x" data-dominant-color="7F8088"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Edit2</span><span class="informations">1920×1080 450 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @yliao (2019-02-18 18:03 UTC)

<p>And the file is not appearing in the destination folder.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c20c95a8d1e3449d06a3715f425ff14f94a568c.png" data-download-href="/uploads/short-url/jZD5CDvqT1ct7bv0MVuDiejpDpW.png?dl=1" title="Export3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c20c95a8d1e3449d06a3715f425ff14f94a568c.png" alt="Export3" data-base62-sha1="jZD5CDvqT1ct7bv0MVuDiejpDpW" width="676" height="500" data-dominant-color="FBFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Export3</span><span class="informations">770×569 20.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @cpinter (2019-02-19 15:31 UTC)

<p>I’ll try to reproduce the issue you’ve had.</p>
<p>One question though. If you haven’t changed anything in the segmentation then why did you go through the Segment Editor route? It’s not necessary to change the master representation to labelmap to export it to STL.<br>
Also no need to copy anything to another segmentation. Instead you can go to Segmentations module, make sure Closed surface is created (there should be a green tick next to it), go to Import/Export section towards the bottom, and do the STL export from there.</p>

---

## Post #10 by @cpinter (2019-02-19 15:34 UTC)

<p>Thanks so much for the images, they are a great help!</p>
<p>I managed to reproduce the problem: the character ‘:’ is not allowed in file names. If you rename the segmentation to not have the colon character, then export is successful.<br>
We will fix this to automatically replace the illegal characters.</p>
<p>However I still recommend not to go throudh Segment Editor and instead do what I described above, because going from surface to labelmap to surface again comes with data loss.</p>

---

## Post #11 by @yliao (2019-02-19 16:25 UTC)

<p>Thank you, Csaba! I needed to modify the structure a little bit to clean up the artifacts. But I will keep it in mind of the alternative method. Thanks!</p>
<p>Yixiang</p>

---

## Post #12 by @cpinter (2019-02-19 16:33 UTC)

<p>I see. I’m already working on a solution for the illegal file name issue. It should be available in tomorrow’s nightly if all goes well, and then you won’t have to rename or copy.</p>

---

## Post #13 by @cpinter (2019-02-19 17:15 UTC)

<p>I fixed the issue in this commit: <a href="https://github.com/Slicer/Slicer/commit/2c39ac184feb665d0a1f229b9fa089656a45612a" rel="nofollow noopener">https://github.com/Slicer/Slicer/commit/2c39ac184feb665d0a1f229b9fa089656a45612a</a><br>
Tomorrow’s nightly should be good. Thanks for helping us fix this problem!</p>

---

## Post #14 by @labixin (2019-04-17 04:25 UTC)

<p>Hi Csaba,<br>
I met with the similar problem and I followed your instructions. But still nothing is showing up in the destination folder or anywhere else. Your help is greatly appreciated! <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75571ec47fc524159a72df2027e2c9c10328677f.jpeg" data-download-href="/uploads/short-url/gK2w7SLGYBaPIyU86L6Pgk3ChtR.jpeg?dl=1" title="01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/75571ec47fc524159a72df2027e2c9c10328677f_2_689x373.jpeg" alt="01" data-base62-sha1="gK2w7SLGYBaPIyU86L6Pgk3ChtR" width="689" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/75571ec47fc524159a72df2027e2c9c10328677f_2_689x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/75571ec47fc524159a72df2027e2c9c10328677f_2_1033x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75571ec47fc524159a72df2027e2c9c10328677f.jpeg 2x" data-dominant-color="6F6F79"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">01</span><span class="informations">1268×686 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @labixin (2019-04-17 04:35 UTC)

<p>Finally when I moved or copied to another segmentation, it worked out well. But I wonder whether it is the same as RTst which relates to the original image? And could you tell me how to extract the coordinate information of the contour? Thank you. <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a765eff3b6805548948cf2548a1c05dd37a1670.png" alt="04" data-base62-sha1="jKTuZdhAFkx8LhTbVpl57FyKi1q" width="536" height="338"></p>

---

## Post #16 by @cpinter (2019-04-17 13:46 UTC)

<p>Can you please</p>
<ol>
<li>Start a fresh Slicer</li>
<li>Load the RTSS</li>
<li>Try to export it the way your screenshot shows</li>
<li>Send us the log (About / Report an error)</li>
</ol>
<p>Thanks!</p>

---

## Post #17 by @labixin (2019-04-18 01:34 UTC)

<p>Sorry I didn’t find where to upload the .log file.</p>
<details>
<summary>
Log</summary>
<pre><code>[DEBUG][Qt] 18.04.2019 09:01:13 [] (unknown:0) - Session start time .......: 2019-04-18 09:01:13
[DEBUG][Qt] 18.04.2019 09:01:13 [] (unknown:0) - Slicer version ...........: 4.11.0-2018-12-21 (revision 27668) win-amd64 - installed release
[DEBUG][Qt] 18.04.2019 09:01:13 [] (unknown:0) - Operating system .........: Windows / 7 / Service Pack 1 (Build 7601) - 64-bit
[DEBUG][Qt] 18.04.2019 09:01:13 [] (unknown:0) - Memory ...................: 3964 MB physical, 7927 MB virtual
[DEBUG][Qt] 18.04.2019 09:01:13 [] (unknown:0) - CPU ......................: GenuineIntel , 4 cores, 4 logical processors
[DEBUG][Qt] 18.04.2019 09:01:13 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 18.04.2019 09:01:13 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 18.04.2019 09:01:13 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 18.04.2019 09:01:13 [] (unknown:0) - Additional module paths ..: C:/Users/Administrator/AppData/Roaming/NA-MIC/Extensions-27668/SegmentMesher/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Administrator/AppData/Roaming/NA-MIC/Extensions-27668/CleaverExtension/lib/Slicer-4.11/cli-modules, C:/Users/Administrator/AppData/Roaming/NA-MIC/Extensions-27668/OpenCAD/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Administrator/AppData/Roaming/NA-MIC/Extensions-27668/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Administrator/AppData/Roaming/NA-MIC/Extensions-27668/SlicerRT/lib/Slicer-4.11/cli-modules, C:/Users/Administrator/AppData/Roaming/NA-MIC/Extensions-27668/SlicerRT/lib/Slicer-4.11/qt-loadable-modules, C:/Users/Administrator/AppData/Roaming/NA-MIC/Extensions-27668/SlicerRT/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Administrator/AppData/Roaming/NA-MIC/Extensions-27668/MeshToLabelMap/lib/Slicer-4.11/cli-modules, C:/Users/Administrator/AppData/Roaming/NA-MIC/Extensions-27668/IntensitySegmenter/lib/Slicer-4.11/cli-modules, C:/Users/Administrator/AppData/Roaming/NA-MIC/Extensions-27668/MarkupsToModel/lib/Slicer-4.11/qt-loadable-modules, C:/Users/Administrator/AppData/Roaming/NA-MIC/Extensions-27668/SegmentationWizard/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Administrator/AppData/Roaming/NA-MIC/Extensions-27668/VolumeClip/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Administrator/AppData/Roaming/NA-MIC/Extensions-27668/ScatteredTransform/lib/Slicer-4.11/cli-modules, C:/Users/Administrator/AppData/Roaming/NA-MIC/Extensions-27668/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules
[DEBUG][Python] 18.04.2019 09:01:19 [Python] (C:\Program Files\Slicer 4.11.0-2018-12-21\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 18.04.2019 09:01:21 [Python] (C:\Program Files\Slicer 4.11.0-2018-12-21\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 18.04.2019 09:01:21 [Python] (C:\Program Files\Slicer 4.11.0-2018-12-21\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 18.04.2019 09:01:22 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 18.04.2019 09:01:25 [] (unknown:0) - Switch to module:  "DICOM"
[DEBUG][Qt] 18.04.2019 09:01:41 [] (unknown:0) - New patient inserted: 18
[DEBUG][Qt] 18.04.2019 09:01:41 [] (unknown:0) - New patient inserted as :  18
[DEBUG][Qt] 18.04.2019 09:01:41 [] (unknown:0) - Need to insert new study:  "1.2.840.113704.1.111.4716.1524036773.1"
[DEBUG][Qt] 18.04.2019 09:01:41 [] (unknown:0) - Study Added
[DEBUG][Qt] 18.04.2019 09:01:41 [] (unknown:0) - Need to insert new series:  "1.2.840.113704.1.111.4716.1524036821.7"
[DEBUG][Qt] 18.04.2019 09:01:41 [] (unknown:0) - Series Added
[DEBUG][Qt] 18.04.2019 09:01:43 [] (unknown:0) - "DICOM indexer has successfully processed 79 files [1.81s]"
[INFO][Python] 18.04.2019 09:01:44 [Python] (C:\Program Files\Slicer 4.11.0-2018-12-21\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMWidgets.py:471) - Imported a DICOM directory, checking for extensions
[INFO][Stream] 18.04.2019 09:01:44 [] (unknown:0) - Imported a DICOM directory, checking for extensions
[DEBUG][Qt] 18.04.2019 09:01:50 [] (unknown:0) - Found patient in the database as UId:  18
[DEBUG][Qt] 18.04.2019 09:01:50 [] (unknown:0) - Used existing study:  "1.2.840.113704.1.111.4716.1524036773.1"
[DEBUG][Qt] 18.04.2019 09:01:50 [] (unknown:0) - Study Added
[DEBUG][Qt] 18.04.2019 09:01:50 [] (unknown:0) - Need to insert new series:  "2.16.840.1.114362.1.11826050.22065096001.513296353.681.20"
[DEBUG][Qt] 18.04.2019 09:01:50 [] (unknown:0) - Series Added
[DEBUG][Qt] 18.04.2019 09:01:50 [] (unknown:0) - "DICOM indexer has successfully processed 1 files [0.04s]"
[INFO][Python] 18.04.2019 09:01:52 [Python] (C:\Program Files\Slicer 4.11.0-2018-12-21\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMWidgets.py:471) - Imported a DICOM directory, checking for extensions
[INFO][Stream] 18.04.2019 09:01:52 [] (unknown:0) - Imported a DICOM directory, checking for extensions
[DEBUG][Python] 18.04.2019 09:01:55 [Python] (C:/Program Files/Slicer 4.11.0-2018-12-21/bin/../lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine
[DEBUG][Python] 18.04.2019 09:01:55 [Python] (C:/Program Files/Slicer 4.11.0-2018-12-21/bin/../lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 0 multivolumes!
[DEBUG][Python] 18.04.2019 09:01:55 [Python] (C:/Program Files/Slicer 4.11.0-2018-12-21/bin/../lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine
[DEBUG][Python] 18.04.2019 09:01:56 [Python] (C:/Program Files/Slicer 4.11.0-2018-12-21/bin/../lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 1 multivolumes!
[DEBUG][Python] 18.04.2019 09:01:58 [Python] (C:/Program Files/Slicer 4.11.0-2018-12-21/bin/../lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:165) - MultiVolumeImportPlugin:examineMultiseries
[DEBUG][Python] 18.04.2019 09:01:58 [Python] (C:/Program Files/Slicer 4.11.0-2018-12-21/bin/../lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:170) - DICOMMultiVolumePlugin found 0 multivolumes!
[INFO][Stream] 18.04.2019 09:01:59 [] (unknown:0) - Loading series '1: RTSTRUCT: RTstruct' from file 'D:/crayon/workspace/Images/zhangyanhua/0418zyh/1/RTSTRUCT14642.1.dcm'
[INFO][Python] 18.04.2019 09:01:59 [Python] (C:/Program Files/Slicer 4.11.0-2018-12-21/bin/../lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:301) - Loading with imageIOName: GDCM
[WARNING][Python] 18.04.2019 09:02:01 [Python] (C:/Program Files/Slicer 4.11.0-2018-12-21/bin/../lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:699) - Irregular volume geometry detected, but maximum error non-zero but is within tolerance (maximum error of 2.56e-06 mm, tolerance threshold is 0.001 mm).
[INFO][Stream] 18.04.2019 09:01:59 [] (unknown:0) - Loading with imageIOName: GDCM
[CRITICAL][Stream] 18.04.2019 09:02:01 [] (unknown:0) - Irregular volume geometry detected, but maximum error non-zero but is within tolerance (maximum error of 2.56e-06 mm, tolerance threshold is 0.001 mm).
[DEBUG][Qt] 18.04.2019 09:02:03 [] (unknown:0) - Switch to module:  "Volumes"
[DEBUG][Qt] 18.04.2019 09:02:11 [] (unknown:0) - Switch to module:  "Segmentations"
[ERROR][VTK] 18.04.2019 09:03:09 [vtkSTLWriter (000000001C8A1AA0)] (D:\D\P\Slicer-0-build\VTK\IO\Geometry\vtkSTLWriter.cxx:243) - Couldn't open file: F://1: RTSTRUCT: RTstruct.stl Reason: Invalid argument
[WARNING][Qt] 18.04.2019 09:03:32 [] (unknown:0) - bool __cdecl qSlicerSegmentationsModuleWidget::copySegmentsBetweenSegmentations(bool,bool) : No segments are selected
[ERROR][VTK] 18.04.2019 09:03:35 [vtkTransformPolyDataFilter (0000000017E0C400)] (D:\D\P\Slicer-0-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data
[ERROR][VTK] 18.04.2019 09:03:35 [vtkCompositeDataPipeline (000000001DB7C670)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:709) - Input port 0 of algorithm vtkCleanPolyData(000000001D9D8A00) has 0 connections but is not optional.
[ERROR][VTK] 18.04.2019 09:03:39 [vtkCompositeDataPipeline (000000001DB7C670)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:709) - Input port 0 of algorithm vtkCleanPolyData(000000001D9D8A00) has 0 connections but is not optional.
</code></pre>
</details>

---

## Post #18 by @lassoan (2019-04-18 02:18 UTC)

<aside class="quote no-group quote-modified" data-username="labixin" data-post="17" data-topic="5797">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>[ERROR][VTK] 18.04.2019 09:03:09 [vtkSTLWriter (000000001C8A1AA0)] (D:\D\P\Slicer-0-build\VTK\IO\Geometry\vtkSTLWriter.cxx:243) - Couldn’t open file: F://1: RTSTRUCT: RTstruct.stl Reason: Invalid argument</p>
</blockquote>
</aside>
<p>This indicates that saving failed because “F://1: RTSTRUCT: RTstruct.stl” is not a valid filename. Either rename the segmentation node to not contain special character, such as colon (<code>:</code>) or use a more recent nightly version of Slicer (that removes special characters from the path automatically).</p>

---

## Post #19 by @labixin (2019-04-18 02:30 UTC)

<p>I got it, thank you! Succeed in exporting.</p>

---

## Post #20 by @cpinter (2019-04-18 15:00 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Maybe we should add the colon character to this expression<br>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/commit/2c39ac184feb665d0a1f229b9fa089656a45612a#diff-eafb0b84084b2a3d71c87526bab43e60R2347" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    
<h4>
  <a href="https://github.com/Slicer/Slicer/commit/2c39ac184feb665d0a1f229b9fa089656a45612a" target="_blank" rel="nofollow noopener">BUG: Fix export segmentation to file with illegal characters in node name</a>
</h4>

  <pre class="message" style="white-space: normal;">Re https://discourse.slicer.org/t/export-dicom-rt-structure-as-segmentation/5797
git-svn-id: http://svn.slicer.org/Slicer4/trunk@27967 3bd1e089-480b-0410-8dfb-8563597acbee</pre>

<div class="date">
  by <a href=""></a>
  on <a href="https://github.com/Slicer/Slicer/commit/2c39ac184feb665d0a1f229b9fa089656a45612a" target="_blank" rel="nofollow noopener">05:14PM - 19 Feb 19 UTC</a>
</div>

<div class="github-commit-stats">
  changed <strong>2 files</strong>
  with <strong>33 additions</strong>
  and <strong>4 deletions</strong>.
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #21 by @lassoan (2019-04-18 16:00 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="20" data-topic="5797">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Maybe we should add the colon character to this expression</p>
</blockquote>
</aside>
<p>Current code (in master branch) works well. Colon is not allowed in the filename.</p>

---

## Post #22 by @cpinter (2019-04-18 16:11 UTC)

<p>You’re right. The characters in the regexp are the allowed ones…</p>

---
