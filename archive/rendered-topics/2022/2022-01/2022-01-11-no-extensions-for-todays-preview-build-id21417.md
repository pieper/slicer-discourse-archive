# No extensions for today's preview build

**Topic ID**: 21417
**Date**: 2022-01-11
**URL**: https://discourse.slicer.org/t/no-extensions-for-todays-preview-build/21417

---

## Post #1 by @muratmaga (2022-01-11 19:58 UTC)

<p>I can’t tell if that’s something on my end, but when I open the extension manager in today’s build (windows), there are no extensions listed. Searching them doesn’t find anything. There are no error messages in the log.</p>
<p>My regular stable works fine with the extension manager on the same computer (can install/uninstall new extensions).</p>

---

## Post #2 by @Sam_Horvath (2022-01-11 20:52 UTC)

<p>Looking into it.  It appears that all of the extension builds did not show up on CDash, which is strange.</p>

---

## Post #3 by @jamesobutler (2022-01-11 20:53 UTC)

<p>I see that as well (on Windows platform).</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/x.png?v=10" title=":x:" class="emoji" alt=":x:"> No extensions found <a href="https://slicer-packages.kitware.com/api/v1/file/hashsum/SHA512/03db475afb059242cc6dc43855b967a971efe7ef2cfccb2ac0caeceef75181d3bf72c1cf17b105b9ed48b5580e3e7f3c65b28196f1f16c0ad747a6e408a4d941/download" rel="noopener nofollow ugc">Slicer 4.13.0-2022-01-10</a><br>
<a href="https://extensions.slicer.org/catalog/All/30527/win" class="onebox" target="_blank" rel="noopener nofollow ugc">https://extensions.slicer.org/catalog/All/30527/win</a></p>
<p><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=10" title=":white_check_mark:" class="emoji" alt=":white_check_mark:"> Extensions found <a href="https://slicer.cdash.org/viewFiles.php?buildid=2548545" rel="noopener nofollow ugc">Slicer 4.13.0-2022-01-06</a><br>
<a href="https://extensions.slicer.org/catalog/All/30526/win" class="onebox" target="_blank" rel="noopener nofollow ugc">https://extensions.slicer.org/catalog/All/30526/win</a></p>

---

## Post #4 by @Sam_Horvath (2022-01-11 20:58 UTC)

<p>Windows error for extensions, Linux one is the same</p>
<pre><code class="lang-auto">[OUTPUT] 
* Extra verbosity turned on

[HANDLER_VERBOSE_OUTPUT] 
Reading Script: D:/D/DashboardScripts/overload-vs2019-slicerextensions_preview_nightly.cmake

[HANDLER_OUTPUT] 
-- Setting 'CTEST_TEST_TIMEOUT' variable with default value '900'

-- Setting 'CTEST_PARALLEL_LEVEL' variable with default value '8'
-- Setting 'CTEST_DROP_SITE' variable with default value 'slicer.cdash.org'
-- Setting 'run_ctest_submit' variable with default value 'TRUE'
-- Setting 'run_ctest_with_disable_clean' variable with default value 'FALSE'
-- Setting 'run_ctest_with_update' variable with default value 'TRUE'
-- Setting 'run_ctest_with_configure' variable with default value 'TRUE'
-- Setting 'run_ctest_with_build' variable with default value 'TRUE'
-- Setting 'run_ctest_with_notes' variable with default value 'TRUE'
-- Setting 'Slicer_UPLOAD_EXTENSIONS' variable with default value 'TRUE'
-- Setting 'run_extension_ctest_submit' variable with default value 'TRUE'
-- Setting 'run_extension_ctest_with_configure' variable with default value 'TRUE'
-- Setting 'run_extension_ctest_with_build' variable with default value 'TRUE'
-- Setting 'run_extension_ctest_with_test' variable with default value 'TRUE'
-- Setting 'run_extension_ctest_with_packages' variable with default value 'TRUE'
-- CTEST_GIT_COMMAND: C:/Users/svc-dashboard/AppData/Local/Programs/Git/cmd/git.exe
-- Removing binary directory [D:/D/P/S-0-E-b]
-- Removing binary directory [D:/D/P/S-0-E-b] - done
-- SCRIPT_MODE .......................: nightly
-- CTEST_BUILD_CONFIGURATION .........: Release
-- ADDITIONAL_CMAKECACHE_OPTION ......: 

