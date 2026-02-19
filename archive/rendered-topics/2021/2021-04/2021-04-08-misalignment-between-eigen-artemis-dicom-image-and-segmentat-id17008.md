---
topic_id: 17008
title: "Misalignment Between Eigen Artemis Dicom Image And Segmentat"
date: 2021-04-08
url: https://discourse.slicer.org/t/17008
---

# Misalignment between Eigen Artemis DICOM image and segmentation

**Topic ID**: 17008
**Date**: 2021-04-08
**URL**: https://discourse.slicer.org/t/misalignment-between-eigen-artemis-dicom-image-and-segmentation/17008

---

## Post #1 by @sulaimanvesal (2021-04-08 22:09 UTC)

<p>Hi,</p>
<p>I wanted to ask this point, that why my segmentation output during export placed at the corner of NRRD volume. Even though the volume origin is at (0.0, 0.0, 0.0).<br>
Below is the code that I am using to export a vtk model to a segmentation label map.</p>
<pre><code># Center the view
layoutManager = slicer.app.layoutManager()
threeDWidget = layoutManager.threeDWidget(0)
threeDView = threeDWidget.threeDView()
threeDView.resetFocalPoint()

usPath =  "/Volumes/REC00000" 
segPath = "/Volumes/SURFRCON.vtk"

volumeNode   = slicer.util.loadVolume(usPath)
prostateNode = slicer.util.loadModel(segPath)

seg = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
seg.SetReferenceImageGeometryParameterFromVolumeNode(volumeNode)
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(prostateNode, seg)
# seg.CreateBinaryLabelmapRepresentation()

labelmapVolumeNode1 = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(seg, labelmapVolumeNode1, volumeNode)

