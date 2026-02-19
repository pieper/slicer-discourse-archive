---
topic_id: 11510
title: "Trouble With Qt And Qtquick Not Being Properly Included In M"
date: 2020-05-12
url: https://discourse.slicer.org/t/11510
---

# Trouble with Qt, and QtQuick not being properly included in macos .app

**Topic ID**: 11510
**Date**: 2020-05-12
**URL**: https://discourse.slicer.org/t/trouble-with-qt-and-qtquick-not-being-properly-included-in-macos-app/11510

---

## Post #1 by @jamesjcook (2020-05-12 21:37 UTC)

<p>I’m working with a customized slicer app we branched off several years ago and I’ve got to re-establish a development environment.<br>
We’ve got a layer of qtquick on top of slicer simplifying the interface, and some custom meta-data handling code.</p>
<p>The customization is currently based on slicer nightly source from 2018-07-12.<br>
I have a mostly functional windows environment with windows server 2016, cmake 3.12.4, and visual studio 2015, and qt 5.10.1(using the official qt binaries). The mostly in this context is incomplete qt bundling when I build the package for distribution.</p>
<p>I’m now working on a mac environment.<br>
I’ve managed to get compiled, however the Qt frameworks are empty when I build the package and deploy someplace else.<br>
I’m working with mac 10.14, cmake 3.12.4, xcode 9.4.1 and qt5.10.1. I tried and failed with the latest cmake, xcode, and qt versions. I’m using make in the terminal instead of building in xcode, as I’m more familiar with linux.</p>
<p>With empty frameworks the deployed application crashes immediately. I’ve been able to hack my distribution by filling in the blanks in the bundle/Frameworks directories which will allow the application to start.<br>
Unfortunately the qtquick layer is all blank white boxes. My experience is this means invalid qml. This comes with an error in the slicer log</p>
<blockquote>
<p>qrc:/MyQMLView.qml:2:1: module “QtQuick” is not installed</p>
</blockquote>
<p>The line in question is<br>
import QtQuick 2.3</p>
<p>Commenting this line causes an “is not a type” error later in the code, after creating a Rectangle.</p>
<p>In windows I had a problem with the qtquick layer also and patched over the issue by finding the qtquick2plugin.dll file and adding the QtQuick.2 folder to the bin folder of my installation.</p>
<p>With mac I’ve tried to patch things in the same way by finding a similar file.<br>
I think QtQuick.2/libqtquick2plugin.dylib is the answer, but placing the Qtquick.2 folder in bin like I did in windows didn’t work.<br>
I’ve also tried placing QtQuick.2 in the lib/QtPlugins folder, and putting the dylib in any of the directories that should be loaded on start.</p>
<p>Can anyone shed any light on what I’m missing?  or where I should put it?</p>

---

## Post #2 by @jamesjcook (2020-05-14 16:48 UTC)

<p>Some additional steps I’ve taken,</p>
<ul>
<li>update the libqtquick2plugin.dylib using otool + install_name_tool so the pathing information looks the same as the other plugins.</li>
<li>macdeployqt with my .app dir, and the src qml folders.</li>
<li>copy the QtQuick.2 folder in bin, lib/QtPlugins, lib sub folders</li>
<li>copy only the libqtquick2plugin.dylib file into the various folders<br>
and I’ve tried a bunch of combinations of these.</li>
</ul>

---
