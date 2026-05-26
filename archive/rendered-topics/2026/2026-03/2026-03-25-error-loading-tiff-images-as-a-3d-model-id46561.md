---
topic_id: 46561
title: "Error loading tiff images as a 3D model"
date: 2026-03-25
url: https://discourse.slicer.org/t/46561
last_bumped: 2026-04-13T11:27:58.707Z
---

# Error loading tiff images as a 3D model

**Topic ID**: 46561
**Date**: 2026-03-25
**URL**: https://discourse.slicer.org/t/error-loading-tiff-images-as-a-3d-model/46561

---

## Post #1 by @Varsha (2026-03-25 15:00 UTC)

<p>I am trying to load 15 tiff images which are basically images taken at different z slices and create a 3D model out of it. When I try doing this using the Image Stack option under Slicer Morph, the load button remains de-activated. Could anyone advise on what I might be doing wrong? Alternatively, when I try to load it using the ‘Add Data’ option, even though I de-select ‘Single output/ file’ and select ‘Volume’ option, I keep getting error messages of the kind shown below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f872e9a69b271cd0682459a53310100683dc08b.png" data-download-href="/uploads/short-url/icagqqzJJQuAfKXN7pqh28BLF0f.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f872e9a69b271cd0682459a53310100683dc08b_2_352x500.png" alt="image" data-base62-sha1="icagqqzJJQuAfKXN7pqh28BLF0f" width="352" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f872e9a69b271cd0682459a53310100683dc08b_2_352x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f872e9a69b271cd0682459a53310100683dc08b_2_528x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f872e9a69b271cd0682459a53310100683dc08b_2_704x1000.png 2x" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">864×1227 49.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf99477a5236dfba4a5305288c77c2e899b82085.png" data-download-href="/uploads/short-url/rkXAXdbVngcnv26BgiJzIUg98BT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf99477a5236dfba4a5305288c77c2e899b82085.png" alt="image" data-base62-sha1="rkXAXdbVngcnv26BgiJzIUg98BT" width="690" height="345" data-dominant-color="E2E0E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">930×466 28.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any idea why this might be happening?</p>

---

## Post #2 by @muratmaga (2026-03-25 15:38 UTC)

<ol>
<li>Upgrade to the latest stable (5.10), you are using and unmaintained version of Slicer.</li>
<li>Copy the files somewhere that’s not on Onedrive. Cloud synced folders can sometimes cause weird issues.</li>
</ol>
<p>If these don’t help, you need to share the dataset.</p>

---

## Post #3 by @Varsha (2026-03-30 08:31 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a> thanks for the quick response.</p>
<p>I have upgraded to the 5.10 version, and also tried loading the images from a non One-Drive location. However, I still get the same error message, and still can’t get the Load option to work. I would be grateful if you could advice as to what might be going wrong here. What might be the best way to share these images here for troubleshooting?</p>

---

## Post #4 by @muratmaga (2026-03-30 15:55 UTC)

<p>you can upload somewhere like google drive, onedrive, etc. and share the link.</p>

---

## Post #5 by @Varsha (2026-03-30 16:56 UTC)

<p><a href="https://unimailderbyac-my.sharepoint.com/:f:/g/personal/303958_derby_ac_uk/IgBg3XLCIatQQZ0-TGaBdDMkATKKgni1dM67KIzjBRQx6Q0?e=rBLajb" rel="noopener nofollow ugc">Bone 1</a></p>
<p>Hopefully, this is accessible.</p>

---

## Post #6 by @muratmaga (2026-03-30 18:21 UTC)

<p>I am not seeing a link</p>

---

## Post #7 by @Varsha (2026-03-30 20:17 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a> the folder Bone 1 contains the images. I have also included a separate link here if that helps: <a href="https://unimailderbyac-my.sharepoint.com/:f:/g/personal/303958_derby_ac_uk/IgBg3XLCIatQQZ0-TGaBdDMkATKKgni1dM67KIzjBRQx6Q0?e=UbAsNo" rel="noopener nofollow ugc">Bone 1</a></p>

---

## Post #8 by @muratmaga (2026-03-30 21:22 UTC)

