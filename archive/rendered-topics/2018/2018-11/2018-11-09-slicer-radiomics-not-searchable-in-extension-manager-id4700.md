# Slicer Radiomics not searchable in extension manager

**Topic ID**: 4700
**Date**: 2018-11-09
**URL**: https://discourse.slicer.org/t/slicer-radiomics-not-searchable-in-extension-manager/4700

---

## Post #1 by @stevenagl12 (2018-11-09 17:56 UTC)

<p>Hi, I am trying to get the radiomics extension and it is no longer searchable in 3D Slicer’s extension manager… I know that you can build it from the source code as well, but I would rather not have to do that.</p>

---

## Post #2 by @jamesobutler (2018-11-09 18:23 UTC)

<p>If you are using Windows, you should read the post: <a href="https://discourse.slicer.org/t/radiomics-extension-build-errors-on-windows/4616">Radiomics extension build errors on Windows</a>.  The build appears to still be failing as of last night (<a href="http://slicer.cdash.org/viewBuildError.php?buildid=1426550" rel="nofollow noopener">http://slicer.cdash.org/viewBuildError.php?buildid=1426550</a>).</p>

---

## Post #3 by @JoostJM (2018-11-12 09:58 UTC)

<p>The issue is also covered in the SlicerRadiomics github issue <a href="https://github.com/Radiomics/SlicerRadiomics/issues/50" rel="nofollow noopener">#50</a>. In short, one of the dependencies for PyRadiomics is failing to compile. We are currently trying to resolve this issue, but it takes time, especially since the issue is not in PyRadiomics source code.</p>

---
