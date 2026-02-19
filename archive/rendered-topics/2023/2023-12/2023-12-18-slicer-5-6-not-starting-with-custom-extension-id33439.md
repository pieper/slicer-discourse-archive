---
topic_id: 33439
title: "Slicer 5 6 Not Starting With Custom Extension"
date: 2023-12-18
url: https://discourse.slicer.org/t/33439
---

# Slicer 5.6 not starting with custom extension

**Topic ID**: 33439
**Date**: 2023-12-18
**URL**: https://discourse.slicer.org/t/slicer-5-6-not-starting-with-custom-extension/33439

---

## Post #1 by @Vincebisca (2023-12-18 09:55 UTC)

<p>Hello,</p>
<p>A year ago I developped a custom extension as part of an internal project on 3D Slicer 4.11.<br>
At the time, I managed to transfer to Slicer 5.0 without issues and use the extension on this version too. The project finished and I haven’t updated the extension since then. However, I had to re-install it recently and I tried to do so on Slicer 5.6. When I try to start it with the extension installed, the software seem to fall in an infinite starting loop, telling me that the computer lacks the graphic capabilities to start it. And I can’t close it with the task manager either, it just reboots everytime I close it.</p>
<p>I am not a programmer and the extension is not very well made, but I wanted to know if you have any idea on what might cause this problem, and what I can do to solve it.<br>
Or if it’s not feasible, how I could download Slicer 5.0 to use it on this version of the software.</p>
<p>Thank you in advance !</p>

---

## Post #2 by @RafaelPalomar (2023-12-18 12:52 UTC)

<p><a class="mention" href="/u/vincebisca">@Vincebisca</a>, what type of modules were included in the extension (C++ loadable, Python, CLI)?</p>
<p>When you say “transfer” do you mean manually copying the module files from one Slicer installation to another? Have you tried to <strong>build</strong> your extension against Slicer 5.6? Moving binary files generated using Slicer 4.11 to a 5.6 installation (or for that matter, pointing Slicer’s 5.6 paths to modules generated with 4.11) is something I would expect producing the errors you describe.</p>
<p>Generally speaking, moving Slicer backwards to fit one specific extension is not a good idea as you will miss on bug fixes, new features, etc. On the long term it does not even look very sustainable as Slicer is very dynamic and changes rapidly. A much better approach would be to build your extension against a new Slicer and update the extension.</p>
<p>I hope this helps.</p>

---

## Post #3 by @Vincebisca (2023-12-18 13:04 UTC)

<p>Hello <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> , thank you for your reply !</p>
<p>Maybe extension is not the right term, “module” might be better suited. Actually I built it on the Slicelet code template. It is written in Python but uses function from other modules such as SegmentEditorExtraEffects or Elastix.</p>
<p>The module is juste a folder that I copy in the extension folder of Slicer and then add to the software by adding the module’s path in the application settings &gt; module.</p>
<p>I don’t really know what you mean by “build the extension against Slicer 5.6”…</p>
<p>Actually an hour ago I managed to start 5.6, and the module seemed to work, but when I tried to close it the software fell in the starting loop once again…</p>
<p>I hope this made the situation a bit clearer, thanks for your help !</p>

---

## Post #4 by @Vincebisca (2023-12-18 13:07 UTC)

<p>As an additionnal information, when starting, the loading window gets stuck on “registering modules &gt; instanciating modules” back and fort. And I get the following error pop-up :</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75038146157ea37aac46d1d172a101d63baf0b09.png" alt="Errore message 2023_12_18" data-base62-sha1="gH9n9q1drbJt3uoZ12AQ3h7zDPr" width="498" height="115"></p>

---

## Post #5 by @RafaelPalomar (2023-12-18 13:16 UTC)

