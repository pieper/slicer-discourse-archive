---
topic_id: 3146
title: "Openigtlink Drag And Drop Trackerserver"
date: 2018-06-12
url: https://discourse.slicer.org/t/3146
---

# OpenIGTLink drag and drop TrackerServer

**Topic ID**: 3146
**Date**: 2018-06-12
**URL**: https://discourse.slicer.org/t/openigtlink-drag-and-drop-trackerserver/3146

---

## Post #1 by @katharina_hecker (2018-06-12 06:44 UTC)

<p>Hi,<br>
I´m trying to use the Module: OpenIGTLink to get matrices from Matlab into 3D Slicer(4.8.1). Now I have downloaded therefore the Slicer Extensions and the zip folder for windows (64-bit). When I want to drag and drop the TrackerServer into the cmd window nothing happens. It is not taken in. (by the way if it´s important: When I just try to open TrackerServer itself, in a millisecond a window appears and closes again)<br>
Can anyone give me recommendations how to solve this problem? It is really important for me and I can use any help.<br>
Thank you very much!</p>

---

## Post #2 by @wpgao (2018-06-12 09:50 UTC)

<p>You should set the parameters (i.e., server IP and port) to the TrackerServer!</p>

---

## Post #3 by @katharina_hecker (2018-06-12 09:51 UTC)

<p>ok and sorry to ask: how can i do this?</p>

---

## Post #4 by @wpgao (2018-06-12 11:17 UTC)

<p>In the cmd console, you Can input the command “path/TrackerServer localhost 18947 20”</p>

---

## Post #5 by @katharina_hecker (2018-06-12 19:32 UTC)

<p>thank you now it’s working</p>

---
