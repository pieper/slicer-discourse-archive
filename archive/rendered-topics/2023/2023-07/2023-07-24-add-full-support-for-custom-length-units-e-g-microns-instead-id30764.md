# Add full support for custom length units (e.g., microns instead of milimeters)

**Topic ID**: 30764
**Date**: 2023-07-24
**URL**: https://discourse.slicer.org/t/add-full-support-for-custom-length-units-e-g-microns-instead-of-milimeters/30764

---

## Post #1 by @swilm (2023-07-24 20:39 UTC)

<p>Hi<br>
I loaded in a nrrd file that was properly scaled and it is showing that the scale of the volume is correct, however when I add a scale bar it is in the wrong units. is there a way to change the units on the scale bar? In the screenshot you can see that the volume scale is in microns but the 3D scale bar is in cm.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a9d2b696d54a98dbb4def03f983bc5214de5dea.jpeg" data-download-href="/uploads/short-url/jMeCLdXhABpyr62UnQpngGpEFUC.jpeg?dl=1" title="Screenshot 2023-07-24 163506" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a9d2b696d54a98dbb4def03f983bc5214de5dea_2_690x410.jpeg" alt="Screenshot 2023-07-24 163506" data-base62-sha1="jMeCLdXhABpyr62UnQpngGpEFUC" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a9d2b696d54a98dbb4def03f983bc5214de5dea_2_690x410.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a9d2b696d54a98dbb4def03f983bc5214de5dea_2_1035x615.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a9d2b696d54a98dbb4def03f983bc5214de5dea_2_1380x820.jpeg 2x" data-dominant-color="B3B3BE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-07-24 163506</span><span class="informations">1920×1142 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-07-25 05:14 UTC)

<p>Thanks for reporting. This is a known issue - see <code>View ruler (horizontal ruler displayed in slice and 3D view nodes)</code> in:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5040">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5040" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5040" target="_blank" rel="noopener">Fix custom unit management</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-07-11" data-time="18:44:38" data-timezone="UTC">06:44PM - 11 Jul 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">For numerical stability of various processing methods, it is important to avoid <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">very small and very large numbers.

By default, Slicer uses millimeter as unit, therefore for microscopy images the image spacing could be very small (for example, 0.00006mm) and derived values even smaller (volume of a voxel would be 0.000000000000216mm3). This could lead to display issues (hard to read the numbers, not enough space to display them) and numerical instabilities and loss of precision. The solution is to use a more appropriate unit, such as micrometer or tenth of a micrometer.

Slicer allows specifying what is the unit of length values of the scene and has unit-aware slider and spinbox widgets to correctly display them. However, the implementation is not fully complete and consistent. Remaining tasks:

- [ ] Use unit-aware widgets (or unit-aware formatting) whenever displaying numerical values with units. There are a number of places where “mm” unit is hardcoded and should be display should be replaced with unit-aware widgets.
  - [ ] Transforms module display settings: I remember I had crashes with these widgets in Transform module’s display section and could not easily find the root cause, so just hardcoded mm, but we should give this another go. Examples include: view rulers (horizontal line at the bottom of views) and markups measurements (length of line and curves, surface area of closed curves).
  - [x] Markups measurements
  - [x] Slice offset slider
  - [ ] Segment statistics
  - [ ] Labelmap statistics
  - [ ] View ruler (horizontal ruler displayed in slice and 3D view nodes)
  - [ ] Models module, information section
- [ ] Importers should convert distance units. For example, when loading a DICOM file and the length unit is not mm, the voxel size must be scaled accordingly.
- [ ] Exporters should write distance units into files.
- [ ] CLI module interface should be made unit-aware.
- [ ] All transformable data in the scene must be rescaled when a scene with a different unit is imported.
- [ ] Maybe offer the user to rescale all spatial data in the scene when length unit is changed.

Until all these are implemented, a workaround is to enter values in a different unit (e.g., enter 0.06 "mm" instead of the real 0.06 micrometer), but don't change the unit in application settings. Then user would know that all units that Slicer displays in millimeters are actually in the other chosen unit (i.e., micrometer). See some more details and explanation here: https://discourse.slicer.org/t/distance-measurement-and-rendering-of-microscopy-images/791</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>These fixes would probably require contribution from the community - either contribution of development efforts or funding. This issue may also get more attention if it turns out to be a highly requested feature - so I move it now to the “Feature request” category so that people can vote on it.</p>

---
