# Strategies to link Slicer 3D with a navigation system

**Topic ID**: 1721
**Date**: 2017-12-26
**URL**: https://discourse.slicer.org/t/strategies-to-link-slicer-3d-with-a-navigation-system/1721

---

## Post #1 by @terajnol (2017-12-26 08:31 UTC)

<p>Operating system: Win 10, 64bits<br>
Slicer version: 4.9</p>
<p>Hi everyone,<br>
I possess an inertial unit system (from Xsens company) to track motion (especially rotation angles) of a device and I would like to connect it to Slicer to simulate a navigation system.</p>
<p>My idea is to use SlicerIGT extension to correctly handle this navigation system. But it is difficult for me to correctly understand how to make SlicerIGT listening to my inertial unit. I could use PLUS toolkit but my device is not part of the supported devices (I am right now trying to explore more PLUS). Alongside my inertial unit, I have a C/C++ SDK to get real-time data from my device. Do you have any general idea on how to connect this SDK to Slicer, or if PLUS toolkit allows connection with “not supported” devices ?</p>
<p>Thank you for your help,</p>

---

## Post #2 by @terajnol (2017-12-26 09:49 UTC)

<p>Since the C++ SDK to get data from my inertial unit is fairly easy to use, another solution would be to call from my Python module a C++ object or program. What do you think about this other solution ? In this case, what would be the procedure to communicate between a C++ program and my Python module ?</p>

---

## Post #3 by @leochan2009 (2017-12-26 14:36 UTC)

<p>Hi Tera,</p>
<p>As OpenIGTLink library (a C/C++ library for socket communication) is used in SlicerIGT to communicate with Slicer, my suggestion is to write a c++ program which gets the data from the inertial unit SDK and transmit the data via openigtlink library. In Slicer, a module called OpenIGTLinkIF could receive the data  and convert the data to either volume or transformation nodes.<br>
here are some links for your reference:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/OpenIGTLinkIF" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/OpenIGTLinkIF</a><br>
<a href="http://openigtlink.org/" class="onebox" target="_blank" rel="nofollow noopener">http://openigtlink.org/</a></p>
<p>Regarding your solution, we are developing a SWIG-wrapped python library to wrap the openigtlink library. In the future you will be able to call from your python module</p>
<p>Best,<br>
Longquan</p>

---

## Post #4 by @lassoan (2017-12-26 14:49 UTC)

<p>Which Xsens device do you have?</p>
<p><a href="https://www.plustoolkit.org">Plus toolkit</a> can already connect to a number of low-cost IMUs (PhidgetSpatial, Microchip, CHRobotics) and send live tracking data through OpenIGTLink to Slicer. You can use any of these interface classes as examples or modify them to connect to your device. If you have any questions about how to do this, <a href="https://github.com/PlusToolkit/PlusLib/issues/new">post an issue at Plus github page</a>.</p>

---

## Post #5 by @terajnol (2017-12-26 15:04 UTC)

<p>Thank you for your answers.<br>
It is the first time I am working on communication between such software and hardware and I was a bit lost.<br>
I was starting to consider OpenIGT as the only good option to my problem.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I have a Xsens MTw Awinda motion tracker. I will try to use the examples of Plus toolkit to make it work. And I will post on the github page if I have any trouble.<br>
Anyway, if this doesn’t work, I will directly use the OpenIGTLink library in my C++ program as <a class="mention" href="/u/leochan2009">@leochan2009</a> suggested.</p>

---

## Post #6 by @leochan2009 (2017-12-26 15:29 UTC)

<p>Hi Tera,</p>
<p>Yes, the short term solution is to use OpenIGTLink directly. I think Andras’s suggestion is a long term and better solution. It would be helpful for the community to have more device supported.<br>
Don’t hesitate to ask any questions.</p>
<p>Best and Good Luck!</p>
<p>Longquan</p>

---
