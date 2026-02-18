# Debug Slicer and SlicerRT Together

**Topic ID**: 26955
**Date**: 2022-12-28
**URL**: https://discourse.slicer.org/t/debug-slicer-and-slicerrt-together/26955

---

## Post #1 by @sani1486 (2022-12-28 05:25 UTC)

<p>Hello<br>
I am Looking for a way to simultaneously debug the slicer itself along with its Slicer RT extension together. I know how to run the slicerRt or Slicer in debug mode separately. But then I would actually like to check the call stacks and everything from SlicerRT to Slicer.<br>
Appreciation in Advance.</p>

---

## Post #2 by @pieper (2022-12-28 14:16 UTC)

<p>I guess you mean using an IDE debugger to look at the C++ code?  Yes, that should work normally if you build both the Slicer core and the SlicerRT extension in debug mode and either start up the app from the IDE or connect to the running process.</p>

---

## Post #3 by @sani1486 (2022-12-31 09:22 UTC)

<p>Thanks for your reply, I did build both of them in debug mode and i ran</p>
<pre><code class="lang-auto">.\S5D\Slicer-build\Slicer.exe --VisualStudio --launcher-no-splash --launcher-additional-settings E:/RTD/inner-build/AdditionalLauncherSettings.ini E:\RTD\inner-build\SlicerRT.sln
</code></pre>
<p>which eventually started SlicerRT sln, and I set up the ALL_BUILD project according to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/windowscpp.html" rel="noopener nofollow ugc">Debugging using Visual Studio</a><br>
from slicer doc. What is happening is I can set breakpoints in the slicer part of code,  for example <code>vtkMRMLSegmentationNode.cxx</code>. but if I try to set a breakpoint in SlicerRT code, for example, <code>vtkSlicerDicomRtImportExportModuleLogic.cxx</code>, MSVC says breakpoint won’t be hit because no symbol is loaded, so I went ahead and loaded a Dicom RT structure file, in the Dicom data browser, and found RT Structure examine failed, apparently, the initiated slicer.exe don’t think a slicerRT extension is loaded, which by the way doesn’t happen when I run the <code>SlicerWithSlicerRT.exe</code> file found in SlicerRt’s inner-build. So I think SlicerRT and Slicer were built fine. I just can’t seem to understand why the slicerRT specific modules and debug symbols aren’t loaded.</p>

---

## Post #4 by @sani1486 (2022-12-31 09:40 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> However, I got curious about the AdditionalLauncherSettings.ini file, and there are few paths listed, Strangely some of these paths don’t really exist on my device. the ini file is pasted down below. the c style <code>/**/</code> commented paths don’t exist.</p>
<pre><code class="lang-auto">[General]
additionalPathVariables=PYTHONPATH

[LibraryPaths]
1\path=E:/RTD/inner-build/lib/Slicer-5.3/cli-modules/Debug
2\path=E:/RTD/inner-build/lib/Slicer-5.3/qt-loadable-modules/Debug
/* 3\path=E:/RTD/lib/Slicer-5.3/Debug */
size=3

[Paths]
1\path=E:/RTD/inner-build/lib/Slicer-5.3/cli-modules/Debug
2\path=E:/RTD/inner-build/bin/Debug
/* 3\path=E:/RTD/bin/Debug */
size=3

[EnvironmentVariables]




[PYTHONPATH]
1\path=E:/RTD/inner-build/lib/Slicer-5.3/qt-scripted-modules
2\path=E:/RTD/inner-build/lib/Slicer-5.3/qt-loadable-modules/Debug
/* 3\path=E:/RTD/inner-build/lib/Slicer-5.3/qt-loadable-modules/Python */
/* 4\path=E:/RTD/lib/Slicer-5.3/Debug */
size=4

</code></pre>

---

## Post #5 by @pieper (2023-01-01 20:45 UTC)

<p>It sounds like you are close.  I haven’t debugged extensions with visual studio for quite a while myself, but I agree the paths look wrong in that ini file.   Perhaps there’s been some format change in the visual studio build files and the launcher settings code needs to be updated.</p>
<p>What I would suggest though is to start Slicer with the <code>SlicerWithSlicerRT.exe</code> command and then just connect the debugger to the process once it starts so it should pick up all the paths from the running process.  You can then load data and do your debugging.</p>

---

## Post #6 by @cpinter (2023-01-04 11:17 UTC)

<p>Your approach sounds good. This command starts VS for me with the ability to debug Slicer and SlicerRT:<br>
<code>..\S5D\Slicer-build\Slicer.exe --VisualStudio --launcher-no-splash --launcher-additional-settings ./SlicerRT_D/inner-build/AdditionalLauncherSettings.ini c:\d\_Extensions\SlicerRT_D\inner-build\SlicerRT.sln</code></p>
<p>Then when the solution opens, make sure that you select a project other than <code>ALL_BUILD</code> as startup, it can be any of them (qSlicer… or vtkMRML…). Then, in the project settings you need to set the command to be the <code>SlicerApp-real.exe</code>, such as <code>c:\d\S5D\Slicer-build\bin\Debug\SlicerApp-real.exe</code>. Then when you start the debugger, the breakpoints in Slicer and SlicerRT (and CTK etc) should be hit.</p>
<p>Of course what <a class="mention" href="/u/pieper">@pieper</a> suggests with <code>SlicerWithSlicerRT.exe</code> should work too, but what I have wrote above is how I have been doing it forever and it still works.</p>

---
