# Error when using reduced nrrd file

**Topic ID**: 23062
**Date**: 2022-04-20
**URL**: https://discourse.slicer.org/t/error-when-using-reduced-nrrd-file/23062

---

## Post #1 by @ekt (2022-04-20 23:47 UTC)

<p>I had a very large file (~4.4GB) so I used Fiji to reduce the number of images and bring the file size down to 1.5GB. Now when I try to load it into slicer the images don’t seem to have any width? They all show up in the red view but show nothing in the green view and show up as a line in the yellow view. Is this something that needs to be fixed in Fiji or Slicer? Or is there a better way to reduce my file size?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32bd13eaf986d3004879fd8c308355a8fb98f906.png" data-download-href="/uploads/short-url/7eQYbWEawrXNxTm7N6Hv8DWQBIG.png?dl=1" title="Screenshot 2022-04-20 164304" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32bd13eaf986d3004879fd8c308355a8fb98f906_2_690x373.png" alt="Screenshot 2022-04-20 164304" data-base62-sha1="7eQYbWEawrXNxTm7N6Hv8DWQBIG" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32bd13eaf986d3004879fd8c308355a8fb98f906_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32bd13eaf986d3004879fd8c308355a8fb98f906_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32bd13eaf986d3004879fd8c308355a8fb98f906_2_1380x746.png 2x" data-dominant-color="87879A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-04-20 164304</span><span class="informations">1920×1040 288 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2022-04-21 00:19 UTC)

<p>Probably Fiji didn’t set the spacing of the exported volume correctly. You can check if that’s the issue by going to volumes module and check image dimensions as well spacing.</p>
<p>Slicer has plenty of tools to down sample data, why are you using Fiji and complicating your workflow.</p>
<p>You can use the imagestacks module in SlicerMorph to import your data directly as reduced, if that’s what you want. Or you can import at full resolution and use crop volume to down sample.</p>

---
