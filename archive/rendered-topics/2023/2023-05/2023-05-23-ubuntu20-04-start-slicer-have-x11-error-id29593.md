---
topic_id: 29593
title: "Ubuntu20 04 Start Slicer Have X11 Error"
date: 2023-05-23
url: https://discourse.slicer.org/t/29593
---

# Ubuntu20.04, start Slicer, have X11 error

**Topic ID**: 29593
**Date**: 2023-05-23
**URL**: https://discourse.slicer.org/t/ubuntu20-04-start-slicer-have-x11-error/29593

---

## Post #1 by @Liang_Ma (2023-05-23 03:05 UTC)

<p>Hello, I download the recent release, run Slicer application, and meet such an error ( a GUI display shortly and crashed)</p>
<p>$ ./Slicer<br>
The X11 connection broke: No error (code 0)<br>
X connection to :1 broken (explicit kill or server shutdown).<br>
$ echo $DISPLAY<br>
:1</p>
<p>I run xclock/xeyes to confirm that there is no problem with my other  X applications.</p>
<p>Note I am using a Nvidia 3060 GPU card and I am using Nvidia driver</p>

---

## Post #2 by @Liang_Ma (2023-05-23 07:33 UTC)

<p>OK, I switched over to another Nvidia driver version–problem solved…</p>

---
