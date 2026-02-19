---
topic_id: 21595
title: "Persistent Favorites Folder In Add Data Gui"
date: 2022-01-24
url: https://discourse.slicer.org/t/21595
---

# Persistent favorites folder in Add Data GUI

**Topic ID**: 21595
**Date**: 2022-01-24
**URL**: https://discourse.slicer.org/t/persistent-favorites-folder-in-add-data-gui/21595

---

## Post #1 by @phcerdan (2022-01-24 10:30 UTC)

<p>Dropping a folder to the list of favorites is great:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92964f3da5adc1ba819af6155232be5be7e83b7c.png" data-download-href="/uploads/short-url/kULKkV3NvqY5s4qUPCl5ofehysQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92964f3da5adc1ba819af6155232be5be7e83b7c_2_690x242.png" alt="image" data-base62-sha1="kULKkV3NvqY5s4qUPCl5ofehysQ" width="690" height="242" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92964f3da5adc1ba819af6155232be5be7e83b7c_2_690x242.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92964f3da5adc1ba819af6155232be5be7e83b7c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92964f3da5adc1ba819af6155232be5be7e83b7c.png 2x" data-dominant-color="E7E9EA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">743×261 24.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But it would be even better if it persist after a restart, or at least that there is an option in general settings to set my favorites folders.</p>
<p>Another related option is to store the recent folders automatically like Paraview.</p>

---

## Post #2 by @chir.set (2022-01-24 18:04 UTC)

<p>I suppose it’s a Qt behaviour, and Qt applications don’t have control of this.</p>
<p>Of the two directories I add this way, one almost always survives a restart, not the other one. The former is added in during ‘Export to file system’ in the DICOM module, and the latter with ‘Import DICOM files’ functions. They visually look the same though.</p>

---

## Post #3 by @jamesobutler (2022-01-24 18:10 UTC)

<p>Using current Slicer preview on Windows, clicking “Choose Directory to Add” brings up the Windows native file dialog so it remembers the last selected location and just overall easier to navigate to favorites/quick access locations from the Window File Explorer. This was as of Late June 2021 (<a href="https://github.com/Slicer/Slicer/commit/2c3bbb7ddbde3618c6056d419eacfb70c12b4e8f" class="inline-onebox" rel="noopener nofollow ugc">ENH: Improve directory and file selection by using native dialogs · Slicer/Slicer@2c3bbb7 · GitHub</a>). Not sure if you’re using current Slicer stable (4.11.20210226) which is older than that.</p>

---

## Post #4 by @chir.set (2022-01-24 19:08 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="21595">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Not sure if you’re using current Slicer stable (4.11.20210226) which is older than that.</p>
</blockquote>
</aside>
<p>I always use latest preview on Linux, built weekly.</p>

---

## Post #5 by @lassoan (2022-01-24 19:59 UTC)

<p>The Qt file dialog could not keep up with improvements in native file dialogs (that are provided by the operating system). The Qt dialog has a few nice features, such as automatic conversion of path separator characters from <code>\</code> to <code>/</code> on Windows and ability to add more file loading/saving options inside the dialog, but lacks integrated search, recently used places, networking, etc. features and overall does not look familiar to users. Therefore, we decided to switch to native file dialogs everywhere.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5d332593ae6eb17946bbaeaccf960002c646a47.png" data-download-href="/uploads/short-url/wN7PiZdosoBxqbEhWFwXqYx0eXR.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5d332593ae6eb17946bbaeaccf960002c646a47_2_690x248.png" alt="image" data-base62-sha1="wN7PiZdosoBxqbEhWFwXqYx0eXR" width="690" height="248" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5d332593ae6eb17946bbaeaccf960002c646a47_2_690x248.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5d332593ae6eb17946bbaeaccf960002c646a47_2_1035x372.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5d332593ae6eb17946bbaeaccf960002c646a47_2_1380x496.png 2x" data-dominant-color="959595"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1482×533 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you still see a Qt file dialog somewhere in a recent Slicer Preview Release then let us know. It might be a case where we rely on some special Qt filedialog features so we could not easily replace it with a native dialog, but maybe we just missed it.</p>

---

## Post #6 by @chir.set (2022-01-24 20:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="21595">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you still see a Qt file dialog somewhere in a recent Slicer Preview Release</p>
</blockquote>
</aside>
<p>Well, they are everywhere in KDE / Linux, with factory built and self built Slicer. I never see a KDialog like this one :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02d6969d73b5a18a28ecfe6c7079648aa4234cc3.png" data-download-href="/uploads/short-url/p6HUR1JGrXmYg1ssVkzwBe1WFR.png?dl=1" title="Screenshot_20220124_211535" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02d6969d73b5a18a28ecfe6c7079648aa4234cc3_2_690x481.png" alt="Screenshot_20220124_211535" data-base62-sha1="p6HUR1JGrXmYg1ssVkzwBe1WFR" width="690" height="481" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02d6969d73b5a18a28ecfe6c7079648aa4234cc3_2_690x481.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02d6969d73b5a18a28ecfe6c7079648aa4234cc3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02d6969d73b5a18a28ecfe6c7079648aa4234cc3.png 2x" data-dominant-color="2C3034"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20220124_211535</span><span class="informations">751×524 66.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It’s not a fundamental issue to me, just reporting.</p>

---

## Post #7 by @lassoan (2022-01-24 21:06 UTC)

<p>Thanks, it is good to know. Probably if Qt cannot access a native file dialog then it uses its own. Can you take a screenshot of the file dialogs that Slicer displays on your system?</p>

