---
topic_id: 37872
title: "Failed To Build Slicer Cause The Ctk Build Exited With Code"
date: 2024-08-14
url: https://discourse.slicer.org/t/37872
---

# Failed to build Slicer cause the CTK.build exited with code 1

**Topic ID**: 37872
**Date**: 2024-08-14
**URL**: https://discourse.slicer.org/t/failed-to-build-slicer-cause-the-ctk-build-exited-with-code-1/37872

---

## Post #1 by @jhan1245 (2024-08-14 06:57 UTC)

<p>Hello,</p>
<p>I have been attempting to build the latest version of Slicer over the past few days, but I encountered a failure when trying to build CTK. And here is the error log what I received.</p>
<p>CMake = 3.28.1<br>
Visual studio = 2022 , toolset v143<br>
QT = 5.15.2<br>
OS = WIindows 11 pro 23H2</p>
<pre><code class="lang-auto">      1&gt;Checking Build System
      CTKCore.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\Release\CTKCore.dll
      CTKCorePythonQt.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\Release\CTKCorePythonQt.pyd
      CTKDICOMCore.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\Release\CTKDICOMCore.dll
      CTKDICOMCorePythonQt.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\Release\CTKDICOMCorePythonQt.pyd
      CTKWidgets.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\Release\CTKWidgets.dll
      CTKDICOMWidgets.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\Release\CTKDICOMWidgets.dll
      CTKDICOMWidgetsPlugins.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\designer\Release\CTKDICOMWidgetsPlugins.dll
      PythonQt Wrapping - Generating generated_cpp/org_commontk_CTKDICOMWidgets/org_commontk_CTKDICOMWidgets_init.cpp
      Traceback (most recent call last):
        File "C:\T\SR\CTK\CMake\ctkWrapPythonQt.py", line 252, in &lt;module&gt; ctk_wrap_pythonqt(options.target, options.namespace, options.output_dir, args, options.extra_verbose)
        File "C:\T\SR\CTK\CMake\ctkWrapPythonQt.py", line 93, in ctk_wrap_pythonqtcontent = f.read()
      UnicodeDecodeError: 'cp949' codec can't decode byte 0xbf in position 2: illegal multibyte sequence
C:\Program Files\Microsoft Visual Studio\2022\Professional\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(254,5): error MSB8066: Custom build for 
'C:\T\SR\CTK-build\CTK-build\CMakeFiles\84d21e351f9783d195f938f6a6844a08\org_commontk_CTKDICOMWidgets_init.cpp.rule;
C:\T\SR\CTK-build\CTK-build\CMakeFiles\84d21e351f9783d195f938f6a6844a08\moc_org_commontk_CTKDICOMWidgets.cpp.rule;
C:\T\SR\CTK-build\CTK-build\CMakeFiles\1899b50f5d8953e3a01d207c6d8dd4ae\moc_ctkDICOMWidgetsPythonQtDecorators.cpp.rule' exited with code 1. 
[C:\T\SR\CTK-build\CTK-build\Libs\DICOM\Widgets\CTKDICOMWidgetsPythonQt.vcxproj] [C:\T\SR\CTK-build\CTK.vcxproj] [C:\T\SR\CTK.vcxproj]
         Creating library C:/T/SR/CTK-build/CTK-build/bin/Release/CTKImageProcessingITKCore.lib 
         and object C:/T/SR/CTK-build/CTK-build/bin/Release/CTKImageProcessingITKCore.exp
      CTKImageProcessingITKCore.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\Release\CTKImageProcessingITKCore.dll
         Creating library C:/T/SR/CTK-build/CTK-build/bin/Release/CTKImageProcessingITKCorePythonQt.lib 
         and object C:/T/SR/CTK-build/CTK-build/bin/Release/CTKImageProcessingITKCorePythonQt.exp
      CTKImageProcessingITKCorePythonQt.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\Release\CTKImageProcessingITKCorePythonQt.pyd
      CTKVisualizationVTKCore.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\Release\CTKVisualizationVTKCore.dll
      CTKVisualizationVTKWidgets.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\Release\CTKVisualizationVTKWidgets.dll
      CTKQtTesting.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\Release\CTKQtTesting.dll
      CTKQtTestingPythonQt.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\Release\CTKQtTestingPythonQt.pyd
      CTKScriptingPythonCore.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\Release\CTKScriptingPythonCore.dll
      CTKScriptingPythonWidgets.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\Release\CTKScriptingPythonWidgets.dll
      CTKScriptingPythonWidgetsPlugins.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\designer\Release\CTKScriptingPythonWidgetsPlugins.dll
      CTKScriptingPythonWidgetsPythonQt.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\Release\CTKScriptingPythonWidgetsPythonQt.pyd
      CTKVisualizationVTKCorePythonQt.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\Release\CTKVisualizationVTKCorePythonQt.pyd
      CTKVisualizationVTKWidgetsPlugins.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\designer\Release\CTKVisualizationVTKWidgetsPlugins.dll
      CTKVisualizationVTKWidgetsPythonQt.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\Release\CTKVisualizationVTKWidgetsPythonQt.pyd
      CTKWidgetsPlugins.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\designer\Release\CTKWidgetsPlugins.dll
      CTKWidgetsPythonQt.vcxproj -&gt; C:\T\SR\CTK-build\CTK-build\bin\Release\CTKWidgetsPythonQt.pyd

