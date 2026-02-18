# Installing whitematteranalysis: cl.exe not found

**Topic ID**: 9327
**Date**: 2019-11-28
**URL**: https://discourse.slicer.org/t/installing-whitematteranalysis-cl-exe-not-found/9327

---

## Post #1 by @LearningSlicerYay (2019-11-28 17:27 UTC)

<p>Hi all</p>
<p>I am trying to install whitematteranalysis but I keep on getting the error that cl.exe is not found, even though I’ve installed the C++ Visual Studio Build Tools. Has anyone encountered this error before?</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2019-11-28 19:13 UTC)

<p>It means that CMake cannot find the compiler. It may be normal that CMake cannot detect build tools installed at custom locations.</p>
<p>One solution is to install Visual Studio IDE, as most of the developers do. VS places build tools in standard location where CMake can find them.</p>
<p>If you prefer not to install VS IDE then you may need to run CMake from an environment where build tools are available in the PATH variable (e.g., from developer command prompt).</p>

---

## Post #3 by @zhangfanmark (2019-11-29 18:05 UTC)

<p>Hi</p>
<p>whitematteranalysis is currently not integrated into Slicer yet. You don’t need to compile anything. It is a python package that you can install using pip. <a href="https://github.com/SlicerDMRI/whitematteranalysis" rel="nofollow noopener">https://github.com/SlicerDMRI/whitematteranalysis</a></p>
<p>Regards,<br>
Fan</p>

---
