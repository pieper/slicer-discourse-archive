---
topic_id: 6231
title: "Bug Slicer Nightly Freezes On Macos Mojave At Start"
date: 2019-03-21
url: https://discourse.slicer.org/t/6231
---

# Bug: Slicer nightly freezes on MacOS Mojave at start

**Topic ID**: 6231
**Date**: 2019-03-21
**URL**: https://discourse.slicer.org/t/bug-slicer-nightly-freezes-on-macos-mojave-at-start/6231

---

## Post #1 by @Alex_Vergara (2019-03-21 11:10 UTC)

<p>Behaviour: Slicer freezes at start for about 1 minute (sometimes more), then it starts normally. The freeze is even before the splash screen. Once the splash screen is shown it starts normally.<br>
System: Slicer nightly 2019-03-17, MacOS Mojave Dark mode.</p>
<p>The stable version 4.10 runs perfectly, no freeze.</p>
<p>Edit: If I launch it from terminal the behaviour is not shown, only launching from the desktop icon. Really odd and annoying!</p>

---

## Post #2 by @jamesobutler (2019-03-21 12:10 UTC)

<p>I know that slicer takes significantly longer to load the first time after booting up of a computer. Then all subsequent launches are launched faster.</p>
<p>Is what you are describing different than this? I can’t think of an explanation where it is slow to launch from a desktop icon and then faster with the terminal. I would attempt a restart of your system and then do the inverse.</p>

---

## Post #3 by @Alex_Vergara (2019-03-21 12:31 UTC)

<p>Thanks for your reply.<br>
Indeed it is different, it is not about loading slower, I know modules take time to load. This is about a full freeze for around one minute even before loading anything. The odd part is that stable version does not have this behaviour, otherwise I would thought of a system problem.</p>

---

## Post #4 by @pieper (2019-03-21 14:30 UTC)

<p>It might be something with the extension manager checking for updates.  Maybe try disabling the extension manager (in the application preferences).  Another thing you might do is run Instruments (from Xcode) to see what the app is doing during the freeze.</p>

---
