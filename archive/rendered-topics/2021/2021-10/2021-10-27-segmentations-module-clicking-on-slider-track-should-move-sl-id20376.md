---
topic_id: 20376
title: "Segmentations Module Clicking On Slider Track Should Move Sl"
date: 2021-10-27
url: https://discourse.slicer.org/t/20376
---

# Segmentations module: clicking on slider track should move slider in steps; spinner should increment last digit

**Topic ID**: 20376
**Date**: 2021-10-27
**URL**: https://discourse.slicer.org/t/segmentations-module-clicking-on-slider-track-should-move-slider-in-steps-spinner-should-increment-last-digit/20376

---

## Post #1 by @DIV (2021-10-27 04:28 UTC)

<p>The <strong>Segmentations</strong> module has several sliders in the <em>Display</em> panel, all showing values from 0.00 to 1.00 (to two decimal places).  These are accompanied by number boxes (text fields) with spinners, and tick-boxes (check-boxes).</p>
<p>Current behaviour:</p>
<ul>
<li>
<strong>tick-box</strong> toggles the <em>effective</em> value to either 0.00 or the user’s preference;</li>
<li>dragging the <strong>slider knob</strong> moves in steps of size 0.10;</li>
<li>clicking the <strong>slider rail</strong> jumps to either 0.00 or 1.00;</li>
<li>clicking the <strong>spinner</strong> moves in steps of size 0.10;</li>
<li>any desired (valid) number can be typed into the <strong>text field</strong>.</li>
</ul>
<p>Desired behaviour:</p>
<ul>
<li>
<strong>tick-box</strong> toggles the <em>effective</em> value to either 0.00 or the user’s preference (<em>no change</em>);</li>
<li>dragging the <strong>slider knob</strong> moves in steps of size 0.05 or 0.01 (<em>medium or fine resolution</em>);</li>
<li>clicking the <strong>slider rail</strong> moves in steps of size 0.10 (<em>coarse resolution</em>);</li>
<li>clicking the <strong>spinner</strong> moves in steps of size 0.05 or 0.01 (<em>medium or fine resolution</em>);</li>
<li>any desired (valid) number can be typed into the <strong>text field</strong> (<em>no change</em>).</li>
</ul>
<p>The suggested GUI changes are consistent with the behaviour of vertical scrollbars in a wide variety of applications such as in word processing, PDF document reading/editing, and spreadsheet processing.  That is, clicking the scrollbar acts like <code>Page up</code> or <code>Page down</code> (large steps), <em>not</em> like <code>Home</code> or <code>End</code>;  dragging the scrollbar allows fine control (steps as small, or smaller, than by clicking the arrows at the end of the bar).</p>
<p>The current behaviour of clicking the slider rail is particularly useless, because most of the sliders start with a default value of 1.00, so the current slider rail behaviour in those cases is a redundant duplication of the tick-box.</p>
<p>—DIV</p>

---

## Post #2 by @jamesobutler (2021-10-27 16:16 UTC)

<p>Code in question lives here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/5a86e3f0d83a50deb1a2e289f7213058f7ef6556/Modules/Loadable/Segmentations/Widgets/Resources/UI/qMRMLSegmentationDisplayNodeWidget.ui#L60-L66">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/5a86e3f0d83a50deb1a2e289f7213058f7ef6556/Modules/Loadable/Segmentations/Widgets/Resources/UI/qMRMLSegmentationDisplayNodeWidget.ui#L60-L66" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/5a86e3f0d83a50deb1a2e289f7213058f7ef6556/Modules/Loadable/Segmentations/Widgets/Resources/UI/qMRMLSegmentationDisplayNodeWidget.ui#L60-L66" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/5a86e3f0d83a50deb1a2e289f7213058f7ef6556/Modules/Loadable/Segmentations/Widgets/Resources/UI/qMRMLSegmentationDisplayNodeWidget.ui#L60-L66</a></h4>



    <pre class="onebox"><code class="lang-ui">
      <ol class="start lines" start="60" style="counter-reset: li-counter 59 ;">
          <li>&lt;widget class="ctkSliderWidget" name="SliderWidget_Opacity"&gt;</li>
          <li> &lt;property name="singleStep"&gt;</li>
          <li>  &lt;double&gt;0.100000000000000&lt;/double&gt;</li>
          <li> &lt;/property&gt;</li>
          <li> &lt;property name="pageStep"&gt;</li>
          <li>  &lt;double&gt;1.000000000000000&lt;/double&gt;</li>
          <li> &lt;/property&gt;</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote no-group" data-username="DIV" data-post="1" data-topic="20376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>dragging the <strong>slider knob</strong> moves in steps of size 0.05 or 0.01 ( <em>medium or fine resolution</em> );</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="DIV" data-post="1" data-topic="20376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>clicking the <strong>spinner</strong> moves in steps of size 0.05 or 0.01 ( <em>medium or fine resolution</em> );</p>
