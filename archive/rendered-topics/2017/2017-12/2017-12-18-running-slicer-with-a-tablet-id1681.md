---
topic_id: 1681
title: "Running Slicer With A Tablet"
date: 2017-12-18
url: https://discourse.slicer.org/t/1681
---

# Running Slicer with a Tablet

**Topic ID**: 1681
**Date**: 2017-12-18
**URL**: https://discourse.slicer.org/t/running-slicer-with-a-tablet/1681

---

## Post #1 by @terajnol (2017-12-18 11:14 UTC)

<p>Hi all,</p>
<p>One of the most convenient way to use Slicer 3D in a surgery room is with a touchscreen/tablet.<br>
From the existing posts and Youtube videos, it is possible to do so with a VNC free remote desktop software or just by running Slicer directly on a Windows tablet (ie Surface Pro).</p>
<p>About the later case, are there Slicer functionalities which cannot be run on a tablet (with no graphical card) ? What about segmentation and 3D reconstruction? Is there a part of preprocessing which you would advice to run before the surgery ?</p>
<p>I am speaking in term of software processing constraints and putting aside problems linked with DICOM loading and touch/mouse manipulation.</p>
<p>Thanks !</p>

---

## Post #2 by @pieper (2017-12-18 12:47 UTC)

<p>Slicer should run pretty well on a windows tablet.  If there’s no GPU then you can only run software (CPU) volume rendering but that isn’t typically a big problem.</p>
<p>Using the user interface with touch controls can be difficult, so it can make sense to make a custom interface with big buttons as described here:</p>
<aside class="onebox pdf">
  <header class="source">
      <a href="https://na-mic.org/w/images/b/b0/Slicelets2016.pdf" target="_blank" rel="nofollow noopener">na-mic.org</a>
  </header>
  <article class="onebox-body">
    <a href="https://na-mic.org/w/images/b/b0/Slicelets2016.pdf" target="_blank" rel="nofollow noopener"><span class="pdf-onebox-logo"></span></a>
<h3><a href="https://na-mic.org/w/images/b/b0/Slicelets2016.pdf" target="_blank" rel="nofollow noopener">Slicelets2016.pdf</a></h3>

<p class="filesize">824.13 KB</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p><a href="http://www.slicerigt.org/wp/developer-tutorial/" class="onebox" target="_blank">http://www.slicerigt.org/wp/developer-tutorial/</a></p>

---

## Post #3 by @lassoan (2017-12-18 14:09 UTC)

<p>We’ve been using Slicer extensively in the operating room and interventional CT, MRI, and US imaging suites for various procedures during the last couple of years. Slicer is very flexible and it can run on even very modest tablets, so it is the clinical application and environment that determine what the best setup is:</p>
<ul>
<li>what operations you need to perform (visualization only, or tool navigation, segmentation, registration, quantification)?</li>
<li>who operates the device: the surgeon or an engineer/computer scientist?</li>
<li>is the operator scrubbed in (need sterile interface)?</li>
<li>is there a display available for Slicer on the monitor boom that is used as the main display?</li>
</ul>
<aside class="quote no-group" data-username="terajnol" data-post="1" data-topic="1681">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/eb8c5e/48.png" class="avatar"> terajnol:</div>
<blockquote>
<p>Is there a part of preprocessing which you would advice to run before the surgery ?</p>
</blockquote>
</aside>
<p>It is advisable to do everything that is possible before surgery to minimize operating room time and reduce chance of any unexpected difficulties.</p>
<p>If you give more information about the medical procedure and your environment (see questions above) then we can give more specific advice.</p>

---

## Post #4 by @terajnol (2017-12-19 14:00 UTC)

<p>Thank you for your answers.</p>
<p>Yes I was thinking about running a slicelet for a custom, touchscreen-suitable and light application.<br>
For now, I am still developping a scripted module for fast tests but you may hear about me and some of my questions in few months when I will start developping the slicelet.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>, to give you more details, here is what I can say about my procedure (but nothing is fixed yet) :</p>
<ul>
<li>DICOM loading and preprocessing (segmentation, image registration and various other processing) will be made before the surgery. Ideally, we would like to let the surgeon do all operations on the same device (then a windows tablet)</li>
<li>During the surgery, the surgeon will use Slicer only for 3D model manipulation and landmarks translation. We don’t think yet a second monitor is necessary in the surgery room.</li>
</ul>
<p>Yes for sure, maximum of manipulation and processing should be done before the surgery but again, we would like to run everything on one single device. We were thinking about having the heavy calculation run on the cloud or on a VPN free remote desktop but the use of a single device will make things easier.</p>
<p>But if you say that even modest tablet can run Slicer without too many problems, then segmentation and volume rendering shouldn’t be a problem for a Windows Surface Pro (i5 processor, 4-6Gb RAM).</p>
<p>During the surgery, we then need a sterile interface for the tablet, but we are thinking about specific plastic bags which allow touchscreen functionalities.</p>

