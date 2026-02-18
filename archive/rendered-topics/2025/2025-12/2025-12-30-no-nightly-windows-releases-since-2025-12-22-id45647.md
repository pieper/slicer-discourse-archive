# No nightly Windows releases since 2025-12-22

**Topic ID**: 45647
**Date**: 2025-12-30
**URL**: https://discourse.slicer.org/t/no-nightly-windows-releases-since-2025-12-22/45647

---

## Post #1 by @lassoan (2025-12-30 21:09 UTC)

<p>Could someone at Kitware have a look at the Windows build machine? There have been no Windows builds for about a week now. Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b95c6ed3b8726cc993cc17d86ca1ecde1d9f7a3.png" data-download-href="/uploads/short-url/3W1MPppAP98OIk7UXjT2Doq851N.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b95c6ed3b8726cc993cc17d86ca1ecde1d9f7a3_2_690x242.png" alt="image" data-base62-sha1="3W1MPppAP98OIk7UXjT2Doq851N" width="690" height="242" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b95c6ed3b8726cc993cc17d86ca1ecde1d9f7a3_2_690x242.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b95c6ed3b8726cc993cc17d86ca1ecde1d9f7a3_2_1035x363.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b95c6ed3b8726cc993cc17d86ca1ecde1d9f7a3_2_1380x484.png 2x" data-dominant-color="C0C4CC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2337×822 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/ebrahim">@ebrahim</a></p>

---

## Post #2 by @ebrahim (2026-01-02 17:43 UTC)

<p>I just logged in and took a look at the Task Scheduler in bluestreak. I see the nightly build task wasn’t kicked off from 12/22 until today, with the message “Launch condition not met, user not logged-on”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d7e3e6bac0b0f116e1d400e00359c5163a8456f.jpeg" data-download-href="/uploads/short-url/kbHNzftC9osimZ2p2zCt0WKlmvt.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d7e3e6bac0b0f116e1d400e00359c5163a8456f_2_690x179.jpeg" alt="image" data-base62-sha1="kbHNzftC9osimZ2p2zCt0WKlmvt" width="690" height="179" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d7e3e6bac0b0f116e1d400e00359c5163a8456f_2_690x179.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d7e3e6bac0b0f116e1d400e00359c5163a8456f_2_1035x268.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d7e3e6bac0b0f116e1d400e00359c5163a8456f.jpeg 2x" data-dominant-color="DDE3E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1263×329 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Looking further into it (but please let me know if anyone immediately knows what caused this, e.g. if it has happened before)</p>

---

## Post #3 by @lassoan (2026-01-02 18:21 UTC)

<p>Most likely thebuaer eas logged out due to an automatic update. On Cdash you can mark certain builds as “expected” and you can set up email notification for yourself about errors, such as a missing expected build. This could help in detecting and resolving such cases in the future faster.</p>

---

## Post #4 by @ebrahim (2026-01-02 18:23 UTC)

<p>Yeah I am guessing the machine rebooted on Dec 22 for some reason and needed to be logged into, but no one was there to do it at that time. I have done it now so I hope the issue is fixed now.</p>
<p>But I will also try to get the task scheduler settings changed to not require a user to be logged in to avoid this manual step if the machine gets rebooted</p>
<blockquote>
<p>On Cdash you can mark certain builds as “expected” and you can set up email notification for yourself about errors, such as a missing expected build. This could help in detecting and resolving such cases in the future faster.</p>
</blockquote>
<p>That is useful, thanks I will look into it!</p>

---

## Post #5 by @lassoan (2026-01-02 18:29 UTC)

<p>You need a display for tests and it is also easier to detect and fix any errors if you can log on to the interactive session and see for example that a popup is displayed and that’s blocking the workflow.</p>
<p>You could set up auto-login, so that the machine automatically logs in a user after reboot. If the user has limited privileges (e.g., it could be a local user on that computer) then probably there are no security concerns.</p>

---

## Post #6 by @ebrahim (2026-01-19 16:39 UTC)

<p>Just an update on the nightly windows releases: I know it has been spotty with some days being skipped. I was experimenting with allowing the tasks to run without login, and it resulted in a failure of the nightly task for the last few days because it requires a security policy change that I must wait for our IT to make. They should make that change soon and then I will get to see if this configuration works.</p>
<p>So just a day or two and if it fails again after the change I will revert to the previous working configuration. If it succeeds, then it would be great because we would no longer need to manually log in every time the system reboots.</p>

---
