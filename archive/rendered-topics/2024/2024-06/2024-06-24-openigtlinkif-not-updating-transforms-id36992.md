---
topic_id: 36992
title: "Openigtlinkif Not Updating Transforms"
date: 2024-06-24
url: https://discourse.slicer.org/t/36992
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
