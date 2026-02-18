# Create sphere with designated center point

**Topic ID**: 33153
**Date**: 2023-11-30
**URL**: https://discourse.slicer.org/t/create-sphere-with-designated-center-point/33153

---

## Post #1 by @lccmyers (2023-11-30 20:42 UTC)

<p>I’d like to know how to create a sphere with customizable size with the centroid of the sphere being a designated markup point, any ideas?</p>

---

## Post #2 by @chir.set (2023-11-30 22:06 UTC)

<aside class="quote no-group" data-username="lccmyers" data-post="1" data-topic="33153">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/848f3c/48.png" class="avatar"> lccmyers:</div>
<blockquote>
<p>customizable size with the centroid of the sphere being a designated markup point</p>
</blockquote>
</aside>
<p>You may install the ‘ExtraMarkups’ extension using the ‘Extensions manager’. It provides the ‘Shape’ custom markups that does that.</p>

---

## Post #3 by @lccmyers (2023-11-30 22:15 UTC)

<p>Great, thank you! If I have a point that I want to be the center of the sphere, how do I designate that point as the center? I took a look at the documentation for the extension but wasn’t able to figure it out.</p>

---

## Post #4 by @chir.set (2023-12-01 08:19 UTC)

<p>Control points of markups nodes are <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#edit-control-point-positions-in-existing-markups" rel="noopener nofollow ugc">movable</a> using the mouse. Just place the centre of the sphere on your target point.</p>

---

## Post #5 by @chir.set (2023-12-01 16:57 UTC)

<aside class="quote no-group" data-username="lccmyers" data-post="3" data-topic="33153">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/848f3c/48.png" class="avatar"> lccmyers:</div>
<blockquote>
<p>If I have a point</p>
</blockquote>
</aside>
<p>If you mean that you know the coordinates of the point as [r, a, s], just enter these values in the ‘Markups’ module’s widget, for the first point if the sphere is in ‘Centered mode’.</p>

---

## Post #6 by @lassoan (2023-12-03 02:14 UTC)

<p>There are also several examples for this in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#define-edit-a-circular-region-of-interest-in-a-slice-viewer">script repository</a>.</p>

---

## Post #7 by @philippepellerin (2023-12-03 10:59 UTC)

<p>Great, this markup add is very usefull, thanks again.</p>

---

## Post #8 by @lccmyers (2023-12-04 19:11 UTC)

<p>Thank you everyone for the help! I’m attempting to download the “ExtraMarkups” extension and it doesn’t seem to be working. Here’s a photo of what my markups view should look like first, and then what mine looks like after installing the extension second.</p>
<p>What it should be:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/062cf81d2db1ad95bd3f0ea674fb611bc109a795.png" data-download-href="/uploads/short-url/SDd4CoQN1lvmB0BbVaitESgEsd.png?dl=1" title="Screenshot 2023-12-04 at 12.59.01 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/062cf81d2db1ad95bd3f0ea674fb611bc109a795_2_690x391.png" alt="Screenshot 2023-12-04 at 12.59.01 PM" data-base62-sha1="SDd4CoQN1lvmB0BbVaitESgEsd" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/062cf81d2db1ad95bd3f0ea674fb611bc109a795_2_690x391.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/062cf81d2db1ad95bd3f0ea674fb611bc109a795.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/062cf81d2db1ad95bd3f0ea674fb611bc109a795.png 2x" data-dominant-color="424549"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-12-04 at 12.59.01 PM</span><span class="informations">836×474 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What mine is:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22c97534133730a6d1688161edb75147a2e8063c.png" data-download-href="/uploads/short-url/4XJR28WGDpb2t7B2Tb6eErbp0Mk.png?dl=1" title="Screenshot 2023-12-04 at 12.59.06 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22c97534133730a6d1688161edb75147a2e8063c_2_690x213.png" alt="Screenshot 2023-12-04 at 12.59.06 PM" data-base62-sha1="4XJR28WGDpb2t7B2Tb6eErbp0Mk" width="690" height="213" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22c97534133730a6d1688161edb75147a2e8063c_2_690x213.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22c97534133730a6d1688161edb75147a2e8063c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22c97534133730a6d1688161edb75147a2e8063c.png 2x" data-dominant-color="3A3A3A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-12-04 at 12.59.06 PM</span><span class="informations">996×308 20.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve tried to install the extension manually but slicer says it is already installed, I’m hoping I’m just missing something really simple but I’m not sure. I’m on version 5.4 and on a 2020 M1 MacBook Air that’s on Ventura 13.4.1.</p>

---

## Post #9 by @chir.set (2023-12-04 19:53 UTC)

<aside class="quote no-group" data-username="lccmyers" data-post="8" data-topic="33153">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/848f3c/48.png" class="avatar"> lccmyers:</div>
<blockquote>
<p>but slicer says it is already installed,</p>
</blockquote>
</aside>
<p>Well the extra markups are clearly not loaded; the extension is available and operational with 5.4.</p>
<p>You may</p>
<ul>
<li>uninstall 5.4 and reinstall 5.4 and extensions,</li>
<li>uninstall 5.4 and install 5.6 or Preview, and extensions.</li>
</ul>
<p>Software do not work unexpectedly, they must perform similarly on your machine. Now yours is an outlier since it executes x86_64 code via an emulator on an ARM CPU. I don’t know how far this may affect Slicer, there have been multiple reports unexpected behaviour on this forum. Other people using the M1 and M2 processors may share their experience about the ExtraMarkups extension.</p>

---
