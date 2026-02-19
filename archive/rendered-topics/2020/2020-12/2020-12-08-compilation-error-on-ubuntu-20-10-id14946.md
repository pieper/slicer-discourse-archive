---
topic_id: 14946
title: "Compilation Error On Ubuntu 20 10"
date: 2020-12-08
url: https://discourse.slicer.org/t/14946
---

# Compilation error on Ubuntu 20.10

**Topic ID**: 14946
**Date**: 2020-12-08
**URL**: https://discourse.slicer.org/t/compilation-error-on-ubuntu-20-10/14946

---

## Post #1 by @CiroRaggio (2020-12-08 19:22 UTC)

<p>Hi all,<br>
I tried to compile Slicer on Ubuntu 20.10, I had the following error:</p>
<pre><code>  **[99%] Performing configure step for 'Slicer'
 * *loading initial cache file /home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-prefix/tmp/Slicer-cache-Debug.cmake
 * *CMake Error: The source directory "/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug" does not appear to contain CMakeLists.txt.
 * *make[2]: *** [CMakeFiles/Slicer.dir/build.make:139: Slicer-prefix/src/Slicer-stamp/Slicer-configure] Error 1
 * *make[1]: *** [CMakeFiles/Makefile2:197: CMakeFiles/Slicer.dir/all] Error 2
 * *make: *** [Makefile:95: all] Error 2
</code></pre>
<p>I tried setting BUILD_TYPE = Release and BUILD_TYPE = Debug but nothing changed.<br>
Please, can anyone help me?</p>

---

## Post #2 by @lassoan (2020-12-09 18:48 UTC)

<p>Many of us tested built on latest LTS (Ubuntu 20.04), see build instructions <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html">here</a>. If these instructions do not work for 20.10 then you may need to dig into the differences between 20.04 and 20.10.</p>
<p>What was your build command? Can you upload the full build log somewhere and post the link here?</p>

---

## Post #3 by @CiroRaggio (2020-12-11 14:18 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
thanks for the reply,<br>
the command I used is<br>
<code>make -j5 -k</code><br>
and this is the output <a href="https://pastebin.pl/view/e23bfb04" rel="noopener nofollow ugc">https://pastebin.pl/view/e23bfb04</a>.</p>

---

## Post #4 by @lassoan (2020-12-11 15:39 UTC)

<p>It seems that you have mixed Debug and Release configurations:</p>
<pre><code class="lang-auto">loading initial cache file /home/ciro/Scrivania/Slicer/Slicer-Release/Slicer-prefix/tmp/Slicer-cache-Release.cmake
loading initial cache file /home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-prefix/tmp/Slicer-cache-Debug.cmake
</code></pre>
<p>You could try to find where the remnants of the Slicer-SuperBuild-Debug configuration come from and fix it (e.g., remove Slicer-build and Slicer-prefix subfolders and configure&amp;generate the top-level project using CMake), but it would probably take less of your time if you wipe your complete build tree and start the build from scratch.</p>

---

## Post #5 by @CiroRaggio (2020-12-13 08:28 UTC)

<p>I deleted all the code and tried to download and compile again.<br>
Now I have a problem with VTK, this is the output: <a href="https://pastebin.pl/view/29d86a54" rel="noopener nofollow ugc">https://pastebin.pl/view/29d86a54</a></p>

---

## Post #6 by @lassoan (2020-12-14 03:48 UTC)

<p>Have you followed the build instructions? It seems that some external VTK build was found that of course was not compatible.</p>

---

## Post #7 by @CiroRaggio (2020-12-14 07:26 UTC)

<p>Yes, I followed the build instructions for Ubuntu 20.04.</p>

---

## Post #8 by @CiroRaggio (2020-12-16 10:18 UTC)

