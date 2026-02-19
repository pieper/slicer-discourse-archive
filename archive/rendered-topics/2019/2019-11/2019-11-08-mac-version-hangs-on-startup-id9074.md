---
topic_id: 9074
title: "Mac Version Hangs On Startup"
date: 2019-11-08
url: https://discourse.slicer.org/t/9074
---

# Mac version hangs on startup

**Topic ID**: 9074
**Date**: 2019-11-08
**URL**: https://discourse.slicer.org/t/mac-version-hangs-on-startup/9074

---

## Post #1 by @hherhold (2019-11-08 00:30 UTC)

<p>I think I’ve seen this mentioned somewhere along the line but I’m very behind in keeping up with discourse posts, and a quick search didn’t uncover anything.</p>
<p>Slicer seems to hang on my mac when opening - and by hang, I mean the window manager freezes, similar to the topic a while back when the extension manager opening a dialog would completely hang the screen for a few seconds. It also seems to hang on opening Qt file dialogs - picking the output directory for a screen capture, for example, will hang the system for 5-10 seconds.</p>
<p>The discussion a while back mentioned the particular version of Qt being used for mac builds.</p>
<p>Does this sound familiar to anyone?</p>
<p>Thanks in advance!!!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2019-11-08 00:40 UTC)

<p>Yes, this is the issue described in <a href="https://discourse.slicer.org/t/extension-wizard-file-open-dialogs-hang-ui-for-several-seconds/7881/9" class="inline-onebox">Extension Wizard - file open dialogs hang UI for several seconds</a>. It seems that accessibility features (that helps people with disabilities to use the OS) in MacOSX have changed in a non-backward compatible way: software that is built targeting older OS versions sometimes hangs for tens of seconds when used with new OS versions.</p>
<p>One possible solution would be to upgrade Qt to the latest version (hoping that Qt may be able to abstract away the OS API changes). If that does not work then we may need to increase the minimum required MacOSX version (which would prevent running Slicer on older OS versions but would make it run well on latest OS version).</p>
<p>Let’s continue the discussion <a href="https://discourse.slicer.org/t/extension-wizard-file-open-dialogs-hang-ui-for-several-seconds/7881/9">here</a>.</p>

---

## Post #3 by @hherhold (2019-11-08 00:41 UTC)

<p>Ok, sorry for starting a new thread - is there a way to delete this one?</p>

---

## Post #4 by @lassoan (2019-11-08 02:04 UTC)

<p>No problem, maybe someone else will find this thread based on the topic title and will be redirected to the other thread.</p>

---