---

## Post #8 by @chir.set (2022-01-24 21:12 UTC)

<p>Here is one :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b28a9731e3fc0ae6a86cea867cad43bb41a85ded.png" data-download-href="/uploads/short-url/ptrUXDT0aE2NzSY47rdzvyIKY2N.png?dl=1" title="Screenshot_20220124_221018" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b28a9731e3fc0ae6a86cea867cad43bb41a85ded_2_690x366.png" alt="Screenshot_20220124_221018" data-base62-sha1="ptrUXDT0aE2NzSY47rdzvyIKY2N" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b28a9731e3fc0ae6a86cea867cad43bb41a85ded_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b28a9731e3fc0ae6a86cea867cad43bb41a85ded.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b28a9731e3fc0ae6a86cea867cad43bb41a85ded.png 2x" data-dominant-color="28292A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20220124_221018</span><span class="informations">801×426 36 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>from ‘Import DICOM files’.</p>

---

## Post #9 by @phcerdan (2022-01-24 21:23 UTC)

<p>Thanks <a class="mention" href="/u/chir.set">@chir.set</a>, <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, <a class="mention" href="/u/lassoan">@lassoan</a></p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="21595">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Probably if Qt cannot access a native file dialog</p>
</blockquote>
</aside>
<p>I have never seen a native dialog in Linux from Slicer. I am using latest Linux with latest Gnome, and with any Slicer (4.11 stable, latest 4.13) I get the Qt file dialog (see my screenshot in the opener post).</p>
<p>I have been using Slicer in this computer since ages. Not sure if there is any system wide persistent cache folder that I should delete to start seeing native file dialogs.</p>

---

## Post #10 by @lassoan (2022-01-24 22:25 UTC)

<p><a href="https://doc.qt.io/qt-5/qfiledialog.html">QFileDialog documentation</a> only mentions Windows and macOS related to native file dialog, which may indicate that linux may not be (well) supported. <a href="https://github.com/conda-forge/pyqt-feedstock/issues/87">This discussion</a> suggests that file dialogs of some linux distros and some Qt versions may be found depending on how Qt is built that is used for building Slicer.</p>
<p>The favorites could be probably saved by adding <a href="https://doc.qt.io/qt-5/qfiledialog.html#saveState">saveState</a>/<a href="https://doc.qt.io/qt-5/qfiledialog.html#restoreState">restoreState</a> calls.</p>
<p>You can submit an issue for this (either trying to enable native file dialog on linux and/or saving state of the file dialog), but most likely it would not be worked on anytime soon, as its priority would be quite low compared to other fixes and improvements.</p>

---

## Post #11 by @phcerdan (2022-01-25 22:01 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, I wonder how other OSes are able to see the native file dialog when CTK has this option enabled for Qt&gt;=5: <a href="https://github.com/commontk/CTK/blob/88d954ff72676c96002134de379a92fb8551f476/Libs/Widgets/ctkFileDialog.cpp#L130-L135" class="inline-onebox" rel="noopener nofollow ugc">CTK/ctkFileDialog.cpp at 88d954ff72676c96002134de379a92fb8551f476 · commontk/CTK · GitHub</a></p>

---

## Post #12 by @lassoan (2022-01-25 22:09 UTC)

<p>The switch to native dialogs happened in this commit:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/commontk/CTK/commit/c4f1eeead234022e74de978126e3a54f648880e5#diff-410d32c5e7ff5ca929f1d1947d2b82a75ea73112ed088303856f5aade6c13757">
  <header class="source">

      <a href="https://github.com/commontk/CTK/commit/c4f1eeead234022e74de978126e3a54f648880e5#diff-410d32c5e7ff5ca929f1d1947d2b82a75ea73112ed088303856f5aade6c13757" target="_blank" rel="noopener">github.com/commontk/CTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/commit/c4f1eeead234022e74de978126e3a54f648880e5" target="_blank" rel="noopener">ENH: Update ctkFileDialog to use native dialog by default</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2021-06-10" data-time="19:07:38" data-timezone="UTC">07:07PM - 10 Jun 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="changed 1 files with 20 additions and 13 deletions">
        <a href="https://github.com/commontk/CTK/commit/c4f1eeead234022e74de978126e3a54f648880e5" target="_blank" rel="noopener">
          <span class="added">+20</span>
          <span class="removed">-13</span>
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


---

## Post #13 by @phcerdan (2024-07-31 22:35 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> Did you find any workaround on this to work in Linux? I tried changing some <code>QT_QPA_PLATFORMTHEME</code> settings, with no luck.</p>
<p>I tried qt5ct, gtk3.<br>
I can access native dialogs in other qt apps, at least qt6 apps.</p>

---

## Post #14 by @chir.set (2024-08-01 06:34 UTC)

<aside class="quote no-group" data-username="phcerdan" data-post="13" data-topic="21595">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/phcerdan/48/1559_2.png" class="avatar"> phcerdan:</div>
<blockquote>
<p>Did you find any workaround on this to work in Linux?</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/phcerdan">@phcerdan</a></p>
<p>No, since I have never been looking for a solution. I’m just using it as it is.</p>

---

## Post #15 by @phcerdan (2024-11-12 15:24 UTC)

<p>Issue in github related to this: <a href="https://github.com/Slicer/Slicer/issues/7674" class="inline-onebox" rel="noopener nofollow ugc">Native file manager not used on Linux · Issue #7674 · Slicer/Slicer · GitHub</a></p>

---
