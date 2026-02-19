---
topic_id: 32304
title: "Aneurysm Removal And Reconstruct The Parent Vessel"
date: 2023-10-18
url: https://discourse.slicer.org/t/32304
---

# aneurysm removal and reconstruct the parent vessel

**Topic ID**: 32304
**Date**: 2023-10-18
**URL**: https://discourse.slicer.org/t/aneurysm-removal-and-reconstruct-the-parent-vessel/32304

---

## Post #1 by @Tingchenccmu (2023-10-18 15:48 UTC)

<p>I want to perform digital aneurysm removal and reconstruct the parent vessel according to the tutorials. But I can’t find the three Python scripts because I find there is no path of vmtk/vmtkApps/CerebralAneurysms/ParentVesselReconstructions. Do you know why?</p>

---

## Post #2 by @mau_igna_06 (2023-10-19 01:17 UTC)

<aside class="quote no-group" data-username="Tingchenccmu" data-post="1" data-topic="32304">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tingchenccmu/48/67994_2.png" class="avatar"> Tingchenccmu:</div>
<blockquote>
<p>vmtk/vmtkApps/CerebralAneurysms</p>
</blockquote>
</aside>
<p>Does this help?</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/vmtk/vmtk/tree/master/vmtkApps/CerebralAneurysms/ParentVesselReconstruction">
  <header class="source">

      <a href="https://github.com/vmtk/vmtk/tree/master/vmtkApps/CerebralAneurysms/ParentVesselReconstruction" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/vmtk/vmtk/tree/master/vmtkApps/CerebralAneurysms/ParentVesselReconstruction" target="_blank" rel="noopener nofollow ugc"></a></h3>

  <p><a href="https://github.com/vmtk/vmtk/tree/master/vmtkApps/CerebralAneurysms/ParentVesselReconstruction" target="_blank" rel="noopener nofollow ugc">//github.com/vmtk/vmtk/tree/master/vmtkApps/CerebralAneurysms/ParentVesselReconstruction</a></p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Tingchenccmu (2023-10-24 05:32 UTC)

<p>Thanks so much! It does work. <img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=12" title=":grin:" class="emoji" alt=":grin:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @hamedtopic (2023-10-25 21:45 UTC)

<p>Are you working on brain aneurysms?</p>

---

## Post #5 by @hamedtopic (2023-10-25 21:46 UTC)

<p>is it available for us to remove the aneurysm right from the extension in Slicer?</p>

---

## Post #6 by @hamedtopic (2023-10-25 21:58 UTC)

<p>how about aneurysm removal?</p>

---

## Post #7 by @lassoan (2023-10-25 23:48 UTC)

<p>What do you mean by “aneurysm removal”? Removing of aneurysms from the segmentation? You can do that using the Segment Editor module’s Scissors tool.</p>

---

## Post #8 by @hamedtopic (2023-10-26 02:42 UTC)

<p>I mean this: <a href="http://www.vmtk.org/tutorials/ParentVesselReconstruction.html" rel="noopener nofollow ugc">Parent vessel reconstruction | vmtk - the Vascular Modelling Toolkit</a><br>
though it is just for saccular aneurysm.</p>

---

## Post #9 by @lassoan (2023-10-26 03:16 UTC)

<p>The simplest is to cut off the aneurysm sack using Scissors effect and then use Smoothing effect’s brush mode to touch up. This should be quite quick and easy.</p>
<p>If you want to automate it (which may pay off if you need to process hundreds of images and the script works flawlessly) then I would recommend to run the referenced Pypes scripts by copying the contents into Slicer’s Python interpreter (or maybe put it into a Slicer module for your convenience).</p>
<p>Making the Pypes scripts work as they are may be an option, too. I always just use those scripts as examples, so I don’t know if you can still run the via the command line.</p>

---

## Post #10 by @Tingchenccmu (2023-10-27 12:09 UTC)

<p>Hello! I think we have met the same problem. I also want to perform digital aneurysm removal and reconstruct the parent vessel according to the tutorials. But there is something wrong when I run this code “python patchandinterpolatecenterlines.py directoryPath id1 lateral” in PypePad during the Centerlines interpolation step. It shows that no module named ‘vmtk.python’. You know it is so confusing when errors happen according to the tutorials. If you have the answer, please let me know and thanks a lot.</p>

---

## Post #11 by @hamedtopic (2023-10-27 18:04 UTC)

<p>Thanks, Andras, the question is that how accurate the centerline will be by manually removing the aneurysm. But since the code is just for the saccular aneurysms, it may make sense that one does it manually.</p>

---
