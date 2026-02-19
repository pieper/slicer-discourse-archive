---
topic_id: 11827
title: "Latest Nightly Build Won T Work"
date: 2020-06-02
url: https://discourse.slicer.org/t/11827
---

# Latest nightly build won´t work

**Topic ID**: 11827
**Date**: 2020-06-02
**URL**: https://discourse.slicer.org/t/latest-nightly-build-won-t-work/11827

---

## Post #1 by @Lucas_Formighieri (2020-06-02 14:42 UTC)

<p>Hello,</p>
<p>I´m using a Dell laptop (Core i7, 16 gb ram, Nvidia gpu, drivers up to date, Window10 Brazilian Portuguese). I have updated Windows 10 to the latest version (2004) and the NVidia driver too.</p>
<p>I´ve been using Slicer for quite some time and it was working fine.</p>
<p>Since yesterday it began presenting problems. At first, it would crash at start up. It went past the welcome screen. The app window would open, but remained blank, just with the title in the upper bar [“3D Slicer 4.11.0-2020-05-22 (Not responding)”].</p>
<p>Then I replaced it with the latest nightly build (4.11.0-2020-06-01). I kept receiving messages saying a series of dll files were missing (Qt5Core, Qt5Gui, Qt5Network, Qt5WebChannel, Qt5WebEngineWidgets, Qt5Widgets and Qt5Xml). I downloaded these files and copied to the System32 folder. Now I get the error message “0xc00007b”.</p>
<p>The 4.10.2 version works, but I would like to use the features in the newer versions such as Dynamic Modelling.</p>
<p>What should I do?</p>
<p>Thanks!</p>

---

## Post #2 by @Sam_Horvath (2020-06-02 15:17 UTC)

<p>We have been in the process of updating the compiler/Qt version, so the nightly is a bit unstable. The latest nightly has the bug you observed, but that will be addressed in tomorrow’s build.  In the mean time, perhaps try uninstalling re-installing the 2020-05-22 version?  That version had been working correctly in the past, correct?</p>

---

## Post #3 by @Lucas_Formighieri (2020-06-02 17:39 UTC)

<p>Hi,</p>
<p>Thanks for the answer.</p>
<p>Actually, it was the 2020-05-22 that stopped working (blank screen) and led me to try the 2020-06-01.</p>
<p>I don´t have the 2020-05-22 installation file anymore, and I could´t find it for download.</p>
<p>Anyway, I can wait ultil tomorrow for the new build.</p>
<p>Regards,</p>
<p>Lucas</p>

---

## Post #4 by @lassoan (2020-06-02 19:27 UTC)

<p>You can download any previous Slicer version by specifying the release date in the URL. For example:</p>
<p><a href="https://download.slicer.org/?date=2020-05-22" class="onebox" target="_blank">https://download.slicer.org/?date=2020-05-22</a></p>

---

## Post #5 by @Lucas_Formighieri (2020-06-02 19:57 UTC)

<p>Hello,</p>
<p>I downloanded the 2020-05-22 version and installed it. But it still stops at the blank app screen, with “Slicer 4.11.0-2020-05-21-Not responding” on the title bar. This is exactly the behavior whent it first stopped working.</p>
<p>I tried installing it in the default folder and also in a separated folder (C:\Slicer) but the result is the same.</p>
<p>Lucas</p>

---
