---
topic_id: 31220
title: "Warning When Closing Scene"
date: 2023-08-18
url: https://discourse.slicer.org/t/31220
---

# Warning when closing scene

**Topic ID**: 31220
**Date**: 2023-08-18
**URL**: https://discourse.slicer.org/t/warning-when-closing-scene/31220

---

## Post #1 by @lukasvanderstricht (2023-08-18 12:19 UTC)

<p>Hi everyone!</p>
<p>I am working with slicer and I have developed some scripts that automate certain aspects of the segmentation workflow. These include the functionality that run MONAILabel’s automatic segmentation on consecutive samples. The only thing I am struggling with however is the fact that every time a new sample is loaded, there is a pop-up screen asking the user to confirm that the scene can be closed, such as the one below.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa20b415a5fea36f53e7c26ad643a5cc031038a0.png" alt="Screenshot from 2023-08-18 14-07-41" data-base62-sha1="oh1eGhyvrTBO3BeBR5a9X0A5UyI" width="499" height="128"></p>
<p>Of course this pop-up takes away from the automatic streamlined workflow of my scripts because user interaction is necessary to move on here.</p>
<p><strong>My question is: is there a way to disable this pop-up (either from the GUI or in Python).</strong></p>
<p>I have already looked into the application settings of Slicer and have found an option called <code>Confirm on scene close</code> under <code>General</code> that  seems to allow this pop-up to be turned off (see below).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86aa1408b29a171dec71cfce062fb55e2ef7a7fb.png" data-download-href="/uploads/short-url/jdin44oDTKG9ZbjlDjCrX0WdANl.png?dl=1" title="Screenshot from 2023-08-18 14-05-09" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86aa1408b29a171dec71cfce062fb55e2ef7a7fb_2_690x280.png" alt="Screenshot from 2023-08-18 14-05-09" data-base62-sha1="jdin44oDTKG9ZbjlDjCrX0WdANl" width="690" height="280" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86aa1408b29a171dec71cfce062fb55e2ef7a7fb_2_690x280.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86aa1408b29a171dec71cfce062fb55e2ef7a7fb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86aa1408b29a171dec71cfce062fb55e2ef7a7fb.png 2x" data-dominant-color="E7E7E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2023-08-18 14-05-09</span><span class="informations">825×335 56.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, even after deselecting the corresponding box and restarting the application, the pop-up window still pops up every time I retrieve the next sample.</p>
<p>Any ideas for alternatives?</p>
<p>Thanks in advance!</p>
<p>Kind regards</p>
<p>Lukas</p>

---

## Post #2 by @pieper (2023-08-18 16:05 UTC)

<p>this dialog is actually in the MONAILabel code, so you should be able to make a PR with an option to disable it.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Project-MONAI/MONAILabel/blob/main/plugins/slicer/MONAILabel/MONAILabel.py#L1216-L1223">
  <header class="source">

      <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/plugins/slicer/MONAILabel/MONAILabel.py#L1216-L1223" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Project-MONAI/MONAILabel/blob/main/plugins/slicer/MONAILabel/MONAILabel.py#L1216-L1223" target="_blank" rel="noopener">Project-MONAI/MONAILabel/blob/main/plugins/slicer/MONAILabel/MONAILabel.py#L1216-L1223</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="1216" style="counter-reset: li-counter 1215 ;">
          <li>if self._volumeNode or len(slicer.util.getNodesByClass("vtkMRMLScalarVolumeNode")):</li>
          <li>    if not slicer.util.confirmOkCancelDisplay(</li>
          <li>        "This will close current scene.  Please make sure you have saved your current work.\n"</li>
          <li>        "Are you sure to continue?"</li>
          <li>    ):</li>
          <li>        return</li>
          <li>    self.onResetScribbles()</li>
          <li>    slicer.mrmlScene.Clear(0)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