-- CTEST_CMAKE_GENERATOR .............: Visual Studio 16 2019
-- CTEST_BUILD_FLAGS .................: /maxcpucount:4
-- EXTENSIONS_TRACK_QUALIFIER ........: master
-- EXTENSIONS_BUILDSYSTEM_TESTING ....: FALSE
-- EXTENSIONS_INDEX_GIT_REPOSITORY ...: git://github.com/Slicer/ExtensionsIndex.git
-- EXTENSIONS_INDEX_GIT_TAG ..........: origin/master
-- Slicer_DIR ........................: D:/D/P/Slicer-0-build/Slicer-build
-- BITNESS ...........................: 64
-- OPERATING_SYSTEM ..................: Windows10
-- COMPILER ..........................: VS2019
-- QT_VERSION ........................: 5.15.2
-- BUILD_NAME_SUFFIX .................: 
-- CTEST_BUILD_NAME ..................: Windows10-VS2019-64bits-Qt5.15.2-Release
-- HOSTNAME ..........................: overload
-- ORGANIZATION ......................: Kitware
-- CTEST_SITE ........................: overload.kitware
-- DASHBOARDS_DIR ....................: D:/D
-- EXTENSION_DASHBOARD_SUBDIR ........: P
-- EXTENSION_DIRECTORY_BASENAME ......: S
-- Slicer_DIRECTORY_IDENTIFIER .......: 0
-- CTEST_BINARY_DIRECTORY ............: D:/D/P/S-0-E-b
-- Slicer_SOURCE_DIR .................: D:/D/P/Slicer-0
-- EXTENSIONS_BUILDSYSTEM_SOURCE_DIRECTORY: D:/D/P/Slicer-0/Extensions/CMake
-- CTEST_SOURCE_DIRECTORY ............: D:/D/P/Slicer-0/Extensions/CMake
-- CTEST_CONFIGURATION_TYPE ..........: Release
-- CTEST_TEST_TIMEOUT ................: 900
-- CTEST_PARALLEL_LEVEL ..............: 8
-- CTEST_DROP_SITE ...................: slicer.cdash.org
-- run_ctest_submit ..................: TRUE
-- run_ctest_with_disable_clean ......: FALSE
-- run_ctest_with_update .............: TRUE
-- run_ctest_with_configure ..........: TRUE
-- run_ctest_with_build ..............: TRUE
-- run_ctest_with_notes ..............: TRUE
-- Slicer_UPLOAD_EXTENSIONS ..........: TRUE
-- run_extension_ctest_submit ........: TRUE
-- run_extension_ctest_with_configure : TRUE
-- run_extension_ctest_with_build ....: TRUE
-- run_extension_ctest_with_test .....: TRUE
-- run_extension_ctest_with_packages .: TRUE
-- CDASH_PROJECT_NAME ................: SlicerPreview
-- Slicer_EXTENSION_DESCRIPTION_DIR ..: D:/D/P/S-0-E-b/ExtensionsIndex
-- empty_binary_directory ............: TRUE
-- force_build .......................: TRUE
-- model .............................: Nightly
-- track .............................: Extensions-Nightly
-- CTEST_USE_LAUNCHERS ...............: 0
-- Setting ENV{ExternalData_OBJECT_STORES} to D:/D/.ExternalData
-- Slicer_REVISION:30527
-- Configuring D:/D/P/S-0-E-b/CTestConfig.cmake
[HANDLER_VERBOSE_OUTPUT] 
SetCTestConfiguration:SourceDirectory:D:/D/P/Slicer-0/Extensions/CMake

SetCTestConfiguration:BuildDirectory:D:/D/P/S-0-E-b
[HANDLER_OUTPUT] 
Run dashboard with model Nightly
   Source directory: D:/D/P/Slicer-0/Extensions/CMake
   Build directory: D:/D/P/S-0-E-b

   Group: Extensions-Nightly
   First perform the initial checkout: C:/cmake-3.17.2/bin/cmake.exe -P D:/D/DashboardScripts/overload-vs2019-slicerextensions_preview_nightly.cmake-origin-master-nightly-gitclone.cmake
   Perform checkout in directory: D:/D/P/Slicer-0/Extensions
[ERROR_MESSAGE] 
Initial checkout failed!

[HANDLER_VERBOSE_OUTPUT] 
SetCTestConfiguration:BuildDirectory:D:/D/P/S-0-E-b

SetCTestConfiguration:SourceDirectory:D:/D/P/S-0-E-b/ExtensionsIndex
SetCTestConfiguration:SourceDirectory:D:/D/P/S-0-E-b/ExtensionsIndex
SetCTestConfigurationFromCMakeVariable:GITCommand:CTEST_GIT_COMMAND
SetCTestConfiguration:GITCommand:C:/Users/svc-dashboard/AppData/Local/Programs/Git/cmd/git.exe
SetCTestConfigurationFromCMakeVariable:GITUpdateCustom:CTEST_GIT_UPDATE_CUSTOM
SetCTestConfiguration:GITUpdateCustom:C:/cmake-3.17.2/bin/cmake.exe;-P;D:/D/DashboardScripts/overload-vs2019-slicerextensions_preview_nightly.cmake-origin-master-nightly-gitupdate.cmake
[HANDLER_OUTPUT] 
   Updating the repository: D:/D/P/S-0-E-b/ExtensionsIndex

