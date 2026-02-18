# 3D Slicer Release Build Error (Variable Slicer_WC_LAST_CHANGED_DATE is expected to be defined in SlicerPackageAndUploadTarget)

**Topic ID**: 20984
**Date**: 2021-12-09
**URL**: https://discourse.slicer.org/t/3d-slicer-release-build-error-variable-slicer-wc-last-changed-date-is-expected-to-be-defined-in-slicerpackageanduploadtarget/20984

---

## Post #1 by @mertsaner (2021-12-09 21:24 UTC)

<p>Hello,</p>
<p>When I build Slicer in my Windows 11 Intel laptop using the following instructions as stated in Slicer website the I got the following error,<br>
Instructions:</p>
<pre><code class="lang-auto">mkdir C:\D\S4R
cd /d C:\D\S4R
"C:\Program Files\CMake\bin\cmake.exe" -G "Visual Studio 16 2019" -A x64 -DQt5_DIR:PATH=C:\Qt\5.15.2\msvc2019_64\lib\cmake\Qt5 C:\D\S4
"C:\Program Files\CMake\bin\cmake.exe" --build . --config Release
</code></pre>
<p>The error is not immediate and it showed after four hours of building.<br>
Thanks for any help.</p>
<p>ERROR:</p>
<pre><code class="lang-auto">CMake/LastConfigureStep/CMakeLists.txt:41 (include)
  This warning is for project developers.  Use -Wno-dev to suppress it.

  CMake Error at CMake/SlicerPackageAndUploadTarget.cmake:118 (message):
    Variable Slicer_WC_LAST_CHANGED_DATE is expected to be defined.
  Call Stack (most recent call first):
    CMake/LastConfigureStep/CMakeLists.txt:41 (include)


  -- Configuring incomplete, errors occurred!
  See also "C:/Users/merts/Slicer-build/CMakeFiles/CMakeOutput.log".
  See also "C:/Users/merts/Slicer-build/CMakeFiles/CMakeError.log".
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Micro
soft\VC\v160\Microsoft.CppCommon.targets(241,5): error MSB8066: Custom buil
d for 'C:\Users\merts\CMakeFiles\64875fd35109041c8e0baea88f0c3fbf\Slicer-mk
dir.rule;C:\Users\merts\CMakeFiles\64875fd35109041c8e0baea88f0c3fbf\Slicer-
download.rule;C:\Users\merts\CMakeFiles\64875fd35109041c8e0baea88f0c3fbf\Sl
icer-update.rule;C:\Users\merts\CMakeFiles\64875fd35109041c8e0baea88f0c3fbf
\Slicer-patch.rule;C:\Users\merts\CMakeFiles\64875fd35109041c8e0baea88f0c3f
bf\Slicer-configure.rule;C:\Users\merts\CMakeFiles\64875fd35109041c8e0baea8
8f0c3fbf\Slicer-build.rule;C:\Users\merts\CMakeFiles\64875fd35109041c8e0bae
a88f0c3fbf\Slicer-forceconfigure.rule;C:\Users\merts\CMakeFiles\64875fd3510
9041c8e0baea88f0c3fbf\Slicer-install.rule;C:\Users\merts\CMakeFiles\6a457aa
83091fe4a6245d53ff14120bf\Slicer-complete.rule;C:\Users\merts\CMakeFiles\2e
18417901a880d0571e033b5beb779a\Slicer.rule;C:\D\S4\CMakeLists.txt' exited w
ith code 1. [C:\Users\merts\Slicer.vcxproj]
</code></pre>

---

## Post #2 by @jcfr (2021-12-09 21:46 UTC)

<p>Thanks for report <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=15" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>Here are few questions to help understand what is happening.</p>
<h3><a name="p-70953-questions-1" class="anchor" href="#p-70953-questions-1" aria-label="Heading link"></a>Questions</h3>
<p>Which version of Slicer source are you building against ?</p>
<p>Which version of CMake are you using ?</p>
<p>And what is the output of the following commands executed in the Slicer source tree:</p>
<pre><code class="lang-auto">$ git rev-parse --verify -q --short=7 HEAD
30d8416

