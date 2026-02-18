# The program repeatedly turns on automatically.

**Topic ID**: 36494
**Date**: 2024-05-30
**URL**: https://discourse.slicer.org/t/the-program-repeatedly-turns-on-automatically/36494

---

## Post #1 by @Seokjun_Hwang (2024-05-30 11:49 UTC)

<p>After linking it with Jupyter Notebook, the Slicer program keeps turning on automatically even after I close it. Could you please help identify the cause and provide a solution? Even after closing Jupyter Notebook and Anaconda, the program keeps turning on.</p>

---

## Post #2 by @muratmaga (2024-05-30 14:59 UTC)

<p>You have to stop the jupyter kernel in Slicer module before you exit.</p>

---

## Post #3 by @lassoan (2024-05-30 15:12 UTC)

<p>If you already closed the browser (and cannot reopen the closed Jupyter server’s tab with Ctrl-Shift-T) then you can get the URL of the server as described <a href="https://github.com/Slicer/SlicerJupyter?tab=readme-ov-file#shutdown-all-slicer-jupyter-kernels">here</a>.</p>

---
