# Batch editing of 3DAngio CBCT slice thickness dicom tag

**Topic ID**: 36576
**Date**: 2024-06-03
**URL**: https://discourse.slicer.org/t/batch-editing-of-3dangio-cbct-slice-thickness-dicom-tag/36576

---

## Post #1 by @rruo (2024-06-03 15:24 UTC)

<p>Hello,  we have a cbct slices from a 3d angiography system but all the slices have the same slice location.   Is there a way to batch process and edit the slice location in Slicer?  there are 512 images and the location would be incremented by 0.3mm.   Thank you for the information.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7209fb45b35b6f71909a0df2dd74f2e1fa9ea83.jpeg" data-download-href="/uploads/short-url/nQtDirXrQdVZbTap7ZQdelbxd19.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7209fb45b35b6f71909a0df2dd74f2e1fa9ea83_2_690x430.jpeg" alt="image" data-base62-sha1="nQtDirXrQdVZbTap7ZQdelbxd19" width="690" height="430" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7209fb45b35b6f71909a0df2dd74f2e1fa9ea83_2_690x430.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7209fb45b35b6f71909a0df2dd74f2e1fa9ea83_2_1035x645.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7209fb45b35b6f71909a0df2dd74f2e1fa9ea83.jpeg 2x" data-dominant-color="555555"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1332×832 79.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-06-03 15:30 UTC)

<p>There is no need to edit <code>slice thickness</code> or <code>slice location</code> tags. These tags must not be taken into account for reconstructing a 3D volume from slices. Only “image position patient” and “image orientation patient” tags matter.</p>
<p>If the tags are missing then it may be because the image is not intended for 3D reconstruction (you could have a look if tyou can export the image in a different way) or the image could have been corrupted by some post-processing (e.g., anonymization or processing in some other software; you can try skipping these steps to confirm that this is the issue).</p>

---

## Post #3 by @rruo (2024-06-04 12:01 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="36576">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>image position patient</p>
</blockquote>
</aside>
<p>Thank you for the reply!</p>
<p>Yes we have both of the tags you mentioned</p>
<p>(0020,0032) Image Position Patient DS 3 String [0.0, 0.0, 0.0]<br>
(0020,0037) Image Orientation Patient DS 6 String [1.0, 0.0, 0.0, 0.0, 1.0, 0.0]</p>
<p>The original files are taken from an older 3d angio system.  The current software version does not prepare 3d ct volumes which we would like to use for aiding with contouring in avm cases.   It only puts out ‘photos’ or screencaptures of the 3d volume slices.  But the manufacturer was able to give us the raw 512 image slice set.</p>
<p>But each individual slice/file has the exact same ‘location’ in the ‘z’ value.  I thought this would be the issue for our TPS not being able to construct a 3d volume from the series.</p>
<p>Do you have any suggestion on how we would be able to produce a 3d ct set from these slices?</p>
<p>Thanks for any info you have.</p>

---

## Post #4 by @lassoan (2024-06-04 13:44 UTC)

<p>You can use the DICOM patcher in Slicer for setting Image Position Patient values if you know the spacing. You may be able to use the “Generate slice position for multi-frame volumes” rule or create a new rule similat to it:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/acf3dd47940665869765584564b38439f73ff1d5/Modules/Scripted/DICOMPatcher/DICOMPatcher.py#L410-L485">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/acf3dd47940665869765584564b38439f73ff1d5/Modules/Scripted/DICOMPatcher/DICOMPatcher.py#L410-L485" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/acf3dd47940665869765584564b38439f73ff1d5/Modules/Scripted/DICOMPatcher/DICOMPatcher.py#L410-L485" target="_blank" rel="noopener">Slicer/Slicer/blob/acf3dd47940665869765584564b38439f73ff1d5/Modules/Scripted/DICOMPatcher/DICOMPatcher.py#L410-L485</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="410" style="counter-reset: li-counter 409 ;">
          <li>class AddMissingSliceSpacingToMultiframe(DICOMPatcherRule):</li>
          <li>    """Add missing slice spacing info to multiframe files"""</li>
          <li></li>
          <li>    def processDataSet(self, ds):</li>
          <li>        import pydicom</li>
          <li></li>
          <li>        if not hasattr(ds, "NumberOfFrames"):</li>
          <li>            return</li>
          <li>        numberOfFrames = ds.NumberOfFrames</li>
          <li>        if numberOfFrames &lt;= 1:</li>
          <li>            return</li>
          <li></li>
          <li>        # Multi-frame sequence, we may need to add slice positions</li>
          <li></li>
          <li>        # Error in Dolphin 3D CBCT scanners, they store multiple frames but they keep using CTImageStorage as storage class</li>
          <li>        if ds.SOPClassUID == "1.2.840.10008.5.1.4.1.1.2":  # Computed Tomography Image IOD</li>
          <li>            ds.SOPClassUID = "1.2.840.10008.5.1.4.1.1.2.1"  # Enhanced CT Image IOD</li>
          <li></li>
          <li>        sliceStartPosition = ds.ImagePositionPatient if hasattr(ds, "ImagePositionPatient") else [0, 0, 0]</li>
          <li>        sliceAxes = ds.ImageOrientationPatient if hasattr(ds, "ImageOrientationPatient") else [1, 0, 0, 0, 1, 0]</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/acf3dd47940665869765584564b38439f73ff1d5/Modules/Scripted/DICOMPatcher/DICOMPatcher.py#L410-L485" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @rruo (2024-06-10 17:16 UTC)

<p>Thank you, I will try this out.</p>

---

## Post #6 by @rruo (2024-06-13 18:57 UTC)

<p>Hello,</p>
<p>I ran the dicom patch and loaded my files into Slicer. But how do I batch edit the location or patient position? The slice thickness would 0.3mm. Is this possible with slicer?</p>
<p>Thanks for the help and info,<br>
Russell</p>

---

## Post #7 by @lassoan (2024-06-13 19:16 UTC)

<p>Yes, sure, it should be no problem to update slice positions in Slicer. You can see that there is already a rule that can update slice positions for certain images. You can slightly tune this rule or create a new rule to process your data. You can simply edit the DICOMPatcher.py file in a text editor and click “Reload” button in the module GUI.</p>

---

## Post #8 by @rruo (2024-06-13 19:46 UTC)

<p>Hi Andre,</p>
<p>Thanks for the help. Apologies for the silly questions… I’m an end user and not really a programmer so I’m not really sure where I can edit this in the code.</p>
<p>But would I be able to simply change this to 0.3mm here (red arrow)?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e38ea57814976e9179a64c465abacc6bf25b79c5.png" data-download-href="/uploads/short-url/wt40gcRxKS4a045f4PXkW1ZSYdL.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e38ea57814976e9179a64c465abacc6bf25b79c5.png" data-base62-sha1="wt40gcRxKS4a045f4PXkW1ZSYdL" width="558" height="500" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">1043×934 26.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks again,<br>
Russell</p>

---

## Post #9 by @lassoan (2024-06-13 19:51 UTC)

<p>Yes, you need to set the desired slice spacing. There are a few other small things to check. For example, make sure that the plugin accepts your DICOM image (if not then you can edit the list of accepted SOPClassUIDs).</p>
<p>I would recommend to step through the code using a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/python.html">Python debugger</a> so that you can make sure that it does what you want.</p>

---
