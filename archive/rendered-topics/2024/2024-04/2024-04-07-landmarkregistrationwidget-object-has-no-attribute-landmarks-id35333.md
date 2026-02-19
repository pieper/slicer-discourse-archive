---
topic_id: 35333
title: "Landmarkregistrationwidget Object Has No Attribute Landmarks"
date: 2024-04-07
url: https://discourse.slicer.org/t/35333
---

# 'LandmarkRegistrationWidget' object has no attribute 'landmarksWidget'

**Topic ID**: 35333
**Date**: 2024-04-07
**URL**: https://discourse.slicer.org/t/landmarkregistrationwidget-object-has-no-attribute-landmarkswidget/35333

---

## Post #1 by @chaowang (2024-04-07 13:12 UTC)

<p>Problem report for Slicer 5.6.2 win-amd64: [please describe expected and actual behavior]<br>
‘LandmarkRegistrationWidget’ object has no attribute ‘landmarksWidget’<br>
[CRITICAL][FD] 07.04.2024 18:00:56 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile<br>
[CRITICAL][FD] 07.04.2024 18:00:56 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile<br>
[CRITICAL][Stream] 07.04.2024 18:02:00 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 07.04.2024 18:02:00 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\chao.wang\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\ScriptedLoadableModule.py”, line 263, in onReloadAndTest<br>
[CRITICAL][Stream] 07.04.2024 18:02:00 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     self.onReload()<br>
[CRITICAL][Stream] 07.04.2024 18:02:00 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Users/chao.wang/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/LandmarkRegistration.py”, line 650, in onReload<br>
[CRITICAL][Stream] 07.04.2024 18:02:00 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     slicer.util.reloadScriptedModule(“LandmarkRegistration”)<br>
[CRITICAL][Stream] 07.04.2024 18:02:00 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\chao.wang\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 1405, in reloadScriptedModule<br>
[CRITICAL][Stream] 07.04.2024 18:02:00 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     widget.cleanup()<br>
[CRITICAL][Stream] 07.04.2024 18:02:00 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Users/chao.wang/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/LandmarkRegistration.py”, line 304, in cleanup<br>
[CRITICAL][Stream] 07.04.2024 18:02:00 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     self.landmarksWidget.removeLandmarkObservers()<br>
[CRITICAL][Stream] 07.04.2024 18:02:00 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - AttributeError: ‘LandmarkRegistrationWidget’ object has no attribute ‘landmarksWidget’</p>

---

## Post #2 by @mxtt (2025-01-06 17:58 UTC)

<p>I just went into the code and added these three lines into the <strong>init</strong> function for the widget:</p>
<p>self.landmarksWidget = RegistrationLib.LandmarksWidget(self.logic)<br>
self.interfaceFrame = qt.QWidget(self.parent)<br>
self.volumeSelectors = {}</p>
<p>It’s what said was missing and so I put it into <strong>init</strong>. Not sure if there will be other issues but it seems like this could be a quick fix. I read elsewhere that you can use 4.8.1 or 4.11.</p>

---

## Post #3 by @mxtt (2025-01-06 19:02 UTC)

<p>Comment out this too on line ~73:</p>
<h1><a name="p-121056-selfreloadandtestbuttontooltip-reload-this-module-and-then-run-the-s-self-test-scenario-1" class="anchor" href="#p-121056-selfreloadandtestbuttontooltip-reload-this-module-and-then-run-the-s-self-test-scenario-1" aria-label="Heading link"></a>self.reloadAndTestButton.toolTip = “Reload this module and then run the %s self test.” % scenario</h1>
<p>Probably wont be able to use test functionality - not sure did not try</p>

---
