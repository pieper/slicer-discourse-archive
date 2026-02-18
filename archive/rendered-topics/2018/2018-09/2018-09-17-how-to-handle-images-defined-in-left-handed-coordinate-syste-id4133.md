# How to handle images defined in left-handed coordinate system

**Topic ID**: 4133
**Date**: 2018-09-17
**URL**: https://discourse.slicer.org/t/how-to-handle-images-defined-in-left-handed-coordinate-system/4133

---

## Post #1 by @pieper (2018-09-17 21:10 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="4088">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/how-to-convert-to-stl-from-nii/4088/3">How to convert to .stl from .nii</a></div>
<blockquote>
<p>invalid coordinate system (determinant of voxel-&gt;physical transform is negative,</p>
</blockquote>
</aside>
<p>Small aside on this - the voxel-to-physical coordinate system that describes acquisition geometry can be left handed (e.g. axial foot-first vs head-first).  ITK readers re-arrange the data to enforce right-handedness.</p>
<p>VTKjs supports direction vectors on image data and it was recently fixed to allow left handed matrices <a href="https://github.com/Kitware/vtk-js/issues/858">recently came up in vtkjs</a>,</p>

---

## Post #2 by @lassoan (2018-09-17 21:26 UTC)

<aside class="quote no-group quote-modified" data-username="pieper" data-post="4" data-topic="4088">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"><a href="https://discourse.slicer.org/t/how-to-convert-to-stl-from-nii/4088/4">How to convert to .stl from .nii</a></div>
<blockquote>
<p>voxel-to-physical coordinate system that describes acquisition geometry can be left handed</p>
</blockquote>
</aside>
<p>From <a href="https://nifti.nimh.nih.gov/nifti-1/documentation/nifti1fields/nifti1fields_pages/qsform.html">this specification</a> it seems that left-handed is not permitted in nifti (search for left-handed on the page and see also axes specification a few paragraphs above).</p>
<aside class="quote no-group quote-modified" data-username="pieper" data-post="4" data-topic="4088">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"><a href="https://discourse.slicer.org/t/how-to-convert-to-stl-from-nii/4088/4">How to convert to .stl from .nii</a></div>
<blockquote>
<p>ITK readers re-arrange the data to enforce right-handedness</p>
</blockquote>
</aside>
<p>Is this something that has been added recently? What direction matrix do you see in Volumes module when you load the above-referenced volume into Slicer?</p>

---

## Post #3 by @pieper (2018-09-17 21:56 UTC)

<aside class="quote no-group quote-post-not-found" data-username="lassoan" data-post="5" data-topic="4088">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/how-to-convert-to-stl-from-nii/4088/5">How to convert to .stl from .nii</a></div>
<blockquote>
<p>From <a href="https://nifti.nimh.nih.gov/nifti-1/documentation/nifti1fields/nifti1fields_pages/qsform.html">this specification</a> it seems that left-handed is not permitted in nifti (search for left-handed on the page and see also axes specification a few paragraphs above).</p>
</blockquote>
</aside>
<p>Yes, file formats may not support left handed coordinates - I see now that you were referring to the nifti file being invalid not that directions can’t be invalid as a general rule.</p>
<aside class="quote no-group quote-post-not-found" data-username="lassoan" data-post="5" data-topic="4088">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/how-to-convert-to-stl-from-nii/4088/5">How to convert to .stl from .nii</a></div>
<blockquote>
<p>Is this something that has been added recently? What direction matrix do you see in Volumes module when you load the above-referenced volume into Slicer?</p>
</blockquote>
</aside>
<p>Not new, that was the original design and is still in the documentation.  To be honest though I’m not sure which readers enforce it:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Kitware/ITK/blob/master/Modules/Core/Common/include/itkImageBase.h#L200-L209">
  <header class="source">

      <a href="https://github.com/Kitware/ITK/blob/master/Modules/Core/Common/include/itkImageBase.h#L200-L209" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/ITK/blob/master/Modules/Core/Common/include/itkImageBase.h#L200-L209" target="_blank" rel="noopener">Kitware/ITK/blob/master/Modules/Core/Common/include/itkImageBase.h#L200-L209</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="200" style="counter-reset: li-counter 199 ;">
          <li>*</li>
          <li>* The columns of the Direction matrix are expected to form an</li>
          <li>* orthogonal right handed coordinate system.  But this is not</li>
          <li>* checked nor enforced in itk::ImageBase.</li>
          <li>*</li>
          <li>* For details, please see:</li>
          <li>*</li>
          <li>* https://www.itk.org/Wiki/Proposals:Orientation#Some_notes_on_the_DICOM_convention_and_current_ITK_usage</li>
          <li>*</li>
          <li>* \sa GetDirection() */</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I’d need to dig back in, but as I recall the GDCM reader rearranges the order of the slices so that the direction turns out right-handed.</p>

---

## Post #4 by @lassoan (2018-09-17 23:00 UTC)

<p>We may also end up with left-handed image coordinate system axes if a mirroring transform is applied.</p>
<p>Should we add a helper function in volumes logic that converts images to right-handed coordinate system (by reordering slices and flipping z axis) and call it after image import and after hardening a transform on a volume?</p>

---

## Post #5 by @pieper (2018-09-17 23:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="4133">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Should we add a helper function in volumes logic that converts images to right-handed coordinate system (by reordering slices and flipping z axis)</p>
</blockquote>
</aside>
<p>I think that would make sense, yes.  Because we use ITK so much for processing we should try to ensure that our image data conforms to its expectations.  Hardening seems like the right place to put it.</p>
<p>But probably easiest just to resample into an appropriate right-handed reference grid so not much special code is required.</p>
<p>Actually that reminds me of another issue a student had the other day.  She was setting transforms manually that included shears and then hardening them, which works because the volume node can have non-orthonormal directions.  But when she saved to nifti and reloaded the images were different (unfortunately in a subtle way) because nifti changes the directions to a quaternion.  The workaround was to resample rather than harden.</p>
<p>So I think the code should detect both these cases and resample for hardening or importing.</p>

---

## Post #6 by @Mihail_Isakov (2018-09-18 06:12 UTC)

<p>Hello,<br>
Such Nifti files are common (e.g. MNI152 space).<br>
Here are very useful test files with R/L marks here<br>
<a href="https://nifti.nimh.nih.gov/nifti-1/data" class="onebox" target="_blank" rel="nofollow noopener">https://nifti.nimh.nih.gov/nifti-1/data</a></p>
<p>User’s file (triggered this discussion) has orientation RPI (in ITK terminology, notation “from”),<br>
file named avg152T1_LR_nifti.nii.gz from the link above has the same orientation.</p>
<p>Good news, both test files are correctly displayed in Slicer volume viewer and Slicer<br>
can correctly save them in MetaImage file (not sure about all modules).<br>
I guess because in ITK (and MetaImage format) matrices are fully defined,<br>
this one is<br>
1  0  0<br>
0 -1  0<br>
0  0  1<br>
so there is no need to use cross product (whatever left or right handed) to get 3rd row (Z direction) from 1st and 2nd,<br>
(remember DICOM’s direction cosines, they were in particular case 1,0,0,0,-1,0 and 3rd row (Z direction were cross product, here is a problem. But luckily not visible in classic series thanks to sorting by IPP/IOP,<br>
resulting orientation after correct sorting were RPS (in ITK terminology).</p>
<p>To be sure and safe one can e.g. use ITK’s change orientation filter and<br>
re-orient to RPS (in ITK terminology)<br>
1  0   0<br>
0 -1   0<br>
0  0  -1</p>
<p>or LPI (in ITK terminology)<br>
-1  0  0<br>
0 -1 0<br>
0  0  1</p>
<p>BTW, look at  MHA header to see ITK’s orientation code and transform matrix:<br>
TransformMatrix = 1 0 0 0 -1 0 0 0 1<br>
AnatomicalOrientation = RPI</p>
<p>Regards</p>
<p>Edited:<br>
also s.<br>
<a href="https://nifti.nimh.nih.gov/nifti-1/documentation/faq#Q14" class="onebox" target="_blank" rel="nofollow noopener">https://nifti.nimh.nih.gov/nifti-1/documentation/faq#Q14</a><br>
<a href="https://nifti.nimh.nih.gov/nifti-1/documentation/faq#Q15" class="onebox" target="_blank" rel="nofollow noopener">https://nifti.nimh.nih.gov/nifti-1/documentation/faq#Q15</a></p>

---
