---
topic_id: 2845
title: "Does Slicer Support External Graphics Cards"
date: 2018-05-17
url: https://discourse.slicer.org/t/2845
---

# Does Slicer support external graphics cards?

**Topic ID**: 2845
**Date**: 2018-05-17
**URL**: https://discourse.slicer.org/t/does-slicer-support-external-graphics-cards/2845

---

## Post #1 by @goetzf (2018-05-17 22:45 UTC)

<p>Operating system: OSx high sierra<br>
Slicer version:4.8<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Slicer keeps using all of my CPU so I’m thinking about getting an external graphics card like this:<br>
<a href="https://www.sonnetstore.com/products/egfx-breakawaybox-radeonrx580" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.sonnetstore.com/products/egfx-breakawaybox-radeonrx580</a></p>
<p>Will that work?</p>

---

## Post #2 by @lassoan (2018-05-17 22:53 UTC)

<p>I think it should not matter for applications if you use internal or external GPU. However, only certain operations benefit from a strong GPU, such as volume rendering, or rendering of models that have hundreds of thousands of points. What operations do you do often and take too long?</p>
<p>Most likely you would get much better overall performance if you get a gaming laptop instead of just upgrading the GPU. Additional advantages are that you don’t need to deal with clunky external GPU, you can use virtual reality, and total cost may be lower, too.</p>

---

## Post #3 by @goetzf (2018-05-22 15:10 UTC)

<p>I have uCT data 1200 slices and each .dcm files is about 2.4MB. I need to segment the external and internal anatomy and my computer keeps crashing. Every time I click, the program takes at least 30 seconds to respond. I tried Horos and they don’t have this problem at all. Unfortunately, they don’t have the features I want and there is no free support so I am going back to 3D slicer which I can’t do with my current computer configuration. Here is what I’m working with:<br>
MacOS High Sierra 10.13.4<br>
Processor: 3.5 GHz Intel Core i7<br>
memory: 32 GB 1600 MHz DDR3 (This was upgraded from 8GB that the computer came with)<br>
Graphics: NVIDIA GeForce GTX 775M 2048 MB</p>
<p>It seems like that could be enough but that’s not how the program acts when I am segmenting in 3D slicer. I have access to a newer computer where I can upgrade to 64GB RAM and I was thinking about getting that Radeon video card I mentioned in my earlier post.</p>
<p>Since I have a computer I can switch to, I would like to make it useable rather than buying a whole new computer.</p>
<p>Thank you for your input!</p>
<p>Freya</p>

---

## Post #4 by @muratmaga (2018-05-22 15:42 UTC)

<p>You need to give a bit more information. For example what module is crashing, and what are you clicking on? Is the issue during the load or the segmentation?</p>

---

## Post #5 by @lassoan (2018-05-22 18:12 UTC)

<p>Slicer uses OpenGL for rendering, so rendering speed should be automatically improved if you attach an eGPU and configure your system so that Slicer uses it. However, this most likely to improve the problems that you have mentioned.</p>
<aside class="quote no-group" data-username="goetzf" data-post="3" data-topic="2845">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/b38774/48.png" class="avatar"> goetzf:</div>
<blockquote>
<p>Every time I click, the program takes at least 30 seconds to respond</p>
</blockquote>
</aside>
<p>I’ve worked with larger data sets without problems. In general, memory space may be an issue for large data sets, but 32GB should be OK to get started (especially if you have a hundred GB free disk space to make absolutely sure you don’t run out of memory space). So, as <a class="mention" href="/u/muratmaga">@muratmaga</a> mentioned, we need more information to help - have you enabled “Show 3D”, what effects do you use, etc.?</p>
<p>You may try to downsample your volume by a factor of 2 on all axes, which would result in 8x less memory usage. It is also worth cropping your volume to the minimum size. You can use Crop volumes module for both.</p>

---

## Post #6 by @goetzf (2018-05-22 18:46 UTC)

<p>Good questions. I am now using a computer with 900GB free storage and the following guts:<br>
processor: 4.2 GHz Intel Core i7<br>
Memory 8 GB 2400 MHz DDR4 (can be updated to 64 GB)<br>
Graphics: Radeon Pro 575 4096 MB</p>
<p>I think I had about 300GB free storage on the last computer. I was using a plugin called segmentation wizard. I think I cropped the volume but I will try again. I never got to any volume rendering because my computer told me I had used all available memory and I needed to quit the program before I could finish segmenting the whole animal. Every click was so slow I wasn’t getting anywhere so I tried Horos which performed much better on my computer but I’m not happy with the useability and lack of support. Needless to say, I’m very grateful for your help in trying to figure out the best configuration.</p>

---

## Post #7 by @goetzf (2018-05-22 18:50 UTC)

<p>I have not knowingly enabled  “show 3D”. I will look for that.</p>

---

## Post #8 by @lassoan (2018-05-22 19:03 UTC)

<p>8GB RAM for editing an almost 3GB volume will be very slow. In general, I recommend 10x more RAM than the main working volume size. If increasing RAM size is not easy then crop and resample your volume to make the volume size smaller (as I described above). After cropping is completed, delete the original full-size volume from the scene.</p>
<p>Segmentation wizard extension has been developed for one particular segmentation task. It is not for general purpose segmentation and may work very inefficiently. Use Segment editor module instead.</p>

---

## Post #9 by @goetzf (2018-05-22 19:16 UTC)

<p>Yes you are right it’s slow. It has been working on cropping the volume for the last 20 minutes. Not much different from the other computer that had 32 GB RAM but it’s at least doing something. I need a segmentation editor where I can manually draw a shape every few slices, then have the program interpolate between those. For the external volume, I was using segmentation wizard because it was going by pixel brightness and then I was using the volume brush to correct things. I’'ll see if I can do the same in Segment Editor.</p>
<p>Thank you for the tip on deleting the full-volume. I don’t know how to do that but I will figure it out. Thanks again for your help!</p>
<p>Freya</p>

---

## Post #10 by @lassoan (2018-05-22 23:07 UTC)

<aside class="quote no-group" data-username="goetzf" data-post="9" data-topic="2845">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/b38774/48.png" class="avatar"> goetzf:</div>
<blockquote>
<p>Thank you for the tip on deleting the full-volume</p>
</blockquote>
</aside>
<p>Click on the volume node selector and select “Delete”. If “Delete” is not an option there then you can always go to “Data” module, right-click on the volume and click “Delete”.</p>
<aside class="quote no-group" data-username="goetzf" data-post="9" data-topic="2845">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/b38774/48.png" class="avatar"> goetzf:</div>
<blockquote>
<p>I was using segmentation wizard because it was going by pixel brightness and then I was using the volume brush to correct things</p>
</blockquote>
</aside>
<p>You can do all these using Segment editor effects.</p>
<aside class="quote no-group" data-username="goetzf" data-post="9" data-topic="2845">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/b38774/48.png" class="avatar"> goetzf:</div>
<blockquote>
<p>I need a segmentation editor where I can manually draw a shape every few slices, then have the program interpolate between those</p>
</blockquote>
</aside>
<p>This is provided by “Fill between slices” Segment editor effect.</p>

---
