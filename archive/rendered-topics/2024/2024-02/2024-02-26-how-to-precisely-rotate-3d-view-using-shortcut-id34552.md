# How to precisely rotate 3D view using shortcut

**Topic ID**: 34552
**Date**: 2024-02-26
**URL**: https://discourse.slicer.org/t/how-to-precisely-rotate-3d-view-using-shortcut/34552

---

## Post #1 by @kdboss (2024-02-26 20:15 UTC)

<p>Hi, I’m an orthopedic trauma surgeon learning to use slicer for preoperative planning</p>
<p>I’m trying to use 3d slicer for preoperatively measure the angle for optimal c-arm imaging</p>
<p>I have learned about the code snippet that will show the rotation of 3D view from anther thread and I know the numpad 2 4 6 8 can rotate the 3d image by 15 degrees<br>
I want a more fine-tune control of the rotation and I want to change the rotation one axis at a time using the numpad, read somewhere that the key binding function is hard-coded to the program</p>
<p>Is there any way I can change the binding of numpad to rotate the 3d view by 1 degree instead of 15 degrees?</p>

---

## Post #2 by @kdboss (2024-02-27 16:41 UTC)

<p>Continuing the discussion from <a href="https://discourse.slicer.org/t/how-to-precisely-rotate-3d-view-using-shortcut/34552">How to precisely rotate 3D view using shortcut</a>:</p>
<p>After some searching around the forum, I found a way to do it making a shortcut key  i j k l for pitch up down and yaw left and right with increment 1 degree for each button press by using this code snippet in the .slicerrc.py file</p>
<p>Will leave this here for future reference and anybody who have the same problem</p>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()
threeDView = layoutManager.threeDWidget(0).threeDView()
threeDView.setPitchRollYawIncrement(1)

def step_direction(direction = 'left'):
	if direction == 'left':
		threeDView.yawDirection = threeDView.YawLeft
		threeDView.yaw()
	if direction == 'right':
		threeDView.yawDirection = threeDView.YawRight
		threeDView.yaw()
	if direction == 'up':
		threeDView.pitchDirection = threeDView.PitchUp
		threeDView.pitch()
	if direction == 'down':
		threeDView.pitchDirection = threeDView.PitchDown
		threeDView.pitch()

shortcuts = [
	("j", lambda: step_direction('left')),
	("l", lambda: step_direction('right')),
	("i", lambda: step_direction('up')),
	("k", lambda: step_direction('down'))
	]

for (shortcutKey, callback) in shortcuts:
	shortcut = qt.QShortcut(slicer.util.mainWindow())
	shortcut.setKey(qt.QKeySequence(shortcutKey))
	shortcut.connect( "activated()", callback)
</code></pre>

---
