---
topic_id: 46308
title: "Install Modalityconverter"
date: 2026-02-26
url: https://discourse.slicer.org/t/46308
---

# Install ModalityConverter

**Topic ID**: 46308
**Date**: 2026-02-26
**URL**: https://discourse.slicer.org/t/install-modalityconverter/46308

---

## Post #1 by @jmarichal (2026-02-26 19:26 UTC)

<p>Hi,</p>
<p>New user here! I’m trying to download the ModalityConverter extension: <a href="https://github.com/ciroraggio/SlicerModalityConverter" rel="noopener nofollow ugc">GitHub - ciroraggio/SlicerModalityConverter</a>.</p>
<p>When trying via the extension manager, I got the following error message. So I went on <a href="http://extensions.slicer.org" rel="noopener nofollow ugc">extensions.slicer.org</a> in order to do a manual installation (for Windows), but I can’t find the module. It’s supposed to be under the ‘Image Synthesis’ category, which isn’t present either. Did anyone experience a similar issue?</p>
<p>Thanks for the help!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44da32bf99b63c2121f46eddd2d55a5876c911d3.png" data-download-href="/uploads/short-url/9P5Xf9ACSPVwl8A9TLXclsdPmHp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44da32bf99b63c2121f46eddd2d55a5876c911d3.png" alt="image" data-base62-sha1="9P5Xf9ACSPVwl8A9TLXclsdPmHp" width="366" height="204"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">366×204 6.31 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ced82cc01a6a6bd0f40c359ea053fc541dc72d58.jpeg" data-download-href="/uploads/short-url/tvPvHqQ7P6tUcHujJNIlcCbmGJa.jpeg?dl=1" title="image-1772099183208-sa6t4xifs" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ced82cc01a6a6bd0f40c359ea053fc541dc72d58_2_690x370.jpeg" alt="image-1772099183208-sa6t4xifs" data-base62-sha1="tvPvHqQ7P6tUcHujJNIlcCbmGJa" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ced82cc01a6a6bd0f40c359ea053fc541dc72d58_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ced82cc01a6a6bd0f40c359ea053fc541dc72d58_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ced82cc01a6a6bd0f40c359ea053fc541dc72d58_2_1380x740.jpeg 2x" data-dominant-color="E0E4E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image-1772099183208-sa6t4xifs</span><span class="informations">1917×1030 338 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ciro.raggio (2026-02-26 19:47 UTC)

<p>Hello, thank you for writing. May I ask which version of 3D Slicer you are trying to download the extension from?</p>
<p>ModalityConverter can only be downloaded from the Extension Manager from version Slicer 5.9 onwards. I don’t understand what the error is, but it seems more like a download problem than an extension problem.</p>
<p>If you can’t find the extension with Slicer version higher than 5.9, then you can clone the repository and import it manually!</p>
<p>Let me know if you can do it, otherwise I’ll guide you step by step. <img src="https://emoji.discourse-cdn.com/twitter/grinning_face.png?v=15" title=":grinning_face:" class="emoji" alt=":grinning_face:" loading="lazy" width="20" height="20"></p>

---

## Post #3 by @jamesobutler (2026-02-26 19:57 UTC)

<p>I suspect the download failed because of Zscaler:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/8815">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/8815" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/8815" target="_blank" rel="noopener nofollow ugc">Zscaler Ceertificate Issue</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-11-04" data-time="15:23:49" data-timezone="UTC">03:23PM - 04 Nov 25 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2025-11-04" data-time="19:56:54" data-timezone="UTC">07:56PM - 04 Nov 25 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/sahikabetul" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/54595314?v=4" class="onebox-avatar-inline" width="20" height="20">
          sahikabetul
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

When trying to install new extensions, the download fails. I am runn<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ing Zscaler Internet Security on my device.
This software acts as a Firewall for all web traffic. The logs indicate a SSL inspection error, likely the result
of an untrusted certificate.
 
Does 3D slicer support intermediate certificate to be pinned, and if so what trust store does 3D slicer pull its
certificates from? (i.e Java, Python, ect.)

&lt;img width="329" height="347" alt="Image" src="https://github.com/user-attachments/assets/45bf35f1-3ba7-4a91-a040-233e86aca407" /&gt;

## Environment
- Slicer version: Slicer-5.6.2
- Operating system:  Mac 15.7.1</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It’s an issue that affects me as well with my company issued computer.</p>

---
