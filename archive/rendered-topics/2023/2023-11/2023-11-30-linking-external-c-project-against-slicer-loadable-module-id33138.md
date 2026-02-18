# Linking external C++ project against Slicer loadable-module

**Topic ID**: 33138
**Date**: 2023-11-30
**URL**: https://discourse.slicer.org/t/linking-external-c-project-against-slicer-loadable-module/33138

---

## Post #1 by @Federico (2023-11-30 08:45 UTC)

<p>Hi All,<br>
I saw there were a few posts that asked a similar question already but the answers were not clear enough to me unfortunately.<br>
Is it possible to link an external C++ exe/library against a Slicer Loadable Module (possibly only the logic)?<br>
If yes, how? Any documentation available, ideally for CMake?<br>
I saw that when building Slicer SlicerConfig.cmake and SlicerTargets.cmake are exported. I tried using these files to link against a module, cmake is fine but I have issues with the includes.<br>
Thank you all for your help!</p>

---

## Post #2 by @cpinter (2023-11-30 09:46 UTC)

<p>I think the most typical way to do this is to create a superbuild extension. You can find lots of them by now. SlicerRT, SlicerVMTK, SlicerVirtualReality, etc.</p>

---

## Post #3 by @Federico (2023-11-30 10:25 UTC)

<p>Hi Csaba, thanks for your answer. It seems to me, that these extensions are runtime libraries that are run from Slicer. If this is the case, this is not what I want. I want to load the needed Slicer-libraries from my application at runtime, not the other way around. Am I wrong?</p>

---

## Post #4 by @cpinter (2023-11-30 10:50 UTC)

<p>Ah, I see. Sorry I misunderstood the question then.</p>

---
