---
topic_id: 1211
title: "Screen Capture 600 Frame Limit"
date: 2017-10-12
url: https://discourse.slicer.org/t/1211
---

# Screen capture - 600 frame limit?

**Topic ID**: 1211
**Date**: 2017-10-12
**URL**: https://discourse.slicer.org/t/screen-capture-600-frame-limit/1211

---

## Post #1 by @hherhold (2017-10-12 13:31 UTC)

<p>Is there a reason for the 600 frame limit in the Screen Capture module? (It looks easy enough to change in <a href="http://ScreenCapture.py" rel="nofollow noopener">ScreenCapture.py</a>, I was just wondering if there was a reason for the limit.)</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2017-10-12 13:50 UTC)

<p>The only reason for a maximum limit is the slider widget. If the max value of the slider is too high then it is very hard to adjust the slider in small steps. You could add a maximum number of images spinbox in the Advanced section and send a pull request.</p>

---

## Post #3 by @hherhold (2017-10-12 23:18 UTC)

<p>OK, I’ll give it a go.</p>
<p>Thanks!</p>

---

## Post #4 by @hherhold (2017-10-23 01:45 UTC)

<p>Done, just submitted pull request. It turned out to be more straightforward than I thought it would be.</p>

---

## Post #5 by @jcfr (2017-10-23 05:07 UTC)

<p>Thanks <a class="mention" href="/u/hherhold">@hherhold</a>  for the pull request</p>
<p>For reference:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/826" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/826" target="_blank">Open IGT Link I/F</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:32:42" data-timezone="UTC">10:32PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:32:43" data-timezone="UTC">10:32PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank">
          <img alt="slicerbot" src="https://avatars3.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">This issue was created automatically from an original Mantis Issue. Further discussion may take place here.</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @jcfr (2017-10-23 16:19 UTC)

<p>To follow up on this, based on the suggestions from <a class="mention" href="/u/lassoan">@lassoan</a></p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="1211" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The only reason for a maximum limit is the slider widget. If the max value of the slider is too high then it is very hard to adjust the slider in small steps. You could add a maximum number of images spinbox in the Advanced section and send a pull request.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/hherhold">@hherhold</a> contributed the changes and they just got integrated in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26507">r26507</a> . It means, they will be available in tomorrow nightly build available at <a href="http://download.slicer.org/#installers" class="inline-onebox">Download 3D Slicer | 3D Slicer</a></p>
<p>Well done <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---
