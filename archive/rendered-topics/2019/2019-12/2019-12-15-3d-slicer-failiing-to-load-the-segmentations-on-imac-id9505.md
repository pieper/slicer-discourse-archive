---
topic_id: 9505
title: "3D Slicer Failiing To Load The Segmentations On Imac"
date: 2019-12-15
url: https://discourse.slicer.org/t/9505
---

# 3D slicer failiing to load the segmentations on iMac

**Topic ID**: 9505
**Date**: 2019-12-15
**URL**: https://discourse.slicer.org/t/3d-slicer-failiing-to-load-the-segmentations-on-imac/9505

---

## Post #1 by @nayansi.jha (2019-12-15 14:13 UTC)

<p>Slicer is not loading the segmentation files. It shows the progress bar and then it finishes, but nothing opens. Below is the error log, please help !</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d03edc29ac4af77805badcf43d84427594e9caff.png" data-download-href="/uploads/short-url/tIdZqEIiHMqLeC4yCF5cwwqO0Nh.png?dl=1" title="Screen Shot 2019-12-15 at 3.46.51 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d03edc29ac4af77805badcf43d84427594e9caff_2_690x238.png" alt="Screen Shot 2019-12-15 at 3.46.51 PM" data-base62-sha1="tIdZqEIiHMqLeC4yCF5cwwqO0Nh" width="690" height="238" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d03edc29ac4af77805badcf43d84427594e9caff_2_690x238.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d03edc29ac4af77805badcf43d84427594e9caff_2_1035x357.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d03edc29ac4af77805badcf43d84427594e9caff_2_1380x476.png 2x" data-dominant-color="E5E4EC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2019-12-15 at 3.46.51 PM</span><span class="informations">2892×1000 343 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code class="lang-auto">2019-12-15 15:44:54.680 Slicer[953:52097] Error from CoreDragRequestDragCompleteMessage: -1850

2019-12-15 15:44:55.897 Slicer[953:52097] Error in CoreDragGetMouseLocation: -1850

qSlicerScalarOverlayReader::options(): 0x7f8d3fd3a440

qSlicerScalarOverlayReader::options(): 0x7f8d3fd3a440

qSlicerScalarOverlayReader::options(): 0x7f8d3fd3a440

qSlicerScalarOverlayReader::options(): 0x7f8d3fd3a440

Loaded volume from file: /Users/nayansijha/Desktop/shape crrs 20191214/T0 mandSEG.gipl.gz. Dimensions: 768x768x576. Number of components: 1. Pixel type: unsigned short.

"Volume" Reader has successfully read the file "/Users/nayansijha/Desktop/shape crrs 20191214/T0 mandSEG.gipl.gz" "[2.16s]"

Loaded volume from file: /Users/nayansijha/Desktop/shape crrs 20191214/T0 scan.gipl.gz. Dimensions: 768x768x576. Number of components: 1. Pixel type: short.

"Volume" Reader has successfully read the file "/Users/nayansijha/Desktop/shape crrs 20191214/T0 scan.gipl.gz" "[5.40s]"

Loaded volume from file: /Users/nayansijha/Desktop/shape crrs 20191214/T1 mandSEG.gipl.gz. Dimensions: 768x768x576. Number of components: 1. Pixel type: unsigned short.

"Volume" Reader has successfully read the file "/Users/nayansijha/Desktop/shape crrs 20191214/T1 mandSEG.gipl.gz" "[2.05s]"

Loaded volume from file: /Users/nayansijha/Desktop/shape crrs 20191214/T1 scan.gipl.gz. Dimensions: 768x768x576. Number of components: 1. Pixel type: short.

"Volume" Reader has successfully read the file "/Users/nayansijha/Desktop/shape crrs 20191214/T1 scan.gipl.gz" "[5.49s]"
</code></pre>

---

## Post #2 by @lassoan (2019-12-15 14:38 UTC)

<p>In “Add data” dialog, click “LabelMap” option to load volumes as labelmaps. You can then convert them to segmentation by right-clicking them in Data module.</p>
<p>You can directly load more commonly used file formats (nrrd and nifti) as segmentation directly, by setting “Description” to “Segmentation” in “Add data” dialog.</p>

---

## Post #3 by @nayansi.jha (2019-12-15 21:49 UTC)

