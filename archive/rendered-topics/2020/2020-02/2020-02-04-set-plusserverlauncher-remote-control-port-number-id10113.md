---
topic_id: 10113
title: "Set Plusserverlauncher Remote Control Port Number"
date: 2020-02-04
url: https://discourse.slicer.org/t/10113
---

# Set PlusServerLauncher remote control port number

**Topic ID**: 10113
**Date**: 2020-02-04
**URL**: https://discourse.slicer.org/t/set-plusserverlauncher-remote-control-port-number/10113

---

## Post #1 by @brynpitt (2020-02-04 21:22 UTC)

<p>OS: Windows 10<br>
PLUS Version: PlusApp-2.8.0.20191105-Telemed-Win32</p>
<p><strong>Expected behavior</strong>: Running command</p>
<blockquote>
<p>PlusServerLauncher --port=18905</p>
</blockquote>
<p>should start plus server launcher with remote control server at port number 18905</p>
<p><strong>Actual behavior</strong>: Remote control server port at default value (18904) regardless of --port option</p>
<p>Hello all,</p>
<p>I am trying use OpenIGTLink to remotely control multiple PLUS servers; therefore, I would like to be able to assign each server with a different port number for remote connections.  When I try to run the PlusServerLauncher with a non-default port option, however, the launcher still uses the default value. I am not getting any debug/error messages in the PLUS log.</p>
<p>What is the correct way to set the remote control server port number?</p>
<p>FYI, I need to use this specific version of PLUS because I am using a Telemed Ultrasound.</p>
<p>Also, I have been referencing this page in PLUS user manual: <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/ApplicationPlusServerLauncher.html" class="inline-onebox" rel="noopener nofollow ugc">Plus applications user manual: PlusServerLauncher application</a></p>
<p>Thanks,<br>
Bryn</p>

---

## Post #2 by @Sunderlandkyl (2020-02-04 21:25 UTC)

<p>Thanks for reporting this, I see where the issue is.<br>
I should have it fixed for tomorrow’s 2.9.0 build.</p>

---

## Post #3 by @brynpitt (2020-02-04 21:31 UTC)

<p>Hi Kyle,</p>
<p>Just want to be certain: will the fixed build include the 32-bit Telemed version?</p>
<p>Thanks for the lightning fast response.</p>
<p>–Bryn</p>

---

## Post #4 by @Sunderlandkyl (2020-02-04 21:34 UTC)

<p>Yes, it should be in all 2.9.0 packages.<br>
Fix commited in: <a href="https://github.com/PlusToolkit/PlusApp/commit/022b876e8a5907e36b0b8d9b8a06d63341cee116" rel="nofollow noopener">022b876</a>.</p>

---
