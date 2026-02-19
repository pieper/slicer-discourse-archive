---
topic_id: 17617
title: "Volumes Module Getactivevolumenode Always Returns The First"
date: 2021-05-14
url: https://discourse.slicer.org/t/17617
---

# Volumes module : GetActiveVolumeNode always returns the first node

**Topic ID**: 17617
**Date**: 2021-05-14
**URL**: https://discourse.slicer.org/t/volumes-module-getactivevolumenode-always-returns-the-first-node/17617

---

## Post #1 by @chir.set (2021-05-14 09:48 UTC)

<p>While trying to get the selected node in the Volumes module,</p>
<p>slicer.modules.volumes.logic().GetActiveVolumeNode()</p>
<p>does not seem to behave as expected.</p>
<p>If we load 2 scalar volumes, GetActiveVolumeNode().GetID() always returns ‘vtkMRMLScalarVolumeNode1’, even if the second loaded volume is selected (expecting then vtkMRMLScalarVolumeNode2).</p>
<p>I suppose it’s a bug that needs a fix, or I have a wrong understanding of the function.</p>
<p>Using 4.13.0-2021-05-09 r29893 / 824c6d8 home built on Arch Linux .</p>
<p>Regards.</p>

---

## Post #2 by @lassoan (2021-05-14 21:03 UTC)

<p>Good catch. We’ll remove this method, this is just a remnant of decade-old infrastructure that has been long removed, but apparently not completely.</p>
<p>Although there is an “active volume” stored in the selection node (<code>slicer.app.applicationLogic().GetSelectionNode().GetActiveVolumeID()</code>, which is set whenever a volume is loaded and propagated to be displayed in the viewers) it is not used for anything else (and therefore may be removed in the future), probably because it would be way too limiting to have only a single “active” volume in the scene.</p>
<p>What would you like to use an “active volume” for? What is your end goal?</p>

---

## Post #3 by @chir.set (2021-05-15 07:48 UTC)

<p>The fundamental problem to overcome :<br>
I need to load 512x512x2100+ DICOM volumes and view it with Volume Rendering. Zooming in <em>some</em> volumes reaches a too near limit. If the volume is centred, this limit is much farther. Unfortunately, I don’t have such a volume at hand to post as a sample. And even so, an anonymized DICOM volume is centred by default. So it’s not possible to demonstrate here.<br>
N.B. I am using a recent and quite performing graphics adaptor (Radeon RX 6700 XT), so that’s not the bottleneck leading to the zooming limit.</p>
<p>The single step where I need a UI :<br>
Get hold of a selected volume node in a module; it can be any module. I may also write a custom module with just a node selector and a button; it would be an overkill in my view.</p>
<p>So I thought of getting the active node in the Volumes module, and pass it to functions in slierrc.py via a keyboard shortcut. It would :</p>
<ul>
<li>centre the volume</li>
<li>apply preferred window/level values</li>
<li>show the volume as background in slice views</li>
<li>fit the volume in the slice views</li>
<li>go to the Volume Rendering module</li>
<li>set the MRML volume node</li>
<li>show the node in the 3D view</li>
<li>apply a preferred preset</li>
</ul>
<p>All these occur straightaway with a shortcut. I just saw that even if no volume node is active in the Volumes Module, GetActiveVolumeNode() returns the last loaded volume via ‘Add data’, and not volumes loaded via the DICOM module.</p>
<p>If there is no way of getting the active node in the Volumes module, I’ll end up writing an intermediate module and access it quickly via the toolbar.</p>
<p>Thanks for considering.</p>

---

## Post #4 by @pieper (2021-05-15 14:14 UTC)

<p>Another option could be a subject hierarchy plugin (such as <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/ExportAs/ExportAs.py#L30">this example</a>).  The user would right-click on the volume of interest in the Data module and select your custom action.</p>

---

## Post #5 by @lassoan (2021-05-15 14:20 UTC)

<p>These actions are performed in recent Slicer Preview Releases when you <em>drag-and-drop</em> a volume from the Data module into a view (except setting window/level values, which are set when you load the volume). What is missing/inconsistent is that the volume is not centered in 3D view when you click the eye icon (it is centered in slice views but not in 3D) - I’ll fix this.</p>
<p>If you want to apply a custom operation to all volumes that you load then you can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-automatically-when-a-volume-is-loaded">do this automatically whenever a volume is loaded</a>.</p>
<p>If you want to do it for only certain volumes and there is no other input than the selected volume then you can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#subject-hierarchy-plugin-offering-view-context-menu-action">register a right-click menu action in the subject hierarchy</a>. You can also add a subject hierarchy plugin that takes ownership of all volumes (by returning high confidence value in <code>canOwnSubjectHierarchyItem</code> method) and implements a custom behavior for clicking the eye icon (by overriding <code>setDisplayVisibility</code> method). You can search in the Slicer’s source code for <code>*SubjectHierarchyPlugin.py</code> for examples.</p>
<p>You don’t need a module for either of these, you can just add them to the startup script.</p>
<p>If you need some additional input parameters then it is worth adding new scripted module with a simple GUI.</p>

---

## Post #6 by @chir.set (2021-05-15 17:21 UTC)

<p>The right click menu in the Subject Hierarchy plugin would be most appropriate. I’ll dig through this ASAP.</p>
<p>Thanks for your input.</p>

---
