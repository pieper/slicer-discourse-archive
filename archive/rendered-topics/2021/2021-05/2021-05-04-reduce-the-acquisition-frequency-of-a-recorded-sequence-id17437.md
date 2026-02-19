---
topic_id: 17437
title: "Reduce The Acquisition Frequency Of A Recorded Sequence"
date: 2021-05-04
url: https://discourse.slicer.org/t/17437
---

# Reduce the acquisition frequency of a recorded sequence

**Topic ID**: 17437
**Date**: 2021-05-04
**URL**: https://discourse.slicer.org/t/reduce-the-acquisition-frequency-of-a-recorded-sequence/17437

---

## Post #1 by @AurelieS (2021-05-04 08:23 UTC)

<p>Operating system: win10<br>
Slicer version: 4.11.20200930</p>
<p>Dear 3D Slicer team,</p>
<p>We did a number of freehand 3D ultrasound using 3D Slicer (and PlusServer with ultrasound video acquisition and streaming of Optitrack data).<br>
All is working fine but we believe we may have used too high of an acquisition frequency while recording with the module ‘sequences’, leading to very heavy acquisitions (more than 20Go for a muscle acquisition), and not so well defined volume reconstructions (maybe due to the excessive amount of video data, especially since the video feed had a maximal frequency of 32Hz so we have image duplicates for different probe tracking data … ). The time of reconstruction is also very high for our computer with 64Go RAM and 150Go virtual RAM …<br>
All sequences recorded both the image from the ultrasound and the tracker position of the probe (2 nodes) at 50Hz.<br>
Is it possible, one way or another, to lower the sampling frequency of our sequence, meaning for example to take one sample every of 5 samples of our recorded sequence ?</p>
<p>Thank you in advance,<br>
Cheers,<br>
Aurélie</p>

---

## Post #2 by @AurelieS (2021-05-07 11:16 UTC)

<p>Please find here some raw data, for example S1_BF_1.1 that we do not find of very good reconstruction quality :</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://pcdn-e.pcloud.com/Zyb/fav.ico" class="site-icon" width="16" height="16">
      <a href="https://e.pcloud.link/publink/show?code=kZwTIXZmdvDd9EGDB0iGkqHMvEjAkuVWttV" target="_blank" rel="noopener nofollow ugc">pCloud</a>
  </header>
  <article class="onebox-body">
    

<h3><a href="https://e.pcloud.link/publink/show?code=kZwTIXZmdvDd9EGDB0iGkqHMvEjAkuVWttV" target="_blank" rel="noopener nofollow ugc">Share Anything with pCloud</a></h3>

<p>With pCloud's unique Download Link feature you can share files with everyone. Click to download. 
Join pCloud.com and get up to 20GB FREE cloud storage.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<p>
Password : 3Dslicer</p>
<p>Cheers,<br>
Aurélie</p>

---
