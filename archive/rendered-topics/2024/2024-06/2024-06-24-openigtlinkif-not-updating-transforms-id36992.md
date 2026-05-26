---
topic_id: 36992
title: "OpenIGTLinkIF not updating transforms"
date: 2024-06-24
url: https://discourse.slicer.org/t/36992
last_bumped: 2026-04-04T20:31:45.944Z
---

# OpenIGTLinkIF not updating transforms

**Topic ID**: 36992
**Date**: 2024-06-24
**URL**: https://discourse.slicer.org/t/openigtlinkif-not-updating-transforms/36992

---

## Post #1 by @mikebind (2024-06-24 21:30 UTC)

<p>I am trying to troubleshoot using an NDI trakSTAR electromagnetic 3D tracker using OpenIGTLinkIF.  I have gotten the same system working on other computers, but am running into an odd error where the tracked transforms are not being streamed/updated over the connection, which otherwise looks OK.</p>
<p>Plus Server Launcher reports a successful connection, and OpenIGTLinkIF connects and gets an initial transform for all tracked transforms (and other transforms provided in the configuration file.  But those transforms are never updated afterwards.   Also, I don’t think the initial transforms reported are actually affected by the locations of the tracked sensors, but I’m not sure.</p>
<p>On another laptop I set up last year with the same software, everything works fine and the tracked transforms are updated continuously, using the same configuration file, the same tracker hardware, etc.</p>
<p>The new computer, where it is not working, has a newer version of Slicer (5.6.1 vs 5.2.1), but is otherwise similar (both Windows 10 laptops), same version of Plus.  The messages in the log for Plus Server Launcher look identical. There are no messages in the Slicer error log.  If I use fCal on the new computer and record transforms, I get varying locations if I move the sensors.  I’m a bit at a loss for how to continue troubleshooting.</p>
<p>I just downloaded Slicer 5.2.1 onto the new computer and verified that I get the same behavior (no updating of transforms), so it is not the Slicer version difference. I tried configuring SendValidTransformsOnly to “false” instead of “true” with no effect.</p>
<p>Has anyone else run into a similar issue or have any ideas about how to troubleshoot this?</p>

---

## Post #2 by @HazemShereef (2026-04-04 17:37 UTC)

<p>i am facing a similar issue, did you manage to find a solution?<br>
The initial transform connection is successful, however the transform coordinates doesnt update afterwards, also doesnt seem to change depending on the initial coordinates of the tool to the camera</p>

---

## Post #3 by @mikebind (2026-04-04 19:06 UTC)

<p>The root cause seemed to be somewhere in the security stack of software running at my job.  I did not get a satisfying answer from out IT department, but everything works fine outside of the corporate network, and shows the behavior above inside the corporate network, so it’s some blockage of communication happening there.  I have had temporary success by changing the port number, but after some time, that new port number shows the same behavior (initial connection OK, no error message, but no ongoing communication).  My guess is that there is some sort of adaptive filter which is flagging some communication pattern as suspicious and shutting it down, but when I have raised this theory with IT folks, they didn’t seem aware of that as a possibility.  Still, since the identical code works on a different port number, and also works outside the corporate network, it seems like the issue has to be somewhere in the corporate security software.  It’s a little frustrating, because I’m running the OpenIGTLink server on the same local machine, so there isn’t actually any traffic going out to or in from the wider network, just local communication on the same machine, but I think the method of communication is one that gets intercepted and inspected by the security software and treated as if it were network communication. So, I don’t have a solution for you, but the problem may not be anywhere in your code or setup.</p>

---

## Post #4 by @HazemShereef (2026-04-04 19:29 UTC)

<p>thanks for the fast reply, actually after going in circles and debugging with the help of Claude, i found out what my issue was, it was an issue related to CRC (Cyclic Redundancy Check) is a <strong>error-detection algorithm</strong>. It takes a block of data and produces a short fixed-size number (the “checksum”) that acts as a fingerprint of that data. If even a single bit in the data changes, the checksum will be completely different.<br>
i was using a wrong (maybe old) polynomial in my application<br>
”CRC64_POLY = 0x95AC9329AC4BC9B5ULL;”<br>
when the right one is the <strong>ECMA-182 standard</strong> CRC64 polynomial.<br>
CRC64_POLY = 0x42F0E1EBA9EA3693ULL;</p>
<p>When Slicer received each TRANSFORM message, it parsed the header correctly (registering the node name and type), but when it ran CRC validation on the 48-byte body inside its <code>Unpack()</code> function, the checksum didn’t match. Slicer <strong>silently discarded every single message</strong> to protect the MRML scene from potentially corrupt data. No error was logged, no warning was shown — which is why it was so difficult to diagnose.</p>
<p>When the tracker sends a TRANSFORM message over TCP to Slicer:<br>
[58-byte header] [48-byte body (rotation + translation matrix)]<br>
↓<br>
CRC64 computed<br>
↓<br>
Checksum stored in header bytes 50-57</p>
<p>When Slicer receives it:<br>
Slicer receives the 48-byte body<br>
↓<br>
Slicer computes its own CRC64 of that body<br>
↓<br>
Compares its result against the checksum in the header<br>
↓<br>
Match → accepts and updates MRML node ✓<br>
No match → silently discards the message ✗</p>
<p>i don’t know if that can relate to your issue, but maybe it could help anyone facing the same symptoms.</p>

---

## Post #5 by @pieper (2026-04-04 19:36 UTC)

<p>Just FYI if you are having trouble using the networking you could try using shared memory instead.  With modern python versions it’s very easy to do and is cross platform.  It can also be handy to use RPyC to coordinate between client and server.  We’ve been using this pattern for some simulation experiments (SlicerTMS and SlicerSOFA) but it should also work well for trackers.</p>

---

## Post #6 by @mikebind (2026-04-04 20:28 UTC)

<p>Thanks for sharing your solution. Where do you set this CRC algorithm?  If it’s possible for this to drift out of sync somehow (or something innocently changes the header) it could possibly be related to the issues I am seeing.</p>

---

## Post #7 by @mikebind (2026-04-04 20:31 UTC)

<p>Thanks so much for mentioning this, <a class="mention" href="/u/pieper">@pieper</a> , I will look into it.  For our purposes, we never need to broadcast the messages over an actual network, the tracker hardware is always connected directly to the same laptop which is running the IGTLink server and Slicer, so an alternate means of communication which sidesteps possible firewall issues sounds great.</p>

---
