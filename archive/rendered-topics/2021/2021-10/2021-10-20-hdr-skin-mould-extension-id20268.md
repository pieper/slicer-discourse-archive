---
topic_id: 20268
title: "Hdr Skin Mould Extension"
date: 2021-10-20
url: https://discourse.slicer.org/t/20268
---

# HDR Skin Mould Extension

**Topic ID**: 20268
**Date**: 2021-10-20
**URL**: https://discourse.slicer.org/t/hdr-skin-mould-extension/20268

---

## Post #1 by @kmalexander (2021-10-20 16:46 UTC)

<p>Seems like a release for PerkLab’s SlicerSkinMouldGenerator was never created.  Any chance of getting this extension somehow?  <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a></p>

---

## Post #2 by @preich01 (2021-12-06 05:19 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a> Can you provide instructions on how to implement the SlicerSkinMouldGenerator  extension in Slicer or can it be executed as a python program ?</p>

---

## Post #3 by @cpinter (2021-12-07 09:44 UTC)

<p>Here’s how you could add it as an extension:<br>
Use the Extension Wizard module in Slicer to create an empty extension with the desired metadata. Checkout the <a href="https://github.com/PerkLab/SlicerSkinMouldGenerator">module repo</a>, copy the module code and documentation to the extension directory, add the module folder to the main CMakeLists.txt, commit the whole thing to a GitHub repository, edit the s4ext file, and contribute it to the <a href="https://github.com/Slicer/ExtensionsIndex">ExtensionIndex</a> in form of a pull request. There will be a checklist of what is needed to fully complete the process.</p>
<p>It is a relatively lengthy process, so an alternative is to check out the module repo (linked above), and add it as Additional Module Path in the Application Settings.</p>

---
