---
topic_id: 43536
title: "Error Loading Slicermorphrc Py"
date: 2025-06-29
url: https://discourse.slicer.org/t/43536
---

# Error loading SlicerMorphRC.py

**Topic ID**: 43536
**Date**: 2025-06-29
**URL**: https://discourse.slicer.org/t/error-loading-slicermorphrc-py/43536

---

## Post #1 by @AriD (2025-06-29 07:40 UTC)

<p>Hello,<br>
I’m using 3D Slicer version 5.8.1 and have been working with the SlicerMorph extension for some time. Recently, I started receiving the following error:<br>
“error loading SlicerMorphRC.py<br>
module ‘slicer’ has no attribute ‘vtkMRMLVolumePropertyNode’<br>
see Python console for stack trace”</p>
<p>I have tried the following steps without success:</p>
<ul>
<li>Uninstalling and reinstalling the SlicerMorph extension</li>
<li>Uninstalling and reinstalling 3D Slicer itself</li>
</ul>
<p>I would appreciate any help resolving this issue.</p>
<p>Thank you!</p>

---

## Post #2 by @muratmaga (2025-06-29 18:12 UTC)

<p>I can’t replicate this on my Mac. When I enable SlicerMorphRC.py, there is no error. What platform are you seeing this, and did you make any changes to the resource file (like editing and deleting things).</p>
<p>Also, if you can copy and paste the python console as the error suggest, it might be useful.</p>

---

## Post #3 by @AriD (2025-06-30 07:33 UTC)

