---
topic_id: 32674
title: "Error Loading Freesurfer Segmentation"
date: 2023-11-08
url: https://discourse.slicer.org/t/32674
---

# Error loading freesurfer segmentation

**Topic ID**: 32674
**Date**: 2023-11-08
**URL**: https://discourse.slicer.org/t/error-loading-freesurfer-segmentation/32674

---

## Post #1 by @Maurilio_Genovese (2023-11-08 08:52 UTC)

<p>Hi, I am facing the same problem. When I try to load a freesurfer segmentation (a standard aparc+aseg.mgz) on Ubuntu (either using the importer interface, the load volume interface or a slicerpython command) I will get this error:</p>
<p>ReferenceImageExtentOffset attribute was not found in NRRD segmentation file. Assume no offset.</p>
<p>“Slicer has caught an application error, please save your work and restart.\n\nThe application has run out of memory. Increasing swap size in system settings or adding more RAM may fix this issue.\n\nIf you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="https://slicer.org" rel="noopener nofollow ugc">https://slicer.org</a>\n\n\nThe message detail is:\n\nException thrown in event: std::bad_alloc”</p>
<p>I’m using last version of Slicer and FreeSurferImporter on Ubuntu 23.04</p>

---

## Post #2 by @RafaelPalomar (2023-11-08 13:46 UTC)

<p><a class="mention" href="/u/maurilio_genovese">@Maurilio_Genovese</a>, the error message you get suggests that the image you try to load is too big for the RAM memory you have. Could you provide a pointer to the concrete dataset you try to load and the specifications of your computer? I’m not a user of FreeSurferImporter but I could try to install it and give it a try in my Linux machine.</p>

---

## Post #3 by @Maurilio_Genovese (2023-11-08 17:50 UTC)

<p>I have 8gb RAM memory and I can load without error this segmentation in the same machine windows partition. Moreover a collegue had the same error on a linux high performance machine.<br>
I also tried with standard freesurfer course data (<a>ftp://surfer.nmr.mgh.harvard.edu/pub/data/tutorial_data/buckner_data/tutorial_subjs/good_output/mri/brain.mgz</a> and <a>ftp://surfer.nmr.mgh.harvard.edu/pub/data/tutorial_data/buckner_data/tutorial_subjs/good_output/mri/aparc+aseg.mgz</a>), and I’m still getting the same error on linux.<br>
I think this is a bug and not a problem of my computer setting.<br>
Should I report at SlicerFreeSurfer or is this the right place?<br>
Thanks!</p>

---

## Post #4 by @RafaelPalomar (2023-11-10 10:39 UTC)

<p><a class="mention" href="/u/maurilio_genovese">@Maurilio_Genovese</a> I can reproduce the same issue on my Linux machine (32 GB). To me it looks that is not a memory issue but a bug as you pointed out. The error seems to be triggerd by the <code>QTGUI</code> component: <a href="https://github.com/Slicer/Slicer/blob/ba80bddd4a6cba9cfb82a527309cda30ada2ba6a/Base/QTGUI/qSlicerApplication.cxx#L522-L525" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/ba80bddd4a6cba9cfb82a527309cda30ada2ba6a/Base/QTGUI/qSlicerApplication.cxx#L522-L525</a> in Slicer. I’m currently building a debug version of Slicer to inspect more on this. I’ll come back with more info</p>

---

## Post #5 by @Maurilio_Genovese (2023-11-10 12:13 UTC)

<p>Great! Thank you for your help</p>

---

## Post #6 by @RafaelPalomar (2023-11-11 12:12 UTC)

<p><a class="mention" href="/u/maurilio_genovese">@Maurilio_Genovese</a>, I’ve built Slicer on my machine in both <code>master</code> and <code>v5.4.0</code> with <code>Debug</code> configuration, as well as the SlicerFreeSurfer extension  <code>master</code> with  <code>Debug</code> configuration. On these builds, I cannot reproduce the error and the <code>aparc+aseg.mgz</code> dataset imports successfully.</p>
<p>As a workaround,  you could try to build Slicer and SlicerFreeSurfer yourself (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html</a>)</p>
<p>I’m tagging here some of the developers of 3D Slicer and SlicerFreeSurfer, maybe there is something else we can try to get to the bottom of the problem: <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #7 by @pieper (2023-11-11 14:53 UTC)

<p>Hmm, that’s very strange that the factory build would be throwing an exception but a local build would not.  It might have to do with the system library versions or perhaps an compiler or optimization issues.  You could look at any memory allocation code in the FreeSurfer extension to see if there is any faulty logic, perhaps to do with byte swapping or something that could lead to a crash.  Since you have a debug build you could step through the loading process and see what each allocation is doing and see if any of the logic looks questionable.</p>

---
