# Fail to export PET dicom files

**Topic ID**: 22410
**Date**: 2022-03-09
**URL**: https://discourse.slicer.org/t/fail-to-export-pet-dicom-files/22410

---

## Post #1 by @collamaf (2022-03-09 14:03 UTC)

<p>Operating system: MacOs 12.2.1<br>
Slicer version: 4.13.0-2021-12-28<br>
Expected behavior: Being able to export a just imported PET Dicom series<br>
Actual behavior: “Creating DICOM files from scalar volume failed”</p>
<p>Hello everbody<br>
I tried the following:</p>
<ul>
<li>Open Slicer</li>
<li>Load e PET/CT dicom folder</li>
<li>I correctly see the PET image<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8ca29273a0e527e0a37b706f77f44cd02c1a3a39.png" data-download-href="/uploads/short-url/k479Byqww7ss0ilO0NLSvQPSroZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8ca29273a0e527e0a37b706f77f44cd02c1a3a39_2_690x324.png" alt="image" data-base62-sha1="k479Byqww7ss0ilO0NLSvQPSroZ" width="690" height="324" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8ca29273a0e527e0a37b706f77f44cd02c1a3a39_2_690x324.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8ca29273a0e527e0a37b706f77f44cd02c1a3a39_2_1035x486.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8ca29273a0e527e0a37b706f77f44cd02c1a3a39.png 2x" data-dominant-color="868180"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1179×554 91.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li>I want to export again in DICOM files that PET image, so I</li>
<li>Right click on it</li>
<li>“Export to DICOM”</li>
<li>Check (without touching anything) that “Modality” is set as “PT”</li>
<li>I get the error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5ff98fe6d0e72a71e2ba256e23755c3e255d3197.png" data-download-href="/uploads/short-url/dH22JmEk3v2h5qixdTSpI5jhzan.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5ff98fe6d0e72a71e2ba256e23755c3e255d3197_2_524x500.png" alt="image" data-base62-sha1="dH22JmEk3v2h5qixdTSpI5jhzan" width="524" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5ff98fe6d0e72a71e2ba256e23755c3e255d3197_2_524x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5ff98fe6d0e72a71e2ba256e23755c3e255d3197_2_786x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5ff98fe6d0e72a71e2ba256e23755c3e255d3197_2_1048x1000.png 2x" data-dominant-color="E9E8E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1340×1278 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
<p>The log gives the following:</p>
<p><code> PARSE ERROR: Argument: (--modality)              Value 'PT' does not meet constraint: CT|MR|NM|US|CR|SC</code></p>
<p>Does it mean that it is not possible to export PET Dicom files from Slicer?</p>
<p>I Tried to set the field to “NM”, and the export succeeds. But some metadata are lost in the output files, like the “RescaleSlope”…</p>
<p>Thanks in advance!</p>

---

## Post #2 by @Liu_Lance (2022-04-04 04:44 UTC)

<p>I run into the same problem, still can not find a solution. Have you sovled this?</p>

---

## Post #3 by @collamaf (2022-04-04 05:35 UTC)

<p>Hi<br>
No, no solution nor information found <img src="https://emoji.discourse-cdn.com/twitter/man_shrugging/2.png?v=12" title=":man_shrugging:t2:" class="emoji" alt=":man_shrugging:t2:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @collamaf (2022-07-25 09:22 UTC)

<p>Hi everybody<br>
Just to update that I find this issue also in Slicer 5.1.0-2022-07-06<br>
<a class="mention" href="/u/lassoan">@lassoan</a> Any idea? Thanks</p>

---
