# Compile from source - QSocketNotifier errord

**Topic ID**: 28772
**Date**: 2023-04-06
**URL**: https://discourse.slicer.org/t/compile-from-source-qsocketnotifier-errord/28772

---

## Post #1 by @Peng_Wang (2023-04-06 01:32 UTC)

<p>Operating system: Ubuntu 23.04<br>
Slicer version: 5.3<br>
I am compiling Slicer from source on Ubuntu. It uses the Qt from system (v5.15.8).<br>
When I run Slicer from the Slicer-build/ it give the following error and quit after the splash screen,</p>
<p>QSocketNotifier: Can only be used with threads started with QThread</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2023-04-06 01:34 UTC)

<p>The message may not be related to the crash. Errors are usually due to OpenSSL and Qt, so they are the most likely culprits. Can you get a stack trace?</p>
<p>Does the official Slicer release work well?</p>

---