$ git show -s --format=%ci 30d8416
2021-12-09 14:36:22 -0500
</code></pre>
<p>What is the output associated with the <code>Regular Expression Explorer</code> provided by the <code>cmake-gui.exe</code> corresponding to your version of CMake ?  (Tools → Regular Expression Explorer)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23e52f247a61515e7d6e568e4e1854e4fb5fd40c.png" data-download-href="/uploads/short-url/57xJE7o7RhWaKdxzajXJgpaxcEQ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23e52f247a61515e7d6e568e4e1854e4fb5fd40c_2_547x500.png" alt="image" data-base62-sha1="57xJE7o7RhWaKdxzajXJgpaxcEQ" width="547" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23e52f247a61515e7d6e568e4e1854e4fb5fd40c_2_547x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23e52f247a61515e7d6e568e4e1854e4fb5fd40c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23e52f247a61515e7d6e568e4e1854e4fb5fd40c.png 2x" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">631×576 21.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3><a name="p-70953-possible-source-of-the-regression-2" class="anchor" href="#p-70953-possible-source-of-the-regression-2" aria-label="Heading link"></a>Possible source of the regression</h3>
<p>Regression could have been introduced in the following commit:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/bfc1310f831c40089e575ce03184ab7a8a40201e">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/bfc1310f831c40089e575ce03184ab7a8a40201e" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/bfc1310f831c40089e575ce03184ab7a8a40201e" target="_blank" rel="noopener">ENH: FindGit: Update extraction of WC_LAST_CHANGED_DATE to include time</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2021-06-24" data-time="16:40:48" data-timezone="UTC">04:40PM - 24 Jun 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="changed 1 files with 1 additions and 1 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/bfc1310f831c40089e575ce03184ab7a8a40201e" target="_blank" rel="noopener">
          <span class="added">+1</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This commit improves feature originally introduced in b2b9f44f2 (ENH:
GIT_WC_INF<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/bfc1310f831c40089e575ce03184ab7a8a40201e" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">O with date support for git only repository)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<h3><a name="p-70953-background-3" class="anchor" href="#p-70953-background-3" aria-label="Heading link"></a>Background</h3>
<p>The relevant code is here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/30ad5f592c4ecfd45608af2edafd4029c366afa3/CMake/SlicerPackageAndUploadTarget.cmake#L103-L119">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/30ad5f592c4ecfd45608af2edafd4029c366afa3/CMake/SlicerPackageAndUploadTarget.cmake#L103-L119" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/30ad5f592c4ecfd45608af2edafd4029c366afa3/CMake/SlicerPackageAndUploadTarget.cmake#L103-L119" target="_blank" rel="noopener">CMake/SlicerPackageAndUploadTarget.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/30ad5f592c4ecfd45608af2edafd4029c366afa3/CMake/SlicerPackageAndUploadTarget.cmake#L103-L119" rel="noopener"><code>30ad5f592</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="103" style="counter-reset: li-counter 102 ;">
          <li># Get working copy information</li>
          <li>include(SlicerMacroExtractRepositoryInfo)</li>
          <li>SlicerMacroExtractRepositoryInfo(VAR_PREFIX Slicer SOURCE_DIR ${Slicer_SOURCE_DIR})</li>
          <li></li>
          <li>set(script_arg_list)</li>
          <li>foreach(varname</li>
          <li>  ${script_vars}</li>
          <li>  # Optional variables</li>
          <li>  CTEST_MODEL</li>
          <li>  # Variables set by SlicerMacroExtractRepositoryInfo</li>
          <li>  Slicer_REVISION</li>
          <li>  Slicer_WC_LAST_CHANGED_DATE</li>
          <li>  Slicer_WC_URL</li>
          <li>  )</li>
          <li>  if(NOT DEFINED ${varname})</li>
          <li>    message(FATAL_ERROR "Variable ${varname} is expected to be defined.")</li>
          <li>  endif()</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It then uses the CMake module <code>SlicerMacroExtractRepositoryInfo.cmake</code></p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/30ad5f592c4ecfd45608af2edafd4029c366afa3/CMake/SlicerMacroExtractRepositoryInfo.cmake#L79-L91">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/30ad5f592c4ecfd45608af2edafd4029c366afa3/CMake/SlicerMacroExtractRepositoryInfo.cmake#L79-L91" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/30ad5f592c4ecfd45608af2edafd4029c366afa3/CMake/SlicerMacroExtractRepositoryInfo.cmake#L79-L91" target="_blank" rel="noopener">CMake/SlicerMacroExtractRepositoryInfo.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/30ad5f592c4ecfd45608af2edafd4029c366afa3/CMake/SlicerMacroExtractRepositoryInfo.cmake#L79-L91" rel="noopener"><code>30ad5f592</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="79" style="counter-reset: li-counter 78 ;">
          <li>find_package(Git REQUIRED)</li>
          <li></li>
          <li># Is &lt;SOURCE_DIR&gt; a git working copy ?</li>
          <li>execute_process(COMMAND ${GIT_EXECUTABLE} rev-list -n 1 HEAD</li>
          <li>  WORKING_DIRECTORY ${MY_SOURCE_DIR}</li>
          <li>  RESULT_VARIABLE GIT_result</li>
          <li>  OUTPUT_QUIET</li>
          <li>  ERROR_QUIET)</li>
          <li></li>
          <li>if(${GIT_result} EQUAL 0)</li>
          <li></li>
          <li>  set(${wc_info_prefix}_WC_TYPE git)</li>
          <li>  GIT_WC_INFO(${MY_SOURCE_DIR} ${wc_info_prefix})</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>and uses the CMake function <code>GIT_WC_INFO</code> provided by <code>FindGit.cmake</code> and ultimately run the following to extract the date:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/30ad5f592c4ecfd45608af2edafd4029c366afa3/CMake/FindGit.cmake#L118-L123">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/30ad5f592c4ecfd45608af2edafd4029c366afa3/CMake/FindGit.cmake#L118-L123" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/30ad5f592c4ecfd45608af2edafd4029c366afa3/CMake/FindGit.cmake#L118-L123" target="_blank" rel="noopener">CMake/FindGit.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/30ad5f592c4ecfd45608af2edafd4029c366afa3/CMake/FindGit.cmake#L118-L123" rel="noopener"><code>30ad5f592</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="118" style="counter-reset: li-counter 117 ;">
          <li>execute_process(COMMAND ${GIT_EXECUTABLE} show -s --format=%ci ${${prefix}_WC_REVISION_HASH}</li>
          <li>   WORKING_DIRECTORY ${dir}</li>
          <li>   OUTPUT_VARIABLE ${prefix}_show_output</li>
          <li>   OUTPUT_STRIP_TRAILING_WHITESPACE)</li>
          <li>string(REGEX REPLACE "^([0-9][0-9][0-9][0-9]\\-[0-9][0-9]\\-[0-9][0-9] [0-9][0-9]:[0-9][0-9]:[0-9][0-9] [-+][0-9][0-9][0-9][0-9]).*"</li>
          <li>  "\\1" ${prefix}_WC_LAST_CHANGED_DATE "${${prefix}_show_output}")</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @mertsaner (2021-12-11 12:54 UTC)

