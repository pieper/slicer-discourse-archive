---
topic_id: 7056
title: "Track Images Using Polhemus Fastrak Electromagnetic Tracker"
date: 2019-06-06
url: https://discourse.slicer.org/t/7056
---

# Track images using Polhemus Fastrak electromagnetic tracker

**Topic ID**: 7056
**Date**: 2019-06-06
**URL**: https://discourse.slicer.org/t/track-images-using-polhemus-fastrak-electromagnetic-tracker/7056

---

## Post #1 by @Satvika (2019-06-06 12:45 UTC)

<p>Hi,</p>
<p>We are working on tracking images with Electromagnetic Tracker (Polhemus Fastrak) using PLUS/Slicer. We have position data from the emt and images from ultrasound system:<br>
Q How do we obtain real-time transform matrices from the tracker ?</p>
<p>I referred the link : <a href="https://www.slicer.org/w/images/e/ed/OpenIGTLinkTutorial_Slicer4.1.0_JunichiTokuda_Oct2012.pdf" rel="noopener nofollow ugc">https://www.slicer.org/w/images/e/ed/OpenIGTLinkTutorial_Slicer4.1.0_JunichiTokuda_Oct2012.pdf</a></p>
<p>But I would like to know how real time position/transform matrix can be obtained.</p>
<p>Thank you!</p>

---

## Post #2 by @muratmaga (2023-03-22 18:47 UTC)

<p><a class="mention" href="/u/satvika">@satvika</a>,</p>
<p>I am actually quite curious about that system. Can you get coordinates (e.g., as pointLists, or continuous curves) from that device directly into Slicer?</p>

---

## Post #3 by @Satvika (2023-03-28 06:22 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> -</p>
<p>Yes, you can add the device to slicer using SlicerIGT and get the coordinate values from the EMT in real-time. These tutorials might be helpful: <a href="https://www.slicerigt.org/wp/user-tutorial/" class="inline-onebox" rel="noopener nofollow ugc">User tutorial | SlicerIGT</a></p>

---

## Post #4 by @lassoan (2023-03-28 11:42 UTC)

<p>I don’t see Polhemus tracker interface in the source code - <a href="https://github.com/PlusToolkit/PlusLib/tree/master/src/PlusDataCollection" class="inline-onebox">PlusLib/src/PlusDataCollection at master · PlusToolkit/PlusLib · GitHub</a></p>
<p>How did you connect to the Polhemus tracker?<br>
Have you implemented the interface and has not contributed yet to the Plus toolkit?</p>

---

## Post #5 by @lopezchau (2023-09-04 23:21 UTC)

<p>Hello.  Sorry to revive this thread…totally new to this.  Did you manage to connect the Polhemus tracker to 3d Slicer?</p>

---

## Post #6 by @lassoan (2023-09-15 02:44 UTC)

<p>I’m not aware of an OpenIGTLink interface for Polhemus. Since cost of development, testing, optimization, maintenance, and support of a new interface would be higher than the cost of an already supported electromagnetic tracker (such as NDI Aurora or Ascension), probably most people end up buying an already supported tracker instead. Surgical navigation users may also end up choosing NDI instead of Polhemus, because NDI appears to be used in many more clinical products.</p>
<p>If somebody already has several Polhemus tracking systems or wants to use some unique characteristics of these systems then it would worth implementing an OpenIGTLink interface. Maybe a quick&amp;dirty bridge can be put together in Python, which converts Polhemus VRPN messages (received by some VRPN Python package) to OpenIGTLink messages (sent by <a href="https://github.com/lassoan/pyigtl">pyigtl</a>).</p>

---
