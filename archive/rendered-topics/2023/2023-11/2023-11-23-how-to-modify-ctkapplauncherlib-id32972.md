---
topic_id: 32972
title: "How To Modify Ctkapplauncherlib"
date: 2023-11-23
url: https://discourse.slicer.org/t/32972
---

# How to modify CTKAppLauncherLib?

**Topic ID**: 32972
**Date**: 2023-11-23
**URL**: https://discourse.slicer.org/t/how-to-modify-ctkapplauncherlib/32972

---

## Post #1 by @qiqi5210 (2023-11-23 03:30 UTC)

<p>In Windows, when compiling Slicer, is Slicer directly downloaded and used with the pre-compiled CTKAppLauncher? Specifically, the CTKAppLauncher-0.1.31-win-amd64.tar file. If I want to modify CTKAppLauncherLib, do I need to replace the relevant exe files from my compiled CTKAppLauncherLib-build folder to the CTKAPPLAUNCHER folder? However, when I perform this operation, I encounter compilation errors, and the generated exe file size differs significantly from the original. I am using a custom template in Slicer’s generation. I hope someone can provide some assistance. Thank you.</p>

---

## Post #2 by @qiqi5210 (2023-11-23 13:42 UTC)

<p>I have successfully replaced the compiled files from CTKAppLauncher into Slicer. Here, I would like to share my experience. The exes generated within CTKAppLauncherLib-build, compiled from within Slicer, were not functional, possibly due to missing dependencies in my Qt installation. Following the CTKAppLauncher’s build instructions, I obtained a statically compiled version of Qt 5.12 and used it to compile CTKAppLauncher separately. This resolved the issue.</p>

---

## Post #3 by @lassoan (2023-11-23 20:59 UTC)

<p>The launcher is needed to set up Qt paths so that dynamically-loaded Qt libraries can be found. Since Qt paths are not set up for the launcher itself, the launcher has to be built statically (all the libraries has to be linked into the executable).</p>
<p>We don’t build CTKAppLauncher executable as part of the Slicer build process because static linking of Qt libraries would require a paid Qt license.</p>

---
