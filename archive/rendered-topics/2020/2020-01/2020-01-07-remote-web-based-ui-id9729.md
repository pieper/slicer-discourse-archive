---
topic_id: 9729
title: "Remote Web Based Ui"
date: 2020-01-07
url: https://discourse.slicer.org/t/9729
---

# Remote web based UI

**Topic ID**: 9729
**Date**: 2020-01-07
**URL**: https://discourse.slicer.org/t/remote-web-based-ui/9729

---

## Post #1 by @burnhamd (2020-01-07 20:51 UTC)

<p>This is kind of a far fetched question, but I was wondering if anyone has done work on seperating the UI layer of slicer.</p>
<p>My end goal is to have slicer running on a computer, but also have remote web based UI built similarly to webvtk.  I know I can do the entire slicer interface using VNC, but in my case I want different UIs for different people.</p>
<p>My thought is to write a module which exports the MRML node list and subscribes to the events then either use vtk.js on the other side or render locally with something like webvtk and serve it up.</p>

---

## Post #2 by @lassoan (2020-01-07 21:21 UTC)

<p>Offering different UIs for different people is really easy (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets">slicelets</a>), so this would certainly not justify redeveloping the entire Slicer UI from scratch in any framework. However, it is a common user request to be able to run Slicer in a web browser for other reasons - people don’t like the commitment of installing a desktop application, or system administrators don’t want to manage applications on desktop computers, etc.</p>
<p>There are good solutions for accessing patient list and basic 2D/3D visualization in web browser (see <a href="https://github.com/OHIF/Viewers">OHIF viewer</a>). Our current plan is to integrate advanced Slicer features (Segment Editor, visualization of huge data sets, etc.) into web viewers by allowing launching a Slicer instance on a cloud server transparently (by click of a button on the web GUI) on the selected data set, allow interacting with Slicer GUI in the same webpage (this Slicer GUI can be an arbitrarily customized, simplified GUI, with design theme matching the web application’s), and upload results to the web application’s database. We will work on this OHIF/Slicer bridge at the <a href="https://projectweek.na-mic.org/PW33_2020_GranCanaria/">upcoming project week</a>.</p>
<p>Running Slicer as a backend and communicate with a web application via web services would be a potential option, too. There have been attempts, for example see <a href="https://github.com/pieper/SlicerWeb">here</a>. This approach may make sense for selected applications, but in general it is not very appealing, as it combines disadvantages of desktop and web applications (high workload of redeveloping sophisticated GUI and dependency on significant server resources).</p>

---
