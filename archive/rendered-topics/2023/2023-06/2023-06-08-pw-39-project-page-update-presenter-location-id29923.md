# PW 39 Project Page Update: Presenter Location

**Topic ID**: 29923
**Date**: 2023-06-08
**URL**: https://discourse.slicer.org/t/pw-39-project-page-update-presenter-location/29923

---

## Post #1 by @Sam_Horvath (2023-06-08 19:08 UTC)

<p>We have updated the project pages to include whether the presenter will be in-person or online:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f274bda1e7a94af376bc85b9a523dee6c5909a4e.png" data-download-href="/uploads/short-url/yARF9tztjzO0g2DVXvDhjW9Gm2W.png?dl=1" title="Screenshot 2023-06-08 11.32.08"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f274bda1e7a94af376bc85b9a523dee6c5909a4e_2_690x222.png" alt="Screenshot 2023-06-08 11.32.08" data-base62-sha1="yARF9tztjzO0g2DVXvDhjW9Gm2W" width="690" height="222" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f274bda1e7a94af376bc85b9a523dee6c5909a4e_2_690x222.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f274bda1e7a94af376bc85b9a523dee6c5909a4e_2_1035x333.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f274bda1e7a94af376bc85b9a523dee6c5909a4e_2_1380x444.png 2x" data-dominant-color="F3F5F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-06-08 11.32.08</span><span class="informations">1498×482 69.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>We have gone through and set the presenter location based on the registration status of the first key investigator, but please let us know / edit the page yourself if we got it wrong.</p>
<p>For new project pages, the Presenter Location can be set when creating the Project Issue, or edited directly when creating a project from the <a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/">template</a> (see code below).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e94221de04509b9e602289911e043cb46a71db47.png" data-download-href="/uploads/short-url/xhuWbde9z0HKCyh8RM63jX8fswL.png?dl=1" title="Screenshot 2023-06-08 13.40.55"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e94221de04509b9e602289911e043cb46a71db47_2_690x204.png" alt="Screenshot 2023-06-08 13.40.55" data-base62-sha1="xhuWbde9z0HKCyh8RM63jX8fswL" width="690" height="204" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e94221de04509b9e602289911e043cb46a71db47_2_690x204.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e94221de04509b9e602289911e043cb46a71db47_2_1035x306.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e94221de04509b9e602289911e043cb46a71db47.png 2x" data-dominant-color="13171D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-06-08 13.40.55</span><span class="informations">1246×369 17.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>For existing project pages, you can edit the <code>presenter_location</code> element at the top of the README.md file in your project folder (see example of the top section of the file below)</p>
<pre><code class="lang-auto">---
layout: pw39-project

permalink: /:path/

project_title: Write full project title here
category: Uncategorized
presenter_location: Online  #&lt;---- Update this line to In-person or Online!

key_investigators:
- name: Person Doe
  affiliation: University

- name: Person2 Doe2
  affiliation: University2
  country: Spain
---
</code></pre>
<p>If you need assistance with this, please feel free to create a Proposal issue on <a href="https://github.com/NA-MIC/ProjectWeek/issues">the GitHub Repo</a> to request that your page be updated.</p>

---
