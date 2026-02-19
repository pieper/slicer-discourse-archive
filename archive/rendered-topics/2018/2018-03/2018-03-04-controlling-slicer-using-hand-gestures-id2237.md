---
topic_id: 2237
title: "Controlling Slicer Using Hand Gestures"
date: 2018-03-04
url: https://discourse.slicer.org/t/2237
---

# Controlling Slicer using hand gestures

**Topic ID**: 2237
**Date**: 2018-03-04
**URL**: https://discourse.slicer.org/t/controlling-slicer-using-hand-gestures/2237

---

## Post #1 by @Ahmed_Soufane (2018-03-04 21:17 UTC)

<p>For the SendMessage command, the handler parameter needs to be connected to the Python interactor process. In order to get c# to send Python code to the 3d slicer, how do you get 3d slicer to act as the process and set up the interactor to act as the handler in the SendMessage method …??</p>

---

## Post #2 by @lassoan (2018-03-04 21:26 UTC)

<p>What SendMessage command do you mean? Would you like to set up socket communication between Slicer and another application? Slicer already can receive messages to update any nodes in the scene and can send updates to connected application through <a href="http://openigtlink.org/">OpenIGTLink</a> protocol.</p>
<p>If you describe what you would like to achieve (what is the background and overall goal of your project) then we can give more specific help.</p>

---

## Post #3 by @Ahmed_Soufane (2018-03-04 22:56 UTC)

<p>Hi,<br>
It’s the command that let’s you use the keyboard to type in a specified application. Ill look into the opebigtlink<br>
It’s to send Python instructions from a c# program (Kinect) to 3d slicer. I am basically interfacing kinect with 3D slicer in order to manipulate medical images by navigating them through gestures.</p>

---

## Post #4 by @Ahmed_Soufane (2018-03-04 22:57 UTC)

<p>I have been trying to send commands for 3D slicer, but for some reason it is not responding</p>

---

## Post #5 by @lassoan (2018-03-04 23:38 UTC)

<p>I would not recommend to try controlling Slicer by simulating keyboard events. It would be extremely fragile. Instead, you can send transforms through OpenIGTLink adjust camera position/orientation and slice position/orientation.</p>
<p>In the long term, I would recommend not to use Kinect, as the product is discontinued and it may stop working at any time. For short-distance interactions (for example, when sensor is fixed to the surgeon’s head, OR table side-rail, or monitor boom), then you can readily use a LeapMotion controller (see Slicer module here: <a href="https://github.com/lassoan/SlicerLeapMotionControl">https://github.com/lassoan/SlicerLeapMotionControl</a>):</p>
<div class="lazyYT" data-youtube-id="BG8udCVo1gg" data-youtube-title="Using a LeapMotion controller in 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>For Kinect-like room-scale tracking, you can use a webcam or other camera with a 2D barcode attached to the hand or tool. Marker tracking is provided by <a href="http://www.plustoolkit.org">Plus toolkit</a> and <a href="http://www.slicerigt.org/">SlicerIGT extension</a>:</p>
<div class="lazyYT" data-youtube-id="MOqh6wgOOYs" data-youtube-title="Webcam-based tracking in 3D Slicer/SlicerIGT" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>If you need markerless tracking then I would recommend Intel RealSense cameras. We don’t have readily available body model or gesture recognition, so you would need to find a solution yourself.</p>
<p>We experimented with these touchless user interfaces in the past couple of years, but our conclusion was that (at least for our intra-operative applications), the easiest to learn and richest control can be achieved by running Slicer on a touch-screen tablet, which is placed in a sterile bag. We create a custom user interface for our Slicer module, which has large buttons, which are easy to see and push through the sterile bag, while wearing gloves.</p>
<div class="lazyYT" data-youtube-id="90l0T1ADe_Y" data-youtube-title="Navigated breast conserving surgery" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque&amp;start=54"></div>

---
