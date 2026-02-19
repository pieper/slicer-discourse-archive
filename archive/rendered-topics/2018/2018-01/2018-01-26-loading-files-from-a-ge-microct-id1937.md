---
topic_id: 1937
title: "Loading Files From A Ge Microct"
date: 2018-01-26
url: https://discourse.slicer.org/t/1937
---

# Loading files from a GE microCT 

**Topic ID**: 1937
**Date**: 2018-01-26
**URL**: https://discourse.slicer.org/t/loading-files-from-a-ge-microct/1937

---

## Post #1 by @locobra (2018-01-26 01:06 UTC)

<p>Operating system: MacOSX 10.10<br>
Slicer version: 4<br>
Expected behavior: NA<br>
Actual behavior:<br>
I have files that I would like to open in 3DSlicer, which were created on a GE microCT system. The output files from the machine are the series of X-ray tiff images and pca, which is opened in a linked software for alignment and correction called Phoenix Datosx. This software outputs a series of files including pcj, pcp, pcr, vgl and vol.<br>
I was wondering if there is a plugin that will read these files and import as a regular dicom or tiff files from other CT scanners.<br>
Thank you.</p>

---

## Post #2 by @hherhold (2018-01-26 13:20 UTC)

<p>I don’t think Slicer will import datos|x files like VGL and VOL - I believe these are proprietary formats for Volume Graphics VG Studio Max. (Would be very happy to be corrected on this if Slicer could read these…?)</p>
<p>What I do (we use the same type of scanner and reconstruction software) is to export a stack of TIFF files from datos|x - the button is usually in the right hand side of the tool bar up top. The stack can then be imported into Slicer.</p>
<p>What I often wind up doing, however, is doing a little preprocessing of that TIFF stack with Fiji/ImageJ, cropping and maybe converting to 8 bit (depending on the data), setting the voxel size, and then exporting as NRRD. This can then be easily loaded and analyzed in slicer. This is optional, however, as Slicer can import a TIFF stack all by itself.</p>
<p>Not saying this is the best way, and if anybody has any suggestions on better ways, I’m all ears.</p>
<p>Hope this helps.</p>
<p>-Hollister</p>

---

## Post #3 by @pieper (2018-01-26 13:49 UTC)

<p>Hi Lorian and Hollister -</p>
<p>Here’s some code that worked for reading some vgi/vol data that I got from a microCT a while back.  I’m happy to contribute this along with some scanned phantoms if anyone wants to turn it into an extension.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/pieper/CaseHub/blob/master/BenchtopNeuro/BenchtopNeuro.py#L378-L460" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/CaseHub/blob/master/BenchtopNeuro/BenchtopNeuro.py#L378-L460" target="_blank" rel="nofollow noopener">pieper/CaseHub/blob/master/BenchtopNeuro/BenchtopNeuro.py#L378-L460</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="378" style="counter-reset: li-counter 377 ;">
<li>def volumeNodeFromVolArray(self, volArray, shape, vtkDataType, dimensions, volName, spacing):</li>
<li>
</li>
<li>  volArray = volArray.reshape(shape)</li>
<li>
</li>
<li>  # make a vtkImage data of the vol data</li>
<li>  image = vtk.vtkImageData()</li>
<li>  image.SetDimensions(dimensions)</li>
<li>  image.AllocateScalars(vtk.VTK_FLOAT, 1)</li>
<li>  imageArray = vtk.util.numpy_support.vtk_to_numpy(image.GetPointData().GetScalars()).reshape(shape)</li>
<li>  imageArray[:] = volArray</li>
<li>
</li>
<li>  # make a slicer volume node for the image</li>
<li>  volumeNode = slicer.vtkMRMLScalarVolumeNode()</li>
<li>  volumeNode.SetName(volName)</li>
<li>  volumeNode.SetSpacing(*spacing)</li>
<li>  volumeNode.SetAndObserveImageData(image)</li>
<li>  slicer.mrmlScene.AddNode(volumeNode)</li>
<li>  volumeNode.CreateDefaultDisplayNodes()</li>
<li>
</li>
<li>  # make this volume visible</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/pieper/CaseHub/blob/master/BenchtopNeuro/BenchtopNeuro.py#L378-L460" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>HTH,<br>
Steve</p>

