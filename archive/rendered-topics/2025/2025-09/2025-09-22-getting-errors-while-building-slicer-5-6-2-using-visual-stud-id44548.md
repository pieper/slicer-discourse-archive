---
topic_id: 44548
title: "Getting Errors While Building Slicer 5 6 2 Using Visual Stud"
date: 2025-09-22
url: https://discourse.slicer.org/t/44548
---

# Getting errors while building Slicer 5.6.2 using  Visual Studio 2022

**Topic ID**: 44548
**Date**: 2025-09-22
**URL**: https://discourse.slicer.org/t/getting-errors-while-building-slicer-5-6-2-using-visual-studio-2022/44548

---

## Post #1 by @kiran (2025-09-22 20:52 UTC)

<p>Hi all,</p>
<p>I’m trying to build <strong>Slicer 5.6.2</strong> from source on Windows 10 using Visual Studio 2022 (CMake 3.29.2, Ninja/VS generator). The CMake <strong>configure step completes successfully</strong> — all dependencies are found and I see <code>SuperBuild - Slicer[OK]</code>.</p>
<p>However, when I try to build the <code>Slicer</code> target, the build fails with this error:<br>
error code MSB8066<br>
Custom build for ‘C:\Users\Admin\Slicer-5.6.2-build\CMakeFiles\3a1e9347e5c691c76dc8fd672ddc792e\Slicer-mkdir.rule;C:\Users\Admin\Slicer-5.6.2-build\CMakeFiles\3a1e9347e5c691c76dc8fd672ddc792e\Slicer-download.rule;C:\Users\Admin\Slicer-5.6.2-build\CMakeFiles\3a1e9347e5c691c76dc8fd672ddc792e\Slicer-update.rule;C:\Users\Admin\Slicer-5.6.2-build\CMakeFiles\3a1e9347e5c691c76dc8fd672ddc792e\Slicer-patch.rule;C:\Users\Admin\Slicer-5.6.2-build\CMakeFiles\3a1e9347e5c691c76dc8fd672ddc792e\Slicer-configure.rule;C:\Users\Admin\Slicer-5.6.2-build\CMakeFiles\3a1e9347e5c691c76dc8fd672ddc792e\Slicer-build.rule;C:\Users\Admin\Slicer-5.6.2-build\CMakeFiles\3a1e9347e5c691c76dc8fd672ddc792e\Slicer-forceconfigure.rule;C:\Users\Admin\Slicer-5.6.2-build\CMakeFiles\3a1e9347e5c691c76dc8fd672ddc792e\Slicer-install.rule;C:\Users\Admin\Slicer-5.6.2-build\CMakeFiles\c5da1549ecc272d07054fb076acf0418\Slicer-complete.rule;C:\Users\Admin\Slicer-5.6.2-build\CMakeFiles\f26948234eae581a147caa198a7bd78d\Slicer.rule;C:\Users\Admin\Slicer-5.6.2\CMakeLists.txt’ exited with code 1.</p>
<p>Unfortunately, the error message is not very informative.</p>
<p>Things I’ve checked so far:</p>
<ul>
<li>
<p>CMake configure succeeds, reports all dependencies <code>[OK]</code></p>
</li>
<li>
<p>Qt 5.15.2 is installed and found</p>
</li>
<li>
<p>Python and OpenSSL are found</p>
</li>
<li>
<p>No clear error appears in the Visual Studio output</p>
</li>
</ul>
<p>Questions:</p>
<ol>
<li>
<p>Where should I look for the <strong>real error logs</strong>? (e.g. in <code>Slicer-prefix/src/Slicer-stamp/…</code>)</p>
</li>
<li>
<p>Has anyone seen this <code>MSB8066 exit code 1</code> issue on Windows builds recently?</p>
</li>
<li>
<p>Since my goal is to use Slicer libraries in my own project (not necessarily build the entire SuperBuild), would you recommend building only selected parts, or linking directly against the official Slicer binaries instead?</p>
</li>
</ol>

---
