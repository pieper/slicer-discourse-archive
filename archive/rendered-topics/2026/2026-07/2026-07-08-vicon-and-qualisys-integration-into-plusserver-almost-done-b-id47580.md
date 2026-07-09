---
topic_id: 47580
title: "VICON and QUALISYS integration into PlusServer - almost done but remaining jitter issues"
date: 2026-07-08
url: https://discourse.slicer.org/t/47580
last_bumped: 2026-07-08T15:52:59.253Z
---

# VICON and QUALISYS integration into PlusServer - almost done but remaining jitter issues

**Topic ID**: 47580
**Date**: 2026-07-08
**URL**: https://discourse.slicer.org/t/vicon-and-qualisys-integration-into-plusserver-almost-done-but-remaining-jitter-issues/47580

---

## Post #1 by @AurelieS (2026-07-08 15:52 UTC)

<p>Hi everyone,</p>
<p>We have been working on integrating <strong>Vicon Nexus</strong> into our 3D ultrasound acquisition workflow based on <strong>PlusServer</strong>. The goal is to obtain a Vicon integration behaving as closely as possible to the native devices (Optitrack, NDI, etc.) already available in Plus, which gives perfect 3D reconstructions.</p>
<p>We have implemented a working solution based on the <strong>Vicon DataStream SDK</strong>. Instead of developing a new Plus device directly, we chose the following architecture:</p>
<pre><code class="lang-auto">Vicon Nexus (DataStream SDK)
        ↓
Python bridge (echoCap library)
        ↓
OpenIGTLink Transform messages on port 18946
        ↓
PlusServer 
        ↓
VirtualMixer with ultrasound images sent on port 18944
        ↓
Tracked ultrasound images
</code></pre>
<p>The Python bridge runs asynchronously:</p>
<ul>
<li>a dedicated thread continuously waits for new Vicon frames (<code>GetFrame()</code> in <code>EServerPush</code> mode),</li>
<li>each frame is converted into a 4×4 transform,</li>
<li>transforms are streamed to PlusServer through OpenIGTLink.</li>
</ul>
<p>We have progressively improved the implementation:</p>
<ul>
<li>switched from synchronous polling to asynchronous acquisition,</li>
<li>removed unnecessary processing from the acquisition loop,</li>
<li>experimented with different timestamp strategies (system timestamps, Vicon frame-based timestamps, no explicit timestamps),</li>
<li>investigated possible OpenIGTLink buffering effects,</li>
<li>verified that the Vicon tracking itself is stable (very low calibration residuals).</li>
</ul>
<p>The situation is now the following:</p>
<ul>
<li><strong>Probe spatial calibration works very well</strong> (RMS &lt; 3 mm using fiducials in 3D Slicer).</li>
<li><strong>Temporal calibration (fCal) usually converges to a stable offset (~150-200ms)</strong>, although it occasionally returns incorrect values.</li>
<li>However, <strong>3D ultrasound reconstruction still exhibits noticeable jitter/waviness</strong> during scanning.</li>
<li>Sometimes the alignment is almost perfect, then progressively drifts before becoming correct again, suggesting that the image/transform synchronization is not always consistent.</li>
</ul>
<p>An important observation is that:</p>
<ul>
<li>the ultrasound images are acquired at <strong>60 Hz</strong>,</li>
<li>Vicon streams at <strong>100 Hz</strong>,</li>
<li>in 3D Slicer, despite a target acquisition frequency of 30Hz, output is around <strong>22 Hz (similar to what we have using Optitrack and NDI, which give perfect 3D reconstructions, so not a direct issue)</strong>.</li>
</ul>
<p>With exactly the same ultrasound setup and reconstruction pipeline, using the native <strong>OptiTrack</strong> device in PlusServer produces excellent reconstructions without visible jitter.</p>
<p>This makes us think that there is still an architectural difference between our bridge and the native Plus implementation (buffering, timestamp handling, interpolation, transform repository, or another internal mechanism).</p>
<p>Our implementation is available on GitHub (in private for now), and we would be very happy to collaborate with anyone familiar with the Plus tracking pipeline.</p>
<p>Would someone from the PlusServer development team be interested in helping us review this implementation and identify what is still missing to obtain behavior comparable to the native OptiTrack device?</p>
<p>Any advice on how Plus internally handles transform timestamps, buffering, interpolation, or synchronization with the VirtualMixer would also be greatly appreciated.</p>
<p>Thank you very much for your time!</p>
<p>Best regards,</p>
<p>Aurélie Sarcher &amp; Fabien Leboeuf</p>

---
