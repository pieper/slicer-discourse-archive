# Clone of model node can change the original model node

**Topic ID**: 14521
**Date**: 2020-11-10
**URL**: https://discourse.slicer.org/t/clone-of-model-node-can-change-the-original-model-node/14521

---

## Post #1 by @ungi (2020-11-10 16:16 UTC)

<p>Tested on Windows with latest stable (4.11.20200930) version.<br>
How to reproduce:</p>
<ol>
<li>Load or create a surface model node.</li>
<li>Clone it in the Data module</li>
<li>Create a transform node for the clone (model copy) and move it somewhere else</li>
<li>Harden the transform on the clone.<br>
At this point I would expect the original surface model node to not change. However, at the point of hardening the transform, both models go to the new transformed position. So I think the poly data is not really duplicated when cloning the model node.<br>
I think this is bug, the original node should not depend on changes made in the cloned node.</li>
</ol>

---

## Post #2 by @lassoan (2020-11-10 19:22 UTC)

<p>Thanks for reporting this, I’ve fixed this <a href="https://github.com/Slicer/Slicer/commit/6f3975bb4e6913bbff553733f047010a298bb3c3">here</a>, will be available in tomorrow’s Preview Release.</p>

---
