# Build for mac from windows

**Topic ID**: 19667
**Date**: 2021-09-14
**URL**: https://discourse.slicer.org/t/build-for-mac-from-windows/19667

---

## Post #1 by @sheerinaseem (2021-09-14 13:50 UTC)

<p>Our team of developers are working on building a teaching and education tool using slicer. The development is currently being done on a Windows setup. I however have a mac. Is there a way the build can be genrated for a macbook system on windows development environment itself?</p>
<p>Please help!<br>
Thanks</p>

---

## Post #2 by @lassoan (2021-09-15 01:23 UTC)

<p>I don’t think you can cross-compile Qt desktop applications on PC for macOS, but you have several other options:</p>
<ul>
<li>You might be able to run macOS on a virtual machine on Windows. I haven’t tried this ever, so I’m not sure how much it is officially supported by apple and how robust it is, but you can give it a try, you might be able to set up everything for free.</li>
<li>Your safest option is to buy a cheap macbook or mac mini. A used one is fine, but preferably not older than about 3 years. The nice thing is that you can do realistic testing, troubleshooting if you ever need that, and it may be faster than the virtual options.</li>
<li>You could also rent a macOS computer on the cloud. Since building, and especially packaging can take really long time (many hours), the cost could relatively quickly reach the price of a used mac. It may be a good option if you don’t need to build often, or if you want to share one virtual computer between many developers.</li>
</ul>

---

## Post #3 by @sheerinaseem (2021-09-16 14:59 UTC)

<p>Thanks alot for this. It looks like getting a cheap windows system will be a slightly feasable option.</p>

---
