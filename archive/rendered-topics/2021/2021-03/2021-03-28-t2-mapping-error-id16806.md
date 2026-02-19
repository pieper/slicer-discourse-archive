---
topic_id: 16806
title: "T2 Mapping Error"
date: 2021-03-28
url: https://discourse.slicer.org/t/16806
---

# T2 mapping error

**Topic ID**: 16806
**Date**: 2021-03-28
**URL**: https://discourse.slicer.org/t/t2-mapping-error/16806

---

## Post #1 by @selmanca (2021-03-28 21:07 UTC)

<p>Operating system: Win 10<br>
Slicer version: 4.13.0</p>
<p>Hello developers,<br>
I am trying to use T2 mapping module for knee cartilage. After choosing input volume and T2 output volume, I click apply and it gives this error message in Python Interactor:<br>
module ‘string’ has no attribute ‘split’<br>
I think that it may be related with incompatibility of the T2 mapping code with Python version (3.6.7) of the latest Slicer version.<br>
Could you help me with this problem?<br>
Thanks</p>

---

## Post #2 by @pieper (2021-03-30 13:24 UTC)

<p>You are right, that extension probably hasn’t been updated to the lates python.  That’s usually not hard to fix, so maybe you can file an issue and or propose a fix to the developer.</p>
<p><a href="https://github.com/QIICR/Slicer-PETDICOMExtension/pull/new/15-fix-ofstream" class="onebox" target="_blank" rel="noopener">https://github.com/QIICR/Slicer-PETDICOMExtension/pull/new/15-fix-ofstream</a></p>

---

## Post #3 by @selmanca (2021-03-30 15:09 UTC)

<p>thanks for the suggestion</p>

---
