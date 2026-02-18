# Quantification based on centerline curve or centerline model?

**Topic ID**: 25676
**Date**: 2022-10-13
**URL**: https://discourse.slicer.org/t/quantification-based-on-centerline-curve-or-centerline-model/25676

---

## Post #1 by @JBierens (2022-10-13 11:43 UTC)

<p>I am wondering if the Centerline quantification table is based on the properties of the centerline model or centerline curves. Sometimes when I extract the centerline, I only get one centerline curve, that is only covering a small part of the model. Other times I get multiple centerline curves that cover the full centerline model. Also, what could be a reason I only get one centerline curve sometimes?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca090cd418a6f023e0b2f2e1f78ebbe435e33d59.png" data-download-href="/uploads/short-url/sPhQ0mFLX01n9Or9rio5kcQALix.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca090cd418a6f023e0b2f2e1f78ebbe435e33d59_2_690x388.png" alt="image" data-base62-sha1="sPhQ0mFLX01n9Or9rio5kcQALix" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca090cd418a6f023e0b2f2e1f78ebbe435e33d59_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca090cd418a6f023e0b2f2e1f78ebbe435e33d59_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca090cd418a6f023e0b2f2e1f78ebbe435e33d59_2_1380x776.png 2x" data-dominant-color="BABDDD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 322 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7128d7082658d2e406f6b44821bb9c225e92a42f.png" data-download-href="/uploads/short-url/g93s6Pgfy7Wq0xHd037kOglj2J9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7128d7082658d2e406f6b44821bb9c225e92a42f_2_690x388.png" alt="image" data-base62-sha1="g93s6Pgfy7Wq0xHd037kOglj2J9" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7128d7082658d2e406f6b44821bb9c225e92a42f_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7128d7082658d2e406f6b44821bb9c225e92a42f_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7128d7082658d2e406f6b44821bb9c225e92a42f_2_1380x776.png 2x" data-dominant-color="BCC0DF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @JBierens (2022-10-18 11:18 UTC)

<p>Could someone please help me?</p>

---

## Post #3 by @JBierens (2022-10-18 11:41 UTC)

<p>Ive understood by now that the geometrical properties are computed for each branch, so I think that means that the CellIDs in the table represent every centerline curve (can someone please confirm this?).</p>
<p>Still I am wondering why I get a table with multiple CellID lines while I only get one centerline curve sometimes. Does someone know why?</p>

---

## Post #4 by @lassoan (2022-10-18 16:32 UTC)

<p>To create curves, we need to interpret the list of branches in the centerline tree. This is implemented by using vtkvmtkCenterlineBranchExtractor followed by vtkvmtkMergeCenterlines - see details <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/913e0f9a7a4a085b80d877ff3730e98374b9ee98/ExtractCenterline/ExtractCenterline.py#L834-L856">here</a>. During this process, cells of the model are split and merged so that in the end one curve always corresponds to one branch.</p>

---

## Post #5 by @JBierens (2022-10-19 07:59 UTC)

<p>Thank you for your answer. Still, it is not clear to me why 3D slicer sometimes shows me only one curve, that does not cover my model (see the second image in the original post). Do you know why or how I can solve this?</p>

---
