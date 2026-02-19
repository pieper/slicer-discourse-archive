---
topic_id: 1104
title: "Cannot Compile Slicer On Mac Macos Sierra Clang 9 Cmake 3 9"
date: 2017-09-22
url: https://discourse.slicer.org/t/1104
---

# Cannot compile Slicer on Mac - macOS Sierra + clang 9 + cmake 3.9.1

**Topic ID**: 1104
**Date**: 2017-09-22
**URL**: https://discourse.slicer.org/t/cannot-compile-slicer-on-mac-macos-sierra-clang-9-cmake-3-9-1/1104

---

## Post #1 by @fedorov (2017-09-22 18:27 UTC)

<p>I recently had to reinstall the OS on my Mac, and since then I cannot compile Slicer due to this error:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8b6e55fffe81f63d670ee797775ab2caa1b2c5a.png" data-download-href="/uploads/short-url/zuegsIBSkJTXovmqbCDzvlgoZ6i.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8b6e55fffe81f63d670ee797775ab2caa1b2c5a.png" alt="image" data-base62-sha1="zuegsIBSkJTXovmqbCDzvlgoZ6i" width="690" height="211" data-dominant-color="0D0D0D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">794×243 24.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I installed Qt using the brew recipe, turned off TCL, and set deployment target to 10.11, following instructions <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Unix-like" class="inline-onebox">Documentation/Nightly/Developers/Build Instructions - Slicer Wiki</a>.</p>
<p>I also communicated with <a class="mention" href="/u/blowekamp">@blowekamp</a>, and he said:</p>
<blockquote>
<p>SimpleITK compiled with modern Apple Clang compiler requires either an old SDK ~10.6 for GNU’s stdlibc++, or required C++11 enabled. I am not sure how the defaults have changed recently for Slicer…</p>
</blockquote>
<p>Did anything relevant change recently in Slicer?</p>
<p>Here’s relevant system info:</p>
<pre><code class="lang-plaintext">$ cmake --version
cmake version 3.9.1

CMake suite maintained and supported by Kitware (kitware.com/cmake).

$ gcc -v
Configured with: --prefix=/Applications/Xcode.app/Contents/Developer/usr --with-gxx-include-dir=/usr/include/c++/4.2.1
Apple LLVM version 9.0.0 (clang-900.0.37)
Target: x86_64-apple-darwin16.7.0
Thread model: posix
InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin

$ qmake -v
QMake version 2.01a
Using Qt version 4.8.7 in /usr/local/lib
</code></pre>

---

## Post #2 by @blowekamp (2017-09-22 18:59 UTC)

<p>For this case with OS X 10.11 SDK, and clang C+11 should be enabled for SimpleITK. This should happen automatically. This should be indicated in the configuration file by the following entry in the SimpleITK’s CMakeCache.txt:</p>
<p>SITK_CHECK_CXX11:STRING=FALSE</p>
<p>note: FALSE indicates that -stdc++=11 is required</p>

---

## Post #3 by @fedorov (2017-09-22 19:22 UTC)

<p><a class="mention" href="/u/blowekamp">@blowekamp</a> I confirm I have that entry:</p>
<pre><code class="lang-nohighlight">$ grep SITK_CHECK_CXX11 CMakeCache.txt
SITK_CHECK_CXX11:INTERNAL=FALSE
</code></pre>
<p>But <a class="mention" href="/u/jcfr">@jcfr</a> confirmed recently c++11 is not currently supported in Slicer: <a href="https://discourse.slicer.org/t/transition-to-vtk-8-0/379/4">Transition to VTK 8.0</a></p>

---

## Post #4 by @jcfr (2017-09-22 19:22 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="1" data-topic="1104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Did anything relevant change recently in Slicer?</p>
</blockquote>
</aside>
<p>Based on comment of <a class="mention" href="/u/blowekamp">@blowekamp</a> <a href="https://github.com/SimpleITK/SimpleITK/issues/260#issuecomment-327180550">here</a>, starting with <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4/trunk/SuperBuild/External_SimpleITK.cmake?r1=26340&amp;r2=26339&amp;pathrev=26340">r26340</a> we now explicitly pass  <code>CMAKE_CXX_STANDARD</code>, <code>CMAKE_CXX_STANDARD_REQUIRED</code> and <code>CMAKE_CXX_EXTENSIONS</code> options.</p>
<p><a class="mention" href="/u/blowekamp">@blowekamp</a> Should we do things differently to support both C++98 and C++11 ?</p>

---