</blockquote>
</aside>
<p>^ These would both be accomplished by changing the <code>singleStep</code> property to the desired new value.</p>
<aside class="quote no-group" data-username="DIV" data-post="1" data-topic="20376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>clicking the <strong>slider rail</strong> moves in steps of size 0.10 ( <em>coarse resolution</em> );</p>
</blockquote>
</aside>
<p>^ This would be accomplished by changing the <code>pageStep</code> property to the desired new value.</p>
<p><a class="mention" href="/u/div">@DIV</a> Could you issue a PR <a href="https://github.com/Slicer/Slicer/pulls" class="inline-onebox" rel="noopener nofollow ugc">Pull requests · Slicer/Slicer · GitHub</a> with these changes?</p>

---

## Post #3 by @DIV (2021-10-28 01:08 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="20376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p><a class="mention" href="/u/div">@DIV</a> Could you issue a PR <a href="https://github.com/Slicer/Slicer/pulls" rel="noopener nofollow ugc">Pull requests · Slicer/Slicer · GitHub</a> with these changes?</p>
</blockquote>
</aside>
<p>I’d rather leave it to the experts <img src="https://emoji.discourse-cdn.com/twitter/stuck_out_tongue.png?v=12" title=":stuck_out_tongue:" class="emoji" alt=":stuck_out_tongue:" loading="lazy" width="20" height="20"><br>
Otherwise you’ll have to step me through the process.  I clicked on the link, and read some documentation, but for a pull request it seems I must maybe make a new branch or a new fork or make some edits on an existing branch?  At the link for the code the pencil editing button shows “<em>You must be on a branch to make or propose changes to this file</em>”.<br>
—DIV</p>

---

## Post #4 by @lassoan (2021-10-28 04:16 UTC)

<p>Page size is typically 30% in most of the percentage sliders, but I agree that <strong>10% page step</strong> would be a bit more useful.</p>
<p>Step size in Powerpoint is set so that you can get from 0% to 100% using the up/down spin sliders in about 6 seconds. This would mean about <strong>5% single step size</strong> in Slicer (on my computer).</p>
<aside class="quote no-group" data-username="DIV" data-post="3" data-topic="20376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>At the link for the code the pencil editing button shows “ <em>You must be on a branch to make or propose changes to this file</em> ”.</p>
</blockquote>
</aside>
<p>You can go on and make the change and github will offer to create the fork. So, modifying a single file and creating a pull request is trivial.</p>
<p>However, we would need to the change all the 0-100% sliders across the application the same way (unless there is a specific reason to make the step sizes different). That would mean modifying several .ui files. For this, after github creates the fork and branch, you can go to your fork and modify additional .ui files there. Github will add those changes to the pull request automatically.</p>
<p>You experiment with github and creating pull requests, forking the repository, etc. as you cannot mess up anything in the official Slicer repository.</p>

---

