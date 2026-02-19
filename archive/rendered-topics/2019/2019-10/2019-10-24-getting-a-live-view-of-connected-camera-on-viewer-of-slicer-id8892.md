---
topic_id: 8892
title: "Getting A Live View Of Connected Camera On Viewer Of Slicer"
date: 2019-10-24
url: https://discourse.slicer.org/t/8892
---

# Getting a live view of connected camera on viewer of Slicer

**Topic ID**: 8892
**Date**: 2019-10-24
**URL**: https://discourse.slicer.org/t/getting-a-live-view-of-connected-camera-on-viewer-of-slicer/8892

---

## Post #1 by @aalarcon96 (2019-10-24 20:00 UTC)

<p>Hello,</p>
<p>I am building my own loadable module for Slicer. On my module, I have placed a button (using Qt designer) that when I press it I want to see the live view of the camera connected to my computer one of the viewers of 3D Slicer. Is this possible without using OpenIGTLink?</p>
<p>Thank you in advance.</p>

---

## Post #2 by @lassoan (2019-10-24 20:14 UTC)

<p>In recent Slicer Preview Releases, you can use any Python packages. There should be packages that can acquire images from a webcam.</p>

---

## Post #3 by @aalarcon96 (2019-10-24 20:21 UTC)

<p>Hi Andras,</p>
<p>Thank you for the quick response. Is there a way to use signals and slots on the module’s source files to get the live view on the viewer? Instead of using a python package.</p>

---

## Post #4 by @lassoan (2019-10-24 21:34 UTC)

<p>How to notify availability of a new image (signals/slots, callback functions, observers, polling, etc.) is a minor implementation detail. First you need to decide what interface you would like to access your camera. Options get it from external process via OpenIGTLink, Python multimedia packages, or Qt multimedia package. There are so many options that without knowing more about your application and constraints, it is hard to give more specific advice.</p>

---

## Post #5 by @aalarcon96 (2019-10-25 13:44 UTC)

<p>Hi Andras,</p>
<p>So basically I have a realsense RGB-D camera and I want to visualize it on 3D slicer. Eventually I will add more features to the module but this is my starting point. I built Slicer 4.11.0, created a loadable module, designed the GUI on Qt designer, and now am trying to have logic behind the GUI. For our application, OpenIGTLink is going to end up being too slow and from what I have read online most of the people using RealSense cameras and 3D Slicer use OpenIGTLink so I did not know if there were other ways. This is my first time creating a module for Slicer so I am still learning. Are there any specific things you need to know in order to point me in the right direction?</p>
<p>Thanks!</p>

---

## Post #6 by @lassoan (2019-10-25 14:13 UTC)

<p>We use Intel RealSense camera connected to Plus toolkit, connected to 3D Slicer via OpenIGTLink. We can send over all data (RGB image, D image) and/or do data processing in Plus and send the results (tracked object positions, etc.) to Slicer.</p>
<p>If you want to do data acquisition and processing in the same process as your GUI then the programming gets much more complicated, so I would suggest to follow current approach and do these concurrent low-level tasks in another process.</p>

---
