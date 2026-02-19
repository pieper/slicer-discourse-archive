---
topic_id: 764
title: "Build Error Ctk Custombuild Failed"
date: 2017-07-25
url: https://discourse.slicer.org/t/764
---

# Build error - CTK CustomBuild failed

**Topic ID**: 764
**Date**: 2017-07-25
**URL**: https://discourse.slicer.org/t/build-error-ctk-custombuild-failed/764

---

## Post #1 by @JK_Kim (2017-07-25 17:55 UTC)

<p>I am following the instructions for building (<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions</a>) and getting the following four errors. I am on Window 7 using VS2013(update 4).  Everything else works well other than these four errors. Can anyone help with this. This is my first Slicer build. Thank you~~<br>
JK</p>
<p>Error	1	error MSB6006: “cmd.exe” exited with code 1. [G:\Libs\slicer\Slicer_072417_64\CTK-build\CTK-build\Libs\Widgets\CTKWidgetsPythonQt.vcxproj] [G:\Libs\slicer\Slicer_072417_64\CTK-build\CTK.vcxproj]	C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets	170	5	CTK<br>
Error	2	error MSB6006: “cmd.exe” exited with code 1. [G:\Libs\slicer\Slicer_072417_64\CTK-build\CTK-build\Libs\Widgets\CTKWidgetsPythonQt.vcxproj] [G:\Libs\slicer\Slicer_072417_64\CTK-build\CTK.vcxproj]	C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets	170	5	CTK<br>
Error	3	error MSB6006: “cmd.exe” exited with code 1. [G:\Libs\slicer\Slicer_072417_64\CTK-build\CTK-build\Libs\Widgets\CTKWidgetsPythonQt.vcxproj] [G:\Libs\slicer\Slicer_072417_64\CTK-build\CTK.vcxproj]	C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets	170	5	CTK<br>
Error	4	error MSB6006: “cmd.exe” exited with code 1. [G:\Libs\slicer\Slicer_072417_64\CTK-build\CTK-build\Libs\Widgets\CTKWidgetsPythonQt.vcxproj] [G:\Libs\slicer\Slicer_072417_64\CTK-build\CTK.vcxproj]	C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets	170	5	CTK</p>
<p>&lt;CustomBuild<br>
Sources                     ="@(CustomBuild)“<br>
BuildSuffix                 =”$(_BuildSuffix)"</p>
<pre><code>  TrackerLogDirectory         ="%(CustomBuild.TrackerLogDirectory)"
  MinimalRebuildFromTracking  ="%(CustomBuild.MinimalRebuildFromTracking)"

  TLogReadFiles               ="@(CustomBuildTLogReadFiles)"
  TLogWriteFiles              ="@(CustomBuildTLogWriteFiles)"
  TrackFileAccess             ="$(TrackFileAccess)"
  ToolArchitecture            ="$(CustomBuildToolArchitecture)"
  TrackerFrameworkPath        ="$(CustomBuildTrackerFrameworkPath)"
  TrackerSdkPath              ="$(CustomBuildTrackerSdkPath)"

  AcceptableNonZeroExitCodes  ="%(CustomBuild.AcceptableNonZeroExitCodes)"
  &gt;
&lt;/CustomBuild&gt;</code></pre>

---

## Post #2 by @lassoan (2017-07-25 17:56 UTC)

<p>Unfortunately, a change was introduced a few days ago that breaks debug-mode build on windows. See details here: <a href="https://discourse.slicer.org/t/slicer-debug-mode-buid-error-in-2017-07-23-version-on-windows-due-to-bzip2/751/5">Slicer debug-mode buid error in 2017-07-23 version on Windows due to bzip2</a></p>

---

## Post #3 by @jcfr (2017-07-25 18:00 UTC)

<blockquote>
<p>Re: Slicer debug-mode buid error in 2017-07-23 version on Windows due to bzip2 + CTK errors</p>
</blockquote>
<p>This is being addressed. I will keep you posted.</p>

---

## Post #4 by @jcfr (2017-07-26 02:06 UTC)

<p><a class="mention" href="/u/jk_kim">@JK_Kim</a> Please update the source and try to rebuild. This should be fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26174">26174</a></p>

---
