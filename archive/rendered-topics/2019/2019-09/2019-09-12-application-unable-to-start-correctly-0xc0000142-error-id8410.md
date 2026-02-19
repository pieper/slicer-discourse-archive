---
topic_id: 8410
title: "Application Unable To Start Correctly 0Xc0000142 Error"
date: 2019-09-12
url: https://discourse.slicer.org/t/8410
---

# Application unable to start correctly (0xc0000142) error

**Topic ID**: 8410
**Date**: 2019-09-12
**URL**: https://discourse.slicer.org/t/application-unable-to-start-correctly-0xc0000142-error/8410

---

## Post #1 by @muratmaga (2019-09-12 21:27 UTC)

<p>I just downloaded and installed (into my user space) Slicer nightly. I ended up getting this error message. I already tried uninstall and reinstalled (to different locations) a bunch of times as generic help for this error code suggests on web.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7cfa2317812e6b3684d29e4cb8d2476c1e36880e.png" alt="slicer_start_error" data-base62-sha1="hPB7B5FoH3sieXxAQbwLXy8HrTE" width="395" height="152">.</p>

---

## Post #2 by @jamesobutler (2019-09-12 21:31 UTC)

<p>I can provide info that I downloaded today’s nightly for Windows and it started normally for me.</p>

---

## Post #3 by @lassoan (2019-09-12 21:36 UTC)

<p>Today’s Preview Release works well for me, too.</p>
<p>Have you installed any new software recently? Do previous Slicer releases work well?</p>
<p>See troubleshooting information here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Troubleshooting#Instruction_for_Windows" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Troubleshooting#Instruction_for_Windows</a></p>

---

## Post #4 by @muratmaga (2019-09-13 01:53 UTC)

<p>This was a windows 7 computer with a working Slicer that was recently migrated to Windows 10. It must be some sort of a corporate user policy change that probably broke the functionality. I managed to install other new programs (e.g., TurboVNC etc) that all seem to work.</p>
<p>It will be hard to chase, so I will just have them do a fresh reinstall of OS.</p>

---

## Post #5 by @evan (2019-09-20 15:09 UTC)

<p>I also experienced this error on the 4.11.0-2019-09-03 and 4.11.0-2019-09-17 slicer nightlies. Attempted the following with no avail:</p>
<ul>
<li>Two different Windows 10 machines (both 3rd generation Intel)</li>
<li>Installing to a custom directory</li>
<li>Installing to the default suggested directory</li>
<li>Opening as administrator</li>
<li>Opening with the ‘–disable-settings’ flag</li>
</ul>
<p>I was however able to install and run both nightly versions without error on a Linux machine (7th gen Intel).</p>
<p>Edit: After reading the <a href="https://discourse.slicer.org/t/cant-start-slicer-on-linux-on-one-machine/8175/26">post linked above</a>, I see now it is a CPU support issue.</p>

---
