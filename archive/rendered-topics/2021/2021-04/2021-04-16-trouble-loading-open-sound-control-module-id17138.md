# Trouble loading Open Sound Control Module

**Topic ID**: 17138
**Date**: 2021-04-16
**URL**: https://discourse.slicer.org/t/trouble-loading-open-sound-control-module/17138

---

## Post #1 by @smallvalthoss (2021-04-16 19:13 UTC)

<p>Here is the error I get whenever loading the open sound control module. Any help is appreciated.</p>
<pre><code>Traceback (most recent call last):
  File "C:/Users/Madhavi/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SoundControl/lib/Slicer-4.11/qt-scripted-modules/OpenSoundControl.py", line 43, in __init__
	self.logic = OpenSoundControlLogic()
  File "C:/Users/Madhavi/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SoundControl/lib/Slicer-4.11/qt-scripted-modules/OpenSoundControl.py", line 178, in __init__
	self.oscClient = OSC.OSCClient()
AttributeError: module 'OSC' has no attribute 'OSCClient'</code></pre>

---
