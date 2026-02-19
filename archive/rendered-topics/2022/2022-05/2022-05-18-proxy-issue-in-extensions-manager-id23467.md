---
topic_id: 23467
title: "Proxy Issue In Extensions Manager"
date: 2022-05-18
url: https://discourse.slicer.org/t/23467
---

# Proxy issue in Extensions Manager

**Topic ID**: 23467
**Date**: 2022-05-18
**URL**: https://discourse.slicer.org/t/proxy-issue-in-extensions-manager/23467

---

## Post #1 by @simonoxen (2022-05-18 10:18 UTC)

<p>Hi, when using work computer (MacOS, network with proxy) I’ve been having the issue that extensions cannot be downloaded from the Extensions Manager.</p>
<p>Extensions show, but fails to retrieve metadata and to install them. The error shows:</p>
<pre><code class="lang-auto">Execution of PAC script at "http%3A%2F%2Fproxy.[...]" failed: The operation couldn’t be completed. (NSURLErrorDomain error -1002.)
</code></pre>
<p>(I replaced my institution by <code>[...]</code>)</p>
<p>I looked a bit more into it and the issue was reported here <a href="https://bugreports.qt.io/browse/QTBUG-98024" class="inline-onebox" rel="noopener nofollow ugc">[QTBUG-98024] "Execution of PAC script … failed" on macOS, invalid URL escaping of proxy auto configuration URL - Qt Bug Tracker</a> . Relating to an issue in Qt 5.12 that was <a href="https://github.com/qt/qtbase/commit/94c3c7a491e0c25cf2179efe04c2fbd80b370c1c#diff-3cfd00a70578d8e3f82970fc01470b3da316178d6123267c6bc677a4e1251592" rel="noopener nofollow ugc">solved</a> for Qt 6.0.</p>
<p>I’ve been manually installing extensions and helping other in my institution to do so, but this has become a bit cumbersome and annoying for new users.</p>
<p>I guess if Slicer updates the qt version this issue could be solved. Are there planes for that? If not, is there a way to fix this from another side? I’ve been looking a bit, but thought to ask to get better directions.</p>
<p>I found this weird since downloads from other points of the application (such as downloading sample data) work flawlessly.</p>
<p>Thanks a lot for the help.</p>

---

## Post #2 by @pieper (2022-05-18 12:57 UTC)

<p>Thanks for the report <a class="mention" href="/u/simonoxen">@simonoxen</a>.  We will switch to Qt 6.x as soon as feasible, I don’t know the status of all the components but I suspect it will happen in the next year or sooner for the preview version.  It might make sense to write a small python script that downloads using non-Qt methods and runs the installation if your manual workaround is to cumbersome.</p>

---

## Post #3 by @lassoan (2022-05-19 20:41 UTC)

<p>Qt6 raises minimum platform requirements and it requires solid support in all underlying libraries, so unless there are several other pressing issues that Qt6 solves then end of this year could be a realistic target. I added an <a href="https://github.com/Slicer/Slicer/issues/6388">issue</a> and tentatively targeted it for Slicer-5.2.</p>
<p>It seems that the fix for this particular issue is a single-line change in Qt, so we could possibly patch it in our Qt builds. <a class="mention" href="/u/jcfr">@jcfr</a> do we still build Qt from source on factory machines?</p>
<p><a class="mention" href="/u/simonoxen">@simonoxen</a> could you try if you <a href="https://github.com/jcfr/qt-easy-build">build Qt from source</a> and apply <a href="https://github.com/qt/qtbase/commit/94c3c7a491e0c25cf2179efe04c2fbd80b370c1c#diff-3cfd00a70578d8e3f82970fc01470b3da316178d6123267c6bc677a4e1251592">this patch</a> then it fixes the issue for you?</p>

---

## Post #4 by @simonoxen (2022-05-23 09:36 UTC)

