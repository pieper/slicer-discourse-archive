---
topic_id: 47440
title: "Release of Slicer 5.12 in progress"
date: 2026-06-23
url: https://discourse.slicer.org/t/47440
last_bumped: 2026-07-09T02:11:40.311Z
---

# Release of Slicer 5.12 in progress

**Topic ID**: 47440
**Date**: 2026-06-23
**URL**: https://discourse.slicer.org/t/release-of-slicer-5-12-in-progress/47440

---

## Post #1 by @ebrahim (2026-06-23 21:40 UTC)

<p>We’ve temporarily disabled regular Preview and Stable builds of Slicer (and associated extensions) while we prepare the Slicer 5.12 Stable release.</p>
<p>The Slicer repository will be tagged, and the release process will start shortly afterward.</p>

<p>You can track progress in the pinned release issue: <a href="https://github.com/Slicer/Slicer/issues/9180" class="inline-onebox">Release Slicer v5.12 · Issue #9180 · Slicer/Slicer · GitHub</a></p>
<p>Thanks for your patience <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=15" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @ebrahim (2026-06-24 17:38 UTC)

<p>Preview builds are now re-enabled.</p>
<p>We are continuing to work on the Slicer 5.12 stable release</p>

---

## Post #3 by @ebrahim (2026-06-24 21:03 UTC)

<p>Slicer 5.12 is now available!</p>
<p>In the coming days the community will be putting together a release announcement.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://download.slicer.org/">
  <header class="source">
      <img src="https://download.slicer.org/assets/favicons/favicon-32x32.png?v=Gv63MLlwnz" class="site-icon" alt="" width="32" height="32">

      <a href="https://download.slicer.org/" target="_blank" rel="noopener">3D Slicer</a>
  </header>

  <article class="onebox-body">
    <img width="128" height="128" src="https://download.slicer.org/assets/img/3d-slicer-128x128.png" class="thumbnail onebox-avatar" alt="">

<h3><a href="https://download.slicer.org/" target="_blank" rel="noopener">Download 3D Slicer</a></h3>

  <p>3D Slicer is a free, open source software for visualization, processing, segmentation, registration, and analysis of medical, biomedical, and other 3D images and meshes; and planning and navigating image-guided procedures.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lukas-folle (2026-06-25 11:28 UTC)

<p>So Slicer 5.11 stable release is skipped?<br>
This does look a bit confusing to me:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7eb0ef25288a10f91d3a550b6b43ae394121aab.png" data-download-href="/uploads/short-url/swyCRKEtH6NPAnwvUJZjW4w2nEL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7eb0ef25288a10f91d3a550b6b43ae394121aab_2_690x352.png" alt="image" data-base62-sha1="swyCRKEtH6NPAnwvUJZjW4w2nEL" width="690" height="352" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7eb0ef25288a10f91d3a550b6b43ae394121aab_2_690x352.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7eb0ef25288a10f91d3a550b6b43ae394121aab_2_1035x528.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7eb0ef25288a10f91d3a550b6b43ae394121aab_2_1380x704.png 2x" data-dominant-color="F6F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1553×794 60 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @pieper (2026-06-25 11:32 UTC)

<p>That should resolve later today or tomorrow.  The Preview will be renumbered to 5.13.0.  5.12 will be the last Qt5 based Slicer, and 5.13 will become the active refactoring (expect some breaking changes in the API) for a Slicer 6.0 release based on Qt6.</p>

---

## Post #6 by @Sam_Horvath (2026-06-25 13:59 UTC)

<p>The Previews are odd-numbered, the stables are even numbered.</p>

---

## Post #7 by @Sam_Horvath (2026-06-25 14:03 UTC)

<p>There also seems to be an issue with the download site updating to 5.13, working on this</p>

---

## Post #8 by @ebrahim (2026-07-08 11:19 UTC)

<p>Here are the commits I am planning to include before I tag 5.12.1:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/commit/8d6575b975adf262a0f226ae906aa25747967203" class="inline-onebox">COMP: Update DCMTKcs to fix OpenJPEG over-linking on macOS · Slicer/Slicer@8d6575b · GitHub</a></li>
<li><a href="https://github.com/Slicer/Slicer/pull/9273/" class="inline-onebox">BUG: Disable pip install UI off main thread by ebrahimebrahim · Pull Request #9273 · Slicer/Slicer · GitHub</a> (after it is merged)</li>
</ul>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> please let me know if I missed any that you had in mind</p>

---

## Post #9 by @ebrahim (2026-07-08 20:19 UTC)

<p>This evening, regular macOS preview and stable builds of Slicer and associated extensions will be disabled in favor of a <strong>patch</strong> release.</p>
<p>Nightly Windows and Linux builds may be unaffected.</p>
<p>To track the progress, see <a href="https://github.com/Slicer/Slicer/issues/9271" class="inline-onebox">Patch Release Slicer v5.12.1 · Issue #9271 · Slicer/Slicer · GitHub</a></p>

---

## Post #10 by @ebrahim (2026-07-09 02:11 UTC)

<p>Incremental stable builds seem to be still running now for windows and linux, with the scheduled nightly task is about to start in an hour … so I am are disabling those as well to get the patch release completed. Regular linux and windows preview and stable builds will be disabled for tonight, not just macOS. Sorry for any inconvenience; ty for your patience everyone!</p>

---