## Post #5 by @DIV (2021-10-29 03:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="20376" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Page size is typically 30% in most of the percentage sliders, but I agree that <strong>10% page step</strong> would be a bit more useful.</p>
<p>Step size in Powerpoint is set so that you can get from 0% to 100% using the up/down spin sliders in about 6 seconds. This would mean about <strong>5% single step size</strong> in Slicer (on my computer).</p>
</blockquote>
</aside>
<p>Sounds reasonable, and I think compatible with my suggestions.</p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="4" data-topic="20376" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<aside class="quote no-group" data-username="DIV" data-post="3" data-topic="20376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>At the link for the code the pencil editing button shows “ <em>You must be on a branch to make or propose changes to this file</em> ”.</p>
</blockquote>
</aside>
<p>You can go on and make the change and github will offer to create the fork. So, modifying a single file and creating a pull request is trivial.</p>
<p>However, we would need to the change all the 0-100% sliders across the application the same way (unless there is a specific reason to make the step sizes different). That would mean modifying several .ui files. For this, after github creates the fork and branch, you can go to your fork and modify additional .ui files there. Github will add those changes to the pull request automatically.</p>
<p>You experiment with github and creating pull requests, forking the repository, etc. as you cannot mess up anything in the official Slicer repository.</p>
</blockquote>
</aside>
<p>Then it sounds like someone (or a small team) with excellent familiarity with the whole project would be better placed to make these changes systematically across all of the relevant files.</p>
<p>I am not completely averse to experimenting and making changes on github, although it would be nice to have some basic pointers — like which branch to work with (nightly?  4.11?), or how to make the edit if the ‘pencil’ button just produces an error.  Not much point spending time making changes on files that that nobody else can access, for example, or which can’t be readily merged with the ‘active’ development code.<br>
Of course, there’s also a balance in allocating the time between my ‘day job’ and learning about github &amp; perhaps making some small contributions there.</p>
<p>—DIV</p>

---

## Post #6 by @lassoan (2021-10-29 03:32 UTC)

<aside class="quote no-group" data-username="DIV" data-post="5" data-topic="20376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>like which branch to work with (nightly? 4.11?),</p>
</blockquote>
</aside>
<p>All developments and fixes are done in the master branch.</p>
<aside class="quote no-group" data-username="DIV" data-post="5" data-topic="20376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>how to make the edit if the ‘pencil’ button just produces an error</p>
</blockquote>
</aside>
<p>We don’t do anything special in Slicer’s github repository. Suggesting file modification works the same way as in all other repositories.</p>
<p>The <em>You must be on a branch to make or propose changes to this file</em> message means* that you need to choose a branch where you want to modify the file on. So, select the <code>master</code> branch in the version selector near the top-left corner:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/813ad5df76ffecbc7f78b902974a7b7b2fc99066.png" data-download-href="/uploads/short-url/irdEb3QpfL5vF5mzjKbgQYeTS3I.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/813ad5df76ffecbc7f78b902974a7b7b2fc99066_2_690x488.png" alt="image" data-base62-sha1="irdEb3QpfL5vF5mzjKbgQYeTS3I" width="690" height="488" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/813ad5df76ffecbc7f78b902974a7b7b2fc99066_2_690x488.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/813ad5df76ffecbc7f78b902974a7b7b2fc99066.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/813ad5df76ffecbc7f78b902974a7b7b2fc99066.png 2x" data-dominant-color="D9DADC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">895×633 50.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="DIV" data-post="5" data-topic="20376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>Not much point spending time making changes on files that that nobody else can access, for example, or which can’t be readily merged with the ‘active’ development code.</p>
</blockquote>
</aside>
<p>All of Slicer’s source code is on github, you have full read access the latest master version, which is the same that all developers are actively working on. You also have full write access on your fork (that github creates for you automatically when you edit a file). You can make all changes in your fork and then create a pull request to ask for your proposed changes integrated into the official repository.</p>
<aside class="quote no-group" data-username="DIV" data-post="5" data-topic="20376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>Of course, there’s also a balance in allocating the time between my ‘day job’ and learning about github &amp; perhaps making some small contributions there.</p>
</blockquote>
</aside>
<p>We appreciate your feedbacks (it is particularly valuable to get perspective of a new user). Learning the github contribution process can be useful in general and finding percentage sliders in the Slicer GUI takes similar effort for everyone, but if you cannot work on these now it is fine, we understand that you need to prioritize (same for all of us). Just let us know what you plan to do to make sure there is a follow up.</p>

