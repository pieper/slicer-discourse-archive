# Combine Multiple Orientations / Volumes in Axial View

**Topic ID**: 37073
**Date**: 2024-06-27
**URL**: https://discourse.slicer.org/t/combine-multiple-orientations-volumes-in-axial-view/37073

---

## Post #1 by @waterbottle (2024-06-27 17:33 UTC)

<p>Hi all,</p>
<p>Still new to slicer. I am working on MRIs in Slicer. Some MRIs load in as one big volume which works for my needs, however others come split into “imageOrientationPatient X” where X = some number, typically from 1-6. I’d like to combine all of these different orientations which are all in the Axial view so that I can use TotalSegmentor on them. Please see below image to see what I mean:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/402ad9c6927ee06fc787d1447f2bfaf51080de59.png" data-download-href="/uploads/short-url/99EmE8AhUeV2lMpPmOxCCxpKyGB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/402ad9c6927ee06fc787d1447f2bfaf51080de59_2_690x122.png" alt="image" data-base62-sha1="99EmE8AhUeV2lMpPmOxCCxpKyGB" width="690" height="122" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/402ad9c6927ee06fc787d1447f2bfaf51080de59_2_690x122.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/402ad9c6927ee06fc787d1447f2bfaf51080de59_2_1035x183.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/402ad9c6927ee06fc787d1447f2bfaf51080de59_2_1380x244.png 2x" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2044×362 29.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’m not totally sure if this is what the Stitch Volumes module is for, but I tried that and get the below error. Really appreciate any help yall can provide</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2ebc450b93efb13d4e94e183543cfd3b8823b90.png" data-download-href="/uploads/short-url/rOlKXyjALegVqruLZ9Qtld7D0xW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2ebc450b93efb13d4e94e183543cfd3b8823b90_2_690x214.png" alt="image" data-base62-sha1="rOlKXyjALegVqruLZ9Qtld7D0xW" width="690" height="214" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2ebc450b93efb13d4e94e183543cfd3b8823b90_2_690x214.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2ebc450b93efb13d4e94e183543cfd3b8823b90.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2ebc450b93efb13d4e94e183543cfd3b8823b90.png 2x" data-dominant-color="DDDBDB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">822×256 15.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you so much!</p>

---

## Post #2 by @waterbottle (2024-07-08 16:33 UTC)

<p>Hi all, if anyone reads this later, please make sure you read <a href="https://github.com/PerkLab/SlicerSandbox?tab=readme-ov-file#how-to-use-1" rel="noopener nofollow ugc">this in the stitch modules documentation,</a> it solved my problems!</p>

---
