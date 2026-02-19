---
topic_id: 6183
title: "Orthogonal Planes Axes And Angle Measurement"
date: 2019-03-18
url: https://discourse.slicer.org/t/6183
---

# orthogonal planes/axes and angle measurement

**Topic ID**: 6183
**Date**: 2019-03-18
**URL**: https://discourse.slicer.org/t/orthogonal-planes-axes-and-angle-measurement/6183

---

## Post #1 by @clauzi (2019-03-18 04:15 UTC)

<p>Operating system: Windows 7<br>
Slicer version: 4.10.1<br>
Expected behavior: unknown<br>
Actual behavior: unknown</p>
<p>Is there a possibility in 3D Slicer to place orthogonal planes in a CT and measure angles between these and other planes created?</p>
<p>Thanks so much</p>

---

## Post #2 by @lassoan (2019-03-18 04:38 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/AnglePlanes" rel="nofollow noopener">AnglePlanes extension</a> should allow you to define all the planes you need and compute angles between them.</p>

---

## Post #3 by @clauzi (2019-03-20 12:52 UTC)

<p>Hi Andras,</p>
<p>Great, thanks. I’ll try that.</p>
<p>I am brand new to Slicer and haven’t really worked with it a lot yet, so I apologise for my ignorance in advance.</p>
<p>Is the AnglePlanes extension part of the slicer software already or do I have to download it in addition?</p>
<p>Many thanks and have a good day,</p>
<p>Claudia</p>

---

## Post #4 by @lassoan (2019-03-20 13:18 UTC)

<p>You can download it from the Extension Manager (menu: View / Extension Manager).</p>

---

## Post #5 by @clauzi (2019-04-04 16:10 UTC)

<p>Hi Andras,</p>
<p>sorry to bother you again. Where does the new extension (angle planes) appear in the slicer program? I cannot find it in the modules section after downloading it.</p>
<p>Thanks so much,</p>
<p>Claudia</p>

---

## Post #6 by @lassoan (2019-04-04 17:40 UTC)

<p>I don’t remember which category the module should show up in but you can hit Ctrl-F and start typing the name of a module to find it.</p>

---

## Post #7 by @clauzi (2019-04-04 22:40 UTC)

<p>You’re a star. Found it.<br>
Another related question to the AnglePlane module. Is is possible to create a plane as a best fit of several triangles - like brushing an area - or can I only create planes with landmarks?</p>
<p>I tried to fit the coloured plane to the area I want to have included in the plane, but I find it really difficult to navigate the plane in 360degrees.</p>
<p>THANKS!!!</p>
<p>Claudia</p>

---

## Post #8 by @clauzi (2019-04-05 11:44 UTC)

<p>Hi Andras,</p>
<p>Me again. I just found your name as a contact person related to the Plus Toolkit as well. I just wanted to warn you that I might send you lots of questions and messages about Slicer, IGT, plus toolkit etc. in the next weeks and months! <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"></p>
<p>I am a veterinarian and not an engineer and more or less new to all these programs. I have worked with Polaris Vicra before but on a very basic level. Is it okay if I contact you with any issues or problems I have?</p>
<p>That would be great!</p>
<p>Thanks and have a good day,</p>
<p>Claudia</p>

---

## Post #9 by @lassoan (2019-04-05 12:08 UTC)

<aside class="quote no-group" data-username="clauzi" data-post="7" data-topic="6183">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/35a633/48.png" class="avatar"> clauzi:</div>
<blockquote>
<p>can I only create planes with landmarks?</p>
</blockquote>
</aside>
<p>You can align slice plane with 3 landmark points by copy-pasting these few lines of code to Slicer’s Python interactor (menu: View / Python interactor): <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Fit_slice_plane_to_markup_fiducials" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>
<aside class="quote no-group" data-username="clauzi" data-post="8" data-topic="6183">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/35a633/48.png" class="avatar"> clauzi:</div>
<blockquote>
<p>I might send you lots of questions and messages about Slicer, IGT, plus toolkit etc.</p>
</blockquote>
</aside>
<p>We’ll keep answering the best we can. You can post questions related to Plus / hardware setup in Plus toolkit’s issue tracker and all other questions (Slicer, SlicerIGT) here.</p>

---

## Post #10 by @clauzi (2019-04-05 12:29 UTC)

<p>Thanks, Andras.</p>
<p>One question:</p>
<p>If I want to do surgical navigation based on CT images using Polaris Vicra - what extensions do I need in 3D Slicer and what additional software do I have to download on my PC so that the images, optical trackers and software can communicate with ach other?</p>
<p>I don’t understand programming and don’t have a lot of help form the engineers. So if I know what I have to compile to make it work I might be able to wrap my head around it!</p>
<p>Thank you so much!!</p>
<p>Claudia</p>

---

## Post #11 by @lassoan (2019-04-05 15:20 UTC)

<p>There are many readily-usable tools for surgical navigation in 3D Slicer, so most likely you don’t need to develop anything new, just install 3D Slicer and SlicerIGT extension and Plus toolkit and configure them. <a href="http://www.slicerigt.org/wp/user-tutorial/" rel="nofollow noopener">SlicerIGT tutorials</a> provide step-by-step instructions.</p>

---

## Post #12 by @clauzi (2019-04-05 15:31 UTC)

<p>Thanks so much for all your support. I’ll try to get my head around it and get it running.</p>
<p>Have a great weekend,</p>
<p>Claudia</p>

---
