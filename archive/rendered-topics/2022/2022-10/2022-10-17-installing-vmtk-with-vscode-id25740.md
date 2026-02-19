---
topic_id: 25740
title: "Installing Vmtk With Vscode"
date: 2022-10-17
url: https://discourse.slicer.org/t/25740
---

# Installing VMTK with VSCode

**Topic ID**: 25740
**Date**: 2022-10-17
**URL**: https://discourse.slicer.org/t/installing-vmtk-with-vscode/25740

---

## Post #1 by @Malalvarez (2022-10-17 21:40 UTC)

<p>Hi, i am new at this, and trying to install VMTK and use it with Python 3.9 in Visual Studio Code. Is that possible? Or only from Anaconda is possible?</p>

---

## Post #2 by @lassoan (2022-10-17 21:44 UTC)

<p>If you don’t want to build VMTK then you can <a href="https://github.com/vmtk/vmtk/issues/359">install it from conda-forge</a>:</p>
<pre><code>conda install -c conda-forge vmtk
</code></pre>
<p>or you can download 3D Slicer, install VMTK extension, and use the virtual environment that 3D Slicer provides (PythonSlicer.exe).</p>

---

## Post #3 by @Malalvarez (2022-10-19 15:15 UTC)

<p>Do you have any tutorial to install it via anaconda? Thanks!</p>

---

## Post #4 by @lassoan (2022-10-19 16:05 UTC)

<p>I cannot help with that, as I don’t use Anaconda. You should be able to find instructions on the web. If you have trouble using VMTK in Python then I would recommend to use it within 3D Slicer, via a convenient graphical user interface.</p>

---
