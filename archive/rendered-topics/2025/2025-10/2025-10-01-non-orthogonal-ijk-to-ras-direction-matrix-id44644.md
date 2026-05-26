---
topic_id: 44644
title: "Non-orthogonal IJK to RAS Direction Matrix"
date: 2025-10-01
url: https://discourse.slicer.org/t/44644
last_bumped: 2026-04-24T12:58:57.192Z
---

# Non-orthogonal IJK to RAS Direction Matrix

**Topic ID**: 44644
**Date**: 2025-10-01
**URL**: https://discourse.slicer.org/t/non-orthogonal-ijk-to-ras-direction-matrix/44644

---

## Post #1 by @mwirtz (2025-10-01 15:39 UTC)

<p>Hey there!<br>
I am trying to load CT scans via the DICOM module, which have a non-zero GantryDetectorTilt (not 100% sure it is related) and it seems to cause a non-orthogonal IJK to RAS matrix (see screenshot). Also the case appear “skewed”, i.e. with a shearing angle, in 3D Slicer (see screenshot).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bb48396f2e74f01fba018c8fcac4e50412ac8c8.jpeg" data-download-href="/uploads/short-url/hEltERRYSQCzAJTM0nNp4hkkZZe.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bb48396f2e74f01fba018c8fcac4e50412ac8c8_2_690x230.jpeg" alt="image" data-base62-sha1="hEltERRYSQCzAJTM0nNp4hkkZZe" width="690" height="230" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bb48396f2e74f01fba018c8fcac4e50412ac8c8_2_690x230.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bb48396f2e74f01fba018c8fcac4e50412ac8c8_2_1035x345.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bb48396f2e74f01fba018c8fcac4e50412ac8c8_2_1380x460.jpeg 2x" data-dominant-color="464646"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2152×718 273 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For this case, the ImageOrientationPatient in the DICOM file is:<br>
<code>(0020,0037) DS [1\0\0\0\0.99357185567659-0.1132032137679] #  42, 6 ImageOrientationPatient</code></p>
<p>I would’ve expected that 3DSlicer complements the perpendicular axis by the cross product, which would lead to an IJK to RAS Direction Matrix of e.g.:<br>
```<br>
<code>[-1, 0, 0]</code><br>
<code>[0 -0.9936, -0.1132]</code><br>
<code>[0, -0.1132, 0.9936]</code><br>
```<br>
I already played a bit around with the settings in Edit→Settings→DICOM (acquisition geometry reularization) but could not make it orthogonal.</p>
<p>Any ideas?</p>

---

## Post #2 by @pieper (2025-10-01 16:08 UTC)

<p>That should be handled directly with the acquisition transform when you load from DICOM.  Did you try hardening the volume through the transform?</p>

---

## Post #3 by @pieper (2025-10-01 16:13 UTC)

<p>Also this looks suspicious - there should be only numbers and backslashes in this value.</p>
<aside class="quote no-group" data-username="mwirtz" data-post="1" data-topic="44644">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/3da27b/48.png" class="avatar"> mwirtz:</div>
<blockquote>
<p>(0020,0037) DS [1\0\0\0\0.99357185567659-0.1132032137679] # 42, 6</p>
</blockquote>
</aside>
<p>Was this data processed by some other software or did it come straight from a scanner?</p>

---

## Post #4 by @mwirtz (2025-10-01 18:35 UTC)

<p>Yes, I tried the option <code>harden regularization transform</code> without success.</p>
<p>Sorry, the DICOM tag was copied from a DICOM visualization software, no clue why a backslash got lost… Accessing the tag directly via <code>pydicom.dcmread()</code> shows no apparent issue though - as far as I can see:</p>
<pre><code class="lang-auto">Python 3.12.10 (main, Apr  9 2025, 04:03:51) [Clang 20.1.0 ] on linux
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import pydicom
&gt;&gt;&gt; pydicom.dcmread("ffc7e0e2fe27516c387ca0e908a40b25.dcm").ImageOrientationPatient
[1, 0, 0, 0, 0.99357185567659, -0.1132032137679]
</code></pre>

---

## Post #5 by @pieper (2025-10-01 18:53 UTC)

<p>Can you answer this question and provide any other context?</p>
<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="44644">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Was this data processed by some other software or did it come straight from a scanner?</p>
</blockquote>
</aside>
<p>I ask because I’m surprised the acquisition transform didn’t work since it relies on the per-slice position and orientation data from the dicom header.  Is the scan perhaps a multiframe image? (all slices are in one file?)</p>

---

## Post #6 by @lassoan (2025-10-02 21:19 UTC)

<p>Loading of tilted-gantry images should work well. There must be something unusual in your image that prevents this mechanism to work. Is the file stored in enhanced multiframe format (single file for the entire 3D stack)? Could you copy all messages related to acquisition normalization that are logged when you load the image (you can access the logs in menu: Help → Report a bug).</p>

---

