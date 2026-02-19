---
topic_id: 22394
title: "Slicer Program Closes After Logging Out And Back In On Windo"
date: 2022-03-09
url: https://discourse.slicer.org/t/22394
---

# Slicer program closes after logging out and back in on Windows 10

**Topic ID**: 22394
**Date**: 2022-03-09
**URL**: https://discourse.slicer.org/t/slicer-program-closes-after-logging-out-and-back-in-on-windows-10/22394

---

## Post #1 by @mbutle28 (2022-03-09 06:07 UTC)

<p>Hello!</p>
<p>I’ve noticed a recurring problem I have with my installation of Slicer 4.112021226. The problem is this:<br>
when I have the program open, then log out (with program still open) of my profile on the machine, then log back in, the program window closes spontaneously after a few seconds. What happens is the red X button in the top right corner looks like it has been pressed (it hasn’t), then the main header bar reads (Not Responding), then crash.</p>
<p>The OS I’m using is Windows 10 Pro. I wondered if it might be a graphics issue, but there are no problems like this when I’m actively running the program, even for heavy tasks. Uninstalling and re-installing the same version (latest stable one – 4.112021226) doesn’t solve the problem.</p>
<p>Any advice/help/insight is so appreciated, thank you!!</p>

---

## Post #2 by @lassoan (2022-03-09 06:19 UTC)

<p>When you log out (more accurately “Sign out”) from Windows10 then all the applications will be closed, so Slicer (and none of the other applications) will resume when you sign in again. What do you mean exactly by “log out”: sign out, lock the computer (hit Windows+L), put the computer into sleep, hibernate the computer, switch users, …?</p>
<p>I could not reproduce a Slicer crash on my computer with any of the above “log out” operations but if you have multiple monitors, older computer, not very robust drivers, etc. then locking your computer or putting into sleep might provoke an application error.</p>

---

## Post #3 by @mbutle28 (2022-03-09 11:24 UTC)

<p>To be honest, I’m not 100% sure what occurs on this “log out” that I describe, because this problem happens (as far as I know) only when I’m accessing the PC with Slicer on it remotely via Windows Remote Desktop. Specifically, what happens (sometimes) is that my remote connection is disrupted, so I have to “log in” again to the PC (i.e. reestablish the remote connection), and that’s when I encounter this problem. That said, I think by “log out” I mean a simple lock operation, since when this happens <strong>none of the other programs closes or is disrupted in any way</strong>.</p>
<p>Perhaps what you mention about the multiple monitors issue could be at work here? Or maybe it’s a driver issue?</p>
<p>Thanks for trying to reproduce the errors! Sorry I wasn’t clearer before.</p>
<p>Maybe what I’ll have to do is run Slicer locally rather than remotely…</p>

---

## Post #4 by @lassoan (2022-03-09 16:59 UTC)

<p>Thanks for the information, it is very useful. Remote desktop connection is an entirely different story than working locally. Slicer relies on hardware-accelerated graphics and Windows Remote Desktop Protocol earlier did not support this at all. Recent years Windows versions allow remotely started applications to access graphics hardware, but apparently it is not robust.</p>
<p>Updating tour graphics drivers might solve the issue (or the issue may get fixed by future Windows or graphics driver updates).</p>
<p>If updates don’t help then I would recommend to use a different remote desktop client, such as RealVNC, AnyDesk, Chrome Remote Desktop, NoMachine, or TightVNC. They all work at a bit higher level than Windows RDP (grab the rendered screen content) therefore they are much more robust.</p>
<p>If you must use Windows RDP then you can <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start">switch to a software renderer</a>. This<br>
will make the application not use hardware acceleration anymore, so it should be less sensitive to graphics driver bugs, but it makes rendering slower.</p>

---

## Post #5 by @mbutle28 (2022-03-09 19:18 UTC)

<p>This is extraordinarily helpful! Thanks so much for this detailed explanation and feedback. These sorts of software details are things I don’t think about reflexively because I don’t have so much expertise there.</p>
<p>I (quite naively, I guess!) didn’t even know there were other options for the remote desktop. I’ll be sure to try out one/some and report back!</p>
<p>Thanks again!</p>

---

## Post #6 by @mbutle28 (2022-03-11 16:46 UTC)

<p>I just tried setting up a connection using NoMachine, and it appears to solve the problem! I didn’t really stress test it too much yet, but it looks promising.</p>
<p>Either way, I will have discovered a new, more robust remote desktop software that I like a lot better than Windows Remote Desktop!</p>
<p>Thanks so much again!!</p>

---