<p>Hello,<br>
I am using Slicer 4.11.20210226, and CMake 3.22.1<br>
When you mean slicer source tree which place do mean exactly?</p>
<p>In CMake GUI, I see empty screen in the Tools/Regular Expression Explorer, you can see my screen in the below.</p>
<p>Regarding Links you provided, how are they related with the issue I experience?</p>
<p>Thank you,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3adb3b4a924707b14ae1aa582f2b49783cde0a5.png" data-download-href="/uploads/short-url/nlXYUx8Tlsa0ZItbq10P1dg5D0h.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3adb3b4a924707b14ae1aa582f2b49783cde0a5.png" alt="1" data-base62-sha1="nlXYUx8Tlsa0ZItbq10P1dg5D0h" width="541" height="500" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">717×662 19.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2021-12-11 15:45 UTC)

<p>Slicer needs to extract date and time from the git log during build. Your build fails because this date&amp;time is in an unexpected format, most likely due to your regional settings (how date&amp;time is formatted). That’s why <a class="mention" href="/u/jcfr">@jcfr</a> asked to get the an example of a printout of the date from git, and then testing that in CMake’s regular expression explorer. The window is expected to be empty and you copy the content there.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> can you copy the regular expression that needs to be tested? (it would be error-prone to copy it from the screenshot)</p>