## Post #5 by @fedorov (2017-09-22 19:29 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="4" data-topic="1104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>we now explicitly pass  CMAKE_CXX_STANDARD</p>
</blockquote>
</aside>
<p>I confirm it is set to 98 in SimpleITK cache:</p>
<pre><code class="lang-plaintext">$ grep -r CXX_STANDARD CMakeCache.txt
CMakeCache.txt:CMAKE_CXX_STANDARD:STRING=98
CMakeCache.txt:CMAKE_CXX_STANDARD_REQUIRED:BOOL=ON
</code></pre>
<p>But as <a class="mention" href="/u/blowekamp">@blowekamp</a> said, C++11 is required.</p>
<p>Considering your comment in the above referenced thread (<a href="https://discourse.slicer.org/t/transition-to-vtk-8-0/379/4" class="inline-onebox">Transition to VTK 8.0 - #4 by jcfr</a>), I guess I am being forced to switch to VTKv8 <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"> I will try that next.</p>

---

## Post #6 by @fedorov (2017-09-22 19:33 UTC)

<p>If I switch to VTKv8, I get compile error in LibArchive <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=5" title=":frowning:" class="emoji" alt=":frowning:"></p>
<pre><code class="lang-nohighlight">[ 11%] Building C object libarchive/CMakeFiles/archive_static.dir/archive_read_disk_posix.c.o
/Users/fedorov/build/Slicer-Release/LibArchive/libarchive/archive_read_disk_posix.c:1984:6: error: 'futimens' is only available on macOS 10.13 or newer
      [-Werror,-Wunguarded-availability-new]
        if (futimens(fd, timespecs) == 0)
            ^~~~~~~~
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk/usr/include/sys/stat.h:373:5: note: 'futimens' has been explicitly marked partial here
int     futimens(int __fd, const struct timespec __times[2]) __API_AVAILABLE(macosx(10.13), ios(11.0), tvos(11.0), watchos(4.0));
        ^
/Users/fedorov/build/Slicer-Release/LibArchive/libarchive/archive_read_disk_posix.c:1984:6: note: enclose 'futimens' in a __builtin_available check to silence this warning
        if (futimens(fd, timespecs) == 0)
            ^~~~~~~~
1 error generated.
</code></pre>

---

## Post #7 by @blowekamp (2017-09-22 19:45 UTC)

<p>I am guessing that this patch:<br>
<a href="https://github.com/Slicer/Slicer/commit/fb11a9a147568e283ef25dd4555617ec399dfd2d#diff-109aeb3808fbb9cd5a014863e7556a16" class="onebox" target="_blank" rel="nofollow noopener">https://github.com/Slicer/Slicer/commit/fb11a9a147568e283ef25dd4555617ec399dfd2d#diff-109aeb3808fbb9cd5a014863e7556a16</a></p>
<p>Now for the  slicer superbuild, is <code>CMAKE_CXX_STANDARD:STRING=98</code> explicitly set or is in coming from the above patch when <code>CMAKE_CXX_STANDARD</code> is not defined and some kind of default is being set?</p>
<p>Currently SimpleITK just adds <code>--stdc++=11</code> to the CMAKE_CXX_FLAGS since it (previously) works with all version of CMake. But is appears the CMAKE_CXX_STANDARD variable are overriding it. Atleast in these try compiles.</p>

---

## Post #8 by @jcfr (2017-09-22 20:25 UTC)

<p>As a side note, failure to build SimpleITK using C++98 on recent macOS is already tracked in  <a href="https://issues.slicer.org/view.php?id=4434" class="inline-onebox">compatibility issue with osx · Issue #4434 · Slicer/Slicer · GitHub</a></p>
<blockquote>
<p>it appears the CMAKE_CXX_STANDARD variable are overriding it.</p>
</blockquote>
<p>Most likely, but I thought that using CMake &gt; 3.8.2 is used (see <a href="https://github.com/SimpleITK/SimpleITK/issues/260#issuecomment-327180550">here</a>)</p>
<blockquote>
<p>some kind of default is being set?</p>
</blockquote>
<p>Default are set in the toplevel CMakeLists.txt where we explicitly requires CMake &gt;3.8.2.</p>
<p><a href="https://github.com/Slicer/Slicer/blob/ac3a3faba26e9536ce58a5832d5bf67cabf2d93a/CMakeLists.txt#L7-L21" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/ac3a3faba26e9536ce58a5832d5bf67cabf2d93a/CMakeLists.txt#L7-L21</a></p>
<aside class="quote no-group" data-username="fedorov" data-post="6" data-topic="1104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>If I switch to VTKv8, I get compile error in LibArchive</p>
</blockquote>
</aside>
<p>This was reported by <a class="mention" href="/u/pieper">@pieper</a> and is tracked in <a href="https://issues.slicer.org/view.php?id=4438" class="inline-onebox">LibArchive: cannot build with deployment target 10.9 · Issue #4438 · Slicer/Slicer · GitHub</a></p>

---

## Post #9 by @blowekamp (2017-09-22 20:34 UTC)

<p>Friday after noon ramblings on this issue:</p>
<p>Further experimentation yields that if SimpleITK is configured with the CMAKE_CXX_STANDARD flags must not be null for CMAKE. Therefor I presume Slicers Superbuild is explicitly setting the standard. ( Why not c++03?)</p>
<p>I would consider not passing these CMAKE_CXX_STANDARD flags for this problematic case to SimpleITK. When on OS X, and the standard version is less that 11 and the OS X SDK is greater that 10.7? These flags should not be passed. This will enable SimpleITK to set the flag as need.</p>
<p>While SimpleITK could manipulate the CMAKE_CXX_STANARD flag for this case, because older cmake’s try_compile does not respect this option it would yield inconsistent and trouble prone behavior. There are a lot of factors that effect this situation… I’ll have to think about it further…</p>
<p>Compiling ITK with C++98 while compiling SimpleITK C++11, is not ideal, but all the tests seem to pass for the wrapping. The problem may be if SimpleITK C++ interface is used with this mixed standard configuration.</p>

---

## Post #10 by @jcfr (2017-09-22 20:45 UTC)

<blockquote>
<p>Compiling ITK with C++98 while compiling SimpleITK C++11, is not ideal, but all the tests seem to pass for the wrapping.</p>
</blockquote>
<p>I see</p>
<p>Thanks for the details answer. Things are now clearer.</p>
<p>Since c++11 is a hard requirement for SimpleITK. I will update Slicer build system to not pass the <code>CMAKE_CXX_STANDARD</code> related options if building with C++98 (aka Qt4). That way the builtin logic of SimpleITK will be used to initialize the flags and always use c+11 …</p>
<blockquote>
<p>Why not c++03?</p>
</blockquote>
<p>My understand is that c++98 matches the case where nothing was explicitly specified. And this seems to be a reasonable choice.</p>

---

## Post #11 by @blowekamp (2017-09-22 21:33 UTC)

<p>If using libc++ then C++11 is required.</p>

---

## Post #12 by @jcfr (2017-09-22 22:16 UTC)

<aside class="quote no-group" data-username="blowekamp" data-post="11" data-topic="1104" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/blowekamp/48/1386_2.png" class="avatar"> blowekamp:</div>
<blockquote>
<p>If using libc++ then C++11 is required.</p>
</blockquote>
</aside>
<p>Gotcha.</p>
<p>And this is the case when targeting macOS &gt; 10.9</p>

---

## Post #13 by @blowekamp (2017-09-25 20:03 UTC)

<p>Currently, Slicer is explicitly requesting C++98, and SimpleITK will not override that request even though it is not compatible in this configuration. I think that is reasonable behavior for SimpleITK when CMAKE_CXX_STANDARD(_REQUIRED is explicitly set, but for Slicer as a whole it does not work well.</p>
<aside class="quote no-group" data-username="jcfr" data-post="10" data-topic="1104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>My understand is that c++98 matches the case where nothing was explicitly specified. And this seems to be a reasonable choic</p>
</blockquote>
</aside>
<p>I <a href="https://stackoverflow.com/questions/21221411/when-will-gnu-c-support-c11-without-explicitly-asking-for-it" rel="noopener nofollow ugc">think</a> that the GCC compilers default to the GNU dialect, and GCC 6 version default to gnu++14. So these options selected are having an effect. While on MSVC there does not seem to be a way to specify the C++ standard, it is just evolving with the releases.</p>
<p>While the logic needed to determine if C++11 is needed for SimpleITK can easily be said as: “If using libc++ then C++11 is required”, or “SimpleITK requires C++98 with TR1 or C++11”, it is harder to detect this case in CMake because of the interdependency of the ways to set C++ version, the OS X Deployment Target, and the CXX command line flags ( -stdlib=, -std=). I do have a try compile which checks for libc++ without C++11:<a href="https://github.com/SimpleITK/SimpleITK/blob/next/CMake/sitk_check_cxx11_required.cxx#L4" rel="noopener nofollow ugc">https://github.com/SimpleITK/SimpleITK/blob/next/CMake/sitk_check_cxx11_required.cxx#L4</a></p>
<p>I have created a pull request that improves the situation in SimpleITK:</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/SimpleITK/SimpleITK/pull/302">
  <header class="source">

      <a href="https://github.com/SimpleITK/SimpleITK/pull/302" target="_blank" rel="noopener nofollow ugc">github.com/SimpleITK/SimpleITK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/SimpleITK/SimpleITK/pull/302" target="_blank" rel="noopener nofollow ugc">Fix c++11 flag detection</a>
      </h4>

    <div class="branches">
      <code>SimpleITK:next</code> ← <code>blowekamp:FixC++11FlagDetection</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2017-09-25" data-time="19:30:18" data-timezone="UTC">07:30PM - 25 Sep 17 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/blowekamp" target="_blank" rel="noopener nofollow ugc">
            <img alt="blowekamp" src="https://avatars.githubusercontent.com/u/321061?v=4" class="onebox-avatar-inline" width="20" height="20">
            blowekamp
          </a>
        </div>

        <div class="lines" title="5 commits changed 2 files with 57 additions and 21 deletions">
          <a href="https://github.com/SimpleITK/SimpleITK/pull/302/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+57</span>
            <span class="removed">-21</span>
          </a>
        </div>
      </div>
  </div>
</div>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It handles CMake CXX standard flags for older versions of CMake and gives better error messages when the C++ version is not able to be set as needed. For this case it would produce the following message:</p>
<blockquote>
<p>CMake Error at CMake/sitkCheckCXX11.cmake:110 (message):<br>
SimpleITK requires usage of C++11 or C++ Technical Report 1 (TR1), but were<br>
neither able to detect TR1 nor automatically enable C++11.  Please review<br>
your configuration settings and enable C++11.</p>
</blockquote>

---

## Post #14 by @fedorov (2017-09-25 22:11 UTC)

<p>Let me know if there is anything that I could try.</p>
<p>Meanwhile, I am compiling Slicer with SDK 10.13 and with SimpleITK disabled.</p>

---

## Post #15 by @jcfr (2017-09-25 23:31 UTC)

<p><a class="mention" href="/u/blowekamp">@blowekamp</a> It all makes sense, I just didn’t have a chance to get to this.</p>
<p>As soon as I finalize Slicer <a href="https://github.com/Slicer/Slicer/pull/796">PR#796</a> , most likely tonight, I will get to this.</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> Thanks for your patience</p>

---

## Post #16 by @blowekamp (2017-09-27 13:36 UTC)

<p>With the current state of things in Slicer with OS X, I believe the easiest way currently to get things to build with SimpleITK is to set <code>CMAKE_OSX_DEPLOYMENT_TARGET=10.8</code>.</p>

---

## Post #17 by @fedorov (2017-09-27 14:54 UTC)

<aside class="quote no-group" data-username="blowekamp" data-post="16" data-topic="1104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/blowekamp/48/1386_2.png" class="avatar"> blowekamp:</div>
<blockquote>
<p>the easiest way currently to get things to build with SimpleITK is to set CMAKE_OSX_DEPLOYMENT_TARGET=10.8</p>
</blockquote>
</aside>
<p>Not really - due to another issue, superbuild will fail in LibArchive with SDK earlier than 10.13: <a href="https://issues.slicer.org/view.php?id=4438" class="inline-onebox">LibArchive: cannot build with deployment target 10.9 · Issue #4438 · Slicer/Slicer · GitHub</a>. Just to save the time for anyone following this thread.</p>

---

## Post #18 by @jcfr (2017-09-29 15:52 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> The LibArchive issue should be addressed in</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/801" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/801" target="_blank">Scalar bar visualization</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:32:14" data-timezone="UTC">10:32PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:32:15" data-timezone="UTC">10:32PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank">
          <img alt="slicerbot" src="https://avatars3.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">This issue was created automatically from an original Mantis Issue. Further discussion may take place here.</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Thanks for <a class="mention" href="/u/ihnorton">@ihnorton</a> for suggesting the update.</p>

---

## Post #19 by @fedorov (2017-10-02 14:42 UTC)

<p>Thank you JC! I confirm LibArchive can now be compiled on SDK 10.13. I disabled SimpleITK and will report if the overall build is successful.</p>

---

## Post #20 by @jcfr (2017-10-02 14:44 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="19" data-topic="1104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I disabled SimpleITK and will report if the overall build is successful.</p>
</blockquote>
</aside>
<p>Sounds good. The SimpleITK build issue will be addressed this week.</p>

---

## Post #21 by @fedorov (2017-10-02 17:40 UTC)

<p>I confirm - build succeeded.</p>

---

## Post #22 by @jcfr (2017-10-03 04:29 UTC)

<p>SimpleITK build should be fixed by <a href="https://github.com/Slicer/Slicer/pull/802">https://github.com/Slicer/Slicer/pull/802</a></p>
<p><a class="mention" href="/u/blowekamp">@blowekamp</a> Let me know what you think</p>

---