<p>Yes,I have tried that several times(clicking label map option to load volumes) but the segmentations don’t upload either with direct drag and drop or with the add data method.I even tried to install previous versions but I am getting the same problem continuously. The screen starts loading but after several seconds it just goes blank.</p>

---

## Post #4 by @lassoan (2019-12-15 22:39 UTC)

<p>Can you share one example file? (upload to dropbox/onedrive/google drive and post the link)</p>

---

## Post #5 by @nayansi.jha (2019-12-15 23:21 UTC)

<p>Yes sure.<br>
I made a small video with drop and drag method.Please have a look.<br>
<a href="https://drive.google.com/open?id=1IK3FVRTs7AwgIdIIHNAXB8Xz6fDZuKsN" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/open?id=1IK3FVRTs7AwgIdIIHNAXB8Xz6fDZuKsN</a></p>

---

## Post #6 by @lassoan (2019-12-15 23:36 UTC)

<p>Google drive did not let me access any files (“You need permission…”)? Can you grant access or make the files public? Can you upload a .gipl.gz file, too?</p>

---

## Post #7 by @nayansi.jha (2019-12-15 23:42 UTC)

<p>Sorry for botheration. I gave you access and uploaded the gipl files as well.</p>

---

## Post #8 by @lassoan (2019-12-16 00:17 UTC)

<p>What you did was mostly correct, except you should never click “Centered” option, as it discards the real image position and moves it to the coordinate system center.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a88533e0913165280393302958459506d7c9020.png" data-download-href="/uploads/short-url/3MIulPNxoyQFJBaidq832RBa1jy.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a88533e0913165280393302958459506d7c9020_2_690x219.png" alt="image" data-base62-sha1="3MIulPNxoyQFJBaidq832RBa1jy" width="690" height="219" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a88533e0913165280393302958459506d7c9020_2_690x219.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a88533e0913165280393302958459506d7c9020_2_1035x328.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a88533e0913165280393302958459506d7c9020_2_1380x438.png 2x" data-dominant-color="EEEEF2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1486×473 30.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You don’t see anything in 3D view, because you only show a 3D view and images are not shown in 3D view by default. Switch to 4-up view layout using the <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89c66d615159707ed47b4a72482f9972aeef37ee.png" alt="image" data-base62-sha1="jEOxB60OsSkqPwT5wqXtd8joAxM" width="54" height="53"> button on the toolbar.</p>
<p>You can show CT volumes using “Volume rendering” module.</p>
<p>To visualize segmentations in 3D, I would recommend to convert labelmap volume nodes to segmentation nodes using “Data” module then go to “Segmentations” module and click on “Create” button next to “Closed surface” in “Representations” section.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/1943f22b1ec7d8f47f3bf7f0dc250daae8fb92d1.png" data-download-href="/uploads/short-url/3BvvDIiFist1huh35AAJP8dHXtD.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/1943f22b1ec7d8f47f3bf7f0dc250daae8fb92d1_2_664x500.png" alt="image" data-base62-sha1="3BvvDIiFist1huh35AAJP8dHXtD" width="664" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/1943f22b1ec7d8f47f3bf7f0dc250daae8fb92d1_2_664x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/1943f22b1ec7d8f47f3bf7f0dc250daae8fb92d1_2_996x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/1943f22b1ec7d8f47f3bf7f0dc250daae8fb92d1.png 2x" data-dominant-color="EAE8EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1010×760 45.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Visualization of CT volumes using volume rendering and segmentations as closed surface in 3D:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b6d425f4c94aa025446f8178aa86d8341a7054a.jpeg" data-download-href="/uploads/short-url/jTqse8JVaAGSFzDIQ7NGY283oYW.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b6d425f4c94aa025446f8178aa86d8341a7054a_2_690x305.jpeg" alt="image" data-base62-sha1="jTqse8JVaAGSFzDIQ7NGY283oYW" width="690" height="305" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b6d425f4c94aa025446f8178aa86d8341a7054a_2_690x305.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b6d425f4c94aa025446f8178aa86d8341a7054a_2_1035x457.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b6d425f4c94aa025446f8178aa86d8341a7054a_2_1380x610.jpeg 2x" data-dominant-color="A0A09F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×999 536 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @nayansi.jha (2019-12-16 00:42 UTC)

<p>I got it.Thanks a million times.You have been a great help.</p>

---
