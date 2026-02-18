# Loading GE Ultrasound 

**Topic ID**: 40298
**Date**: 2024-11-20
**URL**: https://discourse.slicer.org/t/loading-ge-ultrasound/40298

---

## Post #1 by @ipintos (2024-11-20 21:02 UTC)

<p>Hi all,</p>
<p>I have a set of US data from a couple of patients that were exported from EchoPAC with the idea of working with raw data to train an AI model. The folder structure is:</p>
<pre><code class="lang-auto">TEST02
---DICOMDIR
---GEMS_DB
      |____ArcAudit.dbs
      |____ArcData.dbs
      |____ArcParam.dbs
      |____Master.db
      |____Master.log
---GEMS_IMG
      |____---2019_DEC
               |____---16
                        |____---JV123120
                                 |____JCGCLG3C
                                 |____JCGCLK3E
                                 |____ ...
</code></pre>
<p>I installed the SlicerHeart extension and followed the instructions in <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md" class="inline-onebox" rel="noopener nofollow ugc">SlicerHeart/Docs/ImageImportExport.md at master · SlicerHeart/SlicerHeart · GitHub</a> (I got the DLL file and run regsvr32 Image3dLoaderGe.dll as administrator). Then I load the data from the DICOM database using the DICOMDIR file. As a result only two volumes (out of 68 files) get loaded as 3D volumes with time, each with an ECG table as shown in the image.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/405b2468a28c2e52e24dc33bddd671251312d12c.png" data-download-href="/uploads/short-url/9bjPqhwbCdQaGBmWPJijAWLGubG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/405b2468a28c2e52e24dc33bddd671251312d12c_2_690x357.png" alt="image" data-base62-sha1="9bjPqhwbCdQaGBmWPJijAWLGubG" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/405b2468a28c2e52e24dc33bddd671251312d12c_2_690x357.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/405b2468a28c2e52e24dc33bddd671251312d12c_2_1035x535.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/405b2468a28c2e52e24dc33bddd671251312d12c_2_1380x714.png 2x" data-dominant-color="312F2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1915×992 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The remaining files fail to load as US, but I can drop them and load as volumes. Though in that case they look like screen shots as shown below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1ba2ab5d5fbabebc6d98cf3add0831cb76359108.jpeg" data-download-href="/uploads/short-url/3WtpneAYJX7RnePPIj2CXE9MtMA.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1ba2ab5d5fbabebc6d98cf3add0831cb76359108_2_690x357.jpeg" alt="image" data-base62-sha1="3WtpneAYJX7RnePPIj2CXE9MtMA" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1ba2ab5d5fbabebc6d98cf3add0831cb76359108_2_690x357.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1ba2ab5d5fbabebc6d98cf3add0831cb76359108_2_1035x535.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1ba2ab5d5fbabebc6d98cf3add0831cb76359108_2_1380x714.jpeg 2x" data-dominant-color="262529"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×993 205 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For the other patient data, which has the same structure, when loading with the DICOMDIR I get a warning message:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a556703c23c6c2a6cad00406f76d269929907df.png" data-download-href="/uploads/short-url/hsddXElas4aUH5StM0I8P1YNAmz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a556703c23c6c2a6cad00406f76d269929907df.png" alt="image" data-base62-sha1="hsddXElas4aUH5StM0I8P1YNAmz" width="526" height="206"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">526×206 11.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and when loaded the shape of the image is rectangular and no table appears, though the frame sequence runs with time.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72dc643b50eaf27230c777d695ba255c68f979f3.png" data-download-href="/uploads/short-url/go6CkLNIToDjJ3VGW3f9rN9iLBx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72dc643b50eaf27230c777d695ba255c68f979f3_2_690x357.png" alt="image" data-base62-sha1="go6CkLNIToDjJ3VGW3f9rN9iLBx" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72dc643b50eaf27230c777d695ba255c68f979f3_2_690x357.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72dc643b50eaf27230c777d695ba255c68f979f3_2_1035x535.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72dc643b50eaf27230c777d695ba255c68f979f3_2_1380x714.png 2x" data-dominant-color="262629"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×993 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How can I load all the data correctly? or is there a problem with the data? In that case, anyone knows how to export it to get all the infor and correct formats?</p>
<p>Operating system: Windows 11<br>
Slicer version: 5.6.2</p>

---

## Post #2 by @lassoan (2024-11-20 21:11 UTC)

<p>Loading of 3D+t ultrasound images look good.</p>
<p>You also seem to have some 2D+t ultrasound acquisitions, which are essentially screen captures from the ultrasound system. They are usually littered with burnt-in annotations and they are only 2D, but you can still make 2D measurements on them.</p>
<p>We improved import of these images in recent Slicer Preview Releases, so I would recommend to use that instead of the latest Slicer Stable Release (currently Slicer-5.6.2).</p>
<p>You may also find the <a href="https://github.com/SlicerUltrasound/SlicerUltrasound"><code>Ultrasound</code> extension</a> useful. It can help with post-processing and annotating ultrasound image sequences for deep learning training.</p>

---