<p>I managed to compile, but Slicer quits after a few seconds.<br>
This is the output:</p>
<blockquote>
<p>ciro@ciro:~/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build$ ./Slicer --launcher-verbose<br>
info: AdditionalSettingsFilePath <span class="chcklst-box fa fa-square-o fa-fw"></span><br>
info: LauncherSplashImagePath [/home/ciro/Scrivania/Slicer/Applications/SlicerApp/Resources/Images/Slicer-SplashScreen.png]<br>
info: LauncherSplashScreenHideDelayMs [3000]<br>
info: ApplicationToLaunch [/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build/bin/./SlicerApp-real]<br>
info: ApplicationToLaunchArguments <span class="chcklst-box fa fa-square-o fa-fw"></span><br>
info: AdditionalSettingsFilePath <span class="chcklst-box fa fa-square-o fa-fw"></span><br>
info: LauncherDir [/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build]<br>
info: LauncherName [Slicer]<br>
info: OrganizationDomain [<a href="http://www.na-mic.org" rel="noopener nofollow ugc">www.na-mic.org</a>]<br>
info: OrganizationName [NA-MIC]<br>
info: ApplicationName [Slicer]<br>
info: ApplicationRevision [29523]<br>
info: SettingsFileName [/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build/./SlicerLauncherSettings.ini]<br>
info: SettingsDir [/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build]<br>
info: UserAdditionalSettingsDir [/home/ciro/.config/NA-MIC]<br>
info: UserAdditionalSettingsFileName [/home/ciro/.config/NA-MIC/Slicer-29523.ini]<br>
info: UserAdditionalSettingsFileBaseName <span class="chcklst-box fa fa-square-o fa-fw"></span><br>
info: AdditionalSettingsDir <span class="chcklst-box fa fa-square-o fa-fw"></span><br>
info: AdditionalSettingsExcludeGroups <span class="chcklst-box fa fa-square-o fa-fw"></span><br>
info: LauncherNoSplashScreen [0]<br>
info: AdditionalLauncherHelpShortArgument [-h]<br>
info: AdditionalLauncherHelpLongArgument [–help]<br>
info: AdditionalLauncherNoSplashArguments [–no-splash,–help,–version,–home,–program-path,–no-main-window,–settings-path,–temporary-path]<br>
info: DetachApplicationToLaunch [0]<br>
info: LoadEnvironment [-1]<br>
info: LauncherSplashImagePath [/home/ciro/Scrivania/Slicer/Applications/SlicerApp/Resources/Images/Slicer-SplashScreen.png]<br>
info: LauncherSplashScreenHideDelayMs [3000]<br>
info: ApplicationToLaunch [/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build/bin/./SlicerApp-real]<br>
info: ApplicationToLaunchArguments <span class="chcklst-box fa fa-square-o fa-fw"></span><br>
info: &lt;APPLAUNCHER_DIR&gt; → [/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build]<br>
info: &lt;APPLAUNCHER_NAME&gt; → [Slicer]<br>
info: &lt;APPLAUNCHER_SETTINGS_DIR&gt; (RegularSettings) → [/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build]<br>
info: &lt;APPLAUNCHER_SETTINGS_DIR&gt; (UserAdditionalSettings) → [/home/ciro/.config/NA-MIC]<br>
info: &lt;APPLAUNCHER_SETTINGS_DIR&gt; (AdditionalSettings) → [&lt;APPLAUNCHER_SETTINGS_DIR-NOTFOUND&gt;]<br>
info:  → [:]<br>
info: Setting env. variable [SLICER_HOME]:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build<br>
info: Setting env. variable [PIP_REQUIRE_VIRTUALENV]:0<br>
info: Setting env. variable [ITK_AUTOLOAD_PATH]:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build/lib/Slicer-4.13/ITKFactories/.<br>
info: Setting env. variable [PYTHONNOUSERSITE]:1<br>
info: Setting env. variable [PYTHONHOME]:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/python-install<br>
info: Setting env. variable [SSL_CERT_FILE]:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build/share/Slicer-4.13/Slicer.crt<br>
info: Setting env. variable [LD_LIBRARY_PATH]:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build/bin/.:…/lib/Slicer-4.13/qt-loadable-modules:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build/lib/Slicer-4.13/cli-modules/.:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build/lib/Slicer-4.13/qt-loadable-modules/.:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/OpenSSL:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/python-install/lib:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/VTK-build/lib/.:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/teem-build/bin/.:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/DCMTK-build/lib/.:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/ITK-build/lib/.:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/CTK-build/CTK-build/bin/.:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/CTK-build/QtTesting-build/.:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/CTK-build/PythonQt-build/.:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/LibArchive-install/lib:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/SimpleITK-build/SimpleITK-build/lib/.:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/SlicerExecutionModel-build/ModuleDescriptionParser/bin/.:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/python-install/lib/python3.6/site-packages/numpy/core:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/python-install/lib/python3.6/site-packages/numpy/lib:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/JsonCpp-build/src/lib_json/.<br>
info: Setting env. variable [PATH]:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build/bin/.:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build/lib/Slicer-4.13/cli-modules/.:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/python-install/bin:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/teem-build/bin/.<br>
info: Setting env. variable [QT_PLUGIN_PATH]:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build/bin:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/CTK-build/CTK-build/bin:/usr/lib/plugins<br>
info: Setting env. variable [PYTHONPATH]:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build/bin/.:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build/bin/Python:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build/lib/Slicer-4.13/qt-loadable-modules/.:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build/lib/Slicer-4.13/qt-loadable-modules/Python:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build/lib/Slicer-4.13/qt-scripted-modules:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/python-install/lib/python3.6:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/python-install/lib/python3.6/lib-dynload:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/python-install/lib/python3.6/site-packages:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/VTK-build/lib/python3.6/site-packages:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/CTK-build/CTK-build/bin/Python:/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/CTK-build/CTK-build/bin/.<br>
info: Starting [/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build/bin/./SlicerApp-real]<br>
info: launcher-timeout (ms) [-1000]<br>
info: DisableSplash [0]<br>
error: [/home/ciro/Scrivania/Slicer/Slicer-SuperBuild-Debug/Slicer-build/bin/./SlicerApp-real] exit abnormally - Report the problem.</p>
</blockquote>

---

## Post #9 by @RafaelPalomar (2020-12-16 10:34 UTC)

<p><a class="mention" href="/u/ciroraggio">@CiroRaggio</a>, have a look at this post: <a href="https://discourse.slicer.org/t/cant-start-latest-stable-on-ubuntu-20-04/14029/35" class="inline-onebox">Can't start latest stable on ubuntu 20.04</a>. You might have to pass a flag to the slicer python (<code>-DBUILTIN_CTYPES=ON</code>) to make it run properly in Ubuntu 20.10</p>

---
