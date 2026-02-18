# Build process failed with errors

**Topic ID**: 23114
**Date**: 2022-04-25
**URL**: https://discourse.slicer.org/t/build-process-failed-with-errors/23114

---

## Post #1 by @Mrwa_Awoda (2022-04-25 13:03 UTC)

<p>My op-system is Windows 10.</p>
<p>Qt5.15.2</p>
<p>CMake version 3.22.2</p>
<p>Visual Studio 17 2022</p>
<p>I’m having errors with the Slicer build process in Release mode. Some errors such as (<code>Error		File C:/D/S4R/SimpleITK/CMake/CTestCustom.cmake.in does not exist.	SimpleITK	C:\D\S4R\CUSTOMBUILD	1</code>) appeared because the folders inside the build folder (S4R) are empty after the configuration process (from CMake). It solved after I copied the specific folder (SimpleITK for example) from another computer where the build successfully completed and built the SimpleITK package only in VS. Still don’t know why my build folder(S4R) are empty.</p>
<p>I followed all the building instructions and installed the prerequisites as the words said here “<a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html" class="inline-onebox" rel="noopener nofollow ugc">Windows — 3D Slicer documentation</a>”</p>
<p>Another errors I get due to something wrong with the ‘CMakeFile’ in the build folder still don’t know how to fix it. Here is the error in text :</p>
<pre><code class="lang-auto">|---|---|---|---|---|---|---|
|Error|MSB8066|Custom build for 'C:\D\S4R\CMakeFiles\b2bcbfa553be6b76f5311151bbb771b6\SimpleITK-configure.rule;C:\D\S4R\CMakeFiles\b2bcbfa553be6b76f5311151bbb771b6\SimpleITK-build.rule;C:\D\S4R\CMakeFiles\b2bcbfa553be6b76f5311151bbb771b6\SimpleITK-install.rule;C:\D\S4R\CMakeFiles\d0fbb327fb5d8976f542b004b1325aa2\SimpleITK-complete.rule;C:\D\S4R\CMakeFiles\dbe9d635f197b17f63b9c895eaab2164\SimpleITK.rule' exited with code 1.|SimpleITK|C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets|242||
</code></pre>
<p>and here is the output of the SimpleITK build process:</p><aside class="onebox googledocs" data-onebox-src="https://docs.google.com/document/d/1a8QkPN_z8nUCj_FaKFQoRLEESXepceMO95_O4TD18tM/edit?usp=sharing">
  <header class="source">

      <a href="https://docs.google.com/document/d/1a8QkPN_z8nUCj_FaKFQoRLEESXepceMO95_O4TD18tM/edit?usp=sharing" target="_blank" rel="noopener nofollow ugc">docs.google.com</a>
  </header>

  <article class="onebox-body">
    <a href="https://docs.google.com/document/d/1a8QkPN_z8nUCj_FaKFQoRLEESXepceMO95_O4TD18tM/edit?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-docs-logo"></span></a>

<h3><a href="https://docs.google.com/document/d/1a8QkPN_z8nUCj_FaKFQoRLEESXepceMO95_O4TD18tM/edit?usp=sharing" target="_blank" rel="noopener nofollow ugc">SimpleITK Build Output</a></h3>

<p>Build started... 1&amp;gt;------ Build started: Project: SimpleITK, Configuration: Release x64 ------ 1&amp;gt;Performing configure step for 'SimpleITK' 1&amp;gt;loading initial cache file C:/D/S4R/SimpleITK-prefix/tmp/SimpleITK-cache-Release.cmake 1&amp;gt;--...</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Same errors here with the CLI:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fb4e410e3c4f7d56c4a987b4e152c332c016585.jpeg" data-download-href="/uploads/short-url/2eWIzMog1NLOjmoXj1eSF1tVmkJ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fb4e410e3c4f7d56c4a987b4e152c332c016585.jpeg" alt="image" data-base62-sha1="2eWIzMog1NLOjmoXj1eSF1tVmkJ" width="650" height="500" data-dominant-color="1F1818"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">790×607 66.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I had another error (<code>cannot open input file 'optimized.lib' ...</code>) solved with rename the Python libs files.</p>

---

## Post #2 by @lassoan (2022-04-25 13:17 UTC)

