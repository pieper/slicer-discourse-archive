# How to access/get to the scale space particles system?

**Topic ID**: 13675
**Date**: 2020-09-23
**URL**: https://discourse.slicer.org/t/how-to-access-get-to-the-scale-space-particles-system/13675

---

## Post #1 by @shahrokh (2020-09-23 15:16 UTC)

<p>Hello Dear Developers and Users</p>
<p>Excuse me for asking this question again. I asked this question in <strong>3Dslicer Support</strong> but did not receive any answer or guidance.</p>
<p>How can I access <strong>the scale space particles</strong> ?<br>
I found out that this technique is used in <strong>SlicerCIP</strong>.<br>
Is it possible to get this particle system for the further processing?<br>
On what images is it possible to extract this particle system?</p>
<p>According to article entitled <strong>Sampling and Visualizing Creases with Scale-Space Particles</strong> and author Kindlmann et al (2009), and description on the site of <a href="http://people.cs.uchicago.edu/~glk/ssp/" rel="noopener nofollow ugc">Scale-Space Particles: Paper and Software</a>, I install <a href="http://teem.sourceforge.net/" rel="noopener nofollow ugc">teem</a> but I do not know how to use it for extraction of <strong>scale space particles system</strong>.</p>
<p>please guide me. In this case, I have no idea how to do it.<br>
Thanks a lot.<br>
Shahrokh</p>

---

## Post #2 by @shahrokh (2020-09-21 16:02 UTC)

<p>Hello Dear Developers and Users</p>
<p>How can I access <strong>the scale space particles</strong>?<br>
I found out that this technique is used in SlicerCIP.<br>
Is it possible to get this particle system for the further processing?<br>
On what images is it possible to extract this particle system?</p>
<p>please guide me. In this case, I have no idea how to do it.<br>
Thanks a lot.<br>
Shahrokh</p>

---

## Post #3 by @shahrokh (2020-09-29 11:10 UTC)

<p>Hello Dear Developers and Users</p>
<p>In the <strong>Particles</strong> module, which is a subset of the <strong>Chest Imaging Platform</strong> module, I see that the information of particles  must be available as input in the <strong>Input Particles FileName</strong> section.</p>
<p>The question that arises here is that this information (particles) <strong>how</strong> and by <strong>what</strong> the module is produced.</p>
<p>Please guide me. I did not find any document on this subject.</p>
<p>I asked this question in <a href="https://discourse.slicer.org/t/how-to-access-get-to-the-scale-space-particles/13591">3DSlicer Support</a> and  the <a href="https://discourse.slicer.org/t/how-to-access-get-to-the-scale-space-particles-system/13675">Community of 3DSlicer</a>, but unfortunately I do not get any feedback.</p>
<p>Also today I expressed my problems about teem building in <a href="https://sourceforge.net/p/teem/mailman/teem-users/?viewmonth=202009" rel="noopener nofollow ugc">teem-users</a>.</p>
<p>Excuse me, perhaps I’m making a mistake and being careless.<br>
Please guide me.</p>
<p>Please guide me.<br>
Shahrokh</p>

---

## Post #4 by @lassoan (2020-09-29 13:01 UTC)

<p>Since the work was published more than 10 years ago, people who worked on it have already moved on to other projects, became professors, managers, etc. so it is unlikely that they will find your question or have time to answer, and probably all they could offer is vague memories. So, most likely you need to do your own research, try to read all documentations and examples that you can find, run and debug them, see how they work.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> It seems that Alex worked on <a href="https://github.com/acil-bwh/SlicerCIP/tree/Slicer-CIP/Loadable/ParticlesDisplay">particle display in Slicer</a> 5-6 years ago. Do you remember anything about how it worked?</p>

---

## Post #5 by @pieper (2020-09-29 13:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="13675">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/pieper">@pieper</a> It seems that Alex worked on <a href="https://github.com/acil-bwh/SlicerCIP/tree/Slicer-CIP/Loadable/ParticlesDisplay">particle display in Slicer</a> 5-6 years ago. Do you remember anything about how it worked?</p>
</blockquote>
</aside>
<p>Only my own vague recollections.  I wasn’t involved.</p>
<p><a class="mention" href="/u/shahrokh">@shahrokh</a> I concur with <a class="mention" href="/u/lassoan">@lassoan</a>’s description of the situation.  As you have seen, there’s a community here who are more than willing to share their time and experience but sometimes you don’t get an answer because nobody is familiar with the details and they have their own pressing responsibilities.  We appreciate your participation in the community and hope you understand that not all questions can be answered.</p>
<p>I agree that the scale space particle approach is really cool work.  We are fortunate that the authors made their work available for us to study and use.  If you can research how to make it work it would be great if you can document your efforts and share with others who might have similar questions in the future.</p>

---

## Post #6 by @shahrokh (2020-11-18 10:43 UTC)

<p>Hello Dear Dr. Andras Lasso and Dear Dr. Steve Pieper</p>
<p>With the guidance and support of Dr. Raúl San José Estépar and Dr. Pietro Nardelli, I was able to extract the particle system for the pulmonary arteries.<br>
The steps for running along with tips for solving errors, on Ubuntu, are provided on the <a href="https://groups.google.com/g/chestimagingplatform-users/c/KO68D66yt0o" rel="noopener nofollow ugc">ChestImagingPlatform-users</a> site.</p>
<p>Best regards.<br>
Shahrokh.</p>

---

## Post #7 by @pieper (2020-11-18 14:12 UTC)

<p>Nice!  Thanks for following up.</p>

---
