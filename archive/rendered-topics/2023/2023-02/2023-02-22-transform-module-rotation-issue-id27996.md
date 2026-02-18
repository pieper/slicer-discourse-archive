# Transform module rotation issue

**Topic ID**: 27996
**Date**: 2023-02-22
**URL**: https://discourse.slicer.org/t/transform-module-rotation-issue/27996

---

## Post #1 by @Young_Wang (2023-02-22 23:29 UTC)

<p>Hi everyone,</p>
<p>I’m working on aligning two volumes using the transform module, and I noticed something funky. I wonder if anyone else has encountered the same issue before. I got a rough alignment done with simple translation but I noticed when I try to use rotation to touch up. The volume doesn’t align with where I hope it should be. I’m curious to know what’s the rotation origin of the rotation and if is there a way to change it.<br>
Thank you for your help in advance.</p>

---

## Post #2 by @ebrahim (2023-02-23 05:48 UTC)

<p>You can look at <em>Volume Information</em> in the <em>Volumes</em> module to see and edit the image origin.</p>
<p>One possible source of added confusion: Note that translation and rotation do not commute. The effect of doing them in one order or the other is effectively to change the center of rotation.</p>

---

## Post #3 by @Young_Wang (2023-02-23 13:32 UTC)

<p><a class="mention" href="/u/ebrahim">@ebrahim</a> thank you for the reply. Is it safe to assume that the rotation center is the volume center? I also notice there is a local and global frame toggle in the transform module but I don’t think it promotes you which one is being used.</p>

---

## Post #4 by @ebrahim (2023-02-23 14:47 UTC)

<blockquote>
<p>Is it safe to assume that the rotation center is the volume center?</p>
</blockquote>
<p>I believe the rotation center is the image origin, which could be anywhere</p>

---
