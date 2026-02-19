---
topic_id: 2155
title: "Splash Screen Does Not Disappear After Startup And Covers An"
date: 2018-02-22
url: https://discourse.slicer.org/t/2155
---

# Splash screen does not disappear after startup and covers another popup

**Topic ID**: 2155
**Date**: 2018-02-22
**URL**: https://discourse.slicer.org/t/splash-screen-does-not-disappear-after-startup-and-covers-another-popup/2155

---

## Post #1 by @fedorov (2018-02-22 23:34 UTC)

<p>I just discovered that if Slicer is launched for the first time (ie after removing the settings directory), the splash screen does not disappear after startup, and covers the popup window prompting to accept that Slicer is not FDA approved. See demo below. Today’s nightly on Mac.</p>
            <video title="2018-02-22_18-33-47.mp4" width="695" height="492" style="max-width:100%" controls="">
              <source src="https://content.screencast.com/users/andrey.fedorov/folders/Snagit/media/d4db6baf-3fa1-4c81-b337-8958a2dfb002/2018-02-22_18-33-47.mp4"></source>
            </video>


---

## Post #2 by @pieper (2018-02-23 01:45 UTC)

<p>I can confirm this by running:</p>
<pre><code class="lang-auto">$ /Volumes/Slicer-4.9.0-2018-02-21-macosx-amd64/Slicer.app/Contents/MacOS/Slicer --disable-settings
</code></pre>
<p>A workaround is to hit the enter key to bypass the hidden dialog.</p>
<p>Here is the error log -</p>
<pre><code class="lang-auto">Session start time .......: 2018-02-22 20:44:34
Slicer version ...........: 4.9.0-2018-02-21 (revision 26937) macosx-amd64 - installed
Operating system .........: Mac OS X / 10.13.3 / 17D47 - 64-bit
Memory ...................: 65536 MB physical, 0 MB virtual
CPU ......................: GenuineIntel Intel(R) Xeon(R) CPU E5-2697 v2 @ 2.70GHz, 12 cores, 24 logical processors
Developer mode enabled ...: no
Prefer executable CLI ....: yes
Additional module paths ..: (none)
Number of registered modules: 136
Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)
Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)
libpng warning: iCCP: known incorrect sRGB profile
Number of instantiated modules: 136
Scripted subject hierarchy plugin registered: Annotations
[6570:80131:0222/204438.066624:ERROR:gl_context_cgl.cc(137)] Error creating context.
[6570:80131:0222/204438.134244:ERROR:gl_context_cgl.cc(137)] Error creating context.
Scripted subject hierarchy plugin registered: SegmentEditor
Scripted subject hierarchy plugin registered: SegmentStatistics
Number of loaded modules: 136
Switch to module:  "Welcome"
Uncaught TypeError: channel.execCallbacks[message.id] is not a function
</code></pre>

---

## Post #3 by @lassoan (2018-02-23 06:38 UTC)

