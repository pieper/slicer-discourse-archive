---
topic_id: 35688
title: "Windows Dashboard Extension Builds Interrupted Due To Hardwa"
date: 2024-04-23
url: https://discourse.slicer.org/t/35688
---

# Windows dashboard: Extension builds interrupted due to hardware issue

**Topic ID**: 35688
**Date**: 2024-04-23
**URL**: https://discourse.slicer.org/t/windows-dashboard-extension-builds-interrupted-due-to-hardware-issue/35688

---

## Post #1 by @ungi (2024-04-23 17:15 UTC)

<p>Hello, a lot of extensions are missing from the extension manager on Windows. They either don’t even show up on the dashboard like SlicerIGT, or they show up but no built like SlicerRT. Could somebody please check what is wrong with the computer that builds extensions for Windows? Thanks!</p>

---

## Post #2 by @jcfr (2024-04-23 17:35 UTC)

<p>Based on the <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2024-04-23&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=overload">dashboard</a>, last extensions were built 8hrs ago, we are looking into the issue.</p>
<p>Thanks for the patience <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---

## Post #3 by @jcfr (2024-04-25 13:06 UTC)

<h3><a name="p-110238-updates-1" class="anchor" href="#p-110238-updates-1" aria-label="Heading link"></a>Updates</h3>
<ul>
<li>
<p><strong>April 25th, 2024:</strong> A hardware error was reported and we had to powercycle the system. <img src="https://emoji.discourse-cdn.com/twitter/zap.png?v=15" title=":zap:" class="emoji" alt=":zap:" loading="lazy" width="20" height="20">  Regular extensions builds did not complete <img src="https://emoji.discourse-cdn.com/twitter/zap.png?v=15" title=":zap:" class="emoji" alt=":zap:" loading="lazy" width="20" height="20"></p>
</li>
<li>
<p><strong>April 23rd, 2024:</strong> Two days ago, we power cycled the system and it was back on online. We also ran diagnostics and nothing was reported.</p>
</li>
</ul>
<p>cc: <a class="mention" href="/u/ungi">@ungi</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a></p>

---

## Post #4 by @jcfr (2024-04-25 14:31 UTC)

<h3><a name="p-110248-updates-1" class="anchor" href="#p-110248-updates-1" aria-label="Heading link"></a>Updates</h3>
<ul>
<li><strong>April 25th, 2024:</strong> The system will be shutdown to proceed to firmware updates from 3pm to 4pm ET.</li>
</ul>

---

## Post #5 by @Sam_Horvath (2024-04-29 14:18 UTC)

<p><strong>Updates</strong></p>
<ul>
<li><strong>April 29, 2024</strong>: We are continuing to see hardware errors with the Windows factory system.  The builds will be moved to a different machine (<a href="https://github.com/Slicer/DashboardScripts/issues/66">status</a>). We hope to have the build process restored for tomorrow</li>
</ul>

---

## Post #6 by @jcfr (2024-04-29 15:28 UTC)

<h3><a name="p-110429-updates-1" class="anchor" href="#p-110429-updates-1" aria-label="Heading link"></a>Updates:</h3>
<ul>
<li><strong>April 29, 2024</strong> :
<ul>
<li><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> <em>Slicer Preview</em> build have been relocated to “bluestreak” dashboard.</li>
<li><img src="https://emoji.discourse-cdn.com/twitter/hourglass_flowing_sand.png?v=15" title=":hourglass_flowing_sand:" class="emoji" alt=":hourglass_flowing_sand:" loading="lazy" width="20" height="20"> <em>Slicer Stable</em> build of extensions are currently disabled and will be transferred later this week.</li>
</ul>
</li>
</ul>

---

## Post #7 by @jcfr (2024-04-30 13:35 UTC)

<h3><a name="p-110529-updates-1" class="anchor" href="#p-110529-updates-1" aria-label="Heading link"></a>Updates:</h3>
<ul>
<li><strong>April 30, 2024</strong> :
<ul>
<li>
<p><em>Slicer Preview</em> build of the Windows package was successfully generated and uploaded. <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b4025a3086b2f448096b6bd4d6b446b0f7d9ec9.png" data-download-href="/uploads/short-url/1BwGz17DcFuSVVSTnOgyhjs32C5.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b4025a3086b2f448096b6bd4d6b446b0f7d9ec9_2_517x70.png" alt="image" data-base62-sha1="1BwGz17DcFuSVVSTnOgyhjs32C5" width="517" height="70" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b4025a3086b2f448096b6bd4d6b446b0f7d9ec9_2_517x70.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b4025a3086b2f448096b6bd4d6b446b0f7d9ec9_2_775x105.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b4025a3086b2f448096b6bd4d6b446b0f7d9ec9_2_1034x140.png 2x" data-dominant-color="C5CBD2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2896×398 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ul>
</li>
</ul>
<h3><a name="p-110529-next-2" class="anchor" href="#p-110529-next-2" aria-label="Heading link"></a>Next:</h3>
<ul>
<li><em>Slicer Preview</em> build of the Windows extensions are in progress <img src="https://emoji.discourse-cdn.com/twitter/hourglass_flowing_sand.png?v=15" title=":hourglass_flowing_sand:" class="emoji" alt=":hourglass_flowing_sand:" loading="lazy" width="20" height="20"></li>
</ul>

