# Error, export to DICOM

**Topic ID**: 12429
**Date**: 2020-07-07
**URL**: https://discourse.slicer.org/t/error-export-to-dicom/12429

---

## Post #1 by @cotozakot (2020-07-07 20:26 UTC)

<p>I want to export segmentation to a DICOM file. Unfortunately, an error appears all the time.</p>
<p>Warning: Warning: 718 of 718 selected files listed in the database cannot be found on disk.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e8eb9c629c32ea1cfa4417a1ba6ddb92415279d.png" alt="image" data-base62-sha1="kl7AwK05NsMypH46K1CmPPAdwIZ" width="530" height="153"></p>

---

## Post #2 by @lassoan (2020-07-07 20:31 UTC)

<p>Have you imported the data sets from removable storage (DVD, USB drive, external hard drive)? Do you still have it plugged in?</p>
<p>Which Slicer version do you use?</p>

---

## Post #3 by @cotozakot (2020-07-08 06:52 UTC)

<p>Yes, I imported data from a disc. However, I have them in a folder on my computer. Version is 4.11.0</p>
<p>wt., 7 lip 2020, 22:42 użytkownik Andras Lasso via 3D Slicer Community &lt;<a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a>&gt; napisał:</p>

---

## Post #4 by @cpinter (2020-07-08 08:41 UTC)

<p>4.11.0 with which date?</p>
<p>Is it possible that a folder in the full path contains a non-ascii character? If so, can you try to import it from a folder the full path of which has only ascii characters and no spaces?</p>

---

## Post #5 by @lassoan (2020-07-08 12:08 UTC)

<p>Please also upload the application log somewhere (menu: Help / Report a bug) and post the link here.</p>

---

## Post #6 by @Varsha (2021-03-10 08:08 UTC)

<p>I am facing a similar problem. How can this issue be corrected?</p>

---

## Post #7 by @cotozakot (2021-03-10 08:42 UTC)

<p>I am not able to help you. I have not solved this problem so far.<br>
Sylwia Bień</p>

---

## Post #8 by @lassoan (2021-03-10 16:27 UTC)

<p><a class="mention" href="/u/varsha">@Varsha</a> If you use the latest Slicer Stable Release and still have problems with exporting DICOM then please describe what you did exactly, what you expected to happen, and what happened instead. Also post the application log here of a failed export (menu: Help / Report a bug).</p>

---

## Post #9 by @Varsha (2021-03-11 17:34 UTC)

<p>When attempting to import DICOM images, the message displayed is 0 patients. Even after using DICOM patcher the problem is not corrected. On using other DICOm readers to import the images under Applications, the message displayed is Updating database and this continues for almost 6 hours before images are loaded.</p>

---

## Post #10 by @Varsha (2021-03-11 17:42 UTC)

<p>DEBUG][Qt] 11.03.2021 22:42:54 [] (unknown:0) - Session start time …: 2021-03-11 22:42:54<br>
[DEBUG][Qt] 11.03.2021 22:42:54 [] (unknown:0) - Slicer version …: 4.11.20200930 (revision 29402 / 002be18) win-amd64 - installed release<br>
[DEBUG][Qt] 11.03.2021 22:42:54 [] (unknown:0) - Operating system …: Windows / Personal / (Build 19041, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 11.03.2021 22:42:54 [] (unknown:0) - Memory …: 8107 MB physical, 13927 MB virtual<br>
[DEBUG][Qt] 11.03.2021 22:42:54 [] (unknown:0) - CPU …: GenuineIntel , 4 cores, 4 logical processors<br>
[DEBUG][Qt] 11.03.2021 22:42:54 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 11.03.2021 22:42:54 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 11.03.2021 22:42:54 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 11.03.2021 22:42:54 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 11.03.2021 22:42:54 [] (unknown:0) - Application path …: C:/Users/Varsha Warrier/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin<br>
[DEBUG][Qt] 11.03.2021 22:42:54 [] (unknown:0) - Additional module paths …: C:/Users/Varsha Warrier/AppData/Roaming/NA-MIC/Extensions-29402/AnglePlanesExtension/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Varsha Warrier/AppData/Roaming/NA-MIC/Extensions-29402/BoneTextureExtension/lib/Slicer-4.11/cli-modules, C:/Users/Varsha Warrier/AppData/Roaming/NA-MIC/Extensions-29402/BoneTextureExtension/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Varsha Warrier/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRadiomics/lib/Slicer-4.11/cli-modules, C:/Users/Varsha Warrier/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRadiomics/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Varsha Warrier/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRT/lib/Slicer-4.11/cli-modules, C:/Users/Varsha Warrier/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRT/lib/Slicer-4.11/qt-loadable-modules, C:/Users/Varsha Warrier/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRT/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Varsha Warrier/AppData/Roaming/NA-MIC/Extensions-29402/EasyClip/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Varsha Warrier/AppData/Roaming/NA-MIC/Extensions-29402/SlicerDevelopmentToolbox/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Varsha Warrier/AppData/Roaming/NA-MIC/Extensions-29402/PETDICOMExtension/lib/Slicer-4.11/cli-modules, C:/Users/Varsha Warrier/AppData/Roaming/NA-MIC/Extensions-29402/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Varsha Warrier/AppData/Roaming/NA-MIC/Extensions-29402/DCMQI/lib/Slicer-4.11/cli-modules<br>
[DEBUG][Python] 11.03.2021 22:42:58 [Python] (C:\Users\Varsha Warrier\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[DEBUG][Python] 11.03.2021 22:42:59 [Python] (C:\Users\Varsha Warrier\AppData\Roaming\NA-MIC\Extensions-29402\SlicerRadiomics\Lib\site-packages\pykwalify\compat.py:20) - Using yaml library: C:\Users\Varsha Warrier\AppData\Roaming\NA-MIC\Extensions-29402\SlicerRadiomics\Lib\sit</p>

---

## Post #11 by @lassoan (2021-03-24 16:03 UTC)

<p>If you can upload logs of an attempted DICOM import somewhere (dropbox, onedrive, etc.) and post the link here then we can investigate. If you can share the data set with us (upload somewhere and post the link) then we can ensure that Slicer’s importer works well with it.</p>

---
