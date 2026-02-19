---
topic_id: 38516
title: "Split Large Python Script Into Smaller Files"
date: 2024-09-24
url: https://discourse.slicer.org/t/38516
---

# Split large python script into smaller files

**Topic ID**: 38516
**Date**: 2024-09-24
**URL**: https://discourse.slicer.org/t/split-large-python-script-into-smaller-files/38516

---

## Post #1 by @maximeb (2024-09-24 12:57 UTC)

<p>Hi!</p>
<p>Our team is developing a 3D Slicer module.</p>
<p>However, we are unable to fragment the code that is used so our script has now more than 3 000 lines in one python script (and we would like to have for example 10 python scripts of 300 lines that make working the module we are developing for example). How can we fragment a python script into multiple files of a 3D Slicer module code?</p>
<p>Thank you in advance for considering this aspect,</p>

---

## Post #2 by @pieper (2024-09-24 13:04 UTC)

<p>You can split the code into different files and put them in a lib directory.  See for example how this is one in the DICOM module and the <a href="https://github.com/Slicer/Slicer/tree/main/Modules/Scripted/DICOMLib">DICOMLib directory</a>.</p>

---

## Post #3 by @maximeb (2024-09-24 13:07 UTC)

<p>Ok thanks for your quick answer! It is greatly appreciated!<br>
Cheers,</p>

---
