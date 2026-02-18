# Cannot write data file:...labelmap associated ColorTable.ctbl

**Topic ID**: 13057
**Date**: 2020-08-17
**URL**: https://discourse.slicer.org/t/cannot-write-data-file-labelmap-associated-colortable-ctbl/13057

---

## Post #1 by @ahopf (2020-08-17 21:05 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior: Save full scene<br>
Actual behavior: Saves empty “TempWrite” directory in the destination directory. The labelmap.nrrd is empty when reopened in Slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac50b66345c28bc44543a4bb37dce2b5f1f74298.jpeg" data-download-href="/uploads/short-url/oAn38jaQFyOGGvXzo6NFQDrF1eE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac50b66345c28bc44543a4bb37dce2b5f1f74298_2_690x186.jpeg" alt="image" data-base62-sha1="oAn38jaQFyOGGvXzo6NFQDrF1eE" width="690" height="186" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac50b66345c28bc44543a4bb37dce2b5f1f74298_2_690x186.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac50b66345c28bc44543a4bb37dce2b5f1f74298_2_1035x279.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac50b66345c28bc44543a4bb37dce2b5f1f74298.jpeg 2x" data-dominant-color="E8E9EA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1310×354 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>[ERROR][VTK] 17.08.2020 15:28:37 [vtkMRMLColorTableStorageNode (000001EBAEB8B390)] (D:\D\S\Slicer-4102\Libs\MRML\Core\vtkMRMLColorTableStorageNode.cxx:237) - ERROR opening colour file D:/Adam/Bullseye/1) EVD Neurosurgical Application/2020-08-09_cadaver_evd_pre-clinical proof-of-concept/5) scenes/GL1810218/4) GL1810218_preop ct to postop ct_preop ct skin segmentation threshold optimization/GL1810218_preop_skin segmentation_-300-label_ColorTable.ctbl</p>

---

## Post #2 by @lassoan (2020-08-17 22:02 UTC)

<p>The extremely long filename may be an issue. Could you try a shorter filename and path?</p>

---
