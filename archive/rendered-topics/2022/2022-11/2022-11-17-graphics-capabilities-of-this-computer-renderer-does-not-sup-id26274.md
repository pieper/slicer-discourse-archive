# Graphics capabilities of this computer: Renderer does not support required OpenGL capabilities

**Topic ID**: 26274
**Date**: 2022-11-17
**URL**: https://discourse.slicer.org/t/graphics-capabilities-of-this-computer-renderer-does-not-support-required-opengl-capabilities/26274

---

## Post #1 by @user_ghost (2022-11-17 05:34 UTC)

<p>Hello every teachers:<br>
my 3D Slicer’s version is 4.11 , when i open it, these information shows as follows<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/257ae2b0302eb5e897415316ca0316ef2fd1880b.png" alt="image" data-base62-sha1="5lyWJIJ2NsRG0EMOGHBhxxqHGD9" width="510" height="211"><br>
how can i fix it</p>

---

## Post #2 by @jay1987 (2022-11-17 05:40 UTC)

<p>it’s possible  that your operating system does not support OpenGL</p>

---

## Post #3 by @user_ghost (2022-11-17 05:50 UTC)

<p>i can open it   two hours ago.this question happened just now</p>

---

## Post #4 by @Dhruba (2022-11-17 06:50 UTC)

<p>Maybe hit “Ignore”, then see if it works as before. Otherwise, uninstall and then install again.</p>

---

## Post #5 by @cmartin (2022-11-17 10:26 UTC)

<p>Have you tried to update your graphics driver? Just install the latest version of it and see if this has any effects.</p>

---

## Post #6 by @fab672000 (2022-11-17 17:42 UTC)

<p>Your most probable issue is that you run a graphics drivers currently without opengl support, it may support mesa though in linux based os’es.  but you have to dig in the documentations, possibly need to rebuild 3d slicer or at least reconfigure it for mesa options if you don’t find an opengl capable driver for your gfx?</p>

---

## Post #7 by @lassoan (2022-11-18 13:52 UTC)

<p><a class="mention" href="/u/user_ghost">@user_ghost</a> What operating system do you use? Do you use the computer via some remote desktop software?</p>

---