<p>You have a space in your filenames. That’s not acceptable. Get rid off the space and it should work fine.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e182b530b4ede78db5edeff38982bea20ae637c6.png" data-download-href="/uploads/short-url/waXtcorXZehVq88xmjYe7M9pNHg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e182b530b4ede78db5edeff38982bea20ae637c6_2_690x181.png" alt="image" data-base62-sha1="waXtcorXZehVq88xmjYe7M9pNHg" width="690" height="181" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e182b530b4ede78db5edeff38982bea20ae637c6_2_690x181.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e182b530b4ede78db5edeff38982bea20ae637c6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e182b530b4ede78db5edeff38982bea20ae637c6.png 2x" data-dominant-color="E9E9E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">916×241 30.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/Extensions-34045/SlicerMorph/lib/Slicer-5.10/qt-scripted-modules/ImageStacks.py", line 412, in populateFromArchetype
    self.setFilePaths(filePaths)
  File "/Applications/Slicer.app/Contents/Extensions-34045/SlicerMorph/lib/Slicer-5.10/qt-scripted-modules/ImageStacks.py", line 358, in setFilePaths
    self.logic.filePaths = filePaths
    ^^^^^^^^^^^^^^^^^^^^
  File "/Applications/Slicer.app/Contents/Extensions-34045/SlicerMorph/lib/Slicer-5.10/qt-scripted-modules/ImageStacks.py", line 694, in filePaths
    image = reader.Execute()
            ^^^^^^^^^^^^^^^^
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/SimpleITK/SimpleITK.py", line 6215, in Execute
    return _SimpleITK.ImageFileReader_Execute(self)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: Exception thrown in SimpleITK ImageFileReader_Execute: /Users/svc-dashboard/D/S/A/ITK/Modules/IO/TIFF/src/itkTIFFImageIO.cxx:1414:
ITK ERROR: TIFFImageIO(0x7fe427b77b50): Problem reading the row: 120

</code></pre>

---

## Post #9 by @Varsha (2026-03-31 09:51 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a> I have got rid of the spaces in the image name itself. However, I keep getting the same error. I might of course have just done the wrong thing. Does this look right? I just can’t get the Load button to activate.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82bdafcee3f1d7518f28c8459c0be3880b80e2aa.png" data-download-href="/uploads/short-url/iEAtkMfXCOv7yOGpewgaaTFSwjg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82bdafcee3f1d7518f28c8459c0be3880b80e2aa_2_433x500.png" alt="image" data-base62-sha1="iEAtkMfXCOv7yOGpewgaaTFSwjg" width="433" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82bdafcee3f1d7518f28c8459c0be3880b80e2aa_2_433x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82bdafcee3f1d7518f28c8459c0be3880b80e2aa_2_649x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82bdafcee3f1d7518f28c8459c0be3880b80e2aa_2_866x1000.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1058×1220 52.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @pieper (2026-03-31 12:50 UTC)

<p>I believe he meant in the directory path too, so “Bone1” not “Bone 1”.</p>

---

## Post #11 by @issakomi (2026-03-31 15:40 UTC)

<blockquote>
<pre><code class="lang-auto">ITK ERROR: TIFFImageIO(0x7fe427b77b50): Problem reading the row: 120
</code></pre>
</blockquote>
<p><span lang="en">ITK’s TIFFImageIO can’t read these images. I’m not sure why, they’re multi-page, BTW.</span></p>
<p>This (extract 1st page) might help (I haven’t tested it in Slicer, but ITK’s TIFFImageIO can open output_Bone* images).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54e64238bfeb09f442368b831863d6de1150128b.png" data-download-href="/uploads/short-url/c73qW4eBxdDOLwofPcat6tEdcN5.png?dl=1" title="Screenshot at 2026-03-31 17-30-48" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54e64238bfeb09f442368b831863d6de1150128b_2_690x368.png" alt="Screenshot at 2026-03-31 17-30-48" data-base62-sha1="c73qW4eBxdDOLwofPcat6tEdcN5" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54e64238bfeb09f442368b831863d6de1150128b_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54e64238bfeb09f442368b831863d6de1150128b_2_1035x552.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54e64238bfeb09f442368b831863d6de1150128b_2_1380x736.png 2x" data-dominant-color="0F0F0F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot at 2026-03-31 17-30-48</span><span class="informations">1920×1026 208 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Edit:</p>
<p><code>convert</code> belongs to ImageMagick</p>
<p>Edit:</p>
<p>the second page seems to be the same image, but 160 × 120 pixels, perhaps it is not important.</p>

