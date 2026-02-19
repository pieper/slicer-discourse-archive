---
topic_id: 17062
title: "Volumetric Assessment"
date: 2021-04-13
url: https://discourse.slicer.org/t/17062
---

# Volumetric assessment

**Topic ID**: 17062
**Date**: 2021-04-13
**URL**: https://discourse.slicer.org/t/volumetric-assessment/17062

---

## Post #1 by @rmarahman (2021-04-13 12:59 UTC)

<p>Dear Users,<br>
I am using 3D Slicer version 4.11. Over 10 years ago I used the program to do volumetric assessments on white matter disease in the brain. I am now attempting to do volumetric assessments on brain tumours and really struggling to figure out how to do the same thing on the updated version.</p>
<p>I have read the multiple online tutorials and I’ve gotten closer to my goal but not achieved it. I need to highlight the volume of a tumour over multiple MRI slices and have the program calculate the total tumour volume for me.</p>
<p>Is there anyone I can humbly beg to give me a rapid tutorial on volumetric assessment? I live in New Zealand and will get up in the middle of the night if that suits you. Happy to do it over Zoom or Skype!</p>
<p>Best regards,<br>
Rosanna Rahman</p>

---

## Post #2 by @spujol (2021-04-13 13:13 UTC)

<p>Hi Rosanna,</p>
<p>The general workflow for volumetric assessment is to use the Segment Editor for segmenting the tumor and the Segment Statistics module to compute the volume of the tumor segmentation.</p>
<p>The Neurosurgical Planning tutorial shows an example of tumor segmentation in a GBM case:<br>
<a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Slicer4_Neurosurgical_Planning_Tutorial" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/4.10/Training#Slicer4_Neurosurgical_Planning_Tutorial</a></p>
<p>Sonia</p>

---

## Post #3 by @pieper (2021-04-13 17:29 UTC)

<p>You could join one of our regular Slicer meetings on Tuesdays, but it seems those are at 2am for you,  If the tutorial doesn’t get you going and you are still stuck we could probably arrange a ‘office hour’ slot at a mutually convenient time.</p>

---

## Post #4 by @rmarahman (2021-04-14 08:16 UTC)

<p>Thank you kindly for your responses Sonia and Steve. I thought I had visited that particular tutorial, but perhaps the couple that I saw were named similarly but were more about 3D rendering of brain tumours and that’s why I was left confused!</p>
<p>I will run through the link you’ve provided on the weekend and get back to you guys if i still have some lingering questions! This is vital I learn so I am definitely will in to be up at 2am to gain some of the group’s wisdom!</p>
<p>Thanks again.</p>
<p>Best wishes,<br>
Rosanna</p>

---

## Post #5 by @spujol (2021-04-14 14:15 UTC)

<p>Hi Rosanna,</p>
<p>The Image Phenotyping tutorial for brain tumor characterization might be helpful:</p>
<p><a href="https://spujol.github.io/ImagePhenotypingTutorial/" rel="noopener nofollow ugc">https://spujol.github.io/ImagePhenotypingTutorial/</a></p>
<p>The first part of the tutorial provides step-by-step instructions for segmenting a meningioma and calculating its volume.</p>
<p>Sonia</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f555f934d075e22f53f4a3147a26f2e7ed994605.png" alt="Outlook-a3bejiaf.png" data-base62-sha1="z0lb0vSFvOXWxBw0xTCVuLMwwqp" width="298" height="39"></p>

---

## Post #6 by @rmarahman (2021-04-14 19:40 UTC)

<p>Thank you for the extra help Sonia! I’ll study both tutorials avidly! <img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=9" title=":grin:" class="emoji" alt=":grin:"><br>
Best wishes,<br>
Rosanna</p>

---

## Post #7 by @Dexter777 (2021-04-17 15:27 UTC)

<p>Steve,<br>
Where is the link for the Tuesday Slicer meeting? I don’t see it here or on the Isomics site.</p>
<p>Thanks.</p>

---

## Post #8 by @pieper (2021-04-17 16:24 UTC)

<p>Hi - The developer hangouts are announced and discussed in <a href="https://discourse.slicer.org/c/community/hangout/20">the discourse hangout community</a>.  The direct link to join on Tuesdays at 10am US eastern time is <a href="https://bit.ly/slicer-googlemeet-hosted-by-kitware">https://bit.ly/slicer-googlemeet-hosted-by-kitware</a>.</p>

---

## Post #9 by @rmarahman (2021-04-28 23:39 UTC)

<p>Dear Steve,</p>
<p>My apologies for the delay. I have now gone through the tutorials that Sonia referred to and while they are quite comprehensive for GBM segmentation, they provide far more detail (in the volumetric assessment) then I’m looking for. What I wish to do is quite a bit more basic, outlining both cystic &amp; solid tumour by slice with the program filling in the volume in between versus letting the program decide on my tumour volumes via standardized colour/tone. I just can’t figure out how to make those changes because anytime I try to draw or paint the drawing stays on the image versus being attached to the slice!</p>
<p>Could I please ask for some personal instruction at your earliest convenience? I’m based in Wellington, New Zealand and I can make myself free most mornings from 6-7:30am or evenings from 6-12pm (except my Wednesdays on both accounts). I can be contacted directly via <a href="mailto:rmarahman@gmail.com">rmarahman@gmail.com</a></p>
<p>Thank you in advance for your time and consideration of my request.</p>
<p>Best regards,<br>
Rosanna</p>

---
