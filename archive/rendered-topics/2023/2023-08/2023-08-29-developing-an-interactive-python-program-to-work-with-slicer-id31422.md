---
topic_id: 31422
title: "Developing An Interactive Python Program To Work With Slicer"
date: 2023-08-29
url: https://discourse.slicer.org/t/31422
---

# Developing an interactive python program to work with Slicer GUI

**Topic ID**: 31422
**Date**: 2023-08-29
**URL**: https://discourse.slicer.org/t/developing-an-interactive-python-program-to-work-with-slicer-gui/31422

---

## Post #1 by @ruili (2023-08-29 12:05 UTC)

<p>Hi all,</p>
<p>I am hoping to write some python script that can work with the slicer software interactively to semi-automate the process of vessel segmentation and centerline extraction. Specifically, after loading a volume file into slicer, I want to prompt the user to drag the ROI box (in volume rendering module) around to define an ROI that contains the vessels of interest. Then I want to execute some script to automatically read the location of the ROI box, run my customised segmentation pipeline, and display the segmentation result on the running slicer window. Next, I will need the user to correct parts of the segmentation using eraser, paint, etc. Once this is done, the user may click some button to start the process of extracting the centerlines using the vmtk module in slicer automatically.</p>
<p>I understand that you can copy and paste your python script into the python console of a running slicer to automatically execute some tasks. However, this can be quite tedious when processing a lot of data or if the script is very long. Thus, I was wondering if I can just run a python script locally, which can interact with slicer by having the user clicking some buttons, and achieve the pipeline described above.</p>
<p>I am quite new to the python API of slicer and interactive programming in general. Thus, your suggestions will be highly appreciated!</p>
<p>Sincerely</p>

---

## Post #2 by @yulaomao (2023-08-29 13:16 UTC)

<p>You can achieve the functionality you mentioned by writing a script module. Write down your workflow in a UI-based manner, where you can complete your tasks by clicking pre-designed buttons in a specific order. You can learn how to write a script module to accomplish this.</p>

---

## Post #3 by @ebrahim (2023-08-29 13:20 UTC)

<p>On scripted modules: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#extensions" class="inline-onebox" rel="noopener nofollow ugc">Extensions — 3D Slicer documentation</a></p>
<p>You can get started using the extension wizard</p>
<p>It can be helpful to look at examples that are in slicer: <a href="https://github.com/Slicer/Slicer/tree/main/Modules/Scripted" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/tree/main/Modules/Scripted</a></p>

---

## Post #4 by @chir.set (2023-08-29 13:24 UTC)

<aside class="quote no-group" data-username="ruili" data-post="1" data-topic="31422">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/dec6dc/48.png" class="avatar"> ruili:</div>
<blockquote>
<p>define an ROI that contains the vessels of interest</p>
</blockquote>
</aside>
<p>Since your workflow is interactive, you may consider ‘<a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/QuickArterySegmentation.md" rel="noopener nofollow ugc">Quick artery segmentation</a>’ module in SlicerVMTK extension, available via the extensions manager. It works with an ROI and can extract centerlines by remote controlling the ‘Extract centerline’ module.</p>

---

## Post #5 by @ruili (2023-08-29 15:05 UTC)

<p>Thank you for your suggestion. I tried searching for this module in the Extensions Manager but with no success. There does not seem to be any extension with ‘quick’ in its name at all. Do you know if the full name of the extension is just “Quick Artery Segmentation” or anything else?</p>

---

## Post #6 by @chir.set (2023-08-29 15:22 UTC)

<p>You are mixing up ‘Extensions’ and ‘Modules’.</p>
<p>An extension is a collection of modules.</p>
<p>The extension name here is SlicerVMTK, which you will find in the ‘Extensions manager’. The latter does not  search for modules in extensions, but for the extensions themselves.</p>

---

## Post #7 by @ruili (2023-08-29 19:53 UTC)

<p>Thank you very much for the clarification. I have installed the SlicerVMTK extension. However, when I looked for the quick artery segmentation module, it does not seem to be available. My Slicer version is 5.2.2 on MacOS. Do you know whether this is a compatibility problem or anything else?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e4cb99457587b88aeecfdf924132f37ee58b95f.png" alt="Screenshot 2023-08-29 at 20.44.00" data-base62-sha1="dsdgp8HsQBZGhKIeWl7bbMIVXKn" width="674" height="443"></p>

---

## Post #8 by @chir.set (2023-08-29 20:05 UTC)

<p>It’s probably not finding the ‘FloodFilling’ effect of the ‘Segment editor’, it’s not a native effect that it requires. You should install the ‘SegmentEditorExtraEffects’ extension too.</p>
<p>It’s always a good idea to go through the application log (View/Error log) to have more information to resolve some runtime problems yourself, or to post here.</p>

---

## Post #9 by @ruili (2023-08-30 10:52 UTC)

<p>That worked. Thank you so much!</p>

---
