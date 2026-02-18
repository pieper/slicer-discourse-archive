# Starting Slicer in Ubuntu 20.04

**Topic ID**: 20078
**Date**: 2021-10-09
**URL**: https://discourse.slicer.org/t/starting-slicer-in-ubuntu-20-04/20078

---

## Post #1 by @ogdenk (2021-10-09 05:03 UTC)

<p>Hi Everyone,</p>
<p>I am starting to use 3D Slicer in Linux.  Overall it seems to be working great, but I have an issue with associating the application with the .mrml file format.  I am not a long time Linux user, and I can’t seem to get this to work.  Can someone offer me a suggestion for this?</p>
<p>Thanks!</p>
<p>Kent</p>

---

## Post #2 by @chir.set (2021-10-09 07:46 UTC)

<p>If you are already in your file manager, you could just drag and drop on a slice view or a 3D view.</p>
<p>File association depends on your desktop environment and file manager. In KDE/Dolphin, you would right click, Properties, Options. Not the best thing to do with Slicer files, it’s not like with a text editor that you would open and close many times a day.</p>

---

## Post #4 by @ogdenk (2021-10-12 13:15 UTC)

<p>Ok, Thanks for that. I was just hoping to avoid having to open Slicer, like I can do in Windows. Working in Ubuntu is just a little different, but no big deal.</p>
<p>Kent</p>

---

## Post #5 by @muratmaga (2021-10-12 14:44 UTC)

<p>you can write a little .desktop file, associate an icon it will be part of your applications. An example is here<br>
<a href="https://github.com/muratmaga/virtualgl_docker_examples/blob/vgl_slicer_turbovnc_novnc-eglbackend/usr/share/applications/slicer.desktop" class="inline-onebox" rel="noopener nofollow ugc">virtualgl_docker_examples/slicer.desktop at vgl_slicer_turbovnc_novnc-eglbackend · muratmaga/virtualgl_docker_examples · GitHub</a>.</p>
<p>Where you copy and add this file depends on your OS and window manager though.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> is it possible to bundle something like this in Slicer or have an easier way to integrate with the UIs application menu?</p>

---

## Post #6 by @lassoan (2021-10-12 16:19 UTC)

<p>What do you do with such a .desktop file?<br>
Drag-and-drop it somewhere in the window manager?</p>
<p>Does the file have to contain absolute path to the Slicer executable? If yes, then the file has to be generated at runtime. How is it usually done in other applications? Is a popup shown after the application starts?</p>
<p>Somewhat related: how file associations and custom URL handlers are usually set up on popular distributions and window managers?</p>

---

## Post #7 by @muratmaga (2021-10-12 16:46 UTC)

<p>In most linuxes that I used (ubuntu/centos) they are added to /usr/share/applications to make it an item available in the start menu. but requires sudo access, and since most people use apt or yum to install these packages, it is not issue for them, but it would be for us.</p>
<p>I was hoping someone more knowledgeable than me with Linux can clarify if it is possible to do this in user space, without sudo access and in a WM generic way. I think some files written under .config.</p>
<p>I am not sure about the absolute vs relative path issue. I always put the full path to the executable. But in our case it is not predictable.</p>

---

## Post #8 by @pieper (2021-10-12 17:12 UTC)

<p>I’ve never explored these options deeply in linux because there’s so much variability across distributions.  If we want to help people do this I’d suggest developing a script that would perform linux-specific customizations on the fly and let people debug and contribute so that it supports a range of systems.</p>

---