---

## Post #4 by @locobra (2018-01-27 12:17 UTC)

<p>Dear Hollister and Pieper,</p>
<p>Thank you for the answers. I’ll be trying both.<br>
I’m not yet versed on Python to help with the extension creation, although it would be a fantastic tool, because I have seen the expansion of GE CT and microCT equipment in the Life Sciences field, and it’s heartbreaking that hands are tied due to software pricing.</p>
<p>Best,<br>
Lorian.</p>

---

## Post #5 by @pieper (2018-01-27 18:20 UTC)

<p>If you have an example file we could see if it works with this code.  I had .vgi/.vol files and I think they came from either a Bruker or Nikon scanner so I’m not even sure it’s the same format (is VGL the same a .vgi?)</p>

---

## Post #6 by @tsehrhardt (2018-01-29 01:01 UTC)

<p>I convert tiff stacks to nrrd in Fiji as well. The nrrd loads much faster, plus you can use Fiji to delete slices and do other editing as well.</p>
<p>Terrie</p>

---

## Post #7 by @qinwuxutexas (2019-10-01 02:01 UTC)

<p>Hi Steve, I am having a similar or maybe the same problem. I had .vol file (3D reconstructed volume file using GE CT scan) and .vgl (created from .vol file using the VG Studio software). I am looking for the code/method to open the .vol file and then extract 2D slices out, can you help try a .vol file using the code you provided, etc.? Maybe I am not that good in the Python code and am unable to make it work. I may send the .vol file example to you though it has relatively very large file size. Thank you:)</p>

---

## Post #8 by @muratmaga (2019-10-01 04:43 UTC)

<p>VG Studio Max used to save a vgi file that you can open with any text editor. The volume representation section described the volume size, data type etc… A very old vgi file I have shows this information:</p>
<blockquote>
<p>{volume1}<br>
[representation]<br>
size = 865 519 369<br>
mirror = 0 0 0 0<br>
resamplemode = not activated<br>
indexedcolormode = false<br>
datatype = unsigned integer<br>
datarange = 0 -1<br>
bitsperelement = 16<br>
[file1]<br>
FileFormat = raw<br>
Size = 865 519 369<br>
Name = C:/CT_Data/AUJM-2002-25/VGStudio/maxilla.raw<br>
Datatype = unsigned integer<br>
BitsPerElement = 16<br>
[description]</p>
</blockquote>
<p>If you can get this information, you can use <a href="https://github.com/lassoan/SlicerRawImageGuess" class="inline-onebox">GitHub - lassoan/SlicerRawImageGuess</a> to get your data into Slicer.</p>

---

## Post #9 by @pieper (2019-10-01 12:33 UTC)

<p><a class="mention" href="/u/qinwuxutexas">@qinwuxutexas</a> - if you have the dimension information you should be able to use the code <a class="mention" href="/u/muratmaga">@muratmaga</a> pointed to and just fill in the blanks.  Or you can experiment by writing a <a href="http://teem.sourceforge.net/nrrd/format.html" rel="nofollow noopener">nhdr file</a> with the volume information.</p>
<p>If you are really stuck, then yes, put it on a public share (dropbox, google drive, onedrive, etc) and one of us can probably give specific advice.  For inspiration, can you tell us what kind of data it is and what your overall goal is?</p>

---

## Post #10 by @hherhold (2019-10-01 12:53 UTC)

<p>I sometimes use Fiji/ImageJ to do this - you can import a GE CT scan .vol file as raw, you just need to put in the image dimensions (usually in the .pca file) and specify little-endian byte order. You can crop if you like, then export as NRRD.</p>

---

## Post #11 by @lassoan (2019-10-02 01:04 UTC)

<aside class="quote no-group" data-username="pieper" data-post="9" data-topic="1937">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Or you can experiment by writing a <a href="http://teem.sourceforge.net/nrrd/format.html">nhdr file</a> with the volume information</p>
</blockquote>
</aside>
<p>Once you determined the correct image size, SlicerRawImageGuess can create a nhdr header for you, which you can use to load the proprietary volume into Slicer or any other standard image viewer.</p>