---

## Post #5 by @lassoan (2017-12-19 15:15 UTC)

<aside class="quote no-group" data-username="terajnol" data-post="4" data-topic="1681">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/eb8c5e/48.png" class="avatar"> terajnol:</div>
<blockquote>
<p>developping a scripted module for fast tests</p>
</blockquote>
</aside>
<p>That’s a good start. You can transition seamlessly from a simple scripted module to a slicelet with custom user interface.</p>
<aside class="quote no-group" data-username="terajnol" data-post="4" data-topic="1681">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/eb8c5e/48.png" class="avatar"> terajnol:</div>
<blockquote>
<p>During the surgery, the surgeon will use Slicer only for 3D model manipulation and landmarks translation</p>
</blockquote>
</aside>
<p>What landmarks do you need to translate and why? Is it for patient registration? Do you use surgical navigation (StealthStaion, BrainLab, etc.)?</p>
<aside class="quote no-group" data-username="terajnol" data-post="4" data-topic="1681">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/eb8c5e/48.png" class="avatar"> terajnol:</div>
<blockquote>
<p>we would like to run everything on one single device</p>
</blockquote>
</aside>
<p>A Microsoft Surface Pro can run Slicer very well, so it should not be a problem.</p>
<aside class="quote no-group" data-username="terajnol" data-post="4" data-topic="1681">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/eb8c5e/48.png" class="avatar"> terajnol:</div>
<blockquote>
<p>During the surgery, we then need a sterile interface for the tablet</p>
</blockquote>
</aside>
<p>We use sterile X-ray cassette holder bags with Surface Pro. They are large enough so that it is easy to drop the tablet in them. We have the tablet in a rugged case, as it makes it easier to hold it without pressing the touch screen or turning it off (and may prevent the tablet from breaking if dropped). We disabled Windows button to prevent accidentally opening Start menu.</p>
<p>Even if Slicer runs on the tablet, it is important to set up a separate laptop with VNC access to that Slicer instance so that the engineer in the operating room can quickly check things, fix something, or help the surgeon if he/she does not know how to do something. During patient cases, it is typically not feasible for the engineer to explain anything to the surgeon.</p>

---

## Post #6 by @terajnol (2017-12-19 15:34 UTC)

<p>Thanks for your advices and information.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="1681">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What landmarks do you need to translate and why? Is it for patient registration? Do you use surgical navigation (StealthStaion, BrainLab, etc.)?</p>
</blockquote>
</aside>
<p>About the landmarks, yes I am using them for bone registration. I am not using surgical navigation yet, but this could be of great help in the future. I may come back to the forum with questions about that later.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="1681">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Even if Slicer runs on the tablet, it is important to set up a separate laptop with VNC access to that Slicer instance so that the engineer in the operating room can quickly check things, fix something, or help the surgeon if he/she does not know how to do something. During patient cases, it is typically not feasible for the engineer to explain anything to the surgeon.</p>
</blockquote>
</aside>
<p>I understand your concern about the surgeon using Slicer on his/her own, but our goal is to build an easy-to-use application, even for non-experimented users. Of course, in the first times, additional tech or engineer will be here to help the surgeon, maybe on a separated computer with VPN access.</p>

---

## Post #7 by @terajnol (2018-02-19 16:08 UTC)

<p>Hi all,</p>
<p>I am back after a long break and still working on Slicer. It is still a pleasure to use this software!</p>
<p>I received my Surface Pro tablet and I have a new question related to this post.<br>
Is it possible to handle touch screen manipulation from a python script? For example, from the touch screen, it is possible to rotate the 3D view but I couldn’t find how to translate the view or apply a zoom. I think Slicer is not directly handling the touch screen, do I need to use mouse events ? Is this working for multi-touch recognition (i.e. 2 fingers to zoom or to translate)?</p>
<p>Thanks again !</p>

---

## Post #8 by @lassoan (2018-02-20 03:51 UTC)

<p>Slicer uses VTK for handling render window interactions and VTK currently does not support Windows multi-touch events. Using your fingers you can only rotate (touch-and-drag) and zoom (long-touch-and-drag) in 3D viewer; and adjust window/level and zoom in 2D viewer.</p>

---

## Post #9 by @timeanddoctor (2018-02-20 08:32 UTC)

<p>I use my tablet based on windows10 (Xiaomi2,2G RAM, China). The slicer runs very good except open Volume Reconstruct.</p>

---

## Post #10 by @terajnol (2018-02-20 08:48 UTC)

<p>Ok, thanks for your answers. Zoom and rotation are then possible on 3D view, and I will display sliders or arrow buttons to let the user translate the view.</p>
<p>To inform other users, I am using a Windows Surface Pro tablet (i5, 8Gb of RAM) and Slicers is running perfectly, including volume rendering.</p>

---
