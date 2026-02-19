---
topic_id: 32648
title: "Real Time Orientation Changing Through Python"
date: 2023-11-07
url: https://discourse.slicer.org/t/32648
---

# Real Time Orientation Changing Through Python

**Topic ID**: 32648
**Date**: 2023-11-07
**URL**: https://discourse.slicer.org/t/real-time-orientation-changing-through-python/32648

---

## Post #1 by @floppygator45 (2023-11-07 18:25 UTC)

<p>Relatively new to 3D slicer. I have been looking at the reference guide that 3dslicer provided and found 3D object orientation can be changed through python. Currently this is the code I have where it prints a random yaw value and sends it to 3D slicer to change the orientation. The issue is that the orienation does not update but waits for the “while” loop to complete before updating the yaw orientation in 3D slicer. I would like to see the 3D object updated for each new yaw value if that is possible. Here is my code for reference. Any help would be appreciated.</p>
<pre><code class="lang-auto">import random
from time import sleep
count = 0
while True:
    yaw1 = random.randrange(90)
    layoutManager = slicer.app.layoutManager()
    threeDWidget = layoutManager.threeDWidget(0)
    threeDView = threeDWidget.threeDView()
    threeDView.yawDirection = threeDView.YawRight
    threeDView.setPitchRollYawIncrement(yaw1)
    threeDView.yaw()
    sleep(2)
    print(yaw1)
    count += 1
    if count &gt;= 5:
        break
</code></pre>

---

## Post #2 by @mau_igna_06 (2023-11-07 18:35 UTC)

<p>Maybe you are looking for something like this inside your for loop:</p>
<pre><code class="lang-auto">threeDView.setPitchRollYawIncrement(yaw1)
threeDView.yaw()
slicer.app.processEvents() # let's updates on the slicer scene happen
</code></pre>
<p>Hope it helps</p>

---

## Post #3 by @pieper (2023-11-07 21:46 UTC)

<p>In addition to Mauro’s suggestion, I’d add that you shouldn’t use <code>sleep</code> in your Slicer python code.  Instead you should use <a href="https://doc.qt.io/qt-5/qtimer.html"><code>qt.QTimer</code></a> related functions with callbacks so that your code integrates cleanly with the event loop like <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/Endoscopy/Endoscopy.py#L64-L66">this example</a>.</p>

---
