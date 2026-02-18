# Slicer caught an application error

**Topic ID**: 34672
**Date**: 2024-03-03
**URL**: https://discourse.slicer.org/t/slicer-caught-an-application-error/34672

---

## Post #1 by @muratmaga (2024-03-03 03:48 UTC)

<p>I am working these two files:</p>
<p><a href="https://raw.githubusercontent.com/SlicerMorph/SampleData/master/IMPC_sample_data.nrrd" class="onebox" target="_blank" rel="noopener">https://raw.githubusercontent.com/SlicerMorph/SampleData/master/IMPC_sample_data.nrrd</a></p>
<p>and its segmentation</p>
<p><a href="https://raw.githubusercontent.com/SlicerMorph/MD/main/IMPC_sample_data.seg.nrrd" class="onebox" target="_blank" rel="noopener">https://raw.githubusercontent.com/SlicerMorph/MD/main/IMPC_sample_data.seg.nrrd</a></p>
<p>When I load them both into the scene, switch to Segment editor and create a new segment and try to paint, I am getting this error.</p>
<p><code>[Qt] "Slicer has caught an application error, please save your work and restart.\n\nIf you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at https://slicer.org\n\n\nThe message detail is:\n\nException thrown in event: vector"</code></p>
<p>After this point paint tool doesnt work anymore. This on a Mac (intel) with 5.6.1 and seems to happen with the preview (Feb 7th) on the same computer. There is nothing else in the log files…</p>

---

## Post #2 by @lassoan (2024-03-03 13:18 UTC)

<p>This is moet likely because voxel type of the segmentation is float or double. This does not make sense, index values must be stored in integer type for numerical stability and space efficiency. Please check the file and if this is indeed the case then report the issue to the developers of the software that produced thile file.</p>
<p>Still, we cannot prevent unknowing users attempting to load flawed segmentations files, therefore we are adding automatic conversion at segmentation loading:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7605">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7605" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7605" target="_blank" rel="noopener">BUG: Fix issues caused by invalid Segmentation binary labelmap scalar types</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>Sunderlandkyl:segmentation_scalar_type_validation</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-02-26" data-time="16:45:17" data-timezone="UTC">04:45PM - 26 Feb 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/Sunderlandkyl" target="_blank" rel="noopener">
            <img alt="Sunderlandkyl" src="https://avatars.githubusercontent.com/u/9222709?v=4" class="onebox-avatar-inline" width="20" height="20">
            Sunderlandkyl
          </a>
        </div>

        <div class="lines" title="1 commits changed 8 files with 342 additions and 70 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7605/files" target="_blank" rel="noopener">
            <span class="added">+342</span>
            <span class="removed">-70</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Adds the functions ValidateSegmentationImageType and CastToSmallestUnsignedInteg<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7605" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">erType to vtkOrientedImageDataResample.
- IsSegmentationScalarTypeValid: Returns True if the scalar type of the image is valid for representing segmentations. False otherwise.
- CastToSmallestUnsignedIntegerType: Casts the contents of the image to the smallest unsigned integer type that can contain all values in the image.
- ValidateSegmentationImageType: Checks to see if the scalar type of the image is a valid type, and casts the image to the smallest valid type if it is not.

The function ValidateSegmentationImageType is used during binary labelmap read/import to automatically convert the labelmap.
If a labelmap representation with an invalid scalar type is added to a segment, we only log a warning and don't automatically convert the labelmap.
Before performing binary labelmap to closed surface conversion, we check that the scalar type is valid, and log/return an error if it is not.

This should prevent errors from arising due to the use of floating point images for segmentations.

Re #6941</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @muratmaga (2024-03-04 17:42 UTC)

<p>We have generated that segmentation, but I think the issue is segment editor defaults to the data type of the master volume (or at least I though it did), and in this case, these were indeed float volumes (intensity normalized).</p>

---

## Post #4 by @lassoan (2024-03-06 12:18 UTC)

<p>Slicer should always create integer segmentations, but of course it is possible that we missed something. How did you create the segmentation ‐ using the GUI (using which module, how?) or by Python script (can you send a link to the code)?</p>

---
