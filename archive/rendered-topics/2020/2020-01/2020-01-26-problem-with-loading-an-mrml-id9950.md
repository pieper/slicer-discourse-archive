---
topic_id: 9950
title: "Problem With Loading An Mrml"
date: 2020-01-26
url: https://discourse.slicer.org/t/9950
---

# Problem with loading an mrml

**Topic ID**: 9950
**Date**: 2020-01-26
**URL**: https://discourse.slicer.org/t/problem-with-loading-an-mrml/9950

---

## Post #1 by @rlazol (2020-01-26 02:06 UTC)

<p>Operating system: win10<br>
Slicer version: 4.10.2<br>
Expected behavior: Previously if we clicked onto an mrml file it loaded the entire scene - CT sequences, models, segmentations.<br>
Actual behavior: Upon loading a Slicer mrml file, it does not show either the CT sequence or the segmentations. We tried overloading them on top of each other but no result.<br>
The root of the proble is perhaps that my collague started to work from a pendrive and it all worked fine. She could reopen here projects. But than she copied the files onto the computer and now it does not work. Not even if she puts it back onto the pendrive. What could be wrong? Is it possible that we have to start all over again? How to avoid such incidents?</p>

---

## Post #2 by @lassoan (2020-01-26 02:24 UTC)

<p>The MRML file does not store bulk data (images, models, segmentations, etc), just the relative paths of the data files (NRRD, STL,… files).</p>
<p>You either have to manually copy all the related data files along with the “mrml” file, or save all data in the scene in the single-file, portable “mrb” (MRML bundle) format. You can switch between mrml / mrb format by clicking on the package icon in the “Save data” window.</p>

---

## Post #3 by @rlazol (2020-01-26 09:21 UTC)

<p>Thanks for the reply.  The question is, is there a way to recover once the files are messed up?  In other words, how can I read the original structure from the mrml file?  If the user didn’t tick the “segmentations”, then we lost the file, did we?</p>
<details>
<summary>
Original in Hungarian</summary>
<p>Szia!<br>
Köszönöm a választ. A kérdés az, hogy van-e mód arra ,hogy ha egyszer összekutyulódott a file rendszer, akkor visszaálljon? Máshogy fogalmazva, hogy tudom kiolvasni az eredeti struktúrát az mrml fileból? Ha a lány a “segmentations”-t nem pipálta ki, akkor azt buktuk, ugye?</p>
<p>Laci</p>
</details>

---

## Post #4 by @lassoan (2020-01-26 12:19 UTC)

<p>By default all modified files are automatically selected for saving. Unless the user has manually unchecked the checkbox in Save data window, the file is saved somewhere and you can load it into Slicer by drag-and-drop / Add data.</p>

---

## Post #5 by @rlazol (2020-01-26 17:12 UTC)

<p>Thank you so much!<br>
Reinitz Laci</p>

---
