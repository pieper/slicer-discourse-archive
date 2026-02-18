# Progressbar in 3D Slicer python script - how can I make it stay in foreground?

**Topic ID**: 18280
**Date**: 2021-06-22
**URL**: https://discourse.slicer.org/t/progressbar-in-3d-slicer-python-script-how-can-i-make-it-stay-in-foreground/18280

---

## Post #1 by @rbumm (2021-06-22 18:58 UTC)

<p>Hi,</p>
<p>How can I make the progressbar created like this</p>
<pre><code>    progressbar = slicer.util.createProgressDialog(windowTitle='Processing...', autoClose=False)
    progressbar.setCancelButton(None)
    progress =0
    steps = 7
    progressStep = 100/steps       
    # Update progress value
    progressbar.setValue(progress)
    progress += progressStep
    # Update label text
    progressbar.labelText = "Starting processing ..."
    slicer.app.processEvents()
</code></pre>
<p>. . .</p>
<p>stay in foreground? It is called from the process logic of my extension  and keeps disappearing from the screen (Slicer switches itself to foreground) , from time to time</p>
<p>Thank you and best regards</p>
<p>Rudolf</p>

---

## Post #2 by @lassoan (2021-06-22 23:07 UTC)

<p>In general, it is better to avoid popup windows and instead place all widgets in the module widget (and disable parts of the GUI that you want to prevent from being manipulated). If you want to use a popup window then set the application’s main window as parent to make sure it always appears above the main window.</p>

---

## Post #3 by @rbumm (2021-06-23 07:02 UTC)

<p>Thank you.<br>
This works for me now:</p>
<pre><code class="lang-auto">progressbar=slicer.util.createProgressDialog(parent=slicer.util.mainWindow(),windowTitle='Processing...',autoClose=False)
</code></pre>

---
