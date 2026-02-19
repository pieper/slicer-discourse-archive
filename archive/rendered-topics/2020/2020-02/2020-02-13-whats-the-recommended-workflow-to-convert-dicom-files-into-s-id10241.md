---
topic_id: 10241
title: "Whats The Recommended Workflow To Convert Dicom Files Into S"
date: 2020-02-13
url: https://discourse.slicer.org/t/10241
---

# What's the recommended workflow to convert DICOM files into slices?

**Topic ID**: 10241
**Date**: 2020-02-13
**URL**: https://discourse.slicer.org/t/whats-the-recommended-workflow-to-convert-dicom-files-into-slices/10241

---

## Post #1 by @AmateurRadiologist (2020-02-13 13:48 UTC)

<p><strong>First the bragging</strong><br>
I am the proud owner of a Faxitron MX-20 X-ray cabinet, equipped with a 20μm spot size micro-focus tube, with a fixed beam current at 300μA, a voltage anywhere between 10 and 35kV and an exposure time from 0.1 to 300 seconds. It is equipped with a Hamamatsu 120x120mm digital imager with a 20μm pixel size and 14-bit intensity resolution. And the best of it all is that this instrument is inherently safe to operate. Leaks are checked for regularly.<br>
This instrument creates beautifully detailed images, but it was never intended for CT.</p>
<p><strong>Then about me</strong><br>
I am a professional embedded software engineer, specialized in Linux kernel development, microcontroller firmware and electronic interfacing. I have a broad interest in physics, especially where physics meet electronics and software.</p>
<p><strong>Now about my 'problem’</strong><br>
Putting my cabinet on its side and equipping it with a turn-table, I would like to use it to make CT scans.<br>
Doing my research, I discovered I needed to create sinograms and apply an inverse radon transformation on each of those to end up with slices. I traveled to SciPy, Astra and TomoPy. I learned that most standard implementations assume a parallel beam geometry, while my instrument has its source relatively close to the imager, hence its conical geometry can not be neglected. But I have no ambition in learning Python. Properly motivated this could change, but I could not imagine I was the only person trying this, so I looked further and found Slicer 3D.</p>
<p><strong>Finally the questions</strong><br>
My instrument produces flat-field and dark-field corrected images, each in its own Dicom formatted file. These files do not contain any geometry information.<br>
If I create 99 images of a single object, each with the object turned 1.8 degree further, what would be the recommended work-flow to transform these 99 Dicom files into a set of cross sections?<br>
I realize that geometry matters: imager perpendicularity to the source, imager center alignment to source center, distance between source and imager, imager diameter, and I’m not even getting started about the turntable.<br>
Which of these geometry parameters really matter, which do I need to get right, and which ones can be calibrated out relatively easy by for example scanning a cube?</p>
<p>Thank you for reading. Eagerly waiting for wisdom!</p>

---

## Post #2 by @pieper (2020-02-13 14:32 UTC)

<p>Sounds like a cool project!</p>
<p>There is an inverse projection open source toolkit, from Kitware I thought, but I can’t put my fingers on the link right now.  Maybe <a class="mention" href="/u/thewtex">@thewtex</a> knows?</p>
<p>Your project reminds me of this guy’s garage CT scanner.  You can see at the end he uses Slicer to view the reconstructed volume slices.</p>
<div class="lazyYT" data-youtube-id="hF3V-GHiJ78" data-youtube-title="DIY X-ray CT scanner controlled by an Arduino" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #3 by @pieper (2020-02-13 14:46 UTC)

<p>D’oh, I remember now!  This is what you want: <a href="https://www.openrtk.org/">https://www.openrtk.org/</a></p>

---

## Post #4 by @AmateurRadiologist (2020-02-13 15:26 UTC)

<p>Thanks for your response!</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="10241">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Your project reminds me of this guy’s garage CT scanner. You can see at the end he uses Slicer to view the reconstructed volume slices.</p>
</blockquote>
</aside>
<p>Hm, I was well aware of this and all other cool projects of Ben, but it didn’t occur to me to re-watch his CT scanner video, because I thought he did everything in MathLab. But you’re right, he is indeed using 3D slicer! Thank you for the hint. I’ll drop him a message. I’ve emailed him before and he’s a very friendly guy.</p>
<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="10241">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>D’oh, I remember now! This is what you want: <a href="https://www.openrtk.org/" rel="noopener nofollow ugc">https://www.openrtk.org/ </a></p>
</blockquote>
</aside>
<p>I’m going through the documentation right now. Especially the page on geometry is very useful. Thank you!</p>

---
