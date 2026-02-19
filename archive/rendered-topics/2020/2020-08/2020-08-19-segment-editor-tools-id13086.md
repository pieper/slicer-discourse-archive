---
topic_id: 13086
title: "Segment Editor Tools"
date: 2020-08-19
url: https://discourse.slicer.org/t/13086
---

# Segment editor tools

**Topic ID**: 13086
**Date**: 2020-08-19
**URL**: https://discourse.slicer.org/t/segment-editor-tools/13086

---

## Post #1 by @Reham_Hassan (2020-08-19 13:07 UTC)

<p>Operating system:mac os 10.15.5<br>
Slicer version:4.11.0<br>
Expected behavior:<br>
Actual behavior:<br>
Im new to the slicer app , just started the summer course, yesterday in the course showing the segment editor, i had fewer tools than the instructor, who suggested that the problem with the slicer morph extension installation<br>
i removed and reinstalled it but it didn’t work<br>
will this affect today’s topic mainly using SlicerMorph including  landmark-based geometric morphometrics, GPA module</p>
<p>OR is there is a method to check if the installation process is correct</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-08-19 13:40 UTC)

<p>If you have any doubts that extensions are successfully installed, uninstall them, and reinstall. Wait until you are asked to install additional dependencies and choose to install all of them. To make sure they are all completely installed, wait 5 minutes before restarting Slicer.</p>
<p>Several extensions add more Segment Editor effects - see Segmentation category on the Extension Manager. The most important ones are SegmentEditorExtraEffects and SurfaceWrapSolidify extensions.</p>

---

## Post #3 by @Reham_Hassan (2020-08-19 15:09 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ea115313e24b45fd664614651f05b62cd1af6c4.jpeg" data-download-href="/uploads/short-url/fMFDGezvtyHpSLHRifN240nHWfy.jpeg?dl=1" title="Screen Shot 2020-08-19 at 5.01.02 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ea115313e24b45fd664614651f05b62cd1af6c4_2_690x431.jpeg" alt="Screen Shot 2020-08-19 at 5.01.02 PM" data-base62-sha1="fMFDGezvtyHpSLHRifN240nHWfy" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ea115313e24b45fd664614651f05b62cd1af6c4_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ea115313e24b45fd664614651f05b62cd1af6c4_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ea115313e24b45fd664614651f05b62cd1af6c4_2_1380x862.jpeg 2x" data-dominant-color="A8ACB1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-08-19 at 5.01.02 PM</span><span class="informations">2560×1600 784 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2da821068547c7677f3c669358fc61db74fc084b.jpeg" data-download-href="/uploads/short-url/6vTHsgYYQsX6YzdWu5f8fJrucpJ.jpeg?dl=1" title="Screen Shot 2020-08-19 at 5.04.51 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2da821068547c7677f3c669358fc61db74fc084b_2_690x431.jpeg" alt="Screen Shot 2020-08-19 at 5.04.51 PM" data-base62-sha1="6vTHsgYYQsX6YzdWu5f8fJrucpJ" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2da821068547c7677f3c669358fc61db74fc084b_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2da821068547c7677f3c669358fc61db74fc084b_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2da821068547c7677f3c669358fc61db74fc084b_2_1380x862.jpeg 2x" data-dominant-color="E5E7E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-08-19 at 5.04.51 PM</span><span class="informations">2560×1600 530 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>i tried uninstall and reinstall extensions, still don’t have the whole list of tools for the segmentation, im trying to practice how to segment teeth from one of your answers here <a href="https://discourse.slicer.org/t/teeth-segmentaion/9775/9" class="inline-onebox">Teeth Segmentation - #9 by lassoan</a><br>
in which a water shed effect is required which i don’t have</p>
<p>thank you for your reply</p>

---

## Post #4 by @lassoan (2020-08-19 22:18 UTC)

<p>What errors do you see in the Python console?</p>

---

## Post #5 by @Reham_Hassan (2020-08-20 12:22 UTC)

<p>Python 3.6.7 (default, Aug  9 2020, 23:06:58)<br>
[GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)] on darwin</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pandas/compat/<strong>init</strong>.py:120: UserWarning: Could not import the lzma module. Your installed Python is incomplete. Attempting to use lzma compression will result in a RuntimeError.<br>
warnings.warn(msg)</p>

---

## Post #6 by @lassoan (2020-08-20 13:18 UTC)

