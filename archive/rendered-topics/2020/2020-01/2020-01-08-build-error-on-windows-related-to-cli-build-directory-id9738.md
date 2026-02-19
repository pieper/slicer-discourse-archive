---
topic_id: 9738
title: "Build Error On Windows Related To Cli Build Directory"
date: 2020-01-08
url: https://discourse.slicer.org/t/9738
---

# Build error on Windows related to CLI build directory

**Topic ID**: 9738
**Date**: 2020-01-08
**URL**: https://discourse.slicer.org/t/build-error-on-windows-related-to-cli-build-directory/9738

---

## Post #1 by @cpinter (2020-01-08 09:25 UTC)

<p>Hi all,<br>
I have done four Slicer builds recently, and all four had the same issue: the CLI directory was not created:</p>
<pre><code>"c:\d\S4D\ALL_BUILD.vcxproj" (default target) (1) -&gt;
"C:\d\S4D\Slicer.vcxproj" (default target) (33) -&gt;
(CustomBuild target) -&gt;
  CUSTOMBUILD : error : Target (for copy_if_different command) "C:/d/S4D/Slicer-build/lib/Slicer-4.11/cli-modules/Debug" is not a directory. [C:\d\S4D\Slicer-b
uild\Base\QTCLI\Testing\InstallPyCLITest4.vcxproj] [C:\d\S4D\Slicer.vcxproj]
</code></pre>
<p>After I created the folder manually, the build succeeded. The latest revision I tried was this one<br>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/commit/c353d7cc622f1e0f85d7a0b255dae20a1ba588b3" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/c353d7cc622f1e0f85d7a0b255dae20a1ba588b3" target="_blank">BUG:  Prevent CLISerializationTest.py from modifying source tree</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2020-01-07" data-time="15:51:41" data-timezone="UTC">03:51PM - 07 Jan 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/sjh26" target="_blank">
          <img alt="sjh26" src="https://avatars2.githubusercontent.com/u/25040869?v=4" class="onebox-avatar-inline" width="20" height="20">
          sjh26
        </a>
        
      </div>

      <div class="lines" title="changed 1 files with 10 additions and 4 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/c353d7cc622f1e0f85d7a0b255dae20a1ba588b3" target="_blank">
          <span class="added">+10</span>
          <span class="removed">-4</span>
        </a>
      </div>
    </div>

  </div>
</div>


  <div class="github-row">
    <pre class="github-content" style="white-space: normal;">svn-url: http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28715
git-svn-id: http://svn.slicer.org/Slicer4/trunk@28715 3bd1e089-480b-0410-8dfb-8563597acbee</pre>
  </div>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>and the only commit that happened since then is certainly unrelated, so I thought I’d ask about this.</p>
<p>I see that <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>’s windows build on the factory succeeded, however, with <a href="http://slicer.cdash.org/buildSummary.php?buildid=1794380">VS2017 and Qt 5.12.6</a>. I use VS2019 with 2015 toolset and Qt 5.10.1.</p>
<p>Has anyone encountered this issue?<br>
Thanks!</p>

---

## Post #2 by @jamesobutler (2020-01-08 11:37 UTC)

<p>Yes others have run into this issue including myself though not sure what is the cause. I had also used VS 2019 with 2015 toolset and Qt 5.10.1 when it happened.</p>
<p>See this recent post</p><aside class="quote quote-modified" data-post="1" data-topic="9644">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/harajyoti_das/48/5529_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/not-all-modules-are-enabled-after-build/9644">Not all modules are enabled after build</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hi, I have build the 3d slicer following the instructions given in the document. I am getting the following error: 
CUSTOMBUILD : error : Target (for copy_if_different command) “C:/D/D/Slicer-build/lib/Slicer-4.11/cli-modules/Debug” is not a directory. [C:\D\D\Slicer-build\Base\QTCLI\Testing\InstallPyCLITest4.vcxproj] 
This is what I get when I launch the slicer.exe 
qt.network.ssl: QSslSocket: cannot resolve SSL_set_alpn_protos 
qt.network.ssl: QSslSocket: cannot resolve SSL_CTX_set_alpn_select…
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2020-01-08 13:58 UTC)

