---
topic_id: 29928
title: "How To Disable The Splash Screen Before Launching The Progra"
date: 2023-06-09
url: https://discourse.slicer.org/t/29928
---

# How to disable the splash screen before launching the program

**Topic ID**: 29928
**Date**: 2023-06-09
**URL**: https://discourse.slicer.org/t/how-to-disable-the-splash-screen-before-launching-the-program/29928

---

## Post #1 by @nnzzll (2023-06-09 03:32 UTC)

<p>I am developing a custom app of Slicer and I need to setup the splash screen defined by user’s choice.</p>
<p>I’ve read this post :<a href="https://discourse.slicer.org/t/change-the-splash-screen-of-slicer-upon-launch/18478">change-the-splash-screen-of-slicer-upon-launch</a>, noticed that there are two splash screen during launch. I replaced the second splash screen successfully but I don’t know how to disable the first splash screen in my own code.</p>
<p>I know that I can modify the <code>XXXLauncherSettings.ini</code> but it is under the <code>Slicer-build</code> directory which can’t (and shouldn’t) be tracked by git.</p>
<p>And from this post:<a href="https://discourse.slicer.org/t/modify-value-in-slicerlaunchersettings-ini-from-application/23000">modify-value-in-slicerlaunchersettings-ini-from-application</a> I know I can modify the <code>.ini</code> file in application but at that time the application is already launched. What I need is to modify the value before launching the program.</p>

---

## Post #2 by @lassoan (2023-06-16 14:54 UTC)

<p>You can replace the launcher splashscreen image in your custom application.</p>
<p>Disabling the launcher splashscreen might not be a good idea because it may take a couple of seconds for the SlicerApp-real splashscreen to appear and the user may not know what’s happening in the meantime and may start the application repeatedly. However, if you want to do it then you can do that by modifying the launcher configuration <a href="https://github.com/Slicer/Slicer/blob/c3d74d68839078ec02b1053d4ba413643e84630c/SuperBuild/python_configure_python_launcher.cmake#L239">as it is done for the Python launcher</a>.</p>

---

## Post #3 by @apparrilla (2024-10-03 22:16 UTC)

<p>Sorry <a class="mention" href="/u/lassoan">@lassoan</a> ,  Do you mean there is a Cmake Flag “SPLASHSCREEN_DISABLED” for CustomApps?</p>

---

## Post #4 by @lassoan (2024-11-07 05:48 UTC)

<p>The CMake option name is <code>SLICERAPP_SPLASHSCREEN_ENABLED</code> and it is used <a href="https://github.com/Slicer/Slicer/blob/fefe4a3401b557f0aec9628c4be2f92fcc4e23eb/CMake/SlicerMacroBuildApplication.cmake#L700-L710">here</a>. If you use the Slicer Custom Application Template then you may be able to set the option in <a href="https://github.com/KitwareMedical/SlicerCAT/blob/main/Applications/SlicerCATApp/slicer-application-properties.cmake">slicer-application-properties.cmake</a>.</p>

---