---

## Post #5 by @mertsaner (2021-12-12 23:30 UTC)

<p>I have changed date&amp;time settings and rerun the build in debug mode this time, and issue persist.</p>
<p>Error Code:</p>
<pre><code class="lang-auto"> -- Setting 'CTEST_MODEL' variable with default value 'Experimental'
  -- Setting 'SLICER_PACKAGE_MANAGER_CLIENT_EXECUTABLE' variable with default value 'SLICER_PACKAGE_MANAGER_CLIENT_EXEC
  UTABLE-NOTDEFINED'
  -- Setting 'SLICER_PACKAGE_MANAGER_URL' variable with default value 'SLICER_PACKAGE_MANAGER_URL-NOTDEFINED'
  CMake Warning (dev) at CMake/SlicerMacroExtractRepositoryInfo.cmake:75 (message):
    Skipping repository info extraction: directory [C:/D/S4] is not a GIT or
    SVN checkout
  Call Stack (most recent call first):
    CMake/SlicerPackageAndUploadTarget.cmake:105 (SlicerMacroExtractRepositoryInfo)
    CMake/LastConfigureStep/CMakeLists.txt:41 (include)
  This warning is for project developers.  Use -Wno-dev to suppress it.

  CMake Error at CMake/SlicerPackageAndUploadTarget.cmake:118 (message):
    Variable Slicer_WC_LAST_CHANGED_DATE is expected to be defined.
  Call Stack (most recent call first):
    CMake/LastConfigureStep/CMakeLists.txt:41 (include)


  -- Setting 'SLICER_PACKAGE_MANAGER_API_KEY' variable with default value 'OBFUSCATED'
  -- Configuring incomplete, errors occurred!
  See also "C:/Users/merts/Slicer-build/CMakeFiles/CMakeOutput.log".
  See also "C:/Users/merts/Slicer-build/CMakeFiles/CMakeError.log".
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(241
,5): error MSB8066: Custom build for 'C:\Users\merts\CMakeFiles\64875fd35109041c8e0baea88f0c3fbf\Slicer-mkdir.rule;C:\U
sers\merts\CMakeFiles\64875fd35109041c8e0baea88f0c3fbf\Slicer-download.rule;C:\Users\merts\CMakeFiles\64875fd35109041c8
e0baea88f0c3fbf\Slicer-update.rule;C:\Users\merts\CMakeFiles\64875fd35109041c8e0baea88f0c3fbf\Slicer-patch.rule;C:\User
s\merts\CMakeFiles\64875fd35109041c8e0baea88f0c3fbf\Slicer-configure.rule;C:\Users\merts\CMakeFiles\64875fd35109041c8e0
baea88f0c3fbf\Slicer-build.rule;C:\Users\merts\CMakeFiles\64875fd35109041c8e0baea88f0c3fbf\Slicer-forceconfigure.rule;C
:\Users\merts\CMakeFiles\64875fd35109041c8e0baea88f0c3fbf\Slicer-install.rule;C:\Users\merts\CMakeFiles\6a457aa83091fe4
a6245d53ff14120bf\Slicer-complete.rule;C:\Users\merts\CMakeFiles\2e18417901a880d0571e033b5beb779a\Slicer.rule;C:\D\S4\C
MakeLists.txt' exited with code 1. [C:\Users\merts\Slicer.vcxproj]
</code></pre>

---

## Post #6 by @jamesobutler (2021-12-12 23:46 UTC)

