---
topic_id: 19166
title: "Vmtk Library Is Not Found And Extensions Are Imcompatibe Wit"
date: 2021-08-12
url: https://discourse.slicer.org/t/19166
---

# VMTK library is not found and extensions are imcompatibe with slicer (MAC and Win, 4.13.0 built 2021-08-11 )

**Topic ID**: 19166
**Date**: 2021-08-12
**URL**: https://discourse.slicer.org/t/vmtk-library-is-not-found-and-extensions-are-imcompatibe-with-slicer-mac-and-win-4-13-0-built-2021-08-11/19166

---

## Post #1 by @xiaolin (2021-08-12 08:58 UTC)

<p>Hi everyone. Yesterday I downloaded Slicer 4.13.0 2021-08-11 in Mac and Windows, but there are some issues regarding the extensions ( incompatible with slicer) , VMTK library is not found when I used the " ExtractCenterline". Does anybody know how to address the issues?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e07db8378e44fe858935f5cda39ab890546cfa44.jpeg" data-download-href="/uploads/short-url/w1WiZI5j5cWDFcYfHS94nGYHWyU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e07db8378e44fe858935f5cda39ab890546cfa44_2_690x337.jpeg" alt="image" data-base62-sha1="w1WiZI5j5cWDFcYfHS94nGYHWyU" width="690" height="337" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e07db8378e44fe858935f5cda39ab890546cfa44_2_690x337.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e07db8378e44fe858935f5cda39ab890546cfa44_2_1035x505.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e07db8378e44fe858935f5cda39ab890546cfa44_2_1380x674.jpeg 2x" data-dominant-color="F2F2F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2872×1406 235 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/822120cd9d02629dd5e2d65f046a7890684743cf.jpeg" data-download-href="/uploads/short-url/izb2XZFMAtId5qHeQCDIH0qSZWv.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/822120cd9d02629dd5e2d65f046a7890684743cf_2_690x389.jpeg" alt="image" data-base62-sha1="izb2XZFMAtId5qHeQCDIH0qSZWv" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/822120cd9d02629dd5e2d65f046a7890684743cf_2_690x389.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/822120cd9d02629dd5e2d65f046a7890684743cf_2_1035x583.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/822120cd9d02629dd5e2d65f046a7890684743cf_2_1380x778.jpeg 2x" data-dominant-color="909391"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1083 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks in advance.</p>

---

## Post #2 by @jamesobutler (2021-08-12 11:24 UTC)

<p>That was an issue with yesterday’s Slicer version. Try again with today’s version.</p>
<p>See the following for more details</p>
<aside class="quote" data-post="2" data-topic="19158">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/unable-to-install-extension-incompatible-with-slicer-r30110/19158/2">Unable to install extension - "Incompatible with Slicer r30110"</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Thanks for the report, it is a side effect of <a href="https://discourse.slicer.org/t/upcoming-downtime-for-download-slicer-org-and-extension-manager-due-to-package-server-transition/17444/3" class="inline-onebox">Upcoming downtime for download.slicer.org and extension manager due to package server transition - #3 by jcfr</a>, issue has been identified earlier today and I am currently working on this. 
For reference, this is now tracked in <a href="https://github.com/Slicer/Slicer/issues/5786" class="inline-onebox" rel="noopener nofollow ugc">Installed extensions are not loaded · Issue #5786 · Slicer/Slicer · GitHub</a>
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2021-08-12 18:15 UTC)

<p>There is also an independent issue (caused by switching to VTK9) with VMTK packaging, only on macOS:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/issues/37">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/37" target="_blank" rel="noopener">github.com/vmtk/SlicerExtension-VMTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/37" target="_blank" rel="noopener">VMTK gone missing recently in Slicer-4.11.20210226 and latest Slicer-4.13</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-08-09" data-time="19:08:54" data-timezone="UTC">07:08PM - 09 Aug 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The extension installation package does not contain VMTK binaries, only the Slic<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">er module .py files, for both latest Slicer Stable Release and Slicer Preview Release on macOS.

It seems that the recent upgrade to VTK9 broke packaging for VTK-8.2.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/jcfr">@jcfr</a> may be able to fix it by the end of this week, but if not then he said he would be able to get back to it in a few weeks.</p>

---
