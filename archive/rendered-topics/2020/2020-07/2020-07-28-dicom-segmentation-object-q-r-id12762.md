---
topic_id: 12762
title: "Dicom Segmentation Object Q R"
date: 2020-07-28
url: https://discourse.slicer.org/t/12762
---

# Dicom segmentation object Q/R

**Topic ID**: 12762
**Date**: 2020-07-28
**URL**: https://discourse.slicer.org/t/dicom-segmentation-object-q-r/12762

---

## Post #1 by @Krishna_Nanda (2020-07-28 20:05 UTC)

<p>Hello,</p>
<p>We have setup the 3D Slicer dicom browser to be able to Q/R into a vendor software. The query shows all the series, including a dicom segmentation object (modality SEG). The retrieve is successful in pulling all other series except dicom seg. We were expecting the dicom seg to behave like other dicom series with regards to Q/R. We were wondering if there is any specific function that needs to be enabled to make this work?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2020-07-28 20:24 UTC)

<p>That’s interesting - glad you were able to get the rest working and I agree it’s odd the SEG wouldn’t come over.  I can’t think of anything in the Slicer/ctk dicom networking layer that would even care what kind of instance it is.</p>
<p>Can you confirm that it’s not actually in the database and it’s just not being loaded correctly?  You would need the Quantitative Reporting extension installed to load.  Can you load it if you download a different way?</p>
<p>Another thing to try would be using the dcmtk command line tools to CGET the instance and see if it works.  I know some dimse implementation need to be configured to allow storage of certain SOP classes, and maybe they also need to be configured to allow retrieval too.</p>

---

## Post #3 by @lassoan (2021-11-02 12:22 UTC)

<p>Maybe the presentation contexts needs some adjustment, similarly to how the configuration had to be tuned for fixing sending of DICOM segmentation objects:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/21f8ba46beb67ae169387dd94237b0d7f8087302">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/21f8ba46beb67ae169387dd94237b0d7f8087302" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/21f8ba46beb67ae169387dd94237b0d7f8087302" target="_blank" rel="noopener">ENH: Add custom DICOM send configuration</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2021-06-14" data-time="21:15:53" data-timezone="UTC">09:15PM - 14 Jun 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/robertsoakes" target="_blank" rel="noopener">
          <img alt="robertsoakes" src="https://avatars.githubusercontent.com/u/3779876?v=4" class="onebox-avatar-inline" width="20" height="20">
          robertsoakes
        </a>
      </div>

      <div class="lines" title="changed 3 files with 121 additions and 12 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/21f8ba46beb67ae169387dd94237b0d7f8087302" target="_blank" rel="noopener">
          <span class="added">+121</span>
          <span class="removed">-12</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The default configuration provided with the DCMTK dicomscu program used to send <span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/21f8ba46beb67ae169387dd94237b0d7f8087302" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">data from Slicer does not allow the transfer of DICOM-SEG. This patch provides:
- an alternative configuration that includes the needed presentation context UID needed for DICOM-SEG files to be sent using DICOM and DICOMweb (using dicomscu)
- retry logic that first attempts to transfer the DCM instance using the standard configuration and (if that fails) will attempt a second transfer using the fallback configuration</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
