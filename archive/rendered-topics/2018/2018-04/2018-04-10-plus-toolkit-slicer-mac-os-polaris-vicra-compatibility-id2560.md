---
topic_id: 2560
title: "Plus Toolkit Slicer Mac Os Polaris Vicra Compatibility"
date: 2018-04-10
url: https://discourse.slicer.org/t/2560
---

# Plus Toolkit + Slicer + Mac OS + Polaris Vicra compatibility

**Topic ID**: 2560
**Date**: 2018-04-10
**URL**: https://discourse.slicer.org/t/plus-toolkit-slicer-mac-os-polaris-vicra-compatibility/2560

---

## Post #1 by @banderies (2018-04-10 18:15 UTC)

<p>My lab will be getting a Polaris Vicra shortly, and I am getting ready to set it up with Slicer. We are also getting iMac Pros, and I would like to use one of them with the Vicra and Slicer. However, I am not certain of the compatibility of the Polaris drivers or plus toolkit with Mac. Does anyone know if the combination in my title is compatible?</p>
<p>Thanks!</p>

---

## Post #2 by @ihnorton (2018-04-11 20:37 UTC)

<p>I think PLUS on Mac is compatible-in-principle with Vicra  – Vicra has a built-in USB-serial converter, and IIRC the chip they use is Mac compatible. That said, I haven’t run it myself, and I would expect the configuration is much less tested than Windows… cc <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Note though that I believe all of the NDI tools are Windows-only, so if you need Architect to create custom tool ROM files then you will need a Windows box.</p>

---

## Post #3 by @lassoan (2018-04-12 19:25 UTC)

<p>I think there are people who use PLUS on Mac to connect to Polaris Vicra. You need to build PLUS yourself, as we don’t provide binary packages for Mac. If you need any help, post it as an issue on <a href="https://github.com/PlusToolkit/PlusLib/issues">PLUS project page</a>.</p>
<p>You can also run Plus on Windows or Linux and send tracking data to a Slicer instance running on Mac.</p>

---
