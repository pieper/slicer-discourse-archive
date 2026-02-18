# Hanging popup some times after loading DICOM files

**Topic ID**: 6057
**Date**: 2019-03-07
**URL**: https://discourse.slicer.org/t/hanging-popup-some-times-after-loading-dicom-files/6057

---

## Post #1 by @torquil (2019-03-07 10:28 UTC)

<p>Sometimes after loading som DICOM files, the popup window showing the text “Processing…” doesn’t disappear unless I close it manually. I don’t know why it happens, and it doesn’t happen every time. Usually it just disppears almost immediately after it appears. But when I look at many different DICOM files in a row, it inevitably happens after a while. I use CRTL+w to close each scene and then go to the DICOM browser to select a different entry in the DICOM browser, click on “Examine” and then “Load”.</p>
<p>The problem is not tied to any specific DICOM files. I’m not able to reproduce it reliably.</p>
<p>Here is a screenshot showing the hanging popup window:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81f6a22d0923cd6891be660b6d4b9b1230ead403.png" data-download-href="/uploads/short-url/ixI0dxS19jv844gob1qLifuvXkT.png?dl=1" title="slicer3d_processing_popup" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81f6a22d0923cd6891be660b6d4b9b1230ead403_2_690x461.png" alt="slicer3d_processing_popup" data-base62-sha1="ixI0dxS19jv844gob1qLifuvXkT" width="690" height="461" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81f6a22d0923cd6891be660b6d4b9b1230ead403_2_690x461.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81f6a22d0923cd6891be660b6d4b9b1230ead403_2_1035x691.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81f6a22d0923cd6891be660b6d4b9b1230ead403_2_1380x922.png 2x" data-dominant-color="8D8EB5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer3d_processing_popup</span><span class="informations">1500×1004 47 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best regards,<br>
Torquil Sørensen</p>

---

## Post #2 by @jamesobutler (2019-03-07 13:06 UTC)

<p>You might have found something related to the issue discussed at <a href="https://github.com/Slicer/Slicer/pull/951" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/951</a>.</p>
<p>Which Slicer version are you using?</p>

---

## Post #3 by @torquil (2019-03-07 13:27 UTC)

<p>I’m using Slicer 3D nightly version 4.11.0-2019-03-03 r27973 on Linux. I think the problem has occured on all the Slicer versions I have used for several months. I have only used the nightly builds.</p>

---

## Post #4 by @jeffmax (2024-11-19 14:36 UTC)

<p>I have noticed this problem as well in all versions of Slicer I have tried, including a recent preview release. For whatever reason, it happens reliably when I am using Slicer with Xpra (both HTML5 and Python client). I believe I have traced the issue to this spot in the code not reliably working:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMLib/DICOMBrowser.py#L624">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMLib/DICOMBrowser.py#L624" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMLib/DICOMBrowser.py#L624" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/main/Modules/Scripted/DICOMLib/DICOMBrowser.py#L624</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="614" style="counter-reset: li-counter 613 ;">
          <li>    messages = []</li>
          <li>    loadedNodeIDs = DICOMLib.loadLoadables(self.loadablesByPlugin, messages,</li>
          <li>                                           lambda progressLabel, progressValue, progressDialog=progressDialog: progressCallback(progressDialog, progressLabel, progressValue))</li>
          <li></li>
          <li>    loadedFileParameters = {}</li>
          <li>    loadedFileParameters["nodeIDs"] = loadedNodeIDs</li>
          <li>    slicer.app.ioManager().emitNewFileLoaded(loadedFileParameters)</li>
          <li></li>
          <li>    qt.QApplication.restoreOverrideCursor()</li>
          <li></li>
          <li class="selected">    progressDialog.close()</li>
          <li></li>
          <li>    if messages:</li>
          <li>        slicer.util.warningDisplay("\n".join(messages), windowTitle=_("DICOM loading"))</li>
          <li></li>
          <li>    self.onLoadingFinished()</li>
          <li></li>
          <li>def warnUserIfLoadableWarningsAndProceed(self):</li>
          <li>    warningsInSelectedLoadables = False</li>
          <li>    details = ""</li>
          <li>    for plugin in self.loadablesByPlugin:</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>This occurs in the workflow where a QProgressDialog has already been <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMLib/DICOMBrowser.py#L474" rel="noopener nofollow ugc">opened</a> and <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMLib/DICOMBrowser.py#L490" rel="noopener nofollow ugc">closed</a> immediately prior.</p>
<p>I also noticed that if I manually expand the popup, there appears to be a lot of artifacts from prior windows all around the area that was previously visible when it was smaller.</p>
<p>I don’t have much experience with Qt, but I do not see anything obviously wrong with the use of the QProgressDialog. It is a minor issue but if anyone has ideas I would appreciate it.</p>

---

## Post #5 by @jeffmax (2024-11-19 21:55 UTC)

<p>Just noting that adding</p>
<pre><code>progressDialog.setParent(None) 
</code></pre>
<p>before</p>
<pre><code>progressDialog.close()
</code></pre>
<p>seems to resolve the issue, but I am not clear why.</p>

---

## Post #6 by @pieper (2024-11-19 21:57 UTC)

<p>That sounds harmless so if it works, why not add it.  Do you want to put in a PR?</p>

---

## Post #7 by @jeffmax (2024-11-19 22:37 UTC)

<p>Sure, I can do that. I do a little more testing first.</p>

---

## Post #8 by @jeffmax (2024-11-21 17:37 UTC)

<p>Upon further testing, adding the line:</p>
<pre><code>progressDialog.deleteLater() 
</code></pre>
<p>after</p>
<pre><code>progressDialog.close()
</code></pre>
<p>also solves the problem. Doing both deleteLater() and setParent(None) together also works. I am not sure if one or the other, or both makes more sense. Happy to open a PR though. Unless someone with more understanding in the QT widget lifecycle has input, I would put both into the PR.</p>

---

## Post #9 by @pieper (2024-11-21 18:07 UTC)

<p>I’m not sure either.  I’ve only seen this on linux, so maybe it’s just a corner case.  As long as one of the approach works we should probably just go ahead with whatever works and seems least intrusive.</p>

---