---

## Post #12 by @muratmaga (2019-10-02 03:50 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, SlicerRawImageGuess might need some updates for python3. Got some errors when I was trying a raw volume.</p>

---

## Post #13 by @qinwuxutexas (2019-10-08 01:04 UTC)

<p>Thank you:) I am going to try this.</p>

---

## Post #14 by @qinwuxutexas (2019-10-08 01:05 UTC)

<p>I am going to try this to see.Thank you:)</p>

---

## Post #15 by @Jeff_Zeyl (2020-08-23 13:52 UTC)

<p>When I try opening the vol files in SlicerRawImageGuess (running in Slicer 4.11) it loads fine, but crops out a portion of the volume for some reason. I’ve played with the various options but the crop still remains. I’m not sure if this is a bug or if there is another reason. If I use ImageJ and the same volume dimensions (using import–&gt; raw) I have no problems and it opens the full volume.</p>

---

## Post #16 by @lassoan (2020-08-23 14:46 UTC)

<p>What is the volume size? If you generate the nrrd header, restart Slicer, and load the image by opening the header file then is the image still cropped?</p>
<p>Can you save the micro-CT in the scanner as DICOM file? You can then load it with DICOM module.</p>

---

## Post #17 by @Jeff_Zeyl (2020-09-26 13:32 UTC)

<p>Yes, the volume is still cropped in the generated nrrd header. The original vol file is 3.6 GB (running on a machine with 16 GB RAM) and it gets cropped down to 1.8 GB. The missing bit can be scrolled through, but it’s blank (black). I can save an nrrd file from FIJI and then load as nrrd and it loads fine.</p>

---

## Post #18 by @lassoan (2020-09-26 13:46 UTC)

<p>What is the image size?<br>
Is the size correct in the nhdr file that RawImageGuess generates?</p>

---

## Post #19 by @Jeff_Zeyl (2020-09-27 16:04 UTC)

<p>The dimensions of the volumes I’ve tried are around 1737x 1139x 2022. Yes, the header has correct dimensions in the nrrd. Basically the volume loads correctly in x and y (in the red window) for about the first ~third in the z dimension; for the rest it’s black/empty</p>

---

## Post #20 by @lassoan (2020-09-28 01:15 UTC)

<p>Something is not right. In general, CTs must be stored on 16 bits, as when only 8 bits are used then the dynamic range would be so low that you could not represent hard tissues (bones) and air and still distinguish various soft tissues. Therefore size of an image of 1737x1139x2022 voxels should be about 8GB.</p>
<p>If the file size is just 4GB then most likely at some point the image was converted to 8 bits (which is acceptable when you image dry bone in air). In this case, in Raw Image Guess module you need to set <code>Pixel type</code> -&gt; <code>8 bit unsigned</code> to make the image load correctly.</p>

---

## Post #21 by @Jeff_Zeyl (2020-09-28 05:50 UTC)

<p>Sorry for the confusion - I mixed my reference to two different volumes I was testing. Yes, that one (1737x1139x2022) is about 7.8 GB. Another smaller one (1119x1338x1294) is 3.6 GB. Both had the same issue. Here’s the example vgi info associated with the vol file:</p>
<p>{volume1}<br>
[representation]<br>
size = 1737 1139 2022<br>
bitsperelement = 16<br>
datatype = unsigned integer<br>
datarange = 0 65535<br>
[file1]<br>
Mirror = 0 1 1<br>
RegionOfInterestStart = 0 0 0<br>
RegionOfInterestEnd   = 1736 1138 2021<br>
FileFormat = raw<br>
Size = 1737 1139 2022<br>
Name = X:\24082020 Jeff\24082020_02 WBC-01-2020\24082020_02 WBC-01-2020.vol<br>
bitsperelement = 16<br>
datatype = unsigned integer<br>
datarange = 0 65535<br>
[description]<br>
text = 0<br>
{default}<br>
[version]<br>
release = VGStudioMax 1.0<br>
{volumeprimitive9}<br>
[section1]<br>
max = 65535<br>
offset = 0<br>
min = 0<br>
name = section [0]<br>
[geometry]<br>
clipplane1 = -1 0 0 1737<br>
clipbox = 0 0 0 1737 1139 2022<br>
position = 0 0 0<br>
status = visible<br>
relativeposition = 0 0 0<br>
resolution = 0.050000 0.050000 0.050000<br>
center = 868 569 1011<br>
scale = 1 1 1<br>
rotate = 1 0 0 0 1 0 0 0 1<br>
unit = mm<br>
[volume]<br>
volume = volume1<br>
[description]<br>
text = X:\24082020 Jeff\24082020_02 WBC-01-2020\24082020_02 WBC-01-2020.vol<br>
[segment1]<br>
opacityvalue = 0.0  2.0<br>
status = activated<br>
description = 0<br>
redvalue = 255 255<br>
greenvalue = 255 255<br>
bluevalue = 255 255<br>
redx = 0 65535<br>
greenx = 0 65535<br>
bluex = 0 65535<br>
opacityx = 0 65535</p>

