# Best & easiest web service to run 3d slicer.

**Topic ID**: 24649
**Date**: 2022-08-05
**URL**: https://discourse.slicer.org/t/best-easiest-web-service-to-run-3d-slicer/24649

---

## Post #1 by @MZA (2022-08-05 06:50 UTC)

<p>Hi everyone,<br>
What is the easiest appstream or cloud web service I can use to run 3d slicer 5.0.3 for segmentation (files with extension .seg.nrrd &amp; .nii). My laptop cannot run versions beyond 4.8.1 and the segmentation files I have are not working on this version.<br>
I am asking the (easiest) because I am not an expert, I just want to run version 5.0.3.<br>
Any advice.<br>
Thanks in advance.</p>

---

## Post #2 by @pieper (2022-08-05 13:12 UTC)

<p>There are lots of options these days to rent a nice workstation by the hour or even by the minute and it would be great if people could share their experience with various options.</p>
<p>We <a href="https://discourse.slicer.org/t/running-slicer-in-a-web-browser-via-amazon-appstreams/21431">have had good luck</a> with AWS app streaming which can be set up through the web console and offers a wide range of options from small machines through huge GPU workstations running windows or linux.  Realistically it takes a while to figure out how to get it running but once you do it’s easy.  I’ve also got <a href="https://github.com/pieper/SlicerMachines">a project to make bootable cloud disk images running Slicer</a> but this is even more complicated to use.</p>
<p>There are many providers and convenience, cost, and network latency may make one or another option better.  Search for terms like “vdi” (virtual desktop interface) and “virtualization” to see options.  You just need any kind of desktop with a browser that lets you install the slicer application.  If you are only doing segmentation a GPU could even be optional.</p>

---

## Post #3 by @MZA (2022-08-25 17:00 UTC)

<p>Thank you for your reply.<br>
Any tutorials how to use 3D Slicer on AWS App Stream?</p>

---

## Post #4 by @pieper (2022-08-25 19:17 UTC)

<p>The generic App Stream tutorials work fine.  I tested it recently to build an image and the only unique thing you need to do is install Slicer in the image builder step, which is basically just running the regular windows installer.  The overall process is a bit involved but it’s nicely documented.</p>

---
