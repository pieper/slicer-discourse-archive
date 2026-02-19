---
topic_id: 6774
title: "Nightly Build Does Not Run"
date: 2019-05-13
url: https://discourse.slicer.org/t/6774
---

# Nightly build does not run

**Topic ID**: 6774
**Date**: 2019-05-13
**URL**: https://discourse.slicer.org/t/nightly-build-does-not-run/6774

---

## Post #1 by @sheharyar_anwar (2019-05-13 11:38 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10<br>
Expected behavior: Run successfully after build<br>
Actual behavior: Closes with error that certain .dll files are missing just after appearance of logo. Specifically mentions CTKWidgets.dll, CTKVisualizationVTKCore.dll, CTKQtTesting.dll was not found.</p>

---

## Post #2 by @lassoan (2019-05-13 11:47 UTC)

<p>You need to start Slicer with Slicer.exe.</p>
<p>If you did that and you still get errors then it means that the DLLs are actually missing, most likely do to a build error. Check your build log.</p>

---

## Post #3 by @lassoan (2019-05-14 16:35 UTC)

<p>A post was split to a new topic: <a href="/t/simple-filters-module-do-not-have-any-filters-in-latest-nightly-version/6787">Simple Filters module do not have any filters in latest nightly version</a></p>

---

## Post #4 by @sheharyar_anwar (2019-05-15 12:32 UTC)

<p>It was a build error. The .dll files were actually missing. Rebuilding solved my problem.</p>

---

## Post #5 by @Mihai_Simion (2021-01-16 02:02 UTC)

<p><a href="https://www.mitk.org/download/releases/MITK-2018.04.2/Windows/MITK-v2018.04.2-windows-x86_64.exe" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.mitk.org/download/releases/MITK-2018.04.2/Windows/MITK-v2018.04.2-windows-x86_64.exe</a><br>
CTKWidgets.dll  is a dynamic link library file that is part of developed by <strong>German Cancer Research Center (DKFZ)</strong> .</p>
<ul>
<li>Name: <strong>CTKWidgets.dll</strong>
</li>
<li>Software: <strong>MITK - Medical Imaging and Interaction Toolkit</strong>
</li>
<li>Publisher: <strong>German Cancer Research Center (DKFZ)</strong>
</li>
<li>Publisher URL: <strong>[<a href="http://www.mitk.org" rel="noopener nofollow ugc">www.mitk.org</a>](<a href="http://www.mitk.org/" rel="noopener nofollow ugc">http://www.mitk.org/</a>)</strong>
</li>
<li>Help file:</li>
<li>Known to be up to <strong>144.73 MB</strong> in size on most Windows;</li>
</ul>

---

## Post #6 by @lassoan (2021-01-16 05:05 UTC)

<p>This forum is for 3D Slicer. You may get help with MITK via their <a href="https://sourceforge.net/p/mitk/mailman/mitk-users">mailing list</a>.</p>

---
