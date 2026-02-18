# DICOM images out of order

**Topic ID**: 22247
**Date**: 2022-03-01
**URL**: https://discourse.slicer.org/t/dicom-images-out-of-order/22247

---

## Post #1 by @carlosar (2022-03-01 19:26 UTC)

<p>Operating system: Linux, Ubuntu 20.04<br>
Slicer version: 4.11.20210226<br>
Expected behavior:<br>
When loading a DICOM database from the root folder, the order of the images is not inferred from <code>(0020, 0013) Instance Number</code> tag, however, when loading the first image in the series via the drag and drop functionality, the order is preserved.</p>
<p>Actual behavior: Not sure if this is expected behavior, since the discussion on ordering below indicates that the sorted images depend on having some geometry tags.</p>
<p>I do get the warning about this from this function:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/3de75b9c4c6f3ee9a1e5da17059b9f11517e16ab/Modules/Scripted/DICOMLib/DICOMUtils.py#L567">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/3de75b9c4c6f3ee9a1e5da17059b9f11517e16ab/Modules/Scripted/DICOMLib/DICOMUtils.py#L567" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/3de75b9c4c6f3ee9a1e5da17059b9f11517e16ab/Modules/Scripted/DICOMLib/DICOMUtils.py#L567" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/3de75b9c4c6f3ee9a1e5da17059b9f11517e16ab/Modules/Scripted/DICOMLib/DICOMUtils.py#L567</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="557" style="counter-reset: li-counter 556 ;">
          <li>        return loadSeriesWithVerification(seriesUIDs, self.selectedPlugins, self.loadedNodes)</li>
          <li>    return False</li>
          <li></li>
          <li>  def __exit__(self, type, value, traceback):</li>
          <li>    pass</li>
          <li></li>
          <li>#------------------------------------------------------------------------------</li>
          <li># TODO: more consistency checks:</li>
          <li># - is there gantry tilt?</li>
          <li># - are the orientations the same for all slices?</li>
          <li class="selected">def getSortedImageFiles(filePaths, epsilon=0.01):</li>
          <li>  """ Sort DICOM image files in increasing slice order (IS direction) corresponding to a series</li>
          <li></li>
          <li>      Use the first file to get the ImageOrientationPatient for the</li>
          <li>      series and calculate the scan direction (assumed to be perpendicular</li>
          <li>      to the acquisition plane)</li>
          <li></li>
          <li>      epsilon: Maximum difference in distance between slices to consider spacing uniform</li>
          <li>  """</li>
          <li>  warningText = ''</li>
          <li>  if len(filePaths) == 0:</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Similar discussions:</p><aside class="quote quote-modified" data-post="1" data-topic="15129">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/779978/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slice-order-in-dicom-loader/15129">Slice order in dicom loader</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, 
I wanted to confirm the mechanism with which Slicer orders dicom slices. I need the slice order (basically z-coordinate value) with filenames to write to csv for my application use and I found that the examineFiles function in DICOMScalarVolumePlugin.py  uses getSortedImageFiles function DICOMUtils.py to order them. 
I wanted to know whether is this the Slicer’s backend for showing ordered slices in Slicer viewer so I can call this examineFiles function to get array of sorted files and inde…
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="1" data-topic="11508">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/what-determines-dicom-import-image-type-ordering/11508">What determines DICOM import "Image Type" ordering?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, I am importing DICOM Dixon images and am getting inconsistent ordering of the image types.  Slicer correctly identifies that there are 4 image types, but does not order them in a consistent way.  Other software (e.g. Horos) consistently orders them.   <a href="https://radiopaedia.org/articles/dixon-method?lang=us" rel="noopener nofollow ugc">Dixon images </a> involve 4 series, a water image (W), a fat image (F), and two raw images from which the water and fat images are derived, one referred to as the in-phase (IP) and the other referred to as the opposite-phase (OP). 
Horos consist…
  </blockquote>
</aside>

<p>Is this expected behavior?</p>

---

## Post #2 by @lassoan (2022-03-01 19:31 UTC)