<aside class="quote no-group" data-username="mertsaner" data-post="5" data-topic="20984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mertsaner/48/13445_2.png" class="avatar"> mertsaner:</div>
<blockquote>
<p>C:/Users/merts/Slicer-build/</p>
</blockquote>
</aside>
<p>Are you following the example of the build instructions for the location on the Slicer build folder? Are you using “C:/S4R” or “C:/Users/merts/Slicer-build/”? A longer initial build directory could lead to downstream issues.</p>

---

## Post #7 by @jcfr (2021-12-13 16:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="20984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>can you copy the regular expression that needs to be tested?</p>
</blockquote>
</aside>
<pre><code class="lang-auto">^([0-9][0-9][0-9][0-9]\\-[0-9][0-9]\\-[0-9][0-9] [0-9][0-9]:[0-9][0-9]:[0-9][0-9] [-+][0-9][0-9][0-9][0-9]).*
</code></pre>
<p><em>Copied from <a href="https://github.com/Slicer/Slicer/blob/30ad5f592c4ecfd45608af2edafd4029c366afa3/CMake/FindGit.cmake#L118-L123">Slicer/CMake/FindGit.cmake#L118-L123</a></em></p>

---

## Post #8 by @mertsaner (2021-12-13 18:45 UTC)

<p>Yes, I follow the instructions there and I use C:\D\S4D to build debug release</p>

---

## Post #9 by @mertsaner (2021-12-13 18:48 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f400c93181df42f579f5928ee416b5bbe042ab4c.png" data-download-href="/uploads/short-url/yOybzhqeRHSZohWkb1Ja2dd6dzu.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f400c93181df42f579f5928ee416b5bbe042ab4c_2_540x500.png" alt="2" data-base62-sha1="yOybzhqeRHSZohWkb1Ja2dd6dzu" width="540" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f400c93181df42f579f5928ee416b5bbe042ab4c_2_540x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f400c93181df42f579f5928ee416b5bbe042ab4c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f400c93181df42f579f5928ee416b5bbe042ab4c.png 2x" data-dominant-color="F3F3F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">726×671 24.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @mertsaner (2021-12-13 18:51 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49e7936a98e30d42f7dd62941a75b2b747b7fe14.png" data-download-href="/uploads/short-url/axN0gxyc3VUWRRJsOLX0ztdY0kI.png?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49e7936a98e30d42f7dd62941a75b2b747b7fe14.png" alt="3" data-base62-sha1="axN0gxyc3VUWRRJsOLX0ztdY0kI" width="538" height="500" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">722×671 24.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @jamesobutler (2021-12-13 20:36 UTC)

<p>I’m just noticing from your screenshots that your “where to build the binaries” is “C:/users/merts/Documents/Slicer_built” which doesn’t seem to match with “C:/D/S4D”. It’s indicating your build is going into your user location instead.</p>

---

## Post #12 by @wang_yali (2021-12-17 12:29 UTC)

<p>same error.<br>
I have solved this problem now. I am using Slicer 4.13, CMake 3.21.4, VS2019.</p>

---

## Post #13 by @mertsaner (2021-12-20 13:31 UTC)

<p><a class="mention" href="/u/wang_yali">@wang_yali</a> Could you explain how did you solve the problem?</p>

---

## Post #14 by @wang_yali (2021-12-21 04:23 UTC)