<pre><code class="lang-auto">1&gt;CMake Warning at C:/D/S4R/SimpleITK/CMake/sitkLanguageOptions.cmake:138 (message):
1&gt;  Python version less than 2.7: "".
</code></pre>
<p>This indicates that there was something wrong with the Python build.</p>
<aside class="quote no-group" data-username="Mrwa_Awoda" data-post="1" data-topic="23114">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mrwa_awoda/48/10236_2.png" class="avatar"> Mrwa_Awoda:</div>
<blockquote>
<p>It solved after I copied the specific folder (SimpleITK for example) from another computer</p>
</blockquote>
</aside>
<p>This may mask the root cause of the error. Please remove the entire build folder (c:/D/S4R) and restart the build from scratch. When the build fails find the very first build error and copy it here. Do not change anything in the build tree until you hear back from us.</p>

---

## Post #3 by @Mrwa_Awoda (2022-04-26 08:17 UTC)

<p>Regarding a Python issue, should I update it? Although my current version is 3.10 already…</p>
<p>here is the first build error:</p>
<pre><code class="lang-auto">|Error|MSB8066|Custom build for 'C:\D\S4R\CMakeFiles\55933ca4f27d3b7bf2f7c4bb6b3e9b43\python-dicom-requirements-mkdir.rule;C:\D\S4R\CMakeFiles\55933ca4f27d3b7bf2f7c4bb6b3e9b43\python-dicom-requirements-download.rule;C:\D\S4R\CMakeFiles\55933ca4f27d3b7bf2f7c4bb6b3e9b43\python-dicom-requirements-update.rule;C:\D\S4R\CMakeFiles\55933ca4f27d3b7bf2f7c4bb6b3e9b43\python-dicom-requirements-patch.rule;C:\D\S4R\CMakeFiles\55933ca4f27d3b7bf2f7c4bb6b3e9b43\python-dicom-requirements-configure.rule;C:\D\S4R\CMakeFiles\55933ca4f27d3b7bf2f7c4bb6b3e9b43\python-dicom-requirements-build.rule;C:\D\S4R\CMakeFiles\55933ca4f27d3b7bf2f7c4bb6b3e9b43\python-dicom-requirements-generate_project_description.rule;C:\D\S4R\CMakeFiles\55933ca4f27d3b7bf2f7c4bb6b3e9b43\python-dicom-requirements-install.rule;C:\D\S4R\CMakeFiles\d0fbb327fb5d8976f542b004b1325aa2\python-dicom-requirements-complete.rule;C:\D\S4R\CMakeFiles\dbe9d635f197b17f63b9c895eaab2164\python-dicom-requirements.rule;C:\D\S4\CMakeLists.txt' exited with code 1.|python-dicom-requirements|C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets|242||
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e87906da9126c4cb37f46217429a674c44204e04.jpeg" data-download-href="/uploads/short-url/xay4s1Z1BtaNBFTXFH5ERMj0ei0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e87906da9126c4cb37f46217429a674c44204e04_2_690x233.jpeg" alt="image" data-base62-sha1="xay4s1Z1BtaNBFTXFH5ERMj0ei0" width="690" height="233" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e87906da9126c4cb37f46217429a674c44204e04_2_690x233.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e87906da9126c4cb37f46217429a674c44204e04.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e87906da9126c4cb37f46217429a674c44204e04.jpeg 2x" data-dominant-color="413B64"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">865×293 77.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>and here is the output of the build:</p><aside class="onebox googledocs" data-onebox-src="https://docs.google.com/document/d/1xQiTaJitWg4fi5bmxPXF-bAY7vvM-7AN/edit?usp=sharing&amp;ouid=109318822956054168149&amp;rtpof=true&amp;sd=true">
  <header class="source">

      <a href="https://docs.google.com/document/d/1xQiTaJitWg4fi5bmxPXF-bAY7vvM-7AN/edit?usp=sharing&amp;ouid=109318822956054168149&amp;rtpof=true&amp;sd=true" target="_blank" rel="noopener nofollow ugc">docs.google.com</a>
  </header>

  <article class="onebox-body">
    <a href="https://docs.google.com/document/d/1xQiTaJitWg4fi5bmxPXF-bAY7vvM-7AN/edit?usp=sharing&amp;ouid=109318822956054168149&amp;rtpof=true&amp;sd=true" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-docs-logo"></span></a>