outputpath = "/Volumes/test.nrrd"
slicer.util.saveNode(labelmapVolumeNode1, outputpath)
slicer.mrmlScene.RemoveNode(labelmapVolumeNode1)
slicer.mrmlScene.Clear(0)
</code></pre>
<p>This is the output of GetOrigin(), GetSpacing() for reference volume (volumeNode) and exported NRRD (test.nrrd) .</p>
<pre><code>test.nrrd:(0.0, 0.0, 0.0) (0.37800000000000006, 0.37800000000000006, 1.0)
REC00000: (0.0, 0.0, 0.0) (0.37800000000000006, 0.37800000000000006, 1.0)
</code></pre>
<p>This is also the nrrd output. As you can see the segmentation map is centered in upper right corner.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afe9109910a25a61a322c898ce209e231bfa1a40.png" data-download-href="/uploads/short-url/p6aTzTM4aTwifVt1igY0QJmhEqs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afe9109910a25a61a322c898ce209e231bfa1a40.png" alt="image" data-base62-sha1="p6aTzTM4aTwifVt1igY0QJmhEqs" width="557" height="500" data-dominant-color="080809"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">732×656 5.99 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @sulaimanvesal (2021-04-10 06:17 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Could you please help me with this problem?</p>

---

## Post #3 by @lassoan (2021-04-10 15:25 UTC)

<p>Volume origin is defined in physical space: IJK=(0,0,0) voxel content will be whatever is in the segmentation at the physical RAS=(0,0,0) position.</p>

---

## Post #4 by @sulaimanvesal (2021-04-13 16:35 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> , I have checked my data and as you correctly mentioned, my volumeNode is in IJK coordinate and my vtk mesh file is in RAS coordinate (with different origin and pixel spacing).</p>
<p>I looked in the forum on how to convert RAS to IJK coordinates but could not really make it. I was wondering if there is a python example that can help me!</p>
<p>Another question is that should I export my vtk mesh file from RAS to IJK before ExportVisibleSegmentsToLabelmapNode or after?</p>

---

## Post #5 by @lassoan (2021-04-13 16:49 UTC)

<p>You can find example to IJK&lt;-&gt;RAS conversions in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates">script repository</a>.</p>

---

## Post #6 by @sulaimanvesal (2021-04-15 18:51 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>I could figure it out the problem and could align the volume with segmentation label map using the following piece of code (I know centering the volume in this way is not recommended but since I am just exporting the label maps to NRRD for my segmentation task, and it solved my issue):</p>
<pre><code># Center volume 
if center_volume:
     volumesLogic = slicer.modules.volumes.logic()
     volumesLogic.CenterVolume(volumeNode)
</code></pre>
<p>I explored my multi-frames DICOM images and I noticed that I am working with raw data. It means the DICOM header does not have the <strong>PixelSpacing</strong> tag, but that information stored in metadata as a private tag. When I load the images into the 3D Slicer, it automatically map the volume to a pixel spacing of <strong>[1.0 , 1.0, 1.0] mm</strong> and origin of <strong>[0.0, 0.0, 0.0]</strong>.</p>
<p>I was wondering if there is any way, that we can tell the Slicer to pick the Pixel-Spacing from the private tag when we load the data? I tried to resample the data but it was not a practical approach.</p>
<ol>
<li>
<p>I realized, what if I add a new tag to DICOM headers of my RAW DICOMS as “PixelSpacing” and copy the information from private tag and store it as a new DICOM file, would it load on 3D Slicer correctly? I am not sure.</p>
<p>(1129, 1004) Private tag data                    IS: [67, 3899, 2884, -4096]<br>
(1129, 1005) Private tag data                    IS: [67, 3899, 543, -4096]<br>
(1129, 1008) Private tag data                    DS: “0.0”<br>
(1129, 1015) Private tag data                    IS: “4096”<br>
(1129, 1016) Private tag data                    DS: [0.24960000813007, 0.24960000813007, 0.24960000813007]<br>
(1129, 1017) Private tag data                    DS: “4.0”<br>
(1129, 1023) Private tag data                    IS: “4”</p>
</li>
</ol>
<p>Best.</p>

---

## Post #7 by @lassoan (2021-04-15 19:14 UTC)

<p>In general, basic image metadata, such as pixel spacing must not be stored in private tags. Unfortunately, some imaging vendors do use private tags (and it takes time to convince them to better adhere to standards) and for these cases we add DICOM plugins to retrieve and use metadata in private fields.</p>
<p>The <code>(1129, 1016)</code> tag is used by Eigen Artemis 3D ultrasound systems to store pixel spacing information. We already have a plugin for this device in SlicerHeart extension. All you need to do is to install SlicerHeart extension and the <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/DicomUltrasoundPlugin/DicomUltrasoundPlugin.py">DICOMUltrasoundPlugin</a> will recognize this image and load it correctly.</p>

---

## Post #8 by @sulaimanvesal (2021-04-16 15:34 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for your always support. You are correct, my images come for Eigen Artemis 3D ultrasound system.<br>
I have installed SlicerHeart as you said and I can see it in the list of plugins on DICOM module when I load my DICOM images. However, it does not work and it loads the data as 2D image only rather multi-frame 3D like before. When you go to volume module the origin and spacing again pointing at [1.0, 1.0, 1.0] and [0.0 ,0.0, 0.0].</p>
<p>I copied the python function <strong>examineEigenArtemis3DUS</strong> form <strong>DICOMUltrasoundPlugin</strong> for troubleshooting and tested manually on Jupyter. For outputSpace and OutputOrigin, it gives me the correct conversion when I give a test sample:</p>
<pre><code>OutputSpace: [0.24960000813007, 0.24960000813007, 0.24960000813007] 
OutputOrigin: [61.90080201625736, 61.90080201625736, -36.31680118292518] 
</code></pre>
<p>I was wondering, if I can use this new OutputSpace and OutputOrigin to enforce Slicer python use them as the coordinates when I call slicer.util.loadVolume, rather than the default spacing and origin.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf36c4ab1284920d8362048dbbd43732fb9f8c76.jpeg" data-download-href="/uploads/short-url/tz6aXz3TbNuJGZkNoVnvaUy6WzA.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf36c4ab1284920d8362048dbbd43732fb9f8c76_2_594x500.jpeg" alt="image" data-base62-sha1="tz6aXz3TbNuJGZkNoVnvaUy6WzA" width="594" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf36c4ab1284920d8362048dbbd43732fb9f8c76_2_594x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf36c4ab1284920d8362048dbbd43732fb9f8c76_2_891x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf36c4ab1284920d8362048dbbd43732fb9f8c76_2_1188x1000.jpeg 2x" data-dominant-color="31313C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2426×2040 219 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/599ac1e65df03ce6a274b66234b0ba16158b3709.png" data-download-href="/uploads/short-url/cMG3MVFOdMYnUC24eb2fKcwg8sx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/599ac1e65df03ce6a274b66234b0ba16158b3709_2_690x460.png" alt="image" data-base62-sha1="cMG3MVFOdMYnUC24eb2fKcwg8sx" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/599ac1e65df03ce6a274b66234b0ba16158b3709_2_690x460.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/599ac1e65df03ce6a274b66234b0ba16158b3709_2_1035x690.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/599ac1e65df03ce6a274b66234b0ba16158b3709_2_1380x920.png 2x" data-dominant-color="E8E8E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1406×938 55.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2021-04-16 15:52 UTC)

