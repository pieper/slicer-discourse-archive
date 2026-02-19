---
topic_id: 26395
title: "Covid Lung Radiomics Feature Extraction"
date: 2022-11-23
url: https://discourse.slicer.org/t/26395
---

# Covid lung radiomics feature extraction

**Topic ID**: 26395
**Date**: 2022-11-23
**URL**: https://discourse.slicer.org/t/covid-lung-radiomics-feature-extraction/26395

---

## Post #1 by @Nima_Yousefi (2022-11-23 07:16 UTC)

<p>Hello<br>
I’m working on feature extraction from lung  and extracted features from left and right lung.<br>
My question is: is it possible to extract features from total lung?</p>

---

## Post #2 by @rbumm (2022-11-23 08:17 UTC)

<p>Yes, if you use Lung CT Segmenter and perform a lung segmentation, the module will create a segment “thoracic cavity” which - if you do not check “vessel segmentation” - will contain both the right and left lung.<br>
I´ll add a standard segment named “lungs” within the next few days.</p>

---

## Post #3 by @Nima_Yousefi (2022-11-23 15:32 UTC)

<p>I have another question if you can help me <a class="mention" href="/u/rbumm">@rbumm</a><br>
I checked “airway segmentation” then After radiomics features extracted, both image nrrd file and its labelmap(mask) nrrd file add to directory path and then “remove” from it.</p>
<p>Is it intended?</p>

---

## Post #4 by @rbumm (2022-11-23 20:16 UTC)

<p>Do you mean the files that are displayed here?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90a509b4eee4b405033d589cc91a04d63185bc53.png" data-download-href="/uploads/short-url/kDAlz8GN0hRqH9pwHDevfhpsuJB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90a509b4eee4b405033d589cc91a04d63185bc53.png" alt="image" data-base62-sha1="kDAlz8GN0hRqH9pwHDevfhpsuJB" width="690" height="72" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">881×93 2.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>They seem to be temporary files.</p>

---

## Post #5 by @Nima_Yousefi (2022-11-23 20:46 UTC)

<p>Yes exactly<br>
Actually I’m looking for a binary mask like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97cb7bd3f12c05eb221d64077942663e9c1bea43.jpeg" data-download-href="/uploads/short-url/lEQ3I6nt8QbhD3QuVsDFDfDinYv.jpeg?dl=1" title="Screenshot_20221123-112422_Firefox" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97cb7bd3f12c05eb221d64077942663e9c1bea43_2_580x500.jpeg" alt="Screenshot_20221123-112422_Firefox" data-base62-sha1="lEQ3I6nt8QbhD3QuVsDFDfDinYv" width="580" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97cb7bd3f12c05eb221d64077942663e9c1bea43_2_580x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97cb7bd3f12c05eb221d64077942663e9c1bea43.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97cb7bd3f12c05eb221d64077942663e9c1bea43.jpeg 2x" data-dominant-color="3A3A3A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20221123-112422_Firefox</span><span class="informations">776×668 15 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How can I create something like this in slicer?</p>

---

## Post #6 by @rbumm (2022-11-24 09:04 UTC)

<aside class="quote no-group" data-username="Nima_Yousefi" data-post="5" data-topic="26395">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nima_yousefi/48/66845_2.png" class="avatar"> Nima_Yousefi:</div>
<blockquote>
<p>How can I create something like this in slicer?</p>
</blockquote>
</aside>
<p>You could run Lung CT Segmenter, then go to “Data”, right-click “Lung Segmentation”  and “Export visible segments to binary labelmap”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4ef19b4f317e567d4a1af3fdf455c15d6cfeb23.png" data-download-href="/uploads/short-url/pOCdkjyi1bOjazhjlcX8GIuG8in.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4ef19b4f317e567d4a1af3fdf455c15d6cfeb23_2_690x267.png" alt="image" data-base62-sha1="pOCdkjyi1bOjazhjlcX8GIuG8in" width="690" height="267" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4ef19b4f317e567d4a1af3fdf455c15d6cfeb23_2_690x267.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4ef19b4f317e567d4a1af3fdf455c15d6cfeb23_2_1035x400.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4ef19b4f317e567d4a1af3fdf455c15d6cfeb23.png 2x" data-dominant-color="A2A59F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1243×481 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Of course, many other options exist in 3D Slicer’s “Segment Editor” to create binary masks.</p>

---

## Post #7 by @Nima_Yousefi (2022-12-01 14:57 UTC)

<p>Hello Dr bumm.<br>
I have one question<br>
Did “lungs” segmenter added to lung segmenter option  in the lastest slicer update?</p>

---

## Post #8 by @rbumm (2022-12-01 15:31 UTC)

<p>Yes, “lungs” now get automatically created upon your request (Slicer 5.2.1), but you would need to checkbox them in “Data” as “visible”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a1cef60dd477760d866a027c9caec10ad5fbc02.jpeg" data-download-href="/uploads/short-url/3J0pfNPhAUQpFwElV2I6nzH1KSK.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a1cef60dd477760d866a027c9caec10ad5fbc02_2_690x288.jpeg" alt="image" data-base62-sha1="3J0pfNPhAUQpFwElV2I6nzH1KSK" width="690" height="288" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a1cef60dd477760d866a027c9caec10ad5fbc02_2_690x288.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a1cef60dd477760d866a027c9caec10ad5fbc02_2_1035x432.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a1cef60dd477760d866a027c9caec10ad5fbc02_2_1380x576.jpeg 2x" data-dominant-color="96999C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×802 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @Nima_Yousefi (2022-12-06 07:10 UTC)

<p>Hello Dr bumm.<br>
is it possible to show radiomics features like glcm on the ct images in the slicer?<br>
Example:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6f619fea8515917934380edf9ac40dde581b0e9.jpeg" data-download-href="/uploads/short-url/nP0wS9s8g4dLWs8KGKotANJhZdD.jpeg?dl=1" title="Screenshot_20221206-103027_Drive" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6f619fea8515917934380edf9ac40dde581b0e9_2_690x269.jpeg" alt="Screenshot_20221206-103027_Drive" data-base62-sha1="nP0wS9s8g4dLWs8KGKotANJhZdD" width="690" height="269" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6f619fea8515917934380edf9ac40dde581b0e9_2_690x269.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6f619fea8515917934380edf9ac40dde581b0e9.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6f619fea8515917934380edf9ac40dde581b0e9.jpeg 2x" data-dominant-color="AFB6C1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20221206-103027_Drive</span><span class="informations">972×379 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Best regard.</p>

---

## Post #10 by @rbumm (2022-12-06 09:52 UTC)

<p>Hello <a class="mention" href="/u/nima_yousefi">@Nima_Yousefi</a> ,</p>
<p>This is an interesting question, I do not have a direct solution and am not aware of a pyradiomics voxel-mapping 3D Slicer function.<br>
You may need to run voxel-based radiomics from the command line to obtain the results you are aiming for.</p>
<p>Could maybe <a class="mention" href="/u/joostjm">@JoostJM</a> or other specialists comment, thank you.</p>

---

## Post #11 by @Nima_Yousefi (2023-01-03 19:14 UTC)

<p>Greeting Dr bumm<br>
about Shape, Texture, First Orderfeatures (like mean, autocorrelation , flatness , …)</p>
<p>what is their unit of measurements?</p>
<p>Thanks.</p>

---
