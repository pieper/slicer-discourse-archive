---
topic_id: 611
title: "Low Frame Rate Of Real Time Ultrasound Image Display"
date: 2017-07-01
url: https://discourse.slicer.org/t/611
---

# Low frame rate of real-time ultrasound image display

**Topic ID**: 611
**Date**: 2017-07-01
**URL**: https://discourse.slicer.org/t/low-frame-rate-of-real-time-ultrasound-image-display/611

---

## Post #1 by @Fatemeh_Salehi (2017-07-01 14:40 UTC)

<p>Hello!</p>
<p>I’m really interested in using your plus application and slicerIGT and also read most of your manual guide files but unfortunately i have a problem in my first step.I want to use telemed for record data and when  I see its result in echo wave its OK and images are continual but when i run plus and see output in 3d slicer(slicerIGT) it  has delay and is slow and images not sequential.Please help me to fix this problem.</p>
<p>I would be very grateful for your kind help.</p>

---

## Post #2 by @lassoan (2017-07-01 14:48 UTC)

<p>We usually don’t experience significantly lower frame rate in Slicer than in Telemeed EchoWave.</p>
<p>What is your update rate? (you can get it by installing <code>Debugging tools</code> extension in Slicer; start <code>Node modified statistics</code> module, select your image node, and click <code>Compute statistics</code>).</p>
<p>Are you running Slicer and EchoWave on the same computer?</p>
<p>Please also add to your answer: Plus config file, Slicer application log (menu: Help / Report a bug), and a screenshot of the Slicer screen.</p>

---

## Post #3 by @Fatemeh_Salehi (2017-07-03 11:09 UTC)

<p>Thanks a lot for your prompt reply<br>
i have attached whatever you said and also short videos of slicer and echo wave.<br>
Yes we are running them on the same computer.<br>
I have short videos of slicer and echo wave response if you insert an email i can send them too.<br>
<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/7549c432167e6ef42428ef7f5c909c8068c70d08.png" data-download-href="/uploads/short-url/gJzUhANrXij4ZMmbWJ4Q4FhP7eM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/7549c432167e6ef42428ef7f5c909c8068c70d08.png" alt="image" data-base62-sha1="gJzUhANrXij4ZMmbWJ4Q4FhP7eM" width="690" height="454" data-dominant-color="F4F1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1000×658 40.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Fatemeh_Salehi (2017-07-08 20:27 UTC)

<p>I have attached whatever you said and also short videos of slicer and echo wave.<br>
Yes we are running them on the same computer.<br>
I have short videos of slicer and echo wave response if you insert an email i can send them too.<br>
(Reminder)</p>

---

## Post #5 by @lassoan (2017-07-09 11:50 UTC)

<p>Screenshots of the log files show a small fraction of the log file content. Please provide the log files themselves (upload them to Dropbox or OneDrive and copy the link here).</p>
<p>Also, please try it with latest nightly version of Slicer and Plus. It works reliably and several fixes and improvements have been implemented since the last stable version.</p>

---

## Post #6 by @Fatemeh_Salehi (2017-07-10 07:23 UTC)

<p>Thanks…links of log files : <a href="https://drive.google.com/file/d/0B2z7D55qZUFQZF9JVjlrUks1VXc/view?usp=sharing" rel="nofollow noopener">https://drive.google.com/file/d/0B2z7D55qZUFQZF9JVjlrUks1VXc/view?usp=sharing</a></p>
<p><a href="https://drive.google.com/file/d/0B2z7D55qZUFQWUZFNEItRmFWSFU/view?usp=sharing" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/file/d/0B2z7D55qZUFQWUZFNEItRmFWSFU/view?usp=sharing</a></p>
<p>Also we have already tried latest nightly Slicer and Plus.</p>

---

## Post #7 by @Fatemeh_Salehi (2017-07-18 11:59 UTC)

<p>Thanks…links of log files : <a href="https://drive.google.com/file/d/0B2z7D55qZUFQZF9JVjlrUks1VXc/view?usp=sharing2" rel="nofollow noopener">https://drive.google.com/file/d/0B2z7D55qZUFQZF9JVjlrUks1VXc/view?usp=sharing2</a></p>
<p><a href="https://drive.google.com/file/d/0B2z7D55qZUFQWUZFNEItRmFWSFU/view?usp=sharing" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/file/d/0B2z7D55qZUFQWUZFNEItRmFWSFU/view?usp=sharing</a></p>
<p>Also we have already tried latest nightly Slicer and Plus.<br>
(reminder)</p>

---

## Post #8 by @lassoan (2017-07-18 12:52 UTC)

<p>Please provide the followings:</p>
<ul>
<li>Slicer log file - using latest nightly version (the log file you attached was for Slicer 4.6.2)</li>
<li>Plus log file - using latest development snapshot of Plus. Set log level to DEBUG.<br>
Thanks!</li>
</ul>

---

## Post #9 by @Fatemeh_Salehi (2017-07-23 11:53 UTC)

<p>thanks alot  for your help<br>
<a href="https://drive.google.com/file/d/0B2z7D55qZUFQMWFzclFoekhlWHM/view?usp=sharing" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/file/d/0B2z7D55qZUFQMWFzclFoekhlWHM/view?usp=sharing</a></p>
<p><a href="https://drive.google.com/file/d/0B2z7D55qZUFQWEJoeVdxWDBtMUk/view?usp=sharing" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/file/d/0B2z7D55qZUFQWEJoeVdxWDBtMUk/view?usp=sharing</a></p>

---
