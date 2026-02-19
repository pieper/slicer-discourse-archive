---
topic_id: 42966
title: "Under Arch Installed Slicer And Slicerswissskullstripper Ran"
date: 2025-05-16
url: https://discourse.slicer.org/t/42966
---

# Under arch, installed Slicer and SlicerSwissSkullStripper. Ran and got undefined symbol: _ZN10slicer_itk13ProcessObject9SetOutputERKSsPNS_10DataObjectE error

**Topic ID**: 42966
**Date**: 2025-05-16
**URL**: https://discourse.slicer.org/t/under-arch-installed-slicer-and-slicerswissskullstripper-ran-and-got-undefined-symbol-zn10slicer-itk13processobject9setoutputerksspns-10dataobjecte-error/42966

---

## Post #1 by @hoteh (2025-05-16 12:52 UTC)

<blockquote>
<p>Slicer --version<br>
Slicer 5.8.1-2025-03-02</p>
</blockquote>
<blockquote>
<p>SwissSkullStripper<br>
Last update: Mon Mar 03 2025 4257d72</p>
</blockquote>
<p>Any more information required?</p>

---

## Post #2 by @lassoan (2025-05-16 12:52 UTC)

<p>This is discussed here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/lassoan/SlicerSwissSkullStripper/issues/2">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerSwissSkullStripper/issues/2" target="_blank" rel="noopener">github.com/lassoan/SlicerSwissSkullStripper</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/lassoan/SlicerSwissSkullStripper/issues/2" target="_blank" rel="noopener">Under arch, installed Slicer and SlicerSwissSkullStripper. Ran and got undefined symbol: _ZN10slicer_itk13ProcessObject9SetOutputERKSsPNS_10DataObjectE error:</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-05-15" data-time="19:34:47" data-timezone="UTC">07:34PM - 15 May 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/mrect" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/134049387?v=4" class="onebox-avatar-inline" width="20" height="20">
          mrect
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">&gt; Slicer --version
Slicer 5.8.1-2025-03-02

&gt; SwissSkullStripper
Last update: Mo<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">n Mar 03 2025  4257d72

Any more information required?</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2025-05-16 12:55 UTC)

<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> <a class="mention" href="/u/jcfr">@jcfr</a> do you have any ideas for this?</p>

---

## Post #4 by @PaoloZaffino (2025-05-16 13:44 UTC)

<p>I use Arch Linux, if I can run some tests just let me know</p>

---

## Post #5 by @hoteh (2025-05-16 14:03 UTC)

<p>are you also using Slicer 5.8.1-2025-03-02 ? If so, that is odd that I am experiencing it and not you. Unless there is an extra library that should be marked as required? <a href="https://aur.archlinux.org/packages/3dslicer" rel="noopener nofollow ugc">https://aur.archlinux.org/packages/3dslicer</a></p>

---

## Post #6 by @chir.set (2025-05-16 15:05 UTC)

<p>With Slicer <code>5.8.1 r33241 / 11eaf62</code> from the official Slicer download site, which is only repacked by the <code>AUR</code> <code>PKGBUILD</code>, SwissSkullStripper <code>4257d72 (2025-03-03)</code> runs without errors on Arch. Slicer is not in <code>/opt</code> but in <code>$HOME</code>. How do you install an extension in <code>/opt</code> ?</p>

---

## Post #7 by @RafaelPalomar (2025-05-16 15:28 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="6" data-topic="42966">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>How do you install an extension in <code>/opt</code> ?</p>
</blockquote>
</aside>
<p>I guessthe reason is because Slicer is compiled with <code>-Slicer_STORE_SETTINGS_IN_APPLICATION_HOME_DIR=OFF</code></p>
<p><a class="mention" href="/u/hoteh">@hoteh</a>, <a class="mention" href="/u/lassoan">@lassoan</a> I’m not very surprised extensions cause problems. The <code>3dslicer</code> package is not a repackaged 3D Slicer binary, but a locally built one. Binary extensions are currently built on an old <code>CentOS</code> environment with <code>gcc-7</code>. This is far too different from the bleeding edge environment that arch provides with <code>gcc-13</code>. The SwissSkullStripper probably won’t be the only extension crashing. We experienced the same issue with the flatpak experience; we managed to get a flatpak version of Slicer, but extensions (some) will crash.</p>
<p><a class="mention" href="/u/hoteh">@hoteh</a>, I have tried the official 3D Slicer binary with the SwissSkullStripper extension and seems to work fine.</p>

---

## Post #8 by @hoteh (2025-05-16 15:29 UTC)

<p>I had an issue with the install path when installing the binary <a href="https://aur.archlinux.org/packages/3dslicer-bin" rel="noopener nofollow ugc">3dslicer-bin</a>, but when installing from source, <a href="https://aur.archlinux.org/packages/3dslicer" rel="noopener nofollow ugc">3dslicer</a> it appears to install in the proper path. As per the doc <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#archlinux" class="inline-onebox" rel="noopener nofollow ugc">Getting Started — 3D Slicer documentation</a> that makes sense. There is an explicit warning against using 3dslicer-bin for that reason.</p>
<p>I could try installing 3dslicer-bin, and then giving write permision to /opt/3dslicer (I did that for freesurfer).</p>

---

## Post #9 by @hoteh (2025-05-16 15:37 UTC)

<p>SOLVED!<br>
I installed 3dslicer-bin, added write permissions to /opt/3dslicer, and all is well.</p>

---
