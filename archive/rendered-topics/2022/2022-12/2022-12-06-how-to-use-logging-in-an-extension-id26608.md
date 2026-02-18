# How to use logging in an extension?

**Topic ID**: 26608
**Date**: 2022-12-06
**URL**: https://discourse.slicer.org/t/how-to-use-logging-in-an-extension/26608

---

## Post #1 by @Guillaumeee (2022-12-06 16:30 UTC)

<p>Hello, I need to manipulate log files via my 3d slicer extension.</p>
<p>I tried with the logging library (without success).<br>
Example:</p>
<pre><code class="lang-auto">import logging

logging.basicConfig(
    filename=r'D:\FEALINX\Extension_Pack\compare_segment\segment\logs\Compare_Segment.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(process)d--%(asctime)s-%(levelname)s-%(message)s'
)

logging.info('This is a warning.')
</code></pre>
<p>Do you have any information that could help me?</p>
<p>Thanks a lot for your help !</p>

---

## Post #2 by @lassoan (2022-12-06 16:42 UTC)

<p>A default Python logger is already configured allows you to see all kinds of errors (coming from Python, VTK, ITK, Qt, CTK, etc.) at one place, giving you a clear picture of what is happening in the application. In Slicer-5.2 and later these logs also appear in the Python console (you can adjust the Python console log level in application settings / Python). If you change the default logger configuration then you might make some Python logs not show up in the application log, which may make user support/troubleshooting a bit more difficult.</p>
<p>For debugging on your own computer, I would highly recommend using a Python debugger instead of relying on logging - see setup instructions <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/python.html">here</a>.</p>
<p>Overall, we rarely see a need for custom Python logging, but if you find that you need it anyway then you should be able to set it up. You can see how to make the logs show up in various places (Python console, application log, etc.) <a href="https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/slicerqt.py">here</a>, where the default Python logger is set up.</p>

---