---

## Post #8 by @lassoan (2024-05-02 20:23 UTC)

<p>Has all the problems been resolved? We should then take off the banner from the top of the page.</p>

---

## Post #9 by @Sam_Horvath (2024-05-02 20:38 UTC)

<p>I think we should be good to go now.</p>

---

## Post #10 by @jcfr (2024-05-02 20:41 UTC)

<h3><a name="p-110672-updates-1" class="anchor" href="#p-110672-updates-1" aria-label="Heading link"></a>Updates:</h3>
<ul>
<li><strong>May 2nd, 2024</strong> :
<ul>
<li><em>Slicer Preview</em> build of both the Windows <strong>package</strong> and <strong>extensions</strong> were successfully generated and uploaded. <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></li>
</ul>
</li>
</ul>
<h3><a name="p-110672-next-2" class="anchor" href="#p-110672-next-2" aria-label="Heading link"></a>Next:</h3>
<ul>
<li>Migrate <em>Slicer Stable</em> both Windows extensions.</li>
</ul>
<blockquote>
<p>Has all the problems been resolved? We should then take off the banner from the top of the page.</p>
</blockquote>
<p>As mentioned by <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> , we can now remove the banner.</p>

---

## Post #11 by @GoldenAnpu (2024-05-28 15:54 UTC)

<p>Are there any approximate dates when Slicer Stable builds for Windows extensions will be working again?</p>

---

## Post #12 by @lassoan (2024-05-30 01:24 UTC)

<p>All issues have been resolved (see the dashboard <a href="https://slicer.cdash.org/index.php?project=SlicerStable">here</a>).</p>

---

## Post #13 by @GoldenAnpu (2024-05-31 21:23 UTC)

<p>There is still no update of extensions for Windows in <em>Slicer Stable</em></p>

---

## Post #14 by @jamesobutler (2024-05-31 22:48 UTC)

<p>Kitware (<a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>, <a class="mention" href="/u/jcfr">@jcfr</a>) will have to follow up here since it is their Windows machine building things.</p>
<p>The corresponding open issue about rebuilding Slicer stable on bluestreak and building the Windows based extensions:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/DashboardScripts/issues/66">
  <header class="source">

      <a href="https://github.com/Slicer/DashboardScripts/issues/66" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/DashboardScripts</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/DashboardScripts/issues/66" target="_blank" rel="noopener nofollow ugc">Transfer Windows builds from overload to bluestreak</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-04-29" data-time="14:24:23" data-timezone="UTC">02:24PM - 29 Apr 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/sjh26" target="_blank" rel="noopener nofollow ugc">
          <img alt="sjh26" src="https://avatars.githubusercontent.com/u/25040869?v=4" class="onebox-avatar-inline" width="20" height="20">
          sjh26
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">- [x] Create branch with bluestreak scripts
- [x] Check that girder and credent<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ials files are installed on bluestreak
- [x] add nightly builds to the scheduler</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #15 by @lassoan (2024-06-01 11:37 UTC)

<aside class="quote no-group" data-username="GoldenAnpu" data-post="13" data-topic="35688" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/goldenanpu/48/76712_2.png" class="avatar"> GoldenAnpu:</div>
<blockquote>
<p>There is still no update of extensions for Windows in <em>Slicer Stable</em></p>
</blockquote>
</aside>
<p>You are right. Extensions have not been getting updates on Windows for Slicer Stable Release since 2024-04-28 - see <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;begin=2024-03-01&amp;end=2024-08-01&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=and&amp;field1=buildname&amp;compare1=63&amp;value1=MSBuild&amp;field2=buildname&amp;compare2=63&amp;value2=SlicerIGT">dashboard</a>.</p>
<p>Until the extension updates become available again for the Slicer Stable Release, you can use the Slicer Preview Release, as it contains siginificant new features and all known regressions are resolved.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> It would be great if you could have a look, as we have a couple of new extensions and updates that would be nice to make avaialable for the stable release.</p>

---

## Post #16 by @jcfr (2024-06-19 19:17 UTC)

<p>To follow-up, the build of stable extensions should now be restored.</p>
<hr>
<p>Following  pull request <a href="https://github.com/Slicer/DashboardScripts/pull/70">Slicer/DashboardScripts#70</a>, the Slicer stable build scripts have been updated.</p>
<p>Earlier this afternoon, the Slicer Stable release script was triggered with the environment variable <code>run_ctest_with_upload</code> set to <code>FALSE</code>. Once completed, this will ensure the build tree required to build the Stable Slicer extensions is available.</p>

---
