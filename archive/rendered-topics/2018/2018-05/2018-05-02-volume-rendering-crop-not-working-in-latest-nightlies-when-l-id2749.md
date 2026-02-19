---
topic_id: 2749
title: "Volume Rendering Crop Not Working In Latest Nightlies When L"
date: 2018-05-02
url: https://discourse.slicer.org/t/2749
---

# Volume rendering - crop not working in latest nightlies when loading older file

**Topic ID**: 2749
**Date**: 2018-05-02
**URL**: https://discourse.slicer.org/t/volume-rendering-crop-not-working-in-latest-nightlies-when-loading-older-file/2749

---

## Post #1 by @hherhold (2018-05-02 13:04 UTC)

<p>This is on MacOS 10.12.6, MacBook Pro 15 retina (mid 2015), Radeon R9 M370X graphics.</p>
<p>I have a project (MRML, NRRD, segmentation, etc) that I’ve been working with in the April 15 nightly build. I’ve set up volume rendering with cropping and an ROI in a particular spot. I can reload this into the April 15 nightly and everything works great. When I load the same setup into the 5-2 nightly, nothing shows up in the volume render window unless I turn off cropping.</p>
<p>If I make a new annotation ROI and delete the old one, cropping works fine. Any ideas on why it doesn’t like the original ROI?</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @cpinter (2018-05-02 14:22 UTC)

<p>Hi Hollister,<br>
Thanks for the report! Cropping works fine on Windows, so I’ll try to reproduce it on Mac. Today’s very busy for me, but I’ll try get back to you soon hopefully. In the meantime can you please give me step-by step instructions on how to reproduce it the simplest possible way? Thanks!</p>

---

## Post #3 by @cpinter (2018-05-02 14:27 UTC)

<p>I tried on MacOSX 10.13.3 with the latest nightly and cropping works fine without any tricks. Can other Mac users please try to reproduce Hollister’s issue? Thanks</p>

---

## Post #4 by @hherhold (2018-05-02 15:08 UTC)

<p>Hi Csaba,</p>
<p>No rush - I’ll get you a repro procedure soon.</p>
<p>Thanks!!</p>
<p>-Hollister</p>

---

## Post #5 by @pieper (2018-05-02 16:00 UTC)

<p>With today’s nightly on a mac pro with AMD FirePro D700 graphics volume rendering and cropping is working fine with me in both CPU and GPU modes.  (I download SampleData, enable volume rendering and cropping).</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a>, I’m thinking that <a class="mention" href="/u/hherhold">@hherhold</a> might be reloading a scene file and there’s an issue with the multiple volume update.</p>

---

## Post #6 by @hherhold (2018-05-02 16:59 UTC)

<p>Yeah, loading a file and volume rendering/cropping/everything in the same version works fine.</p>
<p>The issue is loading a file into a new version that was saved in an older version. New = 5-2 nightly, Old = 4-15 nightly.</p>
<p>If you have an old nightly (4-15) around, do this:</p>
<ol>
<li>Run old nightly<br>
2 Load CTACardio</li>
<li>Turn on volume rendering</li>
<li>Turn on cropping</li>
<li>Crop a little</li>
<li>Save</li>
<li>Run new nightly</li>
<li>Load file from old nightly</li>
<li>Observe - no volume rendered.</li>
</ol>
<p>If you turn off cropping, delete the annotation ROI and start over, it works fine. The issue is just loading old files with a new nightly.</p>
<p>Hope this makes sense!</p>
<p>-Hollister</p>

---

## Post #7 by @cpinter (2018-05-03 13:57 UTC)

<p>Yes, it makes complete sense, thanks! I’ll try to look into this soon. I’ll be away for two weeks starting Saturday, so if I can’t get to this tomorrow then it will have to wait a bit, or somebody else will need to try to fix it if it’s urgent.</p>

---

## Post #8 by @hherhold (2018-05-03 14:20 UTC)

<p>Not urgent at all.</p>
<p>The workaround is just to delete the old ROI and make a new one - you lose the position of the cropping ROI, but that’s not a big deal.</p>
<p>Thanks!!!</p>

---

## Post #9 by @cpinter (2018-05-03 14:29 UTC)

<p>I created a Mantis issue:<br>
<a href="https://issues.slicer.org/view.php?id=4547" class="onebox" target="_blank">https://issues.slicer.org/view.php?id=4547</a></p>

---

## Post #10 by @cpinter (2018-05-03 18:19 UTC)

<p>After some diagnosis:</p>
<ol>
<li>The error is reproducible as described</li>
<li>If after loading the scene, we load the ROI separately from the acsv file, and select it as ROI for the volume in the Volume rendering module’s input section, then it’s displayed properly</li>
<li>If we clone the node that we loaded with the scene using subject hierarchy’s clone action, and select it as ROI, then the rendering does not show up</li>
<li>The properties of the good and bad nodes are identical</li>
</ol>
<p>Quite strange. Need to do some debugging to figure this out.</p>

---

## Post #11 by @cpinter (2018-05-03 18:21 UTC)

<p>Not sure if it’s related to this: <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/VolumeRendering/MRMLDM/vtkMRMLVolumeRenderingDisplayableManager.cxx#L549-L556">https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/VolumeRendering/MRMLDM/vtkMRMLVolumeRenderingDisplayableManager.cxx#L549-L556</a></p>
<p>For some reason cropping did not work when I was working on the mult-volume rendering, and after days of debugging I found out that if I invert the normals of the ROI, then it works. It was very strange, as the code that creates the ROI and the normals remained the same. <a class="mention" href="/u/pieper">@pieper</a> maybe you have some insight…</p>

---

## Post #12 by @cpinter (2018-05-03 19:34 UTC)

<p>It was indeed related to the issue I referenced just above. I found the source of the problem which solved the bug Hollister reported, and removed the need for that workaround I referenced. So I can declare complete victory <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Fixed in <a href="https://github.com/Slicer/Slicer/commit/1443b336855a4885fc67e9e4497d3fea25e58e2e">https://github.com/Slicer/Slicer/commit/1443b336855a4885fc67e9e4497d3fea25e58e2e</a></p>
<p>I hope it will work for you too. Now off to vacation!</p>

---
