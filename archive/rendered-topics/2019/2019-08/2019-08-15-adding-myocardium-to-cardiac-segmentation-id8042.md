---
topic_id: 8042
title: "Adding Myocardium To Cardiac Segmentation"
date: 2019-08-15
url: https://discourse.slicer.org/t/8042
---

# Adding myocardium to cardiac segmentation

**Topic ID**: 8042
**Date**: 2019-08-15
**URL**: https://discourse.slicer.org/t/adding-myocardium-to-cardiac-segmentation/8042

---

## Post #1 by @sarvpriya1985 (2019-08-15 03:08 UTC)

<p>Hi everyone,<br>
I recently found a video link on youtube to add myocardium to cardiac segmentation<a href="https://youtu.be/HVoeJNrIRdE" rel="noopener nofollow ugc">(adding myocardium)</a>. I tried repeating steps in segment editor but running into some issues.</p>
<ol>
<li>First step: Segmented blood pool using threshold.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d38d989f52d7d16ef1d6aedc58330e431f4f17ee.jpeg" data-download-href="/uploads/short-url/ubu76Qju4bJRkVRgeR5KQbLVmnY.jpeg?dl=1" title="Capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d38d989f52d7d16ef1d6aedc58330e431f4f17ee_2_690x358.jpeg" alt="Capture2" data-base62-sha1="ubu76Qju4bJRkVRgeR5KQbLVmnY" width="690" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d38d989f52d7d16ef1d6aedc58330e431f4f17ee_2_690x358.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d38d989f52d7d16ef1d6aedc58330e431f4f17ee_2_1035x537.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d38d989f52d7d16ef1d6aedc58330e431f4f17ee_2_1380x716.jpeg 2x" data-dominant-color="909398"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2</span><span class="informations">1915×995 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
<li>Then added this segment (green) to a new segment (yellow)<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf363cb306a67a984bede6b38ccbdfff4da56056.jpeg" data-download-href="/uploads/short-url/tz52pkBLPHYNpZTS0ESzric21DM.jpeg?dl=1" title="Capture3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf363cb306a67a984bede6b38ccbdfff4da56056_2_690x356.jpeg" alt="Capture3" data-base62-sha1="tz52pkBLPHYNpZTS0ESzric21DM" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf363cb306a67a984bede6b38ccbdfff4da56056_2_690x356.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf363cb306a67a984bede6b38ccbdfff4da56056_2_1035x534.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf363cb306a67a984bede6b38ccbdfff4da56056_2_1380x712.jpeg 2x" data-dominant-color="939497"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture3</span><span class="informations">1915×989 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
<li>Then hollow the new yellow segment![Capture4|690x355]<br>
(upload://oiuqXJ6rDUn5gVXnq0VFtRCpL3z.jpeg)</li>
<li>Then subtracted green from yellow segment to have only outer wall<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d56d1985ca0e51b671f0b29800800f1d755294f4.jpeg" data-download-href="/uploads/short-url/us3rFj64dg3CszCMOCfwwXqJJ9W.jpeg?dl=1" title="Capture5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d56d1985ca0e51b671f0b29800800f1d755294f4_2_690x357.jpeg" alt="Capture5" data-base62-sha1="us3rFj64dg3CszCMOCfwwXqJJ9W" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d56d1985ca0e51b671f0b29800800f1d755294f4_2_690x357.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d56d1985ca0e51b671f0b29800800f1d755294f4_2_1035x535.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d56d1985ca0e51b671f0b29800800f1d755294f4_2_1380x714.jpeg 2x" data-dominant-color="919398"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture5</span><span class="informations">1917×993 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> This didn’t show any difference.</li>
<li>Then i added another segment. And use thresholding to  a create a mask for myocardium. And used it as a mask. Then used pain tool to draw covering myocardium as well as blood pool as shown in video (pls see link)</li>
<li>However after that i am seeing that my segmentation for ventricles is gone and all I am seeing is myocardial segmentation.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6fd9af93b87e322487ba0ecba61da7032e33807.jpeg" data-download-href="/uploads/short-url/zeYNTll4r3YSRCTKE7vn05FB1vV.jpeg?dl=1" title="Capture7" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6fd9af93b87e322487ba0ecba61da7032e33807_2_690x357.jpeg" alt="Capture7" data-base62-sha1="zeYNTll4r3YSRCTKE7vn05FB1vV" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6fd9af93b87e322487ba0ecba61da7032e33807_2_690x357.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6fd9af93b87e322487ba0ecba61da7032e33807_2_1035x535.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6fd9af93b87e322487ba0ecba61da7032e33807_2_1380x714.jpeg 2x" data-dominant-color="9C9892"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture7</span><span class="informations">1917×994 215 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
<li>The steps after this in video include- Adding myocardium to first the heart outer surface (that was the reason I tried to subtract, so as to have the outer segment only. They do this by Boolean Union.</li>
<li>Then they add hollow segment to previous step. This all creates a hollow model with myocardium too.</li>
</ol>
<p>I am not sure which step i did wrong, so have tried to attach all screenshots. I am unable to proceed after myocardial segmentation as my previous segmentation gets removed.</p>
<p>Would appreciate any help. The video link is short only about 6 minutes.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #2 by @lassoan (2019-08-15 03:32 UTC)

<p>Probably the easiest way to segment the myocardium is to segment the entire heart (make sure to to adjust masking settings to allow overlap between segments, otherwise your blood pool segments will be overwritten), then subtract the blood pool.</p>
<p>This heart segmentation tutorial includes myocardium segmentation (starting from 11:05):</p>
<div class="lazyYT" data-youtube-id="BJoIexIvtGo" data-youtube-title="Whole heart segmentation from cardiac CT in 10 minutes" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #3 by @sarvpriya1985 (2019-08-15 13:31 UTC)

<p>Thanks Andras. I did look at that.<br>
What I was wondering after adding myocardium (pericardium in the slicer video), how would I combine the hollow heart to myocardium. Do I need to add blood pool also in that union (as shown in the link I shared) or not. I was missing the sequence of events that need union (Thanks for the tip of changing masking segment! I atleast can now add without overwriting other segment. Also when you say “allow overlap” between segments, does that mean I need to pick option “none” in the overwrite menu?</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #4 by @lassoan (2019-08-15 14:13 UTC)

<aside class="quote no-group" data-username="sarvpriya1985" data-post="3" data-topic="8042">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar"> sarvpriya1985:</div>
<blockquote>
<p>would I combine the hollow heart to myocardium</p>
</blockquote>
</aside>
<p>Yes, you can subtract the segmented blood pool from the entire heart segment. [quote=“sarvpriya1985, post:3, topic:8042”]<br>
Also when you say “allow overlap” between segments, does that mean I need to pick option “none” in the overwrite menu?<br>
[/quote]</p>
<p>Yes. The options are renamed in recent Preview Release to make them more explicit.</p>

---

## Post #5 by @sarvpriya1985 (2019-08-15 14:20 UTC)

<p>Thanks Andras.</p>
<p>I will try that and get back.</p>
<p>Sarv</p>

---