[ERROR_MESSAGE] 
Cannot find UpdateCommand  configuration key.

[HANDLER_OUTPUT] 
-- First time build - Initialize CMakeCache.txt

-- FILES_UPDATED ................: -1
-- force_build ..................: TRUE
-- Slicer_PREVIOUS_WC_REVISION ..: 
-- Slicer_WC_REVISION ...........: 30527
[HANDLER_VERBOSE_OUTPUT] 
SetCTestConfiguration:BuildDirectory:D:/D/P/S-0-E-b

SetCTestConfiguration:SourceDirectory:D:/D/P/Slicer-0/Extensions/CMake
SetCTestConfigurationFromCMakeVariable:DropSite:CTEST_DROP_SITE
SetCTestConfiguration:DropSite:slicer.cdash.org
[OUTPUT] 
	Add file: D:/D/DashboardScripts/overload-vs2019-slicerextensions_preview_nightly.cmake

[HANDLER_OUTPUT] 
Submit files

   Send to group: Extensions-Nightly
   SubmitURL: http://slicer.cdash.org
   Submission successful
[HANDLER_VERBOSE_OUTPUT] 
SetCTestConfiguration:BuildDirectory:D:/D/P/S-0-E-b

SetCTestConfiguration:SourceDirectory:D:/D/P/Slicer-0/Extensions/CMake
SetCTestConfiguration:ConfigureCommand:"C:/cmake-3.17.2/bin/cmake.exe" "-GVisual Studio 16 2019" "-Ax64" "-Tv142" "D:/D/P/Slicer-0/Extensions/CMake"
[HANDLER_OUTPUT] 
Configure project

[ERROR_MESSAGE] 
Current Tag empty, this may mean NightlyStartTime / CTEST_NIGHTLY_START_TIME was not set correctly. Or maybe you forgot to call ctest_start() before calling ctest_configure().

Cannot open configure file
</code></pre>

---

## Post #5 by @mikebind (2022-01-11 21:04 UTC)

<p>I see no extensions on today’s preview on Windows.  I grabbed Slicer 4.13.0-2022-01-06 from <a class="mention" href="/u/jamesobutler">@jamesobutler</a>’s message and confirm that I see extensions listed there.  While it seems to be working OK, it does keep showing error messages like the following<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/5173662a8ec215e8ce0520964249d10c2c1c4bc8.png" alt="image" data-base62-sha1="bCxUP3VVXfdJ7xAhXCB2fsQt1tC" width="353" height="81"></p>

---

## Post #6 by @Sam_Horvath (2022-01-11 21:05 UTC)

<p>Yes, no extensions have been built for any platform see: <a href="https://slicer.cdash.org/index.php?project=SlicerPreview" class="inline-onebox">CDash</a></p>

---

## Post #7 by @jamesobutler (2022-01-11 21:05 UTC)

<aside class="quote no-group" data-username="Sam_Horvath" data-post="4" data-topic="21417">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote>
<pre><code class="lang-auto">   First perform the initial checkout: C:/cmake-3.17.2/bin/cmake.exe -P D:/D/DashboardScripts/overload-vs2019-slicerextensions_preview_nightly.cmake-origin-master-nightly-gitclone.cmake
   Perform checkout in directory: D:/D/P/Slicer-0/Extensions
[ERROR_MESSAGE] 
Initial checkout failed!
</code></pre>
</blockquote>
</aside>
<p>This a “no more unauthenticated git” issue? <a href="https://github.blog/2021-09-01-improving-git-protocol-security-github/" class="inline-onebox" rel="noopener nofollow ugc">Improving Git protocol security on GitHub - The GitHub Blog</a></p>
<blockquote>
<p>January 11, 2022 Final brownout.</p>
<p>This is the full brownout period where we’ll temporarily stop accepting the deprecated key and signature types, ciphers, and MACs, and the unencrypted Git protocol. This will help clients discover any lingering use of older keys or old URLs.</p>
</blockquote>

---

## Post #8 by @Sam_Horvath (2022-01-11 21:05 UTC)

<p>That would likely be it!</p>

---

## Post #9 by @Sam_Horvath (2022-01-11 21:09 UTC)

