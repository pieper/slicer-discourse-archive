# Integration with AWS HealthImaging

**Topic ID**: 42604
**Date**: 2025-04-17
**URL**: https://discourse.slicer.org/t/integration-with-aws-healthimaging/42604

---

## Post #1 by @ksidis (2025-04-17 14:48 UTC)

<p>Hello,</p>
<p>Thank you for providing this amazing tool.</p>
<p>I recently got involved in a PoT about AWS HealthImaging (AHI) service (formerly known as  AWS HealthLake). After a quick look I realised that out of the box it only supports DICOMWeb WADO-RS. As a result, the only way to connect it to a running 3DSlicer is by deploying additional solutions that expose a DICOM QIDO endpoint on top of an AHI datastore. Am I correct in my assumption?</p>
<p>Currently, is there any other way (maybe via an extension) to connect to AHI, search and retrieve DICOM images? If not, is it on your roadmap, or you believe that the DICOMWeb capability is something that needs to be addressed from AWS team?</p>
<p>Thank you in advance,</p>
<p>Regards,<br>
Kostas</p>

---

## Post #2 by @pieper (2025-04-17 15:26 UTC)

<p>Hi - As it happens, yes, I did work with some folks at AWS a few years ago to make a prototype that worked well with AWS AHI with an abstraction that also works with standard DICOMweb in the Slicer DICOM database.</p>
<p>The key things this provides are async/parallel frame access and decompression plus virtualized access to large datasets (only the metadata is pulled onto your local machine and then image frames are pulled down on-demand.</p>
<p>We did enough of a proof of concept to show at RNSA but haven’t fully wrapped this up in a release version.  It would be great if someone wants to pick up on this.</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/pieper/DICOMLogic">
  <header class="source">

      <a href="https://github.com/pieper/DICOMLogic" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/40bde67ebc348dbd0d8a98f21164fcf5/pieper/DICOMLogic" class="thumbnail">

  <h3><a href="https://github.com/pieper/DICOMLogic" target="_blank" rel="noopener">GitHub - pieper/DICOMLogic: Essential logic for working with dicom data.</a></h3>

    <p><span class="github-repo-description">Essential logic for working with dicom data.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @ksidis (2025-09-25 09:09 UTC)

<p>Hi again. Could we maybe revisit this, since now AWS AHI has full DICOMweb support?</p>

---

## Post #4 by @pieper (2025-09-25 12:19 UTC)

<p>It would be great if someone can pick this up.  It’s not currently a funded priority for me.</p>
<p>But I will say that the code I linked above does support Google’s DICOMweb so hopefully the AWS implementation would be quite similar and would simplify things a bit.</p>

---

## Post #5 by @ksidis (2025-11-20 13:46 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> is there any plan to include AWS HealthImaging in the <a href="https://github.com/lassoan/SlicerDICOMwebBrowser" rel="noopener nofollow ugc">DICOMwebBrowser extension</a>? After having a quick look at the repo I’ve noticed that it currently supports GoogleCloud.</p>

---
