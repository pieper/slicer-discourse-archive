# Graphics capabilities of this computer:  Renderer does not support required OpenGL capabilities.

**Topic ID**: 33436
**Date**: 2023-12-18
**URL**: https://discourse.slicer.org/t/graphics-capabilities-of-this-computer-renderer-does-not-support-required-opengl-capabilities/33436

---

## Post #1 by @Michelle_Cataldo (2023-12-18 02:28 UTC)

<p>Hi guys, just upgraded my pc from a 1060 to a 4070 (Gigabyte dual fan) OC, to work on Machine learning in the dental area.</p>
<p>I had a Razer blade 13" where my slicer worked, with W10.<br>
Now on my new desktop Mini itx, it isnt working.<br>
I already installed the latest drives and I’m on windows 11.</p>
<p>this is the error:</p>
<pre><code class="lang-auto">See more information and help at:

https://slicer.readthedocs.io/en/v5.6/user_guide/get_help.html#slicer-application-does-not-start

Graphics capabilities of this computer:

Renderer does not support required OpenGL capabilities.
</code></pre>
<p>Can someone guide me?</p>

---

## Post #2 by @RafaelPalomar (2023-12-18 06:32 UTC)

<p><a class="mention" href="/u/michelle_cataldo">@Michelle_Cataldo</a>, if your Mini ITX motherboard has integrated graphics, one thing to try is ensuring that 3D Slicer is using your NVIDIA GPU. You can set this in the NVIDIA Control Panel under Manage 3D settings &gt; Program Settings</p>

---

## Post #3 by @Michelle_Cataldo (2023-12-18 11:35 UTC)

<p>I did trued that, and confirmed that my nvidia 4070 has the 3d and opengl option selecting it directly. Could be a problem with the display? I do use and old monitor with hdmi until the new one comes today. My actual monitor doesnt even have gsync or adaptative sync.</p>
<p>Thank you very much rafael!</p>

---

## Post #4 by @RafaelPalomar (2023-12-18 12:29 UTC)

<p>I doubt the monitor is the problem here. Usually the problem is either drivers or wrong GPU selection to run Slicer. Could you have a look at this post and try the couple of suggestions mentioned there? <a href="https://discourse.slicer.org/t/error-on-first-run/22048/7" class="inline-onebox">Error on first Run - #7 by lassoan</a></p>

---

## Post #5 by @Michelle_Cataldo (2023-12-18 12:39 UTC)

<p>Ok! Ill try them when i get home, also, ill post a status of the nvidia config. Thank you!</p>

---

## Post #6 by @muratmaga (2023-12-18 15:57 UTC)

<p>Also I think the GPU switching is now handled by Windows under the graphics settings. Make sure Slicer is set to use the high-performance 4070 GPU in there as well.</p>

---

## Post #7 by @Michelle_Cataldo (2023-12-19 03:08 UTC)

<p>I got it to work. I changed the display and… tada! Worked. Thank you guys!</p>

---
