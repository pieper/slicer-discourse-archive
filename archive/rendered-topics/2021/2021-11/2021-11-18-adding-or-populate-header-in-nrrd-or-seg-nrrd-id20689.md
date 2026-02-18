# Adding or populate header in nrrd or seg.nrrd

**Topic ID**: 20689
**Date**: 2021-11-18
**URL**: https://discourse.slicer.org/t/adding-or-populate-header-in-nrrd-or-seg-nrrd/20689

---

## Post #1 by @phcerdan (2021-11-18 17:17 UTC)

<p>Is there any interface to add a custom header to a nrrd from Slicer, i.e: <code>quality:=incomplete</code>, or populate a predefined existing header to a Segmentation image (seg.nrrd)?</p>
<p>If not with GUI, with slicer python would be ok too.<br>
As a reference on how is done in ITK: <a href="https://discourse.itk.org/t/how-to-write-a-custom-tag-to-an-image-nrrd-or-other-header/565" class="inline-onebox" rel="noopener nofollow ugc">How to write a custom Tag to an image (NRRD or other) header - Beginner Questions - ITK</a></p>
<p>I would appreciate any insight/suggestion. Thanks!</p>

---

## Post #2 by @lassoan (2021-11-18 20:50 UTC)

<p>Each segment has a state (not started, in progress, completed, flagged) that you can see and modify using the GUI and also saved in the .seg.nrrd file.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aefef8a053bb44476fc1b79981c32015b0cc3ecb.png" data-download-href="/uploads/short-url/oY5lTq3EzuqdRdjw1PIB6UN5w9R.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aefef8a053bb44476fc1b79981c32015b0cc3ecb_2_496x500.png" alt="image" data-base62-sha1="oY5lTq3EzuqdRdjw1PIB6UN5w9R" width="496" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aefef8a053bb44476fc1b79981c32015b0cc3ecb_2_496x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aefef8a053bb44476fc1b79981c32015b0cc3ecb_2_744x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aefef8a053bb44476fc1b79981c32015b0cc3ecb.png 2x" data-dominant-color="E9ECEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">855×861 54.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If this is not sufficient then you can add arbitrary number of custom properties (tag:value pairs) to any segment using Python scripting (using <a href="http://apidocs.slicer.org/master/classvtkSegment.html#a75d0c23fc90fc1252acd14278f64c386">vtkSegment::SetTag method</a>). These custom tags are also stored in the .seg.nrrd file.</p>
<p>You can read all these states and other properties in .seg.nrrd files using <a href="https://pypi.org/project/slicerio/">slicerio</a>  Python package (in any Python environment, not just in Slicer).</p>

---

## Post #3 by @phcerdan (2022-02-17 00:07 UTC)

<p>For completion, this is the way to do it with proper <code>itk</code>.</p>
<pre><code class="lang-python">    import itk
    meta_dict = my_image.GetMetaDataDictionary()
    meta_dict.Set("Segment0_Name", itk.MetaDataObject[str].New(MetaDataObjectValue="horse"))
    meta_dict.Set("Segment0_ID", itk.MetaDataObject[str].New(MetaDataObjectValue="Segment_1"))
    meta_dict.Set("Segment0_Color", itk.MetaDataObject[str].New(MetaDataObjectValue="0.5300 0.6700 0.3700")) # Greenish
    meta_dict.Set("Segment0_LabelValue", itk.MetaDataObject[str].New(MetaDataObjectValue="1"))
    meta_dict.Set("Segment0_Layer", itk.MetaDataObject[str].New(MetaDataObjectValue="0"))

    meta_dict.Set("Segment1_Name", itk.MetaDataObject[str].New(MetaDataObjectValue="dog"))
    meta_dict.Set("Segment1_ID", itk.MetaDataObject[str].New(MetaDataObjectValue="Segment_2"))
    meta_dict.Set("Segment1_Color", itk.MetaDataObject[str].New(MetaDataObjectValue="0.40625 0.2187 0.6796")) # Purplish
    meta_dict.Set("Segment1_LabelValue", itk.MetaDataObject[str].New(MetaDataObjectValue="2"))
    meta_dict.Set("Segment1_Layer", itk.MetaDataObject[str].New(MetaDataObjectValue="0"))

    itk.imwrite(my_image, str(output_dir/ "my_image.nrrd"))
</code></pre>

---
