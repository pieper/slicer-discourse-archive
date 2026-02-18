# How to package 3D Slicer on Ubuntu 16.04, which has been build

**Topic ID**: 13175
**Date**: 2020-08-26
**URL**: https://discourse.slicer.org/t/how-to-package-3d-slicer-on-ubuntu-16-04-which-has-been-build/13175

---

## Post #1 by @Aitekk (2020-08-26 13:19 UTC)

<p>Operating system:Ubuntu 16.04<br>
Slicer version:4.11<br>
Expected behavior:To package 3D Slicer on Ubuntu 16.04 for installing Slicer on other Ubuntu computers.<br>
Actual behavior:I cannot find instructions for packaging on Ubuntu in the guidance document ：<a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html" rel="nofollow noopener">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html</a></p>

---

## Post #2 by @Sunderlandkyl (2020-08-26 13:35 UTC)

<p>You can create a package by navigating to the “Slicer-build” folder and running:<br>
<code>make package</code></p>

---

## Post #3 by @pieper (2020-08-26 13:46 UTC)

<p>Yes, it’s documented here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/macos.html#package-slicer">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/macos.html#package-slicer</a></p>

---

## Post #4 by @lassoan (2020-08-26 15:11 UTC)

<p>The test&amp;package instructions were indeed missing from the Linux build instructions - I’ve added them now: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#package-slicer">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#package-slicer</a></p>
<p>It is very easy to edit readthedocs documentation - click “Edit on github” button in the top-left corner, make any changes, and submit the pull request.</p>

---
