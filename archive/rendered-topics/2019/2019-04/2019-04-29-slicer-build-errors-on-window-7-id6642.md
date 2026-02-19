---
topic_id: 6642
title: "Slicer Build Errors On Window 7"
date: 2019-04-29
url: https://discourse.slicer.org/t/6642
---

# Slicer build errors on Window 7

**Topic ID**: 6642
**Date**: 2019-04-29
**URL**: https://discourse.slicer.org/t/slicer-build-errors-on-window-7/6642

---

## Post #1 by @smrolfe (2019-04-29 15:52 UTC)

<p>Hello,<br>
My Slicer build on a Windows 7 machine is failing due to errors building ITK and VTK. I’ve previously built Slicer on a Windows 10 machine and am using the same settings with the exception of unchecking the Slicer_USE_GIT_PROTOCOL option since this machine is behind a firewall.</p>
<p>The build is failing to build both ITK and VTK. The VTK error message is:</p>
<blockquote>
<p>56&gt;CMake Error at CMakeLists.txt:778 (find_package):<br>
56&gt;  Could not find a package configuration file provided by “VTK” (requested<br>
56&gt;  version 8) with any of the following names:<br>
56&gt;<br>
56&gt;    VTKConfig.cmake<br>
56&gt;    vtk-config.cmake<br>
56&gt;<br>
56&gt;  Add the installation prefix of “VTK” to CMAKE_PREFIX_PATH or set “VTK_DIR”<br>
56&gt;  to a directory containing one of the above files.  If “VTK” provides a<br>
56&gt;  separate development package or SDK, be sure it has been installed.</p>
</blockquote>
<p>ITK is also failing to find the corresponding configuration files. I would appreciate advice on what could cause this kind of error.</p>
<p>Thanks,<br>
Sara</p>

---

## Post #2 by @lassoan (2019-04-29 15:55 UTC)

<p>Has VTK and ITK build completed successfully? (do you see all the VTK dlls in c:\D\S4D\VTK-build\bin…?) If not, then there is an error before these errors are displayed that you need to address first.</p>
<p>Windows7 is not supported anymore by Microsoft, so I don’t think Slicer developers should still support it.</p>

---

## Post #3 by @smrolfe (2019-04-29 16:15 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>. I checked and the VTK dlls are not being built. It looks like this error may be the root cause:</p>
<blockquote>
<p>28&gt;Error downloading object: data/sample.cosmotools (9dc6346): Smudge error: Error downloading data/sample.cosmotools (9dc63465d864ec7a4546f1d006ca0153a5bb4c78fd4a42d16ad1177dabc70d75): batch response: Post <a href="https://gitlab.kitware.com/vtk/vtk-m.git/info/lfs/objects/batch:" rel="noopener nofollow ugc">https://gitlab.kitware.com/vtk/vtk-m.git/info/lfs/objects/batch:</a> x509: certificate signed by unknown authority<br>
28&gt;<br>
28&gt;Errors logged to C:\S_B\VTK.git\modules\VTK-m\lfs\logs\20190426T120855.9153945.log<br>
28&gt;Use <code>git lfs logs last</code> to view the log.<br>
28&gt;CUSTOMBUILD : error : external filter ‘git-lfs filter-process’ failed<br>
28&gt;fatal: data/sample.cosmotools: smudge filter lfs failed<br>
28&gt;Unable to checkout ‘8d0f441e1b391c6ec4c2662ee1454d8c901733fb’ in submodule path ‘ThirdParty/vtkm/vtk-m’</p>
</blockquote>
<p>This looks like it’s still using the git protocol to get VTK, despite this option being disabled in the cmake file? Could this be an issue related to using Windows7?</p>
<p>Thanks,<br>
Sara</p>

---

## Post #4 by @jamesobutler (2019-04-29 16:18 UTC)

<p>If you are reusing a build folder, when was the last time you built successfully?  If you haven’t built since the transition from ITKv4 to ITKv5 (about a month ago), you’ll want to do a clean build.  There have been some other major changes that have required a new clean build to get up-to-date with the current Slicer nightly.</p>

---

## Post #5 by @smrolfe (2019-04-29 16:24 UTC)

<p>Thanks <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, I am starting from a fresh build folder.</p>

---
