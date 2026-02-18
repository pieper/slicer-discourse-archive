# Pass interface variables between classes

**Topic ID**: 31008
**Date**: 2023-08-06
**URL**: https://discourse.slicer.org/t/pass-interface-variables-between-classes/31008

---

## Post #1 by @Kening_Zhang (2023-08-06 09:30 UTC)

<p>Dear developers，<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f12d2be8b04241d0f94722ca02ad8a5fbe5e8356.png" data-download-href="/uploads/short-url/ypxQH3OONodqEnauhprKpqeWVTg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f12d2be8b04241d0f94722ca02ad8a5fbe5e8356_2_690x313.png" alt="image" data-base62-sha1="ypxQH3OONodqEnauhprKpqeWVTg" width="690" height="313" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f12d2be8b04241d0f94722ca02ad8a5fbe5e8356_2_690x313.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f12d2be8b04241d0f94722ca02ad8a5fbe5e8356_2_1035x469.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f12d2be8b04241d0f94722ca02ad8a5fbe5e8356_2_1380x626.png 2x" data-dominant-color="363E47"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1498×680 97.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I create a message box want to update the process phase of my code, I define it in Widget class, and it successfully show in interface,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d94e3f2cd87d310cc55a04c6054fbf7b3f0ce689.png" data-download-href="/uploads/short-url/v0nfKvWLA0UPBbauQ0pMxX1T1X3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d94e3f2cd87d310cc55a04c6054fbf7b3f0ce689.png" alt="image" data-base62-sha1="v0nfKvWLA0UPBbauQ0pMxX1T1X3" width="690" height="79" data-dominant-color="DFDFDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1008×116 4.59 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
But the question is I need to update the state in Logic class,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2a61e4ba5283f37e5e2070796f4872f48d22fc3.png" data-download-href="/uploads/short-url/puoTAHMkdCqM3L0opBOe6xuxfhN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2a61e4ba5283f37e5e2070796f4872f48d22fc3_2_690x155.png" alt="image" data-base62-sha1="puoTAHMkdCqM3L0opBOe6xuxfhN" width="690" height="155" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2a61e4ba5283f37e5e2070796f4872f48d22fc3_2_690x155.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2a61e4ba5283f37e5e2070796f4872f48d22fc3_2_1035x232.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2a61e4ba5283f37e5e2070796f4872f48d22fc3_2_1380x310.png 2x" data-dominant-color="373E45"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1578×356 44.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
When I click apply, error showed,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/1179266911b39e8a4c3121c4f4a0d226427949e3.png" data-download-href="/uploads/short-url/2uzG90vzIrgwUxSZ7ci4MQdM6sP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/1179266911b39e8a4c3121c4f4a0d226427949e3_2_690x212.png" alt="image" data-base62-sha1="2uzG90vzIrgwUxSZ7ci4MQdM6sP" width="690" height="212" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/1179266911b39e8a4c3121c4f4a0d226427949e3_2_690x212.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/1179266911b39e8a4c3121c4f4a0d226427949e3_2_1035x318.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/1179266911b39e8a4c3121c4f4a0d226427949e3.png 2x" data-dominant-color="FDE1E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1322×408 92.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
So I want to know how to pass ui2 between different classes.</p>
<p>Best wishes,<br>
Joshua</p>

---

## Post #2 by @pieper (2023-08-06 18:27 UTC)

<p>We often include a <code>progressCallback</code> option in the Logic constructor that defaults to a noop (e.g. like <code>lambda x: None</code>).  That way the logic code can operate with no GUI, e.g. in batch mode, but when the Widget provides a function that does GUI operations the user gets feedback.</p>

---

## Post #3 by @Kening_Zhang (2023-08-06 18:46 UTC)

<p>Sorry but I think I cannot understand it deeply.<br>
I want to show in the Slicer that user can know the stage of my code.</p>

---

## Post #4 by @pieper (2023-08-06 19:01 UTC)

<p>See how it’s used here for example:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/7ef59614c2458e4f693ab77834e6726cf6ae0540/Modules/Scripted/DICOMLib/DICOMBrowser.py#L409">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/7ef59614c2458e4f693ab77834e6726cf6ae0540/Modules/Scripted/DICOMLib/DICOMBrowser.py#L409" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/7ef59614c2458e4f693ab77834e6726cf6ae0540/Modules/Scripted/DICOMLib/DICOMBrowser.py#L409" target="_blank" rel="noopener">Slicer/Slicer/blob/7ef59614c2458e4f693ab77834e6726cf6ae0540/Modules/Scripted/DICOMLib/DICOMBrowser.py#L409</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="399" style="counter-reset: li-counter 398 ;">
          <li></li>
          <li>messages = []</li>
          <li>if missingFileCount &gt; 0:</li>
          <li>    messages.append(</li>
          <li>        _("Warning: {missing_file_count} of {total_file_count} selected files listed in the database cannot be found on disk.").format(</li>
          <li>            missing_file_count=missingFileCount, total_file_count=allFileCount))</li>
          <li></li>
          <li>if missingFileCount &lt; allFileCount:</li>
          <li>    progressDialog = slicer.util.createProgressDialog(parent=self, value=0, maximum=100)</li>
          <li></li>
          <li class="selected">    def progressCallback(progressDialog, progressLabel, progressValue):</li>
          <li>        progressDialog.labelText = '\n' + _("Checking {what}").format(what=progressLabel)</li>
          <li>        slicer.app.processEvents()</li>
          <li>        progressDialog.setValue(progressValue)</li>
          <li>        slicer.app.processEvents()</li>
          <li>        cancelled = progressDialog.wasCanceled</li>
          <li>        return cancelled</li>
          <li></li>
          <li>    loadablesByPlugin, loadEnabled = DICOMLib.getLoadablesFromFileLists(fileLists, selectedPlugins, messages,</li>
          <li>                                                                        lambda progressLabel, progressValue, progressDialog=progressDialog: progressCallback(progressDialog, progressLabel, progressValue),</li>
          <li>                                                                        self.pluginInstances)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You basically have a method in the Widget class that “knows” about the GUI that gets passed into the logic where there is no access to the GUI by default.  That way the logic class can be used as needed with different UI feedback or none at all.</p>

---