---

## Post #22 by @lassoan (2020-09-28 15:22 UTC)

<p>Can you share an example image (upload to dropbox/onedrive/google drive/… and post the link here) so that we can investigate?</p>

---

## Post #23 by @muratmaga (2020-09-28 20:59 UTC)

<p>VGStudio Max log file indicates data is 16 bit unsigned. Is that what you set in the Raw Image Guess too?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aad50a3d372fa02bb41f56ad7f60f796d7e9e277.png" alt="image" data-base62-sha1="onfBzI0qUQsaS4qu3niIHnbfMYn" width="675" height="219"></p>

---

## Post #24 by @Jeff_Zeyl (2020-09-30 10:17 UTC)

<p>Yes, I selected 16 bit unsigned and little endian. Here’s the input and what it loads:<br>
</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://ssl.gstatic.com/docs/doclist/images/infinite_arrow_favicon_5.ico" class="site-icon" width="16" height="16">
      <a href="https://drive.google.com/drive/folders/1CqWU2-0Txe8Fq-FjigHf6nW2Da8R9rLP?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://drive.google.com/drive/folders/1CqWU2-0Txe8Fq-FjigHf6nW2Da8R9rLP?usp=sharing" target="_blank" rel="noopener nofollow ugc">rawimageguess - Google Drive</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
The first two pics show it loaded fine (a bird neck shown in the volume), but then at 27.1 mm it clips part of the image, and all subsequent images are black. I also noticed the contrast for the loaded volume can’t be adjusted in the usual way using the mouse; not sure if that’s related to this problem

---

## Post #25 by @muratmaga (2020-09-30 14:51 UTC)

<p>Is it possible for you to upload the vol file on the google drive?</p>

---

## Post #26 by @Jeff_Zeyl (2020-10-01 07:25 UTC)

<p>I’ve added an example vol and vgi in the folder</p>

---

## Post #27 by @muratmaga (2020-10-01 17:08 UTC)

<p>Thanks.<br>
<a class="mention" href="/u/lassoan">@lassoan</a> I am getting this error on windows 4.11.0-2020-09-21 r29383 / c299952</p>
<pre><code>Warning: In D:\D\P\Slicer-0-build\VTK\IO\Image\vtkImageReader2.cxx, line 687
vtkImageReader2 (000001CD8B5971B0): File operation failed.
Generic Warning: In D:\D\P\Slicer-0-build\VTK\IO\Image\vtkImageReader2.cxx, line 757
File operation failed. row = 630, Read = 3026, FilePos = -1
</code></pre>
<p>And also the load dialog box for file browser opens as save as.</p>

---

## Post #28 by @muratmaga (2022-08-15 03:59 UTC)

<p>To close the loop on this:</p>
<p>There is now a simple utility module (VoIImportModule) which allows to obtain the image spacing and dimensions provided by the PCR file. The instructions to install the module and how to use it can be found at:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/chz31/VolImportModule/">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/chz31/VolImportModule/" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/477341805ac1868788857900d9648c9fb1c3a4296a1fbd91599f406964fa5cc7/chz31/VolImportModule" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/chz31/VolImportModule/" target="_blank" rel="noopener nofollow ugc">GitHub - chz31/VolImportModule</a></h3>

  <p>Contribute to chz31/VolImportModule development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #29 by @jusopar (2023-02-21 01:45 UTC)

