---
topic_id: 23655
title: "Stable Update Notification"
date: 2022-05-31
url: https://discourse.slicer.org/t/23655
---

# Stable update notification

**Topic ID**: 23655
**Date**: 2022-05-31
**URL**: https://discourse.slicer.org/t/stable-update-notification/23655

---

## Post #1 by @muratmaga (2022-05-31 17:17 UTC)

<p>I brought his up earlier on the forum. For stable releases, we need to have a mechanism that will check whether a newer stable version is available and if so, notify the people (with an option to disable that check).</p>
<p>I suspect there are a lot of people who are using the older stable (4.11) and are not aware that a new stable is released, unless they are actively tracking the Slicer community. Or likewise there will be a new patch release of the stable (as I understood) soon, and people who are using 5.0.2 (current version), will not be notified of this.</p>

---

## Post #2 by @jamesobutler (2022-05-31 19:26 UTC)

<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5502">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5502" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5502" target="_blank" rel="noopener nofollow ugc">Add automatic application update notification</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-03-03" data-time="18:55:00" data-timezone="UTC">06:55PM - 03 Mar 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
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

<p>^ It’s an issue being tracked and currently in the Slicer 5.1 milestone. It’s not going to be something for this Slicer 5.0.x release, but maybe for a future feature release. Slicer 5.0.x announcements will have to come from the community announcement which is one of the last steps to the <a href="https://github.com/Slicer/Slicer/issues/6337" rel="noopener nofollow ugc">release process</a> which hasn’t been completed yet.</p>
<p>That issue was created around the time of whether to alert users automatically if there are updates available for extensions (not auto-updating, but alerting users of new versions of extensions). Currently checks for extension updates is a manual triggered action. <a href="https://github.com/Slicer/Slicer/issues/5470#issuecomment-781613400" class="inline-onebox" rel="noopener nofollow ugc">Add "Update Extension" option under Manage Extensions · Issue #5470 · Slicer/Slicer · GitHub</a></p>

---

## Post #3 by @pieper (2022-05-31 20:30 UTC)

<p>Does anyone want to chine in on whether checking for updates should be on by default or only if a user opts in?  Maybe there’s should be a dialog box the first time you run slicer on a new machine asking for preference? (extra dialogs at start are annoying too of course).</p>

---

## Post #4 by @muratmaga (2022-05-31 20:38 UTC)

<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="23655">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Does anyone want to chine in on whether checking for updates should be on by default or only if a user opts in?</p>
</blockquote>
</aside>
<p>Checking for Updates for extension or releases?</p>
<p>Either, i would prefer it enabled, but when the message is displayed (i.e there is na update), offer to turn update check off.</p>
<p>That way it is up to the user about Not getting notified.</p>

---

## Post #5 by @pieper (2022-05-31 21:00 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="23655">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Checking for Updates for extension or releases?</p>
</blockquote>
</aside>
<p>Checking for extension updates currently happens when you go to the extension manager, which is itself a network operation, so no user approval is really required.  Checking for updates of the application at startup would allow us to track how many times the software is used, which would be useful for us, but some people might consider it a privacy issue (although I’m sure other software does it all the time and people don’t seem to care much anymore).  I was wondering if anyone feels strongly one way or the other how we approach this.</p>

---

## Post #6 by @jamesobutler (2022-05-31 23:28 UTC)

<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="23655">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>checking for updates should be on by default or only if a user opts in?</p>
</blockquote>
</aside>
<p>Based on this <a href="https://github.com/Slicer/Slicer/issues/5502#issuecomment-842400963" rel="noopener nofollow ugc">comment</a>, it would need to be opt-in.</p>
<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="23655">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Maybe there’s should be a dialog box the first time you run slicer on a new machine asking for preference?</p>
</blockquote>
</aside>
<p>I’ll provide information below about my current implementation to serve as ideas for Slicer.</p>
<p>I currently have support for auto version checking for my Slicer custom app by checking a release notes file on the web and comparing the latest version with version of my custom app being run. The update selection is saved as a user setting (False/True or missing if deferred decision by pressing “Cancel”). They can manually check with an action in the menu bar at Help-&gt;Check For Updates.</p>
<pre><code class="lang-auto">[Application]
auto_version_check=False
last_update_check=2022-05-31 18:58:54.201097
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff2a3dd60e63531429d0aeb52265284808865632.png" alt="image" data-base62-sha1="ApifW9dw4VqbH2lgdCNx2gaEq5Q" width="409" height="110"></p>
<p>If the user has selected “Manual”, I’m a little bit annoying and I will display a message on the status bar if they haven’t manually checked for a new version in the past 30 days. See code below.</p>
<pre data-code-wrap="python"><code class="lang-python">long_number_days_since_last_check = 30
if time_since_last_check &gt; timedelta(days=long_number_days_since_last_check):
    message = f"It has been over {long_number_days_since_last_check} days since the last check for a version update. Please go to Help-&gt;Check For Updates."
    slicer.util.mainWindow().statusBar().showMessage(message, 30000)  # shown for 30 seconds before cleared
