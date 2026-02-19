---
topic_id: 26197
title: "Slicersalt 4 0 1 Summary Highlights And Changelog"
date: 2022-11-11
url: https://discourse.slicer.org/t/26197
---

# SlicerSALT 4.0.1: Summary, Highlights and Changelog

**Topic ID**: 26197
**Date**: 2022-11-11
**URL**: https://discourse.slicer.org/t/slicersalt-4-0-1-summary-highlights-and-changelog/26197

---

## Post #1 by @bpaniagua (2022-11-11 15:09 UTC)

<p>The SlicerSALT team is proud to announce that version 4.0.1 is <a href="http://salt.slicer.org/download">now available for download</a>. This release introduces new features as well as bug fixes for better performance and stability. The development of SlicerSALT is supported by the NIH National Institute of Biomedical Imaging Bioengineering <a href="https://reporter.nih.gov/search/BJkO3JrNdUeE1qvjz2dWxA/project-details/10426508">R56EB021391</a> and <a href="https://reporter.nih.gov/search/lG6PR605E0efYbG9_QKCGw/project-details/10363506">R01EB021391</a> (Shape Analysis Toolbox: From medical images to quantitative insights of anatomy).</p>
<p><img src="https://lh6.googleusercontent.com/S-UVHMGKP5eSpmxQ1otbUhw6aoGvk3bJGmYyiwHoAnKYEzsXjc544ORMXffxZLruQbOf0wehQfFzCtciQyipn25GFhoE5-lKMCO9CScAxP1GTw2WUIPh4lGVxp2PkmmIwaFxUH4sOM-Tw5dTCG0QpgTQ7uJDZex1jgckI9-ytUkDqnMicca-SXbewSN-Jw" alt="" width="624" height="352" role="presentation"></p>
<p>SlicerSALT 4.0.1 includes a new extension, SlicerPipelines, that allows the creation and use of simple modules in 3D Slicer without coding. This extension was developed as part of SlicerSALT and has been added to the Slicer Extensions Index.</p>
<h1><a name="p-85967-changelog-1" class="anchor" href="#p-85967-changelog-1" aria-label="Heading link"></a>Changelog</h1>
<p>Features</p>
<p><a href="https://www.kitware.com/introducing-slicerpipelines-a-coding-free-way-to-create-simple-modules-in-3d-slicer/">Slicer Pipelines</a></p>
<p>Skeletal representations</p>
<p><a href="https://www.kitware.com/slicersalt-shapevariationanalyzer-for-skeletal-representations/">Refactored functionality</a></p>
<p><a href="https://www.kitware.com/slicersalt-shapevariationanalyzer-for-skeletal-representations/">Shape Variation Analyzer</a> (Composite Principal Nested Spheres)</p>
<p>SlicerDWD extension</p>
<p>DentalModelSeg extension added</p>
<p>Updated tutorials</p>
<h2><a name="p-85967-fixes-2" class="anchor" href="#p-85967-fixes-2" aria-label="Heading link"></a>Fixes</h2>
<p>Updates to the SlicerSALT to be compatible with Slicer 5.0</p>
<p>Updates to the Covariance Significance Testing layout</p>
<p>Crash fixes and stability</p>
<p>Bug fixes for Population based shape analysis and SPHARM-PDM</p>
<p>Python syntax warnings</p>
<p>Check for SPV instead of Gaussian Blur module</p>
<p>Update tooltips for RigidAlignmentModule</p>
<p>Bug fixes for sample data for S-rep and tutorials (does not auto populate UI)</p>
<p>Updates to splash screen and logos</p>
<p>Bug fixes to solve stability issues on Windows</p>
<p>Fix use of deprecated unencrypted git protocol</p>
<p>Shape Variation Analyzer usability improvements</p>
<p>New significance figs, fix shaking sliders, use std for sliders and projection</p>
<p>Transform model to LPS coordinate by default</p>
<h1><a name="p-85967-acknowledgements-3" class="anchor" href="#p-85967-acknowledgements-3" aria-label="Heading link"></a>Acknowledgements</h1>
<ul>
<li>UNC
<ul>
<li>Martin Styner &amp; lab</li>
<li>Steve Pizer &amp; lab</li>
<li>Tengfei Li</li>
</ul>
</li>
<li>NYU Tandon School of Engineering
<ul>
<li>Guido Gerig</li>
</ul>
</li>
<li>Kitware
<ul>
<li>Beatriz Paniagua</li>
<li>Jared Vicory</li>
<li>Connor Bowley</li>
<li>Sam Horvath</li>
<li>Jean-Christophe Fillion-Robin</li>
<li>James Fishbaugh</li>
<li>Ye Han</li>
<li>David Allemang</li>
</ul>
</li>
</ul>

