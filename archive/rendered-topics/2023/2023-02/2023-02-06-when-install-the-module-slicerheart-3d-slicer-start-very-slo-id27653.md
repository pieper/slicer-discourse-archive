# When install the module SlicerHeart, 3D Slicer start very slowly

**Topic ID**: 27653
**Date**: 2023-02-06
**URL**: https://discourse.slicer.org/t/when-install-the-module-slicerheart-3d-slicer-start-very-slowly/27653

---

## Post #1 by @slicer365 (2023-02-06 10:29 UTC)

<p>When install the module SlicerHeart ,the 3Dslicer start very slowly,</p>
<p>the problem occur in the stable version and latest version.</p>

---

## Post #2 by @lassoan (2023-02-06 13:41 UTC)

<p>Warm start (starting Slicer after it was started recently) on Windows 10 on a desktop computer takes 4.5 seconds.</p>
<p>SlicerHeart installs SlicerIGT and SlicerIGSIO extensions, which measurable increases the startup time, to about 6.5 seconds. Considering the large number of modules these 3 extensions contain, the increase is reasonable.</p>
<p>The first startup after installing SlicerHeart is slower, about 18 seconds because ValveBatchExport module installs <code>pandas</code> python package. Our policy is not to install Python packages during module loading (because it slows down the next startup and the user may never use that module), and instead all additional Python packages must be installed on first use. I’ll fix this.</p>
<p>If your computer has network connectivity issues (slow network or uses corporate firewall or proxy server) then pandas installation may fail at each startup, slowing down each startup. As a quick fix, make sure pandas is installed by running <code>pip_install('pandas')</code> while connected to the internet.</p>

---
