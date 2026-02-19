---
topic_id: 20587
title: "Openigtlink Fiducial Marker Transfer Seems To Max Out At 2 1"
date: 2021-11-11
url: https://discourse.slicer.org/t/20587
---

# OpenIGTLink Fiducial Marker Transfer seems to max out at 2^16 bytes

**Topic ID**: 20587
**Date**: 2021-11-11
**URL**: https://discourse.slicer.org/t/openigtlink-fiducial-marker-transfer-seems-to-max-out-at-2-16-bytes/20587

---

## Post #1 by @afhall (2021-11-11 19:46 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11<br>
Expected behavior: OpenIGTLink - Fiducial marker transfer of all points<br>
Actual behavior: OpenIGTLink seems to max out at 2^16 bytes regardless of number of fiducials to be transferred.</p>

---

## Post #2 by @lassoan (2021-11-11 19:56 UTC)

<p>Can you tell a bit about your use case? How many points do you want to transfer? How many times per second? What is the OpenIGTLink client and server (Slicer, Plus, pyigtl, …)?</p>

---

## Post #3 by @afhall (2021-11-11 20:07 UTC)

<p>Hi Andras, thanks very much for your inquiry.</p>
<p>We were wanting to transfer up to 500 fiducial makers, which put the total byte transfer over 65K.<br>
This is a one-time transfer, at the beginning of our procedure.</p>
<p>3D Slicer is the server, and the client is custom code on our Kuka LBR, which has worked well for smaller numbers of fiducials.<br>
We have a very larger data buffer on the robot side, but all the data after 65K is zeros…the data within the first 65K is correct.</p>
<p>But you make an excellent point that this could be a limitation on the Kuka side.<br>
We could probably hook up a laptop and make a quick simulation in Matlab to test.<br>
Do you think this would be a reasonable debug step?</p>
<p>Best regards,<br>
Andy</p>

---

## Post #4 by @lassoan (2021-11-11 20:21 UTC)

<p>I’ve tried and 600 points are transferred without problems via OpenIGTLink between two Slicer instances. This confirms that the problem is on the Kuka side.</p>
<p>You can also use <a href="https://github.com/lassoan/pyigtl">pyigtl</a> as an OpenIGTLink test client.</p>
<p>Note that fiducials are intended for cases when the user needs to identify each individual point (user can recognize each point by name or by spatial position). 500 fiducial markers are more likely describe a point cloud, which can be much more efficiently stored in a Model node in Slicer and transferred as POLYDATA message in OpenIGTLink.</p>

---

## Post #5 by @afhall (2021-11-11 20:26 UTC)

<p>Thanks Andras!<br>
We will verify from our side, for our own education.<br>
…and I suspected there was a more efficient transfer structure, but since we saw this “error” wanted to bring it up.<br>
We very much appreciate your help and guidance!!<br>
Best regards,<br>
Andy</p>

---

## Post #6 by @lassoan (2021-11-11 20:38 UTC)

<p>One more thing that you may find useful - this is an example to send 600 random fiducial point positions via pyigtl:</p>
<pre><code class="lang-python">import pyigtl
import numpy as np

client = pyigtl.OpenIGTLinkClient(host="127.0.0.1", port=18944)
point_message = pyigtl.PointMessage(device_name="points", positions=np.random.rand(600,3)*20)
client.send_message(point_message)
</code></pre>

---

## Post #7 by @lassoan (2021-11-12 06:20 UTC)

<p>It sounds like a very interesting project. It would be nice if you could post some images or videos if you got some features working.</p>

---

## Post #8 by @afhall (2021-11-15 19:21 UTC)

<p>Thanks again Andras, and once we get the thing working we’d be glad to post something.</p>

---
