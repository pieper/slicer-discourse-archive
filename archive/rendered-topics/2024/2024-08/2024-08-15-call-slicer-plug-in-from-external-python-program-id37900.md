---
topic_id: 37900
title: "Call Slicer Plug In From External Python Program"
date: 2024-08-15
url: https://discourse.slicer.org/t/37900
---

# Call Slicer plug-in from external python program

**Topic ID**: 37900
**Date**: 2024-08-15
**URL**: https://discourse.slicer.org/t/call-slicer-plug-in-from-external-python-program/37900

---

## Post #1 by @ning_w (2024-08-15 09:58 UTC)

<p>I am trying to do secondary development based on 3D slicer, using Python language, and now I have encountered a problem, and I am here to ask for your help. I want to use the plug-in OpenIGTLink that calls slcier externally, can I achieve this function? Or can I install this plug-in into my secondary development software? Can you give me some suggestions or ideas?</p>

---

## Post #2 by @lassoan (2024-08-15 12:32 UTC)

<p>You can use <a href="https://pypi.org/project/pyigtl/">pyigtl</a> Python package to send/receive data to/from 3D Slicer in any Python environment via OpenIGTL protocol.</p>

---

## Post #3 by @ning_w (2024-08-16 09:24 UTC)

<p>Thank you very much for your answer, but I want to call this plugin now, is there any way? Use Python language, or can this plugin be installed on the software I developed?</p>

---

## Post #4 by @lassoan (2024-08-16 10:47 UTC)

<p>If your program is in Python then you can use pyigtl, if in C/C++ then you can use <a href="https://github.com/openigtlink/OpenIGTLink" class="inline-onebox">GitHub - openigtlink/OpenIGTLink: Free, open-source network communication library for image-guided therapy</a></p>

---

## Post #5 by @ning_w (2024-08-16 09:20 UTC)

<p>I am trying to do secondary development based on slicer, and I have made a new software using Python. Now I have a problem: how to install the slicer plug-in: OpenIGTLink in my software? Or how to use Python code in the compiler pycharm to call this plug-in? Please help me, as a beginner, I really need help.</p>

---

## Post #6 by @lassoan (2024-08-16 10:51 UTC)

<p>You can only use Slicer extensions in the Slicer application. You can use OpenIGTLink library or pyigtl in your software to communicate with Slicer.</p>

---

## Post #7 by @ning_w (2024-08-19 01:42 UTC)

<p>Thank you very much. According to your guidance, I have connected to the data sent by plus server in my python code, using pyigtl, and got: message = client.wait_for_message(“ToolToReference”, timeout=5). How can I use this probe model to connect to my NDI? Later, I also want to use the registration plug-in: Fiducial Registration Wizard. How can I implement this function in my python code? Please help me, I really want to learn. Thank you again.</p>

---

## Post #8 by @lassoan (2024-08-19 07:25 UTC)

<p>If you want to call Slicer functions you can use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html#slicer-endpoints"><code>/slicer</code> endpoint</a> in the REST API of Slicer. You can simply plain Python <code>requests</code> to run Python commands the same way as you would run them in the Python console of Slicer.</p>
<p>For your convenience, you canuse slicerio package to start the Slicer application (<a href="https://github.com/lassoan/slicerio/blob/0566bf6616cd561d24a64225523f005f7c3c90ee/slicerio/server.py#L10"><code>slicerio.server.start_server</code></a>).</p>

---
