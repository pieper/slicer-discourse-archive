---
topic_id: 12335
title: "Where Should I Download Vtk Qt And Ctk From"
date: 2020-07-02
url: https://discourse.slicer.org/t/12335
---

# Where should I download vtk, qt, and ctk from?

**Topic ID**: 12335
**Date**: 2020-07-02
**URL**: https://discourse.slicer.org/t/where-should-i-download-vtk-qt-and-ctk-from/12335

---

## Post #1 by @vertebra (2020-07-02 14:03 UTC)

<p>In my python module, where should I download vtk, qt, and ctk from? Thanks.</p>
<p>Also, it’s a great honor to receive new user of the month. Thank you, thank you.</p>

---

## Post #2 by @lassoan (2020-07-02 20:59 UTC)

<p>VTK is available on PyPI. For Qt and CTK we use PythonQt for Python wrapping, so they cannot be used in a standalone Python environment but you have to use them in an application, which embeds Python, such as 3D Slicer.</p>

---

## Post #3 by @zhiyuan (2022-04-20 07:34 UTC)

<p>Sorry, I don’t understand this meaning. For example, in your quicksegmen code, import VTK, QT, slicer, etc., how do I need to download the package in Anaconda</p>

---

## Post #4 by @lassoan (2022-04-20 11:41 UTC)

<p>Your don’t need Anaconda. All these packages are already installed in the Python environment that Slicer provides. You can install more packages using pip (instead of conda).</p>

---

## Post #5 by @zhiyuan (2022-04-24 07:39 UTC)

<p>I want to run your program on pycahrm instead of slicer, so I need to configure the environment. Slicer I can directly install pip, but QT, CTK I use pip install qt to report an error<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/cad45cca460845dc151ac4079e033b0b4aff7865.png" data-download-href="/uploads/short-url/sWjqSoCieFla2k8UyUMFz0PwM4Z.png?dl=1" title="T@DJBJFH%XELR(CTH7$_L" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/cad45cca460845dc151ac4079e033b0b4aff7865.png" alt="T@DJBJFH%XELR(CTH7$_L" data-base62-sha1="sWjqSoCieFla2k8UyUMFz0PwM4Z" width="690" height="58" data-dominant-color="181010"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">T@DJBJFH%XELR(CTH7$_L</span><span class="informations">926×78 7.03 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2022-04-24 15:01 UTC)

<p>Setting up Slicer’s Python environment requires importing libraries, instantiating many objects and configuring them. These are implemented in C++, in SlicerApp-real.exe. If you specify in Pycharm to use PythonSlicer.exe as a Python interpreter then you can import some libraries, such as vtk, SimpleITK, etc., but not all. For example, PythonQt is not designed to be imported like that and some other libraries are not (or not fully) Python-wrapped.</p>
<p>Therefore, if you want to run a Python script that uses qt, ctk, or any Slicer application classes then you need to use the Python virtual environment that Slicer sets up. You can make Pycharm debugger automatically connect to it as described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/overview.html#Python-debugging">here</a>, so once you set it up, it is all nice and and convenient. You can also <a href="https://github.com/Slicer/SlicerJupyter">use Slicer as a Jupyter notebook kernel</a> if you want to run scripts interactively in Slicer’s virtual Python environment.</p>

---