<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/DashboardScripts/blob/70e366eeedeccf9c849a04bb335a76311d32dd58/metroplex-slicerextensions_preview_nightly.cmake#L44">
  <header class="source">

      <a href="https://github.com/Slicer/DashboardScripts/blob/70e366eeedeccf9c849a04bb335a76311d32dd58/metroplex-slicerextensions_preview_nightly.cmake#L44" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/DashboardScripts/blob/70e366eeedeccf9c849a04bb335a76311d32dd58/metroplex-slicerextensions_preview_nightly.cmake#L44" target="_blank" rel="noopener">Slicer/DashboardScripts/blob/70e366eeedeccf9c849a04bb335a76311d32dd58/metroplex-slicerextensions_preview_nightly.cmake#L44</a></h4>



  <pre class="onebox">    <code class="lang-cmake">
      <ol class="start lines" start="34" style="counter-reset: li-counter 33 ;">
          <li>                                                      # Set to Slicer version XYZ for Stable release build</li>
          <li>dashboard_set(Slicer_SOURCE_DIR "${DASHBOARDS_DIR}/${Slicer_DASHBOARD_SUBDIR}/${Slicer_DIRECTORY_BASENAME}-${Slicer_DIRECTORY_IDENTIFIER}")</li>
          <li>dashboard_set(Slicer_DIR        "${DASHBOARDS_DIR}/${Slicer_DASHBOARD_SUBDIR}/${Slicer_DIRECTORY_BASENAME}-${Slicer_DIRECTORY_IDENTIFIER}-build/Slicer-build")</li>
          <li>
          </li>
<li># CTEST_SOURCE_DIRECTORY: &lt;Slicer_SOURCE_DIR&gt;/Extensions/CMake</li>
          <li># CTEST_BINARY_DIRECTORY: &lt;DASHBOARDS_DIR&gt;/&lt;EXTENSION_DASHBOARD_SUBDIR&gt;/&lt;EXTENSION_DIRECTORY_BASENAME&gt;-&lt;Slicer_DIRECTORY_IDENTIFIER&gt;-E[-T]-b</li>
          <li>dashboard_set(EXTENSION_DASHBOARD_SUBDIR   "${Slicer_RELEASE_TYPE}")</li>
          <li>dashboard_set(EXTENSION_DIRECTORY_BASENAME "S")</li>
          <li>
          </li>
<li>dashboard_set(EXTENSIONS_INDEX_GIT_TAG        "origin/${EXTENSIONS_INDEX_BRANCH}") # origin/master, origin/X.Y, ...</li>
          <li class="selected">dashboard_set(EXTENSIONS_INDEX_GIT_REPOSITORY "git://github.com/Slicer/ExtensionsIndex.git")</li>
          <li>
          </li>
<li># Build Name: &lt;OPERATING_SYSTEM&gt;-&lt;COMPILER&gt;-&lt;BITNESS&gt;bits-QT&lt;QT_VERSION&gt;[-&lt;BUILD_NAME_SUFFIX&gt;]-&lt;CTEST_BUILD_CONFIGURATION</li>
          <li>set(BUILD_NAME_SUFFIX "")</li>
          <li>
          </li>
<li>set(ADDITIONAL_CMAKECACHE_OPTION "</li>
          <li>CMAKE_JOB_POOLS:STRING=compile=16;link=8</li>
          <li>CMAKE_JOB_POOL_COMPILE:STRING=compile</li>
          <li>CMAKE_JOB_POOL_LINK:STRING=link</li>
          <li>")</li>
          <li>
      </li>
</ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @Sam_Horvath (2022-01-11 21:09 UTC)

<p>I will work on fixing this in the dashboard scripts so that the build can resume correctly tomorrow</p>

---

## Post #11 by @Sam_Horvath (2022-01-11 21:21 UTC)

<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/DashboardScripts/commit/654644e8c5b43a9fae72abc29df5b9473e019b0d">
  <header class="source">

      <a href="https://github.com/Slicer/DashboardScripts/commit/654644e8c5b43a9fae72abc29df5b9473e019b0d" target="_blank" rel="noopener">github.com/Slicer/DashboardScripts</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/DashboardScripts/commit/654644e8c5b43a9fae72abc29df5b9473e019b0d" target="_blank" rel="noopener">Update ExtensionsIndex URL to use https: instead of git://</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2022-01-11" data-time="21:20:27" data-timezone="UTC">09:20PM - 11 Jan 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/sjh26" target="_blank" rel="noopener">
          <img alt="sjh26" src="https://avatars.githubusercontent.com/u/25040869?v=4" class="onebox-avatar-inline" width="20" height="20">
          sjh26
        </a>
      </div>

      <div class="lines" title="changed 7 files with 7 additions and 7 deletions">
        <a href="https://github.com/Slicer/DashboardScripts/commit/654644e8c5b43a9fae72abc29df5b9473e019b0d" target="_blank" rel="noopener">
          <span class="added">+7</span>
          <span class="removed">-7</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">- git:// has been removed as an authentication method</p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #12 by @Sam_Horvath (2022-01-12 14:33 UTC)

<p>Build looks good today, extensions should now be available for all platforms</p>

---
