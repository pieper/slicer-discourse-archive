---
topic_id: 766
title: "Updated Slicer Binary Automatic Notification"
date: 2017-07-25
url: https://discourse.slicer.org/t/766
---

# Updated Slicer binary automatic notification

**Topic ID**: 766
**Date**: 2017-07-25
**URL**: https://discourse.slicer.org/t/updated-slicer-binary-automatic-notification/766

---

## Post #1 by @fedorov (2017-07-25 20:20 UTC)

<p>Please add <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> to this post if you think it would be helpful for the Slicer application to automatically query the central server for the availability of an updated binary, and automatically notify the user.</p>
<p>I am also using ITK-Snap, and just discovered that (similar to virtually all modern applications these days) it has this feature (although it just points to the download page and the user needs to install the update manually).</p>
<p>It would be great to hear other users’ thoughts on this feature.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/6a956251f5f0566b2b63ff4f51ac2fca586c4273.jpg" data-download-href="/uploads/short-url/fcSFh85S2qjurmd5Ss6FSOsvoeD.jpg?dl=1" title="image.jpg"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6a956251f5f0566b2b63ff4f51ac2fca586c4273_2_592x500.jpg" width="592" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6a956251f5f0566b2b63ff4f51ac2fca586c4273_2_592x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a956251f5f0566b2b63ff4f51ac2fca586c4273.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a956251f5f0566b2b63ff4f51ac2fca586c4273.jpeg 2x" data-dominant-color="E3E7E8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">855×722 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2017-07-25 20:39 UTC)

<p>We have also discussed in the past that a by-product of checking for updates at startup time is that the server can log how many times the check is performed, thereby giving us an estimate of how often the program is being run.  We could also track things like what extensions are installed, what OS is being used, etc.</p>
<p>Would anyone object if this kind of tracking was enabled by default?  Should it have an opt-out option for privacy?</p>

---

## Post #3 by @lassoan (2017-07-26 01:00 UTC)

<p>I would not object if allowing storage of update query logs was enabled by default. Google has already convinced me a long time ago that I should hand over all kinds of information in return for free stuff - this would not be different (other than that we don’t look for profit).</p>
<p>I don’t like those update notifications that just open my web browser, but they are very easy to implement, and certainly better than nothing.</p>
<p>I guess the automatic update would be only for stable releases - so we would have one more reason to make stable releases more frequently.</p>

---

## Post #4 by @muratmaga (2017-07-26 01:42 UTC)

<p>+1 Auto update notification, but won’t make sense for nightlies.</p>
<p>As a user, I don’t mind tracking by Slicer. I know the people, I trust the community. However, if you go down that road, please make it clear during the installation with a little bit of justification (to inform users that may not be part of the active community why you are doing it and what you are collecting. Funding being the primary reason).</p>
<p>Keep the default option as opt-in, let the user know about and decide for themselves. You really don’t want to force people or do it behind their back. It is a piece of information you are currently not collecting and any additional information you are going to get will be icing on the cake. Maybe even consider making what you are collecting publicly available…</p>
<p>My two cents.<br>
M</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/677f06bdf711468707faf594c72c7993f90d2513.png" data-download-href="/uploads/short-url/eLzkAGZovUCazoJL65K1uagmWFJ.png?dl=1" title="77C3A3DB5AF54B56A741600A3E5A8000.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/677f06bdf711468707faf594c72c7993f90d2513.png" width="690" height="0" data-dominant-color="BFCDDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">77C3A3DB5AF54B56A741600A3E5A8000.png</span><span class="informations">708×1 83 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2021-03-04 14:11 UTC)

<p>See some more discussion here:</p>
<aside class="quote quote-modified" data-post="5" data-topic="16341">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/snapshot-release-updates-and-user-notification/16341/5">Snapshot release updates and user notification</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I’m sure there are users on both ends of the spectrum of whether they think the telemetry provides helpful benefits or think it is spying. 
My impression is most users want Slicer to “just work” so alerting of the latest version of the application or extension with bug fixes would be appreciated. I would be fine if it is transparent what type of data is being collected and having some form of auto-check being the default enabled so they have to opt-out instead of opt-in. The option to opt-out sh…
  </blockquote>
</aside>

<p>Feature request in the issue tracker here:</p>
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

## Post #6 by @lassoan (2022-09-18 04:42 UTC)

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

## Post #7 by @lassoan (2023-03-21 02:15 UTC)



---
