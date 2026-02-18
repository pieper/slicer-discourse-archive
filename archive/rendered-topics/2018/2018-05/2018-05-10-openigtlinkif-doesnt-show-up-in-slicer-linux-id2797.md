# OpenIGTLinkIF doesn't show up in slicer linux

**Topic ID**: 2797
**Date**: 2018-05-10
**URL**: https://discourse.slicer.org/t/openigtlinkif-doesnt-show-up-in-slicer-linux/2797

---

## Post #1 by @samira (2018-05-10 21:22 UTC)

<p>Hi,</p>
<p>I just built Slicer in linux, but for some reason the OpenIGTLinkIF doesn’t get built automatically and I don’t see an option for it in the Cmake, the way it is in windows Slicer or maybe the older version of Slicer.<br>
Do I need to do something to have it in the slicer?</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2018-05-10 22:45 UTC)

<p>From Slicer 4.9, OpenIGTLinkIF is no longer bundled with Slicer core (to allow more frequent updates and using of external video codecs for compressed video transmission). You can find the repository here: <a href="https://github.com/openigtlink/SlicerOpenIGTLink">https://github.com/openigtlink/SlicerOpenIGTLink</a></p>

---

## Post #3 by @samira (2018-05-10 23:02 UTC)

<p>Thanks Andras,</p>
<p>Slicer documentation can be much better than what it is now <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Samira</p>

---

## Post #4 by @jcfr (2018-05-11 12:31 UTC)

<aside class="quote no-group" data-username="samira" data-post="3" data-topic="2797">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/34f0e0/48.png" class="avatar"> samira:</div>
<blockquote>
<p>Slicer documentation can be much better than what it is now</p>
</blockquote>
</aside>
<p>Thanks for the feedback <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20">  Whenever possible, we are always looking into improving it</p>
<p>Where would you have expected to find such information ?</p>

---

## Post #5 by @samira (2018-06-13 21:48 UTC)

<p>Sorry I haven’t seen this.<br>
I am working with Slicer since six years ago.<br>
I started working again on a project with slicer linux this time after a pause. I am a software person and I know how to follow instructions, but building slicer based on the build instruction is not easy.<br>
For example after lots of struggles I found out that I need to build Slicer with QT5 not QT4. It is still QT4 in the main instruction, however you can find one line in the instruction that as of 2018 you need to use QT5.<br>
No where you can find the information Andras gave me here.<br>
And I couldn’t find any information about how to add openIGTLink to the slicer when you build it separately. I really appreciate it if you guide me how <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
Hope this comments make a little bit of improvement in slicer documentation.</p>
<p>Thanks a lot,<br>
Samira</p>

---

## Post #6 by @lassoan (2018-06-13 22:00 UTC)

<p>Thanks for the feedback. You are right, nightly build instructions have not been updated (describes how to build last stable version instead of the nightly). I’ve added an <a href="https://issues.slicer.org/view.php?id=4571">issue</a> to make sure we update build instructions before Slicer-4.10.</p>

---

## Post #7 by @samira (2018-06-13 22:35 UTC)

<p>Thank you Andras, you are always super helpful <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