</code></pre>
<p>If there is a update available I show release notes for all versions between the current version and the latest version available.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/105a2c455e2f8d0c3ddb005ee9384d316ecff87e.png" alt="image" data-base62-sha1="2kEPIsnEvwq7t9KLLNgpuwqRHIO" width="502" height="362"></p>
<p>I allow the user to “Ignore” the version update (saved as a user setting) if they don’t care about the update (often minor bug fix releases) and if they have “automatic” check mode turned on, then they will only be alerted of the next available release.</p>
<pre><code class="lang-auto">[Application]
ignore_version=1.13.1
</code></pre>
<p>They can use the “Download” button to automatically download the installer, close the current instance, and run the installer.</p>

---

## Post #7 by @pieper (2022-06-01 00:01 UTC)

<p>Thanks <a class="mention" href="/u/jamesobutler">@jamesobutler</a> that behavior sounds pretty reasonable to me.</p>

---

## Post #8 by @muratmaga (2022-06-01 01:18 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="6" data-topic="23655">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Based on this <a href="https://github.com/Slicer/Slicer/issues/5502#issuecomment-842400963">comment</a>, it would need to be opt-in.</p>
</blockquote>
</aside>
<p>I think there is a huge difference in terms privacy between going to a website and comparing a revision number and reporting to user that there is an update, vs doing telemetry on their usage habits.</p>
<p>A silent change (that is opt-in behavior) like this will defeat its primary purpose, which is to bring unengaged users more up-to-date with Slicer. First they have to know that’s an option.</p>

---

## Post #9 by @jamesobutler (2022-06-01 02:03 UTC)

<p>The pop-up I described that asks the user to opt-in does not seem to be a silent option and seems to be a very respectful option with clear transparency.</p>

---

## Post #10 by @muratmaga (2022-06-01 03:06 UTC)

<p>This is fine if it is executed right after the first run.</p>

---

## Post #11 by @pieper (2022-06-01 14:07 UTC)

<p>Yes, or maybe after a few runs, with a message like “You’ve used Slicer 10 times now and we hope you are enjoying it.  If you want to have Slicer automatically check for updates, click Ok.”.  This way it wouldn’t be in your face the first time you start the app (we already have the ‘not for clinical use’ dialog).</p>
<p>Another option could be to check the date, and if the version is more than 6 months old offer to check for updates and/or turn on auto update check.</p>

---

## Post #12 by @muratmaga (2022-06-01 15:23 UTC)

<aside class="quote no-group" data-username="pieper" data-post="11" data-topic="23655">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Yes, or maybe after a few runs, with a message like “You’ve used Slicer 10 times now and we hope you are enjoying it. If you want to have Slicer automatically check for updates, click Ok.”. This way it wouldn’t be in your face the first time you start the app (we already have the ‘not for clinical use’ dialog).</p>
</blockquote>
</aside>
<p>If we are going to be this verbose, I suggest making it clear in the message why staying up-to-date is important. May be something like “Extensions can only be updated for the latest stable release.”</p>

---

## Post #13 by @jamesobutler (2022-06-01 16:38 UTC)

<p>I would discourage any update notifications for Slicer Preview builds. We can’t be certain that the latest preview build is a better working option than the current Slicer Preview that a user may be using as there are periods of instability as various dependencies get updated. Then there would be no need for a statement like “Extensions can only be updated for the latest stable release” because there would not be any update notifications for Preview builds.</p>

---

