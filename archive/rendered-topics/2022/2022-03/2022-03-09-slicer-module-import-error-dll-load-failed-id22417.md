# Slicer Module import error: dll load failed

**Topic ID**: 22417
**Date**: 2022-03-09
**URL**: https://discourse.slicer.org/t/slicer-module-import-error-dll-load-failed/22417

---

## Post #1 by @jiachaoliang (2022-03-09 19:39 UTC)

<p>I got an error when to use “import cv2”.</p>
<p>“ModuleNotFoundError: No Module named ‘cv2’”</p>
<p>But I had opencv-python-4.5.5.64 successfully installed right before this error code.</p>
<p>Any further clue? Many thanks!</p>

---

## Post #2 by @ebrahim (2022-03-10 01:59 UTC)

<p>Slicer has its own python environment. Use <code>slicer.util.pip_install</code> to install what you need. <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#install-a-python-package" rel="noopener nofollow ugc">See here.</a></p>

---
