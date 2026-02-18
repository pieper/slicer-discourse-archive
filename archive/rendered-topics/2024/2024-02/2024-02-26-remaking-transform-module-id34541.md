# Remaking transform module

**Topic ID**: 34541
**Date**: 2024-02-26
**URL**: https://discourse.slicer.org/t/remaking-transform-module/34541

---

## Post #1 by @mohammed_alshakhas (2024-02-26 12:27 UTC)

<p>i wish the transform model would adopt the same improvement in interacting with markups as in the screenshot. The way transform module operation is not helpful at all.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89295c7ea236cc3640f8a2b1212f6be59ad01348.jpeg" data-download-href="/uploads/short-url/jzo1PWULyFIkCvCSusARUFDAmSI.jpeg?dl=1" title="Screenshot 2024-02-26 at 15.25.47" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89295c7ea236cc3640f8a2b1212f6be59ad01348_2_690x448.jpeg" alt="Screenshot 2024-02-26 at 15.25.47" data-base62-sha1="jzo1PWULyFIkCvCSusARUFDAmSI" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89295c7ea236cc3640f8a2b1212f6be59ad01348_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89295c7ea236cc3640f8a2b1212f6be59ad01348_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89295c7ea236cc3640f8a2b1212f6be59ad01348_2_1380x896.jpeg 2x" data-dominant-color="9F9D9E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-02-26 at 15.25.47</span><span class="informations">1920×1247 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-02-26 13:59 UTC)

<p>Transforms module was already very helpful as it was - probably you meant that in your specific workflow you would also want to have visual editing of transforms. The good news is that <a class="mention" href="/u/sunderlandkyl">@sunderlandkyl</a> has already implemented it. You can edit transforms (and therefore move/rotate/scale any node) using the same handles as you use for moving around markups. We just wanted a few more touchups before announcing the feature, but it is already available in recent Slicer Preview Releases.</p>

---

## Post #3 by @mohammed_alshakhas (2024-02-27 16:00 UTC)

<p>of course, that is what I meant.  i can only speak for my purposes<br>
my main issues with it were<br>
1 rotational movement was and still is confusing to me, axial rotational movement for example ends up in a sagittal direction and such.<br>
2 if I needed to modify a linear transform it would go back to the initial, not from the last position. which I wouldn’t say I liked to deal with. Sometimes I need to tweak the transformation a bit. but I had to repeat the whole transformation. for my purposes, it’s not a simple process to get position to where I want since I do complex head positioning<br>
3 some rotation movement has an origin that’s not at  center of volume</p>

---
