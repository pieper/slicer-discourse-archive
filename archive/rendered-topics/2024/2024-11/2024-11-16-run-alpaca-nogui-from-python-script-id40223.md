# Run ALPACA nogui from python script

**Topic ID**: 40223
**Date**: 2024-11-16
**URL**: https://discourse.slicer.org/t/run-alpaca-nogui-from-python-script/40223

---

## Post #1 by @atha_morph (2024-11-16 01:20 UTC)

<p>Hello all,<br>
I would like to run ALPACA lib or the initial python library, in my python script.<br>
Any Idea how can I do it?<br>
I would like to give as input Source model, Source landmarks and Target model and the final return would be Target Landmarks.</p>

---

## Post #2 by @muratmaga (2024-11-16 02:33 UTC)

<p>This came up a few times, but I never quite understand why. You will not benefit from building a script only to do interactive landmark transfer. And we already provide an interface to do batch landmark transfer for many samples.</p>

---

## Post #3 by @atha_morph (2024-11-16 09:59 UTC)

<p>Hello Murat,<br>
Thank you for the suggestion.<br>
Can I use batch landmark transfer with no gui?<br>
In other case ,can I just use the python libraries <em>open3d</em> or <em>pycpd</em>?</p>

---

## Post #4 by @muratmaga (2024-11-16 23:26 UTC)

<p>Why don’t you want to use GUI?</p>
<p>In any event, you can look at the logic part of the ALPACA module and build up a entirely scripted version. Though, I still don’t understand why…</p>
<p>ALPACA does not use open3d anymore. We have switched to ITK.</p>

---
