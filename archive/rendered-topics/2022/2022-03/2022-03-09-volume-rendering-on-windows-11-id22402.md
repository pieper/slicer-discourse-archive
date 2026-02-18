# Volume rendering on Windows 11?

**Topic ID**: 22402
**Date**: 2022-03-09
**URL**: https://discourse.slicer.org/t/volume-rendering-on-windows-11/22402

---

## Post #1 by @cpinter (2022-03-09 11:39 UTC)

<p>Hi all,</p>
<p>One of the computers I use for development updated itself to Windows 11, and since then volume rendering does not show up in the 3D views, neither with Slicers that had been installed before the update, nor newer Slicers.</p>
<p>Has anyone tried to use Slicer with Windows 11? If so, does volume rendering work? Any other strange findings?</p>
<p>Any ideas what to try to fix volume rendering? An obvious idea is updating the display driver - I’ll do that now.</p>
<p>Thanks!</p>

---

## Post #2 by @muratmaga (2022-03-09 12:07 UTC)

<p>On my windows 11 laptop, GPU volume rendering works normally. Is it possible that you have some driver issue?</p>

---

## Post #3 by @cpinter (2022-03-09 17:21 UTC)

<p>I just had the opportunity to update the driver. It did fix the volume rendering issue.</p>

---

## Post #4 by @cpinter (2022-03-11 10:24 UTC)

<p>I just tried volume rendering in VR and it does NOT show up.</p>
<p>Now thinking about it, maybe at the time of posting I remembered the original problem wrong (and it showed up on the monitor just not in VR).</p>
<p>Suggestions are welcome, thanks!</p>

---

## Post #5 by @adamrankin (2022-03-11 14:49 UTC)

<p>I can confirm this issue occurring. Windows 10, recent build of Slicer. Volume rendering did not show up in VR, models of segmented data did show up in VR.</p>

---
