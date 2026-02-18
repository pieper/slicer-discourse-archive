# Slicer crashing during Model Making

**Topic ID**: 18534
**Date**: 2021-07-06
**URL**: https://discourse.slicer.org/t/slicer-crashing-during-model-making/18534

---

## Post #1 by @lna090001 (2021-07-06 16:39 UTC)

<p>My slicer keeps crashing during model making. I load my volume, adjust the dimensions and use the legacy editor to segment (it is what i am used to). After I have generated a label map, I will use the model maker button to make a model. Often times slicer crashes when I go to open model maker and observe the volume (mm3) of the model. I lose hours of work each time it crashes. Please help. I have a good graphics card and 32 gb memory.</p>
<p>Problem report for Slicer 4.11.20200930 win-amd64: [please describe expected and actual behavior]</p>
<p>[DEBUG][Qt] 06.07.2021 10:21:47 [] (unknown:0) - Session start time …: 2021-07-06 10:21:47<br>
[DEBUG][Qt] 06.07.2021 10:21:47 [] (unknown:0) - Slicer version …: 4.11.20200930 (revision 29402 / 002be18) win-amd64 - installed release<br>
[DEBUG][Qt] 06.07.2021 10:21:47 [] (unknown:0) - Operating system …: Windows /  Professional / (Build 19042, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 06.07.2021 10:21:47 [] (unknown:0) - Memory …: 32716 MB physical, 55366 MB virtual<br>
[DEBUG][Qt] 06.07.2021 10:21:47 [] (unknown:0) - CPU …: AuthenticAMD AMD Ryzen 5 3600 6-Core Processor              , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 06.07.2021 10:21:47 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 06.07.2021 10:21:47 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 06.07.2021 10:21:47 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 06.07.2021 10:21:47 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 06.07.2021 10:21:47 [] (unknown:0) - Application path …: C:/Users/Lori/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin<br>
[DEBUG][Qt] 06.07.2021 10:21:47 [] (unknown:0) - Additional module paths …: C:/Users/Lori/AppData/Roaming/NA-MIC/Extensions-29402/BoneTextureExtension/lib/Slicer-4.11/cli-modules, C:/Users/Lori/AppData/Roaming/NA-MIC/Extensions-29402/BoneTextureExtension/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Lori/AppData/Roaming/NA-MIC/Extensions-29402/BoneThicknessMapping/lib/Slicer-4.11/qt-scripted-modules<br>
[DEBUG][Python] 06.07.2021 10:21:50 [Python] (C:\Users\Lori\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[DEBUG][Python] 06.07.2021 10:21:53 [Python] (C:\Users\Lori\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 06.07.2021 10:21:54 [Python] (C:\Users\Lori\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 06.07.2021 10:21:54 [Python] (C:\Users\Lori\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 06.07.2021 10:21:54 [] (unknown:0) - Switch to module:  “Volumes”<br>
[WARNING][Qt] 06.07.2021 10:21:54 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  242<br>
[WARNING][Qt] 06.07.2021 10:21:54 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  242<br>
[WARNING][Qt] 06.07.2021 10:21:54 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  242<br>
[WARNING][Qt] 06.07.2021 10:21:54 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  242<br>
[WARNING][Qt] 06.07.2021 10:21:54 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 06.07.2021 10:21:54 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 06.07.2021 10:21:54 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 06.07.2021 10:21:54 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 06.07.2021 10:21:54 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 06.07.2021 10:21:54 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 06.07.2021 10:21:54 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 06.07.2021 10:21:54 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 06.07.2021 10:21:54 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 06.07.2021 10:21:54 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 06.07.2021 10:21:54 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 06.07.2021 10:21:54 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253</p>

---

## Post #2 by @lassoan (2021-07-06 16:43 UTC)

<p>Legacy Editor based workflows are not supported anymore. You can use Segment Editor module instead and enable 3D display by clicking on “Show 3D” button.</p>
<p>If you can reproduce a crash without using the legacy Editor module then please share the scene (upload somewhere and post the link here) and we’ll fix that. Thank you!</p>

---
