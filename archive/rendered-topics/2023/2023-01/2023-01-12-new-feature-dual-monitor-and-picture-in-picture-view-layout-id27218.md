# New feature: Dual monitor and picture-in-picture view layout

**Topic ID**: 27218
**Date**: 2023-01-12
**URL**: https://discourse.slicer.org/t/new-feature-dual-monitor-and-picture-in-picture-view-layout/27218

---

## Post #1 by @lassoan (2023-01-12 22:03 UTC)

<p>Slicer can now display 3D, slice, plot, etc. views in multiple windows and not just in the main application window - see <a href="https://youtu.be/PJuXSXkPvHs">1-minute demo video</a>.</p>
<p>Display views in separate windows - can be dragged to a second screen or additional touchscreen or drawing tablet:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a351e604051ca1b0e319eb20c4b4dd2f1c024610.jpeg" data-download-href="/uploads/short-url/niNifHBkKk94D7SWYp27YY6S2dO.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a351e604051ca1b0e319eb20c4b4dd2f1c024610_2_690x425.jpeg" alt="image" data-base62-sha1="niNifHBkKk94D7SWYp27YY6S2dO" width="690" height="425" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a351e604051ca1b0e319eb20c4b4dd2f1c024610_2_690x425.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a351e604051ca1b0e319eb20c4b4dd2f1c024610_2_1035x637.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a351e604051ca1b0e319eb20c4b4dd2f1c024610_2_1380x850.jpeg 2x" data-dominant-color="534150"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1184 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The extra window can be displayed floating over the application window as “picture-in-picture”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f8580f53dd5d589e66bb297967b28535b19d659.jpeg" data-download-href="/uploads/short-url/6MoteFNJJeMUpKCVcplWmAXIur7.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f8580f53dd5d589e66bb297967b28535b19d659_2_690x417.jpeg" alt="image" data-base62-sha1="6MoteFNJJeMUpKCVcplWmAXIur7" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f8580f53dd5d589e66bb297967b28535b19d659_2_690x417.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f8580f53dd5d589e66bb297967b28535b19d659_2_1035x625.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f8580f53dd5d589e66bb297967b28535b19d659_2_1380x834.jpeg 2x" data-dominant-color="524E4D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1163 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The additional window can be also docked into application window (any corners or sides):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa9760a69191c1caf71940284979eb8112f217a0.jpeg" data-download-href="/uploads/short-url/ol7uGfPGHN7S6KYrpeIZXRK5yUM.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa9760a69191c1caf71940284979eb8112f217a0_2_690x416.jpeg" alt="image" data-base62-sha1="ol7uGfPGHN7S6KYrpeIZXRK5yUM" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa9760a69191c1caf71940284979eb8112f217a0_2_690x416.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa9760a69191c1caf71940284979eb8112f217a0_2_1035x624.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa9760a69191c1caf71940284979eb8112f217a0_2_1380x832.jpeg 2x" data-dominant-color="565154"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1159 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Views can be maximized/restored independently in each window.</p>
<p>Currently, only a single additional layout is added, which adds one extra window. Custom views can be specified by an XML description (see example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/advanced_topics.html#example-layout-containing-two-viewports">description</a> and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-view-layout">code</a>).</p>

---

## Post #2 by @RafaelPalomar (2023-01-13 16:30 UTC)

<p>This is very useful, thanks for working on it!</p>

---

## Post #3 by @philippepellerin (2023-01-15 09:36 UTC)

<p>Thanks for this one, again a great work!</p>

---
