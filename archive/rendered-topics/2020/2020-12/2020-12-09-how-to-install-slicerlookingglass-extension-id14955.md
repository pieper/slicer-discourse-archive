---
topic_id: 14955
title: "How To Install Slicerlookingglass Extension"
date: 2020-12-09
url: https://discourse.slicer.org/t/14955
---

# How to install SlicerLookingGlass extension

**Topic ID**: 14955
**Date**: 2020-12-09
**URL**: https://discourse.slicer.org/t/how-to-install-slicerlookingglass-extension/14955

---

## Post #1 by @Jozka (2020-12-09 03:11 UTC)

<p>HI,</p>
<p>I would like to install <a href="https://github.com/KitwareMedical/SlicerLookingGlass" rel="noopener nofollow ugc">SlicerLookingGlass</a> extension, but I could not find it in Extensions Manager in Slicer app or do not know how to install from source codes in GitHub. Does anyone have an experience of using the extension?</p>

---

## Post #2 by @lassoan (2020-12-09 18:53 UTC)

<p>SlicerLookingGlass requires VTK9. We ran into <a href="https://github.com/Slicer/Slicer/issues?q=is%3Aissue+is%3Aopen+label%3Adomain%3Avtk9">problems with upgrading Slicer to VTK9</a>, so we had to revert to VTK8 until the problems are fixed. We should be able to move to VTK9 within 1-2 weeks and then SlicerLookingGlass extension will be available.</p>

---

## Post #3 by @Jozka (2020-12-10 07:53 UTC)

<p>Thank you very much for the information. I am looking forward to seeing new version of Slicer based on VTK9.</p>

---

## Post #4 by @Jozka (2021-01-18 01:48 UTC)

<p>I’ve found a <a href="https://www.youtube.com/watch?v=7-ROJ6awzqk" rel="noopener nofollow ugc">YouTube clip</a> which shows an actual operation of Looking Glass with 3D slicer. I am wondering if there is a way to enable the extension. I still could not find SlicerLookingGlass extension on beta build 2021-01-17.</p>

---

## Post #5 by @lassoan (2021-01-18 02:14 UTC)

<p>We still have a few more open issues with VTK9 in Slicer, so you either need to build Slicer with VTK9 yourself or wait for us to switch the Slicer Preview Release to VTK9. It will take at least 1-2 weeks, hopefully not much more.</p>
<p>If it is urgent for you and cannot build Slicer then maybe <a class="mention" href="/u/jcfr">@jcfr</a> can send you a private build.</p>

---

## Post #6 by @Jozka (2021-01-18 02:29 UTC)

<p>Thank you for your message. I now understand that it was achieved by self-build app. I’m grateful for your hard work to maintain and upgrade 3D slicer codes.</p>

---

## Post #7 by @redbeard (2021-02-04 04:02 UTC)

<p>Hi Andras,</p>
<p>I have just purchased a LookingGlass device and want to display a CT Scan on it.   Has the SlicerLookingGlass extension been completed?   I cant find it anywhere.</p>
<p>Kind regards<br>
Malcolm</p>

---

## Post #8 by @jcfr (2021-02-04 07:22 UTC)

<p>In  the next two weeks, we will re-enable VTK 9 in the Slicer nightly build and the LookingGlass extension will be available for download.</p>
<p>In the meantime, you could first build Slicer from source setting the <code>Slicer_VTK_VERSION_MAJOR</code> option to <code>9</code>, and then you could build the <a href="https://github.com/KitwareMedical/SlicerLookingGlass">SlicerLookingGlass</a> extension.</p>

---

## Post #9 by @Jozka (2021-02-26 07:19 UTC)

<p>I install the latest preview release of Slicer each day to find SlicerLookingGlass extension. Is there any way to know whether the latest build is based on VTK9 or still VTK8 without installation?</p>

---

## Post #10 by @lassoan (2021-02-27 21:02 UTC)

<p>The extension will be available for the Slicer Preview Release in a few days.</p>

---

## Post #11 by @Justin_Hirsch (2021-05-14 15:57 UTC)

<p>I am trying to get my looking glass portrait working with slicer.  I have the Preview Release of slicer installed and the LookingGlass extension installed but I cannot find the panel anywhere in the software.  I am running on a MacBook Pro with the integrated GPU.  Is a discrete GPU required for this integration?</p>
<p>Otherwise, any tips on how I can get this working?</p>
<p>Thanks</p>
<p>Justin</p>

---

## Post #12 by @Jozka (2021-05-15 00:50 UTC)

<p>Hi Justin,</p>
<p>You can find it to click Find Module icon which is available in the shape of magnifying glass next to Module list and to type “LookingGlass” in Module finder window.</p>

---

## Post #13 by @Justin_Hirsch (2021-05-18 20:14 UTC)

<p>It didn’t appear in that list either.  I turned on development mode and then when looking at the logs I saw a message that the libHoloPlayCore.dylib file was missing.  I found a copy in a different app and added to the Application Frameworks directory.  Now the plugin shows up in the menu and sort of works, although I found it often crashses the software when using it, and the output aspect ratio is a bit off.</p>

---

## Post #14 by @lassoan (2021-05-18 20:37 UTC)

<p>The crashes may be due to a slightly incompatible dylib.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> while <a class="mention" href="/u/jcfr">@jcfr</a> finds the time to investigate this, could you make the libHoloPlayCore.dylib that is on the factory machine available so that <a class="mention" href="/u/justin_hirsch">@Justin_Hirsch</a> can test with that?</p>

---

## Post #15 by @Sam_Horvath (2021-05-19 12:35 UTC)

<p>This package: <a href="https://www.paraview.org/files/dependencies/HoloPlayCore-0.1.1-Open-20200923.tar.gz">https://www.paraview.org/files/dependencies/HoloPlayCore-0.1.1-Open-20200923.tar.gz</a> has the binaries used on the Slicer Factory.</p>

---

## Post #16 by @egipane (2021-08-16 13:52 UTC)

<p>I have had my Looking Glass Portrait for a week now and tried using it during segmentations using Slicer as a secondary 3D screen. Everything connects and view 1 is shown on the looking glass although the focus is set extremely close.</p>
<p>Buttons in the side menu to adjust the focal plane do not change anything.<br>
Is this a known issue?</p>

---

## Post #17 by @lassoan (2021-09-03 05:05 UTC)

<p>I’m not sure when <a class="mention" href="/u/jcfr">@jcfr</a>, the main developer of this extension can investigate this, so probably the best would be to <a href="https://github.com/KitwareMedical/SlicerLookingGlass/issues">submit an issue in the SlicerLookingGlass repository</a>. If you submit an issue then copy the link here.</p>

---

## Post #18 by @curtislisle (2021-12-30 19:43 UTC)

<p>I am trying to use a Looking Glass Portrait with Slicer.  I am currently running Slicer 4.13.0-2021-08-27. I have used the Extension manager to install the SlicerLookingGlass extension, and I have the HoloPlay daemon installed and running.  When I try to invoke the LookingGlass extension, I see in the Slicer error console, that a VTK library (libvtkRenderingLookingGlass.so) is missing.   I’ll file an issue on the SlicerLookingGlass repository, but wanted to mention the issue here.</p>

---

## Post #19 by @lassoan (2022-01-03 20:23 UTC)

<p>I would recommend to try with the latest Slicer Preview Release. If you have access to Windows PC, it would be nice if you could try with that, too.</p>

---
