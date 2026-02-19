---
topic_id: 10060
title: "Module Is Not Registered On Windows Linux Nightly Built"
date: 2020-02-01
url: https://discourse.slicer.org/t/10060
---

# Module is not registered on Windows/Linux nightly built

**Topic ID**: 10060
**Date**: 2020-02-01
**URL**: https://discourse.slicer.org/t/module-is-not-registered-on-windows-linux-nightly-built/10060

---

## Post #1 by @shanshan (2020-02-01 13:32 UTC)

<p>Slicer Ver 4.11 2020-01-31 on Windows<br>
Slicer Ver 4.11 2020-01-31 on Mac<br>
Slicer Ver 4.11 2020-01-30 on Linux</p>
<p>I am having trouble with loading a module we coded last summer into the nightly built of Slicer on Windows and Linux, though there is no problem with loading the module on Mac.<br>
The error we got was simply saying the module is not registered without no further details entailed.</p>
<p>Note that this module can be loaded without any problems on Slicer Ver 4.11 2019-08-29 of any OS.</p>
<p>Has anything changed for Linux and Windows nightly built over the past few months that we should be aware when developing our own module?</p>
<p>Thank you so much for your time and help!</p>

---

## Post #2 by @lassoan (2020-02-01 13:41 UTC)

<p>If this is a CLI or loadable module (not a Python scripted module) then you need to build your module with <em>exactly</em> the same Slicer version as the one you want to use it with.</p>
<p>If you use exactly the same source code version, compiler version, build options, Qt version, etc. to build Slicer on your computer as the official build computers use then your module will even work with official Slicer builds. Any difference may cause ABI incompatibility and is expected to make your module fail to load or the application to crash.</p>

---
