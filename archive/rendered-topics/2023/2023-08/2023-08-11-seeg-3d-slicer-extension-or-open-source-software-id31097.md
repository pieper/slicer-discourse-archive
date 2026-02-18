# SEEG 3D slicer extension or open-source software

**Topic ID**: 31097
**Date**: 2023-08-11
**URL**: https://discourse.slicer.org/t/seeg-3d-slicer-extension-or-open-source-software/31097

---

## Post #1 by @Gonzalo_Rojas_Costa (2023-08-11 04:52 UTC)

<p>Hi:</p>
<p>Any SEEG 3D Slicer extension or open-source software? I need an extension or software to place the SEEG electrodes in an MRI image and brain mesh model.</p>
<p>Sincerely,</p>
<p>Gonzalo Rojas Costa</p>

---

## Post #2 by @simonoxen (2023-08-11 07:44 UTC)

<p>Hi,</p>
<p>Lead-DBS supports seeg up to some extent, you can see supported electrode models here <a href="https://github.com/netstim/leaddbs/tree/develop/templates/electrode_models" rel="noopener nofollow ugc">https://github.com/netstim/leaddbs/tree/develop/templates/electrode_models</a></p>
<p>MMVT is another option for seeg/ecog <a href="https://mmvt.mgh.harvard.edu/" rel="noopener nofollow ugc">https://mmvt.mgh.harvard.edu/</a>. Related recent publication: <a href="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0287921" class="inline-onebox" rel="noopener nofollow ugc">Modular pipeline for reconstruction and localization of implanted intracranial ECoG and sEEG electrodes</a></p>
<p>Not sure if <a class="mention" href="/u/greydon_gilmore">@Greydon_Gilmore</a> 's Trajectory Guide supports this <a href="https://github.com/greydongilmore/trajectoryGuideModules" class="inline-onebox" rel="noopener nofollow ugc">GitHub - greydongilmore/trajectoryGuideModules</a></p>
<p>Slicer would definitely be a great platform to further implement these features.</p>

---

## Post #3 by @Greydon_Gilmore (2023-08-15 23:55 UTC)

<p>Hi all,</p>
<p>Yes, trajectoryGudie does support SEEG. In fact, it supports any neurosurgical trajectory you want to plan/localize/VTA model (i.e. DBS, SEEG, tumor biopsy etc.).</p>
<p>Here is a sample of SEEG planning output in trajectoryGuide:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fc5ba8f64efa34de0ade9ffbabc93b4a42d69ed.jpeg" data-download-href="/uploads/short-url/fWMD809zqyqwqmoEjB3MzoTc7ZX.jpeg?dl=1" title="3d_transparent_anterior" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fc5ba8f64efa34de0ade9ffbabc93b4a42d69ed_2_690x443.jpeg" alt="3d_transparent_anterior" data-base62-sha1="fWMD809zqyqwqmoEjB3MzoTc7ZX" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fc5ba8f64efa34de0ade9ffbabc93b4a42d69ed_2_690x443.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fc5ba8f64efa34de0ade9ffbabc93b4a42d69ed_2_1035x664.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fc5ba8f64efa34de0ade9ffbabc93b4a42d69ed_2_1380x886.jpeg 2x" data-dominant-color="201F21"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d_transparent_anterior</span><span class="informations">1920×1233 80.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/153c5a0b20acc7a80a51ed8c069e9ef8aba27b09.jpeg" data-download-href="/uploads/short-url/31Rks1928R0Bj7SP2qnfAkUcrPz.jpeg?dl=1" title="3d_transparent" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/153c5a0b20acc7a80a51ed8c069e9ef8aba27b09_2_690x443.jpeg" alt="3d_transparent" data-base62-sha1="31Rks1928R0Bj7SP2qnfAkUcrPz" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/153c5a0b20acc7a80a51ed8c069e9ef8aba27b09_2_690x443.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/153c5a0b20acc7a80a51ed8c069e9ef8aba27b09_2_1035x664.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/153c5a0b20acc7a80a51ed8c069e9ef8aba27b09_2_1380x886.jpeg 2x" data-dominant-color="201F1F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d_transparent</span><span class="informations">1920×1233 78.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please note, I can provide limited support at this time for trouble-shooting. I will try my best. You can find documentation for my software tool here: <a href="https://trajectoryguide.greydongilmore.com/" rel="noopener nofollow ugc">https://trajectoryguide.greydongilmore.com/</a>.</p>
<p>Greydon</p>

---
