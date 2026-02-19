---
topic_id: 25824
title: "Launching Slicer Executable From Command Line"
date: 2022-10-21
url: https://discourse.slicer.org/t/25824
---

# Launching slicer executable from command line

**Topic ID**: 25824
**Date**: 2022-10-21
**URL**: https://discourse.slicer.org/t/launching-slicer-executable-from-command-line/25824

---

## Post #1 by @Shravan_Seshadri (2022-10-21 03:11 UTC)

<p>I am trying to launch the 3d slicer from a linux command line to install monailabel plugin. I am remotely ssh’sd into a linux machine- and am serving monailabel server to localhost but when i run the slicer executable nothing happens. No sure what the issue is here- do I have to start the server before running the slicer executable and hpw dp I get the GUI to display?</p>

---

## Post #2 by @pieper (2022-10-21 12:35 UTC)

<p>With MONAI Label, only the server is run on the remote host, and you can do this with ssh by tunneling the port.  Slicer runs on your local machine for graphics. You install the slicer module on the local Slicer.  You can watch some of the videos on <a href="https://monai.io/label.html">the web site</a> to get the idea.</p>

---