<p>Hello,<br>
Thank you for your quick response.<br>
I don’t know if this is related, but this started happening after installing <strong>SlicerIGT</strong> extension, and I have tried deleting and reinstalling this as well - but no change.<br>
The following is the python script when I open slicer:</p>
<p>Python 3.9.10 (main, Mar 2 2025, 20:55:00) [MSC v.1942 64 bit (AMD64)] on win32</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\BEM-LAB-PC\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\imp.py”, line 169, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 613, in _exec<br>
File “”, line 850, in exec_module<br>
File “”, line 228, in <em>call_with_frames_removed<br>
File “C:/Users/BEM-LAB-PC/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/Sandbox/lib/Slicer-5.8/qt-scripted-modules/ColorizeVolume.py”, line 16, in <br>
from slicer import vtkMRMLScalarVolumeNode, vtkMRMLSegmentationNode, vtkMRMLSequenceBrowserNode, vtkMRMLVectorVolumeNode<br>
ImportError: cannot import name ‘vtkMRMLSequenceBrowserNode’ from ‘slicer’ (C:\Users\BEM-LAB-PC\AppData\Local\slicer.org\Slicer 5.8.1\bin\Python\slicer_<em>init</em></em>.py)<br>
[Qt] loadSourceAsModule - Failed to load file “C:/Users/BEM-LAB-PC/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/Sandbox/lib/Slicer-5.8/qt-scripted-modules/ColorizeVolume.py” as module “ColorizeVolume” !<br>
[Qt] Fail to instantiate module “ColorizeVolume”<br>
[Qt] libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
[Qt] The following modules failed to be instantiated:<br>
[Qt] ColorizeVolume<br>
Traceback (most recent call last):<br>
File “C:/Users/BEM-LAB-PC/AppData/Local/slicer.org/Slicer 5.8.1/bin/../lib/Slicer-5.8/qt-scripted-modules/DataProbe.py”, line 60, in addView<br>
self.infoWidget = DataProbeInfoWidget(parent)<br>
File “C:/Users/BEM-LAB-PC/AppData/Local/slicer.org/Slicer 5.8.1/bin/../lib/Slicer-5.8/qt-scripted-modules/DataProbe.py”, line 98, in <strong>init</strong><br>
self._createSmall()<br>
File “C:/Users/BEM-LAB-PC/AppData/Local/slicer.org/Slicer 5.8.1/bin/../lib/Slicer-5.8/qt-scripted-modules/DataProbe.py”, line 406, in _createSmall<br>
self.sliceAnnotations = DataProbeLib.SliceAnnotations()<br>
File “C:\Users\BEM-LAB-PC\AppData\Local\slicer.org\Slicer 5.8.1\lib\Slicer-5.8\qt-scripted-modules\DataProbeLib\SliceViewAnnotations.py”, line 109, in <strong>init</strong><br>
self.parameterNode = self.dataProbeUtil.getParameterNode()<br>
File “C:\Users\BEM-LAB-PC\AppData\Local\slicer.org\Slicer 5.8.1\lib\Slicer-5.8\qt-scripted-modules\DataProbeLib\DataProbeUtil.py”, line 24, in getParameterNode<br>
node = self._createParameterNode()<br>
File “C:\Users\BEM-LAB-PC\AppData\Local\slicer.org\Slicer 5.8.1\lib\Slicer-5.8\qt-scripted-modules\DataProbeLib\DataProbeUtil.py”, line 45, in _createParameterNode<br>
slicer.mrmlScene.AddNode(node)<br>
TypeError: AddNode argument 1: method requires a VTK object<br>
Traceback (most recent call last):<br>
File “C:/Users/BEM-LAB-PC/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/MorphPreferences.py”, line 62, in loadPresetFile<br>
exec(open(vrPresetPath).read(), globals())<br>
File “”, line 11, in <br>
AttributeError: module ‘slicer’ has no attribute ‘vtkMRMLVolumePropertyNode’<br>
[Python] Error loading SlicerMorphRC.py<br>
[Python] module ‘slicer’ has no attribute ‘vtkMRMLVolumePropertyNode’<br>
[Python] See Python Console for Stack Trace<br>
Traceback (most recent call last):<br>
File “C:/Users/BEM-LAB-PC/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/Sandbox/lib/Slicer-5.8/qt-scripted-modules/UserStatistics.py”, line 66, in setup<br>
self.logic = UserStatisticsLogic()<br>
File “C:/Users/BEM-LAB-PC/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/Sandbox/lib/Slicer-5.8/qt-scripted-modules/UserStatistics.py”, line 271, in <strong>init</strong><br>
self.addObserver(slicer.mrmlScene, slicer.mrmlScene.NodeAddedEvent, self.onNodeAdded)<br>
File “C:\Users\BEM-LAB-PC\AppData\Local\slicer.org\Slicer 5.8.1\bin\Python\slicer\util.py”, line 2822, in addObserver<br>
tag = obj.AddObserver(event, method, priority)<br>
AttributeError: ‘MRMLCorePython.vtkMRMLScene’ object has no attribute ‘AddObserver’<br>
Traceback (most recent call last):<br>
File “C:/Users/BEM-LAB-PC/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/Sandbox/lib/Slicer-5.8/qt-scripted-modules/UserStatistics.py”, line 42, in showUserConfirmationDialog<br>
logic = slicer.modules.userstatistics.widgetRepresentation().self().logic<br>
AttributeError: ‘UserStatisticsWidget’ object has no attribute ‘logic’<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
[Qt] Property ‘verbose’’ of object ‘qSlicerWebPythonProxy’ has no notify signal and is not constant, value updates in HTML will be broken!<br>
[Qt] Property ‘verbose’’ of object ‘qSlicerWebPythonProxy’ has no notify signal and is not constant, value updates in HTML will be broken!<br>
[Qt] Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/33241/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png</a>’. This content should also be served over HTTPS.<br>
[Qt] A cookie associated with a cross-site resource at <a href="http://www.nitrc.org/" rel="noopener nofollow ugc">http://www.nitrc.org/</a> was set without the <code>SameSite</code> attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with <code>SameSite=None</code> and <code>Secure</code>. You can review cookies in developer tools under Application&gt;Storage&gt;Cookies and see more details at <a href="https://www.chromestatus.com/feature/5088147346030592" class="inline-onebox" rel="noopener nofollow ugc">Chrome Platform Status</a> and <a href="https://www.chromestatus.com/feature/5633521622188032" class="inline-onebox" rel="noopener nofollow ugc">Chrome Platform Status</a>.<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
[Qt] Property ‘verbose’’ of object ‘qSlicerWebPythonProxy’ has no notify signal and is not constant, value updates in HTML will be broken!<br>
[Qt] Property ‘verbose’’ of object ‘qSlicerWebPythonProxy’ has no notify signal and is not constant, value updates in HTML will be broken!</p>

---
