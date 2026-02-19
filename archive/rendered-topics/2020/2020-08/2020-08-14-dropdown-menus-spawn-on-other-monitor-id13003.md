---
topic_id: 13003
title: "Dropdown Menus Spawn On Other Monitor"
date: 2020-08-14
url: https://discourse.slicer.org/t/13003
---

# Dropdown menus spawn on other monitor

**Topic ID**: 13003
**Date**: 2020-08-14
**URL**: https://discourse.slicer.org/t/dropdown-menus-spawn-on-other-monitor/13003

---

## Post #1 by @mikebind (2020-08-14 18:25 UTC)

<p>Problem report for Slicer 4.11.0-2020-08-10 win-amd64.</p>
<p>Some dropdown menus (e.g. for recent modules, layouts, crosshair, but NOT the Modules selector) spawn on a different screen than is occupied by the Slicer application.  The screenshot below shows an example with the layout menu.  The screenshot bridges an external monitor (upper, where the Slicer window is) and my laptop screen (lower, where the layout menu appears).  The top of the layout menu is at the top of my laptop screen.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6524bd44a5548ff84ebcf8aba770936efa7c790e.jpeg" data-download-href="/uploads/short-url/eqKWaiLB3yzjLpmAbfxARuxxHAy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6524bd44a5548ff84ebcf8aba770936efa7c790e_2_444x500.jpeg" alt="image" data-base62-sha1="eqKWaiLB3yzjLpmAbfxARuxxHAy" width="444" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6524bd44a5548ff84ebcf8aba770936efa7c790e_2_444x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6524bd44a5548ff84ebcf8aba770936efa7c790e_2_666x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6524bd44a5548ff84ebcf8aba770936efa7c790e_2_888x1000.jpeg 2x" data-dominant-color="AFADB0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1914×2154 753 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I move the Slicer application window to my laptop screen, all the dropdown menus appear in their proper places.</p>
<p>This problem was <strong>not</strong> present in the prior preview release I used, 2020-05-27. It is also not present in any of the module UI dropdowns (built-in or ones I’ve added with QComboBox or qMRMLNodeComboBoxes).  So far, I have only seen it occur with dropdowns from the Slicer Toolbar.  It happens for all of those except the module selector (the one which shows the currently selected module).</p>
<p>Both screens are high resolution (laptop is 3840x2160 and external monitor is 3440x1440).</p>

---

## Post #2 by @pieper (2020-08-14 18:33 UTC)

<p>Interesting - can you report the Qt versions for one that works vs one that doesn’t?  (<code>qt.qVersion()</code> in the python window).</p>

---

## Post #3 by @jamesobutler (2020-08-14 18:49 UTC)

<p>That looks similar to <a href="https://bugreports.qt.io/browse/QTBUG-85012" rel="nofollow noopener">https://bugreports.qt.io/browse/QTBUG-85012</a>.</p>
<p>2020-05-27 on Windows was using Qt 5.14.2 and then starting with 2020-05-29 on Windows it is using Qt 5.15.0.</p>
<p>I would guess maybe once there is a Qt 5.15.1, it will be fixed.</p>

---

## Post #4 by @mikebind (2020-08-14 19:05 UTC)

<p>I agree it looks very similar. Hopefully it will be resolved soon, it is inconvenient and messy (but ultimately still functional).</p>

---

## Post #5 by @Alex_Vergara (2020-08-14 19:25 UTC)

<p>This happens to me in Mac in full window mode when I have multiple monitors</p>
<p>Mac handles multiple screens in each monitor, somehow slicer fails to render the menu in the proper one</p>

---

## Post #6 by @pieper (2020-08-14 19:41 UTC)

<p>I haven’t seen this bug on my two-monitory mac setup, but I’ve seen some odd behavior like this on linux, even with single screen sessions (menus pop up a few inches from where they should).</p>

---

## Post #7 by @cpinter (2020-08-14 20:06 UTC)

<p>I have had this on my Windows 10 machine, with Qt 5.15.0. When the Slicer main window is on the secondary screen, the module history list shows up in the corner of the primary monitor.</p>
<p>Some stuff are unfortunately not right with Qt 5.15 LTS <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=9" title=":frowning:" class="emoji" alt=":frowning:"></p>

---

## Post #8 by @ungi (2020-08-16 02:32 UTC)

<p>It is the same issue on my computer too. I’ve been planning to report it…</p>

---

## Post #9 by @lassoan (2020-08-16 14:53 UTC)

<p>I’ve created a bug for it so that we consider it for Slicer-5.0 release: <a href="https://github.com/Slicer/Slicer/issues/5106">https://github.com/Slicer/Slicer/issues/5106</a></p>

---

## Post #10 by @mikebind (2020-09-16 19:21 UTC)

<p>This issue is still present on the 2020-09-15 preview release on Windows.  It looks like Qt has been updated to fix this, any word on when that fix will appear in the preview releases?  Thanks!</p>

---

## Post #11 by @jamesobutler (2020-09-16 19:53 UTC)

<p>You can follow the progress of updating the Slicer preview factory builds to Qt 5.15.1 in <a href="https://github.com/Slicer/DashboardScripts/pull/31" rel="noopener nofollow ugc">https://github.com/Slicer/DashboardScripts/pull/31</a>.  I’ve already confirmed by building Slicer from source with Qt 5.15.1 that it fixes the issue.</p>

---

## Post #12 by @dvijay (2024-09-02 04:07 UTC)

<p>This issue is almost 4 years old, so I assumed that even with installation (not building from source) it might have been fixed but I am facing the same issue still. Slicer: 5.6.1 r32438 / 117ce5f on Windows 11.</p>
<p>It only happens on secondary monitor I connect using HDMI and not on the primary monitor (laptop screen).</p>

---

## Post #13 by @Matteboo (2024-09-02 11:25 UTC)

<p>Same thing is happening for me the first time I open a drop down menu on my second monitor. But if I close the menu and open it again it appears in the correct location.</p>

---

## Post #14 by @lassoan (2024-09-02 21:46 UTC)

<p>Which menu appears on a wrong monitor? Only the layout selection menu or others, too?</p>
<p>Unfortunately, there is a Qt bug that has not been fixed in Qt-5.12 (that we use in currently Slicer) that very large menus appear on the first screen if they are opened near the bottom of the screen (so that the full menu would not fit below the menu). Maybe <a href="https://github.com/Slicer/Slicer/issues/6388">upgrading to Qt6 would fix the issue</a>. Or, we could make the layout selector menu shorter (which could be useful anyway, as there are just too many menu items in it now).</p>

---

## Post #15 by @Matteboo (2024-09-03 12:23 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae9613f8528e9b5c9c5f6433dd3f33b7c75015e0.png" alt="image" data-base62-sha1="oUsCtecil8JsyobU6zrg6KDPLDq" width="624" height="372"></p>
<p>This kind of drop down menu. It only does that the frst time I open a menu after starting up slicer sometimes. It behaves differently on my home and work set-up, so I guess it has to do with wich screen is the main screen or if I connected the screen after slicer load up maybe.<br>
Nothing major, I just thought it could help find the origin of the issue.</p>

---
