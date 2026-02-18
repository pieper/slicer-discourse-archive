# window display problem

**Topic ID**: 24927
**Date**: 2022-08-25
**URL**: https://discourse.slicer.org/t/window-display-problem/24927

---

## Post #1 by @yang (2022-08-25 20:29 UTC)

<p>Operating system: win10<br>
Slicer version: 4.11</p>
<p>Expected behavior:<br>
I opened the main window of the slicer in full screen, but when I clicked the button, the pop-up dialog was displayed behind the main window. I thought it was a problem with my own code, I created a small demo, simulated it with the same code, clicked the button and the popup appeared above the main window. So far, my code is fine, but I can’t figure out why.</p>
<p>void qSlicerMainWindowPrivate::init()<br>
{<br>
Q_Q(qSlicerMainWindow);<br>
this-&gt;setupUi(q);</p>
<p>q-&gt;setWindowFlags(Qt::FramelessWindowHint);<br>
q-&gt;setFixedSize(QSize(1920, 1080));</p>
<p>//this-&gt;setupStatusBar();<br>
//q-&gt;setupMenuActions();<br>
//this-&gt;StartupState = q-&gt;saveState();<br>
//this-&gt;readSettings();<br>
}</p>
<p>Actual behavior:<br>
Click the button, a dialog box will pop up on the main window</p>

---
