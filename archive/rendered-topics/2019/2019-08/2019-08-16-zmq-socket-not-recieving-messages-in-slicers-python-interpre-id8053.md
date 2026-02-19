---
topic_id: 8053
title: "Zmq Socket Not Recieving Messages In Slicers Python Interpre"
date: 2019-08-16
url: https://discourse.slicer.org/t/8053
---

# ZMQ socket not recieving messages in Slicer's python interpreter

**Topic ID**: 8053
**Date**: 2019-08-16
**URL**: https://discourse.slicer.org/t/zmq-socket-not-recieving-messages-in-slicers-python-interpreter/8053

---

## Post #1 by @fergujm2 (2019-08-16 03:10 UTC)

<p>Hi,</p>
<p>We have a small data acquisition script that we are trying to run in Slicer’s python interpreter.  Currently, we create a connection to our device and request a data stream from the device at a certain frequency.  Then we create a subscriber that receives the requested messages on a separate Python thread.  This is all done using the ZMQ python socket library (we had to pip_install(‘zmq’) for this) to manage the TCP connections to our device.</p>
<p>We have verified that this communication is working when using a standard Python3 interpreter via the command line.  We have also verified that it works when invoking the SlicerPython interpreter via the command line. When using it in Slicer, we have verified that the request to stream data has been received by our device.  However, we have not been able to receive the requested data messages in Slicer.  We also turned off the Windows Firewall and made new outbound and inbound connection rules to allow connections for Slicer, SlicerApp-Real, SlicerPython, PythonSlicer, and Python-Real, but none of this worked.</p>
<p>We know we should probably be using Plus for our communication, but we only have a Python API for our device currently.</p>
<p>Thanks,</p>
<p>James and Bryn</p>

---

## Post #2 by @lassoan (2019-08-16 05:07 UTC)

<p><a href="https://github.com/Slicer/SlicerJupyter" rel="nofollow noopener">SlicerJupyter</a> extension uses ZeroMQ (C++ implementation) to communicate with the Jupyter notebook backend. You may use the same approach. The tricky part is how to poll the message queue and retrieve messages without completely blocking the main thread.</p>
<p>Another option is to send messages from Python via OpenIGTLink using <a href="https://github.com/SlicerIGT/pyIGTLink" rel="nofollow noopener">pyIGTLink</a>.</p>

---
