# Qt5 binary package

**Topic ID**: 27710
**Date**: 2023-02-08
**URL**: https://discourse.slicer.org/t/qt5-binary-package/27710

---

## Post #1 by @lassoan (2023-02-08 19:18 UTC)

<p>I’ve been helping a developer building Slicer on Windows, and I’m shocked to see what The Qt Company did again: they removed Qt-5.15 binaries from their servers. Qt5 versions more recent than Qt-5.12 are no longer available as binary packages.</p>
<p>Our options seem to be:</p>
<ul>
<li>A. Recommend developers to use Qt-5.12: Not a great solution, as all the bugs that have been fixed since Qt-5.12 would return.</li>
<li>B. Build latest Qt5 version from source. Difficulty is that <a href="https://github.com/jcfr/qt-easy-build">Qt easy-build</a> has not been updated recently for Windows (as we did not expect the Qt Company to retrospectively remove Qt versions that it provided earlier).</li>
<li>C. Expedited upgrade to Qt6: It would not be an easy task, as we need to upgrade CTK and PythonQt and then Slicer to support Qt6.</li>
<li>D. Pay for Qt: This could be reasonable if the The Qt Company would set a reasonable price for their services and they would not be so hostile tp open-source developers.</li>
</ul>
<p>Have you run into this issue recently? How did you solve this issue?</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/cpinter">@cpinter</a> How do you think we should proceed?</p>

---

## Post #2 by @lassoan (2023-02-08 19:35 UTC)

<p>I’ve checked again on a different computer, using the Qt online installer to install Qt from scratch and this time <strong>Qt5 binary packages up to Qt-5.15.2 were available for installation again</strong>. It might have been a glitch in the file hosting server yesterday or something wrong in that computer’s configuration. Anyway, this is no longer an emergency.</p>
<p>Still, this short scare showed how exposed we are to Qt changes. We could reduce our vulnerability by making Qt easy-build work again for Windows, but probably a more forward-looking solution would be to increase priority of switching to Qt6.</p>

---

## Post #3 by @pieper (2023-02-08 19:40 UTC)

<p>I agree, this is an odd situation.  I personally think that the Qt company is hurting themselves by discouraging open source developer participation.  If developers don’t know Qt then companies will have no reason to use it in products.</p>
<p>For now, I think the best options are to migrate more quickly to Qt 6, which is something we want to do anyway, and work on getting qt-easy-build working (ideally for Qt 5 and 6).</p>

---

## Post #4 by @jamesobutler (2023-02-08 19:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="27710">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It might have been a glitch in the file hosting server yesterday or something wrong in that computer’s configuration. Anyway, this is no longer an emergency.</p>
</blockquote>
</aside>
<p>What you originally described seemed like an issue of an outdated Qt Maintenance Tool as though it was too old and didn’t know yet of Qt 5.15.</p>
<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="27710">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>For now, I think the best options are to migrate more quickly to Qt 6, which is something we want to do anyway, and work on getting qt-easy-build working (ideally for Qt 5 and 6).</p>
</blockquote>
</aside>
<p>+1 here. The qt-easy-build makes sense for the non-cmake build process of Qt5, but since Qt6 is cmake-ified natively it would seemingly just slot into the superbuild process if not using binaries.</p>
<p>Below is an open PR of mine that is working towards Qt6 support by replacing the deprecated Qt Script dependency.</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6710">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6710" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6710" target="_blank" rel="noopener nofollow ugc">COMP: Replace deprecated Qt Script usage</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>jamesobutler:qt-script-removal</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2022-11-29" data-time="23:58:37" data-timezone="UTC">11:58PM - 29 Nov 22 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
            <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
            jamesobutler
          </a>
        </div>

        <div class="lines" title="3 commits changed 8 files with 19 additions and 23 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6710/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+19</span>
            <span class="removed">-23</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Qt Script was available in Qt 5 for backwards compatibility with Qt 4 only. Slic<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6710" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">er dropped Qt 4 support in https://github.com/Slicer/Slicer/commit/c7fe93d44fc93fe56f0d085e4843b41b261bc0a2.

 QJSEngine and related classes in the Qt QML module should be used instead. https://doc.qt.io/qt-5/qtscript-index.html

I have built successfully on the Windows platform with the standard Slicer build configuration. All tests are passing as well. `1&gt;100% tests passed, 0 tests failed out of 662`. Before building Slicer I removed the Qt Script component from my local install. I used the Qt Maintenance Tool application to remove the Qt Script component from the Qt 5.15 selection.

This is also work towards #6388 because Qt Script is removed in Qt 6.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @jamesobutler (2023-02-08 19:51 UTC)

<p>I can confirm with my Qt Maintenance tool with the non-default options of “Archive” and “LTS” categories that all Qt 5 options are still present.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05aea52837906b6c0300d26a336157dc60682359.jpeg" data-download-href="/uploads/short-url/OgyTANYdSSjeIiXwnda7eczBl7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05aea52837906b6c0300d26a336157dc60682359_2_690x458.jpeg" alt="image" data-base62-sha1="OgyTANYdSSjeIiXwnda7eczBl7" width="690" height="458" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05aea52837906b6c0300d26a336157dc60682359_2_690x458.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05aea52837906b6c0300d26a336157dc60682359.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05aea52837906b6c0300d26a336157dc60682359.jpeg 2x" data-dominant-color="132912"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">952×632 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2023-02-08 20:15 UTC)

<p>Thanks for checking. The Qt maintenance tool knew about all the latest Qt6 packages, so it was not simply old, but something less trivial.</p>
<p>Anyway, it seems there is a consensus on escaping to Qt6. We’ll try to prioritize this when <a class="mention" href="/u/jcfr">@jcfr</a> is back. Until then I’ll start working on getting <a href="https://github.com/Slicer/Slicer/pull/6710" class="inline-onebox">COMP: Replace deprecated Qt Script usage by jamesobutler · Pull Request #6710 · Slicer/Slicer · GitHub</a> integrated.</p>

---

## Post #7 by @jamesobutler (2023-02-09 03:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="27710">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The Qt maintenance tool knew about all the latest Qt6 packages, so it was not simply old, but something less trivial.</p>
</blockquote>
</aside>
<p>Likely just not selecting the LTS/Archive categories to filter. The tool by default only shows latest supported versions and also already installed versions.</p>

---

## Post #8 by @lassoan (2023-02-09 03:44 UTC)

<p>I enabled LTS and Archive, clicked filter, it spent some time refreshing packages, still it only showed Qt6 packages. I will try it again.</p>

---

## Post #9 by @cpinter (2023-02-09 10:01 UTC)

<p>Thanks for starting the topic Andras. I think I have seen such a glitch before but in a few minutes the package was available again so I probably thought it was a network issue. I agree with trying to prioritize the switch to Qt6.</p>
<p>Do we know how much Qt would cost for a platform like Slicer? As far as I know you can purchase licenses per developer (may be mistaken or may have changed), which model does not fit our case well.</p>

---

## Post #10 by @pieper (2023-02-09 13:12 UTC)

<p>I’ve never seen that the Qt company would have a purchase option that would make sense for Slicer.  We are very careful to stick with their LGPL requirements so it would be hard to justify spending money on any such option even if they had it.  As long as we are able to support our current use cases with the LGPL option I think we are in a good spot, and keeping up with their latest versions isn’t a bad idea so long as it doesn’t break something we really need.</p>
<p>I’m intrigued that the new CMake support in Qt could make it easier for us to integrate with Slicer’s superbuild.  Even if you usually would want to build against a binary package for efficiency having the build from source option would be great.</p>

---
