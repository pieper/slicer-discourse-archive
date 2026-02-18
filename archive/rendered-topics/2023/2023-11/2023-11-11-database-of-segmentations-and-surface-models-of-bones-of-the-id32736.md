# Database of segmentations and surface models of bones of the entire lower body created from cadaver CT scans

**Topic ID**: 32736
**Date**: 2023-11-11
**URL**: https://discourse.slicer.org/t/database-of-segmentations-and-surface-models-of-bones-of-the-entire-lower-body-created-from-cadaver-ct-scans/32736

---

## Post #1 by @MCM-Fischer (2023-11-11 09:36 UTC)

<p>Hello everybody</p>
<p>I’ve published a database of full lower body bone models. The segmentations were performed with 3D Slicer. More information can be found in:</p>
<blockquote>
<p>Fischer, M.C.M. Database of segmentations and surface models of bones of the entire lower body created from cadaver CT scans. <em>Sci Data</em> <strong>10</strong>, 763 (2023). <a href="https://doi.org/10.1038/s41597-023-02669-z" rel="noopener nofollow ugc">https://doi.org/10.1038/s41597-023-02669-z</a></p>
</blockquote>
<p>See also:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/MCM-Fischer/VSDFullBodyBoneModels">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/MCM-Fischer/VSDFullBodyBoneModels" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/9190a39c1a2c5d5386da721d2bca7158fd0e12bf53169f84f08ade01d51ea00c/MCM-Fischer/VSDFullBodyBoneModels" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/MCM-Fischer/VSDFullBodyBoneModels" target="_blank" rel="noopener nofollow ugc">GitHub - MCM-Fischer/VSDFullBodyBoneModels: Surface models of bones created...</a></h3>

  <p>Surface models of bones created from CT datasets of the open source VSDFullBody database. - GitHub - MCM-Fischer/VSDFullBodyBoneModels: Surface models of bones created from CT datasets of the open ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>          <a href="https://user-images.githubusercontent.com/43516130/265526827-b1e706f4-8b43-42d6-b249-1633aaa28381.JPG" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://user-images.githubusercontent.com/43516130/265526827-b1e706f4-8b43-42d6-b249-1633aaa28381.JPG" width="" height="">
          </a>
</p>
<p>Kind regards</p>

---

## Post #2 by @lassoan (2023-11-13 06:32 UTC)

<p>Thanks for sharing!</p>
<p>For my curiousity, I’ve tried fully automatic segmentation of these CTs using <a href="https://github.com/lassoan/SlicerTotalSegmentator">TotalSegmentator extension</a>. In a few minutes, it provided results that looked similar to yours, except that yours have a few segments divided into smaller regions.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cdac2522fadbf8b405314ed6acac0c02f01352e.jpeg" data-download-href="/uploads/short-url/dfqCdw6QMj0L90ri6OWmVjn1Q4u.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cdac2522fadbf8b405314ed6acac0c02f01352e_2_629x500.jpeg" alt="image" data-base62-sha1="dfqCdw6QMj0L90ri6OWmVjn1Q4u" width="629" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cdac2522fadbf8b405314ed6acac0c02f01352e_2_629x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cdac2522fadbf8b405314ed6acac0c02f01352e_2_943x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cdac2522fadbf8b405314ed6acac0c02f01352e_2_1258x1000.jpeg 2x" data-dominant-color="9A9CC2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1646×1307 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @MCM-Fischer (2024-02-09 17:23 UTC)

<p>Hi Andras</p>
<p>That’s awesome! This was actually part of the idea of the publication to provide some test (and additional training) data for AI segmentation models.</p>
<p>I had to buy a new computer first to test TotalSegmentator (ThinkPad P1 i9 RTX 3080 Ti 16 GB VRAM 64 GB RAM).<br>
I’ve tried it with the volume SMIR.Lower_limb.051Y.F.CT.168.nrrd from this data set <a href="https://zenodo.org/records/8302449/files/006.zip?download=1" rel="noopener nofollow ugc">https://zenodo.org/records/8302449/files/006.zip?download=1</a></p>
<p>However, TotalSegmentator only segmented the volume down to the knees. The bones of the shanks and feet are missing.<br>
Do you maybe have an idea what could be the reason?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9b9ad26040ba83a06e6a2b87fc97584cd5f9efc.png" data-download-href="/uploads/short-url/odsv8KhkRHxpleFYgPwD35wENMU.png?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9b9ad26040ba83a06e6a2b87fc97584cd5f9efc_2_513x500.png" alt="grafik" data-base62-sha1="odsv8KhkRHxpleFYgPwD35wENMU" width="513" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9b9ad26040ba83a06e6a2b87fc97584cd5f9efc_2_513x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9b9ad26040ba83a06e6a2b87fc97584cd5f9efc_2_769x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9b9ad26040ba83a06e6a2b87fc97584cd5f9efc.png 2x" data-dominant-color="A9A7B1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">959×933 193 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Kind regards</p>

---

## Post #4 by @lassoan (2024-02-10 18:40 UTC)

<p>For lower leg segmentation you need to get an academic or commercial license from <a href="https://github.com/wasserth/TotalSegmentator?tab=readme-ov-file#subtasks">here</a>.</p>

---
