---
topic_id: 23494
title: "Why After Adding Data From Files The Slicer Flashback"
date: 2022-05-19
url: https://discourse.slicer.org/t/23494
---

# why after adding data from files the slicer flashback?

**Topic ID**: 23494
**Date**: 2022-05-19
**URL**: https://discourse.slicer.org/t/why-after-adding-data-from-files-the-slicer-flashback/23494

---

## Post #1 by @Frankling712 (2022-05-19 16:09 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7c9e786cd1627795f68d7bfbfd311d5ce450377.png" data-download-href="/uploads/short-url/uMXewLnxwyzHG1wJ2y21NdQ7Ren.png?dl=1" title="adding" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7c9e786cd1627795f68d7bfbfd311d5ce450377.png" alt="adding" data-base62-sha1="uMXewLnxwyzHG1wJ2y21NdQ7Ren" width="690" height="408" data-dominant-color="EDEDF5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">adding</span><span class="informations">724×429 8.55 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-05-19 16:10 UTC)

<p>What do you mean by flashback? Does it occur with the very latest Slicer Preview Release?</p>

---

## Post #3 by @pieper (2022-05-19 17:13 UTC)

<p><a class="mention" href="/u/frankling712">@Frankling712</a> note that if you load the .mrml file, you will reload any of the data that was saved with it, so those .fcsv files in the load dialog may be being loaded twice.</p>

---

## Post #4 by @Frankling712 (2022-05-19 17:40 UTC)

<p>i meant that the software slicer always quits after  laoding the data.my friend told me that it was caused by loading too many files,but i think it’s confusing.the data i loaded is what i want.so how should i address this issue?</p>

---

## Post #5 by @Frankling712 (2022-05-19 17:42 UTC)

<p>but if i just load .mrml file,the software slicer can also quit.so how can i figure it out?</p>

---

## Post #6 by @lassoan (2022-05-19 17:44 UTC)

<p>Please give us a bit more information.</p>
<ul>
<li>What Slicer version do you use?</li>
<li>What computer do you have (operating system, CPU model, amount of RAM, free disk space)?</li>
<li>What data do you have problem with? Is the issue with one particular image? How big is the file? What software created that file?</li>
</ul>

---

## Post #7 by @Frankling712 (2022-05-19 17:56 UTC)

<p>version:4.11.20210226  actually i tried different version like 4.13 and 4.11, all failed.<br>
operating system:whindows10 RAM:8GB CPU:intel core i7-8750H 2.20Ghz<br>
free disk space:300GB<br>
the file i loaded is 320 KB.the problem is that the slicer can’t oepen the file,i just need to open one file and get the 3d image.like this<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a47dcc16150babbb76f3ecccad4753cee57c126d.png" alt="forum" data-base62-sha1="nt9P78tzeNpZtOHseqSs2TjyVIx" width="565" height="434"></p>

---

## Post #8 by @Frankling712 (2022-05-19 17:58 UTC)

<p>like what i said,the software always quits after adding files.</p>

---

## Post #9 by @Frankling712 (2022-05-19 18:02 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8c34eb71bb06a5e0b0d0b9e393543208b8d3c68.png" alt="image" data-base62-sha1="qmuix14S0ZkiOGw9lsqOYuADFqM" width="592" height="87"><br>
more information</p>

---

## Post #10 by @lassoan (2022-05-19 18:07 UTC)

<p>Can you reproduce the crash with the very latest Slicer Preview Release (Slicer-5.1)? If yes, then the best would be if you could share the problematic files with us (upload somewhere and post the link here).</p>

---
