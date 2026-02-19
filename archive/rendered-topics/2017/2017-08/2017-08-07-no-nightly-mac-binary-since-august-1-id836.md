---
topic_id: 836
title: "No Nightly Mac Binary Since August 1"
date: 2017-08-07
url: https://discourse.slicer.org/t/836
---

# No nightly Mac binary since August 1

**Topic ID**: 836
**Date**: 2017-08-07
**URL**: https://discourse.slicer.org/t/no-nightly-mac-binary-since-august-1/836

---

## Post #1 by @fedorov (2017-08-07 15:48 UTC)

<p>I downloaded Slicer nightly today, and noticed it is dated Aug 1.</p>
<p>Looking at the dashboard, there is not even an attempt to build on Mac starting August 5.</p>
<p>On <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2017-08-04">Aug 4 the dashboard is red</a>:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/226d951d4d1507fac5ef8e8acf9416197090bf15.png" data-download-href="/uploads/short-url/4Uz0Pp0c4c7JlpTDAMwATdtmquF.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/226d951d4d1507fac5ef8e8acf9416197090bf15_2_690x79.png" alt="image" data-base62-sha1="4Uz0Pp0c4c7JlpTDAMwATdtmquF" width="690" height="79" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/226d951d4d1507fac5ef8e8acf9416197090bf15_2_690x79.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/226d951d4d1507fac5ef8e8acf9416197090bf15_2_1035x118.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/226d951d4d1507fac5ef8e8acf9416197090bf15_2_1380x158.png 2x" data-dominant-color="B4BBBF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1524×176 29.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>On <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2017-08-03">Aug 3</a> there is an error updating the repository:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e5aec4c1ede4af7920ac6195efeac217545d870.png" alt="image" data-base62-sha1="kjkBm3fYPvUPfNpSh9EdDLLNgyI" width="561" height="44"></p>

---

## Post #2 by @jcfr (2017-08-07 18:35 UTC)

<p>To clarify, macOS have initially been broken due to the update of LibArchive. A <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26206">fix</a> was integrated on Friday.</p>
<p>All of this combine with the infrastructure changes described in <a href="https://discourse.slicer.org/t/dashboards-cmake-updated-on-linux-macos-and-windows-build-machines/823">this thread</a>, glitches regarding the macOS build where to be expected.</p>
<p>I will follow up shortly with an update.</p>

---

## Post #3 by @jcfr (2017-08-07 18:39 UTC)

<p>The problem is that the newly installed CMake does not run on the macOS build machine. See below.</p>
<p>This also explain why no error were reported.</p>
<p>A fix will soon be implemented.</p>
<pre><code class="lang-auto">dyld: Library not loaded: /usr/lib/libc++.1.dylib
  Referenced from: /Users/kitware/Dashboards/Support/CMake-3.9.0.app/Contents/bin/ctest
  Reason: image not found
/Users/kitware/DashboardScripts/factory.sh: line 6:  1531 Trace/BPT trap          /Users/kitware/Dashboards/Support/CMake-3.9.0.app/Contents/bin/ctest -S /Users/kitware/DashboardScripts/factory-64bits_slicer4_release_nightly.cmake -VV -O /Users/kitware/Dashboards/Logs/factory-64bits_slicer4_release_nightly.log
dyld: Library not loaded: /usr/lib/libc++.1.dylib
  Referenced from: /Users/kitware/Dashboards/Support/CMake-3.9.0.app/Contents/bin/ctest
  Reason: image not found

</code></pre>

---

## Post #4 by @jcfr (2017-08-07 21:11 UTC)

<p>CMake version used on the macOS factory (running Darwin 10.6.8) has been updated to use a custom build of CMake 3.9.0.</p>
<p>As documented on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory#Software">build work description</a> page, this is required because since CMake release &gt;= 3.6 , Darwin &gt;= 10.7 is required to use the official release package.</p>
<p>The <a href="https://cmake.org/download/">CMake download page</a> has also been updated accordingly.</p>

---

## Post #5 by @jonieva (2017-08-08 13:51 UTC)

<p>I’m not sure if the problem is related, but I also realized that many extensions are not building in Linux either (among them the Chest Imaging Platform), without any errors in CDash whatsoever.</p>

---

