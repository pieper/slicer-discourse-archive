---
topic_id: 34463
title: "Stop Python Script Without Causing 3D Slicer To Close"
date: 2024-02-22
url: https://discourse.slicer.org/t/34463
---

# Stop python script without causing 3D Slicer to close

**Topic ID**: 34463
**Date**: 2024-02-22
**URL**: https://discourse.slicer.org/t/stop-python-script-without-causing-3d-slicer-to-close/34463

---

## Post #1 by @Teresa_Marotta (2024-02-22 03:21 UTC)

<p>Is there a way to stop a python script from running in the Python Console without closing 3D Slicer? I’m running a script to populate data into a table and I want to stop the script and export the data to a csv file. I tried using sys.exit() but this causes the application to close. Any help with this is greatly appreciated!</p>

---

## Post #2 by @lassoan (2024-02-22 03:27 UTC)

<p><code>sys.exit()</code> terminates the current process, so if you run the script in the Slicer process then it will quit Slicer. If you don’t want to quit Slicer then you can put your code in a function and call <code>return</code> to quit from it at any point. You can also allow the user to cancel the processing by hitting a button; for this you just need to call <code>slicer.app.processEvents()</code> time to time in your processing code to allow the application to process GUI events.</p>

---
