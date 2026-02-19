---
topic_id: 13768
title: "Extensions Build Error Numpy Not Found"
date: 2020-09-30
url: https://discourse.slicer.org/t/13768
---

# Extensions build error: numpy not found

**Topic ID**: 13768
**Date**: 2020-09-30
**URL**: https://discourse.slicer.org/t/extensions-build-error-numpy-not-found/13768

---

## Post #1 by @JoostJM (2020-09-30 09:28 UTC)

<p>In the SlicerRadiomics extension, PyRadiomics is built as an external dependency. However, in the Linux build, the PyRadiomics build <a href="http://slicer.cdash.org/buildSummary.php?buildid=2025491">fails</a>, due to “No module named numpy”.</p>
<p>Numpy is needed for de setup of PyRadiomics, as it’s headers are required to build the C-extensions in PyRadiomics.</p>
<p>Should I add a pip command to install this dependency? I thought numpy was already part of the Slicer superbuild, and in such a way it would potentially break things if you try to re-install it.</p>

---

## Post #2 by @jamesobutler (2020-09-30 13:22 UTC)

<p>Numpy should be included in the Slicer superbuild. Have you downloaded the latest Slicer preview on Linux to see if you can import numpy in the python interactor?</p>

---

## Post #3 by @JoostJM (2020-10-01 09:16 UTC)

<p>I will take a look. Interestingly though, this error only occurs on the 4.10 stable release. The nightly build completes without error.</p>

---