<p>How do you do it with <code>SegmentEditorExtraEffects</code> and <code>Elastix</code>? Do you install them using the Extension Manager before using your extension?</p>
<p>Do the <code>Show Details...</code> give any relevant information?</p>
<aside class="quote no-group" data-username="Vincebisca" data-post="3" data-topic="33439">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincebisca/48/10722_2.png" class="avatar"> Vincebisca:</div>
<blockquote>
<p>I don’t really know what you mean by “build the extension against Slicer 5.6”…</p>
</blockquote>
</aside>
<p>Never mind. This is not relevant for python modules as they don’t need to be compiled.</p>
<p>I’m not familiar with slicelets, but if you were given a template from Slicer 4.11 you could try to get a new template from Slicer 5.6 and populate it with your code accordingly. I wouldn’t be surprised if some python templates are different today.</p>

---

## Post #6 by @Vincebisca (2023-12-19 08:33 UTC)

<p>I install them with the Extension Manager yes, and they are imported in the code of the module as well.</p>
<p>The “show details” indicates to search for information on the Get Help - Application does not start section of 3D Slicer’s help. I will search there also, but the point is that the application does start, it just starts in a loop infinitely …</p>
<p>yes, finding the up to date template and populate it with the code is a good idea, I searched for the template but didn’t find it yet, I will continue to search.</p>
<p>As a new piece of information : the module actually only works on my computer with Slicer 5.0.3, I tried adding it back to 4.11 and it didn’t work, same with 4.11, 5.0.3 and 5.6.1 on another computer… I don’t know how it can work only on my version of Slicer 5.0.3, maybe that’s a clue to what the problem is?</p>
<p>Thanks again</p>

---

## Post #7 by @RafaelPalomar (2023-12-19 08:45 UTC)

<aside class="quote no-group" data-username="Vincebisca" data-post="6" data-topic="33439">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincebisca/48/10722_2.png" class="avatar"> Vincebisca:</div>
<blockquote>
<p>yes, finding the up to date template and populate it with the code is a good idea, I searched for the template but didn’t find it yet, I will continue to search.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/vincebisca">@Vincebisca</a>, maybe the slicelets infrastructure is no longer available in modern Slicer. I can’t find any references in the documentation. <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> did slicelets get replaced by SlicerCAT?</p>

---

## Post #8 by @Vincebisca (2023-12-19 10:00 UTC)

<p>I am currently trying through the Extension Wizard → Create Extension → Add module to extension.</p>
<p>It generates a similar template to what I had, however, after I populate it with my old code it fails to instantiate the module.</p>

---

## Post #9 by @RafaelPalomar (2023-12-19 11:47 UTC)

<p><a class="mention" href="/u/vincebisca">@Vincebisca</a>, that should be a good way to go. If your module is public I could have a look and see if I can reproduce the problem. There may be some specifics in your module that makes it fail.</p>

---

## Post #10 by @Vincebisca (2023-12-19 15:42 UTC)