## Post #14 by @rbumm (2022-06-01 17:12 UTC)

<p>Good topic, maybe we could put an update message on the welcome screen only if new stable builds are available:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e73f8ca9a9c0222246fd1ee5d27295d6eb3aeb85.png" alt="image" data-base62-sha1="wZIrSVhGx9KKeBykRO7SVZjKu2N" width="542" height="353"></p>
<p>Update notification dialog boxes are quite aggressive and may be disabled soon ? The click should download the new version, ideally with all previously loaded and matching extensions, and restart Slicer <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #15 by @muratmaga (2022-06-01 17:33 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="13" data-topic="23655">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I would discourage any update notifications for Slicer Preview builds</p>
</blockquote>
</aside>
<p>I agree, everything I said is in context of Stable release.</p>

---

## Post #16 by @pieper (2022-06-01 18:16 UTC)

<p>+1 for the idea of putting something on the welcome screen.  Not too subtle or it could be missed, but better not to have a dialog.</p>

---

## Post #17 by @lassoan (2022-06-06 12:27 UTC)

<p>I agree that these are great ideas!</p>
<ul>
<li>offer enabling auto-update in the welcome dialog and whenever doing manual update</li>
<li>slightly nudge the users to enable auto-update by displaying a “check for updates” button in Welcome module or in the status bar after every month or so</li>
<li>show what has changed since the running Slicer version and the latest Slicer version</li>
<li>allow the user to ignore specific application releases</li>
<li>explain why it is important to update (Slicer is constantly improved)</li>
<li>explain why statistics are computed from application and extension download count and location (demonstrating impact helps us getting grant funding; knowing which extensions are used helps us prioritizing developments)</li>
</ul>
<p>I’m working on implementing robust and quick auto-update check and auto-install is updates for extensions. It’ll be ready in a few days. Auto-update of application version could be done at the same time as extension auto-update and could be controlled by the same opt-in for switch.</p>

---

## Post #18 by @lassoan (2022-09-18 04:43 UTC)

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

## Post #19 by @lassoan (2022-09-19 16:13 UTC)

