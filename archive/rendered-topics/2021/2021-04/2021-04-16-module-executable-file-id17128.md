---
topic_id: 17128
title: "Module Executable File"
date: 2021-04-16
url: https://discourse.slicer.org/t/17128
---

# Module executable file

**Topic ID**: 17128
**Date**: 2021-04-16
**URL**: https://discourse.slicer.org/t/module-executable-file/17128

---

## Post #1 by @marianaslicer (2021-04-16 11:28 UTC)

<p>Hi everyone,</p>
<p>I developed a python scriped module using the Extension Wizard module in 3D Slicer (4.13.0) which takes as inputs the PatientID and a 3D volume. The module is running when the user clicks on the “Run” button.<br>
Is it possible to convert the module into an executable file to run the module on another PC without sharing the source code?</p>
<p>Thank you in advance.</p>

---

## Post #2 by @cpinter (2021-04-16 11:46 UTC)

<p>I believe for that you’d need to port your source code to C++, and if you want to move away from the open-source paradigm, then you won’t want the “download Slicer, install extension via extension manager” steps either, so maybe a Slicer custom app would be the best way to go.</p>

---

## Post #3 by @marianaslicer (2021-04-17 08:38 UTC)

<p>Hello,</p>
<p>Thank you very much for your suggestion, it’s what I am looking for!</p>
<p>I looked into this tutorial <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">SlicerCAT: Creating custom applications based on 3D Slicer - Kitware Blog</a> and followed the build instructions available in 3D Slicer documentation <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html" class="inline-onebox" rel="noopener nofollow ugc">Build Instructions — 3D Slicer documentation</a>.</p>
<p>I’m having the same problem as <a href="https://discourse.slicer.org/t/problem-in-building-slicercustomapptemplate/9783/5" class="inline-onebox">Problem in building SlicerCustomAppTemplate - #5 by Pooja_Virkar</a> : there is no file in the Slicer-build directory, so I couldn’t run /Slicer-build/Slicer.exe. I didn’t understand what was done to solve it, could you please explain it to me?</p>

---

## Post #4 by @marianaslicer (2021-04-19 22:16 UTC)

<p>I managed to get the executable file but the DICOM module was not loaded although it was enabled at the cmakefile.txt</p>
<h1><a name="p-58327-enable-slicer-built-in-modules-1" class="anchor" href="#p-58327-enable-slicer-built-in-modules-1" aria-label="Heading link"></a>Enable Slicer built-in modules</h1>
<p>set(Slicer_QTLOADABLEMODULES_ENABLED<br>
)<br>
set(Slicer_QTSCRIPTEDMODULES_ENABLED<br>
DICOM<br>
DICOMLib<br>
DICOMPatcher<br>
DICOMPlugins<br>
)</p>
<p>And I’m getting the following error loading the scripted module:</p>
<p>for patient in slicer.dicomDatabase.patients():</p>
<p>AttributeError: module ‘slicer’ has no attribute ‘dicomDatabase’</p>
<p>Am I doing something wrong? I would appreciate some help. Thanks.</p>

---

## Post #5 by @lassoan (2021-04-19 22:44 UTC)

<p>You need to go to the DICOM module at least once to ensure that a valid DICOM database is created.</p>

---

## Post #6 by @marianaslicer (2021-04-19 23:14 UTC)

<p>But I can’t go to the DICOM module</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8302d5634fd654b9ce9466a8447d31908fd76c2.png" data-download-href="/uploads/short-url/nZRqUfJkM3mFGmz2BVIg73eVLvc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8302d5634fd654b9ce9466a8447d31908fd76c2_2_690x193.png" alt="image" data-base62-sha1="nZRqUfJkM3mFGmz2BVIg73eVLvc" width="690" height="193" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8302d5634fd654b9ce9466a8447d31908fd76c2_2_690x193.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8302d5634fd654b9ce9466a8447d31908fd76c2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8302d5634fd654b9ce9466a8447d31908fd76c2.png 2x" data-dominant-color="DCE5E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">715×201 15.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Maybe there was any problem during the build? I didn’t get any error message…</p>

---

## Post #7 by @lassoan (2021-04-19 23:15 UTC)

<p>Have you had any build errors? If not then you may have disabled DICOM support in your CMake files (CMakeLists.txt an *.cmake files) in your custom application source code.</p>

---

## Post #8 by @marianaslicer (2021-04-21 07:54 UTC)

<p>Hi Andras, thank you for your response. Now I manage to get the DICOM module but I’m still getting the same error. I don’t understand why because from python interaction the application finds the DICOM database.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94629a3f4618f45db09cf279d70b630e8548ce39.png" data-download-href="/uploads/short-url/laFV4FdrZfjrGlcYisL8qJoaqA9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94629a3f4618f45db09cf279d70b630e8548ce39_2_690x366.png" alt="image" data-base62-sha1="laFV4FdrZfjrGlcYisL8qJoaqA9" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94629a3f4618f45db09cf279d70b630e8548ce39_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94629a3f4618f45db09cf279d70b630e8548ce39_2_1035x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94629a3f4618f45db09cf279d70b630e8548ce39.png 2x" data-dominant-color="DFE7ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×725 49 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @cpinter (2021-04-21 08:07 UTC)

<p>It is possible you are trying to access it too early. Maybe do some of the setup in the module widget’s <code>setup</code> function. Or connect a slot to the <code>startupCompleted</code> signal and do it there. To connect:</p>
<p><code>slicer.app.connect("startupCompleted()", self.onStartupCompleted)</code></p>

---

## Post #10 by @marianaslicer (2021-04-21 08:30 UTC)

<p>Thank you very much! It solved my problem!</p>

---

## Post #11 by @marianaslicer (2021-04-21 09:01 UTC)

<p>I have another question: I added to the ElastixParameterSetDatabase file a specific preset to be used in the registration. Should I re-build the project to compile the new preset?<br>
Thanks</p>

---

## Post #12 by @cpinter (2021-04-21 09:34 UTC)

<p>Can you please create a new topic for easier discoverability? If we discuss more, unrelated questions in the same thread people won’t have the chance to find it if they have the same issue…</p>

---
