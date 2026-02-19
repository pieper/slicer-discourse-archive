---
topic_id: 27676
title: "Vr Headset With Macos"
date: 2023-02-07
url: https://discourse.slicer.org/t/27676
---

# VR headset with macOS

**Topic ID**: 27676
**Date**: 2023-02-07
**URL**: https://discourse.slicer.org/t/vr-headset-with-macos/27676

---

## Post #1 by @mohammed_alshakhas (2023-02-07 09:41 UTC)

<p>I’m interested in buying a VR set to use with slicer3D on mac OS.</p>
<p>if anyone would share his experience and recommendation id be very thankful<br>
thanks</p>

---

## Post #2 by @lassoan (2023-02-07 18:04 UTC)

<p>There have been rumors in the past few years that it was possible to have virtual reality on some macOS configurations with special external GPUs, some specific headsets and special software environment, but I have never seen anybody being able to make such thing work.</p>
<p>Apple will probably come up with something in this field, but if you need desktop virtual reality and don’t want to wait then practically your only option is to get a Windows computer.</p>

---

## Post #3 by @mohammed_alshakhas (2023-02-20 12:21 UTC)

<p>Is it the same issue when running windows using parallel software on Mac OS ?</p>

---

## Post #4 by @lassoan (2023-02-20 12:37 UTC)

<p>Parallels would not work, your would need to install Windows on the computer. But that would not be enough.</p>
<p>Virtual reality requires a strong gaming GPU with hdmi connector that matches the headset requirements. I don’t think any macOS computer fulfills these requirements.</p>

---

## Post #5 by @carl (2023-07-25 19:18 UTC)

<p>Old thread i know. But i wonder: What are your thoughts on apples announced visionOS headset in this regard? How difficult would it be to support it?</p>

---

## Post #6 by @lassoan (2023-07-25 20:04 UTC)

<p>All major XR companies (AMD, ARM, Epic Games, HTC, Google, Intel, Microsoft, Meta, Qualcomm, Samsung, Sony, Valve, etc.) works toward using the common OpenXR standard to allow applications, such as Slicer to display content on augmented/virtual reality headsets.</p>
<p>Unfortunately, Apple chose to use a proprietary interface. Therefore Slicer we won’t be able to directly show content on the Vision Pro headset. Maybe things will change in a few years - if VTK toolkit will add support for Vision Pro then Slicer will be able to use it, too. But it is hard to predict what will happen.</p>
<p>What you can do soon is to develop small custom viewers running on the Vision Pro using <a href="https://blog.unity.com/engine-platform/unity-support-for-visionos">Unity</a> that communicate with Slicer using OpenIGTLink - similarly to some of the <a href="https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning">apps that have been developed for the Microsoft HoloLens</a>.</p>

---
