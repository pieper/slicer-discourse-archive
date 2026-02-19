---
topic_id: 19938
title: "Superbuild Extension Builds Failed When Python Was Installed"
date: 2021-09-30
url: https://discourse.slicer.org/t/19938
---

# Superbuild extension builds failed when Python was installed - good solution?

**Topic ID**: 19938
**Date**: 2021-09-30
**URL**: https://discourse.slicer.org/t/superbuild-extension-builds-failed-when-python-was-installed-good-solution/19938

---

## Post #1 by @cpinter (2021-09-30 16:13 UTC)

<p>Hi all,</p>
<p>I could not build first SlicerRT then SlicerOpenIGTLink today, and it seemed that the reason was a custom Python being installed on my Windows machine. See <a href="https://github.com/SlicerRt/SlicerRT/issues/198" class="inline-onebox">Plastimatch build fails · Issue #198 · SlicerRt/SlicerRT · GitHub</a></p>
<p>After chatting with <a class="mention" href="/u/lassoan">@lassoan</a> we decided that we define the missing (and then after uninstalling the custom Python undefined) Python variables, see <a href="https://github.com/SlicerRt/SlicerRT/commit/8b6784709356d6847bcbf7cfa647e48dce3ef2fc" class="inline-onebox">COMP: Fix Plastimatch configuration if Python was installed · SlicerRt/SlicerRT@8b67847 · GitHub</a> and <a href="https://github.com/openigtlink/SlicerOpenIGTLink/pull/116" class="inline-onebox">COMP: Fix subproject configuration if Python was installed by cpinter · Pull Request #116 · openigtlink/SlicerOpenIGTLink · GitHub</a> .</p>
<p>My question is, mainly to <a class="mention" href="/u/jcfr">@jcfr</a> if there is a better solution for this, other than manually adding these variables to the subproject CMake files that fail to configure in this case. Thanks!</p>

---

## Post #2 by @jcfr (2021-09-30 16:49 UTC)

<p>Currently, passing the variables is a sensible approach.</p>
<p>To streamline this, few possible approaches:</p>
<ul>
<li>(1) Update upstream VTK so that these variables are configured into <code>vtk-config</code> (or alike) and ensure project build against a VTK build tree would find the expected python. Now tracked in  <a href="https://gitlab.kitware.com/vtk/vtk/-/issues/18328">https://gitlab.kitware.com/vtk/vtk/-/issues/18328</a>
</li>
<li>(2) In case (1) doesn’t work out, update the Slicer/VTK fork to include relevant changes. Though … would prefer to minimize Slicer specific changes in our fork and try to only include backported changes.</li>
</ul>

---

## Post #3 by @jcfr (2021-09-30 16:55 UTC)

<p>One of the challenge is that there are two ways to find python libraries:</p>
<ul>
<li>
<a href="https://cmake.org/cmake/help/latest/module/FindPython.html">FindPython</a>/<a href="https://cmake.org/cmake/help/latest/module/FindPython3.html">FindPython3</a>
</li>
<li>
<a href="https://cmake.org/cmake/help/latest/module/FindPythonInterp.html">FindPythonInterp</a>/<a href="https://cmake.org/cmake/help/latest/module/FindPythonLibs.html">FindPythonLibs</a> now deprecated</li>
</ul>
<p>This is why we need to pass both set of variables ( <code>PYTHON_*</code> and <code>Python3_*</code>) and it may be challenging to have both sets configured into the VTK build tree …</p>

---
