# Pycharm and 3d slicer

**Topic ID**: 21613
**Date**: 2022-01-25
**URL**: https://discourse.slicer.org/t/pycharm-and-3d-slicer/21613

---

## Post #1 by @zhiyuan (2022-01-25 06:19 UTC)

<p>I would like to ask, can I add the measurement length and angle of 3dslicer and the function of cutting the segmented 3D view to my own Python program. Is to run their own Python program, and then display the divided 3D view, and on this view, cut, length and angle measurement？</p>

---

## Post #2 by @lassoan (2022-01-25 06:27 UTC)

<p>Yes. You can access all features of Slicer via Pycharm. The only thing that you may find unusual is that since Slicer embeds Python, you’ll need to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#run-a-python-script-file-in-the-slicer-environment">launch your Python program using the Slicer executable</a>. You can then attach PyCharm debugger to it as described <a href="https://github.com/SlicerRt/SlicerDebuggingTools#instructions-for-pycharm">here</a>.</p>

---
