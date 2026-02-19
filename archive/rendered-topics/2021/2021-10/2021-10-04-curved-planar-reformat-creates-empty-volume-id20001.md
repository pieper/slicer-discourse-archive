---
topic_id: 20001
title: "Curved Planar Reformat Creates Empty Volume"
date: 2021-10-04
url: https://discourse.slicer.org/t/20001
---

# Curved planar reformat creates empty volume?

**Topic ID**: 20001
**Date**: 2021-10-04
**URL**: https://discourse.slicer.org/t/curved-planar-reformat-creates-empty-volume/20001

---

## Post #1 by @rsulser (2021-10-04 19:36 UTC)

<p>Operating system: Windows 10 (20H2)<br>
Slicer version: 4.11.20210226<br>
Expected behavior: Curved planar reformat creates reformatted volume file<br>
Actual behavior: Volume file created but appears to be empty (with no density curves recovered)</p>
<p>Hello all -</p>
<p>Wondering if anyone with experience with curved planar reformat might be able to lend a hand here?</p>
<p>I seem to be unable to reformat along the centerline of an (admittedly rough) model of a nerve trackway. I’ve extracted a centerline through the “Extract Centerline” tool and all appears to be in order, but the resulting volume (hopefully attached in screenshots and in MOBI <a href="https://www.dropbox.com/sh/u9lwrl39h1iakp1/AABEPh9Qru9HNBa-ugqPGIPDa?dl=0" rel="noopener nofollow ugc">at this link</a>) appears to be empty, and unless I’m missing something, inspection of the histogram yields no discernable curve.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40beaa24958a323b832be46b69d90dd184643781.png" data-download-href="/uploads/short-url/9eL3q5FFVFg6fIPQXxAVmC2l6jn.png?dl=1" title="Screenshot 2021-10-04 144626" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40beaa24958a323b832be46b69d90dd184643781_2_690x370.png" alt="Screenshot 2021-10-04 144626" data-base62-sha1="9eL3q5FFVFg6fIPQXxAVmC2l6jn" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40beaa24958a323b832be46b69d90dd184643781_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40beaa24958a323b832be46b69d90dd184643781_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40beaa24958a323b832be46b69d90dd184643781_2_1380x740.png 2x" data-dominant-color="87868A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-10-04 144626</span><span class="informations">1920×1030 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/485e9a891f003ba9328c4d30c193521462bb0691.png" data-download-href="/uploads/short-url/akd42TbjCpySwSeEGd6wYYSQXux.png?dl=1" title="Screenshot 2021-10-04 144540" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/485e9a891f003ba9328c4d30c193521462bb0691_2_690x370.png" alt="Screenshot 2021-10-04 144540" data-base62-sha1="akd42TbjCpySwSeEGd6wYYSQXux" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/485e9a891f003ba9328c4d30c193521462bb0691_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/485e9a891f003ba9328c4d30c193521462bb0691_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/485e9a891f003ba9328c4d30c193521462bb0691_2_1380x740.png 2x" data-dominant-color="8B8B8E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-10-04 144540</span><span class="informations">1920×1030 94.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/480e2a1ca815e783becdc34b8e824ff0b33ac3c6.jpeg" data-download-href="/uploads/short-url/ahqIXz3DU1n6fFKVOmGqucVhqyq.jpeg?dl=1" title="Screenshot 2021-10-04 144431" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/480e2a1ca815e783becdc34b8e824ff0b33ac3c6_2_690x370.jpeg" alt="Screenshot 2021-10-04 144431" data-base62-sha1="ahqIXz3DU1n6fFKVOmGqucVhqyq" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/480e2a1ca815e783becdc34b8e824ff0b33ac3c6_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/480e2a1ca815e783becdc34b8e824ff0b33ac3c6_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/480e2a1ca815e783becdc34b8e824ff0b33ac3c6_2_1380x740.jpeg 2x" data-dominant-color="96969A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-10-04 144431</span><span class="informations">1920×1030 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve used this extension in other projects with success, and I’m not sure what might make this volume and/or structure different. Perhaps the curve is too complex, or there’s some option I’m forgetting to switch? Any help in troubleshooting would be greatly appreciated!</p>

---

## Post #2 by @lassoan (2021-10-05 18:29 UTC)

<p>Thanks for reporting this. The problem is that the input volume is transformed and Curved Planar Reformat module ignores parent transform of the input volume, see:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/PerkLab/SlicerSandbox/issues/9">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerSandbox/issues/9" target="_blank" rel="noopener">github.com/PerkLab/SlicerSandbox</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/PerkLab/SlicerSandbox/issues/9" target="_blank" rel="noopener">Make CurvedPlanarReformat module take into accound parent transform of volume</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-03-17" data-time="14:29:42" data-timezone="UTC">02:29PM - 17 Mar 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">See https://discourse.slicer.org/t/curved-planar-reformat-module-results-inaccur<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ate/16590</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The easiest workaround is to harden the transform on the volume.</p>

---

## Post #3 by @rsulser (2021-10-05 20:25 UTC)

<p>Ah, thanks for the help! I hardened the transform and the Planar Reformat worked just fine. I will keep this in mind for future uses of the module!</p>

---

## Post #4 by @lassoan (2021-10-05 20:28 UTC)

<p>Great, thanks for the feedback.</p>
<p>We’ll fix this limitation of the module soon.</p>

---
