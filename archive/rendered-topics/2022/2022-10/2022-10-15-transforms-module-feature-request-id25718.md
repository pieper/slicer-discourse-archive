# Transforms module feature request

**Topic ID**: 25718
**Date**: 2022-10-15
**URL**: https://discourse.slicer.org/t/transforms-module-feature-request/25718

---

## Post #1 by @muratmaga (2022-10-15 18:20 UTC)

<p>I have two request for Transforms module:</p>
<ol>
<li>While I can enable the visibility and 3D interaction of the transform in the Data module, I can’t seem to change the type of the interaction (rotate only, translate only, scale on/off) without having to go to the Transform module and expand the display option.</li>
<li>The widgets are not informative. I can’t visually tell whether I grabbed the little handle bar, or I am rotating or trying to scale.</li>
</ol>
<p>The markups interaction widgets, particularly ROI one is great and solves both problems. Is it possible to adopt that for the transform interactions as well?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cc805d7cd511157ba91d3de0076aa18505e10de.png" data-download-href="/uploads/short-url/deMtoQsOFHTVQXrsJXRRhZQwGZg.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cc805d7cd511157ba91d3de0076aa18505e10de_2_690x332.png" alt="image" data-base62-sha1="deMtoQsOFHTVQXrsJXRRhZQwGZg" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cc805d7cd511157ba91d3de0076aa18505e10de_2_690x332.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cc805d7cd511157ba91d3de0076aa18505e10de_2_1035x498.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cc805d7cd511157ba91d3de0076aa18505e10de.png 2x" data-dominant-color="C0C6D2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1278×615 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-10-15 18:40 UTC)

<p>Yes, we’ll need to update the transforms displayable manager to use the same style widgets as for markups, and not just in 3D but in 2D as well</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> as far as I remember you have already done some work on this - was it just moving the widget base classes for these widgets out of markups module, or you went further than that?</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Would you have resources (developer time or funding) to contribute to the implementation?</p>

---

## Post #3 by @smrolfe (2022-10-17 17:27 UTC)

<p>We may be able to contribute. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could you weigh in on what still needs to be done so we can see if it’s feasible?</p>

---

## Post #4 by @Sunderlandkyl (2022-10-17 20:34 UTC)

<p>I made an effort a year or so ago to refactor the transform widgets to support transforming arbitrary nodes through a new DisplayableManager in the MRML core.</p>
<p>It’s been a while since I’ve looked into it, let me take a look into the previous work and figure out a plan.</p>

---
