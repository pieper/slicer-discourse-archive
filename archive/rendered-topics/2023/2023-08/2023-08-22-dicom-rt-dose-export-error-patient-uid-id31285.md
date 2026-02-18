# Dicom RT dose export error: patient UID

**Topic ID**: 31285
**Date**: 2023-08-22
**URL**: https://discourse.slicer.org/t/dicom-rt-dose-export-error-patient-uid/31285

---

## Post #1 by @jborsavage (2023-08-22 14:24 UTC)

<p>3D Slicer community,</p>
<p>I am trying to convert 3ddose files generated in EGSnrc’s dosxyz to dicom RT dose volumes for analysis in Eclipse. However, I am unable to import the dcm files due to errors regarding the plan UID.</p>
<p>My workflow is as follows:</p>
<ol>
<li>import Eclipse plan (image series, structures, etc.)</li>
<li>import 3ddose file</li>
<li>drag and drop 3ddose file under study generated in step 1</li>
<li>convert 3ddose to RT dose volume</li>
<li>export to dicom</li>
</ol>
<p>I’m not editing any dicom tags in the process and I’m not sure if this is something I could fix by editing the metadata of the exported RT dose. Any ideas/suggestions are much appreciated, thanks!!</p>

---

## Post #2 by @jborsavage (2023-08-22 16:26 UTC)

<p>Maybe this post was preemptive, but I figured I’d follow up in case it’s helpful for anyone else who encounters this issue. The RT dose dcm file exported from 3D slicer was missing the ReferencedSOPInstanceUID tag from the dicom header. I edited this tag in Matlab to match the ReferencedSOPInstanceUID in the header of the dose dcm file generated in Eclipse, then wrote the edited header info and image data to a new file. With this edit, Eclipse was able connect the 3D slicer converted dose file to a pre-existing plan and successfully import the file.</p>

---

## Post #3 by @cpinter (2023-08-28 09:38 UTC)

<p>Since this seems to be a shortcoming on the SlicerRT DICOM-RT export side, I added a ticket:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/SlicerRt/SlicerRT/issues/233">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/issues/233" target="_blank" rel="noopener">github.com/SlicerRt/SlicerRT</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerRt/SlicerRT/issues/233" target="_blank" rel="noopener">Set required DICOM reference between dose and CT</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-08-28" data-time="09:38:00" data-timezone="UTC">09:38AM - 28 Aug 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/cpinter" target="_blank" rel="noopener">
          <img alt="cpinter" src="https://avatars.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
          cpinter
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">See https://discourse.slicer.org/t/dicom-rt-dose-export-error-patient-uid/31285</p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Thanks <a class="mention" href="/u/jborsavage">@jborsavage</a> for the report and the description of the solution.</p>

---

## Post #4 by @Mik (2023-09-17 14:37 UTC)

<p>What exactly Referenced Sequence did you use?</p>
<p>The <a href="https://dicom.nema.org/medical/Dicom/2023c/output/chtml/part03/sect_C.8.8.3.html" rel="noopener nofollow ugc">standard</a> allows several options: Referenced RT Plan Sequence (mandatory if you have RtPlan with ControlPointSequence) with tag (300c,0002), Referenced Image Sequence with tag (300c,0002).</p>
<p>I suppose that you just have generated reference to CT data series?</p>

---
