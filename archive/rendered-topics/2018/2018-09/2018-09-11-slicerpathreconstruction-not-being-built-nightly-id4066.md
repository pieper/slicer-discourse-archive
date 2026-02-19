---
topic_id: 4066
title: "Slicerpathreconstruction Not Being Built Nightly"
date: 2018-09-11
url: https://discourse.slicer.org/t/4066
---

# SlicerPathReconstruction not being built nightly?

**Topic ID**: 4066
**Date**: 2018-09-11
**URL**: https://discourse.slicer.org/t/slicerpathreconstruction-not-being-built-nightly/4066

---

## Post #1 by @tavaughan (2018-09-11 15:03 UTC)

<p>I added a new extension called PathReconstruction to the index a few days ago. Unfortunately I can’t find the nightly build for PathReconstruction for Windows on cdash. I can see it for Linux and Mac. It looks like all the modules it depends on (SlicerIGT, SlicerRT, MarkupsToModel) have been built. Does anyone have any ideas why it might not be showing up?</p>

---

## Post #2 by @Sam_Horvath (2018-09-11 16:42 UTC)

<p>Hi Thomas:</p>
<p>I am looking into this on the dashboard.  It seems to be related to a failing test on SlicerIGT.  I will let you know how it goes.</p>
<p>Sam</p>

---

## Post #3 by @lassoan (2018-10-23 17:23 UTC)

<p>I’ve checked this on perklab.factory and found this in the log:</p>
<pre><code class="lang-auto">...
Project "C:\D\N\E-0\ALL_BUILD.vcxproj" (1) is building "C:\D\N\E-0\PathReconstruction.vcxproj" (71) on node 1 (default targets).
Project "C:\D\N\E-0\PathReconstruction.vcxproj" (71) is building "C:\D\N\E-0\SlicerIGT.vcxproj" (72) on node 1 (default targets).
PrepareForBuild:
  Creating directory "x64\Release\SlicerIGT\". 

...
(lots of logs of SlicerIGT being built - no build errors)
...

  InitializeBuildStatus:
    Creating "x64\Release\PACKAGE\PACKAGE.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
  PostBuildEvent:
    setlocal
    cd C:\D\N\E-0\SlicerIGT-build
    if %errorlevel% neq 0 goto :cmEnd
    C:
    if %errorlevel% neq 0 goto :cmEnd
    "C:\Program Files\CMake\bin\cpack.exe" -C Release --config ./CPackConfig.cmake
    if %errorlevel% neq 0 goto :cmEnd
    :cmEnd
    endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
    :cmErrorLevel
    exit /b %1
    :cmDone
    if %errorlevel% neq 0 goto :VCEnd
    :VCEnd
    CPack: Create package using ZIP
    CPack: Install projects
    CPack: - Install project: SlicerIGT
    CPack: Create package
    CPack: - package: C:/D/N/E-0/SlicerIGT-build/27513-win-amd64-SlicerIGT-git2775192-2018-10-10.zip generated.
  FinalizeBuildStatus:
    Deleting file "x64\Release\PACKAGE\PACKAGE.tlog\unsuccessfulbuild".
    Touching "x64\Release\PACKAGE\PACKAGE.tlog\PACKAGE.lastbuildstate".
  Done Building Project "C:\D\N\E-0\SlicerIGT-build\package.vcxproj" (default targets).
  Build succeeded.
      0 Warning(s)
      0 Error(s)
  Time Elapsed 00:00:45.28
  Command exited with the value: 0
  MakeCommand:"C:\Program Files\CMake\bin\cmake.exe" --build . --config "Release" --target "package"
     0 Compiler errors
     0 Compiler warnings
  SetCTestConfiguration:BuildDirectory:C:/D/N/E-0/SlicerIGT-build
  SetCTestConfiguration:SourceDirectory:C:/D/N/E-0/SlicerIGT-build
  SetCTestConfiguration:ProjectName:SlicerIGT
  SetCTestConfiguration:DropMethod:http
  SetCTestConfiguration:DropSite:slicer.cdash.org
  SetCTestConfiguration:DropLocation:/submit.php?project=SlicerPreview
  SetCTestConfiguration:IsCDash:TRUE
  Submit files (using http)
     Send to track: Extensions-Experimental
     Using HTTP submit method
     Drop site:http://slicer.cdash.org/submit.php?project=SlicerPreview
     Upload file: C:/D/N/E-0/SlicerIGT-build/Testing/20181023-1322/Build.xml to http://slicer.cdash.org/submit.php?project=SlicerPreview&amp;FileName=factory.perklab___27513-SlicerIGT-git2775192-MSBuild-64bits-Qt5.9-Release___20181023-1322-Extensions-Experimental___XML___Build.xml&amp;MD5=0749de234e9ec79681c0db2f9288d6fc Size: 1222
     Uploaded: C:/D/N/E-0/SlicerIGT-build/Testing/20181023-1322/Build.xml
     Submission successful
  -- build_SlicerIGT_wrapper_script: Ignoring result 0
  No install step for 'SlicerIGT'
  Completed 'SlicerIGT'
Done Building Project "C:\D\N\E-0\SlicerIGT.vcxproj" (default targets) -- FAILED.
Done Building Project "C:\D\N\E-0\PathReconstruction.vcxproj" (default targets) -- FAILED.
... 
</code></pre>
<p>So, it seems that for no apparent reason, SlicerIGT project build is reported to be failed, which prevents building of extensions that depend on it, such as PathReconstruction.</p>
<p>Could somebody investigate why SlicerIGT extension is reported to fail?</p>

---
