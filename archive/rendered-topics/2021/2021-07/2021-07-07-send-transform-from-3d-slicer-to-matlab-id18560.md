---
topic_id: 18560
title: "Send Transform From 3D Slicer To Matlab"
date: 2021-07-07
url: https://discourse.slicer.org/t/18560
---

# Send transform from 3D slicer to MAtlab

**Topic ID**: 18560
**Date**: 2021-07-07
**URL**: https://discourse.slicer.org/t/send-transform-from-3d-slicer-to-matlab/18560

---

## Post #1 by @Matteo_Boles (2021-07-07 11:27 UTC)

<p>Hello,<br>
I am trying to send a transform from 3D slicer to matlab and I followed the steps in the examples at this link: <a href="https://github.com/PlusToolkit/PlusMatlabUtils" rel="noopener nofollow ugc">PlusToolkit/PlusMatlabUtils: Matlab utilities for reading/writing Plus data structures and communicating with Plus applications (github.com)</a>, but nothing works and in matlab I keep reading “no transforms are available”</p>
<p>How do I solve this problem?</p>

---

## Post #2 by @Matteo_Boles (2021-07-07 12:36 UTC)

<p>Anyone can please help me, I do not really know what to do</p>

---

## Post #3 by @lassoan (2021-07-09 05:46 UTC)

<p>We moved from Matlab to Python. See more information in this <a href="https://github.com/PlusToolkit/PlusMatlabUtils#notice">notice</a>.</p>
<p>I think you can use Python in Matlab. If this is the case then you can use the <a href="https://github.com/lassoan/pyigtl">pyigtl</a> Python package for receiving transforms that 3D Slicer sends.</p>

---
