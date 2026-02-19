---
topic_id: 37649
title: "Usage Of Ctcreate Dosxyznrc On 3D Slicer"
date: 2024-08-01
url: https://discourse.slicer.org/t/37649
---

# Usage of Ctcreate (DOSXYZnrc) on 3D slicer

**Topic ID**: 37649
**Date**: 2024-08-01
**URL**: https://discourse.slicer.org/t/usage-of-ctcreate-dosxyznrc-on-3d-slicer/37649

---

## Post #1 by @yassir_elghazi (2024-08-01 06:39 UTC)

<p>Hello Scientists,<br>
I have just imported the DICOM Folder of a patient, where it contains the DICOM images and RT structures and also doses distribution. it is a complet study exported from TPS. when i import it to the 3D Slicer, i noticed that there is an option of converting images using CTCreate, in order to be read by dosxyznrc, but i don’t know how to execute the conversion. My question is: does 3D Slicer can generate an input file and phantom file for usage in DOSXYZnrc? the attached image displays the option that i talked about !<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/687386ca7bd7d1d907242c3ddd5bf7d7f5627183.png" data-download-href="/uploads/short-url/eU1aCKaX4GeL6FsqrhkGtYdrSkr.png?dl=1" title="image.psd(82)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/687386ca7bd7d1d907242c3ddd5bf7d7f5627183_2_491x500.png" alt="image.psd(82)" data-base62-sha1="eU1aCKaX4GeL6FsqrhkGtYdrSkr" width="491" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/687386ca7bd7d1d907242c3ddd5bf7d7f5627183_2_491x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/687386ca7bd7d1d907242c3ddd5bf7d7f5627183.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/687386ca7bd7d1d907242c3ddd5bf7d7f5627183.png 2x" data-dominant-color="D4D5D3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.psd(82)</span><span class="informations">683×695 36 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2024-08-02 13:12 UTC)

<p>DOSXYZnrc has been integrated into Slicer(RT) as part of a specific dose engine. The dose engines are plugins for the External Beam Planning module, and they can be executed from said module after setting up the beams.</p>
<p>The Orthovoltage plugin does every necessary step as part of its dose computation, and there is no GUI for doing the individual steps. The code that runs the <code>ctcreate</code> step in the dose engine is here:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerRT/blob/master/ExternalBeamPlanning/Widgets/Python/OrthovoltageDoseEngine.py#L306">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/ExternalBeamPlanning/Widgets/Python/OrthovoltageDoseEngine.py#L306" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/ExternalBeamPlanning/Widgets/Python/OrthovoltageDoseEngine.py#L306" target="_blank" rel="noopener">SlicerRt/SlicerRT/blob/master/ExternalBeamPlanning/Widgets/Python/OrthovoltageDoseEngine.py#L306</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="296" style="counter-reset: li-counter 295 ;">
          <li>  try:</li>
          <li>    roiNode = slicer.util.getNode(roiNodeName)</li>
          <li>  except:</li>
          <li>    logging.error("Unable to get ROI by name " + roiNodeName)</li>
          <li></li>
          <li>thicknesses = None</li>
          <li>if sliceThicknessX != "" and sliceThicknessY != "" and sliceThicknessZ != "":</li>
          <li>  thicknesses = [float(sliceThicknessX), float(sliceThicknessY), float(sliceThicknessZ)]</li>
          <li></li>
          <li>##########################################</li>
          <li class="selected"># Call ctcreate</li>
          <li>##########################################</li>
          <li></li>
          <li>runCTCreateDOSXYZnrc = int(self.scriptedEngine.parameter(beamNode, "RunCTCreateDOSXYZnrc"))</li>
          <li>if runCTCreateDOSXYZnrc != self.runDOSXYZnrcOnlyIndex:</li>
          <li>  logging.info("Running ctCreate")</li>
          <li>  materialJSON = self.scriptedEngine.parameter(beamNode, "Materials")</li>
          <li>  try:</li>
          <li>    materials = json.loads(materialJSON)</li>
          <li>  except:</li>
          <li>    logging.error("Unable parse materials JSON string")</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Let me know if you have further questions.</p>

---