<p>Application update notification feature has been integrated in the latest Slicer Preview Release. It will be included in Slicer-5.2 stable release and the update notification will be visible to users when Slicer-5.4 stable release is published.</p>
<p>We discussed in the pull request how the application update mechanism could be further improved in the future. I include this here as a starting point for further discussions:</p>
<p>from <a class="mention" href="/u/jamesobutler">@jamesobutler</a>:</p>
<blockquote>
<p>For an application update notification I think in other programs I’m alerted more upfront with a pop-up dialog on application start? I think like TortoiseGit will do that and some others.</p>
<p>It makes sense to not do that for extension updates but I think more in your face for an application update would be desired. This would be in addition to the button in the Welcome module. The Welcome module button on its own it’s not large and in your face and could be easy to miss and we don’t want users to miss updating to the latest application version.</p>
</blockquote>
<blockquote>
<p>I wonder if some simple widgets for application update notification or extension update notification would make sense in the QStatusBar area as some permanent widgets so it is present regardless of current selected module. The status bar area seems to be frequently used by other applications for notifications.</p>
<p>A statusbar area or “Help-&gt;Check For Updates” menu action is a place I would look first when I’m looking to manually check for application updates when I’m not using automatic checks.</p>
<p>As mentioned in <a href="https://discourse.slicer.org/t/stable-update-notification/23655/6" class="inline-onebox">Stable update notification - #6 by jamesobutler</a>, it would be nice to put Release Notes somewhere to view (these maybe on <a href="http://download.slicer.org">download.slicer.org</a> as well?). This being important for users to see if they really care to update from say Slicer 5.0.3 to 5.0.4 or if has fixes for things they don’t use. This impacts whether users download the new update.</p>
</blockquote>
<p>from <a class="mention" href="/u/lassoan">@lassoan</a>:</p>
<blockquote>
<blockquote>
<p>QStatusBar area as some permanent widgets so it is present regardless of current selected module. The status bar area seems to be frequently used by other applications for notifications.</p>
</blockquote>
</blockquote>
<blockquote>
<p>Popups and other more “in-the-face” notifications would imply that users need more convincing. We don’t know yet if this is needed or not. Even if current notification is not sufficient we have the option of A. make the notifications more prominent; or B. making the updates easier and/or more automatic. I would get back to this question when we gathered some more experience.</p>
<blockquote>
<p>A statusbar area or “Help-&gt;Check For Updates” menu action is a place I would look first when I’m looking to manually check for application updates when I’m not using automatic checks.</p>
</blockquote>
<p>I agree, this would be the standard place. If it just switches to the Welcome module and opens the Updates section then it might fit into Slicer-5.2. If we need a separate reusable update widget then it’ll have to come later.</p>
<blockquote>
<p>it would be nice to put Release Notes somewhere to view (these maybe on <a href="http://download.slicer.org">download.slicer.org</a> as well?)</p>
</blockquote>
<p>Fully agree, it would be nice to add release notes. The current <a href="https://download.slicer.org/find?os=win&amp;stability=release">download.slicer.org API</a> does not provide release note information, so this will have to come later.</p>
<p>Note that currently the main motivation for application update is not the release content but the fact that extensions are only kept up-to-date for the latest stable release (not for any of the previous stable releases). We might reconsider this and keep supporting two stable releases, as it is done in most other serious software. That would allow users to delay their upgrade for one release cycle, while now we expect users to update immediately when we create a new stable release (because we immediately stop supporting the “old” release). The supported second stable release can be always the one right before the latest stable, or - to give users more time for the upgrade - a designated long-term-support (LTS) release. This would require increased maintenance and support effort from both Slicer core developers and all extension developers.</p>
</blockquote>
<p>from <a class="mention" href="/u/pieper">@pieper</a>:</p>
<blockquote>
<p>I agree we can refine the way it behaves after some more experience.</p>
</blockquote>
<p>from <a class="mention" href="/u/jamesobutler">@jamesobutler</a>:</p>
<blockquote>
<p>Ok I was thinking we would make it more in your face as a notification and if people don’t like it then back it off, rather than the other way around as you have now (less in your face and will potentially require making more visible). I would guess we would receive more feedback do like/dislike for the in your face method being the first implementation.</p>
<blockquote>
<p>Popups and other more “in-the-face” notifications would imply that users need more convincing.</p>
</blockquote>
<p>I wouldn’t think they need more convincing but more notification that there is an update. A button in the welcome module only can easily be overlooked.</p>
</blockquote>

---

## Post #20 by @jamesobutler (2022-09-22 14:20 UTC)

<p>When I installed Slicer for the first time with this new update notification the check for updates checkbox was in the PartiallyChecked state. What does it mean to be in the partially checked state?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca03514458bfa5908df7ebf31af6a682b694db5e.png" alt="image" data-base62-sha1="sP5yvH9Tb5MBqn1uD7VWKdEQq0S" width="439" height="137"></p>

---

## Post #21 by @jamesobutler (2022-09-22 14:24 UTC)

<p>In some other applications the About dialog will show the current version, but also if there is an update available. Should it be added here in Slicer too? Currently there is a link to download a newer Slicer version, but doesn’t indicate if there is actually a newer version to download or not.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fb9e78b8edc8bce947fd69208b8e40f11070318.png" alt="image" data-base62-sha1="95Knvoy6f7XzEGo3ZqLuteejpRm" width="673" height="435"></p>

---

## Post #22 by @lassoan (2022-09-22 20:34 UTC)

<p>Partially checked means that application update check or extension update check is enabled but not both. I’ll add an explanation to the tooltip.</p>
<p>How does this message look in the about window?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b471f1c759222193952990b76e57cfcf01468e7e.png" data-download-href="/uploads/short-url/pKi4ji7c9nlvkX1JhxhKzI3YNSm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b471f1c759222193952990b76e57cfcf01468e7e_2_689x430.png" alt="image" data-base62-sha1="pKi4ji7c9nlvkX1JhxhKzI3YNSm" width="689" height="430" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b471f1c759222193952990b76e57cfcf01468e7e_2_689x430.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b471f1c759222193952990b76e57cfcf01468e7e_2_1033x645.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b471f1c759222193952990b76e57cfcf01468e7e.png 2x" data-dominant-color="47474A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1344×838 68.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If there is no update then the window would look like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97576ad65575259a9900f72e9a08ad7c22d08992.png" data-download-href="/uploads/short-url/lAPo6Ai9uz8eAKsPEFYIPrwBhBw.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97576ad65575259a9900f72e9a08ad7c22d08992_2_689x430.png" alt="image" data-base62-sha1="lAPo6Ai9uz8eAKsPEFYIPrwBhBw" width="689" height="430" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97576ad65575259a9900f72e9a08ad7c22d08992_2_689x430.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97576ad65575259a9900f72e9a08ad7c22d08992_2_1033x645.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97576ad65575259a9900f72e9a08ad7c22d08992.png 2x" data-dominant-color="46474A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1344×838 66.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If application update check is disabled in CMake then the <code>Visit the &lt;a href="https://download.slicer.org/"&gt;download site&lt;/a&gt; to check if a new version is available.</code> message would be displayed.</p>

