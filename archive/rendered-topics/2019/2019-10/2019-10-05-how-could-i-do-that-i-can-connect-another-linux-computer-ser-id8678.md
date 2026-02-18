# How could I do that I can connect another linux computer(server) via OpenIGTLink?

**Topic ID**: 8678
**Date**: 2019-10-05
**URL**: https://discourse.slicer.org/t/how-could-i-do-that-i-can-connect-another-linux-computer-server-via-openigtlink/8678

---

## Post #1 by @Zhao_Su (2019-10-05 05:07 UTC)

<p>I want to  connect a robot arm using Slicer. I had already set up the ROS enviroment and installed ROS-IGT_bridge and everything I need. But when I use OpenIGTLinkIF module , and check the Active, the status is always “wait”. Am I right text the contents like this?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/371cce0f682cb51c814bfc234c96aa9a6abe6a44.png" alt="image" data-base62-sha1="7RxYsqnUDbceAbbl47VQi2DabvS" width="545" height="241"></p>

---

## Post #2 by @lassoan (2019-10-07 18:09 UTC)

<p>Hostname shown on the screenshot is invalid.</p>
<p>Make sure one of ROS-IGTL-bridge and Slicer is set up as server and the other as client.</p>
<p>Try to disable firewall temporarily to make sure it is not preventing network connections.</p>

---
