# How can I adjust window level of background volume?

**Topic ID**: 37880
**Date**: 2024-08-14
**URL**: https://discourse.slicer.org/t/how-can-i-adjust-window-level-of-background-volume/37880

---

## Post #1 by @nnzzll (2024-08-14 08:32 UTC)

<p>When foreground volume and background volume are both set up and foreground opacity is not zero,  only foreground volume’s window level can be changed when interaction node switched to AdjustWindowLevel mode.<br>
How can I adjust window level of the background volume?</p>

---

## Post #2 by @cpinter (2024-08-14 08:59 UTC)

<p>If you decrease the opacity of the foreground volume, then you can adjust W/L of the background volume.</p>

---

## Post #3 by @nnzzll (2024-08-14 09:54 UTC)

<p>What I want to do is to adjust W/L of the background and keep the opacity of the foreground volume unchanged, is it possible?</p>

---

## Post #4 by @cpinter (2024-08-14 10:21 UTC)

<p>I don’t quite understand the problem. You change the opacity (if you find the GUI troublesome you can use Ctrl+DragMouseDown to decrease the opacity), then set the W/L then restore the opacity. You typically only need to set the W/L once for volume and workflow.</p>
<p>Alternatively you can use the Volumes module. Select the foreground volume and use the Window/level section.</p>

---

## Post #5 by @lassoan (2024-08-15 12:38 UTC)

<p>You can also always go to Volumes module to adjust window/level of any volume anytime.</p>

---