C:\Program Files\Microsoft Visual Studio\2022\Professional\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(254,5)
: error MSB8066: Custom build for '
C:\T\SR\CTK-build\CMakeFiles\bdeadf76b2a226097eea371c088ff1f3\CTK-configure.rule;
C:\T\SR\CTK-build\CMakeFiles\bdeadf76b2a226097eea371c088ff1f3\CTK-build.rule;
C:\T\SR\CTK-build\CMakeFiles\bdeadf76b2a226097eea371c088ff1f3\CTK-forceconfigure.rule;
C:\T\SR\CTK-build\CMakeFiles\bdeadf76b2a226097eea371c088ff1f3\CTK-install.rule;
C:\T\SR\CTK-build\CMakeFiles\d54a1a094e9ab1ece38bbab3c56288d5\CTK-complete.rule;
C:\T\SR\CTK-build\CMakeFiles\718f3319bb339f95dc70ff401d4b915e\CTK.rule;
C:\T\SR\CTK\CMakeLists.txt' exited with code 1. [C:\T\SR\CTK-build\CTK.vcxproj] [C:\T\SR\CTK.vcxproj]

C:\Program Files\Microsoft Visual Studio\2022\Professional\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(254,5)
: error MSB8066: Custom build for '
C:\T\SR\CMakeFiles\d9658749475c3d792303812dee9bf5c3\CTK-update.rule;
C:\T\SR\CMakeFiles\d9658749475c3d792303812dee9bf5c3\CTK-patch.rule;
C:\T\SR\CMakeFiles\d9658749475c3d792303812dee9bf5c3\CTK-configure.rule;
C:\T\SR\CMakeFiles\d9658749475c3d792303812dee9bf5c3\CTK-build.rule;
C:\T\SR\CMakeFiles\d9658749475c3d792303812dee9bf5c3\CTK-install.rule;
C:\T\SR\CMakeFiles\978258281182d3531409934d713d4cd3\CTK-complete.rule;
C:\T\SR\CMakeFiles\3f47221565dc58dedb5fc6659d43ce89\CTK.rule' exited with code 1. [C:\T\SR\CTK.vcxproj]
</code></pre>
<p>It seems like the issue might be related to cp949 Unicode encoding problems on generated cpp file.</p>
<p>I haven’t made any changes to the code; I simply cloned the main branch from the Slicer Git repository and followed the build instructions, but this error occurred. I’m wondering if there is a solution to this issue.</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2024-08-15 13:07 UTC)