---

## Post #7 by @DIV (2021-11-01 05:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="20376" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We don’t do anything special in Slicer’s github repository. Suggesting file modification works the same way as in all other repositories.</p>
</blockquote>
</aside>
<p>I just wasn’t familiar with the ‘usual’ way of doing things on GitHub either.<br>
FWIW, perhaps for others on the forum, I also came across these “<a href="https://github.com/Slicer/Slicer/blob/a15cbacbb91a3f187a8cd80c00bbb232e881f48b/CONTRIBUTING.md" rel="noopener nofollow ugc">Contributing to Slicer</a>” guidelines.  Somewhat over my head, though.</p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="6" data-topic="20376" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<aside class="quote no-group" data-username="DIV" data-post="5" data-topic="20376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>Not much point spending time making changes on files that that nobody else can access, for example, or which can’t be readily merged with the ‘active’ development code.</p>
</blockquote>
</aside>
<p>All of Slicer’s source code is on github, you have full read access the latest master version, which is the same that all developers are actively working on. You also have full write access on your fork (that github creates for you automatically when you edit a file). You can make all changes in your fork and then create a pull request to ask for your proposed changes integrated into the official repository.</p>
</blockquote>
</aside>
<p>Re-reading my comment, I realise it may have been unclear.  I was not making an assumption or assertion, and I wasn’t referring to the branches that I can see (which must <em>ipso facto</em> be public).  I was indicating that <em>hypothetically</em> — for all I know — I might end up creating a ‘private fork’ (if such a thing exists) that nobody else can access.<br>
Anyway, I’ve had a go now, and maybe it will work.</p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="6" data-topic="20376" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<aside class="quote no-group" data-username="DIV" data-post="5" data-topic="20376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>Of course, there’s also a balance in allocating the time between my ‘day job’ and learning about github &amp; perhaps making some small contributions there.</p>
</blockquote>
</aside>
<p>We appreciate your feedbacks (it is particularly valuable to get perspective of a new user). Learning the github contribution process can be useful in general and finding percentage sliders in the Slicer GUI takes similar effort for everyone, but if you cannot work on these now it is fine, we understand that you need to prioritize (same for all of us). Just let us know what you plan to do to make sure there is a follow up.</p>
</blockquote>
</aside>
<p>I’ve had a go on the indicated file for the Segmentations module, which was the interface that was bothering me.  If nothing else, at least this might give an indication as to whether my Pull Request ended up in the right place.<br>
I haven’t touched any other files/modules, and don’t have that as a priority.</p>
<p>I appreciate your additional help in introducing me to the GitHub process.  Like most things, I imagine that the learning curve is steeper at the start.</p>
<p>—DIV</p>

---

## Post #8 by @lassoan (2021-11-01 20:27 UTC)

<p>Your pull request has been merged. Page/single step of percentage sliders will be updated in tomorrow’s Slicer Preview Release. Thank you for your contribution.</p>

---

## Post #9 by @DIV (2022-04-05 07:56 UTC)

<p>Could someone with knowledge of github please take a look at</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6295#">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6295#" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/6295" target="_blank" rel="noopener nofollow ugc">Harmonising slider step sizes.</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>DIV-on-github:patch-10</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-04-02" data-time="11:01:51" data-timezone="UTC">11:01AM - 02 Apr 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/DIV-on-github" target="_blank" rel="noopener nofollow ugc">
          <img alt="DIV-on-github" src="https://avatars.githubusercontent.com/u/66234612?v=4" class="onebox-avatar-inline" width="20" height="20">
          DIV-on-github
        </a>
      </div>

      <div class="lines" title="2 commits changed 1 files with 5 additions and 5 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/6295/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+5</span>
          <span class="removed">-5</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Can maybe also delete 