<p>Hi Murat,<br>
Thank you for this helpful module!<br>
But I’m not able to find it in 3Dslicer after following the installation steps. I cloned the repository, added the additional module path and restarted 3D slicer. But when I open it again, I cannot find the module. I searched as VolImport or GEVolImport, and nothing is showing up.<br>
Did I miss a step to get the module installed?<br>
Thanks!<br>
Julia</p>

---

## Post #30 by @muratmaga (2023-02-21 06:14 UTC)

<p><a class="mention" href="/u/jusopar">@jusopar</a> This is now incorporated to the SlicerMorph module as a development tool (since more testing needs to be done).</p>
<p>Just update your SlicerMorph to the latest version (from extension manager). Then go to <strong>Edit-&gt;Application Settings-&gt;Developer</strong> and enable “<strong>Developer Mode</strong>”. After this you can use the Module Search (CTRL+F) and search for “GEVol”. You also need to enable the “testing” option (see screenshot).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/6001410d864507070d32ac90b5c2ec1875e232de.png" data-download-href="/uploads/short-url/dHiwuABBkDUrAQg1cqjF60FOeUm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/6001410d864507070d32ac90b5c2ec1875e232de.png" alt="image" data-base62-sha1="dHiwuABBkDUrAQg1cqjF60FOeUm" width="690" height="419" data-dominant-color="E2E1E7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">848×515 33.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #31 by @jusopar (2023-02-21 17:00 UTC)

<p>It worked! Thank you so much!</p>
<p>If I don’t use this development tool, what information form the .pcr file I should use to figure out the image spacing, when importing via Image Stack?</p>
<p>On another topic, how can I enable the scale bar (ruler) for the purpose of capturing a screenshot to be used in a figure in a publication?</p>
<p>Thanks so much again!</p>

---

## Post #32 by @muratmaga (2023-02-21 17:19 UTC)

<p>The only piece of informaiton you</p>
<aside class="quote no-group" data-username="jusopar" data-post="31" data-topic="1937">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jusopar/48/10144_2.png" class="avatar"> jusopar:</div>
<blockquote>
<p>If I don’t use this development tool, what information form the .pcr file I should use to figure out the image spacing, when importing via Image Stack?</p>
</blockquote>
</aside>
<p>Image spacing. You need to dig that out from the pcr file. I think everything else should be fine.</p>
<aside class="quote no-group" data-username="jusopar" data-post="31" data-topic="1937">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jusopar/48/10144_2.png" class="avatar"> jusopar:</div>
<blockquote>
<p>On another topic, how can I enable the scale bar (ruler) for the purpose of capturing a screenshot to be used in a figure in a publication?</p>
</blockquote>
</aside>
<p>if you used this tool (or Imagestacks and provided the right image spacing), your data is already correctly scaled, and you can enable the rulers both in 2D and 3D. In 3D, you need to use the orthographic projection for the ruler to be visible (most people by default use the perspective rendering).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d61ff8a1069c4facbbf4015dbfbfc2afb52896c.jpeg" data-download-href="/uploads/short-url/6ttrFKPik5bGhSzIDd8VpHaADF2.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d61ff8a1069c4facbbf4015dbfbfc2afb52896c_2_363x500.jpeg" alt="image" data-base62-sha1="6ttrFKPik5bGhSzIDd8VpHaADF2" width="363" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d61ff8a1069c4facbbf4015dbfbfc2afb52896c_2_363x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d61ff8a1069c4facbbf4015dbfbfc2afb52896c_2_544x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d61ff8a1069c4facbbf4015dbfbfc2afb52896c_2_726x1000.jpeg 2x" data-dominant-color="636064"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">875×1202 91.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #33 by @jusopar (2023-02-21 17:32 UTC)

<p>Perfect! Thank you so much!</p>

---
