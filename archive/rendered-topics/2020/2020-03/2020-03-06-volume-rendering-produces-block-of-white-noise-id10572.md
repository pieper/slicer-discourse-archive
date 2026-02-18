# Volume rendering produces block of "white noise"

**Topic ID**: 10572
**Date**: 2020-03-06
**URL**: https://discourse.slicer.org/t/volume-rendering-produces-block-of-white-noise/10572

---

## Post #1 by @Mark_1 (2020-03-06 00:05 UTC)

<p>Hello,</p>
<p>I’m very new to using 3D Slicer (this is my first day) so apologies if this is a very basic issue, but I’ve been trying to produce a volume render of a microCT scan of a skull and all that I get is a block of white noise:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/851a67b5943f9809b5f8b9ffdb0af6ae953f12f6.jpeg" data-download-href="/uploads/short-url/iZu4Jar2udYEbllmzBsrAbL4kMm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/851a67b5943f9809b5f8b9ffdb0af6ae953f12f6_2_690x420.jpeg" alt="image" data-base62-sha1="iZu4Jar2udYEbllmzBsrAbL4kMm" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/851a67b5943f9809b5f8b9ffdb0af6ae953f12f6_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/851a67b5943f9809b5f8b9ffdb0af6ae953f12f6_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/851a67b5943f9809b5f8b9ffdb0af6ae953f12f6_2_1380x840.jpeg 2x" data-dominant-color="A1A3B1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1170 487 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I’ve tried all the different presets and played around with the volume properties, but to no avail. I’m able to render volumes from other datasets like MRHead and CTChest with no problem.</p>
<p>The dataset I’m trying to render is this scan of a primate skull from MorphoSource: <a href="https://www.morphosource.org/index.php/Detail/MediaDetail/Show/media_file_id/4390" rel="noopener nofollow ugc">https://www.morphosource.org/index.php/Detail/MediaDetail/Show/media_file_id/4390</a>. I initially had some problems loading this dataset and had to use the DICOM Patcher to fix the files, so I don’t know whether I’m just not handling this particular dataset correctly? I’ve had a look through other similar posts about volume rendering issues but I’m afraid I’m still at a loss, so any help or advice would be appreciated.</p>
<p>Many thanks.</p>
<p>Operating system: Windows 10 Pro 64-bit<br>
Slicer version: 4.10.2</p>

---

## Post #2 by @pieper (2020-03-06 02:13 UTC)

<p>Thanks for providing the link to the data and the steps to reproduce.  The data is super high-res (and quite beautiful) so you’ll need to play around for a bit.  This data pushes the limits.</p>
<p>What I did to get the image below:</p>
<ul>
<li>downloaded from mophosource</li>
<li>unzip and ran through the dicompatcher as you suggested</li>
<li>imported to database and loaded</li>
<li>went into the Volume Rendering module</li>
<li>GPU volume rendering did nothing (error message in log about failure to allocate - means the volume is too big)</li>
<li>switched to CPU rendering and waited</li>
<li>dragged the Shift slider to get reasonable image</li>
</ul>
<p>I suggest avoiding the presets for this data, since it’s not like what they were designed for.  Instead, start with the default and use the shift to get something good.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/581c6ecb6503d921b840d0d75a0434978da42ce7.jpeg" data-download-href="/uploads/short-url/czsVVJloNkTi7amUKJATCfMgHHN.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/581c6ecb6503d921b840d0d75a0434978da42ce7_2_690x467.jpeg" alt="image" data-base62-sha1="czsVVJloNkTi7amUKJATCfMgHHN" width="690" height="467" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/581c6ecb6503d921b840d0d75a0434978da42ce7_2_690x467.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/581c6ecb6503d921b840d0d75a0434978da42ce7_2_1035x700.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/581c6ecb6503d921b840d0d75a0434978da42ce7_2_1380x934.jpeg 2x" data-dominant-color="98989A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1668×1130 477 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Also I think this data is such high resolution it doesn’t work well with the internal volume rendering assumptions and calculations (makes it a good test case for the volume renderer).  But fortunately if you downsample, e.g. with the Crop Volume module, it is able to load in GPU memory and looks really great.  Here I downsampled by 1/2 in all directions.  Plus it’s much faster to work with in the GPU.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a0f05b80dde8614d46b80b286ca72ab49104f02.jpeg" data-download-href="/uploads/short-url/3IwBagLZHLYINBW2mohiHsSvepk.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a0f05b80dde8614d46b80b286ca72ab49104f02_2_690x474.jpeg" alt="image" data-base62-sha1="3IwBagLZHLYINBW2mohiHsSvepk" width="690" height="474" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a0f05b80dde8614d46b80b286ca72ab49104f02_2_690x474.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a0f05b80dde8614d46b80b286ca72ab49104f02_2_1035x711.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a0f05b80dde8614d46b80b286ca72ab49104f02_2_1380x948.jpeg 2x" data-dominant-color="C8CACC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1632×1122 363 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You can also use the presets with this downsampled data, although they are a bit fiddly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6c213fb63f6411084ea94d49c10069895001bfe.jpeg" data-download-href="/uploads/short-url/smilFkTDSZPsBTvCkw3gMF2n2fc.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c6c213fb63f6411084ea94d49c10069895001bfe_2_690x469.jpeg" alt="image" data-base62-sha1="smilFkTDSZPsBTvCkw3gMF2n2fc" width="690" height="469" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c6c213fb63f6411084ea94d49c10069895001bfe_2_690x469.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c6c213fb63f6411084ea94d49c10069895001bfe_2_1035x703.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c6c213fb63f6411084ea94d49c10069895001bfe_2_1380x938.jpeg 2x" data-dominant-color="DADADA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1639×1115 575 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @muratmaga (2020-03-06 03:11 UTC)

