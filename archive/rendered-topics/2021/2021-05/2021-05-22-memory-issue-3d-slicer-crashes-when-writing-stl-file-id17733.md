---
topic_id: 17733
title: "Memory Issue 3D Slicer Crashes When Writing Stl File"
date: 2021-05-22
url: https://discourse.slicer.org/t/17733
---

# Memory issue (3d Slicer crashes when writing STL file)

**Topic ID**: 17733
**Date**: 2021-05-22
**URL**: https://discourse.slicer.org/t/memory-issue-3d-slicer-crashes-when-writing-stl-file/17733

---

## Post #1 by @mikelewis (2021-05-22 14:37 UTC)

<p>Hi</p>
<p>This is my first post; be gentle with me.  I have been using Slicer for a few years to segment CT or MRI scans and extract STL files for use with other CAE tools.  I don’t use it extensively, but I have used the process that is currently giving me issues many times.</p>
<p>A client has provided a CT scan to me which reads in without problems, segments fine, but Slicer crashes when I try to write a STL file of the segment.</p>
<p>The scan is 2081 x 2081 x 1995 .  The volumes output is attached.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/463de66af59a286374f679f9221c20a6147c75d2.png" data-download-href="/uploads/short-url/a1o2G8gg3fW26QkK1whDfuX57zQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/463de66af59a286374f679f9221c20a6147c75d2.png" alt="image" data-base62-sha1="a1o2G8gg3fW26QkK1whDfuX57zQ" width="690" height="414" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1081×649 16.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Note the Image spacing is not correct, in x and y the spacing is 600nm and in z it is 600 um.</p>
<p>I segment between 12 and 254 and then try to write that to a STL file, which is when Slicer crashes.  Attached is an image of memory usage at the point Slicer crashes.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8014b8e64f7f7fa3a271d516c31c452fc386754.png" data-download-href="/uploads/short-url/qfMD1nnTR507kRkWbnS2Tia9c5m.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8014b8e64f7f7fa3a271d516c31c452fc386754_2_690x375.png" alt="image" data-base62-sha1="qfMD1nnTR507kRkWbnS2Tia9c5m" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8014b8e64f7f7fa3a271d516c31c452fc386754_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8014b8e64f7f7fa3a271d516c31c452fc386754_2_1035x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8014b8e64f7f7fa3a271d516c31c452fc386754.png 2x" data-dominant-color="E5E9E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1039×565 87 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Below is the output from Help&gt;Report a bug</p>
<p>I presume this is a memory error, but I have more RAM that the 10X scan resolution.  However, I have taken just the first 500 layers of the scan, and Slicer does not crash in this case.</p>
<p>I have tried the same process on the nightly build - 4.13.0-2021-05-19 - which tells me to increase the virtual memory, but then tells me there are memory leaks (I can provide this output if required).</p>
<p>Thanks for any help in advance.</p>
<p>Regards,</p>
<p>Mike</p>
<p>[DEBUG][Qt] 22.05.2021 11:19:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2021-05-22 11:19:30<br>
[DEBUG][Qt] 22.05.2021 11:19:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 4.11.20210226 (revision 29738 / 7a593c8) win-amd64 - installed release<br>
[DEBUG][Qt] 22.05.2021 11:19:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 19041, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 22.05.2021 11:19:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 262065 MB physical, 366513 MB virtual<br>
[DEBUG][Qt] 22.05.2021 11:19:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 56 cores, 56 logical processors<br>
[DEBUG][Qt] 22.05.2021 11:19:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 22.05.2021 11:19:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 22.05.2021 11:19:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 22.05.2021 11:19:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 22.05.2021 11:19:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/mike.lewis/AppData/Local/NA-MIC/Slicer 4.11.20210226/bin<br>
[DEBUG][Qt] 22.05.2021 11:19:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 22.05.2021 11:19:35 [Python] (C:\Users\mike.lewis\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[DEBUG][Python] 22.05.2021 11:19:40 [Python] (C:\Users\mike.lewis\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 22.05.2021 11:19:41 [Python] (C:\Users\mike.lewis\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 22.05.2021 11:19:41 [Python] (C:\Users\mike.lewis\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 22.05.2021 11:19:41 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[ERROR][VTK] 22.05.2021 11:23:45 [vtkITKArchetypeDiffusionTensorImageReaderFile (0000025137F1B380)] (D:\D\S\Slicer-1\Libs\vtkITK\vtkITKArchetypeDiffusionTensorImageReaderFile.cxx:166) - There is more than one file, use the vtkITKArchetypeImageSeriesReader instead<br>
[INFO][VTK] 22.05.2021 11:25:12 [vtkMRMLVolumeArchetypeStorageNode (000002514BD122C0)] (D:\D\S\Slicer-1\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:509) - Loaded volume from file: D:/Dropbox/Exchange/BioMedical/OxfordBioMedical/VOI_diameter_1,3mm/meniscotot_ir_rec_voi__cor_voi_00001032.bmp. Dimensions: 2081x2081x1995. Number of components: 3. Pixel type: unsigned char.<br>
[DEBUG][Qt] 22.05.2021 11:25:12 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Volume” Reader has successfully read the file “D:/Dropbox/Exchange/BioMedical/OxfordBioMedical/VOI_diameter_1,3mm/meniscotot_ir_rec_voi__cor_voi_00001032.bmp” “[95.82s]”<br>
[DEBUG][Qt] 22.05.2021 11:25:51 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Volumes”<br>
[WARNING][Qt] 22.05.2021 11:25:51 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-1-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 22.05.2021 11:25:51 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-1-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 22.05.2021 11:25:51 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-1-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 22.05.2021 11:25:51 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-1-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 22.05.2021 11:25:51 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-1-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 22.05.2021 11:25:51 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-1-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 22.05.2021 11:25:51 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-1-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 22.05.2021 11:25:51 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-1-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 22.05.2021 11:25:51 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-1-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 22.05.2021 11:25:51 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-1-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 22.05.2021 11:25:51 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-1-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[DEBUG][Qt] 22.05.2021 11:31:14 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “SegmentEditor”<br>
[DEBUG][Qt] 22.05.2021 11:32:54 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Segmentations”</p>

---

## Post #2 by @muratmaga (2021-05-22 15:26 UTC)

<p>Couple quick comments:</p>
<ol>
<li>Log doesn’t indicate the crash, are you sure this is from the session that crashed? When you go to file a bug, you want to choose the one down in the droplist (as the top is the active slicer session).</li>
<li>You seem to load data from a cloud syncing drive. It is a small chance, but strange things happens when you try to read/write to these folder, I would suggest testing from a non-synced folder.</li>
<li>You have an enormously anisotropic data, because you said the correct spacing is 600nm in XY and 600um in Z (a 1000 folds difference, is that really true?). If maintaining correct proportions in slicer you need to change your spacing to 1x1x1000. But such highly anisotropic data would create all sorts of issues in segmentation. So I would suggest first checking whether that’s indeed correct spacing and then decide how to proceed.</li>
<li>In your screenshot above, your volume data type is a vector (as oppose to scalar). CT volumes are typically not vector. That might be the culprit with your crash.  If it is not vector (multichannel image), you can try to use the <code>VectorToScalar</code> module to create a new volume of correct data type, segment and try to save it and see if it works.</li>
</ol>

---

## Post #3 by @mikelewis (2021-05-25 13:23 UTC)

<p>Hi - thanks for the response.</p>
<p>1&amp;2 This is the response from the log file, and I tried writing the stl file to a non cloud syncing drive, where I get a different error message.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30e89f0f904d76436a3148231a07a9725c05a161.png" alt="image" data-base62-sha1="6YFj3YkheeSCydZ1GHDslJTnHm9" width="217" height="137"></p>
<p>a memory diagnostics test shows no errors.  So it’s not clear to me what this memory error is.</p>
<p>3 This is a mistype/misread from me - Z is 600 nm as well.</p>
<p>4 I have tried this and doesn’t seem to make a difference.  However, Resource Monitor says there are up to 4 Hard Faults/sec just before Slicer crashes.</p>
<p>Regards,</p>
<p>Mike</p>

---

## Post #4 by @pieper (2021-05-25 19:31 UTC)

<aside class="quote no-group" data-username="mikelewis" data-post="1" data-topic="17733">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/96bed5/48.png" class="avatar"> mikelewis:</div>
<blockquote>
<p>2081 x 2081 x 1995</p>
</blockquote>
</aside>
<p>That’s a pretty large volume, and depending on the structure it could lead to an extremely large stl file that may push some limits.</p>
<p>If you can come up with a way to replicate this issue using public data others could investigate.</p>

---

## Post #5 by @muratmaga (2021-05-25 19:45 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="17733">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>structure it could lead to an extremely large stl file that may push some limits.</p>
</blockquote>
</aside>
<p>That was what I was thinking too.<br>
<a class="mention" href="/u/mikelewis">@mikelewis</a> does the error continue to persist if you try to write other model format (PLY, OBJ, VTK)? Can you tell us what the model size is (use Models module and expand the information tab).</p>
<p>Also, can you try to downsample the volume before segmentation (use crop volume by a factor of 2 or more) and repeat the segmentation and see if error goes away? If it does, it might have something to do with how large the model is.</p>

---
