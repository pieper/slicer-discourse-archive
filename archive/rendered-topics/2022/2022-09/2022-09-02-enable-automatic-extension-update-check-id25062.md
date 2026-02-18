# Enable automatic extension update check?

**Topic ID**: 25062
**Date**: 2022-09-02
**URL**: https://discourse.slicer.org/t/enable-automatic-extension-update-check/25062

---

## Post #1 by @lassoan (2022-09-02 22:57 UTC)

<p><a href="https://discourse.slicer.org/t/new-feature-automatic-update-of-extensions/24416">Automatic extension update check</a> works really well in Slicer-5.0.3, but since it is not enabled by default and the settings is quite hidden in the extensions manager (see the image below) probably many users are not aware that this very useful feature exists.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56f78d4c425ac8bfc235218f9cdd0e02816e0143.png" data-download-href="/uploads/short-url/cplrhziaD21CC3IRiAG3PDaXqrF.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56f78d4c425ac8bfc235218f9cdd0e02816e0143_2_690x153.png" alt="image" data-base62-sha1="cplrhziaD21CC3IRiAG3PDaXqrF" width="690" height="153" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56f78d4c425ac8bfc235218f9cdd0e02816e0143_2_690x153.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56f78d4c425ac8bfc235218f9cdd0e02816e0143_2_1035x229.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56f78d4c425ac8bfc235218f9cdd0e02816e0143_2_1380x306.png 2x" data-dominant-color="4B4E50"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1802×402 48.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>We should make this feature enabled by default, but since it would mean that Slicer contacts a server regularly (once a day by default), we should probably ask consent from the user.</p>
<p>Does anyone have a suggestion for the text that we should ask from users?<br>
Are there any other suggestions related to auto-update?</p>

---

## Post #2 by @pieper (2022-09-03 17:44 UTC)

<p>I was thinking this kind of option should go in the Welcome module along with an option to check for updates to the app itself.  I think having a single option for both the application and extensions would be more logical and simpler.  Also the status would be visible to the user every time the application starts as long as the Welcome module was their home, which I guess most people never change.</p>
<p>The text could be something like: “Automatically check for updates to the application and installed extensions.  Note that anonymized usage statistics will be recorded.”</p>
<p>Having this enabled by default is fine with me since all OSes, even ubuntu, have auto update checks on by default.  Even venerable open source apps like vim have it enabled by default too, and the checkbox is hidden in the preference dialog.  Anyone who is particularly concerned is no doubt used to looking for ways to disable these features.</p>
<p>I would hesitate to add another dialog at startup since we already have the clinical use warning and we don’t really want to detract from that.</p>

---

## Post #3 by @lassoan (2022-09-06 00:41 UTC)

<p>Thanks for the suggestions, these sound good to me.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> how could we detect that a new Slicer Stable Release is available?</p>

---

## Post #4 by @lassoan (2022-09-07 15:24 UTC)

<p>How does this look?</p>
<p>Automatic update is disabled, the button can be clicked for a one-time update check:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/459c008c3bcce1d433e7abb5dff10f5d370754d4.png" data-download-href="/uploads/short-url/9VNb4avvtv6pPuZnTEDf3EGqt9y.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/459c008c3bcce1d433e7abb5dff10f5d370754d4.png" alt="image" data-base62-sha1="9VNb4avvtv6pPuZnTEDf3EGqt9y" width="400" height="500" data-dominant-color="F0F0F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">446×557 29 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Update is found:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1d5f387594d00412746dc960e0093a904061019.png" alt="image" data-base62-sha1="tWib9hTRsTucV2EXhZwUjmcbi1H" width="464" height="224"></p>
<p>Automatic update is enabled:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a92552d29cebfa8a9dc80c3c1ec1b20b1a0d6524.png" alt="image" data-base62-sha1="o8kEMyffbxSRH5gLEzpdqebuw6M" width="445" height="231"></p>

---

## Post #5 by @lassoan (2022-09-08 03:45 UTC)

<p>This enhancement has been <a href="https://github.com/Slicer/Slicer/pull/6520">integrated into Slicer Preview Release (PR-6520)</a> and will be available for download from 2022-09-09.</p>

---

## Post #6 by @rbumm (2022-09-08 18:25 UTC)

<p>Thank you, <a class="mention" href="/u/lassoan">@lassoan</a>, looking forward to this. Will it even detect when a new stable is available?</p>

---

## Post #7 by @lassoan (2022-09-08 18:32 UTC)

<p>Currently we only check for extension updates. However, now that we are increasing the frequency of application updates (the goal is to have a new stable release every quarter) it is becoming more important to check for application updates, too. I’m not sure that this update check will fit into Slicer-5.2, it mainly depends when the server API will be ready. The task is tracked in this issue:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5502">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5502" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5502" target="_blank" rel="noopener">Add automatic application update notification</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-03-03" data-time="18:55:00" data-timezone="UTC">06:55PM - 03 Mar 21 UTC</span>
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
          type:enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Is your feature request related to a problem? Please describe.

We are tryi<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ng to move towards releasing a new stable version quarterly. However, users may not be aware that a new Slicer core is available. Users also stop getting extension updates if they are not using the latest stable release.

## Describe the solution you'd like

Implement a mechanism that checks if a new version of Slicer is available. The server that queries for new Slicer versions could also collect some statistics about which Slicer versions are used and how often.

## Additional context

https://discourse.slicer.org/t/updated-slicer-binary-automatic-notification/766
https://discourse.slicer.org/t/snapshot-release-updates-and-user-notification/16341</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
