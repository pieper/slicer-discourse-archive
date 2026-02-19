---
topic_id: 12196
title: "Cannot Import Ipywidgets Into Slicer Kernel In Jupyter Noteb"
date: 2020-06-24
url: https://discourse.slicer.org/t/12196
---

# Cannot import ipywidgets into Slicer kernel in Jupyter Notebook

**Topic ID**: 12196
**Date**: 2020-06-24
**URL**: https://discourse.slicer.org/t/cannot-import-ipywidgets-into-slicer-kernel-in-jupyter-notebook/12196

---

## Post #1 by @Ponyo2311 (2020-06-24 12:18 UTC)

<p>Operating system: windows10<br>
Slicer version: Slicer 4.11.0-2020-06-09<br>
Expected behavior: importation of ipywidgets module<br>
Actual behavior: ModuleNotFoundError</p>
<p>I have opened the Jupyter Notebook from my virtual environment, where the ipywidgets module (as the rest of the modules) has been installed.<br>
Unlike in a python kernel (where I can use ipywidgets), it seems to be not available in the Slicer kernel.</p>
<p>When I was installing the Slicer kernel, I followed <a href="https://github.com/Slicer/SlicerJupyter/blob/master/README.md#setup" rel="nofollow noopener">https://github.com/Slicer/SlicerJupyter/blob/master/README.md#setup</a> and double-checked with <a href="https://ipywidgets.readthedocs.io/en/latest/user_install.html" rel="nofollow noopener">https://ipywidgets.readthedocs.io/en/latest/user_install.html</a> whether I missed anything for ipywidgets installation.</p>
<p>Should I install something in a different place other than my virtual environment?</p>

---

## Post #2 by @lassoan (2020-06-24 15:09 UTC)

<p>You need to install ipywidgets in both 3D Slicer’s Python console and in the external Python environment.</p>

---

## Post #3 by @Ponyo2311 (2020-06-24 15:53 UTC)

<p>Yes, now it works!</p>
<p>Thanks a lot</p>

---

## Post #4 by @LalodeAvila369 (2023-08-22 17:47 UTC)

<p>How do you install ipywidgets in 3D Slicer’s Python console?</p>

---

## Post #5 by @jcfr (2023-08-22 19:47 UTC)

<blockquote>
<p>install ipywidgets in 3D Slicer’s Python console?</p>
</blockquote>
<p>For more details, see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#install-a-python-package">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#install-a-python-package</a></p>

---
