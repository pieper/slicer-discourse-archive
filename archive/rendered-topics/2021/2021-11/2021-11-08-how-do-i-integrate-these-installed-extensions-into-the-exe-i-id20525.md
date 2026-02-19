---
topic_id: 20525
title: "How Do I Integrate These Installed Extensions Into The Exe I"
date: 2021-11-08
url: https://discourse.slicer.org/t/20525
---

# How do I integrate these installed extensions into the EXE installation package?  

**Topic ID**: 20525
**Date**: 2021-11-08
**URL**: https://discourse.slicer.org/t/how-do-i-integrate-these-installed-extensions-into-the-exe-installation-package/20525

---

## Post #1 by @LuPingChina (2021-11-08 12:59 UTC)

<p>Operating system:Windows 10<br>
Slicer version:4.13<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Thank you 3D Slicer for providing such a handy medical imaging software.  I have trouble downloading extensions due to network problems. How do I integrate these installed extensions into the EXE installation package?</p>

---

## Post #2 by @lassoan (2021-11-08 20:17 UTC)

<p>This page describes how to download and install extensions without network connection: <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#install-extensions-without-network-connection" class="inline-onebox">Extensions Manager — 3D Slicer documentation</a></p>
<p>Unfortunately, there is an error in the current extensions manager website that breaks the download button:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5863">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5863" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5863" target="_blank" rel="noopener">Download button on Extensions Server does not work</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-09-15" data-time="13:46:20" data-timezone="UTC">01:46PM - 15 Sep 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          priority:high
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Cannot download extensions from the Extensions Server when using a regular web b<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">rowser.

## Steps to reproduce

- Open this page: https://extensions.slicer.org/catalog/All/30181/win?q=slicerigt
- Click the "Download" button -&gt; the button flashes but nothing happens.
- Click on the extension's icon to open the details page.
- Click the "Download" button -&gt; the button flashes but nothing happens.

## Expected behavior

Clicking "Download" should download the extension package.

## Environment
- Microsoft Edge, Google Chrome
- Operating system: Windows, Microsoft Edge browser</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Until the problem gets fixed you can go to the <a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/5f4474d0e1d8c75dfc705482">web user interface of the extensions server backend</a> and download the extensions you need from there. Extensions for Slicer Preview Releases are in the “draft” folder.</p>

---
