# Linux 4.10.1 volume rendering crash issue

**Topic ID**: 5554
**Date**: 2019-01-29
**URL**: https://discourse.slicer.org/t/linux-4-10-1-volume-rendering-crash-issue/5554

---

## Post #1 by @muratmaga (2019-01-29 04:36 UTC)

<p>Trying to open a previously saved mrb, Slicer crashes with this error.</p>
<p>SlicerApp-real[46207]: segfault at 0 ip 00002aab9bc04c4e sp 00007fffffffad30 error 4 in libvtkSlicerVolumeRenderingModuleLogic.so[2aab9bbf9000+15000]</p>
<p>Anyway to understand what’s causing it? This is on Centos 7.2 with slicer 4.10.1</p>

---

## Post #2 by @pieper (2019-01-29 07:56 UTC)

<p>Hi Murat -</p>
<p>Dp you think it’s the file or the machine? Does the same mrb open on a different machine/os?  Can you create a new mrb on that machine and reproduce the issue?</p>

---

## Post #3 by @muratmaga (2019-01-29 16:39 UTC)

<p>It must be the mrb and data it contains. It also crashes on windows or get stuck at 52% if I unpack the contents of the mrb file and load the top level mrml.</p>
<p>We created this scene file, and all other mrbs also created on the same installation of Slicer seems to work fine. Weird.</p>

---