<p>The solution is as follows:</p>
<ol>
<li>We change the variables _WC_LAST_CHANGED_DATE in FindGit.cmake file back to version 4.11</li>
</ol>
<p>from<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/105edfe1523adc31268d9e5bb86d7df9fa640539.png" data-download-href="/uploads/short-url/2kOUfyRwrnIk1EdlCvdnaJ9SBPb.png?dl=1" title="fb2196c03635de9e98e600c09eb628b" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/105edfe1523adc31268d9e5bb86d7df9fa640539_2_690x29.png" alt="fb2196c03635de9e98e600c09eb628b" data-base62-sha1="2kOUfyRwrnIk1EdlCvdnaJ9SBPb" width="690" height="29" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/105edfe1523adc31268d9e5bb86d7df9fa640539_2_690x29.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/105edfe1523adc31268d9e5bb86d7df9fa640539_2_1035x43.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/105edfe1523adc31268d9e5bb86d7df9fa640539.png 2x" data-dominant-color="F6F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fb2196c03635de9e98e600c09eb628b</span><span class="informations">1111×48 25.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
to<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eae55210e27e324436699eeca35f74326e5f3dea.png" data-download-href="/uploads/short-url/xvZ2NwhMe9RKwsCAxNOrQr8kCKK.png?dl=1" title="0eabfffa9dbf40a8f0da7f723e339d4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eae55210e27e324436699eeca35f74326e5f3dea.png" alt="0eabfffa9dbf40a8f0da7f723e339d4" data-base62-sha1="xvZ2NwhMe9RKwsCAxNOrQr8kCKK" width="690" height="58" data-dominant-color="F4F3F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">0eabfffa9dbf40a8f0da7f723e339d4</span><span class="informations">712×60 3.57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
2. Open the <strong>SlicerMacroExtractRepositoryInfo.cmake</strong><br>
add   set(${wc_info_prefix}_WC_LAST_CHANGED_DATE “0000-00-00”) in the file just like the 4.11v.</p>

---

## Post #15 by @jcfr (2021-12-21 06:06 UTC)

<p><a class="mention" href="/u/mertsaner">@mertsaner</a> <a class="mention" href="/u/wang_yali">@wang_yali</a> Could you both run the following commands in your Slicer source tree ?</p>
<p><strong>Rational:</strong> With these results we will be able to update the build-system to properly work without having to do any manual replacement.</p>
<h3><a name="p-71594-commands-to-execute-1" class="anchor" href="#p-71594-commands-to-execute-1" aria-label="Heading link"></a>Commands to execute</h3>
<p>Command 1:</p>
<pre><code class="lang-auto">git rev-parse --verify -q --short=7 HEAD
</code></pre>
<p>Command 2:</p>
<pre><code class="lang-auto">git show -s --format=%ci &lt;output-of-command-1&gt;
</code></pre>
<p>Command 3:</p>
<pre><code class="lang-auto">git --version
</code></pre>
<h3><a name="p-71594-example-of-output-2" class="anchor" href="#p-71594-example-of-output-2" aria-label="Heading link"></a>Example of output</h3>
<p>To illustrate, here is what I get:</p>
<pre><code class="lang-auto">$ git rev-parse --verify -q --short=7 HEAD
fff83f9

$ git show -s --format=%ci fff83f9
2021-12-17 13:11:21 -0500

$ git --version
git version 2.22.0
</code></pre>

---

## Post #16 by @mertsaner (2021-12-21 12:49 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>Here is what I get:</p>
<pre><code class="lang-auto">PS C:\D\S4&gt; git rev-parse --verify -q --short=7 HEAD
8eaa925
PS C:\D\S4&gt; git show -s --format=%ci &lt;output-of-command-1&gt;
At line:1 char:26
+ git show -s --format=%ci &lt;output-of-command-1&gt;
+                          ~
The '&lt;' operator is reserved for future use.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : RedirectionNotSupported

PS C:\D\S4&gt; git --version
git version 2.34.1.windows.1
PS C:\D\S4&gt;
</code></pre>

---

## Post #17 by @mertsaner (2021-12-21 12:50 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> Second one does not work and gives an error</p>

---

## Post #18 by @mertsaner (2021-12-21 12:51 UTC)

<p>I did not find any file named FindGit.cmake , Where is it?<br>
Could you also copy the content that I need to change instead picture?</p>

---

## Post #19 by @wang_yali (2021-12-21 13:53 UTC)

<p>Here ，source folder.<br>
“D:\D\S4\CMake\FindGit.cmake”<br>
“D:\D\S4\CMake\SlicerMacroExtractRepositoryInfo.cmake”</p>

---

## Post #20 by @wang_yali (2021-12-21 14:17 UTC)

