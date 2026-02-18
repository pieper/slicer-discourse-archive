# Error: ReadDataInternal: not found

**Topic ID**: 4386
**Date**: 2018-10-13
**URL**: https://discourse.slicer.org/t/error-readdatainternal-not-found/4386

---

## Post #1 by @ursus33 (2018-10-13 17:27 UTC)

<p>Operating system: Windows 10 64 bit<br>
Slicer version: 4.8.1<br>
Expected behavior: Loading model<br>
Actual behavior:<br>
There is error message like this.<br>
I cannot load the stl data even I have data in my computer.<br>
How can I fix this error?</p>
<p>ReadDataInternal: model file ‘G:/???/???<em>2018-10-11</em>??-?-UpperJaw.stl’ not found.</p>
<p>AddModel: error reading G:/???/???<em>2018-10-11</em>??-?-UpperJaw.stl</p>

---

## Post #2 by @lassoan (2018-10-13 17:30 UTC)

<p>Probably the issue is the presence of special characters in the file and folder names. Rename them to only contain ASCII characters.</p>

---
