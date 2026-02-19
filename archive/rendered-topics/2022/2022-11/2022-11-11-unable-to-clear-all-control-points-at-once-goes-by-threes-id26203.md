---
topic_id: 26203
title: "Unable To Clear All Control Points At Once Goes By Threes"
date: 2022-11-11
url: https://discourse.slicer.org/t/26203
---

# Unable to clear all control points at once, goes by threes?

**Topic ID**: 26203
**Date**: 2022-11-11
**URL**: https://discourse.slicer.org/t/unable-to-clear-all-control-points-at-once-goes-by-threes/26203

---

## Post #1 by @Maria_Feiler (2022-11-11 20:00 UTC)

<p>I only just recent updated my 3DSlicer to 5.0.3, and I was very excited to start using the control point template feature. However. I have found that if I highlight all the fiducials and click the “Clear the position of highlighted control points” button, it does not clear them all. In fact, it clears all but every third landmark. Considering I am doing curve semilandmarks, it is incredibly inconvenient to scroll through and clear each third landmark manually. How do I fix this? Has anyone else encountered this?</p>

---

## Post #2 by @lassoan (2022-11-11 20:04 UTC)

<p>I was not able to reproduce this. Could you record your screen while you are doing it and post the video here? (if the video is longer then what is allowed to be posted then you can upload the file to dropbox, onedrive, google drive, etc. and post just the link here)</p>

---

## Post #3 by @Maria_Feiler (2022-11-11 20:16 UTC)

<p>I have also included the two files in question:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://accounts.google.com/v3/signin/identifier?dsh=S-66625528%3A1668197751655362&amp;continue=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1HPVpjUbTySUbCpIz2MXF_qv3q5Pzmrqf%3Fusp%3Dshare_link&amp;followup=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1HPVpjUbTySUbCpIz2MXF_qv3q5Pzmrqf%3Fusp%3Dshare_link&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=WebLiteSignIn&amp;flowEntry=ServiceLogin&amp;ifkv=ARgdvAs584iY3r4T_QkPIgWSZ4P8yArPlN_RN7kUffKemlLAbGtjkls8QWmj_qCamSqyUCo8aLKf2A">
  <header class="source">

      <a href="https://accounts.google.com/v3/signin/identifier?dsh=S-66625528%3A1668197751655362&amp;continue=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1HPVpjUbTySUbCpIz2MXF_qv3q5Pzmrqf%3Fusp%3Dshare_link&amp;followup=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1HPVpjUbTySUbCpIz2MXF_qv3q5Pzmrqf%3Fusp%3Dshare_link&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=WebLiteSignIn&amp;flowEntry=ServiceLogin&amp;ifkv=ARgdvAs584iY3r4T_QkPIgWSZ4P8yArPlN_RN7kUffKemlLAbGtjkls8QWmj_qCamSqyUCo8aLKf2A" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://accounts.google.com/v3/signin/identifier?dsh=S-66625528%3A1668197751655362&amp;continue=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1HPVpjUbTySUbCpIz2MXF_qv3q5Pzmrqf%3Fusp%3Dshare_link&amp;followup=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1HPVpjUbTySUbCpIz2MXF_qv3q5Pzmrqf%3Fusp%3Dshare_link&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=WebLiteSignIn&amp;flowEntry=ServiceLogin&amp;ifkv=ARgdvAs584iY3r4T_QkPIgWSZ4P8yArPlN_RN7kUffKemlLAbGtjkls8QWmj_qCamSqyUCo8aLKf2A" target="_blank" rel="noopener nofollow ugc">Google Drive: Sign-in</a></h3>

  <p>Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>EDIT: I apologize, I forgot to update the sharing settings. It’s fixed now.</p>

---

## Post #4 by @muratmaga (2022-11-11 21:27 UTC)

<aside class="quote no-group" data-username="Maria_Feiler" data-post="3" data-topic="26203">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/maria_feiler/48/17300_2.png" class="avatar"> Maria_Feiler:</div>
<blockquote>
<p>I have also included the two files in question:</p>
</blockquote>
</aside>
<p>Sorry, I can’t reproduce this behavior with the same version either. If you restart your Slicer session, does the behavior persist?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16190aa59674aa86d026320b852fe03b28845816.png" data-download-href="/uploads/short-url/39u9ExopxllSiPrKSPNyBfLUv0a.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16190aa59674aa86d026320b852fe03b28845816_2_690x252.png" alt="image" data-base62-sha1="39u9ExopxllSiPrKSPNyBfLUv0a" width="690" height="252" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16190aa59674aa86d026320b852fe03b28845816_2_690x252.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16190aa59674aa86d026320b852fe03b28845816_2_1035x378.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16190aa59674aa86d026320b852fe03b28845816.png 2x" data-dominant-color="719ECC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1081×396 26.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @jamesobutler (2022-11-11 21:35 UTC)

<p>I was able to replicate this issue with Slicer 5.0.3 by following the video. It happens specifically when the “Coordinates” option is set to “Hide”. The issue does not occur when the “Coordinates” option is something like “World”.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3ce718ace1827ea2b3993397fd47f7d2530404ea.png" alt="image" data-base62-sha1="8GLLJHKHplYsfXl7ehlWjD8z62e" width="471" height="282"></p>

---

## Post #6 by @muratmaga (2022-11-11 21:46 UTC)

<p>Ok thanks. yes, I can replicate with hidden coordinates even with a preview build. So it is still there.</p>
<p><a class="mention" href="/u/maria_feiler">@Maria_Feiler</a> meanwhile (until this is fixed in a new version), if you just display coordinates it will work as intended.</p>

---

## Post #7 by @Maria_Feiler (2022-11-11 21:47 UTC)

<p>Thank you, everyone! I appreciate all your effort.</p>

---

## Post #8 by @lassoan (2022-11-11 22:29 UTC)

<p>Could someone please add an issue to the bugtracker to make sure we address this? We’ll need to rework the control point list widget to become a standalone, reusable widget (like the simple markups widget) and as part of that work well address this issue, too.</p>

---

## Post #9 by @Maria_Feiler (2022-11-11 22:41 UTC)

<p>I can add it. I’ll include my video as well as a video showing it’s fix.</p>

---

## Post #10 by @jamesobutler (2022-11-12 18:01 UTC)

<p>I’ve issued a PR with an attempted fix:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6657">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6657" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6657" target="_blank" rel="noopener nofollow ugc">BUG: Fix control point state not updated with hidden coordinates</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>jamesobutler:control-point-state-skipped-update</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2022-11-12" data-time="18:00:53" data-timezone="UTC">06:00PM - 12 Nov 22 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
            <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
            jamesobutler
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 19 additions and 15 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6657/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+19</span>
            <span class="removed">-15</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Originally mentioned in https://discourse.slicer.org/t/unable-to-clear-all-contr<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6657" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ol-points-at-once-goes-by-threes/26203.

An incorrect selected item increment was using the number of total columns to skip when finding the next selected row and this was incorrect when columns were hidden. Selected Items only include the visible selections so each row would only have 6 selected items when coordinates were hidden instead of 9 items when coordinates were shown.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
