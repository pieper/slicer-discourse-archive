# Installing python modules hangs the UI

**Topic ID**: 13732
**Date**: 2020-09-28
**URL**: https://discourse.slicer.org/t/installing-python-modules-hangs-the-ui/13732

---

## Post #1 by @strider_hunter (2020-09-28 12:32 UTC)

<p><strong>Context of Issue</strong><br>
I am trying to build a python extension that needs to install python libraries upon loading.<br>
I have the following requirements</p>
<ol>
<li>Install and load modules via code</li>
<li>Show a progress bar and do not hang the UI while performing Step 1</li>
</ol>
<p><strong>Status of Issue</strong></p>
<ul>
<li>Step 1 - I am able to use slicer.util.pip_install(’’) to successfully install the library in the python belonging to slicer</li>
<li>Step 2 - I am able to show the progress bar by using <em>qt.QProgressDialog()</em> (<a href="https://github.com/Slicer/Slicer/blob/87ca5d3378b1fe1bb4eced078887fcbfc1cbd9c2/Modules/Scripted/DICOMLib/DICOMBrowser.py#L442" rel="noopener nofollow ugc">ref</a>).  Unfortunately while loading the module does not hang the UI, installing it does so. Installing a module via the python interpreter does the same thing.</li>
</ul>
<p>Since I plan to share this extension with physicians, the UI-hanging part could be a deterrent in adoption of the extension. Is there a way around it so that I dont block the UI thread?</p>

---

## Post #2 by @lassoan (2020-09-28 13:24 UTC)

<p>Thanks for raising this issue. I’ve also found that I can easily end up with Python downloading hundreds of megabytes of packages and installing them quite slowly, so I agree that it could make sense to indicate progress to users. We implemented <code>pip_install</code> function with the exact purpose of allowing adding features such as progress reporting on GUI, and probably time has arrived to implement it.</p>
<p>It should be as easy as creating a new variant of <a href="https://github.com/Slicer/Slicer/blob/87ca5d3378b1fe1bb4eced078887fcbfc1cbd9c2/Base/Python/slicer/util.py#L2545"><code>logProcessOutput(proc)</code></a>, which would show messages in a GUI window instead of just in Python console. Name of this function could be <code>displayProcessOutput(proc)</code> and make <code> _executePythonModule</code> use it instead of <code>logProcessOutput</code> when requested (e.g., introduce a new <code>showWindow=True</code> argument for <code>_executePythonModule</code> and <code>pip_install</code>).</p>
<p>This new <code>displayProcessOutput(proc)</code> function would be almost exactly the same as <code>logProcessOutput</code>, but it would create a progress dialog and show the name of current operation instead of <a href="https://github.com/Slicer/Slicer/blob/87ca5d3378b1fe1bb4eced078887fcbfc1cbd9c2/Base/Python/slicer/util.py#L2510">logging stdout</a>, and hide the dialog when the process is finished.</p>
<p>You can create a progress bar with busy indicator like this:</p>
<pre><code class="lang-auto">progressbar = slicer.util.createProgressDialog(autoClose=False)
progressbar.minimum=0
progressbar.maximum=0
</code></pre>
<p>You can set label text by calling:</p>
<pre><code class="lang-auto">progressbar.setLabelText(currentOperation)
</code></pre>
<p>Probably we should hide “Cancel” button, because although we could kill the install process, it might leave the package list in an inconsistent state.</p>
<p>We could try to show an actual progress bar instead of a busy indicator (infinite progress bar), but since even Navigator (Anaconda’s GUI client for installing python packages) does not do this, it might be too ambitious.</p>
<p>You can implement and test all these changes by simply editing <code>c:\Users\&lt;username&gt;\AppData\Local\NA-MIC\Slicer 4.11.0-&lt;date&gt;\bin\Python\slicer\util.py</code> file in a recent Slicer installation. If you have any questions then let us know. Thanks for working on this!</p>

---

## Post #3 by @strider_hunter (2020-09-28 14:09 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> for your response. I have taken a look at the functions you mentioned.<br>
But I think we have different goals here.</p>
<p>I simply do not want the app to freeze while using “<em>subprocess.Popen()</em>” in “<em>utils.launchConsoleProcess()</em>” as faced by many others (<a href="https://stackoverflow.com/questions/20471618/subprocess-cause-user-interface-to-freeze" rel="noopener nofollow ugc">ref1</a>, <a href="https://stackoverflow.com/questions/39567467/python-ui-app-hangs-while-updating-stdout-output-to-ui-using-subprocess-popen-in" rel="noopener nofollow ugc">ref2</a>). To further elucidate my point, I have attached a screenshot. Notice the “<strong>Not responding</strong>” error on the top bar of the window as it has downloaded the package and is moving on to installing it. A solution for this is to use “QProcess”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5892e7584d8dbda57ed2958c29ed3e0e38afdba3.png" data-download-href="/uploads/short-url/cDyKWjC5mwE0jkryW2DwOwvFK7h.png?dl=1" title="SliceHang" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5892e7584d8dbda57ed2958c29ed3e0e38afdba3_2_134x499.png" alt="SliceHang" data-base62-sha1="cDyKWjC5mwE0jkryW2DwOwvFK7h" width="134" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5892e7584d8dbda57ed2958c29ed3e0e38afdba3_2_134x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5892e7584d8dbda57ed2958c29ed3e0e38afdba3_2_201x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5892e7584d8dbda57ed2958c29ed3e0e38afdba3_2_268x998.png 2x" data-dominant-color="EBEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SliceHang</span><span class="informations">362×1345 44 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>On the other hand, you’ve proposed a progress bar (which could come in handy for large libraries). But will it prevent the app from freezing up?</p>
<p>I would preferably want the user to be able to do other things as pip does its thing (like loading files etc.)</p>

---

## Post #4 by @lassoan (2020-09-28 14:53 UTC)

<p>The application is blocked by this <a href="https://github.com/Slicer/Slicer/blob/87ca5d3378b1fe1bb4eced078887fcbfc1cbd9c2/Base/Python/slicer/util.py#L2508-L2513">loop in <code>logProcessOutput</code></a> because we don’t want the user to do things while installation is in progress. Running pip install while the user is allowed to do anything in the application would be similar to replacing wheels on your car while you are driving it.</p>
<p>If you are confident that in your module installation does not usually lead to problems (you just install additional packages, no existing packages gets updated) then you can simply remove the loop or show progress bar on the status bar instead of a popup window to not block the GUI.</p>
<p>You probably still want to to make sure the user does not exit the application before the installation is completed and check for the final installation results. You can keep checking the process output every now and then, for example set up a repeating timer for 10sec and check the process output in the callback function.</p>

---

## Post #5 by @pieper (2020-09-28 20:37 UTC)

<p>I agree that a one-time blocking install with a spinning progress par would be completely normal.  Could have a message like “Completing installation” or similar.</p>
<p>You might also want to send the lines to the status bar, just so people can get a sense that things are going on without needing to open the python console.  You can add something like this to the logging line.</p>
<pre><code class="lang-auto">slicer.util.mainWindow().statusBar().showMessage("progress")
</code></pre>

---