&lt;property name="SingleStep" stdset="0"&gt;
         &lt;doubl<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6295" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">e&gt;0.050000000000000&lt;/double&gt;
as duplication.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
I tried making some basic changes to the slider code in the <strong>Model</strong> module but I am getting errors such as</p>
<pre><code class="lang-auto">Modules/Scripted/SegmentStatistics/SegmentStatistics.py:559: [B020] Found for loop that reassigns the iterable it is iterating with each iterable value.
    for name in {name for name in uniqueHeaderNames if uniqueHeaderNames.count(name)&gt;1}:
        ^

Error: The process '/opt/hostedtoolcache/Python/3.9.12/x64/bin/pre-commit' failed with exit code 1
</code></pre>
<p>which may be nothing to do with my changes.</p>
<p>I also tried to amend my own changes, but not sure if that was done correctly.</p>
<p>—DIV</p>

---

## Post #10 by @DIV (2022-04-06 04:46 UTC)

<p>It also fails “<strong>CommitCheck</strong> — Not all of your commit messages are valid.”, but I am unable to see what is the offending part of the message.</p>

---

## Post #11 by @jamesobutler (2022-04-06 13:26 UTC)

<p>You can learn a little about CommitCheck from the post below or more directly at <a href="https://slicer.readthedocs.io/en/latest/developer_guide/style_guide.html#commits" class="inline-onebox" rel="noopener nofollow ugc">Style Guide — 3D Slicer documentation</a>.</p>
<aside class="quote" data-post="1" data-topic="10921">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/commit-message-prefix/10921">Commit message prefix</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    As discussed in <a href="https://github.com/Slicer/Slicer/pull/4783#issuecomment-605662343" rel="noopener nofollow ugc">this issue</a>, the DOC: prefix is now valid when writing commit message. 
The <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Style_Guide#Commits" rel="noopener nofollow ugc">Commit Style Guide</a> and the <a href="https://www.commitcheck.com" rel="noopener nofollow ugc">commit check</a> have both been updated. 
For reference,  here is the regex used to validate the commit title: (BUG|COMP|DOC|ENH|PERF|STYLE)\: \w+
  </blockquote>
</aside>


---

## Post #12 by @DIV (2022-04-07 01:43 UTC)

<p>Thanks, James.<br>
I do now recall that a prefix was mentioned in one of the guides, which I omitted.<br>
So I think I have fixed that, although there seems to be no way to get the check to be re-run (except perhaps making more edits to the code).</p>
<p>Also the link on GitHub to “<a href="https://www.commitcheck.com/status/Slicer/Slicer/b98e6eb8-3231-4faa-8ed4-e97decab7966" rel="noopener nofollow ugc">Details</a>” of the CommitCheck check doesn’t work for me.<br>
I click and get taken immediately to <code>https://www.commitcheck.com/401</code>, which says “_ Something went wrong … You may have been logged out._” and provides a button to “<em>Log in with GitHub</em>” …but when I click to do that, I’m taken to <code>https://www.commitcheck.com/users/auth/github</code>, which shows only “<em>Not found. Authentication passthru.</em>”.</p>
<p>Any ideas on the linting error?<br>
At this point I’m guessing that the code hasn’t changed, but the linting check has been modified since the original code was written.</p>
<p>—DIV</p>

---

## Post #13 by @jamesobutler (2022-04-07 03:24 UTC)

<p>CommitCheck is checking the prefix of the Commits in the PR and not the PR title as you have recently updated. Your PR currently includes commits titled <code>Harmonising slider step sizes.</code> and <code>Update qMRMLModelDisplayNodeWidget.ui</code> which neither have an appropriate commit prefix. You should be able to find resources online discussing how to squash and amend commits. I suggest you practice in a separate branch first before pushing updates to the branch corresponding to your PR.</p>

---

## Post #14 by @lassoan (2023-03-21 02:02 UTC)



---
