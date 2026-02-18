# Ndi polaris failed to connect with plus

**Topic ID**: 2210
**Date**: 2018-02-28
**URL**: https://discourse.slicer.org/t/ndi-polaris-failed-to-connect-with-plus/2210

---

## Post #1 by @emetss (2018-02-28 17:44 UTC)

<p>Operating system: windows 10, or ubuntu 16.04<br>
Plus version:2.6 or 2.7</p>
<p>I have an ndi polaris camera. It has a com port and is connected with the pc through com-usb adapter. The pc recognize it. But still cannot connect with plus. I choose “ndi polaris tracker with passive markers” as configuration xml file. and I tried to type “Serial Port = the com port number i have” but still no connection. Do you have ideas especially for this kind of Polaris camera connection?</p>
<p>regards,</p>

---

## Post #2 by @ihnorton (2018-02-28 17:47 UTC)

<p>See Andras’ response – better to provide necessary information over there and keep discussion in one thread.<br>
<s>What brand of com-usb adapter? In my experience the only ones that worked correctly were FTDI chipset.</s></p>

---

## Post #3 by @lassoan (2018-02-28 19:38 UTC)

<p>Please report this at <a href="https://github.com/PlusToolkit/PlusLib/issues">https://github.com/PlusToolkit/PlusLib/issues</a></p>

---

## Post #4 by @emetss (2018-03-02 20:44 UTC)

<p>I’m using the prolific one. My OS is windows 10. I also tried in ubuntu 16.04. the com is recognized in my pc but cannot connect with plus. I can also connect with other programs (like MITK) but not with Plus. Do you think using the FTDI one will solve the issue?</p>

---

## Post #5 by @ihnorton (2018-03-02 20:45 UTC)

<p>If it works in MITK then it’s probably just a problem in the PLUS configuration. I suggest to open an issue at <a href="https://github.com/PlusToolkit/PlusLib/issues">https://github.com/PlusToolkit/PlusLib/issues</a> as Andras mentioned.</p>

---
