---
topic_id: 32649
title: "Adding Pitch And Roll To 3D Orientation Changing Using Pytho"
date: 2023-11-07
url: https://discourse.slicer.org/t/32649
---

# Adding Pitch and Roll to 3D orientation changing using python

**Topic ID**: 32649
**Date**: 2023-11-07
**URL**: https://discourse.slicer.org/t/adding-pitch-and-roll-to-3d-orientation-changing-using-python/32649

---

## Post #1 by @floppygator45 (2023-11-07 18:53 UTC)

<p>I am currently able to get yaw orientation manipulation working using python for the 3D view. When I try and implement Pitch or Roll the code breaks and gives an error when I try and run it in 3D slicer. The current code I have is:</p>
<pre><code class="lang-auto">import random
import slicer

# Define the number of updates and the interval in seconds
update_count = 5
update_interval = 2  # seconds

# Create a function to update the 3D view
def update_3d_view():
    if update_3d_view.counter &lt; update_count:
        yaw1 = random.uniform(-90, 90)
        threeDWidget = slicer.app.layoutManager().threeDWidget(0)
        threeDView = threeDWidget.threeDView()
        threeDView.resetFocalPoint()
        threeDView.yawDirection = threeDView.YawRight
        threeDView.setPitchRollYawIncrement(yaw1)
        threeDView.yaw()
        print(f"Yaw Rotation: {yaw1} degrees")
        update_3d_view.counter += 1
    else:
        slicer.app.processEvents()  # Ensure any pending events are processed

update_3d_view.counter = 0

# Create a timer to trigger the updates
update_timer = qt.QTimer()
update_timer.timeout.connect(update_3d_view)
update_timer.start(update_interval * 1000)
</code></pre>
<p>My updated code looks like:</p>
<pre><code class="lang-auto">def update_3d_view():
    if update_3d_view.counter &lt; update_count:
        yaw = random.uniform(-90, 90)
        pitch = random.uniform(-45, 45)  # Add pitch rotation
        threeDWidget = slicer.app.layoutManager().threeDWidget(0)
        threeDView = threeDWidget.threeDView()
        threeDView.resetFocalPoint()
        threeDView.yawDirection = threeDView.YawRight
        threeDView.setPitchRollYawIncrement(pitch, 0, yaw)  # Set pitch, roll, and yaw
        threeDView.yaw()
        print(f"Yaw Rotation: {yaw} degrees, Pitch Rotation: {pitch} degrees")
        update_3d_view.counter += 1
    else:
        slicer.app.processEvents()
</code></pre>
<p>the error I get when I add pitch to the code is:<br>
ValueError: Called setPitchRollYawIncrement(double newPitchRollYawIncrement) → void with wrong number of arguments: (-19.14680338362855, 0, 61.92372516991415)</p>
<p>It looks like its not accepting setPitchRollYawIncrement as all three just for yaw.<br>
Any help or guidance in the right direction would be appreciated</p>
<p>Thanks</p>

---