---

## Post #12 by @Varsha (2026-03-31 16:53 UTC)

<p><a class="mention" href="/u/issakomi">@issakomi</a> thanks for looking into this. Apologies- but could you explain in a little more detail how I might rectify this? <a class="mention" href="/u/pieper">@pieper</a> I tried it by changing the directory name as well- the issue persists.</p>

---

## Post #13 by @muratmaga (2026-03-31 17:08 UTC)

<p><a class="mention" href="/u/varsha">@Varsha</a> I opened the image using Fiji. To me images look like series of a focus stack from a microscope. This is not a modality you can do much with 3D Slicer. We expect true, continuous 3D data. It is also clear as <a class="mention" href="/u/issakomi">@issakomi</a> pointed out that the TIFF format they are in is not compatible with the TIFF readers Slicer support.</p>
<p>What are you hoping to do with this in Slicer? Even if you get it, you cannot construct a 3D volume from these.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b4a2093195293e1fa686f7a01078e02dd4d2e1b.jpeg" data-download-href="/uploads/short-url/3TpHVP6twtHon07rxcDvLZLzG43.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b4a2093195293e1fa686f7a01078e02dd4d2e1b_2_630x500.jpeg" alt="image" data-base62-sha1="3TpHVP6twtHon07rxcDvLZLzG43" width="630" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b4a2093195293e1fa686f7a01078e02dd4d2e1b_2_630x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b4a2093195293e1fa686f7a01078e02dd4d2e1b_2_945x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b4a2093195293e1fa686f7a01078e02dd4d2e1b.jpeg 2x" data-dominant-color="897E76"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">965×765 81.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @issakomi (2026-03-31 17:16 UTC)

<aside class="quote no-group" data-username="Varsha" data-post="12" data-topic="46561">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/aeb1de/48.png" class="avatar"> Varsha:</div>
<blockquote>
<p>thanks for looking into this. Apologies- but could you explain in a little more detail how I might rectify this?</p>
</blockquote>
</aside>
<p>I have simply extracted 1st page from multi-page tiff, in particular case there are 2 pages per image. I don’t know is it focus stack or whatever else. 1st is 2880 × 2160 pixels image, the 2nd page <em>seems</em> to be the same image, but 160 × 120 pixels. ITK’s TIFFImageIO can read extracted image. I have done with ImageMagick on Linux, s. screenshot.</p>

---

## Post #15 by @Varsha (2026-04-09 09:28 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a> I was ideally hoping to stack these images to create a 3D model, and then attempt Geometric Morphometric analysis. Would it be possible to reconstruct this into a 3D model using alternate softwares and then input these into 3D Slicer for GM analysis?</p>

---

## Post #16 by @muratmaga (2026-04-09 16:05 UTC)

<p>This is not something I am particularly knowledgeable, but when I searched for it, I saw specific microscopy based photogrammetry tools in which you should be able to do what you want (e.g,. see this video <a href="https://www.youtube.com/watch?v=wznsRLOpSiw" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=wznsRLOpSiw</a>)</p>
<p>The real issue you have only one view, everything I saw (and typically requirement of photogrammetry) is you have multiple angles so that the software can triangulate the 3D model. If you repeat that with many angles (possibly using a motor controlled microscopy stage), and the generate focused images for every angle (i.e., acquire a your focus stack for each angle and generate the focused image), then you might even be able to do it with SlicerMorph’s Photogrammetry extension ( <a href="https://github.com/SlicerMorph/SlicerPhotogrammetry" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/SlicerPhotogrammetry · GitHub</a> ).</p>
<p>If search for “3D models from focus stacks” on internet, there are a lot of resources.</p>
<p>But, yes, if you generate 3D models elsewhere you can do the GM in SlicerMorph.</p>

---

## Post #17 by @Varsha (2026-04-13 11:27 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a>  Thank you! This is really helpful.</p>

---
