# Blank screen on Ubuntu 24.10

**Topic ID**: 39813
**Date**: 2024-10-23
**URL**: https://discourse.slicer.org/t/blank-screen-on-ubuntu-24-10/39813

---

## Post #1 by @Zander_Giuffrida (2024-10-23 05:47 UTC)

<p>I’m running a fresh install of Ubuntu 24.10</p>
<p>I just installed the stable version of Slicer following the instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#linux" rel="noopener nofollow ugc">here</a>.</p>
<p>Specifically I downloaded version 5.6.2 and installed the dependencies using the command listed in the documentation: “sudo apt-get install libglu1-mesa libpulse-mainloop-glib0 libnss3 libasound2t64 qt5dxcb-plugin”</p>
<p>When I run the executable for slicer I get the pop up screen but when it goes away there is nothing on the screen. And when I try to quit the app from the sidebar it is unresponsive.</p>
<p>Any idea what could be causing this issue?</p>

---

## Post #2 by @pieper (2024-10-23 11:52 UTC)

<p>I don’t think people have had much experience with 24.10 yet, so different dependencies might be needed.  A few ideas could be to build from source, use a debugger, or commands like <code>ldd</code> and <code>strace</code> to home in on where the application is exiting.</p>

---
