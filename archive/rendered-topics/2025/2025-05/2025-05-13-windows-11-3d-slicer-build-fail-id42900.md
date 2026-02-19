---
topic_id: 42900
title: "Windows 11 3D Slicer Build Fail"
date: 2025-05-13
url: https://discourse.slicer.org/t/42900
---

# Windows 11, 3D Slicer build fail

**Topic ID**: 42900
**Date**: 2025-05-13
**URL**: https://discourse.slicer.org/t/windows-11-3d-slicer-build-fail/42900

---

## Post #1 by @BaekHyeonSu (2025-05-13 02:12 UTC)

<p>3D slicer build is required to create an extension module using C++.<br>
I installed QT5.15.2, git, and cmake in a Windows 11 environment,<br>
and built according to the development guide, but I found that the build was stopped without any error message. How can I solve this?</p>

---

## Post #2 by @lassoan (2025-05-13 02:17 UTC)

<p>I have built Slcoer from scratch on Windows on a new computer two weeks ago and it went fine. The <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html">build instructions</a> has to be closely followed. For example, make sure you don’t use CMake 4.</p>
<p>Lots of messages are printed during the build process. If you missed them you can restart the build, the build error will be printed again. If you share those then we can tell what is wrong.</p>

---
