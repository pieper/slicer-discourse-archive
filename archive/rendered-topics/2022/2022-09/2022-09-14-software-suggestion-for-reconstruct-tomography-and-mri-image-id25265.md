---
topic_id: 25265
title: "Software Suggestion For Reconstruct Tomography And Mri Image"
date: 2022-09-14
url: https://discourse.slicer.org/t/25265
---

# Software suggestion for reconstruct tomography and MRI images

**Topic ID**: 25265
**Date**: 2022-09-14
**URL**: https://discourse.slicer.org/t/software-suggestion-for-reconstruct-tomography-and-mri-images/25265

---

## Post #1 by @alfredo (2022-09-14 14:27 UTC)

<p>Hi,<br>
I am new to this community. I am a medical student who is getting into radiology and I am looking for software that can open standard DICOM files and reconstruct tomography and MRI images.<br>
I have found many examples both open source (3D Slicer, Invesalius) and proprietary (Osiris X, Pro Surgical 3D, Radi Ant).<br>
In general I would like to avoid the vendor lock-in typical of proprietary software, but at the same time I would like to learn how to use a high-quality solution.<br>
I know you are probably not impartial, however which software would you suggest I use?<br>
Thank you</p>

---

## Post #2 by @muratmaga (2022-09-14 16:01 UTC)

<aside class="quote no-group" data-username="alfredo" data-post="1" data-topic="25265">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/e495f1/48.png" class="avatar"> alfredo:</div>
<blockquote>
<p>In general I would like to avoid the vendor lock-in typical of proprietary software, but at the same time I would like to learn how to use a high-quality solution.</p>
</blockquote>
</aside>
<p>When you left proprietary software out, I am not sure if there is any other biomedical visualization tool that offers the features and flexibility of 3D Slicer (yes, I am definitely not impartial).</p>

---

## Post #3 by @alfredo (2022-09-15 06:02 UTC)

<p>OK, I guess. However, how do the various solutions compare in terms of functionality, performance and usability? Which one has a less steep learning curve?<br>
Thank you</p>

---

## Post #4 by @hherhold (2022-09-15 10:37 UTC)

<p>I’m in an environment where people use multiple solutions for CT analysis, and we have these discussions All The Time.</p>
<p>Having used several of the solutions you’ve mentioned above, <em>all</em> of them have a learning curve, as does any complex program for 3D analysis/visualization/etc. I would say Slicer is no different than any other program in that regard. In particular, Slicer takes a different approach in that Slicer is based on separate modules designed to perform a specific function. The Volume Rendering module is active when you’re doing volume rendering, and (nearly) all visible controls are dedicated to that task. The Segment Editor module is active when you’re segmenting, and (likewise) the UI is “switched over” to that task. This is a different approach than other apps, where all user interface controls are available all the time. This can be a bit of a shift in mindset, but in my experience it lends itself well to a more easily digestible experience (and arguably better productivity, but that’s harder to quantify), as there aren’t 175 buttons on the screen, only 10 of which you want at any given time. But this is a personal choice, and only you can answer what works best for you.</p>
<p>Performance is often a function of the hardware being used. Slicer’s requirements are surprisingly open given the functionality - several high-cost solutions require validated graphics cards, etc. Slicer has no such requirements. System recommendations are discussed often on the forums and are described in the documentation online.</p>
<p>I would say more important questions to answer could be:</p>
<ol>
<li>What are you collaborators most likely to use?</li>
<li>Are you likely to have access to resources to use whatever software (and hardware) you choose for longer than you anticipate?</li>
<li>Do you have any experience in programming (or any interest)? 3D Slicer is open-source and infinitely customizable, with an involved and vibrant community. This may or may not be a plus to you.</li>
</ol>
<p>At any rate, I hope some of this helps. Best of luck on your search.</p>

---

## Post #5 by @lassoan (2022-09-16 04:51 UTC)

<aside class="quote no-group" data-username="alfredo" data-post="1" data-topic="25265">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/e495f1/48.png" class="avatar"> alfredo:</div>
<blockquote>
<p>I am a medical student who is getting into radiology and I am looking for software that can open standard DICOM files and reconstruct tomography and MRI images</p>
</blockquote>
</aside>
<p>For basic image viewing you’ll probably use whatever your hospital provides. You can get your own viewer, such as Weasis, Osirix ($), or RadiAnt ($), but they are probably not much better than what you already get from the hospital, and IT people may not like (and may be less convenient for you) that you need to download DICOM files from the PACS and install your own viewer software.</p>
<p>For advanced 3D analysis there are much less software around. Commercial solutions usually offer very convenient, polished solutions for very specific problems, and they are very expensive (typically tens of thousands $ per year). So, you typically don’t buy these software yourself but use whatever is available at your institution. If you move to a different place they may use something else (so the time that you invested into learning that software may be wasted). Also, commercial software usually use proprietary file formats, so if you move somewhere else or cancel the subscription then you may not have access to your data anymore.</p>
<p>Overall, if you want to learn an advanced radiology image analysis software that you can rely on the long term, no matter where you are and what your institution pays for, and you want to have access to your data in standard open formats forever, then 3D Slicer is a very good choice. I don’t think any other free open-source software comes even close. It is also fully open, extensible, customizable to do exactly what you need with a bit of Python scripting (there are a number of MDs here who write script themselves and you can always collaborate with other researchers or developers to implement any new ideas that you may have).</p>

---
