# Fixing/Saving slice relations from the interactive slice intersection tool

**Topic ID**: 27585
**Date**: 2023-02-01
**URL**: https://discourse.slicer.org/t/fixing-saving-slice-relations-from-the-interactive-slice-intersection-tool/27585

---

## Post #1 by @danpak94 (2023-02-01 17:22 UTC)

<p>Hello,</p>
<p>I feel like this may have been addressed somewhere in the support section already, but I was not able to find the right post.</p>
<ol>
<li>I am wondering if there is a way to “fix” the slice orientation &amp; position set by using the “Interactive Slice Intersection” tool, so that the view does not change when I display a different volume.</li>
</ol>
<p>For example, when I set the slice intersections like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be0915b573a577d0918f0ff6bda3b1eadba6dfbd.jpeg" data-download-href="/uploads/short-url/r78bnij0v7gNCPCD3nnY5fFOxsh.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be0915b573a577d0918f0ff6bda3b1eadba6dfbd_2_690x303.jpeg" alt="image" data-base62-sha1="r78bnij0v7gNCPCD3nnY5fFOxsh" width="690" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be0915b573a577d0918f0ff6bda3b1eadba6dfbd_2_690x303.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be0915b573a577d0918f0ff6bda3b1eadba6dfbd_2_1035x454.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be0915b573a577d0918f0ff6bda3b1eadba6dfbd_2_1380x606.jpeg 2x" data-dominant-color="6E6E79"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×844 82.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>And then display a different volume, the slice views change to the default orthogonal + center position:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea624bc269ed33b79021277f2c1e5e7358b634c1.jpeg" data-download-href="/uploads/short-url/xrskdJTHjy9b9TwUexsRceNIegV.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea624bc269ed33b79021277f2c1e5e7358b634c1_2_690x301.jpeg" alt="image" data-base62-sha1="xrskdJTHjy9b9TwUexsRceNIegV" width="690" height="301" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea624bc269ed33b79021277f2c1e5e7358b634c1_2_690x301.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea624bc269ed33b79021277f2c1e5e7358b634c1_2_1035x451.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea624bc269ed33b79021277f2c1e5e7358b634c1_2_1380x602.jpeg 2x" data-dominant-color="62636E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×840 83.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>But it would be great if I could keep the slice orientation fixed across the different volumes that I’m trying to visualize.</p>
<p>I am aware of the Sequences module, and I can view multiple time points using the same slice views that way, but I would like the option to just change the volume display and still maintain the slice views.</p>
<ol start="2">
<li>On a similar note, what is the accurate way to save the interactive slice view parameters to load them for viewing later? I could not find this easily in the script repository.</li>
</ol>
<p>Thank you.</p>

---