## Post #7 by @mwirtz (2026-04-24 09:09 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> no, no multiframe format. There are 172 individual DICOM files with regards to this scan in my database (each hosting one 2D slice). Here are the requested logs of 3DSlicer, when retreiving and loading the scan via the DICOM module (lots of critical Qt errors without further info). Thanks fir looking into it!</p>
<p>[DEBUG][Qt] 24.04.2026 09:47:40 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Session start time …: 20260424_094740<br>
[DEBUG][Qt] 24.04.2026 09:47:40 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Slicer version …: 5.10.0 (revision 34045 / a2b6d08) win-amd64 - installed release<br>
[DEBUG][Qt] 24.04.2026 09:47:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 22631, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 24.04.2026 09:47:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Memory …: 81750 MB physical, 100190 MB virtual<br>
[DEBUG][Qt] 24.04.2026 09:47:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - CPU …: GenuineIntel , 16 cores, 16 logical processors<br>
[DEBUG][Qt] 24.04.2026 09:47:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 24.04.2026 09:47:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 24.04.2026 09:47:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - DCMTK configuration …: version 3.6.8, no SSL<br>
[DEBUG][Qt] 24.04.2026 09:47:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 24.04.2026 09:47:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Developer mode …: enabled<br>
[DEBUG][Qt] 24.04.2026 09:47:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Application path …: C:/ProgramData/slicer.org/3D Slicer 5.10.0/bin<br>
[DEBUG][Qt] 24.04.2026 09:47:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Additional module paths ..: <a href="http://slicer.org/Extensions-34045/SlicerDevelopmentToolbox/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/SlicerDevelopmentToolbox/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/DCMQI/lib/Slicer-5.10/cli-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/DCMQI/lib/Slicer-5.10/cli-modules</a>, <a href="http://slicer.org/Extensions-34045/QuantitativeReporting/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/QuantitativeReporting/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/PETDICOMExtension/lib/Slicer-5.10/cli-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/PETDICOMExtension/lib/Slicer-5.10/cli-modules</a>, <a href="http://slicer.org/Extensions-34045/PETDICOMExtension/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/PETDICOMExtension/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/DebuggingTools/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/DebuggingTools/lib/Slicer-5.10/qt-scripted-modules</a>, E:/dev/Software/slicer_h5_visualizer/H5Visualizer, <a href="http://slicer.org/Extensions-34045/PyTorch/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/PyTorch/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/NNUNet/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/NNUNet/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/SlicerPythonTestRunner/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/SlicerPythonTestRunner/lib/Slicer-5.10/qt-scripted-modules</a>, E:/dev/Software/slicer_annotation_extension/AnnotateSegObj<br>
[INFO][Stream] 24.04.2026 09:47:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -<br>
[INFO][Python] 24.04.2026 09:47:48 [Python] (C:\ProgramData\slicer.org\3D Slicer 5.10.0\lib\Python\Lib\site-packages\numexpr\utils.py:164) - NumExpr defaulting to 16 threads.<br>
[DEBUG][Python] 24.04.2026 09:47:52 [Python] (C:\ProgramData\slicer.org\3D Slicer 5.10.0\lib\Python\Lib\site-packages\h5py_<em>init</em>_.py:47) - Creating converter from 7 to 5<br>
[DEBUG][Python] 24.04.2026 09:47:52 [Python] (C:\ProgramData\slicer.org\3D Slicer 5.10.0\lib\Python\Lib\site-packages\h5py_<em>init</em>_.py:47) - Creating converter from 5 to 7<br>
[DEBUG][Python] 24.04.2026 09:47:52 [Python] (C:\ProgramData\slicer.org\3D Slicer 5.10.0\lib\Python\Lib\site-packages\h5py_<em>init</em>_.py:47) - Creating converter from 7 to 5<br>
[DEBUG][Python] 24.04.2026 09:47:52 [Python] (C:\ProgramData\slicer.org\3D Slicer 5.10.0\lib\Python\Lib\site-packages\h5py_<em>init</em>_.py:47) - Creating converter from 5 to 7<br>
[DEBUG][Python] 24.04.2026 09:47:55 [Python] (C:\ProgramData\slicer.org\3D Slicer 5.10.0\lib\Slicer-5.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 24.04.2026 09:47:55 [Python] (C:\ProgramData\slicer.org\3D Slicer 5.10.0\lib\Slicer-5.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 24.04.2026 09:47:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 24.04.2026 09:48:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “DICOM”<br>
[CRITICAL][Qt] 24.04.2026 09:49:53 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:53 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:53 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 1<br>
[CRITICAL][Qt] 24.04.2026 09:49:53 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:53 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:53 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:53 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:53 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:53 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:53 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:55 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:56 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:49:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:05 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:05 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:05 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:05 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:05 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:05 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:05 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:05 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 0<br>
[CRITICAL][Qt] 24.04.2026 09:50:05 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 2<br>
[CRITICAL][Qt] 24.04.2026 09:50:05 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 3<br>
[CRITICAL][Qt] 24.04.2026 09:50:05 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - setting value to 100<br>
[DEBUG][Python] 24.04.2026 09:50:48 [Python] (C:\ProgramData\slicer.org\3D Slicer 5.10.0\slicer.org\Extensions-34045\QuantitativeReporting\lib\Slicer-5.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMM3DPluginClass : Caching files<br>
[DEBUG][Python] 24.04.2026 09:50:48 [Python] (C:\ProgramData\slicer.org\3D Slicer 5.10.0\slicer.org\Extensions-34045\QuantitativeReporting\lib\Slicer-5.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMM3DPluginClass : Using cached files<br>
[DEBUG][Python] 24.04.2026 09:50:48 [Python] (C:\ProgramData\slicer.org\3D Slicer 5.10.0\slicer.org\Extensions-34045\QuantitativeReporting\lib\Slicer-5.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 24.04.2026 09:50:48 [Python] (C:\ProgramData\slicer.org\3D Slicer 5.10.0\slicer.org\Extensions-34045\QuantitativeReporting\lib\Slicer-5.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 24.04.2026 09:50:48 [Python] (C:\ProgramData\slicer.org\3D Slicer 5.10.0\slicer.org\Extensions-34045\QuantitativeReporting\lib\Slicer-5.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 24.04.2026 09:50:48 [Python] (C:\ProgramData\slicer.org\3D Slicer 5.10.0\slicer.org\Extensions-34045\QuantitativeReporting\lib\Slicer-5.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMSegmentationPluginClass : Using cached files<br>
[DEBUG][Python] 24.04.2026 09:50:48 [Python] (C:\ProgramData\slicer.org\3D Slicer 5.10.0\slicer.org\Extensions-34045\QuantitativeReporting\lib\Slicer-5.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[DEBUG][Python] 24.04.2026 09:50:49 [Python] (C:\ProgramData\slicer.org\3D Slicer 5.10.0\slicer.org\Extensions-34045\QuantitativeReporting\lib\Slicer-5.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[INFO][Python] 24.04.2026 09:50:49 [Python] (C:/ProgramData/slicer.org/3D Slicer 5.10.0/bin/../lib/Slicer-5.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 24.04.2026 09:50:50 [Python] (C:/ProgramData/slicer.org/3D Slicer 5.10.0/bin/../lib/Slicer-5.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:567) - DICOM window/level (40.0/120.0) set to volume ‘3: CRANEO NIÑ  1.5  H21s’ from SOP instance 1.2.276.0.20.1.4.19.91760167158.6528.1717682259.893772.31.<br>
[DEBUG][Python] 24.04.2026 09:50:50 [Python] (C:/ProgramData/slicer.org/3D Slicer 5.10.0/bin/../lib/Slicer-5.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:567) - DICOM window/level (700.0/3200.0) set to volume ‘3: CRANEO NIÑ  1.5  H21s’ from SOP instance 1.2.276.0.20.1.4.19.91760167158.6528.1717682259.893772.31.</p>

---

## Post #8 by @mwirtz (2026-04-24 09:15 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> as far as I can tell from the DICOM files, the scan came right from a Siemens SOMATOM Definition AS+ scanner. Unfortunately, I do not have the rights to share the original DICOM files here <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=15" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @pieper (2026-04-24 12:58 UTC)

<p>Since you have some python experience, you should be able to trace through the scalar volume reader to see what might be happening.  Try asking an LLM about this method:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L920">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L920" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L920" target="_blank" rel="noopener">Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L920" rel="noopener"><code>main</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="910" style="counter-reset: li-counter 909 ;">
          <li>    mapped the slice corners to match the dicom acquisition.</li>
          <li>    """</li>
          <li>    _columns, _rows, slices = volumeNode.GetImageData().GetDimensions()</li>
          <li>    worldCorners = numpy.zeros(shape=[slices, 2, 2, 3])</li>
          <li>    for slice in range(slices):</li>
          <li>        for row in range(2):</li>
          <li>            for column in range(2):</li>
          <li>                volumeNode.TransformPointToWorld(corners[slice, row, column], worldCorners[slice, row, column])</li>
          <li>    return worldCorners</li>
          <li></li>
          <li class="selected">def createAcquisitionTransform(self, volumeNode, addAcquisitionTransformIfNeeded=True, hardenAcquisitionTransform=False):</li>
          <li>    """Creates the actual transform if needed.</li>
          <li>    Slice corners are cached for inspection by tests</li>
          <li>    """</li>
          <li>    self.originalCorners = self.sliceCornersFromIJKToRAS(volumeNode)</li>
          <li>    self.targetCorners = self.sliceCornersFromDICOM(volumeNode)</li>
          <li>    if self.originalCorners is None or self.targetCorners is None:</li>
          <li>        # can't create transform without corner information</li>
          <li>        return</li>
          <li>    maxError = (abs(self.originalCorners - self.targetCorners)).max()</li>
          <li></li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You can add debug code to print the slice corners and see if there’s something going on this code doesn’t expect.</p>

---