<h3><a href="https://docs.google.com/document/d/1xQiTaJitWg4fi5bmxPXF-bAY7vvM-7AN/edit?usp=sharing&amp;ouid=109318822956054168149&amp;rtpof=true&amp;sd=true" target="_blank" rel="noopener nofollow ugc">Loading Google Docs</a></h3>

<p>This Doc is private</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2022-04-29 16:21 UTC)

<p>I’ve found the issue.</p>
<pre><code class="lang-auto">46&gt;-- Found PythonLibs: optimized;C:/D/S4R/python-install/libs/python39.lib;debug;C:/Users/toshiba/AppData/Local/Programs/Python/Python39/libs/python39_d.lib (found suitable exact version "3.9.10")
</code></pre>
<p>You installed Python on your computer and added to the system path or some other environment variable. This of course interferes with all other Python installations on your system, including the embedded Python interpreter in Slicer.</p>
<p>I would recommend to remove Python from your system path. Alternatively, you can temporarily (while you are building Slicer), rename the <code>C:/Users/toshiba/AppData/Local/Programs/Python</code> to something else (e.g., <code>C:/Users/toshiba/AppData/Local/Programs/PythonTemp</code>) to make sure that it is not found during the build process.</p>

---

## Post #5 by @Mrwa_Awoda (2022-05-03 20:47 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="23114">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I would recommend to remove Python from your system path. Alternatively, you can temporarily (while you are building Slicer), rename the <code>C:/Users/toshiba/AppData/Local/Programs/Python</code> to something else (e.g., <code>C:/Users/toshiba/AppData/Local/Programs/PythonTemp</code> ) to make sure that it is not found during the build process.</p>
</blockquote>
</aside>
<p>Build error solved by this… thankyou!</p>
<p>Yet, to execute the Test-Slicer process I’ve get this</p>
<blockquote>
<pre><code class="lang-auto">Total Test time (real) = 8769.17 sec
1&gt;
1&gt;The following tests FAILED:
1&gt;	622 - py_WebEngine (Timeout)
1&gt;	640 - py_TwoCLIsInParallelTest (Timeout)
1&gt;Errors while running CTest
1&gt;Output from these tests are in: C:/D/S4R/Slicer-build/Testing/Temporary/LastTest.log
1&gt;Use "--rerun-failed --output-on-failure" to re-run the failed cases verbosely.
1&gt;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(156,5): error MSB3073: The command "setlocal
1&gt;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(156,5): error MSB3073: "C:\Program Files\CMake\bin\ctest.exe" --force-new-ctest-process -C Release
1&gt;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(156,5): error MSB3073: if %errorlevel% neq 0 goto :cmEnd
1&gt;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(156,5): error MSB3073: :cmEnd
1&gt;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(156,5): error MSB3073: endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
1&gt;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(156,5): error MSB3073: :cmErrorLevel
1&gt;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(156,5): error MSB3073: exit /b %1
1&gt;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(156,5): error MSB3073: :cmDone
1&gt;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(156,5): error MSB3073: if %errorlevel% neq 0 goto :VCEnd
1&gt;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(156,5): error MSB3073: :VCEnd" exited with code 8.
1&gt;Done building project "RUN_TESTS.vcxproj" -- FAILED.
========== Build: 0 succeeded, 1 failed, 1 up-to-date, 0 skipped ==========
</code></pre>
</blockquote>
<p>here is the “Microsoft.CppCommon.targets” file as a txt:</p>
<blockquote>
<p><a href="https://drive.google.com/file/d/1s7Mjo6bMB9Can05cMBMjgVgeB9ti4Fks/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">Microsoft.CppCommon.targets.txt - Google Drive</a></p>
</blockquote>
<p>would you please check it and help me with what is wrong there!</p>

---

## Post #6 by @jamesobutler (2022-05-03 21:42 UTC)

<aside class="quote no-group" data-username="Mrwa_Awoda" data-post="5" data-topic="23114">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mrwa_awoda/48/10236_2.png" class="avatar"> Mrwa_Awoda:</div>
<blockquote>
<pre><code class="lang-auto">1&gt;The following tests FAILED:
1&gt; 622 - py_WebEngine (Timeout)
1&gt; 640 - py_TwoCLIsInParallelTest (Timeout)
1&gt;Errors while running CTest
</code></pre>
</blockquote>
</aside>
<p>This looks pretty typical. These tests are often unstable and can occasionally fail. You should consider your built Slicer to be working <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20">.</p>

---
