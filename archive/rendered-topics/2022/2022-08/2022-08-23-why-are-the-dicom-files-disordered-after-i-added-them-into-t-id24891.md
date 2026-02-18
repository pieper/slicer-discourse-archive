# Why are the dicom files disordered after I added them into the DICOM database?

**Topic ID**: 24891
**Date**: 2022-08-23
**URL**: https://discourse.slicer.org/t/why-are-the-dicom-files-disordered-after-i-added-them-into-the-dicom-database/24891

---

## Post #1 by @Dawn_GreyHouse (2022-08-23 17:11 UTC)

<p>I have converted 1000+ consecutive CT scanning TIFF files into DICOM files in the right order, but when I add the folder with all the converted files, 3D slicer made them into the wrong order. I checked the converted files, but they are in the right order. Does anyone know why it’s messed up?<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72f36c52c219213cf96a371a044d214fbe7d396b.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72f36c52c219213cf96a371a044d214fbe7d396b.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72f36c52c219213cf96a371a044d214fbe7d396b.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #2 by @pieper (2022-08-23 17:51 UTC)

<p>DICOM files are sorted according to metadata in the header, so if you didn’t convert them with the correct values they will be invalid.  If the source data is tiff you can use the ImageStacks module in SlicerMorph instead.</p>

---
