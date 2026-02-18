# Use slicer vi@ web browser with parameters

**Topic ID**: 43282
**Date**: 2025-06-10
**URL**: https://discourse.slicer.org/t/use-slicer-vi-web-browser-with-parameters/43282

---

## Post #1 by @nicofutur8 (2025-06-10 10:09 UTC)

<p>Hello everyone,</p>
<p>I have created a plugin called “showPatientInfo” which shows certain metadata from a volume stored in DB and also shows if any user has connected.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69e4607f90621a0456264b77ffb3e7c6ce78d7e2.png" data-download-href="/uploads/short-url/f6LqDX4b7QcN7z04gGL2Fw9olPA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69e4607f90621a0456264b77ffb3e7c6ce78d7e2.png" alt="image" data-base62-sha1="f6LqDX4b7QcN7z04gGL2Fw9olPA" width="379" height="228"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">379×228 4.42 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The thing now is I would want to show this plugin via url action (slicer://) as you explained in docs.<br>
I don’t know what command i need to use to load my plugin and also, if it can be done, i would like to send user’s and image’s uids through this “url command”, so that my plugin can receive those UIDs as input parameters.</p>
<p>Thanks in advance, every piece of help is appreciated.<br>
Nico</p>

---

## Post #2 by @pieper (2025-06-10 12:54 UTC)

<p>You need to make a module that connects to the <code>onURLReceived</code> signal from the application.  Here’s an example:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/SlicerSandbox/blob/master/LoadRemoteFile/LoadRemoteFile.py#L48">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/LoadRemoteFile/LoadRemoteFile.py#L48" target="_blank" rel="noopener">github.com/PerkLab/SlicerSandbox</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerSandbox/blob/master/LoadRemoteFile/LoadRemoteFile.py#L48" target="_blank" rel="noopener">LoadRemoteFile/LoadRemoteFile.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/LoadRemoteFile/LoadRemoteFile.py#L48" rel="noopener"><code>master</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="38" style="counter-reset: li-counter 37 ;">
          <li>slicer://viewer/?download=https%3A%2F%2Fgithub.com%2Frbumm%2FSlicerLungCTAnalyzer%2Freleases%2Fdownload%2FSampleData%2FLungCTAnalyzerChestCT.nrrd</li>
          <li>See more information &lt;a href="https://discourse.slicer.org/t/how-to-load-nifti-file-from-web-browser-link/18664/5"&gt;here&lt;/a&gt;.</li>
          <li>"""</li>
          <li>    self.parent.acknowledgementText = """</li>
          <li>This file was originally developed by Andras Lasso, PerkLab and ASH.</li>
          <li>"""</li>
          <li></li>
          <li>    # Initilize self.sampleDataLogic. At this point, Slicer modules are not initialized yet, so we cannot instantiate the logic yet.</li>
          <li>    self.sampleDataLogic = None</li>
          <li></li>
          <li class="selected">    slicer.app.connect("urlReceived(QString)", self.onURLReceived)</li>
          <li></li>
          <li>  def reportProgress(self, message, logLevel=None):</li>
          <li>    # Print progress in the console</li>
          <li>    print(f"Loading... {self.sampleDataLogic.downloadPercent}%")</li>
          <li>    # Abort download if cancel is clicked in progress bar</li>
          <li>    if self.progressWindow.wasCanceled:</li>
          <li>        raise Exception("download aborted")</li>
          <li>    # Update progress window</li>
          <li>    self.progressWindow.show()</li>
          <li>    self.progressWindow.activateWindow()</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/SlicerSandbox/blob/master/LoadRemoteFile/LoadRemoteFile.py#L77">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/LoadRemoteFile/LoadRemoteFile.py#L77" target="_blank" rel="noopener">github.com/PerkLab/SlicerSandbox</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerSandbox/blob/master/LoadRemoteFile/LoadRemoteFile.py#L77" target="_blank" rel="noopener">LoadRemoteFile/LoadRemoteFile.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/LoadRemoteFile/LoadRemoteFile.py#L77" rel="noopener"><code>master</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="67" style="counter-reset: li-counter 66 ;">
          <li>    threeDWidget = layoutManager.threeDWidget(0)</li>
          <li>    threeDView = threeDWidget.threeDView()</li>
          <li>    threeDView.resetFocalPoint()</li>
          <li></li>
          <li>def showSliceViewsIn3d(self):</li>
          <li>  layoutManager = slicer.app.layoutManager()</li>
          <li>  for sliceViewName in layoutManager.sliceViewNames():</li>
          <li>    controller = layoutManager.sliceWidget(sliceViewName).sliceController()</li>
          <li>    controller.setSliceVisible(True)</li>
          <li></li>
          <li class="selected">def onURLReceived(self, urlString):</li>
          <li>  """Process DICOM view requests. URL protocol and path must be: slicer://viewer/</li>
          <li>  Query parameters:</li>
          <li>    - `download`: download and show with default file type</li>
          <li>    - `image` or `volume`: download and show as image</li>
          <li>    - `segmentation`: download and show as segmentation</li>
          <li>    - `show3d`: show segmentation in 3D and center 3D view</li>
          <li>    - `filename`: filename to specify file format and node name for the first node; useful if the download URL does not contain filename</li>
          <li></li>
          <li>  Display a file (using default file type):</li>
          <li></li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
