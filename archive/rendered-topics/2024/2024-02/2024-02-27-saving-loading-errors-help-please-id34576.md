---
topic_id: 34576
title: "Saving Loading Errors Help Please"
date: 2024-02-27
url: https://discourse.slicer.org/t/34576
---

# Saving/Loading errors - help please

**Topic ID**: 34576
**Date**: 2024-02-27
**URL**: https://discourse.slicer.org/t/saving-loading-errors-help-please/34576

---

## Post #1 by @willm1123 (2024-02-27 21:07 UTC)

<p>Hey y’all, I am an undergraduate student new to the Slicer program. I have been working on continuing a manual segmentation of some CT scan data that was started by another student last semester. After my first day of work, my professor and I attempted to save the scene but received error notifications that some files were unable to save properly. However, since the scene itself (the mrml file) and the segmentation data seemed to save fine, we did not think much of it. Unfortunately, when we tried to open the file again to continue work the next week, the scene failed to load properly. It loads the segmentations without the CT slides, and despite hours of trying different things I cannot get the CT slides to load in the scene with the segmentation (I can get them to load separately only). Any insight would be a huge help. As it stands, we are going to lose months of work and have to start all over again. This is the error message we are getting:</p>
<ul>
<li>Error: Loading /Volumes/Seagate/Protamandua scans/FMNH_P_13134_Protamandua_assorted modelling/2023-09-11-Scene.mrml - ERROR: In vtkMRMLStorableNode.cxx, line 326</li>
</ul>
<p>vtkMRMLLabelMapVolumeNode (0x7fbae0090330): vtkMRMLStorableNode::UpdateScene failed: Failed to read node ProtamSkull_8bit_0001 (vtkMRMLLabelMapVolumeNode1) using storage node vtkMRMLVolumeArchetypeStorageNode2.</p>
<ul>
<li>Error: Loading /Volumes/Seagate/Protamandua scans/FMNH_P_13134_Protamandua_assorted modelling/2023-09-11-Scene.mrml - ERROR: In vtkMRMLStorableNode.cxx, line 326</li>
</ul>
<p>vtkMRMLLabelMapVolumeNode (0x7fbae081ed30): vtkMRMLStorableNode::UpdateScene failed: Failed to read node Segmentation-label (vtkMRMLLabelMapVolumeNode2) using storage node vtkMRMLVolumeArchetypeStorageNode1.</p>

---

## Post #2 by @muratmaga (2024-02-27 22:34 UTC)

<p>Those warnings/messages are important.</p>
<p>The scene file is simply a set of pointers to the individual files (segmentation, markups, models, volumes) and saves their properties (colors, lookup tables etc). Without knowing what the error message said, I can only guess. Perhaps it probably wasn’t able to write the file (maybe you tried to save in a place where you don’t have write permission to, like someone else’s folder).</p>
<p>However, if you already have the segmentation, you should be able to import the CT scan from the scratch, and into that scene. You said it loads separately. I am not sure what that means. What happens when you load the scene with segmentations only, and then import that CT file?</p>

---

## Post #3 by @willm1123 (2024-02-29 22:10 UTC)

<p>Thank you for your response. When I try to load the CT data, the segmentation quite literally disappears and vice versa. Also, here is the error message we are getting:</p>
<ul>
<li>Error: Loading /Volumes/Seagate/Protamandua scans/FMNH_P_13134_Protamandua_assorted modelling/2023-09-11-Scene.mrml - ERROR: In vtkMRMLStorableNode.cxx, line 326</li>
</ul>
<p>vtkMRMLLabelMapVolumeNode (0x7fbae0090330): vtkMRMLStorableNode::UpdateScene failed: Failed to read node ProtamSkull_8bit_0001 (vtkMRMLLabelMapVolumeNode1) using storage node vtkMRMLVolumeArchetypeStorageNode2.</p>
<ul>
<li>Error: Loading /Volumes/Seagate/Protamandua scans/FMNH_P_13134_Protamandua_assorted modelling/2023-09-11-Scene.mrml - ERROR: In vtkMRMLStorableNode.cxx, line 326</li>
</ul>
<p>vtkMRMLLabelMapVolumeNode (0x7fbae081ed30): vtkMRMLStorableNode::UpdateScene failed: Failed to read node Segmentation-label (vtkMRMLLabelMapVolumeNode2) using storage node vtkMRMLVolumeArchetypeStorageNode1.</p>

---

## Post #4 by @muratmaga (2024-02-29 22:33 UTC)

<aside class="quote no-group" data-username="willm1123" data-post="3" data-topic="34576">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/51bf81/48.png" class="avatar"> willm1123:</div>
<blockquote>
<p>When I try to load the CT data, the segmentation quite literally disappears and vice versa.</p>
</blockquote>
</aside>
<p>That’s a sign off mismatch in the segmentaiton and original CT image spacing. It should be fixable. Can you share those two only somewhere on the cloud?</p>

---

## Post #5 by @willm1123 (2024-02-29 22:36 UTC)

<p>Depending on what you mean, I perhaps can, but I will not be able to access the files again until tomorrow.</p>

---
