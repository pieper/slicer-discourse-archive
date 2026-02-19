---
topic_id: 2794
title: "Compiling Slicer"
date: 2018-05-10
url: https://discourse.slicer.org/t/2794
---

# Compiling slicer

**Topic ID**: 2794
**Date**: 2018-05-10
**URL**: https://discourse.slicer.org/t/compiling-slicer/2794

---

## Post #1 by @vegoria (2018-05-10 13:28 UTC)

<p>Hi. I’m trying to compile slicer (using linux mint). And keep getting error:</p>
<blockquote>
<p>CMakeFiles/N4ITKBiasFieldCorrectionLib.dir/N4ITKBiasFieldCorrection.cxx.o: In function <code>ModuleEntryPoint': N4ITKBiasFieldCorrection.cxx:(.text+0xacb9): undefined reference to </code>itk::ResourceProbe&lt;double, double&gt;::UpdateMinimumMaximumMeasuredValue(double)’<br>
/usr/bin/ld: CMakeFiles/N4ITKBiasFieldCorrectionLib.dir/N4ITKBiasFieldCorrection.cxx.o: relocation R_X86_64_PC32 against undefined symbol `_ZN3itk13ResourceProbeIddE33UpdateMinimumMaximumMeasuredValueEd’ can not be used when making a shared object; recompile with -fPIC<br>
/usr/bin/ld: final link failed: Bad value<br>
collect2: error: ld returned 1 exit status<br>
make[5]: *** [lib/Slicer-4.9/cli-modules/libN4ITKBiasFieldCorrectionLib.so] Error 1<br>
make[4]: *** [Modules/CLI/N4ITKBiasFieldCorrection/CMakeFiles/N4ITKBiasFieldCorrectionLib.dir/all] Error 2<br>
make[4]: *** Waiting for unfinished jobs…</p>
</blockquote>
<p>could anybody help how to get rid of this problem?</p>

---

## Post #2 by @ihnorton (2018-05-10 13:45 UTC)

<p>Have you tried the SlicerPreview/nightly build? It looks like the SlicerPreview <a>linux build</a> is ok (although the tests have not run in the past few days)… So this may be a local issue.</p>
<p>Those kind of errors may happen when changes are made to the build environment (e.g. upgrading the compiler). CMake-generated projects are not very good at cleaning/updating stale builds, and often it is necessary to delete the ITKv4-build directory or the whole superbuild directory and start over.</p>

---
