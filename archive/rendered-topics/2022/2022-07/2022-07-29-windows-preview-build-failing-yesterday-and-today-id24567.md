---
topic_id: 24567
title: "Windows Preview Build Failing Yesterday And Today"
date: 2022-07-29
url: https://discourse.slicer.org/t/24567
---

# Windows preview build failing yesterday and today

**Topic ID**: 24567
**Date**: 2022-07-29
**URL**: https://discourse.slicer.org/t/windows-preview-build-failing-yesterday-and-today/24567

---

## Post #1 by @mikebind (2022-07-29 15:34 UTC)

<p>I am eager to test the improvements <a class="mention" href="/u/lassoan">@lassoan</a> added in a pull request (see <a href="https://discourse.slicer.org/t/convert-between-multivolume-and-volume-sequence/24504/5" class="inline-onebox">Convert between MultiVolume and Volume Sequence? - #5 by lassoan</a> for discussion) a few days ago, but the Windows preview build has failed each day since then. Looking at the Cdash error (<a href="https://slicer.cdash.org/viewBuildError.php?type=0&amp;buildid=2755183" class="inline-onebox" rel="noopener nofollow ugc">CDash</a>) it doesn’t seem likely to be related to the PR changes, but I don’t know enough to really know.</p>

---

## Post #2 by @Sam_Horvath (2022-07-29 15:39 UTC)

<p>Looking into the problem</p>

---

## Post #3 by @Sam_Horvath (2022-07-29 18:28 UTC)

<p>So, I addressed the original error (git lfs missing), but seem to have found some new ones. Still working on it.</p>
<pre><code class="lang-auto">D:\D\P\S-0-build\DCMTK\ofstd\include\dcmtk/ofstd/ofsockad.h(67,18): error C3861: 'memzero': identifier not found (compiling source file D:\D\P\S-0-build\DCMTK\ofstd\libsrc\ofstd.cc) [D:\D\P\S-0-build\DCMTK-build\ofstd\libsrc\ofstd.vcxproj] [D:\D\P\S-0-build\DCMTK.vcxproj]

</code></pre>

---