<p>Make sure your SlicerHeart extension is up-to-date. Either install latest Slicer Stable Release and update SlicerHeart extension; or install latest Slicer Preview Release and install SlicerHeart extension.</p>
<p>For example, <a href="https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=68550661">Artemis images that are available in TCIA</a> load perfectly with latest Slicer Preview Release:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3000cbc823238729359ba6834206e7b07182592.jpeg" data-download-href="/uploads/short-url/u6AQSnCzlhiPFhsLPg4ab0xQssG.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3000cbc823238729359ba6834206e7b07182592_2_690x302.jpeg" alt="image" data-base62-sha1="u6AQSnCzlhiPFhsLPg4ab0xQssG" width="690" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3000cbc823238729359ba6834206e7b07182592_2_690x302.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3000cbc823238729359ba6834206e7b07182592_2_1035x453.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3000cbc823238729359ba6834206e7b07182592_2_1380x604.jpeg 2x" data-dominant-color="313231"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1915×839 300 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @sulaimanvesal (2021-04-16 17:44 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I downgraded my Slicer to up-to-date stable version. To make sure everything works perfectly, I downloaded the TICA data as well.</p>
<p>Here is as you see: the top row is the same image that you loaded and the second row is our internal data (both Artemis).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c368733001136d1424f63d0e4fd375c791d590d8.jpeg" data-download-href="/uploads/short-url/rSETa6CvqcNpqTQRQSiURjyRBRm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c368733001136d1424f63d0e4fd375c791d590d8_2_690x397.jpeg" alt="image" data-base62-sha1="rSETa6CvqcNpqTQRQSiURjyRBRm" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c368733001136d1424f63d0e4fd375c791d590d8_2_690x397.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c368733001136d1424f63d0e4fd375c791d590d8_2_1035x595.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c368733001136d1424f63d0e4fd375c791d590d8_2_1380x794.jpeg 2x" data-dominant-color="232322"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3838×2210 809 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>One thing I noticed that when I load our own data, gets the following warning:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40dac1d6de027eb76a3e9180a58bee4af2a87f4e.png" data-download-href="/uploads/short-url/9fJf4V7Kvp2TdXwdcVRp18XZXIO.png?dl=1" title="Screen Shot 2021-04-16 at 10.26.52 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40dac1d6de027eb76a3e9180a58bee4af2a87f4e.png" alt="Screen Shot 2021-04-16 at 10.26.52 AM" data-base62-sha1="9fJf4V7Kvp2TdXwdcVRp18XZXIO" width="690" height="416" data-dominant-color="434344"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-04-16 at 10.26.52 AM</span><span class="informations">844×510 45.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is the metadata tag list that we have for my internal DICOM (sorry I can’t send you a sample), I thought maybe there is a difference in terms of tags naming or something else that give the warning and cause this problem in <strong>DICOMUltrasoundPlugin</strong>.</p>
<pre><code>Dataset.file_meta -------------------------------
(0002, 0002) Media Storage SOP Class UID         UI: Ultrasound Multi-frame Image Storage
(0002, 0013) Implementation Version Name         SH: 'EIGEN_361'
(0002, 0016) Source Application Entity Title     AE: 'ARTEMIS'
-------------------------------------------------
(0008, 0020) Date                          DA: '2015'
(0008, 0064) Conversion Type                     CS: 'SYN'
(0008, 0070) Manufacturer                        LO: 'Eigen'
(0018, 1020) Software Versions                   LO: '2.3.0.81'
(0018, 106a) Synchronization Trigger             CS: 'EXTERNAL'
(0018, 5010) Transducer Data                     LO: ['Hitachi', 'Noblus', 'Hitachi C41V']
(0020, 0200) Synchronization Frame of Reference  UI: Universal Coordinated Time
(0028, 0002) Samples per Pixel                   US: 1
(0028, 0004) Photometric Interpretation          CS: 'MONOCHROME2'
(0028, 0008) Number of Frames                    IS: "291"
(0028, 0009) Frame Increment Pointer             AT: (0054, 0080)
(0028, 0010) Rows                                US: 496
(0028, 0011) Columns                             US: 496
(0028, 0034) Pixel Aspect Ratio                  IS: [249, 249]
(0028, 0100) Bits Allocated                      US: 8
(0028, 0101) Bits Stored                         US: 8
(0028, 0102) High Bit                            US: 7
(0028, 0103) Pixel Representation                US: 0
(0028, 1050) Window Center                       DS: "50.0"
(0028, 1051) Window Width                        DS: "0.0"
(0054, 0081) Number of Slices                    US: 291
(1129, 0010) Private Creator                     LO: 'Eigen, Inc'
(1129, 1002) Private tag data                    LO: 'EigProc67'
(1129, 1008) Private tag data                    DS: "0.0"
(1129, 1016) Private tag data                    DS: [0.24960000813007, 0.24960000813007, 0.24960000813007]
(1129, 1017) Private tag data                    DS: "4.0"
</code></pre>

---

## Post #11 by @lassoan (2021-04-16 19:57 UTC)

<p>You can fix up the current plugin to make it read your images as well. It is just a Python script and you can attach a debugger to go through the code step by step to see why it is not recognized.</p>
<p>If that does not work for you then please acquire image of a phantom (or even an empty water tank) and send us that image.</p>

---

## Post #12 by @sulaimanvesal (2021-04-17 00:18 UTC)

<p>Thanks a lot <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I found the error after debugging the python code.  In my Ultrasound DICOM images the PixelSpacingPrivateTag store the values as a list e.g. [0.17, 017, 017], while in TCIA data the PixelSpacingPrivateTag value is a single value e.g. 0.17. The code needs to be updated so it can consider both list and single value otherwise float () throw the error.</p>
<p>This was the fix that I made in the current plugin, not a very fancy way as the return of <code>ds[pixelSpacingPrivateTag].value</code> is sometimes object:</p>
<pre><code>try:
   pixelSpacingPrivate = float(ds[pixelSpacingPrivateTag].value)
except:
   pixelSpacingPrivate = ds[pixelSpacingPrivateTag].value
   pixelSpacingPrivate = float(pixelSpacingPrivate[0])
</code></pre>
<p>I am almost there, this fix nicely solved my issue with TCIA data and STL files alignment (the one that I had problem with centering the volumes). I can’t understand why the vendors don’t follow the same standards for DICOM header, that could save alot of time.</p>
<p>Just one last small problem still here. My local data has gland segmentation as vtk file. If you look at the screenshot it looks like the axial/coronal/sagittal views for vtk model miss-placed. The vtk file generated originally based on the same Ultrasound volumes. Do you have any suggestion on how to correct this issue. I checked the RAS and LPS version when I load vtks but none of them correct the issue.</p>
<p>As I said, this problem is not exist anymore with TCIA data and they are nicely aligned.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fdee5bc87308e837a6783d627d8f4d3f853ba39.jpeg" data-download-href="/uploads/short-url/dG6UJYCXtFIlM8MPf8i1euKhyBz.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5fdee5bc87308e837a6783d627d8f4d3f853ba39_2_690x397.jpeg" alt="image" data-base62-sha1="dG6UJYCXtFIlM8MPf8i1euKhyBz" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5fdee5bc87308e837a6783d627d8f4d3f853ba39_2_690x397.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5fdee5bc87308e837a6783d627d8f4d3f853ba39_2_1035x595.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5fdee5bc87308e837a6783d627d8f4d3f853ba39_2_1380x794.jpeg 2x" data-dominant-color="38383F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3838×2210 780 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #13 by @lassoan (2021-04-17 01:08 UTC)

<p>If you have 3 pixel spacing values then read all 3 and set them in the volume node as x, y, z spacing. If it works well then please send a pull request. Please also add a comment that Artemis Eigen 2.3.0.81 software version generates such images.</p>

---

## Post #14 by @sulaimanvesal (2021-04-18 05:56 UTC)

<p>Actually, the pixel spacing values in my data are always the same. However, I set them in the volume node as x,y,z, but it gives a warning and Slicer load them with default origin and spacing. There should be a fix for this probably.</p>
<p>Regarding the issue that i mentioned for my local data miss-alignment, the following transformation with rotating the model [-90, 0.0, -90], aligned the vtk with Ultrasound volume. However, I wish Slicer could solve this rather than applying transformation.</p>
<p>I will create a pull request on Github though and report the fix for Artemis.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c82c1b8f3d6b8b8e4ad2c15ecdecd38a4c8e2594.jpeg" data-download-href="/uploads/short-url/syNZE6nDJKcZDZpgafjbrnEnb9i.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c82c1b8f3d6b8b8e4ad2c15ecdecd38a4c8e2594_2_690x386.jpeg" alt="image" data-base62-sha1="syNZE6nDJKcZDZpgafjbrnEnb9i" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c82c1b8f3d6b8b8e4ad2c15ecdecd38a4c8e2594_2_690x386.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c82c1b8f3d6b8b8e4ad2c15ecdecd38a4c8e2594_2_1035x579.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c82c1b8f3d6b8b8e4ad2c15ecdecd38a4c8e2594_2_1380x772.jpeg 2x" data-dominant-color="3B3B41"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3836×2148 835 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #15 by @lassoan (2021-04-18 15:31 UTC)

<aside class="quote no-group" data-username="sulaimanvesal" data-post="14" data-topic="17008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sulaimanvesal/48/10463_2.png" class="avatar"> sulaimanvesal:</div>
<blockquote>
<p>However, I set them in the volume node as x,y,z, but it gives a warning</p>
</blockquote>
</aside>
<p>Can you copy here the entire warning message?</p>
<aside class="quote no-group" data-username="sulaimanvesal" data-post="14" data-topic="17008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sulaimanvesal/48/10463_2.png" class="avatar"> sulaimanvesal:</div>
<blockquote>
<p>Regarding the issue that i mentioned for my local data miss-alignment, the following transformation with rotating the model [-90, 0.0, -90], aligned the vtk with Ultrasound volume.</p>
</blockquote>
</aside>
<p>In medical image computing, LPS coordinate system is used most commonly (x=patient left, y=patient posterior, z=patient superior). Therefore if directions of an image or model are known relative to a patient then it makes the most sense to use this convention.</p>
<p>In ultrasound imaging, the probe can be placed on the patient in various orientations, so often you have no clue how image axes relate to patient axes. However, due to human anatomy, endocavity ultrasound probes are quite constrained in their insertion direction, so you can have a good approximation for image to patient matrix for a specific device. This is why the Artemis DICOM plugin applies a rotation in its IJK to RAS matrix:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerHeart/SlicerHeart/blob/d8f9b6e45ddc3b869046c151210f3dae0b80eb82/DicomUltrasoundPlugin/DicomUltrasoundPlugin.py#L800-L810">
  <header class="source">

      <a href="https://github.com/SlicerHeart/SlicerHeart/blob/d8f9b6e45ddc3b869046c151210f3dae0b80eb82/DicomUltrasoundPlugin/DicomUltrasoundPlugin.py#L800-L810" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerHeart/SlicerHeart/blob/d8f9b6e45ddc3b869046c151210f3dae0b80eb82/DicomUltrasoundPlugin/DicomUltrasoundPlugin.py#L800-L810" target="_blank" rel="noopener">SlicerHeart/SlicerHeart/blob/d8f9b6e45ddc3b869046c151210f3dae0b80eb82/DicomUltrasoundPlugin/DicomUltrasoundPlugin.py#L800-L810</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="800" style="counter-reset: li-counter 799 ;">
          <li>outputVolume.GetIJKToRASMatrix(ijk2ras)</li>
          <li></li>
          <li>rot = vtk.vtkMatrix4x4()</li>
          <li>rot.DeepCopy((0, 1, 0, 0,</li>
          <li>              0, 0, 1, 0,</li>
          <li>              1, 0, 0, 0,</li>
          <li>              0, 0, 0, 1))</li>
          <li></li>
          <li>ijk2ras_updated = vtk.vtkMatrix4x4()</li>
          <li>ijk2ras.Multiply4x4(rot, ijk2ras, ijk2ras_updated)</li>
          <li>outputVolume.SetIJKToRASMatrix(ijk2ras_updated)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I understand that this rotation may be unexpected, but it is not arbitrary and I would encourage you to apply the same rotation matrix to the model loaded model.</p>
<p>The only better solution I can think of is would be if Eigen better adhered to DICOM standard and specified image axes in LPS coordinate systems in the first place.</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> Are you in contact with Eigen? Do you know about this ambiguity of the spacing field content (sometimes contains one value, sometimes contains a sequence of 3 values)? Do you know if they are aware that their lack of following DICOM standard or conventions is causing trouble for users?</p>

---

## Post #17 by @fedorov (2021-04-22 15:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="17008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/fedorov">@fedorov</a> Are you in contact with Eigen? Do you know about this ambiguity of the spacing field content (sometimes contains one value, sometimes contains a sequence of 3 values)? Do you know if they are aware that their lack of following DICOM standard or conventions is causing trouble for users?</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> no, I am not in constant contact with Eigen. I do know someone at Eigen, who may have more insight on this, and I will forward the thread. However, based on my experience, I don’t recall when vendors were eager to address this kind of issues raised by researchers. For anything to change, those should be raised by paying customers. I am afraid the reality is that 1) lack of following DICOM standard or conventions as in this example often <strong>does not</strong> cause troubles for <strong>paying</strong> users (clinical users); 2) attempts to follow the standard precisely <strong>may</strong> cause troubles for paying users, because the downstream systems working with the data may not be able to deal with the proper implementation of the standard.</p>
<p>I agree we all should keep raising those issues with the vendors. But most importantly, I hope that paying customers do this more often.</p>

---

## Post #18 by @sulaimanvesal (2021-04-28 06:11 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Sorry for not responding as I was kinda sick for past few days. Thank you so much for detailed response.</p>
<p>Actually, I have solved all my issues. I found the reason behind that missalignment between the 3D Ultrasound image and mesh file after correcting the pixel-spacing and origin. For Eigen Artmeis ultrasound images, there is no tag for patient orientation information and they don’t  even store it as private tag. So I needed a transformation ([0, 1, 0, 0, 0, 1, 1, 0, 0] to apply to all mesh files, and it worked well (I saw now your comment that you also pointed this out).</p>
<p>One more bug that I found in “DICOMULtrasoundPlugin” for Eigen Artemis function that it always takes the private tag as final output-spacing. However, in my dataset I had images that had both standard ds.PixelSpacing tag and also private tag (the values were different, and the correct spacing was the one from ds.PixelSpacing). So, for these type of the images the code should choose the default ds.PixelSpacing to correctly show the images. I have corrected in my version of plugin code, and I thought to share it here also. I am not sure, how common this can be, but for my dataset I found some cases.</p>

---
