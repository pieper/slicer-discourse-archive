# Syntax error in custom slicer build

**Topic ID**: 23184
**Date**: 2022-04-28
**URL**: https://discourse.slicer.org/t/syntax-error-in-custom-slicer-build/23184

---

## Post #1 by @wrx15113330303 (2022-04-28 18:05 UTC)

<p>Hi there, can anyone help me with this problem?<br>
I am following the instruction in SlicerCAT(<a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a>) to build a custom slicer application. I didn’t modify anything in the source code, but I have these syntax errors reported.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8af7482164ca0f81cbb14579779ca9e71c45720a.png" data-download-href="/uploads/short-url/jPlGL0woEUjdEfvdMvv8zKu4Lay.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8af7482164ca0f81cbb14579779ca9e71c45720a_2_690x358.png" alt="image" data-base62-sha1="jPlGL0woEUjdEfvdMvv8zKu4Lay" width="690" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8af7482164ca0f81cbb14579779ca9e71c45720a_2_690x358.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8af7482164ca0f81cbb14579779ca9e71c45720a_2_1035x537.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8af7482164ca0f81cbb14579779ca9e71c45720a_2_1380x716.png 2x" data-dominant-color="2B2B2E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2144×1113 303 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I am using VS 2022, CMake 3.23.1, Git 2.35.1, Slicer 4.13</p>

---

## Post #2 by @cpinter (2022-04-29 10:33 UTC)

<p>Without speaking Chinese I can’t make heads or tails from these errors. Since I assume you understand what it ways I suggest starting to fix the top one and I’d ignore the highlighted CMake one for now.</p>

---

## Post #3 by @wrx15113330303 (2022-04-29 10:44 UTC)

<p>I have figured out the reason. The custom name can not contain characters like ‘-’ etc.</p>

---
