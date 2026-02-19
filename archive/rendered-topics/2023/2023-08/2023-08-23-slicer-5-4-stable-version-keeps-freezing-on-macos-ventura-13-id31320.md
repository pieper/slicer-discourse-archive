---
topic_id: 31320
title: "Slicer 5 4 Stable Version Keeps Freezing On Macos Ventura 13"
date: 2023-08-23
url: https://discourse.slicer.org/t/31320
---

# Slicer 5.4 stable version keeps freezing on macOS Ventura 13.4.1 with M2 processor

**Topic ID**: 31320
**Date**: 2023-08-23
**URL**: https://discourse.slicer.org/t/slicer-5-4-stable-version-keeps-freezing-on-macos-ventura-13-4-1-with-m2-processor/31320

---

## Post #1 by @mohammed_alshakhas (2023-08-23 18:53 UTC)

<p>5.4 stable version keeps freezing every single time I use it</p>

---

## Post #2 by @pieper (2023-08-23 19:24 UTC)

<p>Thanks for testing and reporting.  Is this different behavior than you saw from other versions?  What operations lead to freezing?  What platform are you using?</p>
<p>Do other people see this issue?  I haven’t seen anything in initial testing on mac.</p>

---

## Post #3 by @mohammed_alshakhas (2023-08-23 19:31 UTC)

<p>nothing other than the freezing.  I’m using mac os Ventura 13.4.1 . m2 processor.<br>
it freezes  on different operations sometimes segmenting sometimes rendering or even returning to use the software after a short pause</p>

---

## Post #4 by @jcfr (2023-08-24 05:30 UTC)

<p>Possibly related to these:</p>
<ul>
<li><a href="https://discourse.slicer.org/t/slicer-program-crash-suddenly-in-macbook/26453" class="inline-onebox">Slicer program crash suddenly in MacBook</a></li>
<li><a href="https://discourse.slicer.org/t/gpu-and-cpu-rendering-on-macbookpro-m2-promax/29152/5" class="inline-onebox">GPU and CPU rendering on MacBookPro M2 ProMax - #5 by muratmaga</a></li>
</ul>
<hr>
<p>Note that natively building Slicer on arm64 macOS is definitely something we would like to address.<br>
See <a href="https://github.com/Slicer/Slicer/issues/6811" class="inline-onebox">Support for building/testing/packaging Slicer on Apple arm64 · Issue #6811 · Slicer/Slicer · GitHub</a></p>

---

## Post #5 by @lassoan (2023-08-24 07:17 UTC)

<p>Based on user reports that I’ve found related to freezes and stutters on arm64 systems, it seems that the Rosetta emulator that macOS uses for running x64 executables has quite a lot of robustness issues on various hardware and operating system versions. Updgrading your operating system to the most recent version might solve the problems that you are experiencing.</p>
<p>A native arm64 Slicer version that does not depend on Rosetta emulation should perform more consisently. A <a class="mention" href="/u/jcfr">@jcfr</a> wrote above, it is in the works.</p>

---

## Post #6 by @mohammed_alshakhas (2023-08-24 09:34 UTC)

<p>new issues I noticed</p>
<p>segments appearing in slice view not showing in  3d or vice versa.<br>
this couldn’t be resolved by toggling visibility</p>
<p>in rendering,  changing the color histogram upon reopening file. there is this pattern where I get back the upper spectrum added.  See the attached. you can notice the dark color. I need to delete 5 or 6 points of black color to get the colors back to the original rendering I made</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d76ea7a57fdccd13821e6b28e1d7ceb3ce41a4b.jpeg" data-download-href="/uploads/short-url/8LJTUUfj2uQOwjXEh7oTp397upd.jpeg?dl=1" title="Screenshot 2023-08-24 at 09.37.49" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d76ea7a57fdccd13821e6b28e1d7ceb3ce41a4b_2_690x448.jpeg" alt="Screenshot 2023-08-24 at 09.37.49" data-base62-sha1="8LJTUUfj2uQOwjXEh7oTp397upd" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d76ea7a57fdccd13821e6b28e1d7ceb3ce41a4b_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d76ea7a57fdccd13821e6b28e1d7ceb3ce41a4b_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d76ea7a57fdccd13821e6b28e1d7ceb3ce41a4b_2_1380x896.jpeg 2x" data-dominant-color="8B8B8C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-08-24 at 09.37.49</span><span class="informations">1920×1247 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @pieper (2023-08-24 13:00 UTC)

<p>Do you have access to another machine for testing?  I would be good to see which issues are related to the M2 environment and which may be cross-platform.</p>

---

## Post #8 by @mohammed_alshakhas (2023-08-24 13:50 UTC)

<p>unfortunately i don’t</p>

---
