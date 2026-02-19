---
topic_id: 11834
title: "Error Executing Version Slicer 4 11 0 2020 06 01 Linux Amd64"
date: 2020-06-02
url: https://discourse.slicer.org/t/11834
---

# Error executing version Slicer-4.11.0-2020-06-01-linux-amd64.tar.gz on Ubuntu 16.04

**Topic ID**: 11834
**Date**: 2020-06-02
**URL**: https://discourse.slicer.org/t/error-executing-version-slicer-4-11-0-2020-06-01-linux-amd64-tar-gz-on-ubuntu-16-04/11834

---

## Post #1 by @Julio_Torres (2020-06-02 19:00 UTC)

<p>Operating system:Ubuntu LTS 16.04<br>
Slicer version: 4.11.0-2020-06-01<br>
Expected behavior: run the executable<br>
Actual behavior: I does not execute and appear the following message:</p>
<p>qt.qpa.plugin: Could not load the Qt platform plugin “xcb” in “” even though it was found.<br>
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.</p>
<p>Available platform plugins are: xcb.</p>

---

## Post #2 by @Sam_Horvath (2020-06-02 19:05 UTC)

<p>Hi:  We are in the process of updating Qt on the factory systems, so the nightly build is a bit unstable right now.  Please try this older version:  <a href="http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;name=Slicer-4.11.0-2020-05-25-linux-amd64.tar.gz&amp;checksum=c6d78202a7ad02bd1a380b183390f820" rel="nofollow noopener">http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;name=Slicer-4.11.0-2020-05-25-linux-amd64.tar.gz&amp;checksum=c6d78202a7ad02bd1a380b183390f820</a></p>

---