<p>Thanks for the replies.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="23467">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/simonoxen">@simonoxen</a> could you try if you <a href="https://github.com/jcfr/qt-easy-build" rel="noopener nofollow ugc">build Qt from source</a> and apply <a href="https://github.com/qt/qtbase/commit/94c3c7a491e0c25cf2179efe04c2fbd80b370c1c#diff-3cfd00a70578d8e3f82970fc01470b3da316178d6123267c6bc677a4e1251592" rel="noopener nofollow ugc">this patch</a> then it fixes the issue for you?</p>
</blockquote>
</aside>
<p>Doing this fixes the issue on my work computer. I built and packaged Slicer on my personal computer and then installed Slicer there, now Extensions can be downloaded.</p>
<p><strong>Before</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/396fb9b155c591125d84fb8db5a68966f85f3750.jpeg" data-download-href="/uploads/short-url/8c6AlJIVfZx8ys7Z4Pt6MLK9qlq.jpeg?dl=1" title="Screen Shot 2022-05-23 at 11.12.30" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/396fb9b155c591125d84fb8db5a68966f85f3750_2_690x388.jpeg" alt="Screen Shot 2022-05-23 at 11.12.30" data-base62-sha1="8c6AlJIVfZx8ys7Z4Pt6MLK9qlq" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/396fb9b155c591125d84fb8db5a68966f85f3750_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/396fb9b155c591125d84fb8db5a68966f85f3750_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/396fb9b155c591125d84fb8db5a68966f85f3750_2_1380x776.jpeg 2x" data-dominant-color="E7E8EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-05-23 at 11.12.30</span><span class="informations">1920×1080 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>After</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc7d59dae98cba2a258fd7882db2cb5e3f8a6e30.jpeg" data-download-href="/uploads/short-url/qTskjJTQOOsDh5OS7RLcLQhHNmw.jpeg?dl=1" title="Screen Shot 2022-05-23 at 11.10.37" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc7d59dae98cba2a258fd7882db2cb5e3f8a6e30_2_690x388.jpeg" alt="Screen Shot 2022-05-23 at 11.10.37" data-base62-sha1="qTskjJTQOOsDh5OS7RLcLQhHNmw" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc7d59dae98cba2a258fd7882db2cb5e3f8a6e30_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc7d59dae98cba2a258fd7882db2cb5e3f8a6e30_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc7d59dae98cba2a258fd7882db2cb5e3f8a6e30_2_1380x776.jpeg 2x" data-dominant-color="E7EBEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-05-23 at 11.10.37</span><span class="informations">1920×1080 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There is however another issue now with the build from personal computer: Extensions do not show. They can be downloaded and installed by restoring from previous, but they don’t show. I’m not sure wether this is related or not. Here is the log:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 23.05.2022 11:26:53 [] (unknown:0) - Session start time .......: 2022-05-23 11:26:53
[DEBUG][Qt] 23.05.2022 11:26:53 [] (unknown:0) - Slicer version ...........: 5.0.2-2022-05-06 (revision 30822 / a4420c3) macosx-amd64 - not installed release
[DEBUG][Qt] 23.05.2022 11:26:53 [] (unknown:0) - Operating system .........: macOS / 11.2.1 / 20D74 / UTF-8 - 64-bit
[DEBUG][Qt] 23.05.2022 11:26:53 [] (unknown:0) - Memory ...................: 16384 MB physical, 0 MB virtual
[DEBUG][Qt] 23.05.2022 11:26:53 [] (unknown:0) - CPU ......................: GenuineIntel Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz, 6 cores, 12 logical processors
[DEBUG][Qt] 23.05.2022 11:26:53 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, Sequential threading
[DEBUG][Qt] 23.05.2022 11:26:53 [] (unknown:0) - Qt configuration .........: version 5.15.1, with SSL, requested OpenGL 3.2 (core profile)
[DEBUG][Qt] 23.05.2022 11:26:53 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 23.05.2022 11:26:53 [] (unknown:0) - Developer mode ...........: enabled
[DEBUG][Qt] 23.05.2022 11:26:53 [] (unknown:0) - Application path .........: /Users/simon/bin/Slicer/Slicer-build/bin/Slicer.app/Contents/MacOS
[DEBUG][Qt] 23.05.2022 11:26:53 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 23.05.2022 11:26:55 [Python] (/Users/simon/bin/Slicer/Slicer-build/lib/Slicer-5.0/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 23.05.2022 11:26:55 [Python] (/Users/simon/bin/Slicer/Slicer-build/lib/Slicer-5.0/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 23.05.2022 11:26:55 [Python] (/Users/simon/bin/Slicer/Slicer-build/lib/Slicer-5.0/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 23.05.2022 11:26:55 [] (unknown:0) - Switch to module:  "Welcome"
[INFO][Stream] 23.05.2022 11:26:56 [] (unknown:0) - Loading Slicer RC file [/Users/simon/.slicerrc.py]
[CRITICAL][FD] 23.05.2022 11:26:57 [] (unknown:0) - [1185:119051:0523/112657.831671:ERROR:socket_posix.cc(148)] bind() failed: Address already in use (48)
[CRITICAL][FD] 23.05.2022 11:26:57 [] (unknown:0) - [1185:119051:0523/112657.831721:ERROR:devtools_http_handler.cc(299)] Cannot start http server for devtools.
[CRITICAL][FD] 23.05.2022 11:26:58 [] (unknown:0) - [1185:98819:0523/112658.096282:ERROR:gl_context_cgl.cc(118)] Error creating context.
[CRITICAL][FD] 23.05.2022 11:26:58 [] (unknown:0) - [0523/112658.203425:ERROR:icu_util.cc(199)] Couldn't mmap icu data file
[CRITICAL][FD] 23.05.2022 11:26:58 [] (unknown:0) - [0523/112658.203736:ERROR:icu_util.cc(199)] Couldn't mmap icu data file
[CRITICAL][FD] 23.05.2022 11:26:58 [] (unknown:0) - [0523/112658.707508:ERROR:icu_util.cc(199)] Couldn't mmap icu data file
[CRITICAL][FD] 23.05.2022 11:26:58 [] (unknown:0) - [0523/112658.966048:ERROR:icu_util.cc(199)] Couldn't mmap icu data file
[WARNING][Qt] 23.05.2022 11:26:59 [] (unknown:0) - static bool qSlicerExtensionsManagerModelPrivate::validateExtensionMetadata(const qSlicerExtensionsManagerModelPrivate::ExtensionMetadataType &amp;, int)  failed: expected key ' "meta.screenshots" ' is missing from extension metadata.

</code></pre>
<p>Would be great if this fix could be incorporated! Thanks a lot for the help!</p>

---

## Post #5 by @jamesobutler (2022-05-23 13:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="23467">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>and apply <a href="https://github.com/qt/qtbase/commit/94c3c7a491e0c25cf2179efe04c2fbd80b370c1c#diff-3cfd00a70578d8e3f82970fc01470b3da316178d6123267c6bc677a4e1251592" rel="noopener nofollow ugc">this patch</a> then it fixes the issue for you?</p>
</blockquote>
</aside>
<p>It appears that patch was backported to the Qt 5.15 maintenance branch (see below). Although there is only tags up to Qt 5.15.2 and this patch came afterwards and was likely included in Qt 5.15.3 based on the date, the <a href="https://github.com/qt/qtbase/tree/5.15" class="inline-onebox" rel="noopener nofollow ugc">GitHub - qt/qtbase at 5.15</a> branch appears to have many additional fixes for the Qt 5.15 release. This could potentially be used when building from source.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/qt/qtbase/commit/6af20a8eb621c03d06e18049a1e6559831d73c17">
  <header class="source">

      <a href="https://github.com/qt/qtbase/commit/6af20a8eb621c03d06e18049a1e6559831d73c17" target="_blank" rel="noopener nofollow ugc">github.com/qt/qtbase</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/qt/qtbase/commit/6af20a8eb621c03d06e18049a1e6559831d73c17" target="_blank" rel="noopener nofollow ugc">macOS: Make sure that the reserved characters are not escaped</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2020-12-04" data-time="16:28:24" data-timezone="UTC">04:28PM - 04 Dec 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/AndyShawQt" target="_blank" rel="noopener nofollow ugc">
          <img alt="AndyShawQt" src="https://avatars.githubusercontent.com/u/19864488?v=4" class="onebox-avatar-inline" width="20" height="20">
          AndyShawQt
        </a>
      </div>

      <div class="lines" title="changed 1 files with 1 additions and 1 deletions">
        <a href="https://github.com/qt/qtbase/commit/6af20a8eb621c03d06e18049a1e6559831d73c17" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+1</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The URL for the PAC proxy that is passed needs to be preserved for the
main URL <span class="show-more-container"><a href="https://github.com/qt/qtbase/commit/6af20a8eb621c03d06e18049a1e6559831d73c17" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">part and not entirely percent encoded, only the query part
typically needs to be encoded. So use toEncoded instead for a URL to
ensure they are not percent encoded. This amends
c163ec1dbf873781b77ea67d4449d643c166c0c4

Change-Id: Ie41ab55f71be8e25c18775e61ce7b4d110c2ddbf
Reviewed-by: Tor Arne Vestbø &lt;tor.arne.vestbo@qt.io&gt;
(cherry picked from commit 94c3c7a491e0c25cf2179efe04c2fbd80b370c1c)
Reviewed-by: Qt Cherry-pick Bot &lt;cherrypick_bot@qt-project.org&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2022-05-23 20:59 UTC)

<p>In the Qt install tool the latest available version is Qt-5.15.2. Qt company have already stopped long-term-support for open-source users, so <a href="https://www.qt.io/blog/commercial-lts-qt-5.15.3-released">Qt-5.15.3 release is only available for paying users</a>. Free users needs to use latest Qt release to get patches.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Do you think we could use commercial license for creating Slicer packages using Qt LTS releases, such as Qt-5.15.3? I’m not sure it is a good idea, just wondering about possible options.</p>

---

## Post #7 by @jamesobutler (2022-05-23 21:29 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Are you not wanting to use latest <a href="https://github.com/qt/qtbase/tree/5.15" class="inline-onebox" rel="noopener nofollow ugc">GitHub - qt/qtbase at 5.15</a> which includes the patch for macOS because it would be different from the Qt 5.15.2 pre-built binaries downloaded for the Windows platform? We already build Qt from source for macOS Slicer factory builds.</p>

---

## Post #8 by @lassoan (2022-05-24 02:29 UTC)

<p>Qt-5.15 is a special case. There are some <a href="https://github.com/qt/qtbase/tags">LGPL LTS tags</a>. There are <a href="https://wiki.qt.io/Qt_5.15_Release#Release_Plan">Commercial LTS versions</a> that are a year ahead of thoseLGPL tags. For example <code>Qt 5.15.4-lts-lgpl</code> was released in May 2022, while Qt 5.15.4 was released in May 2021 (a year earlier). I don’t know if this is a coincidence or if there is an agreement that changes must be made public in 12 months (I remember reading something like this somewhere). There is also <a href="https://community.kde.org/Qt5PatchCollection">KDE’s Qt-5.15 patch collection</a>. We could probably build Qt from one of these sources, which would be inconvenient, but tolerable.</p>
<p>After Qt-5.15 I’m not sure if we can continue what we have been doing, but we have a few options to choose from:</p>
<ul>
<li>using Qt’s official rolling latest release: as we know Qt, these often contain regressions (bugs, missing features whenever there is some refactoring); but it is nice that we don’t need to build Qt form source on Windows and Linux</li>
<li>use unofficial LTS-like releases: a chosen Qt version with some important patches applied. We could do this at a very limited scope (merge fixes that users explicitly complain about), but maybe KDE or other project will maintain patch collections for Qt6 that we can use in the future.</li>
<li>buy commercial license that gives access to LTS releases: Qt charges a completely unreasonable price for their commercial license, which makes it impossible to buy every developer a license; so this is not really an option</li>
</ul>

---

## Post #9 by @simonoxen (2022-06-09 15:57 UTC)

<p>btw, I put the packaged Slicer <a href="https://github.com/simonoxen/SlicerForMacWithProxy/releases/tag/v5.0.2" rel="noopener nofollow ugc">here</a>, in case someone wants to test it.</p>

---

## Post #10 by @lassoan (2022-06-12 12:46 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> are we using self-built Qt on the factory machine? Could we apply this one-line patch to Qt?</p>

---
