# Lost an ffmpeg utility in Screen Capture after an update

**Topic ID**: 28382
**Date**: 2023-03-14
**URL**: https://discourse.slicer.org/t/lost-an-ffmpeg-utility-in-screen-capture-after-an-update/28382

---

## Post #1 by @Beth_Bearce (2023-03-14 17:43 UTC)

<p>Hi all,</p>
<p>Up until recently, I was using the Screen Capture module &amp; ffmpeg to generate GIFs of my rotating scans with transparent backgrounds. (I use strange colored slides, and I like having my fish movies just float on the background.) I’ve updated Slicer recently, and now the same commands generate broken GIFs that don’t open, or, if I remove all the ffmpeg “extra options,” it will create GIFs that WILL open, but do not have transparent backgrounds, even though “transparent background” is checked in the advanced options. [I don’t think I needed to specify/encode a transparent background in “extra options” with ffmpeg annotation previously-- I believe I just had to check the “transparent background” button in 3D Slicer.]</p>
<p>I thought that I had probably disconnected the path to ffmpeg during a reinstall or something, but the path still looks fine. And I AM getting GIFs, it’s just the transparency function that no longer seems to work. Any suggestions would be helpful!</p>

---

## Post #2 by @hherhold (2023-03-14 17:51 UTC)

<p>I haven’t checked to see if the options that Slicer feeds to ffmpeg have changed in a while, but is it possible your version of ffmpeg got upgraded?</p>
<p>ffmpeg also takes like a GAZILLION options. It’s actually pretty useful to become familiar with them; I’ve learned quite a few tricks along the way by reading the manpage.</p>

---

## Post #3 by @Beth_Bearce (2023-03-14 18:15 UTC)

<p>I did manage to find a workaround by saving the image series with a transparent background (which does work fine!), and then GIF’ing them myself in an extra step through the terminal, which isn’t too bad. Thank you!</p>

---

## Post #4 by @hherhold (2023-03-14 18:17 UTC)

<p>Yep, I’ve wound up doing the exact same thing at times when I need to feed ffmpeg different options!</p>

---

## Post #5 by @pieper (2023-03-14 20:30 UTC)

<p>It would be great if you could report what’s different. between command line options you used yourself versus the ones Slicer used.  It would be good to know if there’s an ffmpeg versioning difference that needs to be taken into account or if it’s something else.</p>

---
