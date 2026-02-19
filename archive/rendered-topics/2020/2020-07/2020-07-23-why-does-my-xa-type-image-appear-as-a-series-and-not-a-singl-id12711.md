---
topic_id: 12711
title: "Why Does My Xa Type Image Appear As A Series And Not A Singl"
date: 2020-07-23
url: https://discourse.slicer.org/t/12711
---

# Why does my XA type image appear as a series and not a single 2D image?

**Topic ID**: 12711
**Date**: 2020-07-23
**URL**: https://discourse.slicer.org/t/why-does-my-xa-type-image-appear-as-a-series-and-not-a-single-2d-image/12711

---

## Post #1 by @Henry_Cope (2020-07-23 19:16 UTC)

<p>Hello All,</p>
<p>I’m trying to view an xray angiography, but i can only see/load it as a series of DICOMs that look like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cf6542c39077842da89f98c6daa671d68857ba3.png" alt="image" data-base62-sha1="k70BntLcki8D1lKVPrmI4oNuph1" width="319" height="285"><br>
What’s more is that these slices don’t appear as I would expect them to for an X-ray image, as I can’t see the surrounding ribs like I would in this DSA from the same patient:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50c5d27c4f82633abac2807992c90b6837750edc.png" alt="image" data-base62-sha1="bwy1QpLu4KG5ImrjDmShXKrkbWk" width="262" height="157"><br>
I’m really confused as to why it says this series is of type XA when it seems more like a CT. Is there any way to combine the DICOM series into one xray? I would use the DSAs but unlike the DICOM series, they don’t contain the metadata for position and orientation.</p>

---

## Post #2 by @lassoan (2020-07-23 20:37 UTC)

<p>Interestingly, very few users have ever asked for XA (either native or DSA) image support over the years, so we haven’t tested how well it works. There is a good chance that there are some trivial issues that we should fix. Can you share some example sequencea that you have problem with? Preferably images of phantoms or public data sets, but anonymized patient images are OK, too.</p>

---

## Post #3 by @Henry_Cope (2020-07-23 20:51 UTC)

<p>Hi Mr. Lasso,</p>
<p>thanks for the quick response. I’d like to share the anonymized patient data, but I’m not sure what is the best way to go about posting multiple .dcm files. How should I go about uploading them?</p>

---

## Post #4 by @lassoan (2020-07-23 21:12 UTC)

<p>You can upload to dropbox/onedrive/Google drive and post the link here.</p>

---

## Post #5 by @Henry_Cope (2020-07-23 21:31 UTC)

<p>Thank you, here’s the link:<br>
<a href="https://drive.google.com/drive/folders/18eXHksqm7iUQZ1IiX_sVzKosWP_WvBx1?usp=sharing" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/drive/folders/18eXHksqm7iUQZ1IiX_sVzKosWP_WvBx1?usp=sharing</a></p>

---

## Post #6 by @lassoan (2020-07-24 04:13 UTC)

<p>Thank you. This series is created by a Siemens Axiom Artis robotic C-arm that can reconstruct cone-beam CT from rotational XA acquisitions. The series contains is a reconstructed 3D volume and a localizer image.</p>
<p>Presence of the localizer image messes up default loading, so for now you need to open “Advanced” section and chose the two loadables by imageType. One of them is the localizer image, the other one is the volume:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb167dbf0501e9037491ae16cdcad43c712792a5.png" data-download-href="/uploads/short-url/qH3toACUaQtOJjSN2jznSTVTRfT.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb167dbf0501e9037491ae16cdcad43c712792a5_2_690x416.png" alt="image" data-base62-sha1="qH3toACUaQtOJjSN2jznSTVTRfT" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb167dbf0501e9037491ae16cdcad43c712792a5_2_690x416.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb167dbf0501e9037491ae16cdcad43c712792a5_2_1035x624.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb167dbf0501e9037491ae16cdcad43c712792a5_2_1380x832.png 2x" data-dominant-color="EAEEF1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1362 413 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Loaded 3D volume:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ace4042daa8dfb8b91362b27fc17c7f600f84523.jpeg" data-download-href="/uploads/short-url/oFsE9veN4Y5YnCkyrPctQZw9vFx.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ace4042daa8dfb8b91362b27fc17c7f600f84523_2_690x419.jpeg" alt="image" data-base62-sha1="oFsE9veN4Y5YnCkyrPctQZw9vFx" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ace4042daa8dfb8b91362b27fc17c7f600f84523_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ace4042daa8dfb8b91362b27fc17c7f600f84523_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ace4042daa8dfb8b91362b27fc17c7f600f84523_2_1380x838.jpeg 2x" data-dominant-color="9C9CAA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1370 630 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I’ve implemented a mechanism in the DICOM module to detect such localizer images and load the volume correctly with default settings. It is currently <a href="https://github.com/Slicer/Slicer/pull/5055">under review</a> and probably will be available in the Slicer Preview Release within a few days.</p>

---

## Post #7 by @Henry_Cope (2020-07-24 13:31 UTC)

<p>Mr. Lasso,</p>
<p>Thank you for the assistance, I didn’t realize these were rotational XA acquisitions.<br>
I’m still not certain I understand how to reproduce the result you have. I follow the steps that you’ve put, 1. click Advanced, 2. click examine, 3. uncheck the 12: Sagittal (which I’m guessing is the localizer image), 4 and 5. click the the volumes, 6. load these volumes.<br>
But when I load the volumes, it still shows up as a 2D object:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e84b52f752309738f26105a1773bc39e8f917e08.jpeg" data-download-href="/uploads/short-url/x8Y9yXfkfwAyTqbEtAN9RXQU9cs.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e84b52f752309738f26105a1773bc39e8f917e08_2_259x500.jpeg" alt="image" data-base62-sha1="x8Y9yXfkfwAyTqbEtAN9RXQU9cs" width="259" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e84b52f752309738f26105a1773bc39e8f917e08_2_259x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e84b52f752309738f26105a1773bc39e8f917e08_2_388x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e84b52f752309738f26105a1773bc39e8f917e08_2_518x1000.jpeg 2x" data-dominant-color="393945"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">664×1279 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Trying to render this as a 3D volume crashes Slicer for me.</p>

---

## Post #8 by @lassoan (2020-07-25 04:02 UTC)

<p>“12: SAGITTAL - imageType 1” is the single-slice localizer image and “12: SAGITTAL - imageType 2” is the 3D volume. Check only “12: SAGITTAL - imageType 2” and uncheck everything else, then click Load.</p>
<p>You may also try the latest Slicer Preview Release (revision 29227 or later), which should load the correct  image by default (without enabling “Advanced”).</p>

---