<p>$ git rev-parse --verify -q --short=7 HEAD<br>
d8492ca</p>
<p>$ git show -s --format=%ci d8492ca<br>
2021-12-21 22:15:05 +0800</p>
<p>$ git --version<br>
git version 2.34.1.windows.1</p>

---

## Post #21 by @mertsaner (2021-12-22 23:25 UTC)

<p>Hi,<br>
I receive this error when I try to build extensions using Cmake.</p>
<p>– Found Git: C:/Program Files/Git/cmd/git.exe<br>
– Looking for decorator header qSlicerOHModuleModuleWidgetsPythonQtDecorators.h<br>
– Looking for decorator header qSlicerOHModuleModuleWidgetsPythonQtDecorators.h - Not found<br>
– Configuring Loadable module: OHModule [qSlicerOHModuleModuleExport.h]<br>
CMake Warning (dev) at C:/D/S4/CMake/SlicerMacroExtractRepositoryInfo.cmake:75 (message):<br>
Skipping repository info extraction: directory [C:/dev/OHExtension/OH] is<br>
not a GIT or SVN checkout<br>
Call Stack (most recent call first):<br>
C:/D/S4/CMake/SlicerExtensionCPack.cmake:60 (SlicerMacroExtractRepositoryInfo)<br>
CMakeLists.txt:27 (include)<br>
This warning is for project developers.  Use -Wno-dev to suppress it.</p>
<p>CMake Error at C:/D/S4/Extensions/CMake/SlicerFunctionGenerateExtensionDescription.cmake:70 (message):<br>
CMake variable EXTENSION_WC_REVISION is empty !<br>
Call Stack (most recent call first):<br>
C:/D/S4/CMake/SlicerExtensionCPack.cmake:79 (slicerFunctionGenerateExtensionDescription)<br>
CMakeLists.txt:27 (include)</p>
<p>– Configuring incomplete, errors occurred!<br>
See also “C:/dev/OHExtension/OHBuild/CMakeFiles/CMakeOutput.log”.<br>
See also “C:/dev/OHExtension/OHBuild/CMakeFiles/CMakeError.log”.</p>

---

## Post #22 by @lassoan (2021-12-23 16:13 UTC)

<p>I moved this issue here seeing that it is still the issue with extracting revision of the working copy. However, it might be a slightly different issue. How did you create the <code>C:/dev/OHExtension/OH</code> folder  folder? What revision control do you use for developing the extension?</p>

---

## Post #23 by @lassoan (2021-12-23 16:34 UTC)

<p>If you are not using revision control then you can specify working copy version CMake variables manually when you configure your project, either using the CMake GUI or by adding these arguments when you call cmake.exe:</p>
<pre><code>-DYourExtensionName_WC_REVISION:STRING=100 -DEXTENSION_WC_REVISION:STRING=100
</code></pre>
<p>(replace <code>YourExtensionName</code> and <code>100</code> with the actual name of your extension and a revision number)</p>

---

## Post #24 by @huwqchn (2024-07-16 07:58 UTC)

<p>also <code>C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(254,5): error MSB8066: “D:\T\R\CMakeFiles\44934091396c3b054b003113a65e021b\Slicer-configure.rule;D:\T\R\CMakeFiles\44934091396c3b054b003113a65e021b\Slicer-build.rule;D:\T\R\CMakeFiles\44934091396c3b054b003113a65e021b\Slicer-forceconfigure.rule;D:\T\R\CMakeFiles\44934091396c3b054b003113a65e021b\Slicer-install.rule;D:\T\R\CMakeFiles\8d7bfc65e5c95651d8140dc57a2140ef\Slicer-complete.rule;D:\T\R\CMakeFiles\2b07ec81edd0d1d54d3567e2f1beb78f\Slicer.rule” exited with code 1。</code></p>

---

## Post #25 by @ferhue (2025-01-29 10:41 UTC)

<p>See also <a href="https://discourse.slicer.org/t/variable-slicer-wc-last-changed-date-is-expected-to-be-defined/25389/10" class="inline-onebox">Variable Slicer_WC_LAST_CHANGED_DATE is expected to be defined - #10 by ferhue</a></p>

---
