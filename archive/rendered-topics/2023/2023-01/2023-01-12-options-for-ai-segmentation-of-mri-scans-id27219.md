---
topic_id: 27219
title: "Options For Ai Segmentation Of Mri Scans"
date: 2023-01-12
url: https://discourse.slicer.org/t/27219
---

# Options for AI Segmentation of MRI Scans

**Topic ID**: 27219
**Date**: 2023-01-12
**URL**: https://discourse.slicer.org/t/options-for-ai-segmentation-of-mri-scans/27219

---

## Post #1 by @JacobD (2023-01-12 23:29 UTC)

<p>Hello,</p>
<p>I am looking to learn about tools or extensions that are available to assist with the automatic segmentation of a shoulder MRI using AI. Using a specific scanning sequence, multiple reconstructions of the bones of the glenohumeral joint have been created, and as the manual process is slow, I wanted to ask if a tool has been created to help automate the process.</p>
<p>If a tool does not exist for shoulder MRIs, I was wondering if there was a program that could utilize deep learning from a collection of reconstructions of shoulder MRIs, to contribute to a tool that automatically segments them.</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2023-01-13 22:18 UTC)

<p>I don’t know of a model for shoulder MRIs, but you can look into the MONAI Label tool.</p>
<p>We should soon be circulating sign up info for a MONAI Label workshop on January 25 9-11 EST that may be of interest for you or anyone getting started with this kind of project.</p>

---

## Post #3 by @shai-ikko (2023-01-16 10:16 UTC)

<p>That’s very interesting. When you say “circulating”, does that mean here in the forum, or is there some other place I should be looking?</p>

---

## Post #4 by @rbumm (2023-01-16 10:30 UTC)

<p>The workshop will be announced on the <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/">website of the 38th Project Week</a> soon.</p>

---

## Post #5 by @pieper (2023-01-16 17:51 UTC)

<p>Here’s the event page with the registration link:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://projectweek.na-mic.org/PW38_2023_GranCanaria/MONAILabel_Workshop">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/MONAILabel_Workshop" target="_blank" rel="noopener">NA-MIC Project Weeks</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/MONAILabel_Workshop" target="_blank" rel="noopener">MONAI Label Workshop / Tutorial</a></h3>

  <p>Website for NA-MIC Project Weeks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @JacobD (2023-01-18 22:04 UTC)

<p>Thank you for the information. The MONAI Label tool sounds interesting. As I am not previously familiar with it, would utilization of the tool essentially facilitate the development of an application that could be applied to datasets to assist with automatic segmentation? Would the tool be applicable to previously annotated datasets to be able to contribute to the application development?</p>

---

## Post #7 by @pieper (2023-01-18 22:32 UTC)

<p>Yes, that’s exactly what it is for: using new or existing segmentations to train models that perform automatic segmentation.  Exactly how many segmentations are needed is very application dependent, but there are examples of good results.</p>

---

## Post #8 by @JacobD (2023-01-19 15:11 UTC)

<p>Perfect, sounds great! Thank you for the information and assistance!</p>

---