## Post #6 by @fedorov (2017-08-08 15:30 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> the problem is not solved</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3313cf5b19630055db55dd11378398650deb1b72.png" data-download-href="/uploads/short-url/7hQNcVWQngIN64Ql5TUowqDByVk.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3313cf5b19630055db55dd11378398650deb1b72_2_690x84.png" alt="image" data-base62-sha1="7hQNcVWQngIN64Ql5TUowqDByVk" width="690" height="84" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3313cf5b19630055db55dd11378398650deb1b72_2_690x84.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3313cf5b19630055db55dd11378398650deb1b72_2_1035x126.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3313cf5b19630055db55dd11378398650deb1b72.png 2x" data-dominant-color="B5BAC6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1348×165 23.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @jcfr (2017-08-09 13:28 UTC)

<p>MacOSx build is available. See <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2017-08-09">http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2017-08-09</a></p>

---

## Post #8 by @fedorov (2017-08-09 13:30 UTC)

<p>Great, thanks <a class="mention" href="/u/jcfr">@jcfr</a>!</p>

---

## Post #9 by @jcfr (2017-08-09 13:59 UTC)

<aside class="quote no-group" data-username="jonieva" data-post="5" data-topic="836">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/91b2a8/48.png" class="avatar"> jonieva:</div>
<blockquote>
<p>many extensions are not building in Linux</p>
</blockquote>
</aside>
<h3><a name="p-3383-nightly-extension-builds-1" class="anchor" href="#p-3383-nightly-extension-builds-1" aria-label="Heading link"></a>nightly extension builds</h3>
<p>Indeed, looking at the dashboard only few extensions are build. See <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2017-08-09&amp;filtercombine=and&amp;filtercombine=and&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=and&amp;field1=site&amp;compare1=63&amp;value1=factory-south-ubuntu-64bits.kitware&amp;field2=groupname&amp;compare2=63&amp;value2=Extensions-Nightly">here</a></p>
<p>I am looking into it and will report back.</p>
<h3><a name="p-3383-h-462-extension-builds-2" class="anchor" href="#p-3383-h-462-extension-builds-2" aria-label="Heading link"></a>4.6.2 extension builds</h3>
<p>4.6.2 nightly extension failed to build because of configure error related to transition to CMake 3.9.0, see below. To address the issue, I locally backported <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26211">r26211</a> and modified <code>SlicerConfig.cmake</code> found in the corresponding Slicer build tree.</p>
<pre><code class="lang-auto">CMake Error: CTEST_USE_LAUNCHERS is enabled, but the RULE_LAUNCH_COMPILE global property is not defined.
Did you forget to include(CTest) in the toplevel CMakeLists.txt ?
Command exited with the value: 1
</code></pre>

---

## Post #10 by @jcfr (2017-08-09 15:06 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="9" data-topic="836">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>nightly extension builds<br>
Indeed, looking at the dashboard only few extensions are build. See here</p>
<p>I am looking into it and will report back.</p>
</blockquote>
</aside>
<p>Look at the log, I found:</p>
<pre><code class="lang-auto">[  7%] Building CXX object ScanConvertPhasedArray3D/CMakeFfatal: reference is not a tree: aaedd3e108ae3f07f38aa517b14bc00b86ded170
CMake Error at XNATSlicer-prefix/tmp/XNATSlicer-gitclone.cmake:75 (message):
  Failed to checkout tag: 'aaedd3e108ae3f07f38aa517b14bc00b86ded170'
</code></pre>
<p>This is causing the extension build process to stop because checkout of extension sources is not <em>sandboxed</em>. Currently only the build and test steps are.</p>
<p>Here is the commit that recently implemented sandboxing for the test step: <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=25439">r25439</a></p>
<p>I am working on a fix.</p>

---

## Post #11 by @jcfr (2017-08-10 16:57 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="10" data-topic="836">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>I am working on a fix.</p>
</blockquote>
</aside>
<p>This topic should prevent failure of downloading one extension source from impacting the complete build.</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/768">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/768" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/768" target="_blank" rel="noopener">should add links to download sample data</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:31:38" data-timezone="UTC">10:31PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:31:38" data-timezone="UTC">10:31PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="slicerbot" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=768). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #12 by @jcfr (2017-08-10 19:00 UTC)

<p>This last issue should be address in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26223">r26223</a></p>

---
