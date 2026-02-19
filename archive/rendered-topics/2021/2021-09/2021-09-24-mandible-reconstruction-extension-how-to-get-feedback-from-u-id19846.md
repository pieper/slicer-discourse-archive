---
topic_id: 19846
title: "Mandible Reconstruction Extension How To Get Feedback From U"
date: 2021-09-24
url: https://discourse.slicer.org/t/19846
---

# Mandible reconstruction extension - How to get feedback from users?

**Topic ID**: 19846
**Date**: 2021-09-24
**URL**: https://discourse.slicer.org/t/mandible-reconstruction-extension-how-to-get-feedback-from-users/19846

---

## Post #1 by @mau_igna_06 (2021-09-24 21:22 UTC)

<p>I checked the download stats of BoneReconstructionPlanner using <a href="https://slicer-packages.kitware.com/api/v1/app/5f4474d0e1d8c75dfc705482/downloadstats" rel="noopener nofollow ugc">this url</a></p>
<p>These are the results (counting since the extension was uploaded I think)</p>
<pre><code class="lang-auto">"BoneReconstructionPlanner": {
        "linux": {
          "amd64": 19
        },
        "macosx": {
          "amd64": 28
        },
        "win": {
          "amd64": 79
        }
</code></pre>
<p>It is surprising to me that we haven’t heard of none of this users on the forum. Considering the tutorial was uploaded last week, probably most of this users tried to use the extension earlier and most probably were unsuccessful (I wouldn’t bet on silent successes)</p>
<p>How we can improve this?<br>
I see VMTK has a great community, where users ask if they have problems, how that was achieved?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/manjula">@manjula</a> and any one who wants to participate on this conversation</p>

---

## Post #2 by @jamesobutler (2021-09-25 01:23 UTC)

<p>I would guess pure download stats are difficult to associate with number of users. If someone has it download for a Slicer Preview build, then downloads the new preview build each day and chooses the option to reinstall the extension for the new version that could lead to more downloads for the same user. I would also be curious if there are general web bots downloading assets and contributing to download counts.</p>
<p>I don’t believe a decision was made about using user information to get better stats on number of users and for other behavior to then help determine if a project is making an impact or not.</p>

---

## Post #3 by @lassoan (2021-09-25 02:27 UTC)

<p>Users who are just interested in how the extension looks, if it works, etc. don’t need to contact us. You would expect that those who have problems show up, but only about 1 of 100 people actually takes the time to report a problem. We see that for example when we mess up something and there is an error that makes a Slicer release unusable, then out of the 500 average daily downloads, we usually get about 5 error reports (including those who just add a thumbs up to an existing error report).</p>
<p>So, for me getting 0 questions out of 126 downloads is not surprising at all. Those people who are really interested are very likely to show up. You can make that easier by describing how people can reach you (via discourse, via the github repository’s forum, or email).</p>
<p>VMTK is a platform extension - it provides essential algorithms that are used in a wide range of applications (everywhere where you work with tubular structures), so it is expected to get magnitudes more downloads than extensions that implement modules for one specific clinical application.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="19846">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I would also be curious if there are general web bots downloading assets and contributing to download counts.</p>
</blockquote>
</aside>
<p>I asked this from <a class="mention" href="/u/mhalle">@mhalle</a>, who implemented the download stats page and as far as I remember bots are filtered out.</p>

---

## Post #4 by @mau_igna_06 (2021-09-27 19:39 UTC)

<p>I haven’t noticed but there were 270 downloads on the preview release of BoneReconstructionPlanner and the extension doesn’t work on the preview release since May 15th because a change in a function name of vtkMRMLMarkupsPlaneNode used a lot.</p>
<p>I think I should do something about this to stop losing users that try to use the extension with the preview release, at least show an errorDialog that says “This extension doesn’t work on the preview release. Please install it on Slicer’s last stable release”.</p>
<p>What do you think <a class="mention" href="/u/lassoan">@lassoan</a> ?</p>

---

## Post #5 by @lassoan (2021-09-27 19:45 UTC)

<p>I would recommend to fix the extension on the Slicer Preview Release as soon as possible. Is there a reason for not keeping your extension up-to-date?</p>

---

## Post #6 by @mau_igna_06 (2021-09-27 20:56 UTC)

<blockquote>
<p>Is there a reason for not keeping your extension up-to-date?</p>
</blockquote>
<p>We realized of this bug on 2nd week of July. I later asked about what I should do with it on Slicer dev meeting. I was told that making if statements on each place where the changed-name function appeared to make the BoneReconstructionPlanner work on both stable and preview release was not a good solution, also I was told that creating a branch for the stable and another for the preview release was not a good solution either. And the result was that I just leaved the extension working for the stable release only.</p>
<p>If you want me to do one of this solutions I proposed earlier tell me the one you like the most.</p>
<p>By the way, the function that changed name is currently GetObjectToWorldMatrix, previously called GetPlaneToWorldMatrix</p>

---

## Post #7 by @lassoan (2021-09-27 20:58 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="6" data-topic="19846">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>I was told that making if statements on each place where the changed-name function appeared to make the BoneReconstructionPlanner work on both stable and preview release was not a good solution, also I was told that creating a branch for the stable and another for the preview release was not a good solution either.</p>
</blockquote>
</aside>
<p>There might have been some misunderstanding. Both are good solutions.</p>

---

## Post #8 by @mau_igna_06 (2021-09-28 13:24 UTC)

<p>BoneReconstructionPlanner is now compatible with Slicer Preview Releases published since tomorrow</p>

---