<p>Good catch! This is due to an unlucky coincidence of some recently added CTK files containing a BOM, recently modified Python wrapping code not being robust enough for different encodings, and you using a computer that has system code page set to Korean (cp949). If you change your system code page or any of the two other issues are fixed then you’ll be able to build successfully.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a>, please have a look at:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/commontk/CTK/issues/1214">
  <header class="source">

      <a href="https://github.com/commontk/CTK/issues/1214" target="_blank" rel="noopener">github.com/commontk/CTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/issues/1214" target="_blank" rel="noopener">ctkWrapPythonQt.py fails on Korean computers on source files starting with UTF-8 BOM</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-08-15" data-time="13:02:59" data-timezone="UTC">01:02PM - 15 Aug 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">[Some CTK source files start with UTF-8 BOM](https://github.com/commontk/CTK/iss<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ues/1213), which causes [build failures on Korean computers (cp949 system code page)](https://discourse.slicer.org/t/failed-to-build-slicer-cause-the-ctk-build-exited-with-code-1/37872) due to [ctkWrapPythonQt.py](https://github.com/commontk/CTK/blob/f01b620112bba32f01fb0d2f4ed90dd51064ecb1/CMake/ctkWrapPythonQt.py#L93 fails on computers) failing on files containing a BOM.

ctkWrapPythonQt.py should be made more robust to work well regardless of system code page.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/davide_punzo">@Davide_Punzo</a>, could you please fix these files (and maybe disable automatic adding of BOM in your text editor):</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/commontk/CTK/issues/1213">
  <header class="source">

      <a href="https://github.com/commontk/CTK/issues/1213" target="_blank" rel="noopener">github.com/commontk/CTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/issues/1213" target="_blank" rel="noopener">Remove UTF-8 BOM from source files</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-08-15" data-time="12:59:56" data-timezone="UTC">12:59PM - 15 Aug 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">These source files start with UTF-8 BOM, which causes build failure on Korean co<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">mputers:

CTK\Libs\DICOM\Core\ctkDICOMRetrieve.cpp
CTK\Libs\DICOM\Widgets\ctkDICOMJobListWidget.h CTK\Libs\DICOM\Widgets\ctkDICOMPatientItemWidget.h CTK\Libs\DICOM\Widgets\ctkDICOMSeriesItemWidget.h CTK\Libs\DICOM\Widgets\ctkDICOMStudyItemWidget.h CTK\Libs\DICOM\Widgets\ctkDICOMVisualBrowserWidget.h

The build scripts should be improved to not be sensitive to the presence of a UTF-8 BOM, but for consistency, we should not just start using BOM for some source files. For now, the easiest is to keep using ASCII in all CTK source files. If there is a good reason to change this in the future then it should be changed for all source files.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Davide_Punzo (2024-08-15 18:16 UTC)

<p>Sure! Tomorrow morning I will open a PR!</p>

---

## Post #4 by @Davide_Punzo (2024-08-16 05:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="37872">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/davide_punzo">@Davide_Punzo</a>, could you please fix these files (and maybe disable automatic adding of BOM in your text editor):</p>
</blockquote>
</aside>
<p>Done in <a href="https://github.com/commontk/CTK/pull/1215" class="inline-onebox" rel="noopener nofollow ugc">COMP: Remove UTF-8 BOM from source files by Punzo · Pull Request #1215 · commontk/CTK · GitHub</a></p>

---

## Post #5 by @jhan1245 (2024-08-20 00:23 UTC)

<p>After changing the system locale to UTF-8 Beta in Windows and rebuilding the project, it succeeded.<br>
By going into the Control Panel’s system locale settings and selecting ‘Beta: Use Unicode UTF-8 for worldwide language support,’ I was able to solve this issue.</p>
<p>Thank you!</p>

---
