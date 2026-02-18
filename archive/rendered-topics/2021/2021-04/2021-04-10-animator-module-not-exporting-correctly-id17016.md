# Animator Module - Not exporting correctly

**Topic ID**: 17016
**Date**: 2021-04-10
**URL**: https://discourse.slicer.org/t/animator-module-not-exporting-correctly/17016

---

## Post #1 by @ebryson (2021-04-10 04:15 UTC)

<p>Hello! I’m running into a small problem with the Animator module. I’m trying to export a GIF of my model but when I select the directory destination and click export a window showing the GIF pops up, but the file itself doesn’t save anywhere on my computer. Any thoughts?</p>
<p>Thanks! Here’s a screenshot of my settings, maybe that’s where I went wrong…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07a75c0ebf437d6d2c4da453674664104dc1a31a.jpeg" data-download-href="/uploads/short-url/15HUkAElLc3226mIZZ8BhRkAudY.jpeg?dl=1" title="Screen Shot 2021-04-10 at 12.11.23 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/07a75c0ebf437d6d2c4da453674664104dc1a31a_2_690x444.jpeg" alt="Screen Shot 2021-04-10 at 12.11.23 AM" data-base62-sha1="15HUkAElLc3226mIZZ8BhRkAudY" width="690" height="444" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/07a75c0ebf437d6d2c4da453674664104dc1a31a_2_690x444.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/07a75c0ebf437d6d2c4da453674664104dc1a31a_2_1035x666.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/07a75c0ebf437d6d2c4da453674664104dc1a31a_2_1380x888.jpeg 2x" data-dominant-color="181817"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-04-10 at 12.11.23 AM</span><span class="informations">3084×1986 319 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2021-04-10 05:35 UTC)

<p>I can’t replicate this on windows. Perhaps FFMPEG library didn’t install correctly? You may want to switch to <code>Screen Capture</code> module and see if ffmpeg library is installed (see below). Normally it should automatically offer to download and install for windows and mac in the first use.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5f0a94782b212860ee0ce250c2f9cd995a170f4.png" data-download-href="/uploads/short-url/uwBjyYsrGzGANaQAZPsBScMumt6.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5f0a94782b212860ee0ce250c2f9cd995a170f4.png" alt="image" data-base62-sha1="uwBjyYsrGzGANaQAZPsBScMumt6" width="530" height="500" data-dominant-color="EDF0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">674×635 27.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After you created the animation, another option is to use the <code>Screen Capture</code> module to save just a series of images, which then you can turn into animated gif or mp4 using other software. See here for more information: <a href="https://github.com/SlicerMorph/Spr_2021/blob/main/Day_2/SlicerAnimator/SlicerAnimator.md#saving-output" class="inline-onebox">Spr_2021/Day_2/SlicerAnimator/SlicerAnimator.md at main · SlicerMorph/Spr_2021 · GitHub</a></p>

---

## Post #3 by @ebryson (2021-04-10 17:35 UTC)

<p>Hello,</p>
<p>I think that’s it! Looks like the FFMPEG library isn’t installed (see below), I’m not sure what that is though so could you tell me how I can  install it?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bffc5e888321eb254830bdd34647156328939eea.png" data-download-href="/uploads/short-url/ronTwotWM85VoSBu0kA6QwAFAi6.png?dl=1" title="Screen Shot 2021-04-10 at 1.33.26 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bffc5e888321eb254830bdd34647156328939eea_2_406x500.png" alt="Screen Shot 2021-04-10 at 1.33.26 PM" data-base62-sha1="ronTwotWM85VoSBu0kA6QwAFAi6" width="406" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bffc5e888321eb254830bdd34647156328939eea_2_406x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bffc5e888321eb254830bdd34647156328939eea_2_609x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bffc5e888321eb254830bdd34647156328939eea_2_812x1000.png 2x" data-dominant-color="3C3C3F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-04-10 at 1.33.26 PM</span><span class="informations">1546×1900 355 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @muratmaga (2021-04-10 18:41 UTC)

<p>Normally, when you try to use the <code>ScreenCapture</code> module the first time and choose the output as mp4, it should normally offer to download and install it automatically.</p>
<p>In your screenshot above, change the output type from Image series to video.</p>
<p>. Can you try that?</p>

---

## Post #5 by @bcolbert (2021-07-10 18:39 UTC)

<p>I seem to be having a similar issue. When I take you advice and select video and then click capture and it prompts me to download ffmpeg. I click yes but the download fails. It does not offer an explanation as to why. Any suggestions?</p>

---

## Post #6 by @pieper (2021-07-10 19:53 UTC)

<p>You can look in the error log to see if there’s info on the ffmpeg install.  Paste the info here and maybe it’s something we can fix.  In any case, you can also install ffmpeg yourself (<a href="http://ffmpeg.org/download.html" class="inline-onebox">Download FFmpeg</a>)</p>

---

## Post #7 by @lassoan (2021-07-12 12:38 UTC)

<p>FFmpeg automatic installation is only available on Windows. For Linux and macOS you need to install it manually as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/screencapture.html#setting-up-ffmpeg">here</a>.</p>
<p>It would be nice if you could implement automatic installation for macOS and send a pull request.</p>

---

## Post #8 by @Fullcalf42 (2022-06-10 00:26 UTC)

<p>I’m having this very same issue. Following the steps now in hopes it works! With SlicerMorph, I animated moving through a thorax in the axial plane to reveal a pulmonary embolism. Animation looks great, appears to export, but is nowhere to be found in the assigned directory. I’m on a Mac Mini OS Monterey.</p>

---

## Post #9 by @muratmaga (2022-06-10 16:01 UTC)

<aside class="quote no-group" data-username="Fullcalf42" data-post="8" data-topic="17016">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/b2d939/48.png" class="avatar"> Fullcalf42:</div>
<blockquote>
<p>h, I animated moving through a thorax in the axial plane to reveal a pulmonary embolism. Animation looks great, appears to export, but is nowhere to be found in the assigned directory. I’m on a Mac Mini OS Monterey.</p>
</blockquote>
</aside>
<p>From this description it sounds like Animator exports the individual frames, but mp4 conversion fails. Is that correct? Are you sure you have the ffmpeg installed?</p>
<p>To verify, go to the <code>ScreenCapture</code> module, expand the <strong>Advanced</strong> options, and see if you have the ffmpeg executable pointing out to the right location. If not, you can I think you can  <a href="https://evermeet.cx/ffmpeg/">here</a>. But I am not a mac user, so I am not certain.</p>

---

## Post #10 by @Fullcalf42 (2022-06-10 18:49 UTC)

<p>Hi Murat,</p>
<p>I was using the SlicerMorph module, not the Animator. I don’t have ffmpeg installed in the Animator module. I tried the Home Brew solution but it didn’t take. I’ll try the other link you shared. Thanks for trying to help me!</p>

---

## Post #11 by @muratmaga (2022-06-10 21:23 UTC)

<p>Slicermorph’s animator module uses screen capture module under the hood, which relies on the ffmpeg to do the conversion. Please download it and set it location in ScreenCapture and then try animator again.</p>

---

## Post #12 by @Fullcalf42 (2022-06-15 02:40 UTC)

<p>Thank you. I will try these solutions when I return to the office. I appreciate the expert tips.</p>

---
