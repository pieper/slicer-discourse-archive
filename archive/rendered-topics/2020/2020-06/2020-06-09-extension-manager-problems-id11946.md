# Extension manager problems

**Topic ID**: 11946
**Date**: 2020-06-09
**URL**: https://discourse.slicer.org/t/extension-manager-problems/11946

---

## Post #1 by @opetne (2020-06-09 09:23 UTC)

<p>Operation system: Windows 10<br>
Hi,</p>
<p>I downloaded the latest nightly build version 4.11.0 2020.06.08 and tried to install some of the extensions but the extension manager failed to work all times I tried. I opens, the process seems running but nothing happens after waiting for a long time. I wait for the restart button to highlight but nothing happens, it shows that the wanted extension is in uninstall state but when I close the manager and reopen it the cancelled operation sign appears and the “installed extensions” can’t be found. I restarted the program and still no sing of installed extensions…<br>
Plus any time if I install the new version it says that there is no existing DICOM database and I have to reload all the DICOM series what are in the Slicer dicom database folder that the previous version created on my computer…</p>

---

## Post #2 by @Jeff_S (2020-06-09 09:59 UTC)

<p>Hi,<br>
I have the same problem. Yesterday the extension manager database in the latest version worked but today not. I suppose there is a connection problem?</p>

---

## Post #3 by @pieper (2020-06-09 16:10 UTC)

<p>thanks for your patience <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:"></p>
<p>The extension infrastructure is being worked on and we hope there’s a more robust solution in the future, but for now it might help just to wait a few hours and try again.</p>

---

## Post #4 by @lassoan (2020-06-09 16:29 UTC)

<p>It is also a timing issue - between about 1am-10am EST, extensions are not available yet for the latest Slicer Preview Release (see some more information and solution <a href="https://discourse.slicer.org/t/is-it-possible-to-do-a-segmentation-of-the-lumbar-spine-from-ct-data-and-use-the-3d-model-igs-for-further-finite-element-analysis-in-abaqus-or-febio/10444/17">here</a>).</p>
<aside class="quote no-group" data-username="opetne" data-post="1" data-topic="11946">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/71e660/48.png" class="avatar"> opetne:</div>
<blockquote>
<p>Plus any time if I install the new version it says that there is no existing DICOM database and I have to reload all the DICOM series what are in the Slicer dicom database folder that the previous version created on my computer</p>
</blockquote>
</aside>
<p>You need to do this only once. All recent (not more than a few months old) Slicer Preview Releases can work from the same DICOM database. If you open the same database with an older Slicer version (e.g., 4.10) then it will downgrade the database. I would suggest not to mix Slicer-4.10 and 4.11 and just use recent Slicer-4.11 releases now.</p>

---

## Post #5 by @opetne (2020-06-10 07:22 UTC)

<p>Thank you, I’ll check the extension manager outside of this timeframe. By the way, this timeframe covers exactly the european work time (1 am-10 am EST).</p>

---

## Post #6 by @lassoan (2020-06-11 18:49 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/mhalle">@mhalle</a> In certain timezones there is a high chance that people don’t find any extensions for the release they have just downloaded. Would it be possible to somehow synchronize the time the new Slicer Preview Release package shows up on the download page with the time when extension builds are complete? Maybe it could be as simple as having an embargo period between 10pm EST and 12pm EST: packages that are uploaded during this time would all show up at the end of the period (at 12pm EST).</p>
<p>I’ve added a ticket to keep track of this:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/4976" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4976" target="_blank">Show new Slicer Preview Release on download page when extension builds are completed</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-06-11" data-time="18:52:37" data-timezone="UTC">06:52PM - 11 Jun 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank">
          <img alt="lassoan" src="https://avatars0.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">In certain timezones (most of Europe) there is a high chance that people don’t find any extensions for the release they...</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:bug</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #7 by @muratmaga (2020-06-11 19:31 UTC)

<p>I second this request.</p>

---

## Post #8 by @pieper (2020-06-11 20:55 UTC)

<p>Yes, this is confusing for everyone.</p>

---