<p>Maybe parallel build mechanism or default settings have changed in Visual Studio (or maybe CMake?) recently. Have you updated to Visual Studio or CMake recently? I don’t have any issues with Visual Studio 16.4.2 (menu: Help / Check for updates) and CMake 3.14.3.</p>

---

## Post #4 by @Sam_Horvath (2020-01-08 14:56 UTC)

<p>Are you changing any of the default slicer options?  We have had similar issues in the past, since we only build/test a single options set, where enabling/disabling something causes odd errors; ex.<br>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/commit/d299d1527583f5e3b07bbd2838d84b0ce13323a3" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/d299d1527583f5e3b07bbd2838d84b0ce13323a3" target="_blank" rel="nofollow noopener">COMP: Ensure designer launcher directory exists at configuration time</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2019-08-12" data-time="17:45:05" data-timezone="UTC">05:45PM - 12 Aug 19 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="nofollow noopener">
          <img alt="jcfr" src="https://avatars0.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
        
      </div>

      <div class="lines" title="changed 1 files with 3 additions and 0 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/d299d1527583f5e3b07bbd2838d84b0ce13323a3" target="_blank" rel="nofollow noopener">
          <span class="added">+3</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>

  </div>
</div>


  <div class="github-row">
    <pre class="github-content" style="white-space: normal;">This commit fixes the following error reported when configuring the SlicerSALT
custom application:
 CMake Error at /work/Stable/SSALT-200-build/CTKAPPLAUNCHER/CMake/ctkAppLauncher.cmake:278 (message):
 DESTINATION_DIR [/work/Stable/SSALT-200-build/Slicer-build/bin] doesn't
 seem...</pre>
  </div>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #5 by @cpinter (2020-01-08 17:26 UTC)

<p>Thanks for the answers!</p>
<p>I also use Visual Studio 16.4.2 but with CMake 3.16.2.</p>
<p>Regarding CMake options, I always have -DSlicer_USE_PYTHONQT_WITH_OPENSSL:BOOL=ON, and tried with and without SimpleITK. I built Slicer in itself, and as part of custom app as well.<br>
I only tried this on one computer so far, but I’ll try on more and get back with what I found.</p>

---

## Post #6 by @lassoan (2020-01-08 21:40 UTC)

<p>I started a build with CMake 3.16.2 and it failed:</p>
<pre><code>CUSTOMBUILD : error : Target (for copy_if_different command) "D:/D/S4R3/Slicer-build/lib/Slicer-4.11/cli-modules/Release" is not a directory. [D:\D\S4R3\Slicer-build\Base\QTCLI\Testing\InstallPyCLITest4.vcxproj] [D:\D\S4R3\Slicer.vcxproj] 
</code></pre>
<p>The complete build environment, all tools and options were exactly the same, I just updated CMake from 3.14.3 to 3.16.2. It is either a regression in CMake (which is very common - so far something broke in every major CMake release) or somehow we use CMake incorrectly. As described in the <a href="https://discourse.slicer.org/t/not-all-modules-are-enabled-after-build/9644">other thread</a>, the problem is that a parallel build is performed by default (and a file is attempted to be copied to a folder that does not exist yet), even though parallel build is not explicitly requested.</p>
<p>It would be interesting to find out why build is not sequential anymore, but it would be probably also useful to allow parallel builds by creating the output directory.</p>

---

## Post #7 by @lassoan (2020-01-09 04:38 UTC)

<p>Submitted a fix for this build error: <a href="https://github.com/Slicer/Slicer/commit/f59653b8b7aa527ceeaacfa3296b009064619bf7">https://github.com/Slicer/Slicer/commit/f59653b8b7aa527ceeaacfa3296b009064619bf7</a></p>
<p>It would be still nice to find out why CMake behavior is changed but right now I cannot spend more time with this investigation.</p>

---

## Post #8 by @cpinter (2020-01-09 07:41 UTC)

<p>Thank you Andras! At least your fix will make sure Slicer builds with the latest CMake. I agree that it would be interesting to know the actual reason, but I also don’t have capacity to investigate this. For me, your fix is an acceptable solution to this problem.</p>

---
