---
topic_id: 16341
title: "Snapshot Release Updates And User Notification"
date: 2021-03-03
url: https://discourse.slicer.org/t/16341
---

# Snapshot release updates and user notification

**Topic ID**: 16341
**Date**: 2021-03-03
**URL**: https://discourse.slicer.org/t/snapshot-release-updates-and-user-notification/16341

---

## Post #1 by @muratmaga (2021-03-03 18:09 UTC)

<p>Quick question about what happens to the previous snapshot release after a new one is released? For example would the extensions to the previous one (202009) will continue to be updated?</p>
<p>If not, we might have to consider letting the people know that there is a newer stable release (as oppose to they pro-actively do so by clicking on Help-&gt;About Slicer-&gt;Download a newer version. I bet most people is not even aware of that.). Perhaps auto check Slicer stable releases monthly at the startup and just let users know.</p>

---

## Post #2 by @lassoan (2021-03-03 18:56 UTC)

<p>Extensions are only built/updated for the latest stable and preview (not for Slicer-4.11.20200930).</p>
<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="16341">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Perhaps auto check Slicer stable releases monthly at the startup and just let users know.</p>
</blockquote>
</aside>
<p>It would be nice to implement automatic update checks. It could also give us a better idea who uses Slicer, which version, and how often. I’ve added a feature request to track this task:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5502">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5502" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5502" target="_blank" rel="noopener">Add automatic application update notification</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-03-03" data-time="18:55:00" data-timezone="UTC">06:55PM - 03 Mar 21 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2022-09-19" data-time="16:41:28" data-timezone="UTC">04:41PM - 19 Sep 22 UTC</span>
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
          Type: Enhancement
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

## Post #3 by @muratmaga (2021-03-03 19:13 UTC)

<p>As a user, I am not fond of extensive telemetry (particularly if we are not going to act on that data). But some automated way of comparing release numbers, and popping up an informative message that says something like:</p>
<p>“A new stable version is available. Your version is no longer kept up to date for extensions. Would you like download and install this version?”</p>
<p>would be good for user experience. We still occasionally met people on forum who are using version 4.8.</p>

---

## Post #4 by @lassoan (2021-03-03 19:19 UTC)

<p>As a user I’m not fond of (mostly I don’t care about) telemetry, but as a developer you know how useful it is. I think this is very little to ask, but of course users could opt out of update checks.</p>

---

## Post #5 by @jamesobutler (2021-03-03 20:47 UTC)

<p>I’m sure there are users on both ends of the spectrum of whether they think the telemetry provides helpful benefits or think it is spying.</p>
<p>My impression is most users want Slicer to “just work” so alerting of the latest version of the application or extension with bug fixes would be appreciated. I would be fine if it is transparent what type of data is being collected and having some form of auto-check being the default enabled so they have to opt-out instead of opt-in. The option to opt-out should be clear and easy to find. If it is really desired to be opt-in I would suggest on first startup after install of Slicer to pop-up warning on start to force them to explicitly define the setting of whether they want to turn on automatic checking or to have it off (with the ability to turn on/off later supported in settings).</p>
<p>For reference here are setting options for Visual Studio Code as it relates to update checks for the application and its extensions.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f4e4f71bef26f35867e82b6de8e0e9c494be753.png" data-download-href="/uploads/short-url/921RiRlKgRPcsMtv4yQ1l5eGV7d.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f4e4f71bef26f35867e82b6de8e0e9c494be753.png" alt="image" data-base62-sha1="921RiRlKgRPcsMtv4yQ1l5eGV7d" width="690" height="265" data-dominant-color="2D2E30"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">804×309 15.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0efc9a27340841b401df63035e985fc39c6a9ceb.png" data-download-href="/uploads/short-url/28zSHfDc3wRAgcB2whouVsNHBk7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0efc9a27340841b401df63035e985fc39c6a9ceb.png" alt="image" data-base62-sha1="28zSHfDc3wRAgcB2whouVsNHBk7" width="690" height="155" data-dominant-color="292929"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">818×184 11.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @pieper (2021-03-03 20:52 UTC)

<p>I agree that most users are probably fine with update checks and fine with it being turned on by default (with a warning dialog on first install).</p>

---

## Post #7 by @muratmaga (2021-03-04 00:21 UTC)

<p>I agree, this is very acceptable… Particularly you get the benefit of getting notifications.</p>

---

## Post #8 by @fedorov (2021-03-04 14:02 UTC)

<p>Related discussion from a while ago: <a href="https://discourse.slicer.org/t/updated-slicer-binary-automatic-notification/766" class="inline-onebox">Updated Slicer binary automatic notification</a></p>

---

## Post #9 by @lassoan (2022-09-18 04:42 UTC)

<p>A pull request has just been submitted that implements this feature. Feedback is welcome (by commenting on the pull request).</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6537">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6537" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/6537" target="_blank" rel="noopener">Add check for available application updates</a>
    </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:app-update-check</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-09-18" data-time="04:38:23" data-timezone="UTC">04:38AM - 18 Sep 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="3 commits changed 34 files with 1581 additions and 180 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/6537/files" target="_blank" rel="noopener">
          <span class="added">+1581</span>
          <span class="removed">-180</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Now that a new Slicer Stable Releases is planned to be created in every quarter,<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6537" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> but extensions are only updated for the latest stable, it is important to keep moving users to the latest Slicer version.

This commit adds an application update check to make users aware that a more recent Slicer Stable Release is available that the currently running Slicer.

Automatic update check is enabled by default. It can be enabled/disabled in the Welcome module and in Application Settings.
Update check can be initiated manually in the Welcome module.

Application updates can be completely disabled using Slicer_BUILD_APPLICATIONUPDATE_SUPPORT CMake variable, or can be temporarily disabled in Slicer.ini (ApplicationUpdates/Enabled=false).

fixes #5502

![image](https://user-images.githubusercontent.com/307929/190885899-7fec7678-66d5-4fee-ae3d-076e624068b5.png)

![image](https://user-images.githubusercontent.com/307929/190886013-6cfe43d7-a671-4614-88f7-c11a6f7055da.png)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
