---
topic_id: 16578
title: "Slicer Jupyter In Slicer 4 11 20210226 Linux"
date: 2021-03-16
url: https://discourse.slicer.org/t/16578
---

# Slicer Jupyter in Slicer 4.11-20210226 Linux

**Topic ID**: 16578
**Date**: 2021-03-16
**URL**: https://discourse.slicer.org/t/slicer-jupyter-in-slicer-4-11-20210226-linux/16578

---

## Post #1 by @PaoloZaffino (2021-03-16 15:36 UTC)

<p>Hi all,<br>
maybe I’m wrong. but I can not find Slicer Jupyter extension in Slicer 4.11-20210226 (stable) for Linux.<br>
I tried also the preview, but it’s not present as well.</p>
<p>Was it moved into a different extension?</p>
<p>Best,<br>
Paolo</p>

---

## Post #2 by @jamesobutler (2021-03-16 16:53 UTC)

<p>It was not moved to a different extension, but it does have build errors which is why it is not showing up as an available extension through the Extensions Manager.</p>
<p>On Slicer 4.11-20210226 SlicerJupyter is currently available on Windows and macOS. This appears to be the only working configuration at the moment.</p>
<p>Slicer 4.11-20210226 - Linux - <a href="https://slicer.cdash.org/viewBuildError.php?buildid=2180730" rel="noopener nofollow ugc">Build Failure</a>.</p>
<p>Slicer Preview 29771 - Linux - <a href="https://slicer.cdash.org/viewBuildError.php?buildid=2180328" rel="noopener nofollow ugc">Build Failure</a><br>
Slicer Preview 29771 - Windows- <a href="https://slicer.cdash.org/viewBuildError.php?buildid=2180679" rel="noopener nofollow ugc">Build Failure</a><br>
Slicer Preview 29771 - macOS - <a href="https://slicer.cdash.org/viewBuildError.php?buildid=2180924" rel="noopener nofollow ugc">Build Failure</a></p>

---

## Post #3 by @manjula (2021-05-23 14:05 UTC)

<p>Is the Jupyter extension still not available for Linux users ? I cannot find the extension in the stable or in the preview releases.</p>

---

## Post #4 by @jamesobutler (2021-05-23 14:54 UTC)

<p>SlicerJupyter is still having build errors for latest stable and preview release. It is available on both Windows and macOS.</p>
<p>Slicer 4.11-20210226 - Linux - <a href="https://slicer.cdash.org/viewBuildError.php?buildid=2257475" rel="noopener nofollow ugc">Build Failure</a></p>
<p>Slicer Preview 29927 - Linux - <a href="https://slicer.cdash.org/viewBuildError.php?buildid=2256764" rel="noopener nofollow ugc">Build Failure</a></p>
<p>There is currently a GitHub issue regarding its status missing on the Linux platform <a href="https://github.com/Slicer/SlicerJupyter/issues/59" class="inline-onebox" rel="noopener nofollow ugc">Linux: extension SlicerJupyter not available in 4.13 preview releases · Issue #59 · Slicer/SlicerJupyter · GitHub</a>. Given that Linux development often lags behind due to fewer users/developers compared to other platforms, any help to resolve the issue is appreciated from the community.</p>

---

## Post #5 by @guitz (2021-09-21 07:23 UTC)

<p>Hello,<br>
Is there an option to download an older version of the extension, be it for the stable 4.11 or preview 4.13 version?<br>
I tried to navigate the extension server (<a href="http://slicer.kitware.com/midas3/" rel="noopener nofollow ugc">http://slicer.kitware.com/midas3/</a>…) but had no luck there.</p>

---

## Post #6 by @lassoan (2021-09-23 03:14 UTC)

<p>The extension manager was moved to a <a href="https://slicer-packages.kitware.com/#folder/5f4474d0e1d8c75dfc705482">new location</a>. However, you can only find SlicerJupyter for Slicer-4.10, which is very old, very limited.</p>
<p>You can use <a href="https://hub.docker.com/r/lassoan/slicer-notebook">this docker container</a> (source: <a href="https://github.com/Slicer/SlicerDocker/tree/master/slicer-notebook" class="inline-onebox">SlicerDocker/slicer-notebook at master · Slicer/SlicerDocker · GitHub</a>) locally or <a href="https://github.com/Slicer/SlicerJupyter#option-1-run-using-binder">on binder</a> until we fix the build issue. Not fresh, but better than Slicer-4.10.</p>
<p>Or, you can build Slicer and the extension locally (I’ve built SlicerJupyter successfully on a default Ubuntu 20.04 install).</p>

---

## Post #7 by @guitz (2021-09-23 06:31 UTC)

<p>Thank you very much Andras, this really helped.</p>
<p>Actually, by following the link to the extension manager new location I could find the extension package for slicer 4.11.20200930 (so not the last 4.11 version, but certainly still good enough for me).<br>
For reference the direct link to the linux package of this version is<br>
<a href="https://slicer-packages.kitware.com/#item/60b865d93987204c4bf545b0" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/#item/60b865d93987204c4bf545b0</a><br>
It is then possible to install the extension package by pointing the extension manager to the downloaded zip file.</p>
<p>Slicer 4.13 is indeed nicer to use in several respects (again congratulations!) but being able to 4.11 in our linux production environment is already very good.</p>
<p>Cheers!</p>
<p>[edit to inform other readers that one can install the downloaded package directly in slicer by using the extention manager]</p>

---