<p>Make sure you use the DICOM module to <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#read-dicom-files-into-the-scene">load DICOM images</a>. That module uses the correct DICOM tags (image position patient, image orientation patient) to reconstruct the 3D volume. <code>Instance number</code> must not be taken into account when reconstructing a 3D volume from slices.</p>
<p>We have not disabled ITK’s limited DICOM image reader that can be accessed via the “Add data” dialog (or drag-and-dropping the first file to the application window), but that reader should not be used.</p>

---

## Post #3 by @carlosar (2022-03-01 20:43 UTC)

<p>Thanks for the prompt response! I have been using the DICOM Module to load the image, but its possible the data I am using does not have the appropriate tags for orientation or pixel sizing.</p>
<p>When using the drag and drop, does this mean it is using ITK’s DICOM reader instead?</p>
<p>If so, then I guess ITK’s reader either uses the file name and/or <code>Instance Number</code> tag. Is this not recommended?</p>
<p>Since the order of the slices from the patient data I am using is missing the ones used by the DICOM module, would you suggest preprocessing to add the correct metadata to incorporate the correct tags? I am new to DICOM data, any advice would be appreciated!</p>

---

## Post #4 by @lassoan (2022-03-01 21:05 UTC)

<aside class="quote no-group" data-username="carlosar" data-post="3" data-topic="22247">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/49beb7/48.png" class="avatar"> carlosar:</div>
<blockquote>
<p>If so, then I guess ITK’s reader either uses the file name and/or <code>Instance Number</code> tag. Is this not recommended?</p>
</blockquote>
</aside>
<p>ITK reader used to sort the files by default but then a few years ago the behavior changed, and I think you now always need to sort the files before passing it to the reader (ITK provides helper methods for that). In Slicer, we have not invested time into fixing up DICOM loading via the “Add data” dialog, so I think now this methods loads the files unsorted (uses whatever order the files are found on the file system).</p>
<p>Our plan is to intercept DICOM file loading in “Add data” and redirect that to the DICOM module, but this has not been implemented yet:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5726">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5726" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5726" target="_blank" rel="noopener">Disable DICOM import from "Add data" dialog</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-07-06" data-time="20:04:13" data-timezone="UTC">08:04PM - 06 Jul 21 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2023-07-10" data-time="14:44:22" data-timezone="UTC">02:44PM - 10 Jul 23 UTC</span>
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
          Type: Bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">DICOM import via "Add data" dialog has many limitations, such as cannot deal wit<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">h varying slice spacing, 4D volumes, cannot import any other objects than images, etc. and has issues, such as potentially loading the image in incorrectly slice order.

DICOM loading this way should be disabled and preferable replaced by importing via the DICOM module. To match the previous functionality more closely, the import should be done via a temporary DICOM database and should be fast (at least time to first image should be quick and simple).

## Environment
- Slicer version: Slicer-4.11 and later
- Operating system: all</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @carlosar (2022-03-01 21:30 UTC)

<p>Great thanks for the update.</p>
<p>I’ve played around more with loading the data using the DICOM module, and the order is now preserved, when selecting the root folder with all patient/study/series data, but when loading one series individually, the order is not preserved:</p>
<p><code>./root/DICOM/PAT_0000/STD_0000/SER_00XY/OBJ_0001/</code><br>
versus loading at the root</p>
<p><code>./root</code></p>
<p>in either case, the tag <code>Pixel Spacing</code> is not read properly.</p>
<p>Any thoughts on how to debug this? I assume its connected to the warning:</p>
<p><code>No geometry information available for DICOM data, skipping corner calculations</code></p>

---

## Post #6 by @lassoan (2022-03-01 22:50 UTC)

<p>You can enable <code>Detailed logging</code> in Application settings → DICOM to get some more information, but I’m not sure if you get more details if basic geometry fields are invalid/missing.</p>
<p><code>Pixel Spacing</code> is stored as a decimal string. If it is ignored then it is typically because the string is invalid (e.g., you write leading or trailing spaces, incorrect decimal separator, etc.).</p>
<p>DICOM standard is complex and it is hard to create valid images. One way to address this is to have a look at a valid DICOM image that is similar to what you want to create to see what fields are usually set. Then read description of each field in the DICOM standard to see how you should set them for your images.</p>

---
