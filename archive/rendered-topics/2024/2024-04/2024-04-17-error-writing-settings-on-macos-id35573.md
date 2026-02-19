---
topic_id: 35573
title: "Error Writing Settings On Macos"
date: 2024-04-17
url: https://discourse.slicer.org/t/35573
---

# Error writing settings on MacOS

**Topic ID**: 35573
**Date**: 2024-04-17
**URL**: https://discourse.slicer.org/t/error-writing-settings-on-macos/35573

---

## Post #1 by @lskog (2024-04-17 23:50 UTC)

<p>My slicer cannot save any settings I try to change, even its basic ones. I tried to give it the whole disk permissions, but still nothing. All I can see in console is:<br>
[Qt] Error <span class="hashtag-raw">#1</span> while writing setting “ApplicationUpdate/AutoUpdateCheck”<br>
[Qt] Error <span class="hashtag-raw">#1</span> while writing setting “ApplicationUpdate/ServerUrl”<br>
[Qt] Error <span class="hashtag-raw">#1</span> while writing setting “DefaultScenePath”</p>
<p>and such things like for 50 settings.<br>
I’d appreciate any help, hope someone already faced this porblem. Thanks.</p>

---

## Post #2 by @pieper (2024-04-18 15:52 UTC)

<p>Doesn’t happen for me on macs I use.  Be sure you’ve installed the app (not running from the disk image) and that your home directory isn’t full or otherwise unavailable.</p>

---

## Post #3 by @lskog (2024-04-18 19:47 UTC)

<p>Thank you for yourreply. Even tried to install with homebrew. Any possibilities to intall not in applications folder but, for example ~/user/slicer/?</p>

---

## Post #4 by @pieper (2024-04-18 20:06 UTC)

<p>Yes, you can install the applications anywhere you want.</p>
<p>For me the settings are in ~/.config/slicer.org/Slicer.ini so you might check if that exists or is somehow locked.  Perhaps it got set to read-only and or you need to delete a corrupted one.</p>

---

## Post #5 by @lskog (2024-04-18 21:01 UTC)

<p>It worked! Just needed to find .config and change writing permissions. I’m kinda new to mac (less than a month) so it was a bit complicated. Thank you!</p>

---
