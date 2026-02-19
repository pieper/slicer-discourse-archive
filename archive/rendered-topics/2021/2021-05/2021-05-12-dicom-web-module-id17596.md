---
topic_id: 17596
title: "Dicom Web Module"
date: 2021-05-12
url: https://discourse.slicer.org/t/17596
---

# DICOM Web module?

**Topic ID**: 17596
**Date**: 2021-05-12
**URL**: https://discourse.slicer.org/t/dicom-web-module/17596

---

## Post #1 by @spycolyf (2021-05-12 14:23 UTC)

<p>My team is interested in needing an example of  a DICOM WEB function. Does Slicer have a module that I can set up to illustrate DICOM WEB functionality? I hope that question makes sense as I don’t have experience with DICOM WEB. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Thanks</p>

---

## Post #2 by @pieper (2021-05-12 14:30 UTC)

<p>Do you mean searching and loading data via DICOMweb?  Yes, there’s this extension: <a href="https://github.com/lassoan/SlicerDICOMwebBrowser" class="inline-onebox">GitHub - lassoan/SlicerDICOMwebBrowser: 3D Slicer extension for browsing and downloading medical imaging collections from DICOMweb databases</a></p>
<p>There’s also a very experimental implementation of exposing Slicer’s dicom database as a DICOMweb server, but probably you don’t want that.</p>

---

## Post #3 by @lassoan (2021-05-12 17:46 UTC)

<p>Slicer core has two built-in DICOMweb features:</p>
<ol>
<li>Use a custom URL and DICOMweb to open a DICOM study directly from a web browser. This is how you can open Slicer from Kheops website.</li>
<li>You can push DICOM series via DICOMweb from the DICOM module.</li>
</ol>
<p>DICOMweb extension provides a DICOMweb browser that can browse a remote server content and download content to the local DICOM database.</p>
<p>You can find step-by-step instructions for all the above in this <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day1_7_DICOMTutorial.pptx?raw=true">PerkLab bootcamp tutorial</a>.</p>

---

## Post #4 by @spycolyf (2021-05-12 18:05 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, Thanks for the info!</p>

---
