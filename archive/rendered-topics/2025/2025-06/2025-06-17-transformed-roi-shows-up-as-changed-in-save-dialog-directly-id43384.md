---
topic_id: 43384
title: "Transformed Roi Shows Up As Changed In Save Dialog Directly"
date: 2025-06-17
url: https://discourse.slicer.org/t/43384
---

# Transformed ROI shows up as changed in Save dialog directly after opening an mrml scene

**Topic ID**: 43384
**Date**: 2025-06-17
**URL**: https://discourse.slicer.org/t/transformed-roi-shows-up-as-changed-in-save-dialog-directly-after-opening-an-mrml-scene/43384

---

## Post #1 by @MMMPPPMMM (2025-06-17 12:39 UTC)

<p>Hello</p>
<p>I think it is a bug that a transformed ROI shows up as changed in Save dialog directly after opening an MRML scene?</p>
<p>Find an example here: <a href="https://limewire.com/d/CaQaa#kOPpB2AOzu" class="inline-onebox" rel="noopener nofollow ugc">Download Transformed_ROI_Test.zip | LimeWire</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3af80502b35cebdcda17906606036261ee55d872.png" data-download-href="/uploads/short-url/8pF4vIYePbm27MKBIK3WY3GDKb8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3af80502b35cebdcda17906606036261ee55d872.png" alt="image" data-base62-sha1="8pF4vIYePbm27MKBIK3WY3GDKb8" width="573" height="396"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">573×396 29.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Tested with Slicer 5.8.1 r33241 / 11eaf62</p>
<p>Keep up the great work!</p>
<p>Thanks and kind regards</p>

---

## Post #3 by @MMMPPPMMM (2025-07-26 18:30 UTC)

<p>Reupload of the example scene:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.transfernow.net/en/cld?utm_source=20250726eBwXRfaF">
  <header class="source">
      <img src="https://www.transfernow.net/favicon.ico" class="site-icon" alt="" width="48" height="48">

      <a href="https://www.transfernow.net/en/cld?utm_source=20250726eBwXRfaF" target="_blank" rel="noopener nofollow ugc">TransferNow</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/361;"><img src="https://www.transfernow.net/og-image/c2l6ZT02MTczNCZmaWxlQ291bnQ9MSZmaWxlbmFtZT1UcmFuc2Zvcm1lZF9ST0lfVGVzdC56aXAmbGFuZ0NvZGU9ZW4mZXhwaXJlRGF0ZT0yMDI1LTA4LTAyVDE4JTNBMjglM0E0Ni40OTJaJmJnQ29sb3I9JTIzRkZGRkZGJmFjdGlvbkNvbG9yPSUyMzNGNTFCNQ==.jpg?ts=1753554644111" class="thumbnail" alt="" width="690" height="362"></div>

<h3><a href="https://www.transfernow.net/en/cld?utm_source=20250726eBwXRfaF" target="_blank" rel="noopener nofollow ugc">Transformed_ROI_Test.zip is available for download</a></h3>

  <p>Click to access the Transformed_ROI_Test.zip (61.7 KB) download with TransferNow</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @pieper (2025-07-27 04:30 UTC)

<p>Thanks for the report and the reproducible example. What you describe sounds like an issue that should be tracked in the <a href="https://github.com/Slicer/Slicer/issues">github issue tracker</a><br>
rather than the forum so it won’t be lost as people do new releases, etc.</p>

---

## Post #5 by @MMMPPPMMM (2025-07-27 10:13 UTC)

<p>Thanks for the reply.</p>
<p>I’ve asked a friend to open an issue for me:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/8603">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/8603" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/8603" target="_blank" rel="noopener nofollow ugc">Transformed ROI shows up as changed in Save dialog directly after opening an mrml scene</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-07-27" data-time="10:12:32" data-timezone="UTC">10:12AM - 27 Jul 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/oqilipo" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/15254908?v=4" class="onebox-avatar-inline" width="20" height="20">
          oqilipo
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

I think it is a bug that a transformed ROI shows up as changed in Sa<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ve dialog directly after opening an MRML scene.


![](https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3af80502b35cebdcda17906606036261ee55d872.png)


## Steps to reproduce

Open the example scene:

[Transformed_ROI_Test.zip](https://github.com/user-attachments/files/21453265/Transformed_ROI_Test.zip)

## Environment
- Slicer version: Slicer 5.8.1 r33241 / 11eaf62
- Operating system: Windows 11 Pro 10.0.26100</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