---

## Post #2 by @muratmaga (2022-11-11 17:43 UTC)

<p><a class="mention" href="/u/bpaniagua">@bpaniagua</a><br>
I just downloaded the package and the link for tutorials in a help/welcome module returns a 404 URL not found (specifically <a href="https://salt.slicer.org/docs/" class="inline-onebox">Redirecting…</a>)</p>
<p>FYI.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e1bade045b5ffade2e7568b82b9944dd9240cc0.png" data-download-href="/uploads/short-url/20NZc3aw4mdFefuikmEjN4lqOC4.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e1bade045b5ffade2e7568b82b9944dd9240cc0_2_500x500.png" alt="image" data-base62-sha1="20NZc3aw4mdFefuikmEjN4lqOC4" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e1bade045b5ffade2e7568b82b9944dd9240cc0_2_500x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e1bade045b5ffade2e7568b82b9944dd9240cc0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e1bade045b5ffade2e7568b82b9944dd9240cc0.png 2x" data-dominant-color="D9DDE2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">628×628 41.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @bpaniagua (2022-11-11 18:10 UTC)

<p>Nice catch! Reported</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Kitware/SlicerSALT/issues/288">
  <header class="source">

      <a href="https://github.com/Kitware/SlicerSALT/issues/288" target="_blank" rel="noopener">github.com/Kitware/SlicerSALT</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Kitware/SlicerSALT/issues/288" target="_blank" rel="noopener">Modify documentation URL</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-11-11" data-time="18:10:00" data-timezone="UTC">06:10PM - 11 Nov 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/bpaniagua" target="_blank" rel="noopener">
          <img alt="bpaniagua" src="https://avatars.githubusercontent.com/u/2599368?v=4" class="onebox-avatar-inline" width="20" height="20">
          bpaniagua
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">https://discourse.slicer.org/t/slicersalt-4-0-1-summary-highlights-and-changelog<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">/26197/2


Change salt.slicer.org/docs for https://salt.slicer.org/documentation/

Thank you for reporting, Murat.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @bpaniagua (2022-11-11 18:57 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> this has <a href="https://github.com/Kitware/SlicerSALT/issues/288">been fixed</a>.</p>

---

## Post #5 by @lili-yu22 (2024-12-21 05:45 UTC)

<p>when I open a mesh.then open it’s fiducial in the shapepopulationviewer , the slicersalt 5.0 crash.how I can put the fiducial on the mesh in the shapepopulationviewer like the picture2.please help me<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f85d86e5a4855b051aa1c6c5ec6be9f0bc77116c.jpeg" data-download-href="/uploads/short-url/zr8Nb8qjCQgjxK7kQ1Em401BBgg.jpeg?dl=1" title="IMG_20241220_155543_edit_8092433669597" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f85d86e5a4855b051aa1c6c5ec6be9f0bc77116c_2_384x500.jpeg" alt="IMG_20241220_155543_edit_8092433669597" data-base62-sha1="zr8Nb8qjCQgjxK7kQ1Em401BBgg" width="384" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f85d86e5a4855b051aa1c6c5ec6be9f0bc77116c_2_384x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f85d86e5a4855b051aa1c6c5ec6be9f0bc77116c_2_576x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f85d86e5a4855b051aa1c6c5ec6be9f0bc77116c_2_768x1000.jpeg 2x" data-dominant-color="B7B9B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20241220_155543_edit_8092433669597</span><span class="informations">1920×2498 321 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5dc3bd8d5e802e3ae1afc5166cf4b61a011462ab.jpeg" data-download-href="/uploads/short-url/dntM9EZp7SmipvPReYz4hw0bHcL.jpeg?dl=1" title="Screenshot_20241219_151735_edit_56383804812228" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5dc3bd8d5e802e3ae1afc5166cf4b61a011462ab_2_690x493.jpeg" alt="Screenshot_20241219_151735_edit_56383804812228" data-base62-sha1="dntM9EZp7SmipvPReYz4hw0bHcL" width="690" height="493" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5dc3bd8d5e802e3ae1afc5166cf4b61a011462ab_2_690x493.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5dc3bd8d5e802e3ae1afc5166cf4b61a011462ab_2_1035x739.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5dc3bd8d5e802e3ae1afc5166cf4b61a011462ab_2_1380x986.jpeg 2x" data-dominant-color="ACBCB7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20241219_151735_edit_56383804812228</span><span class="informations">1600×1144 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
