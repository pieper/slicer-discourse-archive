# Slicer Elastix extension not available for newest Slicer 13.0. 2021.03.19

**Topic ID**: 16688
**Date**: 2021-03-22
**URL**: https://discourse.slicer.org/t/slicer-elastix-extension-not-available-for-newest-slicer-13-0-2021-03-19/16688

---

## Post #1 by @PalkoD (2021-03-22 11:23 UTC)

<p>Dear All!</p>
<p>I just downloaded the newest version of slicer, and I was trying to restore extensions, and few of the extensions including Elastix, are unfortunately not available for the newest version. This is very unfortunate, because Elastix is on of the key elements of my work. Does anyone know if it is going to available, and when.</p>
<p>Thank you for your answer</p>
<p>I attach the screenshot of the extension manager.</p>
<p>Greetings Daniel Palkovics</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4ad442fc02d519acc68f031cad0d551fcc22bfaf.png" data-download-href="/uploads/short-url/aFY6hsSYwtT3ySgD80AITJol7j1.png?dl=1" title="Screen Shot 2021-03-21 at 13.04.53" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ad442fc02d519acc68f031cad0d551fcc22bfaf_2_690x390.png" alt="Screen Shot 2021-03-21 at 13.04.53" data-base62-sha1="aFY6hsSYwtT3ySgD80AITJol7j1" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ad442fc02d519acc68f031cad0d551fcc22bfaf_2_690x390.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ad442fc02d519acc68f031cad0d551fcc22bfaf_2_1035x585.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ad442fc02d519acc68f031cad0d551fcc22bfaf_2_1380x780.png 2x" data-dominant-color="252525"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-03-21 at 13.04.53</span><span class="informations">1988×1125 197 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @cpinter (2021-03-22 11:25 UTC)

<p>After a quick look at the <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=elastix">dashboard</a> the extension fails to build on all platforms. Maybe it is due to the updated ITK?</p>

---

## Post #3 by @lassoan (2021-03-25 13:25 UTC)

<p>I’ve fixed the build error by updating to latest Elastix library version. SlicerElastix extension is now available for the latest Slicer Preview Release.</p>

---
