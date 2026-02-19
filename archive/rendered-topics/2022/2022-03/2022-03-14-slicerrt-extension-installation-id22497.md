---
topic_id: 22497
title: "Slicerrt Extension Installation"
date: 2022-03-14
url: https://discourse.slicer.org/t/22497
---

# SlicerRT extension installation

**Topic ID**: 22497
**Date**: 2022-03-14
**URL**: https://discourse.slicer.org/t/slicerrt-extension-installation/22497

---

## Post #1 by @Yarden (2022-03-14 15:58 UTC)

<p>Hi,<br>
I wanted to install the slicerRT extension but the extension tab seems empty. Tried to solve it with no success.<br>
I saw there is an option to add an extension file externally so i could upload it to 3d slicer as an archive file.</p>
<p>Is there a file for this extension to download? Or any other advices…?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2022-03-14 16:16 UTC)

<p>SlicerRT extension is currently not available for latest Slicer Preview Release on Linux and macOS due to a build error. A fix is in the works, the extension should be available again within 1-2 days:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/SlicerRt/SlicerRT/pull/207">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/pull/207" target="_blank" rel="noopener">github.com/SlicerRt/SlicerRT</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerRt/SlicerRT/pull/207" target="_blank" rel="noopener">ENH: Temporary fix of compilation error after ITK-5.3 update</a>
    </h4>

    <div class="branches">
      <code>SlicerRt:master</code> ← <code>MichaelColonel:temp-itk5.3-fix</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-02-26" data-time="11:22:41" data-timezone="UTC">11:22AM - 26 Feb 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/MichaelColonel" target="_blank" rel="noopener">
          <img alt="MichaelColonel" src="https://avatars.githubusercontent.com/u/3785912?v=4" class="onebox-avatar-inline" width="20" height="20">
          MichaelColonel
        </a>
      </div>

      <div class="lines" title="1 commits changed 2 files with 29 additions and 0 deletions">
        <a href="https://github.com/SlicerRt/SlicerRT/pull/207/files" target="_blank" rel="noopener">
          <span class="added">+29</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Plastimatch [PR](https://gitlab.com/plastimatch/plastimatch/-/merge_requests/29)<span class="show-more-container"><a href="https://github.com/SlicerRt/SlicerRT/pull/207" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> must be merged before this PR.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Yarden (2022-03-15 13:15 UTC)

<p>Thanks for your reply.<br>
I’m on Windows. I downloaded the master from the link you sent and tried to upload the zip as an external archive file but got the error message “no extension description found in archive…”<br>
I’ll be happy to know how to upload the zip OR to solve the issue with the install extensions that is empty. Or if there is another way to succeed in installing the slicerRT extension…</p>
<p>Thanks!</p>

---

## Post #4 by @Mik (2022-03-15 17:32 UTC)

<p>Try to install recent Slicer Preview. SlicerRT extension should be available to install from extension browser.</p>

---

## Post #5 by @Yarden (2022-03-16 13:15 UTC)

<p>I have the latest stable release 4.11.20210226.<br>
Should it work on the preview release 4.13.0? I saw in another post that this version also has this problem that the extension browser is empty…</p>

---

## Post #6 by @Mik (2022-03-16 13:38 UTC)

<p>Please, download the latest preview release-4.13.0, for example 2022-03-15.</p>

---

## Post #7 by @Yarden (2022-03-21 14:35 UTC)

<p>Thanks!<br>
The problem was that my network at work block some websites. In the 4.13.0 release there was an option to allow anyways, and then I could see all the extensions to download.</p>

---
