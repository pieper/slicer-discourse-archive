---
topic_id: 36346
title: "How Can I Create Dcm Or Mesh Files From Vol And Vgi Files An"
date: 2024-05-23
url: https://discourse.slicer.org/t/36346
---

# How can I create dcm (or mesh) files from .vol and vgi files and .raw?

**Topic ID**: 36346
**Date**: 2024-05-23
**URL**: https://discourse.slicer.org/t/how-can-i-create-dcm-or-mesh-files-from-vol-and-vgi-files-and-raw/36346

---

## Post #1 by @CatherineBone (2024-05-23 12:34 UTC)

<p>Hi, I’ve been given two files that contain the CT scans of two  Neanderthal<br>
The first one contains a .vgi and a .vol and the second a .raw<br>
I need to create dicom files from the .vol files and .raw files that I can create mesh files (obj or stl) from. Or skip the dicome files part and go straight to mesh files.</p>
<p>I’ve downloaded and installed the slicermorph and Raw Image Guess extentions but can’t seem to get any useable data out.</p>
<p>For the .vol data - I load it in using the Raw Image Guess module - tried to enter in the size of the xyz dimentions from the .vgi file but the sliders dont go up that high, and I tried a tutorial online (<a href="https://youtu.be/ajpOQEAyWkA?si=BoqaenOgTG2fNF8f" rel="noopener nofollow ugc">https://youtu.be/ajpOQEAyWkA?si=BoqaenOgTG2fNF8f</a>)  but im just getting lots of fuzziness!<br>
This is the .vgi file:<br>
{volume1}<br>
[representation]<br>
size = 1374 1401 2000<br>
mirror = 0 0 0 0<br>
resamplemode = not activated<br>
datatype = unsigned integer<br>
datarange = 0 65535<br>
bitsperelement = 16<br>
[file1]<br>
RegionOfInterestStart = 0 0 0<br>
RegionOfInterestEnd = 1373 1400 1999<br>
FileFormat = raw<br>
Size = 1374 1401 2000<br>
Name = LB_BH1_01.vol<br>
Datatype = float<br>
datarange = -94.1933 394.005<br>
BitsPerElement = 32<br>
{volumeprimitive1}<br>
[section1]<br>
min = 0<br>
max = 65535<br>
offset = 0<br>
name = section [0]</p>
<p>[geometry]<br>
status = visible<br>
relativeposition = 0 0 0<br>
position = 10.5004 -38.0008 0<br>
resolution = 0.1271 0.1271 0.1271<br>
scale = 1 1 1<br>
center = 687 700.5 1000<br>
rotate = 1 0 0 0 1 0 0 0 1<br>
unit = mm<br>
[volume]<br>
volume = volume1<br>
[description]<br>
text = LB_BH1__<br>
[segment1]<br>
status = activated<br>
description = 0<br>
opacityx = 0 12644 65535<br>
redx = 0 65535<br>
greenx = 0 65535<br>
bluex = 0 65535<br>
opacityvalue = 0 0 2<br>
redvalue = 255 255<br>
greenvalue = 255 255<br>
bluevalue = 255 255<br>
{default}<br>
[version]<br>
release = VGStudioMax 1.2.1 (build 352)<br>
{scene}<br>
[viewer]<br>
perspective = activated<br>
viewing angle = 30<br>
position = 0 5849.72 0<br>
oversampling = 1<br>
up = 0 0 1<br>
lookat = 0 0 0<br>
resultsize = 256 256<br>
[perspective]<br>
status = activated<br>
[light1]<br>
diffuse = 0.333 0.333 0.333<br>
status = activated<br>
ambient = 0.333 0.333 0.333<br>
[light2]<br>
diffuse = 0.333 0.333 0.333<br>
status = not activated<br>
ambient = 0.333 0.333 0.333<br>
[angle]<br>
position = 0 0 0<br>
status = not activated<br>
right = 1 2 0<br>
left = -1 2 0<br>
[resolution]<br>
resolution = 0.1271<br>
unit = mm<br>
displayunit = mm<br>
[rendering]<br>
background = 0 0 0 255<br>
intensity = 0.333<br>
colormode = activated<br>
quickmode = activated<br>
algorithm = scatterhq<br>
{camera1}<br>
[viewer]<br>
perspective = activated<br>
viewingangle = 30<br>
position = 0 5849.72 0<br>
oversampling = 1<br>
up = 0 0 1<br>
lookat = 0 0 0<br>
resultsize = 256 256<br>
[perspective]<br>
status = activated<br>
[rendering]<br>
colormode = activated<br>
quickmode = activated<br>
algorithm = scatterhq</p>
<p>For the .raw file I have a txt file that comes with it… and it says only:<br>
Stitched_RI_H-neanderthal_Gibraltar-1_EM3811_raw_<br>
1558x1722x2870<br>
16 bits unsigned<br>
(uncheck Little-endian byte order)</p>
<p>Again I tried importing this with Raw Image Guess, but no luck!</p>
<p>Any help would be greatly appreciated!<br>
Thanks in advance</p>

---

## Post #2 by @muratmaga (2024-05-23 14:52 UTC)

<p>Please give GEVolImport module in SlicerMorph extension a try. That should be able to import your dataset.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/tree/master/GEVolImport#readme">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/GEVolImport#readme" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/GEVolImport#readme" target="_blank" rel="noopener">SlicerMorph/GEVolImport at master · SlicerMorph/SlicerMorph</a></h3>


  <p><span class="label1">Extension to import microCT data and conduct 3D morphometrics in Slicer - SlicerMorph/SlicerMorph</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @CatherineBone (2024-05-23 15:01 UTC)

<p>Thank you <a class="mention" href="/u/muratmaga">@muratmaga</a>. I dont have a pcr file though - only a .vol and .vgi<br>
Is there a way a .vgi can be turned into a .pcr?<br>
Thank you</p>

---

## Post #4 by @muratmaga (2024-05-23 15:13 UTC)

<p>I don’t think so, but you can ask the imaging lab to give you that file. I think it is a standard output from GE scanners.</p>
<p>Or you can try and fiddle with RawImageGuess with those parameters.<br>
X Y Z should be 1374, 1401 and 2000<br>
and data type should be unsigned integer (unsigned 16 bit).</p>

---

## Post #5 by @CatherineBone (2024-05-23 15:31 UTC)

<p>Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a>. Unfortunately those were the only files available from the Natural History Museum London. They wont be scanning the skull again any time soon.<br>
I tried RawImageGuess, but the XYZ can’t go beyond 1200 - so I can’t enter in 1374, 1401 and 2000.<br>
Is there another program that can access .vol files and turn them into dcm?</p>
<p>Also any suggestions on the .raw files? Again I tried RawImageGuess but the XYZ dimensions are too big for for module.</p>
<p>Thanks for your help</p>

---

## Post #6 by @muratmaga (2024-05-23 16:10 UTC)

<aside class="quote no-group" data-username="CatherineBone" data-post="5" data-topic="36346">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/f19dbf/48.png" class="avatar"> CatherineBone:</div>
<blockquote>
<p>RawImageGuess, but the XYZ can’t go beyond 1200 - so I can’t enter in 1374, 1401 and 2000.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> can you fix that limitation? Perhaps, provide a freehand entry for the size as opposed to a slider with upper bound?</p>
<p><a class="mention" href="/u/catherinebone">@CatherineBone</a> .pcr file is generated during the scan. So unless they deleted their data they should have it.</p>
<p>As an alternative, keep the XYZ dimensions as large as you can, set the spacing 0.1271 for all three, and then click <strong>Generate NRRD Image Header</strong> button. This will save a text file (NHRD), which you can open and then edit the XYZ dimensions correctly. You can then save it, and simply drag this file into slicer. Make sure that saved file (NHRD) sits in the same folder as the VOL file. If the settings are correct, then it should load fine.</p>

---

## Post #7 by @lassoan (2024-05-23 16:21 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="36346">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Perhaps, provide a freehand entry for the size as opposed to a slider with upper bound?</p>
</blockquote>
</aside>
<p>Using sliders is important to allow going through a range of values quickly. You can edit the range in the Advanced section:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a06bb3c93af3656a762e323f8ac92dc398eb6ee.png" data-download-href="/uploads/short-url/lYzX2ZKQwV7yb8vGS8GtAPJDI6i.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a06bb3c93af3656a762e323f8ac92dc398eb6ee_2_648x500.png" alt="image" data-base62-sha1="lYzX2ZKQwV7yb8vGS8GtAPJDI6i" width="648" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a06bb3c93af3656a762e323f8ac92dc398eb6ee_2_648x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a06bb3c93af3656a762e323f8ac92dc398eb6ee_2_972x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a06bb3c93af3656a762e323f8ac92dc398eb6ee_2_1296x1000.png 2x" data-dominant-color="383838"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1928×1487 205 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @muratmaga (2024-05-23 22:25 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="36346">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Advanced section:</p>
</blockquote>
</aside>
<p>Good to know. I didn’t notice the Advanced section.</p>

---
