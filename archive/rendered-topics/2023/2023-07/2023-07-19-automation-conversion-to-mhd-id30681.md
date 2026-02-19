---
topic_id: 30681
title: "Automation Conversion To Mhd"
date: 2023-07-19
url: https://discourse.slicer.org/t/30681
---

# Automation: conversion to .mhd

**Topic ID**: 30681
**Date**: 2023-07-19
**URL**: https://discourse.slicer.org/t/automation-conversion-to-mhd/30681

---

## Post #1 by @SterArcher (2023-07-19 15:52 UTC)

<p>Hi!</p>
<p>I am using Slicer 3D daily to convert my files into .mhd.</p>
<p>Is it possible to automate this, for python script to watch folder and automatically convert anything new to .mhd file?</p>
<p>Best and thank you,</p>
<p>Luka</p>

---

## Post #2 by @pieper (2023-07-19 23:35 UTC)

<p>Yes, you should be able to do that using <a href="https://doc.qt.io/qt-5/qfilesystemwatcher.html" class="inline-onebox">QFileSystemWatcher Class | Qt Core 5.15.14</a></p>
<p>Be aware that you may need to wait until the file is fully written before you start to convert it (e.g. wait until it has stopped getting bigger for a few seconds before reading it).</p>

---

## Post #3 by @SterArcher (2023-07-23 14:16 UTC)

<p>Thank you so much for this! Will try it.</p>

---
