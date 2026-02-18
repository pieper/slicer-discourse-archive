# 3D Slicer 5.2.2 not responding for 2 hours

**Topic ID**: 29613
**Date**: 2023-05-23
**URL**: https://discourse.slicer.org/t/3d-slicer-5-2-2-not-responding-for-2-hours/29613

---

## Post #1 by @TiniNant (2023-05-23 20:28 UTC)

<p>Has anyone encountered the same problem or could find a solution to fix the following problem:<br>
3D slicer does not respond after 5 to 6 minutes of running. Then after 1 hour, it responds for 4 seconds and then doesn’t respond anymore again. 50 minutes later, it finally responds and I can work on it.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8eaaaf49d50700bc8435695758a7bd24e55345b.jpeg" data-download-href="/uploads/short-url/zw1bxnEQ2umVcJsnDkS4YzA08dR.jpeg?dl=1" title="timer slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8eaaaf49d50700bc8435695758a7bd24e55345b.jpeg" alt="timer slicer" data-base62-sha1="zw1bxnEQ2umVcJsnDkS4YzA08dR" width="667" height="500" data-dominant-color="868386"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">timer slicer</span><span class="informations">1030×771 54.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50b17744a369d99260495fd542a37cb07dd0485a.jpeg" data-download-href="/uploads/short-url/bvQpPeuiogSgbOhNcOTvq2npC1s.jpeg?dl=1" title="348356123_240975531961900_1618993588413182923_n" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50b17744a369d99260495fd542a37cb07dd0485a_2_644x500.jpeg" alt="348356123_240975531961900_1618993588413182923_n" data-base62-sha1="bvQpPeuiogSgbOhNcOTvq2npC1s" width="644" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50b17744a369d99260495fd542a37cb07dd0485a_2_644x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50b17744a369d99260495fd542a37cb07dd0485a_2_966x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50b17744a369d99260495fd542a37cb07dd0485a_2_1288x1000.jpeg 2x" data-dominant-color="939395"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">348356123_240975531961900_1618993588413182923_n</span><span class="informations">1573×1221 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ul>
<li>The version of 3D slicer that I use: 5.2.2 (I also tested with Slicer 5.0.2 but same problem)</li>
<li>The operating system: windows 11 enterprise version 22H2</li>
<li>Laptop model : Dell XPS 9315, 12th Gen Intel(R) Core™ i7-1250U 1.10 GHz processor and 32GB RAM, with Intel(R) Iris (R) Xe Graphics card</li>
</ul>
<p>I would like to specify that this problem is encountered on 2 PCs of the same model and same configuration</p>

---

## Post #2 by @muratmaga (2023-05-23 20:40 UTC)

<p>Most likely a driver issue. This is a tiny sample dataset that works well with even 10 year old laptops with that specific version of the slicer.</p>
<p>I wonder if it is the Intel GPU causing the problem.</p>

---

## Post #3 by @lassoan (2023-05-23 22:24 UTC)

<p>Does Slicer become non-responsive after you enable volume rendering? Is the behavior the same if you switch between CPU and GPU volume rendering technique?<br>
Do you see errors or warnings in the application log?<br>
Does the resource monitor show excessive resource usage (memory or CPU)?</p>

---

## Post #4 by @TiniNant (2023-05-23 23:25 UTC)

<p>Slicer doesn’t respond after 5 minutes even if I don’t load a data. And there is no errors nor warning. The resource monitor does not show excessive resource usage.<br>
However, I tested running Slicer as an administrator, and there seems to be no more problems. It works very well.<br>
But I don’t understand the relation with slicer which doesn’t respond if I don’t run it as administrator</p>

---

## Post #5 by @lassoan (2023-05-24 00:04 UTC)

<p>Maybe you have some overly aggressive antivirus software installed.</p>

---

## Post #6 by @muratmaga (2023-05-24 03:53 UTC)

<aside class="quote no-group" data-username="TiniNant" data-post="4" data-topic="29613">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tininant/48/15960_2.png" class="avatar"> TiniNant:</div>
<blockquote>
<p>Slicer doesn’t respond after 5 minutes even if I don’t load a data.</p>
</blockquote>
</aside>
<p>This is obviously not a normal behavior. But will be a little hard to chase. Is this by any chance a company/school managed device?</p>

---

## Post #7 by @TiniNant (2023-05-24 04:26 UTC)

<p>yes, it’s school managed device<br>
But now, if I run it as administrator, there is no more problem.</p>

---

## Post #8 by @muratmaga (2023-05-24 04:57 UTC)

<p>That pretty much tells me whatever policy they are applying to normal users is interfering with Slicer:s normal operations. Slicer does not require admin privileges for anything. Most likely a different policy is being applied when you are running as administrator.</p>

---

## Post #9 by @TiniNant (2023-05-24 13:49 UTC)

<p>You are right. And when I use the school’s VPN, slicer works even if I don’t run it as administrator<br>
Thank you very much for your answer</p>

---
