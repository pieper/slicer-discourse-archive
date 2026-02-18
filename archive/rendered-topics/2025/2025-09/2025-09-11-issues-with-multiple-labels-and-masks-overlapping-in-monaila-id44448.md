# Issues with multiple labels and masks overlapping in Monailabel

**Topic ID**: 44448
**Date**: 2025-09-11
**URL**: https://discourse.slicer.org/t/issues-with-multiple-labels-and-masks-overlapping-in-monailabel/44448

---

## Post #1 by @koumeasa (2025-09-11 14:11 UTC)

<p>Hey everyone, I’m labeling brain segments in MONAILabel.</p>
<p>The masks / ROIs used as input for Monailabel are a subselection extracted by slicerio.extract_segments() function from a 3DSlicer Segmentation node.</p>
<p>I modified the config files from the models <strong>DeepEdit</strong> and <strong>Segmentation</strong> (from the radiology app) to match our masks, but I haven’t made much progress so far.</p>
<p>Here is a screenshot of the <strong>DeepEdit</strong> config file</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72719ab1775b5a04280f3b5506816514cd4f1344.png" data-download-href="/uploads/short-url/gkpPjw5eDkSzpDWz3rSM78TjL3S.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72719ab1775b5a04280f3b5506816514cd4f1344.png" alt="image" data-base62-sha1="gkpPjw5eDkSzpDWz3rSM78TjL3S" width="690" height="495" data-dominant-color="F9F9F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1218×874 47 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve included 5 masks so far, which are clearly identified in 3D Slicer (see figure below):</p>
<p>In <strong>3D Slicer,</strong> the 5 labels are separate and clearly identified</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc865b6d90cebeabbcfbef7b3545efd0b7c2fefa.jpeg" data-download-href="/uploads/short-url/A1WbfiwKOQmyFNL5o6rSLjVhnpE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc865b6d90cebeabbcfbef7b3545efd0b7c2fefa_2_690x475.jpeg" alt="image" data-base62-sha1="A1WbfiwKOQmyFNL5o6rSLjVhnpE" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc865b6d90cebeabbcfbef7b3545efd0b7c2fefa_2_690x475.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc865b6d90cebeabbcfbef7b3545efd0b7c2fefa_2_1035x712.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc865b6d90cebeabbcfbef7b3545efd0b7c2fefa.jpeg 2x" data-dominant-color="7E7E7A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1160×799 65.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, when I open them in MONAI Label, the labels often get collapsed. For example, the ipsilateral and contralateral hemisphere labels may collapse into the contralateral hemisphere, the cerebellum and lateral ventricles become one label, and some labels are completely absent (see figure below):</p>
<p>In <strong>Monailabel,</strong> all 5 labels are collapsed into 3 - cerebellum, ipsilateral and contralateral lateral ventricles</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd420a29025fd29e85a80203b84eb0ad35d38e74.jpeg" data-download-href="/uploads/short-url/thNmZraszSTjcrs67lt0o9ptAGM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd420a29025fd29e85a80203b84eb0ad35d38e74_2_690x474.jpeg" alt="image" data-base62-sha1="thNmZraszSTjcrs67lt0o9ptAGM" width="690" height="474" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd420a29025fd29e85a80203b84eb0ad35d38e74_2_690x474.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd420a29025fd29e85a80203b84eb0ad35d38e74.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd420a29025fd29e85a80203b84eb0ad35d38e74.jpeg 2x" data-dominant-color="7C7B7A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">991×682 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Has anyone encountered this issue before or have any advice on how to fix it?</p>

---

## Post #2 by @koumeasa (2025-09-29 09:29 UTC)

