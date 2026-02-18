# Using Send to DICOM Server with IP address, Port and AET

**Topic ID**: 24535
**Date**: 2022-07-27
**URL**: https://discourse.slicer.org/t/using-send-to-dicom-server-with-ip-address-port-and-aet/24535

---

## Post #1 by @Ian (2022-07-27 23:20 UTC)

<p>Hi all,</p>
<p>I am trying to send de-identified CT scans to an external server from 3D Slicer using the DIMSE protocol. I have the AE Title, Port and IP address of the destination; however, the Send to DICOM Server only allows me to write in the “destination address”. Is there some specific combination of AE Title, Port and IP Address that should be written into the “destination address” to successfully export this scan? Is there some other module I should be using?</p>
<p>Much appreciated,</p>
<p>Ian</p>

---

## Post #2 by @pieper (2022-07-27 23:51 UTC)

<p>I guess it’s a little hidden in the tooltip.  You can use hostname:port in the address.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea61fbc0e2ba5285644b111507cb98b6ebc303c3.png" alt="image" data-base62-sha1="xrrEHSGqKATGyuSYEbRdTvHoykj" width="388" height="265"></p>

---

## Post #3 by @Ian (2022-07-28 13:15 UTC)

<p>Thanks for your response.</p>
<p>My Send to DICOM server pop-up looks a little bit different.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f243398f0f2770cff32f6768dc26a80855a5cdf.png" alt="Screen Shot 2022-07-28 at 9.11.45 AM" data-base62-sha1="29WIReiE2phP8leJ95oN4LrYXan" width="558" height="252"></p>
<p>I downloaded a more recent version (5.0.03) then what I had (4.11.2021026) and the problem was fixed.</p>
<p>Thanks!</p>

---
