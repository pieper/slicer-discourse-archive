---
topic_id: 36906
title: "Issue Running Gpa In Slicermorph"
date: 2024-06-19
url: https://discourse.slicer.org/t/36906
---

# Issue running GPA in Slicermorph

**Topic ID**: 36906
**Date**: 2024-06-19
**URL**: https://discourse.slicer.org/t/issue-running-gpa-in-slicermorph/36906

---

## Post #1 by @isacampos495 (2024-06-19 20:51 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e24c47eeb1b65c2cf28d55c3ca3e39ae50bbb77f.png" data-download-href="/uploads/short-url/whVl3lrQQSgoyx58GrAtXmtVtmL.png?dl=1" title="gpa-analysis-python-error-screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e24c47eeb1b65c2cf28d55c3ca3e39ae50bbb77f_2_690x365.png" alt="gpa-analysis-python-error-screenshot" data-base62-sha1="whVl3lrQQSgoyx58GrAtXmtVtmL" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e24c47eeb1b65c2cf28d55c3ca3e39ae50bbb77f_2_690x365.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e24c47eeb1b65c2cf28d55c3ca3e39ae50bbb77f_2_1035x547.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e24c47eeb1b65c2cf28d55c3ca3e39ae50bbb77f_2_1380x730.png 2x" data-dominant-color="FAF8F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">gpa-analysis-python-error-screenshot</span><span class="informations">1918×1016 68.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hello!</p>
<p>I’ve been trying to run GPA analysis with Slicermorph but it hasn’t been doing anything. I’ve already successfully run ALPACA with multiple data sets to get my landmarks, but when I try to put them into GPA and click the “execute GPA + PCA” button nothing happens. It simply doesn’t run it. I checked the python log to see if I received any kind of error messages in there, and it appears that something is wrong there (although I am not that technically savvy, so I’m not sure what). I’ve tried running GPA with different and smaller landmark data sets and have shut the program down multiple times, but none of that has worked.</p>
<p>Any help is much appreciated, thank you!</p>

---

## Post #2 by @LeidyMoraV (2024-06-19 21:03 UTC)

<p>Have you tried saving the landmarks as .fcsv instead of .json?</p>

---

## Post #3 by @muratmaga (2024-06-19 21:08 UTC)

<p><a class="mention" href="/u/isacampos495">@isacampos495</a> can you share those two mrk.json files?</p>

---

## Post #4 by @muratmaga (2024-06-19 21:52 UTC)

<p>I can’t replicate this with two mrk.json files I have. Couple things to check:</p>
<ol>
<li>
<p>Make sure you are using the latest version of the SlicerMorph extension. Go to the extension manager and click “CHeck Updates”. If you are running a version prior to June 12th, you will see an update. If there is no update, it is the latest version.</p>
</li>
<li>
<p>Make sure you have exactly the same number of landmarks in both files. The error indicates there is a mismatch in the array in somehow.</p>
</li>
</ol>
<p>If you can share two files, we can take a closer look.</p>

---

## Post #5 by @isacampos495 (2024-06-20 14:01 UTC)

<p>I have not tried saving them in a different format. However, it takes so long to produce the files with ALPACA (because I’m doing a couple hundred at a time) that I don’t know how feasible it is for me to redo them as .fcsv files instead of .json</p>

---

## Post #6 by @isacampos495 (2024-06-20 14:10 UTC)

<p>I did just check, and I have not been using the most updated version of Slicermorph. I just updated it and will try running GPA again to see if that fixes the issue. As for the number of landmarks, they should have the same amount. They are files that I auto-landmarked with ALPACA from one source model/landmark file. These are only two of about a couple hundred files that I auto-landmarked with ALPACA. I can’t share the files directly because I can’t upload .json files here, but I was able to put them in a google drive folder, so here is that link to all the files I produced with ALPACA:</p>
<p><a href="https://drive.google.com/drive/folders/1ux2LLGQinrstJx0awFzx5G9g9SVHdotx?usp=drive_link" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1ux2LLGQinrstJx0awFzx5G9g9SVHdotx?usp=drive_link</a></p>

---

## Post #7 by @isacampos495 (2024-06-20 14:12 UTC)

<p>Update: The issue was fixed. I updated Slicermorph and it was immediately able to run the GPA + PCA. Thank you for the help!</p>

---

## Post #8 by @muratmaga (2024-06-20 14:43 UTC)

<aside class="quote no-group" data-username="LeidyMoraV" data-post="2" data-topic="36906" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leidymorav/48/70144_2.png" class="avatar"> LeidyMoraV:</div>
<blockquote>
<p>Have you tried saving the landmarks as .fcsv instead of .json?</p>
</blockquote>
</aside>
<p>You should stop using fcsv and keep them as mrk.json, as eventually fcsv support will be dropped. Earlier we had a bug with a mrk.json reading, but that has been fixed long time ago.</p>

---