<p><strong>UPDATE:</strong> We are still stuck with the overlapping label maps. It seems the most labels collapse into the last 2 or 3 segments (as shown previously in Figure 3).<br>
This problem ONLY occurs in Monailabel module, but not with the 3D Slicer segment editor.</p>
<p><strong>Find below the object information from the mask when loaded with Monailabel.</strong><br>
Thank you so much!</p>
<p>Python 3.9.10 (main, Mar  2 2025, 20:55:00) [MSC v.1942 64 bit (AMD64)] on win32</p>
<blockquote>
<blockquote>
<blockquote>
<p>seg = labelmapNode.GetSegmentation()<br>
print(seg)<br>
vtkSegmentation (0000020B12988720)<br>
Debug: Off<br>
Modified Time: 8177604<br>
SourceRepresentationName:  Binary labelmap<br>
Number of segments: 5<br>
Segments:<br>
Ipsilateral Hemisphere:<br>
Name: Ipsilateral Hemisphere<br>
Color: (0.501961, 0.682353, 0.501961)<br>
NameAutoGenerated: true<br>
ColorAutoGenerated: true<br>
Debug: Off<br>
Modified Time: 8346968<br>
Representations:<br>
Binary labelmap:<br>
ClassName: vtkOrientedImageData<br>
Origin: -14.9414 -14.9414 -129.807<br>
Spacing: 0.11719 0.11719 0.4<br>
Extent: 0 255 0 255 0 39<br>
Scalar type: unsigned char<br>
Number of components: 1<br>
IJKToRASDirections:<br>
1 0 0<br>
0 1 -1.28205e-07<br>
0 0 1<br>
Tags:<br>
TerminologyEntry: Segmentation category and type - 3D Slicer General Anatomy list~SCT^85756007^Tissue~SCT^85756007^Tissue~^^~Anatomic codes - DICOM master list~^^~^^<br>
Contralateral Hemisphere:<br>
Name: Contralateral Hemisphere<br>
Color: (0.945098, 0.839216, 0.568627)<br>
NameAutoGenerated: true<br>
ColorAutoGenerated: true<br>
Debug: Off<br>
Modified Time: 8347271<br>
Representations:<br>
Binary labelmap:<br>
ClassName: vtkOrientedImageData<br>
Origin: -14.9414 -14.9414 -129.807<br>
Spacing: 0.11719 0.11719 0.4<br>
Extent: 0 255 0 255 0 39<br>
Scalar type: unsigned char<br>
Number of components: 1<br>
IJKToRASDirections:<br>
1 0 0<br>
0 1 -1.28205e-07<br>
0 0 1<br>
Tags:<br>
TerminologyEntry: Segmentation category and type - 3D Slicer General Anatomy list~SCT^85756007^Tissue~SCT^85756007^Tissue~^^~Anatomic codes - DICOM master list~^^~^^<br>
Cerebellum:<br>
Name: Cerebellum<br>
Color: (0.694118, 0.478431, 0.396078)<br>
NameAutoGenerated: true<br>
ColorAutoGenerated: true<br>
Debug: Off<br>
Modified Time: 8347574<br>
Representations:<br>
Binary labelmap:<br>
ClassName: vtkOrientedImageData<br>
Origin: -14.9414 -14.9414 -129.807<br>
Spacing: 0.11719 0.11719 0.4<br>
Extent: 0 255 0 255 0 39<br>
Scalar type: unsigned char<br>
Number of components: 1<br>
IJKToRASDirections:<br>
1 0 0<br>
0 1 -1.28205e-07<br>
0 0 1<br>
Tags:<br>
TerminologyEntry: Segmentation category and type - 3D Slicer General Anatomy list~SCT^85756007^Tissue~SCT^85756007^Tissue~^^~Anatomic codes - DICOM master list~^^~^^<br>
Ipsilateral Lateral Ventricle:<br>
Name: Ipsilateral Lateral Ventricle<br>
Color: (0.435294, 0.721569, 0.823529)<br>
NameAutoGenerated: true<br>
ColorAutoGenerated: true<br>
Debug: Off<br>
Modified Time: 8347877<br>
Representations:<br>
Binary labelmap:<br>
ClassName: vtkOrientedImageData<br>
Origin: -14.9414 -14.9414 -129.807<br>
Spacing: 0.11719 0.11719 0.4<br>
Extent: 0 255 0 255 0 39<br>
Scalar type: unsigned char<br>
Number of components: 1<br>
IJKToRASDirections:<br>
1 0 0<br>
0 1 -1.28205e-07<br>
0 0 1<br>
Tags:<br>
TerminologyEntry: Segmentation category and type - 3D Slicer General Anatomy list~SCT^85756007^Tissue~SCT^85756007^Tissue~^^~Anatomic codes - DICOM master list~^^~^^<br>
Contralateral Lateral Ventricle:<br>
Name: Contralateral Lateral Ventricle<br>
Color: (0.847059, 0.396078, 0.309804)<br>
NameAutoGenerated: true<br>
ColorAutoGenerated: true<br>
Debug: Off<br>
Modified Time: 8347894<br>
Representations:<br>
Binary labelmap:<br>
ClassName: vtkOrientedImageData<br>
Origin: -14.9414 -14.9414 -129.807<br>
Spacing: 0.11719 0.11719 0.4<br>
Extent: 0 255 0 255 0 39<br>
Scalar type: unsigned char<br>
Number of components: 1<br>
IJKToRASDirections:<br>
1 0 0<br>
0 1 -1.28205e-07<br>
0 0 1<br>
Tags:<br>
TerminologyEntry: Segmentation category and type - 3D Slicer General Anatomy list~SCT^85756007^Tissue~SCT^85756007^Tissue~^^~Anatomic codes - DICOM master list~^^~^^<br>
Segment converter:<br>
Debug: Off<br>
Modified Time: 8096804<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Rules:<br>
Rule[0]:<br>
Name: Binary labelmap to closed surface<br>
SourceRepresentationName: Binary labelmap<br>
TargetRepresentationName: Closed surface<br>
ConversionParameters:<br>
Decimation factor: 0.0 [Desired reduction in the total number of polygons. Range: 0.0 (no decimation) to 1.0 (as much simplification as possible). Value of 0.8 typically reduces data set size by 80% without losing too much details.]<br>
Smoothing factor: 0.5 [Smoothing factor. Range: 0.0 (no smoothing) to 1.0 (strong smoothing).]<br>
Compute surface normals: 1 [Compute surface normals. 1 (default) = surface normals are computed. 0 = surface normals are not computed (slightly faster but produces less smooth surface display, not used if vtkSurfaceNets3D is used).]<br>
Conversion method: 0 [Conversion method. 0 (default) = vtkDiscreteFlyingEdges3D is used to generate closed surface.1 = vtkSurfaceNets3D (more performant than flying edges).]<br>
SurfaceNets smoothing: 0 [SurfaceNets smoothing. 0 (default) = Smoothing done by vtkWindowedSincPolyDataFilter1 = Smoothing done in surface nets filter.]<br>
Joint smoothing: 0 [Perform joint smoothing.]<br>
Debug: Off<br>
Modified Time: 8096806<br>
Reference Count: 2<br>
Registered Events: (none)<br>
Rule[1]:<br>
Name: Closed surface to binary labelmap (simple image stencil)<br>
SourceRepresentationName: Closed surface<br>
TargetRepresentationName: Binary labelmap<br>
ConversionParameters:<br>
Reference image geometry: 0.11718999999999999;0;0;-14.941405999999999;0;0.11718999999999999;-5.128205128921935e-8;-14.94140500000001;0;0;0.40000017948717936;-129.74360700000003;0;0;0;1;0;255;0;255;0;39; [Image geometry description string determining the geometry of the labelmap that is created in course of conversion. Can be copied from a volume, using the button.]<br>
Oversampling factor: 1 [Determines the oversampling of the reference image geometry. If it’s a number, then all segments are oversampled with the same value (value of 1 means no oversampling). If it has the value “A”, then automatic oversampling is calculated.]<br>
Crop to reference image geometry: 0 [Crop the model to the extent of reference geometry. 0 (default) = created labelmap will contain the entire model. 1 = created labelmap extent will be within reference image extent.]<br>
Collapse labelmaps: 1 [Merge the labelmaps into as few shared labelmaps as possible 1 = created labelmaps will be shared if possible without overwriting each other.]<br>
Debug: Off<br>
Modified Time: 8096808<br>
Reference Count: 2<br>
Registered Events: (none)<br>
Rule[2]:<br>
Name: Closed surface to fractional labelmap (simple image stencil)<br>
SourceRepresentationName: Closed surface<br>
TargetRepresentationName: Fractional labelmap<br>
ConversionParameters:<br>
Reference image geometry: 0.11718999999999999;0;0;-14.941405999999999;0;0.11718999999999999;-5.128205128921935e-8;-14.94140500000001;0;0;0.40000017948717936;-129.74360700000003;0;0;0;1;0;255;0;255;0;39; [Image geometry description string determining the geometry of the labelmap that is created in course of conversion. Can be copied from a volume, using the button.]<br>
Oversampling factor: 1 [Determines the oversampling of the reference image geometry. If it’s a number, then all segments are oversampled with the same value (value of 1 means no oversampling). If it has the value “A”, then automatic oversampling is calculated.]<br>
Crop to reference image geometry: 0 [Crop the model to the extent of reference geometry. 0 (default) = created labelmap will contain the entire model. 1 = created labelmap extent will be within reference image extent.]<br>
Collapse labelmaps: 1 [Merge the labelmaps into as few shared labelmaps as possible 1 = created labelmaps will be shared if possible without overwriting each other.]<br>
Debug: Off<br>
Modified Time: 8096810<br>
Reference Count: 2<br>
Registered Events: (none)<br>
Rule[3]:<br>
Name: Fractional labelmap to closed surface<br>
SourceRepresentationName: Fractional labelmap<br>
TargetRepresentationName: Closed surface<br>
ConversionParameters:<br>
Decimation factor: 0.0 [Desired reduction in the total number of polygons. Range: 0.0 (no decimation) to 1.0 (as much simplification as possible). Value of 0.8 typically reduces data set size by 80% without losing too much details.]<br>
Smoothing factor: 0.5 [Smoothing factor. Range: 0.0 (no smoothing) to 1.0 (strong smoothing).]<br>
Compute surface normals: 1 [Compute surface normals. 1 (default) = surface normals are computed. 0 = surface normals are not computed (slightly faster but produces less smooth surface display, not used if vtkSurfaceNets3D is used).]<br>
Conversion method: 0 [Conversion method. 0 (default) = vtkDiscreteFlyingEdges3D is used to generate closed surface.1 = vtkSurfaceNets3D (more performant than flying edges).]<br>
SurfaceNets smoothing: 0 [SurfaceNets smoothing. 0 (default) = Smoothing done by vtkWindowedSincPolyDataFilter1 = Smoothing done in surface nets filter.]<br>
Joint smoothing: 0 [Perform joint smoothing.]<br>
Fractional labelmap oversampling factor: 1 [Determines the oversampling of the reference image geometry. All segments are oversampled with the same value (value of 1 means no oversampling).]<br>
Threshold fraction: 0.5 [Determines the threshold that the closed surface is created at as a fractional value between 0 and 1.]<br>
Debug: Off<br>
Modified Time: 8096812<br>
Reference Count: 2<br>
Registered Events: (none)</p>
</blockquote>
</blockquote>
</blockquote>

---
