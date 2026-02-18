# Qt single shots freezes

**Topic ID**: 19516
**Date**: 2021-09-05
**URL**: https://discourse.slicer.org/t/qt-single-shots-freezes/19516

---

## Post #1 by @Chintha_Siva_Prasad (2021-09-05 13:21 UTC)

<p>I am running a while loop with some processing in a python-script which I load with mainWindow.To stop UI from freezing, I am using qt-singleshot. Even though the UI is still freezing.</p>

---

## Post #2 by @lassoan (2021-09-05 19:42 UTC)

<p>It is possible that you can overwhelm your computer with your loop so that no much time is left for processing GUI events. Loosen up the loop a bit by calling <code>slicer.app.processEvents()</code> and/or increasing the timer’s timeout to a value that makes the application sufficiently responsive.</p>

---
