---
topic_id: 26423
title: "Landmark Registration Crash"
date: 2022-11-24
url: https://discourse.slicer.org/t/26423
---

# Landmark Registration crash

**Topic ID**: 26423
**Date**: 2022-11-24
**URL**: https://discourse.slicer.org/t/landmark-registration-crash/26423

---

## Post #1 by @little-ear (2022-11-24 14:23 UTC)

<p>Dear 3D Slicer community,<br>
first, thank you for your work. Its a great help in my research - previously CT - now MRI.</p>
<p>Data: I have MR single slice T1 and T2 maps (so literally two single slice images)<br>
Task: I use the T1 map to draw segments, which I want to transfer/align with my T2 map. They have a quite small offset. However, my segments are also small - resulting in relevant data drifts.</p>
<p>Processing: I thought that Landmark Registrations would provide me the best results for single slice images. So I load the data, and place Landmarks.<br>
However, when I change the Registration Type more than once (i.e. to test the difference in the transformations), the 3D slicer crashes.</p>
<p>This is repeatable.</p>
<p>This is my first bug report. Please let me know if and how I should provide more data.</p>
<p>Thank you again for your time and efforts!</p>
<pre><code class="lang-auto">LOG: 
[DEBUG][Qt] 24.11.2022 13:50:53 [] (unknown:0) - Session start time .......: 2022-11-24 13:50:53
[DEBUG][Qt] 24.11.2022 13:50:53 [] (unknown:0) - Slicer version ...........: 5.0.3 (revision 30893 / 7ea0f43) linux-amd64 - installed release
[DEBUG][Qt] 24.11.2022 13:50:53 [] (unknown:0) - Operating system .........: Linux / 5.15.0-53-generic / #59-Ubuntu SMP Mon Oct 17 18:53:30 UTC 2022 / UTF-8 - 64-bit
[DEBUG][Qt] 24.11.2022 13:50:53 [] (unknown:0) - Memory ...................: 15414 MB physical, 16383 MB virtual
[DEBUG][Qt] 24.11.2022 13:50:53 [] (unknown:0) - CPU ......................: AuthenticAMD AMD Ryzen 7 4700U with Radeon Graphics, 8 cores, 8 logical processors
[DEBUG][Qt] 24.11.2022 13:50:53 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, Sequential threading
[DEBUG][Qt] 24.11.2022 13:50:53 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)
[DEBUG][Qt] 24.11.2022 13:50:53 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 24.11.2022 13:50:53 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 24.11.2022 13:50:53 [] (unknown:0) - Application path .........: /home/***/Desktop/Slicer-5.0.3-linux-amd64/bin
[DEBUG][Qt] 24.11.2022 13:50:53 [] (unknown:0) - Additional module paths ..: NA-MIC/Extensions-30893/SlicerDevelopmentToolbox/lib/Slicer-5.0/qt-scripted-modules, NA-MIC/Extensions-30893/DCMQI/lib/Slicer-5.0/cli-modules, NA-MIC/Extensions-30893/QuantitativeReporting/lib/Slicer-5.0/qt-scripted-modules, NA-MIC/Extensions-30893/PETDICOMExtension/lib/Slicer-5.0/cli-modules, NA-MIC/Extensions-30893/PETDICOMExtension/lib/Slicer-5.0/qt-scripted-modules, NA-MIC/Extensions-30893/DiffusionQC/lib/Slicer-5.0/cli-modules, NA-MIC/Extensions-30893/DiffusionQC/lib/Slicer-5.0/qt-scripted-modules, NA-MIC/Extensions-30893/UKFTractography/lib/Slicer-5.0/cli-modules, NA-MIC/Extensions-30893/UKFTractography/lib/Slicer-5.0/qt-loadable-modules, NA-MIC/Extensions-30893/UKFTractography/lib/Slicer-5.0/qt-scripted-modules, NA-MIC/Extensions-30893/SlicerDMRI/lib/Slicer-5.0/cli-modules, NA-MIC/Extensions-30893/SlicerDMRI/lib/Slicer-5.0/qt-loadable-modules, NA-MIC/Extensions-30893/SlicerDMRI/lib/Slicer-5.0/qt-scripted-modules, NA-MIC/Extensions-30893/T1Mapping/lib/Slicer-5.0/cli-modules, NA-MIC/Extensions-30893/SlicerProstate/lib/Slicer-5.0/cli-modules, NA-MIC/Extensions-30893/SlicerProstate/lib/Slicer-5.0/qt-scripted-modules, NA-MIC/Extensions-30893/SlicerRT/lib/Slicer-5.0/cli-modules, NA-MIC/Extensions-30893/SlicerRT/lib/Slicer-5.0/qt-loadable-modules, NA-MIC/Extensions-30893/SlicerRT/lib/Slicer-5.0/qt-scripted-modules, NA-MIC/Extensions-30893/SegmentRegistration/lib/Slicer-5.0/qt-scripted-modules, NA-MIC/Extensions-30893/SlicerANTs/lib/Slicer-5.0/cli-modules, NA-MIC/Extensions-30893/SlicerANTs/lib/Slicer-5.0/qt-scripted-modules, NA-MIC/Extensions-30893/SlicerElastix/lib/Slicer-5.0/qt-scripted-modules
[DEBUG][Python] 24.11.2022 13:50:59 [Python] (/home/***/Desktop/Slicer-5.0.3-linux-amd64/lib/Slicer-5.0/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 24.11.2022 13:51:00 [Python] (/home/***/Desktop/Slicer-5.0.3-linux-amd64/lib/Slicer-5.0/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 24.11.2022 13:51:00 [Python] (/home/***/Desktop/Slicer-5.0.3-linux-amd64/lib/Slicer-5.0/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics
[WARNING][VTK] 24.11.2022 13:51:01 [vtkMRMLThreeDViewDisplayableManagerFactory (0x2011f30)] (/work/Stable/Slicer-0/Libs/MRML/DisplayableManager/vtkMRMLDisplayableManagerFactory.cxx:137) - RegisterDisplayableManager - vtkMRMLTractographyDisplayDisplayableManager is not a displayable manager. Failed to register
[DEBUG][Qt] 24.11.2022 13:51:01 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 24.11.2022 13:51:24 [] (unknown:0) - Switch to module:  ""
</code></pre>

---

## Post #2 by @lassoan (2022-11-26 00:11 UTC)

<p>Thanks for reporting. Could you describe the exact steps that led to the crash?</p>

---

## Post #3 by @little-ear (2022-11-28 10:11 UTC)

<p>I loaded the data to a new scene (<a href="https://drive.google.com/file/d/1BoJIt0BGMirwTCXuf4GA46cp12jn2pHi/view?usp=share_link" rel="noopener nofollow ugc">LINK</a>, so that you can use the same data).<br>
You will find 2 kidney maps in para-sagital slices. They are almost perfectly aligned. However, in other cases I would need to move the segments like 1 or 2 px or rotate a few degrees.<br>
 → “Landmark Registration”.<br>
 → show only sagital slices (and rotate to volume plane)<br>
 → place landmarks on the T1 map and adjust on T2 map<br>
 →  Local BRAINSFit (Defaul)<br>
 → Registration Type<br>
 → Click on Affine Registration<br>
 → Click on Plastimatch<br>
 → Click on ThinPlate Registration → CRASH</p>
<p>Faster Workaround?<br>
Sadly, I found no option to move/rotate segments when they are “para-sagitally” oriented. Best would be to move/rotate them directly on the “rotated to volume view”. That would be the quickest and easiest fix. Maybe I missed a button on the manual transform module?</p>
<p>Thanks in advance</p>

---

## Post #4 by @little-ear (2022-12-06 09:17 UTC)

<p>Please excuse me, I want to give my issue another (final) round of attention.<br>
Esp. on the potential workaround. Any help is welcome.<br>
Thank you.</p>

---

## Post #5 by @pieper (2022-12-06 20:00 UTC)

<p>Hi - thanks for sharing the data and instructions.  I was able to load your data and see the results of your registration and they seem reasonable to me and I did not see a crash with Slicer 5.2.1 on mac.</p>
<p>In terms of the sequence you described, selecting “Local BRAINSFit” and “Plastimatch” shouldn’t matter unless you click the “Refine landmark L-x” button.  Did you actually click that button?</p>
<p>Loading your scene and entering Landmark Registration without the clicking the refinement-related buttons I get the state below, where the registration is looking good and I can edit the thin plate spline with the landmarks.  I was also able to edit the landmarks after aligning the views.</p>
<p>Perhaps the issue you are seeing relates to plastimatch and the SlicerRT extension? (I didn’t try installing that but it doesn’t seem you were using it.)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/241d8c372cf39ece6037ea5ebae8d0f0fd2093a0.jpeg" data-download-href="/uploads/short-url/59uuFlCVeymxtkVhwl5fa0vjEI0.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/241d8c372cf39ece6037ea5ebae8d0f0fd2093a0_2_690x457.jpeg" alt="image" data-base62-sha1="59uuFlCVeymxtkVhwl5fa0vjEI0" width="690" height="457" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/241d8c372cf39ece6037ea5ebae8d0f0fd2093a0_2_690x457.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/241d8c372cf39ece6037ea5ebae8d0f0fd2093a0_2_1035x685.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/241d8c372cf39ece6037ea5ebae8d0f0fd2093a0_2_1380x914.jpeg 2x" data-dominant-color="6F6F6F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1273 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @little-ear (2022-12-07 07:51 UTC)

<p>THANK YOU for having a look on my issue, which helped me to identify the reason for the crash.</p>
<p>I removed SlicerRT and now it works fine. ISSUE SOLVED. Shall I report this to the SlicerRT extension team?</p>
<p>Why did I use SlicerRT? I tried different transformations types. Haven’t found the best solution; perhaps there is non <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @pieper (2022-12-07 13:57 UTC)

<p>Great, I’m glad you are back on track <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>Yes, if the crash is repeatable it helps to report to the SlicerRT team to see if it can be fixed.</p>

---

## Post #8 by @gcsharp (2022-12-07 21:05 UTC)

<p>Duly noted.  I’ll take a look.</p>

---
