# 3d slicer nvidia 

**Topic ID**: 17606
**Date**: 2021-05-13
**URL**: https://discourse.slicer.org/t/3d-slicer-nvidia/17606

---

## Post #1 by @ni5h (2021-05-13 13:55 UTC)

<p>Hi, I am still getting the error code 500 when trying to complete a nvidia ct liver segmentation, I have followed the instructions edit&gt;application setting&gt;nvidia. the server is blank and so it suggests a default server will be used. I have signed up with nvidia, I have gitbash - how do I get this to run/what code do I have to run to get this to work. A step-by-step guide would be really helpful, I am not an expert by any means. Thanks for your help in advance!</p>

---

## Post #2 by @lassoan (2021-05-13 14:51 UTC)

<p>The current hardware of the demo server is not compatible with latest NVidia Clara, but the NVidia AIAA effect in Segment Editor is not fully compatible with older server versions. Until we can upgrade the demo server hardware, you won’t be able to use all models. You either have to wait for our hardware upgrade (at least several weeks) or install NVidia Clara on your computer (requires a good GPU).</p>

---

## Post #3 by @ni5h (2021-06-22 16:24 UTC)

<p>Hi Iassoan, we are again completing a great number of liver segmentations, is there any progress on this Nvidia extension? It would be a great help if we could complete these segmentations in a timely manner, grow from seeds and fill between slices is, at this stage, time consuming. Any ideas how to get segment livers quickly that are a short term extension until the Nvdia upgrade is compatible?</p>

---

## Post #4 by @lassoan (2021-06-22 18:49 UTC)

<p>Yes, there have been lots of progress!</p>
<p>Most exciting is addition of <a href="https://github.com/Project-MONAI/MONAILabel">MONAILabel</a> extension and lots of models, including liver segmentation. You may join the <a href="https://projectweek.na-mic.org/PW35_2021_Virtual/">Slicer Project Week</a> (next week) to learn more</p>
<p>We’ll get our new server within a few weeks and we plan to make available both NVidia Clara and MONAILabel on it.</p>

---

## Post #5 by @ni5h (2021-06-23 10:05 UTC)

<p>Oh that’s great news!</p>
<p>I would love to join this project week but I am on vacation/annual leave next week. Will there be another?</p>
<p>Okay great, I will look out for the MONOAILabel and Nvidia extension, and will check these within a few weeks, will this require just to download the extension or supplementary extensions?</p>

---

## Post #6 by @lassoan (2021-06-23 12:57 UTC)

<aside class="quote no-group" data-username="ni5h" data-post="5" data-topic="17606">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/839c29/48.png" class="avatar"> ni5h:</div>
<blockquote>
<p>Will there be another?</p>
</blockquote>
</aside>
<p>We have a project week twice a year. The next one might be in person again, in Gran Canaria.</p>
<aside class="quote no-group" data-username="ni5h" data-post="5" data-topic="17606">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/839c29/48.png" class="avatar"> ni5h:</div>
<blockquote>
<p>will this require just to download the extension or supplementary extensions?</p>
</blockquote>
</aside>
<p>These features are implemented in the NVidiaAIAA and MONAILabel extensions.</p>

---

## Post #7 by @ni5h (2021-06-23 15:35 UTC)

<p>Apologies, just to ensure I am clear, I have just searched for monolabelAI, this is not yet available unlike the NVIDIA extension, this will be available on the server in a few weeks? I.e. I will have to uninstall the current NVIDIA extension I have and re-install this? But will also be able to use the monolabelAI extension also to see if that compares for a comprehensive 3d liver segmentation. NB. The Nvidia youtibe video looks great, I hope we can start using this!!</p>

---

## Post #8 by @lassoan (2021-06-24 15:53 UTC)

<p>A post was split to a new topic: <a href="/t/add-signature-to-segmentation/18327">Add signature to segmentation</a></p>

---

## Post #9 by @lassoan (2021-06-24 15:54 UTC)

<p>MONAILabel is a new extension, available for recent Slicer Preview Releases.</p>

---

## Post #10 by @ni5h (2021-11-23 18:00 UTC)

<p>Hi there,</p>
<p>I have returned to this query raised some months back. we are looking to again look for quicker solution to liver segmentation - I tried this again and some data sets we have used previously on 3d slicer and there is still the error500 code - what server do I require for this to work? the version I am using is 20210226 - i leave the server blank. I have looked within the community wherey users have had success - what am I doing wrong?</p>

---

## Post #11 by @lassoan (2021-11-23 19:01 UTC)

<p>Make sure the AI assisted segmentation module is up-to-date by uninstalling and installing it. If it does not help then try with the latest Slicer Preview Release.</p>
<p>If the problem persists then probably your data set has very different size and resolution compared to the training data set. Try with the liver images of the <a href="http://medicaldecathlon.com/">medical image segmentation decathlon</a> these are the images that the network was trained on.</p>

---
