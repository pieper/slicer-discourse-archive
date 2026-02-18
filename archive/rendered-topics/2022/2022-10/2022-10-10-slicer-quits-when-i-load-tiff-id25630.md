# Slicer quits when I load TIFF

**Topic ID**: 25630
**Date**: 2022-10-10
**URL**: https://discourse.slicer.org/t/slicer-quits-when-i-load-tiff/25630

---

## Post #1 by @rtlim (2022-10-10 21:17 UTC)

<p><strong>Operating system</strong>: Windows 10 Enterprise<br>
<strong>Slicer version</strong>: 5.0.3<br>
I’ve been trying to load a TIFF file into Slicer but it keeps quitting whenever I try. I’ve tried using the “Add Data” button as well as loading through ImageStacks in SlicerMorph. When I try loading the TIFF file with the “Add Data” button, I click “Choose File(s) to Add”, then I check the “Show Options” button and I uncheck “Single File”. However, this is still not working and the program quits before the image can load in the viewing module. I’ve tried uninstalling and reinstalling Slicer but to no avail. Is there any advice for what else I can do?</p>
<p>Below is the log file content for when I try to load it:<br>
[DEBUG][Qt] 10.10.2022 10:37:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2022-10-10 10:37:02<br>
[DEBUG][Qt] 10.10.2022 10:37:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.0.3 (revision 30893 / 7ea0f43) win-amd64 - installed release<br>
[DEBUG][Qt] 10.10.2022 10:37:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 19042, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 10.10.2022 10:37:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 16106 MB physical, 22506 MB virtual<br>
[DEBUG][Qt] 10.10.2022 10:37:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
[DEBUG][Qt] 10.10.2022 10:37:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 10.10.2022 10:37:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 10.10.2022 10:37:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 10.10.2022 10:37:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 10.10.2022 10:37:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/rtlim/AppData/Local/NA-MIC/Slicer 5.0.3/bin<br>
[DEBUG][Qt] 10.10.2022 10:37:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: NA-MIC/Extensions-30893/CleverSeg/lib/Slicer-5.0/qt-loadable-modules, NA-MIC/Extensions-30893/CleverSeg/lib/Slicer-5.0/qt-scripted-modules, NA-MIC/Extensions-30893/SegmentEditorExtraEffects/lib/Slicer-5.0/qt-loadable-modules, NA-MIC/Extensions-30893/SegmentEditorExtraEffects/lib/Slicer-5.0/qt-scripted-modules, NA-MIC/Extensions-30893/SlicerMorph/lib/Slicer-5.0/qt-scripted-modules, NA-MIC/Extensions-30893/MarkupsToModel/lib/Slicer-5.0/qt-loadable-modules<br>
[WARNING][Qt] 10.10.2022 10:37:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space<br>
[WARNING][Qt] 10.10.2022 10:37:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile<br>
[DEBUG][Python] 10.10.2022 10:37:04 [Python] (C:\Users\rtlim\AppData\Local\NA-MIC\Slicer 5.0.3\lib\Slicer-5.0\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 10.10.2022 10:37:05 [Python] (C:\Users\rtlim\AppData\Local\NA-MIC\Slicer 5.0.3\lib\Slicer-5.0\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 10.10.2022 10:37:05 [Python] (C:\Users\rtlim\AppData\Local\NA-MIC\Slicer 5.0.3\lib\Slicer-5.0\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Python] 10.10.2022 10:37:06 [Python] (C:\Users\rtlim\AppData\Local\NA-MIC\Slicer 5.0.3\lib\Slicer-5.0\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: FormatMarkups<br>
[DEBUG][Qt] 10.10.2022 10:37:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”</p>

---

## Post #2 by @pieper (2022-10-10 21:31 UTC)

<p>People use tiff in many different ways and probably this data uses some convention Slicer’s not compatible with.  If the tiff is a 3D volume you can probably convert it to nrrd with something like imagej.</p>

---

## Post #3 by @rtlim (2022-10-11 03:10 UTC)

<p>Is there any way I could still load it in Slicer or convert it in Slicer? I have a ton of images that have already been saved as tiff files and it would be a big pain to have to convert all of them.</p>

---

## Post #4 by @muratmaga (2022-10-11 04:30 UTC)

<p>If both ImageStacks and Data module fails, there is likely something different about the data. If you can share one dataset, we can try to see what the issue might be. Otherwise, it is hard to guess what the cause might be.</p>

---

## Post #5 by @rtlim (2022-10-11 04:45 UTC)

<p>I couldn’t upload the tiff file and I’m not quite sure how else to put it in the forum, but <a href="https://drive.google.com/uc?export=download&amp;id=1ALQumSEpUzcj8vatNB_uO5AzOIlPp3uN" rel="noopener nofollow ugc">this link</a> should hopefully allow you to download the file. Thanks!</p>

---

## Post #6 by @muratmaga (2022-10-11 16:08 UTC)

<p>You have a multiframe tiff file, where each slice is different in size. That’s not the type of datasets 3D Slicer is designed for. Slicer is expecting a sequence of images with exact dimensions in each slice, and when stacked it constitutes a 3D volume of the structure</p>
<p>Given that this is a histology dataset, and not in 3D in nature (all I saw was a single slide), I don’t think 3D Slicer is not going to be very useful to you. probably ImageJ/FiJI would be better. What do you need the Slicer to do on this data?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1e2207044faec2501fd801f037ce89a132fe8b9.jpeg" data-download-href="/uploads/short-url/tWIgsRjn1G98e9Yc3mXrHnU0u5H.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1e2207044faec2501fd801f037ce89a132fe8b9_2_491x500.jpeg" alt="image" data-base62-sha1="tWIgsRjn1G98e9Yc3mXrHnU0u5H" width="491" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1e2207044faec2501fd801f037ce89a132fe8b9_2_491x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1e2207044faec2501fd801f037ce89a132fe8b9_2_736x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1e2207044faec2501fd801f037ce89a132fe8b9_2_982x1000.jpeg 2x" data-dominant-color="8D7F87"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1885×1917 251 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @rtlim (2022-10-11 19:12 UTC)

<p>Ah I see. I’m using Slicer to contour certain cells in these images. I’ve tried ImageJ before but the plugins for contouring haven’t worked very well. I’ll look into writing a script to convert the TIFF files to PNG so I don’t have to do it manually then. Thanks for all of your help.</p>

---

## Post #8 by @curtislisle (2022-10-11 21:51 UTC)

<p>You might want to investigate the open-source package QuPath to handle pyramidal TIFF files. QuPath is designed specifically for this type of histology imagery and it allow for annotations to be created through the interface. It can be downloaded here: <a href="https://qupath.github.io/" rel="noopener nofollow ugc">https://qupath.github.io/</a></p>

---
