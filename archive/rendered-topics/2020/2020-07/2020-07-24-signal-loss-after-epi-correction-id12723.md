# Signal loss after epi correction

**Topic ID**: 12723
**Date**: 2020-07-24
**URL**: https://discourse.slicer.org/t/signal-loss-after-epi-correction/12723

---

## Post #1 by @mali (2020-07-24 15:41 UTC)

<p>Dear Slicer community,</p>
<p>I hope you can help me with an issue I am struggling with. Iam currently working on DTI scans using Slicer and the PNL Pipeline. After applying epi correction (epi.sh) I am getting images that look a lot different and display much less glyphs in the DTI volume (see screenshots). <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fabee450b037eec83f85b94a90cd0e9757e6684b.jpeg" data-download-href="/uploads/short-url/zMclNgXqHzLQLBt6RZKYOGEUVXt.jpeg?dl=1" title="Screenshot-pre-epi" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fabee450b037eec83f85b94a90cd0e9757e6684b_2_690x388.jpeg" alt="Screenshot-pre-epi" data-base62-sha1="zMclNgXqHzLQLBt6RZKYOGEUVXt" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fabee450b037eec83f85b94a90cd0e9757e6684b_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fabee450b037eec83f85b94a90cd0e9757e6684b_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fabee450b037eec83f85b94a90cd0e9757e6684b_2_1380x776.jpeg 2x" data-dominant-color="7C7F7E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot-pre-epi</span><span class="informations">1920×1080 1.2 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Have you experienced this and know what the problem could be?<br>
I really appreciate any advice! Thanks a lot in advance!</p>
<p>Best wishes,<br>
Marlene</p>

---

## Post #2 by @tbillah (2020-07-24 20:12 UTC)

<p>Hi <a class="mention" href="/u/marlene">@marlene</a>,</p>
<p>Thanks for your question. PNL is a different entity from Slicer <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> Please report issues related to PNL pipeline <a href="https://github.com/pnlbwh/pnlpipe/issues" rel="nofollow noopener">here</a>.</p>

---

## Post #3 by @tbillah (2020-07-24 20:15 UTC)

<p>That being said, we don’t support shell scripts (.sh extension) as part of our pipeline anymore. Please use <a href="https://github.com/pnlbwh/pnlpipe/blob/py3-compatible/pnlscripts/epi.py" rel="nofollow noopener">https://github.com/pnlbwh/pnlpipe/blob/py3-compatible/pnlscripts/epi.py</a> and report your observation back. Then we can try to answer your question.</p>

---

## Post #4 by @zhangfanmark (2020-07-24 21:39 UTC)

<p>Hi <a class="mention" href="/u/mali">@mali</a> It is hard to tell what is going wrong. As far as I know, the epi.sh code is computing a nonlinear registration between b0 and T1(or T2), then applying the transform to all gradient images. It could be something happening when do the transform interpolation. Your corrected DTI map seems to be very noisy. Anyway, I would suggest trying the code that Tashrif pointed out.</p>
<p>Regards,<br>
Fan</p>

---

## Post #5 by @mali (2020-07-25 20:05 UTC)

<p>Thank you Fan, I will try to do so.<br>
Best wishes,<br>
Marlene</p>

---

## Post #6 by @mali (2020-07-25 20:06 UTC)

<p>Thank you Tashrif,</p>
<p>I will try this and report back.</p>
<p>Best wishes,<br>
Marlene</p>

---