<p>This warning should not be an issue. Could you send the full application log (menu: Help/Report a bug)? If it is too long then you can upload it to somewhere and just post the link.</p>

---

## Post #7 by @Reham_Hassan (2020-08-20 13:34 UTC)

<p>[DEBUG][Qt] 20.08.2020 15:32:48 [] (unknown:0) - Session start time …: 2020-08-20 15:32:48</p>
<p>[DEBUG][Qt] 20.08.2020 15:32:48 [] (unknown:0) - Slicer version …: 4.11.0-2020-08-08 (revision 29260 / 47c2915) macosx-amd64 - installed release</p>
<p>[DEBUG][Qt] 20.08.2020 15:32:48 [] (unknown:0) - Operating system …: Mac OS X / 10.15.6 / 19G2021 - 64-bit</p>
<p>[DEBUG][Qt] 20.08.2020 15:32:48 [] (unknown:0) - Memory …: 8192 MB physical, 2048 MB virtual</p>
<p>[DEBUG][Qt] 20.08.2020 15:32:48 [] (unknown:0) - CPU …: GenuineIntel Intel® Core™ i5-4288U CPU @ 2.60GHz, 2 cores, 4 logical processors</p>
<p>[DEBUG][Qt] 20.08.2020 15:32:48 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading</p>
<p>[DEBUG][Qt] 20.08.2020 15:32:48 [] (unknown:0) - Qt configuration …: version 5.15.0, with SSL, requested OpenGL 3.2 (core profile)</p>
<p>[DEBUG][Qt] 20.08.2020 15:32:48 [] (unknown:0) - Developer mode enabled …: no</p>
<p>[DEBUG][Qt] 20.08.2020 15:32:48 [] (unknown:0) - Prefer executable CLI …: yes</p>
<p>[DEBUG][Qt] 20.08.2020 15:32:48 [] (unknown:0) - Application path …: /Applications/Slicer.app/Contents/MacOS</p>
<p>[DEBUG][Qt] 20.08.2020 15:32:48 [] (unknown:0) - Additional module paths …: /Applications/Slicer.app/Contents/Extensions-29260/Auto3dgm/lib/Slicer-4.11/cli-modules, /Applications/Slicer.app/Contents/Extensions-29260/Auto3dgm/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29260/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29260/SurfaceWrapSolidify/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29260/RawImageGuess/lib/Slicer-4.11/qt-scripted-modules</p>
<p>[DEBUG][Python] 20.08.2020 15:32:49 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pydicom/datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…</p>
<p>[WARNING][Qt] 20.08.2020 15:32:56 [] (unknown:0) - libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space</p>
<p>[CRITICAL][Stream] 20.08.2020 15:32:57 [] (unknown:0) - /Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pandas/compat/<strong>init</strong>.py:120: UserWarning: Could not import the lzma module. Your installed Python is incomplete. Attempting to use lzma compression will result in a RuntimeError.</p>
<p>[CRITICAL][Stream] 20.08.2020 15:32:57 [] (unknown:0) - warnings.warn(msg)</p>
<p>[WARNING][Qt] 20.08.2020 15:32:57 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile</p>
<p>[DEBUG][Python] 20.08.2020 15:32:58 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations</p>
<p>[DEBUG][Python] 20.08.2020 15:32:59 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor</p>
<p>[DEBUG][Python] 20.08.2020 15:32:59 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics</p>
<p>[DEBUG][Python] 20.08.2020 15:33:00 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: ExportAs</p>
<p>[DEBUG][Qt] 20.08.2020 15:32:59 [] (unknown:0) - Switch to module: “Welcome”</p>
<p>[DEBUG][Qt] 20.08.2020 15:33:10 [] (unknown:0) - Switch to module: “SegmentEditor”</p>

---

## Post #8 by @lassoan (2020-08-20 13:47 UTC)

<p>Thank you for the logs. It seems that SegmentEditorExtraEffects has not been installed. Path of SurfaceWrapSolidify extension shows up, but it does not appear in the Segment Editor. Please install yesterday’s Slicer Preview Release from <a href="https://download.slicer.org/?offset=-1">https://download.slicer.org/?offset=-1</a> and install SegmentEditorExtraEffects extension and let me know if the additional effects show up in Segment Editor.</p>

---

## Post #9 by @Reham_Hassan (2020-08-21 16:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="13086">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>SegmentEditorExtraEffects</p>
</blockquote>
</aside>
<p>Hi<br>
it worked, i can see the additional effects now, time to practice<br>
thank you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
