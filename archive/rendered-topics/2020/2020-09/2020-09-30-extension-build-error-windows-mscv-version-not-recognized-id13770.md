---
topic_id: 13770
title: "Extension Build Error Windows Mscv Version Not Recognized"
date: 2020-09-30
url: https://discourse.slicer.org/t/13770
---

# Extension build error windows (MSCV version not recognized)

**Topic ID**: 13770
**Date**: 2020-09-30
**URL**: https://discourse.slicer.org/t/extension-build-error-windows-mscv-version-not-recognized/13770

---

## Post #1 by @JoostJM (2020-09-30 09:50 UTC)

<p>The SlicerRadiomics build on windows fails on the configuration step.<br>
From <a href="http://slicer.cdash.org/buildSummary.php?buildid=2025335">the log</a> it appears that it detects a MSVC_version of 1924, but just after that it states that this version is not found.</p>

---

## Post #2 by @jamesobutler (2020-09-30 13:14 UTC)

<p>That’s because FindVcvars.cmake for the v4.10.2 tag only knows up to Visual Studio 2017 (see <a href="https://github.com/Slicer/Slicer/blob/v4.10.2/CMake/FindVcvars.cmake#L132" rel="noopener nofollow ugc">here</a>), but the build machine now is using a newer Visual Studio 2019 version hence why it doesn’t know where to find the vcvars for this newer version. The latest Slicer code has an up-to-date version of FindVcvars.cmake (see <a href="https://github.com/Slicer/Slicer/blob/5e203109175dbfebb1e5151daed0178f12125ef1/CMake/FindVcvars.cmake#L134" rel="noopener nofollow ugc">here</a>).</p>

---

## Post #3 by @JoostJM (2020-09-30 16:52 UTC)

<p>Thanks for the links! However, I’m still a bit confused, why doesn’t my build system use the latest slicer code? Do I need to set something specific somewhere?</p>

---

## Post #4 by @jamesobutler (2020-09-30 18:18 UTC)

<p>The log that you linked was the nightly build of SlicerRadiomics for the Slicer Stable 4.10.2.  That is different from the nightly build of SlicerRadiomics for the Slicer Preview.</p>

---

## Post #5 by @JoostJM (2020-10-01 09:15 UTC)

<p>Ah thanks. I’ve confirmed the build is succeeding for the Nigthly build.</p>

---
