# Importing classes/functions from scripts I built while coding a new module crashes it 

**Topic ID**: 10816
**Date**: 2020-03-24
**URL**: https://discourse.slicer.org/t/importing-classes-functions-from-scripts-i-built-while-coding-a-new-module-crashes-it/10816

---

## Post #1 by @Yana_Podolsky (2020-03-24 13:37 UTC)

<p>While writing a new module in a new extension using python I want to be able to use classes and\or functions from outer scripts (.py file) which I wrote by using:<br>
“from FolderName.FileName import FunctionName”</p>
<p>Every time I add the above line or even the known “from enum import Enum” the module crashes and isn’t shown in 3d slicer.<br>
(“import numpy as np” works)</p>
<p>Needless to say that the above mentions code-lines are perfectly working in simple python codes (no 3d-slicer association)</p>
<p>How can I fix this problem?<br>
Thanks, Yana.</p>

---

## Post #2 by @lassoan (2020-03-24 13:39 UTC)

<p><code>from enum import Enum</code> works perfectly for me. What Slicer version and operating system do you use?</p>

---

## Post #3 by @Yana_Podolsky (2020-03-24 14:48 UTC)

<p>3D-Slicer version:4.10.1<br>
operating system: windows 10 pro</p>

---

## Post #4 by @lassoan (2020-03-24 15:58 UTC)

<p>Please use most recent Slicer Preview Release and let us know if you find any issues.</p>

---