<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> , unfortunately I don’t think I can share the module since it’s an internal tool…</p>
<p>I tried to rebuild the module bit by bit while trying when it failed. I used the template created with the Extension Wizard and progressively copy-pasted the functionnal content of the module’s code. For the GUI, I just copy-pasted de .ui file I had for the original module.</p>
<p>So far, it seems to work better, however, when I start it there are a few errors in the Python Log :</p>
<pre><code class="lang-auto">[Qt] QLayout::addChildLayout: layout "" already has a parent
[Qt] qMRMLSegmentEditorWidget::setMasterVolumeNodeSelectorVisible is deprecated, use setSourceVolumeNodeSelectorVisible method instead.
[Qt] qMRMLSegmentEditorWidget::setMasterVolumeNode is deprecated, use setSourceVolumeNode method instead.
</code></pre>
<p>I tried to find the deprecated functions in my code but it seems they are not from my code…<br>
Additionnaly, when I try to run a resampling function from cropVolumeLogic, I get this kind or error :</p>
<pre><code class="lang-auto">[VTK] Generic Warning: In vtkSlicerCropVolumeLogic.cxx, line 91
[VTK] vtkSlicerCropVolumeLogic::vtkInternal::SetXYZ failed: invalid ROI
[VTK] Generic Warning: In vtkSlicerCropVolumeLogic.cxx, line 117
[VTK] vtkSlicerCropVolumeLogic::vtkInternal::SetROIRadius failed: invalid ROI
[VTK] Generic Warning: In vtkSlicerCropVolumeLogic.cxx, line 104
[VTK] vtkSlicerCropVolumeLogic::vtkInternal::GetROIRadius failed: invalid ROI
[VTK] Generic Warning: In vtkSlicerCropVolumeLogic.cxx, line 78
[VTK] vtkSlicerCropVolumeLogic::vtkInternal::GetROIXYZ failed: invalid ROI
[VTK] Generic Warning: In vtkSlicerCropVolumeLogic.cxx, line 104
[VTK] vtkSlicerCropVolumeLogic::vtkInternal::GetROIRadius failed: invalid ROI
[VTK] Input port 0 of algorithm vtkImageMapToWindowLevelColors (000001D4A44D6D80) has 0 connections but is not optional.
[VTK] Input port 0 of algorithm vtkImageThreshold (000001D4F9D01CF0) has 0 connections but is not optional.
[VTK] Input port 0 of algorithm vtkImageMapToWindowLevelColors (000001D4A44D6D80) has 0 connections but is not optional.
[VTK] Input port 0 of algorithm vtkImageReslice (000001D4F7854220) has 0 connections but is not optional.
</code></pre>
<p>I have no idea how to fix this. Is it possible that the Qt and VTK functions I used are not supported anymore?</p>

---

## Post #11 by @RafaelPalomar (2023-12-22 06:39 UTC)

<p><a class="mention" href="/u/vincebisca">@Vincebisca</a>, it is  difficult to debug the error without knowing the code behind it.</p>
<p>Make sure when debugging, that this happens in a clean Slicer environment (make sure you use a recent version of Slicer  and that there are not old versions of your module set in the module path). Try to identify the lines that produce the errors and see if the functions are still available and in the same form (number of parameters and order of them).</p>

---

## Post #12 by @Vincebisca (2023-12-22 09:19 UTC)

<p>Hi <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> , yes I understand.</p>
<p>For now I have adressed the main problem of the resampling function by replacing the ROI type from vtkMRMLAnnotationROINode to vtkMRMLMarkupsROINode.</p>
<p>The code still gives warnings about Qt elements being deprecated and the “Input port 0 …” lines but it still runs so that’s a start…</p>
<p>I will dig deeper in the code to see if I can identify and replace deprecated elements.</p>
<p>Thanks a lot for your time and help !</p>

---

## Post #13 by @Vincebisca (2024-01-31 09:37 UTC)

<p>Hello again everyone,</p>
<p>I am adding to this topic because there has been new informations. I thought to have solved my initial issue when trying to drag and drop the folder of the extension directly into 3D Slicer’s home page. While that works on PC, it seems that it doesn’t on Mac : the option “Add python scrypted modules to the application” doesn’t appear.</p>
<p>Also, I noticed that when trying the other method, via Edit &gt; Application Settings &gt; Modules, on a fresh version of 3D Slicer, it crashes also wether I use “add” or drag and drop the folder in the module paths window.</p>
<p>The crash doesn’t happen if I already installed the extension once via Drag&amp;Drop and then removed it or re-installed 3D Slicer without wiping the whole “<a href="http://slicer.org" rel="noopener nofollow ugc">slicer.org</a>” folder.</p>
<p>I am wondering what could cause this difference in behavior between import methods. The extension doesn’t seem completely broken since it works when using the Drag&amp;Drop method…</p>
<p>If anyone has a clue on what is happening it would be great !</p>
<p>Thanks,</p>
<p>Vincent</p>

---
