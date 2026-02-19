---
topic_id: 23923
title: "Problem With Packages Vtkvmtk And Pypes"
date: 2022-06-18
url: https://discourse.slicer.org/t/23923
---

# Problem with packages vtkvmtk and pypes

**Topic ID**: 23923
**Date**: 2022-06-18
**URL**: https://discourse.slicer.org/t/problem-with-packages-vtkvmtk-and-pypes/23923

---

## Post #1 by @19lollo95 (2022-06-18 08:40 UTC)

<p>I am working with a script that imports vtkvmtk and pypes but I keep getting the following error message:</p>
<p>No module named ‘vtkvmtk’<br>
…</p>
<p>how can I remedy this? Can I install these packages? If so, from where?</p>

---

## Post #2 by @mau_igna_06 (2022-06-18 09:11 UTC)

<p>The best way to do it if you are using Slicer is to call the extensions manager from the python interactor and install the vmtk extension</p>

---

## Post #3 by @19lollo95 (2022-06-18 09:29 UTC)

<p>I don’t think I quite understand what you mean, sorry</p>

---

## Post #4 by @mau_igna_06 (2022-06-18 10:51 UTC)

<p>The vmtk extension installed will let you import the code you want</p>

---

## Post #5 by @lassoan (2022-06-18 14:30 UTC)

<p><a class="mention" href="/u/19lollo95">@19lollo95</a> do you use VMTK in 3D Slicer’s Python environment or you install it to some other Python environments using pip or conda?</p>

---
