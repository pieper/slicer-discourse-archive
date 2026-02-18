# Load image at Start

**Topic ID**: 41526
**Date**: 2025-02-06
**URL**: https://discourse.slicer.org/t/load-image-at-start/41526

---

## Post #1 by @Djonathan_Souza (2025-02-06 13:54 UTC)

<p>Hello!</p>
<p>I need to start Slicer and load an image.<br>
If I delete everything after “study_path,” the application loads the image, but I need these commands.</p>
<p>“subprocess.call([”/opt/slicer/Slicer", “–no-splash”, “–fullscreen”, study_path, “–disable-python”, “–python-script”, “start.py”])"</p>
<p>In my script, I have this:<br>
“slicer.util.loadVolume(‘path/.dicom’)”<br>
“slicer.app.settings().setValue(‘Python/DockableWindow’, False)”</p>
<p>However, if I enter the application and run the command to execute only my script with the commands,</p>
<p>“slicer.util.loadVolume(‘path/.dicom’)”<br>
“slicer.app.settings().setValue(‘Python/DockableWindow’, False)”</p>
<p>it works normally.</p>

---

## Post #2 by @pieper (2025-02-06 18:34 UTC)

<p>You probably need to wait until the application is fully initialized.  Look in the source code for places where the <code>startupCompleted()</code> signal is used and you should be able to work from there.</p>

---
