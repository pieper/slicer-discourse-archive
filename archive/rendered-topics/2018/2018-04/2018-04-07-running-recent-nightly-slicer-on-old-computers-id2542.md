---
topic_id: 2542
title: "Running Recent Nightly Slicer On Old Computers"
date: 2018-04-07
url: https://discourse.slicer.org/t/2542
---

# Running recent nightly Slicer on old computers

**Topic ID**: 2542
**Date**: 2018-04-07
**URL**: https://discourse.slicer.org/t/running-recent-nightly-slicer-on-old-computers/2542

---

## Post #1 by @Bio_Medical (2018-04-07 08:47 UTC)

<p>i HAVE DOWNLOADED RECent nightly build version but it is not working.Doesnt open when i start <a href="http://slicer.is" rel="nofollow noopener">slicer.is</a> there any previous version of nightlybuild(although ive seen some older releases of stable version on 3d slicer website).how can i make it to work.<br>
THANKYOU</p>

---

## Post #2 by @lassoan (2018-04-07 14:30 UTC)

<p>We have increased minimum graphics card requirement in recent nightly builds. This allows us to make Slicer run magnitudes faster on modern hardware, but sadly it also means that it is less compatible with old hardware. Latest Slicer version may not work on computers that are more then 10 years old or still using operating systems that were discontinued many years ago (such as Windows XP).</p>
<p>How old is the computer and what operating system and graphics card do you have?</p>

---

## Post #3 by @Bio_Medical (2018-04-09 05:12 UTC)

<p>Thankyou very much <a class="mention" href="/u/lassoan">@lassoan</a> for your response.<br>
My laptop is ‘Toshiba satellite a665’.<br>
Operating System:Window 7<br>
Graphic card:intel r hd graphics (core i3)<br>
I have removed all previous versions of 3D slicer from my computer and have re-installed nightly build version,but it just dont open up.<br>
Best regards,</p>

---

## Post #4 by @lassoan (2018-04-09 16:01 UTC)

<aside class="quote no-group" data-username="Bio_Medical" data-post="3" data-topic="2542">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/f14d63/48.png" class="avatar"> Bio_Medical:</div>
<blockquote>
<p>My laptop is ‘Toshiba satellite a665’.</p>
</blockquote>
</aside>
<p>This model was released 8 years ago. OpenGL support of Intel graphics cards was really bad at that time. Many software with above-average graphics requirements did not run correctly even then (see for example <a href="https://www.opengl.org/discussion_boards/showthread.php/173409-Intel-GMA-HD-and-OpenGL/">here</a>).</p>
<p>You might need to upgrade your laptop to use latest versions of Slicer.</p>

---

## Post #5 by @MichaelMoran96 (2019-01-10 01:15 UTC)

<p>Hi thanks for the above info, do you know if any older versions of slicer will run on intel r hd graphics card? your help is much appreciated</p>

---

## Post #6 by @lassoan (2019-01-10 02:07 UTC)

<p>Slicer-4.8 should work with any computer that you bought in the last 10-15 years. You can download these older releases by clicking “older releases” on the <a href="https://download.slicer.org/" rel="nofollow noopener">Slicer download page</a>.</p>
<p>However, it would be terrible to even think about it that you would go back to old Slicer versions, ignoring all the hard work that we put into fixing and improving Slicer and making your work much more difficult and less efficient, just so that you can use an old computer. Any laptop that you bought in the last 5 years should be able to run Slicer’s latest version.</p>

---

## Post #7 by @MichaelMoran96 (2019-01-10 12:44 UTC)

<p>Thanks for the reply, my project is starts around March/April so more than likely i will have a new laptop purchased by then(yoga 920).  I just want to look at the slicer program,as i write up my lit-review.  thanks again for the reply</p>

---
