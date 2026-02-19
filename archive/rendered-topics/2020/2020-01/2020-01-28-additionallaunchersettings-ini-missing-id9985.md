---
topic_id: 9985
title: "Additionallaunchersettings Ini Missing"
date: 2020-01-28
url: https://discourse.slicer.org/t/9985
---

# additionalLauncherSettings.ini missing

**Topic ID**: 9985
**Date**: 2020-01-28
**URL**: https://discourse.slicer.org/t/additionallaunchersettings-ini-missing/9985

---

## Post #1 by @rbahegne (2020-01-28 16:38 UTC)

<p>Hello six month ago i developped an extension. I used the 3d Slicer source version of 25/07/2019.</p>
<p>A collegue of mine tried to compile and launch it. He took the lastest stable 3D Slicer source. He manage to compile it and also my extension. But he can’t launch my extension because AdditionalLauncherSettings.ini is missing. For some unknown reason AdditionalLauncherSettings-configure.cmake is not generated while doing cmake and therefore AdditionalLauncherSettings.ini is not builded. We are currently out of ideas.</p>
<p>Could it be because he used a more recent build of 3D slicer ? Have any hints ?</p>

---

## Post #2 by @lassoan (2020-01-28 17:33 UTC)

<p>AdditionalLauncherSettings is just a convenience and in most cases you don’t need to use it. You can just add your extension DLLs to additional module paths in Slicer application settings / Modules.</p>
<p>Anyway, if additional launcher settings file is not generated using latest <em>preview</em> release (not the stable) then let us know.</p>

---

## Post #3 by @rbahegne (2020-01-29 08:52 UTC)

<p>We followed to instructions : <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions</a></p>
<p>So we just cloned the repo : git://github.com/Slicer/Slicer.git (after it was merged yesterday if i’m correct) and additional launcher settings file is not generated when compiling extension linked with this version of 3D Slicer.</p>

---

## Post #4 by @lassoan (2020-01-29 13:53 UTC)

<p>Compare your extension to the <a href="https://github.com/Slicer/Slicer/tree/master/Utilities/Templates">current extension/module templates</a>. Maybe you have missed adding <code>include(${Slicer_EXTENSION_GENERATE_CONFIG})</code> to your top-level CMakeLists.txt file.</p>

---

## Post #5 by @Sunderlandkyl (2020-02-04 19:43 UTC)

<p>This does seem to be a problem in the latest nightly.</p>
<p>Neither Sequences nor SlicerIGSIO generated an AdditionalLauncherSettings.ini when compiled against the current version of Slicer.</p>

---

## Post #6 by @Davide_Punzo (2020-02-05 08:52 UTC)

<p>I confirm, this happens also in linux.</p>

---

## Post #7 by @lassoan (2020-02-05 15:28 UTC)

<p>This is a regression due to a <a href="https://github.com/Slicer/Slicer/commit/adb735e6a2a1f3e2453aef2f9cfee45549c06d31">recent change</a>. I’ve pushed a <a href="https://github.com/Slicer/Slicer/commit/5ee23651c4bb332f6ff889a6f390b650c024c3e5">fix</a>.</p>

---
