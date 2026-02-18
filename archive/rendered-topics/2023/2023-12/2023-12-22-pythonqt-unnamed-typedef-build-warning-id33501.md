# PythonQt unnamed `typedef` build warning

**Topic ID**: 33501
**Date**: 2023-12-22
**URL**: https://discourse.slicer.org/t/pythonqt-unnamed-typedef-build-warning/33501

---

## Post #1 by @jhlegarreta (2023-12-22 13:06 UTC)

<p>Hi,<br>
I am wondering about the plans to update the PythonQt version so that the below warning can be removed from all builds, including the extensions:</p>
<pre><code class="lang-auto">D:\D\P\S-0-build\CTK-build\CMakeExternals\Install\include\PythonQt\PythonQtClassWrapper.h(66,16): warning C5208: unnamed class used in typedef name cannot declare members other than non-static data members, member enumerations, or member classes (compiling source file D:\D\P\S-0-build\CTK-build\CTK-build\Libs\Core\generated_cpp\org_commontk_CTKCore\org_commontk_CTKCore_module_init.cpp) [D:\D\P\S-0-build\CTK-build\CTK-build\Libs\Core\CTKCorePythonQt.vcxproj] [D:\D\P\S-0-build\CTK-build\CTK.vcxproj] [D:\D\P\S-0-build\CTK.vcxproj]
</code></pre>
<p>It can be seen in e.g. <a href="https://slicer.cdash.org/viewBuildError.php?type=1&amp;buildid=3246386" class="inline-onebox" rel="noopener nofollow ugc">CDash</a> (Items per page: All; look for: C5208)</p>
<p>If I’m not mistaken PythonQt is pulled from<br>
<a href="https://github.com/MeVisLab/pythonqt" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MeVisLab/pythonqt: Dynamic Python binding for Qt Applications</a></p>
<p>The issues seems to have been solved 2 years ago:</p>
<ul>
<li>issue: <a href="https://github.com/MeVisLab/pythonqt/pull/47" class="inline-onebox" rel="noopener nofollow ugc">Fix a C++20 compatibility issue with an unnamed struct (P1766R1) by ClaudioHoffmann · Pull Request #47 · MeVisLab/pythonqt · GitHub</a></li>
<li>fix commit: <a href="https://github.com/MeVisLab/pythonqt/commit/fa274d2a82ee2be43a39491dde0a05cf9569fad4" class="inline-onebox" rel="noopener nofollow ugc">Make this a proper C++ struct · MeVisLab/pythonqt@fa274d2 · GitHub</a></li>
</ul>
<p>Seems like it will be an error in C++20.</p>
<p>Thank you</p>

---