<p>I guess the issue is due to the recent changes caused by extension update checker, which <a href="https://discourse.slicer.org/t/scripted-module-initialization-after-application-startup-is-completed/2080">introduced event processing before application startup is completed</a>. I cannot reproduce the problem on Windows, so I cannot verify this, but probably this line is the culprit:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/d1b9611ad098a291f00625674c50913f3ddf9773/Applications/SlicerApp/qSlicerAppMainWindow.cxx#L1218" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/d1b9611ad098a291f00625674c50913f3ddf9773/Applications/SlicerApp/qSlicerAppMainWindow.cxx#L1218" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/d1b9611ad098a291f00625674c50913f3ddf9773/Applications/SlicerApp/qSlicerAppMainWindow.cxx#L1218</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="1208" style="counter-reset: li-counter 1207 ;">
<li>  }</li>
<li>
</li>
<li>// Replace "%1" in the text by the name and version of the application</li>
<li>message = message.arg(app-&gt;applicationName() + " " + app-&gt;applicationVersion());</li>
<li>
</li>
<li>ctkMessageBox* disclaimerMessage = new ctkMessageBox(this);</li>
<li>disclaimerMessage-&gt;setAttribute( Qt::WA_DeleteOnClose, true );</li>
<li>disclaimerMessage-&gt;setText(message);</li>
<li>disclaimerMessage-&gt;setIcon(QMessageBox::Information);</li>
<li>disclaimerMessage-&gt;setDontShowAgainSettingsKey("MainWindow/DontShowDisclaimerMessage");</li>
<li class="selected">QTimer::singleShot(0, disclaimerMessage, SLOT(exec()));</li>
<li>}</li>
<li>
</li>
<li>//-----------------------------------------------------------------------------</li>
<li>void qSlicerAppMainWindow::setupMenuActions()</li>
<li>{</li>
<li>Q_D(qSlicerAppMainWindow);</li>
<li>
</li>
<li>d-&gt;ViewLayoutConventionalAction-&gt;setData(vtkMRMLLayoutNode::SlicerLayoutConventionalView);</li>
<li>d-&gt;ViewLayoutConventionalWidescreenAction-&gt;setData(vtkMRMLLayoutNode::SlicerLayoutConventionalWidescreenView);</li>
<li>d-&gt;ViewLayoutConventionalQuantitativeAction-&gt;setData(vtkMRMLLayoutNode::SlicerLayoutConventionalQuantitativeView);</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Instead of relying on timer events processed after startup completed, the application’s <code>startupCompleted()</code> signal should be used instead.</p>
<p>There can be many other places where event processing before application startup may cause problems, so probably it would be better to delay the extension update check (gatherExtensionsHistoryInformationOnStartup): it should be started <em>after</em> application startup is completed.</p>
<p>It is also very odd that extension update check is performed at every startup. If extension update check is successfully completed then it should not be performed again within 10-20 hours.</p>

---

## Post #4 by @fedorov (2018-02-23 14:58 UTC)

<p>I also found that (under some conditions that are unclear to me) the DICOM Browser window gets covered by the main app window, and “Show DICOM Browser” button does not bring it back. However, I can’t consistently reproduce this. From <a class="mention" href="/u/lassoan">@lassoan</a> post it sounds like this may be a related issue.</p>

---

## Post #5 by @fedorov (2018-04-17 15:59 UTC)

<p>Ran into this nasty problem again today - this time there was a popup (shown below) that required an answer for the application to start, but it was obscured by the splash screen! (I did not start any DICOM listeners knowingly, not sure where this came from)</p>
<p>Once I <strong>noticed</strong> that popup (it blinks really quickly before splash screen covers it), I then ran Slicer with <code>--no-splash</code> command line argument.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97b9143d88b9207a51f8acaad0fbcd1001f8c1a0.png" alt="image" data-base62-sha1="lEcCWqEwWOqIgG5Qc2Gw6EJa1vq" width="353" height="133"></p>
<p>I think it is somewhat unlikely a beginner or even an average user would be able to identify the issue and find this workaround. I would suggest disabling splash screen until related issues are resolved.</p>

---

## Post #6 by @lassoan (2018-04-17 16:26 UTC)

<p>The problem is that DICOM module starts some operations before application startup is completed. Since extension update checker now starts event processing before application startup is completed, this can cause various issues.</p>
<p>DICOM module (DICOM.py) must be fixed to not start doing any processing in module <strong>init</strong> method (this has been always a bad practice). but perform all operations in a method that is called when slicer.app startupCompleted() signal is emitted. DICOM module already has such a method, so just all initialization steps must be moved there.</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> Can your team give it a try to implement a fix?</p>

---

## Post #7 by @fedorov (2018-04-17 16:39 UTC)

<p>I think there are various situations where popups requiring user action can be covered by the splash screen, effectively blocking the application, so it does not resolve the underlying problem with the splash screen issue.</p>
<p>I have not been doing anything at that level in Slicer for quite a while, and I have a lot of things going on right now. I can’t take on this task you mentioned at this time.</p>

---

## Post #8 by @pieper (2018-04-17 18:51 UTC)

<p>At least for the DICOM module, it looks like it’s just a matter of moving this <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOM/DICOM.py#L44-L68">code</a> into <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOM/DICOM.py#L77">this method.</a> so that it happens after the application is started.</p>
<p>But if it’s not just the DICOM module that can lead to this issue, then there should be a timer that turns off the splash screen.</p>

---

## Post #9 by @lassoan (2018-04-17 21:26 UTC)

<p>There is a timer already. The problem is that the timer event is not processed until the modal popup is closed.</p>
<p>There were a handful of other modules that used one-shot timers to perform tasks at application startup but they have been all fixed. DICOM module was missed because it did not even use timer but directly performed actions in the module class constructor, which must never happen. We should document somewhere that this must be avoided.</p>

---

## Post #10 by @pieper (2018-04-17 22:26 UTC)

<p>Note: this is a mac-specific bug.  On windows and linux the popups appear in front of the splash screen.</p>

---

## Post #11 by @ihnorton (2018-04-18 02:23 UTC)

<p>I’ve seen a few similar weird issues with modal windows getting stuck behind the main one after startup, and making the main unresponsive. Also on Mac. Perhaps related: slice pop-up widgets floating all alone when using command-tab to select a Slicer instance with the main on a different desktop (“Space”?). I had been blaming a window controller extension I use called Spectacle, but seems like there could be some bug(s) in Qt.</p>

---

## Post #12 by @pieper (2018-04-22 19:02 UTC)

<p>Unfortunately rearranging that code so that the dialog is triggered by startupComplete doesn’t work - the  splash screen is still up when the signal is emitted.</p>

---

## Post #13 by @lassoan (2018-04-22 20:05 UTC)

<p>Maybe we should hide the splash window explicitly before emitting the application startup signal?</p>

---

## Post #14 by @pieper (2018-04-22 20:23 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="2155" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Maybe we should hide the splash window explicitly before emitting the application startup signal?</p>
</blockquote>
</aside>
<p>Yes, it seems the core issue is that the <a href="http://doc.qt.io/qt-5/qsplashscreen.html#finish">finish method</a> of the splash screen <a href="https://github.com/qt/qtbase/blob/a37dd93defd91b79fb6730d0ff0515a66a0d3972/src/widgets/widgets/qsplashscreen.cpp#L234-L271">waits until the main window is displayed before going away</a>.</p>
<p>I haven’t had a chance to make a fresh mac build to test it, but closing the splash screen directly should work.</p>

---

## Post #15 by @pieper (2018-04-30 16:01 UTC)

<p>Note that this is a mac Qt5 issue only.  I’ve tried various changes to the code but haven’t found a workable solution yet.</p>

---

## Post #16 by @lassoan (2018-04-30 18:13 UTC)

<p>You mean you cannot force closing of the splash screen (or the splash screen is closed but the popup still does not appear)? Do you still have problems if you create the modal popup after splash screen is closed?</p>

---

## Post #17 by @pieper (2018-05-01 15:22 UTC)

<p>The problem is that the splash screen is closed when the main window appears but the startupComplete signal is emitted before that has happened.  I’m committing a fix now that closes the splashscreen before showing the main window, and this resolves the issue.</p>

---

## Post #18 by @pieper (2018-05-01 15:26 UTC)

<p>Fix committed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27172">r27172</a>.</p>

---

## Post #19 by @fedorov (2018-05-01 15:49 UTC)

<p>Thank you for working on this Steve! I hope this will resolve the issue.</p>

---
