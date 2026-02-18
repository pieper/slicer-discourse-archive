# Extension dependencies in custom apps

**Topic ID**: 23552
**Date**: 2022-05-24
**URL**: https://discourse.slicer.org/t/extension-dependencies-in-custom-apps/23552

---

## Post #1 by @cpinter (2022-05-24 08:59 UTC)

<p>Hi all,</p>
<p>Recently the SlicerIGT extension added a dependency to SlicerIGSIO. This is all good, but it made me face a situation in a custom app that I haven’t had to deal with before.</p>
<p>If an extension depends on another one, we need to define a variable, like <code>SlicerIGSIO_DIR</code>, and then SlicerIGT would find <code>SlicerIGSIOConfig.cmake</code> in that folder (I assume). However, in a custom app, the extension build directories differ from a normal extension build directory. There is no such cmake file for example.</p>
<p>Is there a way to force an extension to generate this cmake file? Or any suggestions how to move forward with this?</p>
<p>Thank you so much!</p>

---

## Post #2 by @Sunderlandkyl (2022-05-24 12:55 UTC)

<p>Maybe we could add a check to SlicerIGT that would only call if it is not part of a custom build.</p>
<p>Does this change in SlicerIGT work?:</p>
<pre><code class="lang-auto">if (NOT DEFINED Slicer_EXTENSION_SOURCE_DIRS)
  find_package(SlicerIGSIO REQUIRED) 
endif()
</code></pre>

---

## Post #3 by @cpinter (2022-05-24 13:11 UTC)

<p>Thanks Kyle, a solution I haven’t considered. Wouldn’t it prevent SlicerIGT from using the algorithms in SlicerIGSIO it depends on?</p>

---

## Post #4 by @Sunderlandkyl (2022-05-24 13:22 UTC)

<p>Good point. I think that since both SlicerIGT and SlicerIGSIO would be part of the build same build, it should be fine.</p>

---

## Post #5 by @cpinter (2022-05-24 13:33 UTC)

<p>OK let me try, thanks!</p>

---

## Post #6 by @cpinter (2022-05-24 19:59 UTC)

<p>Just as I suspected, without having found SlicerIGSIO the build fails with errors like this:</p>
<p><code>E:\s\sR\SlicerIGT\LandmarkDetection\Logic\vtkSlicerLandmarkDetectionLogic.cxx(38,10): fatal error C1083: Cannot open include file: 'vtkIGSIOLandmarkDetectionAlgo.h': No such file or directory [E:\s\sR\Slicer-build\E\SlicerIGT\LandmarkDetection\Logic\vtkSlicerLandmarkDetectionModuleLogic.vcxproj] [E:\s\sR\slicersources-build\Slicer.vcxproj] </code></p>
<p>Somehow we need to allow the discovery of the SlicerIGSIO sources and libraries within the custom app. What I can think of is to configure the <code>SlicerIGSIOConfig.cmake</code> file from an <code>.in</code> file and have that set all the variables.</p>
<p>Any other ideas <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a> ? If not then I’ll try with the <code>.in</code> configure approach. Thanks a lot!</p>

---

## Post #7 by @Sunderlandkyl (2022-05-24 20:17 UTC)

<p>vtkIGSIOLandmarkDetectionAlgo is from IGSIO, not SlicerIGSIO. SlicerIGSIO probably pulled in the IGSIO libraries previously.</p>
<p>What if you use:</p>
<pre><code class="lang-auto">if (NOT DEFINED Slicer_EXTENSION_SOURCE_DIRS)
  find_package(SlicerIGSIO REQUIRED) 
else()
  find_package(IGSIO REQUIRED) 
endif()
</code></pre>

---

## Post #8 by @cpinter (2022-05-24 21:43 UTC)

<p>This makes a lot of sense, Kyle. I didn’t even think that these algorithms were in IGSIO not SliceriGSIO. I started a build and it seems to have gone past these. Will send a PR if it finishes without errors. Thank you!</p>

---
