---
topic_id: 16351
title: "How To Access Slicers Python Api Via An External Program Whi"
date: 2021-03-04
url: https://discourse.slicer.org/t/16351
---

# How to access Slicers Python API via an external program while slicer is running?

**Topic ID**: 16351
**Date**: 2021-03-04
**URL**: https://discourse.slicer.org/t/how-to-access-slicers-python-api-via-an-external-program-while-slicer-is-running/16351

---

## Post #1 by @fuadamaschin (2021-03-04 08:31 UTC)

<p>As far as I’ve understood this there are 2 main ways to access Slicers Python API:</p>
<ul>
<li>Using the built-in python console</li>
<li>Starting slicer with the <code>--python-script</code> or <code>--python-code</code> flag</li>
</ul>
<p>But I want to have an external program running on the same machine as slicer. This program should then be able to control the running slicer instance via Slicers Python API.</p>
<p>Is this possible?</p>
<p>I would be grateful if you could point me to some ressources.</p>

---

## Post #2 by @lassoan (2021-03-04 14:45 UTC)

<p>There are many ways to achieve this, depending on what you would like to achieve and what your programming environment is. A few examples:</p>
<ul>
<li>
<a href="https://github.com/pieper/SlicerWeb">SlicerWeb</a>: expose Slicer’s Python environment as a web service. Well suited for applications that already use web requests.</li>
<li>
<a href="https://github.com/openigtlink/SlicerOpenIGTLink">SlicerOpenIGTLink</a>: very lightweight socket-based protocol for real-time data transfer. Well suited for applications where you need to send dozens or hundreds of requests per second (e.g., continuous data streaming); or for clients that only have access to sockets and do not want to reimplement complex protocols, such as http. There is a native Python implementation: <a href="https://pypi.org/project/pyigtl/">pyigtl</a>.</li>
<li>
<a href="https://github.com/Slicer/SlicerJupyter">SlicerJupyter</a>: protocol for interacting with Slicer using standard Jupyter kernel protocol (quite simple protocol, but built on top of ZeroMQ middleware). Useful for applications that want to offer embedded Python console to Slicer and don’t want to implement a Slicer-specific protocol.</li>
</ul>

---

## Post #3 by @fuadamaschin (2021-03-08 08:09 UTC)

<p>Thanks a lot Andras, these are very helpful pointers, they should fit my use case quite well.</p>

---

## Post #5 by @Pedro_Vitor_Abreu (2021-04-27 16:15 UTC)

<p>Hey Paul,</p>
<p>Did you followed any of these solutions? It worked?</p>
<p>I’m facing a similar situation where I’m trying to establish a connection between Slicer and a Django server.</p>
<p>thanks!<br>
Pedro</p>

---