<p>This is actually not a particularly large volume, but it is 16 bit. Depending on what one wants to see, instead of downsampling at the expense of morphological detail, I would suggest changing the intensity range from 16 bit to 8 bit (First rescale then cast. There is short tutorial in SlicerMorph workshop: <a href="https://github.com/SlicerMorph/W_2020/tree/master/Lab11_SlicerPlusPlus#rescalecast" rel="nofollow noopener">https://github.com/SlicerMorph/W_2020/tree/master/Lab11_SlicerPlusPlus#rescalecast</a>)</p>
<p>However, the main issue for consumers of MorphoSource data and SlicerMorphers is these non-standard DICOMs. With the changes, the old shortcut of just dragging and dropping one of the DCM files and bypassing DICOMbrowser no longer works (I get an ITKIO error). Patching is so slow that by the time one is patched, I can open tens of those in fiji manually, and save as NRRD and load them into SLicer. And for some reason DCM2NIIX extension doesnt like this datasets either.</p>
<p>Would it be possible to bring back the DCM drag and drop approach not to core SLicer, but as part of the SlicerMorph extension perhaps? What do you guys think <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #4 by @lassoan (2020-03-06 04:56 UTC)

<p>First of all, MorphoSource must be fixed. It is a shame to have all that valuable data in invalid format. It does not just cause lost time for users but also promotes bad practices. We can help them validating their DICOM files and/or recommend other formats. This fix will solve many issues - failure to import, slow patching, etc.</p>
<p>We haven’t removed the ability to load DICOM files using Add data module, but that is still the plan. If Add data cannot load this then it might mean that this data is just so badly corrupted.</p>
<p>We will improve “time to first image” in the DICOM browser by showing thumbnails. DICOM import and loading speed should be very good already (except <a href="https://issues.slicer.org/view.php?id=4725">this</a> very recent regression that will be fixed soon).</p>

---

## Post #5 by @muratmaga (2020-03-06 05:15 UTC)

<p>I agree that fixing Morphosource would be ideal solution, but unlikely to happen because they only want to act as repository, and my understanding is that they assume data integrity issues are the responsibility of data donors. I can’t speak for them (will forward this thread to Doug Boyer) but I don’t think they have the bandwidth, or the resources to do the conversion. There is a wide variety of groups donating data from different scanners, so each issue is likely to be unique.</p>
<p>As for adding DCM via Add Data, or drag and drop fails with this for sometime now (not just this dataset, but I don’t have anything else right now). FOr whatever’s worth, Fiji reads the sequence fine.</p>
<blockquote>
<p>vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/murat/Downloads/Morphosource_mcz_mamm_23167_M4821-4390/mcz_mamm_23167_M4821-4390/Pan_troglodytes_23167/new_Pan_231671122.dcm. ITK exception info: error in unknown:  Could not create IO object for reading file C:/Users/murat/Downloads/Morphosource_mcz_mamm_23167_M4821-4390/mcz_mamm_23167_M4821-4390/Pan_troglodytes_23167/new_Pan_231671122.dcm<br>
Tried to create one of the following:<br>
BMPImageIO<br>
BioRadImageIO<br>
DCMTKImageIO<br>
GDCMImageIO<br>
GiplImageIO<br>
JPEGImageIO<br>
LSMImageIO<br>
MGHImageIO<br>
MINCImageIO<br>
MRCImageIO<br>
MetaImageIO<br>
NiftiImageIO<br>
NrrdImageIO<br>
PNGImageIO<br>
StimulateImageIO<br>
TIFFImageIO<br>
VTKImageIO<br>
MRMLIDImageIO<br>
Bruker2dseqImageIO<br>
GE4ImageIO<br>
GE5ImageIO<br>
HDF5ImageIO<br>
JPEG2000ImageIO<br>
You probably failed to set a file suffix, or<br>
set the suffix to an unsupported type.</p>
<p>Algorithm vtkITKArchetypeDiffusionTensorImageReaderFile(000001F7F17A96C0) returned failure for request: vtkInformation (000001F791027340)<br>
Debug: Off<br>
Modified Time: 318245<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1</p>
</blockquote>

---

## Post #6 by @Mark_1 (2020-03-06 10:55 UTC)

<p>Thank you all for responding so quickly and for your advice, and thanks <a class="mention" href="/u/pieper">@pieper</a> for working out a solution - I really appreciate it. I had been wondering whether the resolution of the data might have been an issue because the dataset took so much longer to load than the example datasets, so thank you for also answering what might have been my next question about how to reduce the resolution! I probably should have said, but my ultimate goal is to segment/highlight the braincase of this skull and the skulls of several other primates to use as illustrations in my thesis - along the lines of the bird skull below - so I don’t need the images to be anywhere near the resolution that might be required for analysis.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07a5e559689b4682f1542625c273fe55c36e8cdb.png" alt="image" data-base62-sha1="15ELTUBScqYDqRX9ALJpuuZCkUr" width="212" height="113"></p>
<p>Also, it’s interesting to learn about the issues with MorphoSource. I had no idea - at first glance it looks like such a good resource.</p>

---

## Post #7 by @pieper (2020-03-06 13:33 UTC)

<p><a class="mention" href="/u/mark_1">@Mark_1</a> - good luck with your research!</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/lassoan">@lassoan</a> - we face similar challenges with data in other archives <a href="https://www.cancerimagingarchive.net/">TCIA</a> and  <a href="https://nda.nih.gov/">NDA</a>. It seems people contributing the data don’t have the bandwidth (or guidance) to put the data in better shape, and the archives are glad to take whatever people are willing to share.</p>
<p>What I think we need more of is secondary archives, where people can contribute back ‘crowd curated’ datasets.  Here’s <a href="https://wiki.cancerimagingarchive.net/display/DOI/Standardized+representation+of+the+TCIA+LIDC-IDRI+annotations+using+DICOM">one good example</a> from <a class="mention" href="/u/fedorov">@fedorov</a> where they took some challenging but valuable research data and put it into a form that should facilitate further work.</p>
<p>Perhaps Doug and the MorphoSource community could be encouraging people to clean up resubmit data (and give them some tokens of academic credit for their contributions).  I think it would add a lot of value to the resource.</p>

---

## Post #8 by @fedorov (2020-03-06 14:52 UTC)

<p>On the subject of academic tokens, there are more and more journals these days that publish data descriptors and promote <a href="https://www.go-fair.org/fair-principles/">FAIR data</a>. Some examples include <a href="https://www.nature.com/sdata/">Nature Scientific Data</a> and <a href="https://aapm.onlinelibrary.wiley.com/doi/full/10.1002/mp.12003">Medical Physics dataset articles</a>.</p>
<p>Here’s a data descriptor from the U. Penn group (GBM) which has been cited extremely well: <a href="https://www.nature.com/articles/sdata2017117">https://www.nature.com/articles/sdata2017117</a>.</p>
<p>If someone thinks they have a valuable dataset to share, definitely there are opportunities to publish and build academic credit.</p>

---

## Post #9 by @pieper (2020-03-06 15:02 UTC)

<p>Back to the original topic of how to volume render this data, one difficulty is that the material around the skull has abnormally high signal.  There are pixels that are clearly bone with a value of about 6000, but there’s also clearly background with a value of around 5700.  I don’t see any details on the MorphoSource site, but maybe these bones are preserved in some kind of dense medium?</p>

---

## Post #10 by @muratmaga (2020-03-06 15:57 UTC)

<p>These are all osteological specimen from Harvard’s museum. They wouldn’t have been scanned in any type of medium, but usually placed on a piece of foam. Most likely it is a poorly calibrated scan, as the actual intensity values are nowhere close to the spread of 16bit. So rescaling and converting 8 bit makes sense for this data, because original intensity values are sort of arbitrary.</p>
<p><a class="mention" href="/u/mark_1">@Mark_1</a> MorphoSource is indeed a very valuable resource. However, they do not generate the bulk of the data (only stuff that says Duke primate collection) and certainly not this particular dataset. In any event, if you only need the endocast, you don’t need such high resolution. You can plug the foramen magnum and the other foramina using Segment Editor and then fill the remaining endocranial space.</p>
<p>Alternatively, I just saw a small R utility called endomaker that makes decent endocast from a 3D mesh of skull (<a href="https://twitter.com/ProficoA/status/1233725674315288576" rel="nofollow noopener">https://twitter.com/ProficoA/status/1233725674315288576</a>). It seem to work, but I didn’t go beyond just running a sample data.</p>
<p>Also why do through this all work only to make ullustrations. It will be one click (or one line of code) to measure 3D volumes of those endocrania.</p>

---

## Post #11 by @pieper (2020-03-06 17:16 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="10572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>So rescaling and converting 8 bit makes sense for this data, because original intensity values are sort of arbitrary.</p>
</blockquote>
</aside>
<p>Converting to 8 bit is not a good idea here, since there’s a lot of dynamic range in the scan that would be lost, but probably there are other filtering steps that might help to increase the contrast between thin bone and surrounding air.</p>

---

## Post #12 by @muratmaga (2020-03-06 18:46 UTC)

<p>That actually depends on what you want to do. What I am seeing is endocranial space has a background value of 5700 and the enamal, the densest structure in mammalian skulls, is in the range of 9000s. So the real range is in the 4000 range. Rescaling using this biological range and 8 bit conversion will give you 50% data volume reduction. The equivalent reduction in spatial resolution while keeping the intensities at 16 is going to cost you at the voxel detail.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbfb7f76ab6570f4c620b4a7562aafabc54d2487.png" data-download-href="/uploads/short-url/vo3oF9KLohXS9MVswpqfGRJ9fmf.png?dl=1" title="chim_downsample"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dbfb7f76ab6570f4c620b4a7562aafabc54d2487_2_690x439.png" alt="chim_downsample" data-base62-sha1="vo3oF9KLohXS9MVswpqfGRJ9fmf" width="690" height="439" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dbfb7f76ab6570f4c620b4a7562aafabc54d2487_2_690x439.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dbfb7f76ab6570f4c620b4a7562aafabc54d2487_2_1035x658.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dbfb7f76ab6570f4c620b4a7562aafabc54d2487_2_1380x878.png 2x" data-dominant-color="3E3F4B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">chim_downsample</span><span class="informations">3097×1971 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> c</p>

---

## Post #13 by @pieper (2020-03-06 19:12 UTC)

<p>True, it depends on what you need to accomplish.  But if you go to 8 bits that’s only 256 gray levels and clearly that would be throwing away tons of data here.</p>

---

## Post #14 by @lassoan (2020-03-06 19:29 UTC)

<p>8-bit CT images of bone+air+soft tissue are terrible, essentially unusable. However, if you only have bone+air then 8 bits may be enough, especially if partial volume effect is negligible (because you have extremely small voxel size).</p>

---

## Post #15 by @Mark_1 (2020-03-06 20:03 UTC)

<p>Yes, these data are proving very difficult to work with, at least for me. Unfortunately I haven’t been able to reproduce a render as nice as yours <a class="mention" href="/u/pieper">@pieper</a>.</p>
<p>Here’s a link to the paper describing the dataset and the collection methods used: <a href="https://www.nature.com/articles/sdata20161" rel="nofollow noopener">https://www.nature.com/articles/sdata20161</a>. Yes, it does say that the specimens were placed on a piece of foam for the scanning.</p>
<p>I tried rescaling and casting following the tutorial you linked to <a class="mention" href="/u/muratmaga">@muratmaga</a>, but it didn’t seem to help. The endomaker R function that you mentioned works really well though - very fast and seemingly accurate. Thanks for the tip! However, as you said, that function requires a 3D mesh of a skull as input, so I assume I still need to have a good volume render of the skull before I can make a model from it to export it as a 3D mesh?</p>

---

## Post #16 by @pieper (2020-03-06 20:34 UTC)

<p>I used a spacing scale of 2 with the CropVolume module, in case that helps.</p>
<p>If all you need is a mesh, you can skip the whole volume rendering part and go straight to the SegmentEditor.  You’ll find lots of tutorials for that.</p>

---

## Post #17 by @muratmaga (2020-03-06 21:14 UTC)

<p>As <a class="mention" href="/u/pieper">@pieper</a> said, you don’t need the volume rendering for making a 3D model. If all you care is the endocranial cast, you might even downsample with 4 using the <code>Crop Volume</code> module and then use the downsampled volume in <code>Segment Editor</code>.</p>
<p>We have some tutorials, but ultimately all you will need is the threshold effect (and perhaps island/scissor tool to remove the mandible).</p>
<p>Then go to <code>Segmentations</code> module to export your segmentation as a 3D model and then save it as PLY (through the Save As  dialog box).</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="32" height="32">
      <a href="https://github.com/SlicerMorph/W_2020/tree/master/Lab03_Slicer_3_Segmentation" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/45026482?s=400&amp;v=4" class="thumbnail onebox-avatar" width="400" height="400">

<h3><a href="https://github.com/SlicerMorph/W_2020/tree/master/Lab03_Slicer_3_Segmentation" target="_blank" rel="nofollow noopener">SlicerMorph/W_2020</a></h3>

<p>Contents for the Winter 2020 SlicerMorph workshop. Contribute to SlicerMorph/W_2020 development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #18 by @Chris_Rorden (2020-03-07 11:22 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> I agree with your sense that secondary archives could help. In this example the data is <code>DICOM like</code> but not fully DICOM compliant. Also one could set image intensity to match Hounsfield units. One could even zero out the air voxels which would dramatically improve compression and file transfer. The challenge is doing this in a way that complies with the license of the primary source. In this example, a secondary source would breach the agreement:</p>
<blockquote>
<p>Sharing these files, their derivatives, and/or 3D prints generated from them is only allowed if the user and the third party/parties are engaged in a non-commercial pursuit that cannot be reasonably achieved through each involved individual independently downloading the media.</p>
</blockquote>
<p>By the way, I did adapt dcm2niix to handle most of these images as well as possible. Therefore, an alternative for users would be to convert the images using the <a href="https://github.com/SlicerDMRI/SlicerDcm2nii" rel="noopener nofollow ugc">SlicerDcm2nii plugin</a>.</p>

---

## Post #19 by @lassoan (2020-03-07 12:51 UTC)

<aside class="quote no-group" data-username="Chris_Rorden" data-post="18" data-topic="10572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>By the way, I did adapt dcm2niix to handle most of these images as well as possible.</p>
</blockquote>
</aside>
<p>Oh no, this is exactly the kind of changes that I worry about: software developers degrade safety and/or performance of their software for <em>all</em> data sets and increase maintenance and testing workload, just to make it easier to load corrupted DICOM-like data sets.</p>
<p>Database maintainers have a responsibility to stop this harmful trends. A solution could be to reserve the right to make equivalent transformations to submitted data sets to fix file format errors. I don’t think any data provider group would oppose to such changes.</p>

---

## Post #20 by @muratmaga (2020-03-07 15:32 UTC)

<p>ONe can argue that it is the imaging systems vendor responsibility that they produce compliant files, or the standard to have simpler versions (or subsets) that is easy follow. I don’t think people generating the images are trying to go out their ways to make then non-compliant. They are not imaging technicians/specialist, they are most likely following the directions of the vendor rep who sold the system to them.</p>

---

## Post #21 by @lassoan (2020-03-07 15:56 UTC)

<p>It is true that some non-clinical scanners create invalid images. Some other data sets get corrupted during anonymization or other processing that researchers apply on them.</p>
<p>These invalid files do not cause issues if they are only used internally. A typical scenario is that someone reports that Slicer cannot load some images, we investigate and tell that it is because some mandatory fields were removed  by incorrect anonymization or the scanner created invalid files. They fix their anonymization script or patch the files, and use these correct files afterwards. They may even report back the issue to scanner manufacturers. Problem is solved.</p>
<p>The damage happens when invalid files are made widely available to many people. Distributors of data sets has a responsibility to stop spreading data that causes harm (by degradation of safety and performance, and increased testing and maintenance workload of various DICOM software).</p>
<p>At least there should be mechanisms in place that allow fixing of detected file format issues.</p>

---

## Post #22 by @Julie_Winchester (2020-03-07 18:26 UTC)

<p>Hi all! I am the product manager and lead dev for MorphoSource. I’ve also communicated with some folks here off-thread, but I wanted to chime in on the forum as well. First off, thanks for raising this <a class="mention" href="/u/mark_1">@Mark_1</a> and to everyone else for contributing to the discussion here. Doug and I definitely agree with <a class="mention" href="/u/lassoan">@lassoan</a> that data repositories have a responsibility (and an incentive!) to make sure the data they are sharing is of the highest quality and format compliance. While like everyone else we are dealing with limited time and resources, blindly making malformed data available and doing nothing about it is definitely not something we want to be doing. Also my own research involves CT, so I can personally identify with the pain of problematic data!</p>
<p>To give a bit of background context, right now we are working on basically rebuilding MorphoSource’s software application from the ground-up using Hyrax, an open source digital repository platform initially created for library and information science use cases. As part of this effort, our ability to validate files (and especially DICOMs) coming into the system will be greatly improved. We would be very interested in hearing suggestions for standard-compliant command line tools or workflows that could be used here.</p>
<p>For these particular problematic DICOMs, our preference is to fix them and replace the original files in the repository with more usable versions (while maintaining the iffy originals in dark storage). And we would be happy to work with people in this community to get the problematic data fixed and replaced. Additionally, if there are suggestions for things we can check in an automated way, we can start the process of checking all the data in the system and remediate as needed.</p>
<p>As one final comment, I don’t want it to sound like we are trying to put the burden of this work on anyone else. Doug and I are immediately going to start trying to resolve these issues on our end, to improve things for everyone who uses MorphoSource. But I definitely want to indicate how open and interested we are to hearing suggestions from and working with everyone involved in discussions like this. Our interest is in being a community resource, and responding to the needs and ideas of others is a big part of that.</p>

---

## Post #23 by @lassoan (2020-03-07 22:08 UTC)

<p>Thank you <a class="mention" href="/u/julie_winchester">@Julie_Winchester</a>, these all sound great!</p>
<p>We will set up a meeting to discuss specific steps to take. If anybody wants to participate in this meeting then please let me know in a reply to this post.</p>

---

## Post #24 by @Mark_1 (2020-03-08 11:29 UTC)

<aside class="quote no-group" data-username="Julie_Winchester" data-post="22" data-topic="10572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/julie_winchester/48/6222_2.png" class="avatar"> Julie_Winchester:</div>
<blockquote>
<p>thanks for raising this <a class="mention" href="/u/mark_1">@Mark_1</a></p>
</blockquote>
</aside>
<p>I have to say I never imagined my question would spark this discussion, but I’m glad it was stimulating and that it sounds like the outcome of all of this might be more significant than me getting some pretty pictures for my thesis <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #25 by @Mark_1 (2020-03-08 11:33 UTC)

<aside class="quote no-group" data-username="pieper" data-post="16" data-topic="10572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>If all you need is a mesh, you can skip the whole volume rendering part and go straight to the SegmentEditor</p>
</blockquote>
</aside>
<p>Now I understand the difference between volume rendering and segmenting and when to use each - yes, segmenting is what I should have been doing all along. Sorry to be slow on the uptake! Thanks for the link to that tutorial <a class="mention" href="/u/muratmaga">@muratmaga</a>, it was very clear and helpful.</p>

---

## Post #26 by @Chris_Rorden (2020-03-08 12:25 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I appreciate your concern that by modifying our software to handle DICOM-like images we degrade the performance, and that the increased complexity comes with a cost in terms of maintainability and the probability for unintended consequences. The resulting software can become more brittle. Unfortunately, this is the reality for any tool that wants to handle DICOM data. The standard is so complex, that each vendor has developed their own interpretation. Robustly detecting a simple feature like slice thickness is <a href="http://dclunie.blogspot.com/2013/10/how-thick-am-i-sad-story-of-lonely-slice.html" rel="nofollow noopener">hard</a>, each major vendor has at least one <a href="https://www.na-mic.org/wiki/NAMIC_Wiki:DTI:DICOM_for_DWI_and_DTI" rel="nofollow noopener">proprietary method for reporting DWI information</a>. My software has pages that document the methods used to extract common data from <a href="https://github.com/rordenlab/dcm2niix/tree/master/Siemens" rel="nofollow noopener">Siemens</a>, <a href="https://github.com/rordenlab/dcm2niix/tree/master/GE" rel="nofollow noopener">GE</a> and <a href="https://github.com/rordenlab/dcm2niix/tree/master/Philips" rel="nofollow noopener">Philips</a>. Any DICOM image from any vendor that was touched be a GEIIS system had a thumbnail introduced that broke DICOM compliance as well as many DICOM tools (this bug existed for over a decade, and many of these PACS systems are still in the wild). If you look at many DICOM readers you will note that they will convert tags with length of 13 to length of 10 as a kludge for old GE CT scans (the saving grace is that DICOM tags MUST have an even length, so this can be done without borking compliant DICOM images). Non-standard features like mosaic layout must also be handled.</p>
<p>I would think <a class="mention" href="/u/fedorov">@fedorov</a> would be well placed to work with the groups who share these terrific datasets to help them clean their datasets to be more compliant. I do suspect these complexities are one reason why simpler formats like NRRD/NIfTI have gained a strong niche. From my perspective, the enhanced DICOM was a missed opportunity to create a backward compatible but streamlined solution, much like OpenGL Core deprecated many OpenGL features allowing lean implementations. Unfortunately, this did not happen, and we are in a transition where many enhanced DICOMs break compatibility with existing tools and add complexity to any attempt to provide robust DICOM reading.</p>

---

## Post #27 by @Mark_1 (2020-03-08 15:14 UTC)

<p>I don’t know whether this is the appropriate place for a follow-up question now, but I’ve created a segment from the skull and I am now trying to fill the braincase to create a virtual endocast. Following <a class="mention" href="/u/muratmaga">@muratmaga</a>’s suggestion, I’ve plugged the foramina by painting over them as part of the skull segment, then I thought I could use Flood Filling in the area inside the braincase to create a new endocast segment, but when I try that the whole background gets filled. I don’t know whether I’m not plugging the foramina correctly so voxels inside the braincase are connected to ones outside, or whether I’m not restricting the operation to inside the skull segment correctly, or whether I’m just going about this in completely the wrong way?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3297b4cf84afae9d2dec67b1f5bdd192531ac73.jpeg" data-download-href="/uploads/short-url/nhoHvjiVAiE0f2vT75BRIpE937t.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3297b4cf84afae9d2dec67b1f5bdd192531ac73_2_517x315.jpeg" alt="image" data-base62-sha1="nhoHvjiVAiE0f2vT75BRIpE937t" width="517" height="315" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3297b4cf84afae9d2dec67b1f5bdd192531ac73_2_517x315.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3297b4cf84afae9d2dec67b1f5bdd192531ac73_2_775x472.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3297b4cf84afae9d2dec67b1f5bdd192531ac73_2_1034x630.jpeg 2x" data-dominant-color="6C7891"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1170 312 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #28 by @muratmaga (2020-03-08 16:53 UTC)

<p>After you threshold for the skull, make sure you use the Margin effects and grow the segment for the skull, perhaps by 5 mm or so. This should fill all the holes except for foramen magnum. That you will have to manually patch. Then you should be able to do flood fill as a third segment (Segment_1: Skull, Segment_2: Plug, Segment_3 Endocast). This will result in the undersegmentation of the endocast, which you can dilate it the same amount as you did with the skull to accommodate that difference.</p>
<p>Alternatively, you can build a 3D model from the skull as ply, take to endomaker, get your endocast, and export it as PLY from R, and then import into Slicer as a segmentation to see how well it lines up with your original image…</p>

---

## Post #29 by @muratmaga (2020-03-08 18:10 UTC)

<p><a class="mention" href="/u/mark_1">@Mark_1</a></p>
<ol>
<li>Crop Volume by 4 and use the resultant data</li>
<li>Threshold for skull</li>
<li>Margin effect grow 3mm</li>
<li>Create a blank segment, switch to paint tool set the modify other segments to overlap. Choose 3D brush and set the scale really big, I used about 30-50% range, and paint over the endocranial space entirely without going out too much (overlap with bone is fine).</li>
<li>While keeping Segment_2 as your main segment to edit, go to Logical Operations and choose subtract from Segment_1. This should result just keeping the endocranial space (no more overlap with bone).</li>
<li>You can trim out the remaining (if any) overflow of endocranium with scissors tool.</li>
<li>Use Margin tool to dilate the segment_2 3mm (the same amount you did for skull).</li>
</ol>
<p>This dataset is big, the best thing you can do for yourself as you are learning Slicer is to practice with low-resolution data so that the experimentations go faster, and once you figure out the protocol, you can try with higher resolution. But in terms of the detail on endocranium, you will not get much out of using the high-resolution data.</p>
<p><a class="mention" href="/u/lassoan">@Lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> it would be good to have a tool where we can draw a large 3D sphere from a specified center; almost like the local threshold tool where you click and then expand the radius but in 3D…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f79860940b6a7a6e2f1c769211d655ffb205e6d6.jpeg" data-download-href="/uploads/short-url/zkkoVbkIfi9JHgtSUyxd26ZnTYq.jpeg?dl=1" title="chimp"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f79860940b6a7a6e2f1c769211d655ffb205e6d6_2_672x500.jpeg" alt="chimp" data-base62-sha1="zkkoVbkIfi9JHgtSUyxd26ZnTYq" width="672" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f79860940b6a7a6e2f1c769211d655ffb205e6d6_2_672x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f79860940b6a7a6e2f1c769211d655ffb205e6d6_2_1008x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f79860940b6a7a6e2f1c769211d655ffb205e6d6_2_1344x1000.jpeg 2x" data-dominant-color="505351"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">chimp</span><span class="informations">2343×1743 738 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #30 by @lassoan (2020-03-08 21:47 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="29" data-topic="10572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>it would be good to have a tool where we can draw a large 3D sphere from a specified center; almost like the local threshold tool where you click and then expand the radius but in 3D…</p>
</blockquote>
</aside>
<p>This is what the Paint effect does when “3D brush” option is enabled. You can adjust the sphere size by shift-mousewheel and fine-tune by zooming the view in/out.</p>

---

## Post #31 by @Mark_1 (2020-03-08 23:09 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> That’s brilliant, thank you!</p>

---

## Post #32 by @lassoan (2020-03-09 01:20 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="28" data-topic="10572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Alternatively, you can build a 3D model from the skull as ply, take to endomaker, get your endocast, and export it as PLY from R, and then import into Slicer as a segmentation to see how well it lines up with your original image…</p>
</blockquote>
</aside>
<p>This should not be necessary. Slicer has so many powerful tools (VTK, ITK, and all the contributed extensions) that it is easy to put together fully automatic segmentation scripts for such simple tasks.</p>
<p><strong>Here is how to create the endocast in Slicer fully automatically:</strong></p>
<ol>
<li>Crop Volume by 4 and remove the original volume from the scene</li>
<li>Copy-paste this script into the Python console: <a href="https://gist.github.com/lassoan/4d0b94bda52d5b099432e424e03aa2b1" class="inline-onebox">Automatic endocranium segmentation from dry bone CT scan · GitHub</a></li>
<li>Wait about 2 minutes</li>
</ol>
<p>Prerequisite: Install SurfaceWrapSolidify extension.</p>
<p>The script is not optimized for performance. Probably skull solidify step could be made faster by tuning its parameters. It could be also possible to modify Solidify effect to create internal surfaces instead of external surfaces (this would allow us to fill in discontinuities on the bone without smoothing the surface and could be useful for any cavity segmentation).</p>
<p>If you find it useful you can created a scripted module from the script and add it to SlicerMorph in a matter of minutes, but of course you would need to spend some more time with creating an icon, module documentation page, and tutorial.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11971dd280adb825dbfb942b335fd521ac8bd259.jpeg" data-download-href="/uploads/short-url/2vBSIGd4AiBb1sxPI361vc3GfXP.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/11971dd280adb825dbfb942b335fd521ac8bd259_2_520x500.jpeg" alt="image" data-base62-sha1="2vBSIGd4AiBb1sxPI361vc3GfXP" width="520" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/11971dd280adb825dbfb942b335fd521ac8bd259_2_520x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/11971dd280adb825dbfb942b335fd521ac8bd259_2_780x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/11971dd280adb825dbfb942b335fd521ac8bd259_2_1040x1000.jpeg 2x" data-dominant-color="434547"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1282×1232 295 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you want to do manual segmentation, then there are a few variants of <a class="mention" href="/u/muratmaga">@muratmaga</a>’s manual method that might make things a bit simpler (and might be useful for other segmentation tasks, too):</p>
<p>A. Use Scissors instead of large paintbrush + use Island effect instead of subtract</p>
<p>1-3. Same as in <a class="mention" href="/u/muratmaga">@muratmaga</a>’s method<br>
4. Create a blank segment, switch to Scissors effect, set “Operation” → “Fill inside”, “Editable area” → “Outside all segments”, trace around the endocranial space (remain outside with a safe margin, only need to pay attention to the actual line position at the foramen magnum.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0aa084d3c866816b64170496379cf8acda894bba.jpeg" data-download-href="/uploads/short-url/1w0Gsfwc3JnHSFPIso1XF5f2It4.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0aa084d3c866816b64170496379cf8acda894bba_2_345x500.jpeg" alt="image" data-base62-sha1="1w0Gsfwc3JnHSFPIso1XF5f2It4" width="345" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0aa084d3c866816b64170496379cf8acda894bba_2_345x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0aa084d3c866816b64170496379cf8acda894bba.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0aa084d3c866816b64170496379cf8acda894bba.jpeg 2x" data-dominant-color="2D2B26"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">429×621 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
5. Switch to Islands effect, choose “Keep selected island”, then click in any of the slice views anywhere in the endocranium (this removes all the small disconnected regions outside the skull)<br>
6. Switch to Margin effect, set “Editable area” → “All”, grow by 3mm (the same amount you did for skull)</p>
<p>B. “Plug” the foramen magnum to close volume + fill volume using “Add selected island”</p>
<p>1-3. Same as in <a class="mention" href="/u/muratmaga">@muratmaga</a>’s method<br>
4. Align one of the views to show the foramen magnum: enable slice intersections (in the toolbar, click the dropdown menu of the crosshair button and click “Slice intersections”), and use Shift+MouseMove to move slice views, Ctrl/Cmd + Alt + Left-click-and-drag to rotate slice views.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/152361a757384e266b5dfad9895a52b646d07d7d.jpeg" data-download-href="/uploads/short-url/30ZPxxLU6kIZQr04vcP2IbNBMxT.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/152361a757384e266b5dfad9895a52b646d07d7d_2_690x276.jpeg" alt="image" data-base62-sha1="30ZPxxLU6kIZQr04vcP2IbNBMxT" width="690" height="276" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/152361a757384e266b5dfad9895a52b646d07d7d_2_690x276.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/152361a757384e266b5dfad9895a52b646d07d7d_2_1035x414.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/152361a757384e266b5dfad9895a52b646d07d7d.jpeg 2x" data-dominant-color="2D2F28"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1289×516 215 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
5. Fill in the foramen magnum in the view where the whole opening is visible<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0db938d12baff7250939759f026a262ce960578c.jpeg" data-download-href="/uploads/short-url/1Xp2GqA81PY6G2M6uiqQ9vdCbGQ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0db938d12baff7250939759f026a262ce960578c_2_690x285.jpeg" alt="image" data-base62-sha1="1Xp2GqA81PY6G2M6uiqQ9vdCbGQ" width="690" height="285" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0db938d12baff7250939759f026a262ce960578c_2_690x285.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0db938d12baff7250939759f026a262ce960578c_2_1035x427.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0db938d12baff7250939759f026a262ce960578c.jpeg 2x" data-dominant-color="2D2F27"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1289×534 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
6. Create a new segment, switch to Islands effect, choose “Add selected island”, and click inside the endocranial space in any of the slice views.<br>
7. Switch to Margin effect, grow by 3mm (the same amount you did for skull)</p>

---

## Post #33 by @muratmaga (2020-03-09 02:10 UTC)

<p>This is excellent <a class="mention" href="/u/lassoan">@lassoan</a>, thank you.</p>

---

## Post #34 by @Mark_1 (2020-03-10 20:22 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="33" data-topic="10572" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>This is excellent <a class="mention" href="/u/lassoan">@lassoan</a>, thank you.</p>
</blockquote>
</aside>
<p>Seconded! Thank you so much <a class="mention" href="/u/lassoan">@lassoan</a>! The automatic script is great and I think would make for a useful module for cavity segmentation, though for display purposes it would be ideal if there was a way so that the solidifying didn’t fill gaps such as those between the teeth or cheekbones.</p>
<p>Thank you for providing the manual options as well - I’ve learnt a lot from them about how to combine different tools. Your post would actually make for a nice blog post or mini tutorial if there was somewhere appropriate on the Slicer website, as I’m sure it would be of interest and value to other biological anthropologists or general users who may not come across it under this discussion topic here.</p>

---

## Post #35 by @lassoan (2020-03-10 20:40 UTC)

<aside class="quote no-group" data-username="Mark_1" data-post="34" data-topic="10572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mark_1/48/6305_2.png" class="avatar"> Mark_1:</div>
<blockquote>
<p>The automatic script is great and I think would make for a useful module for cavity segmentation, though for display purposes it would be ideal if there was a way so that the solidifying didn’t fill gaps such as those between the teeth or cheekbones.</p>
</blockquote>
</aside>
<p>The solidified segment is currently approximately a convex hull. There are solidification options for not filling in large holes, but we did not need to enable those because they were not needed. This solidified segment can be removed if you don’t find it useful.</p>
<p>If you need the complete bone model then a simple thresholding (without solidification) should work.</p>
<aside class="quote no-group" data-username="Mark_1" data-post="34" data-topic="10572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mark_1/48/6305_2.png" class="avatar"> Mark_1:</div>
<blockquote>
<p>Your post would actually make for a nice blog post or mini tutorial if there was somewhere appropriate on the Slicer website, as I’m sure it would be of interest and value to other biological anthropologists</p>
</blockquote>
</aside>
<p>It would be great if you could write a blog post like that. I can help with any providing more technical details and review/give feedback on the text.</p>

---

## Post #36 by @muratmaga (2020-03-10 20:54 UTC)

<p><a class="mention" href="/u/smrolfe">@smrolfe</a> We will very likely wrap Andras’s example as an additional module for SlicerMorph.<br>
<a class="mention" href="/u/mark_1">@Mark_1</a> if you write a step-by-step documentation, we can add to SlicerMorph project site (some examples are <a href="https://slicermorph.github.io/#two" rel="nofollow noopener">https://slicermorph.github.io/#two</a>). Some of these tutorials predate SLicerMorph, and is hosted outside, but nowadays is real easy to use the github’s markdown and add this as a page new item. Let me know if this is a route you would like to pursue.</p>

---

## Post #37 by @Mark_1 (2020-03-10 21:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="35" data-topic="10572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There are solidification options for not filling in large holes, but we did not need to enable those because they were not needed</p>
</blockquote>
</aside>
<p>I’m guessing that this would involve setting the “Carve out Cavities” parameters? If so an issue might be that these parameters would likely need to be tweaked for different sized skulls whose cavity sizes may be different, which could interfere with the automaticity of things. In the end I’m hoping to do about 10 more skulls, including that of the smallest primate.</p>
<p>But as you suggested, thresholding and using one of your manual methods would likely be as quick as anything. Probably the greatest time-saver is actually the automatic thresholding part of your script, and I can just use that bit on its own.</p>
<aside class="quote no-group" data-username="lassoan" data-post="35" data-topic="10572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It would be great if you could write a blog post like that.</p>
</blockquote>
</aside>
<p>I could certainly give it a go. I’ll have to have a think about how and when I might do it. The SlicerMorph project site looks like a good place to post it though <a class="mention" href="/u/muratmaga">@muratmaga</a>, as it would fit in nicely with the other tutorials there.</p>

---

## Post #38 by @lassoan (2020-03-10 22:25 UTC)

<aside class="quote no-group" data-username="Mark_1" data-post="37" data-topic="10572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mark_1/48/6305_2.png" class="avatar"> Mark_1:</div>
<blockquote>
<p>I’m guessing that this would involve setting the “Carve out Cavities” parameters? If so an issue might be that these parameters would likely need to be tweaked for different sized skulls whose cavity sizes may be different</p>
</blockquote>
</aside>
<p>Probably the same parameters would work for a wide range of skull sizes, but the extra carving steps might slightly increase the computation time and are not needed at all, if the goal is to just extract the brain cavity.</p>
<p>The automatic threshold computation is available in the Threshold effect GUI, too (in “automatic” section).</p>

---

## Post #40 by @lassoan (2020-04-22 12:12 UTC)

<p><a class="mention" href="/u/mark_1">@Mark_1</a> <a class="mention" href="/u/muratmaga">@muratmaga</a> We have now added a fully automatic cavity segmentation option to “Wrap Solidify” effect. It can extract the largest cavity (you can specify a hole size threshold to prevent leaking into other cavities through small holes) and it also has a manual region initialization option so that you can extract any cavity. It could be added to your excellent endocranium segmentation blog post as an additional option. See more details in this post: <a href="https://discourse.slicer.org/t/fill-or-extract-cavities-in-segmentations-using-the-new-wrap-solidify-effect/11248" class="inline-onebox">Fill or extract cavities in segmentations using the new "Wrap Solidify" effect</a></p>

---
