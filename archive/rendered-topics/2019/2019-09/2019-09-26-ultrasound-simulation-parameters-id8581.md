---
topic_id: 8581
title: "Ultrasound Simulation Parameters"
date: 2019-09-26
url: https://discourse.slicer.org/t/8581
---

# Ultrasound Simulation Parameters

**Topic ID**: 8581
**Date**: 2019-09-26
**URL**: https://discourse.slicer.org/t/ultrasound-simulation-parameters/8581

---

## Post #1 by @hripat (2019-09-26 14:31 UTC)

<p>Hi,</p>
<p>Is there a way to change the Ultrasound simulation parameters? Do users have access to change these parameters on Slicer?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2019-10-02 02:26 UTC)

<p>Ultrasound simulation parameters are described in the PLUS XML configuration file. The easiest way is to edit the file using a text editor. You can change transforms (position of objects, transducer, etc.), imaging depth, etc. by sending transforms via OpenIGTLink. If needed, we could expose more simulation parameters via OpenIGTLink interface.</p>

---