---

## Post #23 by @jamesobutler (2022-09-22 20:39 UTC)

<p>That all seems good to me!</p>
<p>Not sure if just your dev testing, but do we alert of a new application version (5.0.3) for Slicer Preview versions that are actually beyond that version (5.1?). The latest 5.1 preview to 5.0.3 would actually be a downgrade in latest functionality/fixes.</p>

---

## Post #24 by @lassoan (2022-09-22 22:28 UTC)

<p>We display “update available” message if there is a stable release with a more recent revision. For example, now the latest stable is 5.0.3 so we don’t display “update available” message in Slicer-5.1.x versions<br>
However, when Slicer-5.2 stable will be released then “update available” message will be shown in Slicer-5.1.x.</p>

---

## Post #25 by @jamesobutler (2022-11-29 22:28 UTC)

<aside class="quote no-group quote-modified" data-username="jamesobutler" data-post="20" data-topic="23655" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca03514458bfa5908df7ebf31af6a682b694db5e.png" alt="image" data-base62-sha1="sP5yvH9Tb5MBqn1uD7VWKdEQq0S" width="439" height="137"></p>
</blockquote>
</aside>
<p>Using Slicer 5.2.1, I see this checkbox is in the partially checked state. I click it for it to become checked and then close Slicer 5.2.1 and reopen it. I observe that the checkbox is back to being in the partially checked state. It didn’t remember my selection. <a class="mention" href="/u/lassoan">@lassoan</a> is this a bug?</p>
<p>Also if I click it for it to become checked, open Extensions Manager and click the wrench toolbutton I see that “Automatically check for updates” for extensions is still unchecked (supposed to be this way?). If I check this “Automatically check for updates” menu option, then close Slicer 5.2.1 and reopen, I see the checkbox in the “Updates” section of the Welcome module appropriately is in the checked state.</p>

---

## Post #26 by @lassoan (2022-11-30 22:22 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="25" data-topic="23655">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Using Slicer 5.2.1, I see this checkbox is in the partially checked state. I click it for it to become checked and then close Slicer 5.2.1 and reopen it. I observe that the checkbox is back to being in the partially checked state. It didn’t remember my selection. <a class="mention" href="/u/lassoan">@lassoan</a> is this a bug?</p>
</blockquote>
</aside>
<p>Thanks for reporting, it was a bug. I’ve pushed a fix:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/d838e31d2f3e554db83eaeb59d46658ceb6dd9cb">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/d838e31d2f3e554db83eaeb59d46658ceb6dd9cb" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/d838e31d2f3e554db83eaeb59d46658ceb6dd9cb" target="_blank" rel="noopener">BUG: Fix "Check for updates" checkbox in Welcome module</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2022-11-30" data-time="22:21:32" data-timezone="UTC">10:21PM - 30 Nov 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 2 files with 6 additions and 4 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/d838e31d2f3e554db83eaeb59d46658ceb6dd9cb" target="_blank" rel="noopener">
          <span class="added">+6</span>
          <span class="removed">-4</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When "Check for updates" checkbox was in partially checked state, clicking it ch<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/d838e31d2f3e554db83eaeb59d46658ceb6dd9cb" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ange its appearance to checked, but actually did not enable automatic updates.
It is due to `toggled(bool)` signal only emitted when the original state is checked or unchecked (not when it is partially checked).

Fixes issue reported at https://discourse.slicer.org/t/stable-update-notification/23655/25</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
