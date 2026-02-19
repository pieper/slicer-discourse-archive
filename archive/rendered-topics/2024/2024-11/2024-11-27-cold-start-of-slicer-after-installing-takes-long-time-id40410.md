---
topic_id: 40410
title: "Cold Start Of Slicer After Installing Takes Long Time"
date: 2024-11-27
url: https://discourse.slicer.org/t/40410
---

# Cold start of Slicer after installing takes long time

**Topic ID**: 40410
**Date**: 2024-11-27
**URL**: https://discourse.slicer.org/t/cold-start-of-slicer-after-installing-takes-long-time/40410

---

## Post #1 by @muratmaga (2024-11-27 16:43 UTC)

<p>I have been testing the preview builds lately on my Mac. After unpacking the slicer DMG file on the desktop, the first time launch of slicer almost take a minute.  There are no extension or anything. Is this normal?</p>
<p>There is this message in the log file, which am I not sure what it means:</p>
<p><code>2024-11-27 08:42:16.474 Slicer[19293:7600256] WARNING: Secure coding is not enabled for restorable state! Enable secure coding by implementing NSApplicationDelegate.applicationSupportsSecureRestorableState: and returning YES.</code></p>

---

## Post #2 by @pieper (2024-11-27 16:58 UTC)

<p>I haven’t looked into the details, but yes, when you have a new version or even a new build of a developer version on mac it takes quite a while.  I think it’s doing some kind of inspection of each shared library and then caches the result for faster startup the next time.</p>

---
