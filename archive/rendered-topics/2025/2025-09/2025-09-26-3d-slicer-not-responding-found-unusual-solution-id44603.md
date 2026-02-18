# 3D slicer not responding - Found unusual solution

**Topic ID**: 44603
**Date**: 2025-09-26
**URL**: https://discourse.slicer.org/t/3d-slicer-not-responding-found-unusual-solution/44603

---

## Post #1 by @PiasTanmoy (2025-09-26 19:19 UTC)

<p>I have been struggling with Slicer not responding for the last few weeks and finally found a working solution for my case.</p>
<p>System info: Windows 11, Slicer 5.8</p>
<p>Solution: Remove your Slicer settings directory (for example, <code>c:\Users\&lt;yourusername&gt;\AppData\Roaming\slicer.org</code></p>
<p>Reference: <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html" class="inline-onebox" rel="noopener nofollow ugc">Get Help — 3D Slicer documentation</a></p>
<p>However, I need to delete this folder every time before starting Slicer. Otherwise, it doesn’t work.<br>
I am not sure what the permanent solution is.</p>

---

## Post #2 by @lassoan (2025-09-26 19:21 UTC)

<p>You should not need to delete the folder every time. If you find that you often need to do it then probably there is something unusual about your display configuration. Do you use multiple screens?</p>

---

## Post #3 by @PiasTanmoy (2025-09-29 17:04 UTC)

<p>Yes, I have 2 displays with my desktop.<br>
Do you have any suggestions on how to make it work with 2 displays?</p>
<p>Thank you!</p>

---

## Post #4 by @lassoan (2025-09-29 17:25 UTC)

<p>Slicer saves your window positions by default. If you change your display configurations (sometimes unplug a monitor, change resolution, etc.) then the windows might be restored in invalid positions.</p>
<p>If you often change your screen configuration then it may make sense to disable “Save user interface size and position on exit” option in menu: Edit → Application settings → Appearance.</p>
<p>If you rarely change your screen configuration then managing your Slicer application settings file (<a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#settings-file-location">Slicer.ini</a>) can help. For example, you could save a settings file that you use for a single screen and another settings file that you use for two screens.</p>

---

## Post #5 by @PiasTanmoy (2025-09-29 17:54 UTC)

<p>Disabling the “Save user interface size and position on exit” option worked!</p>
<p>I don’t usually change the display configuration. It has been the same for the last few months. I am not sure if the system (e.g., OS) does something in the background or not. But this trick worked for me anyway!</p>
<p>Thank you so much!</p>

---
