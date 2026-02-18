# DentalSegmentator result mesh is inverted

**Topic ID**: 37408
**Date**: 2024-07-16
**URL**: https://discourse.slicer.org/t/dentalsegmentator-result-mesh-is-inverted/37408

---

## Post #1 by @Romulo_Alfaro (2024-07-16 08:19 UTC)

<p>Hello, can someone help me please. I am using the DentalSegmentator Extension but the meshes come out inverted. I’ve been trying to change the settings for several hours but I haven’t been able to solve it. I thank you for your responses.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/089d5356c5b88e8415fe5247ca30ccb1ea95b134.jpeg" data-download-href="/uploads/short-url/1ecT4beidFbXY418O8gUxUvei8Y.jpeg?dl=1" title="Captura de pantalla 2024-07-16 a la(s) 2.32.33 a. m." rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/089d5356c5b88e8415fe5247ca30ccb1ea95b134_2_557x500.jpeg" alt="Captura de pantalla 2024-07-16 a la(s) 2.32.33 a. m." data-base62-sha1="1ecT4beidFbXY418O8gUxUvei8Y" width="557" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/089d5356c5b88e8415fe5247ca30ccb1ea95b134_2_557x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/089d5356c5b88e8415fe5247ca30ccb1ea95b134_2_835x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/089d5356c5b88e8415fe5247ca30ccb1ea95b134_2_1114x1000.jpeg 2x" data-dominant-color="5E514F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-07-16 a la(s) 2.32.33 a. m.</span><span class="informations">1596×1432 64.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @mau_igna_06 (2024-07-16 14:34 UTC)

<p>If that’s a surface (or mesh or, as Slicer calls them, modelNode) then you just need to execute a filter to flip the normals.<br>
In Slicer you can do it like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2cd544b86c66880cf6b0f6edab84d02e11f2f08.png" data-download-href="/uploads/short-url/u4Qbs9h356jKxALwOU6Ia1KxjXW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2cd544b86c66880cf6b0f6edab84d02e11f2f08_2_586x500.png" alt="image" data-base62-sha1="u4Qbs9h356jKxALwOU6Ia1KxjXW" width="586" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2cd544b86c66880cf6b0f6edab84d02e11f2f08_2_586x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2cd544b86c66880cf6b0f6edab84d02e11f2f08_2_879x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2cd544b86c66880cf6b0f6edab84d02e11f2f08_2_1172x1000.png 2x" data-dominant-color="B7B8CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1185×1010 216 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hope it helps</p>

---

## Post #4 by @Romulo_Alfaro (2024-07-16 17:04 UTC)

<p>Thanks for your answer. I did what you told me but when exporting to STL it still gives me an inverted mesh. I still need help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/4911de7a33232e9fec54b2d7fc1cb44296e84f2d.jpeg" data-download-href="/uploads/short-url/aqp8EF3VXrgBaP0BkVV3zuFTjDn.jpeg?dl=1" title="Captura de pantalla 2024-07-16 a la(s) 12.03.18 p. m." rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4911de7a33232e9fec54b2d7fc1cb44296e84f2d_2_690x387.jpeg" alt="Captura de pantalla 2024-07-16 a la(s) 12.03.18 p. m." data-base62-sha1="aqp8EF3VXrgBaP0BkVV3zuFTjDn" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4911de7a33232e9fec54b2d7fc1cb44296e84f2d_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4911de7a33232e9fec54b2d7fc1cb44296e84f2d_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4911de7a33232e9fec54b2d7fc1cb44296e84f2d_2_1380x774.jpeg 2x" data-dominant-color="6C6A66"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-07-16 a la(s) 12.03.18 p. m.</span><span class="informations">1920×1078 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/6613ab04ffb7cff097f2727329d94acc894d17d2.jpeg" data-download-href="/uploads/short-url/ez0Q7bfYdjBHVSUtdWqaVkOmWfo.jpeg?dl=1" title="Captura de pantalla 2024-07-16 a la(s) 12.04.11 p. m." rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/6613ab04ffb7cff097f2727329d94acc894d17d2_2_690x425.jpeg" alt="Captura de pantalla 2024-07-16 a la(s) 12.04.11 p. m." data-base62-sha1="ez0Q7bfYdjBHVSUtdWqaVkOmWfo" width="690" height="425" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/6613ab04ffb7cff097f2727329d94acc894d17d2_2_690x425.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/6613ab04ffb7cff097f2727329d94acc894d17d2_2_1035x637.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/6613ab04ffb7cff097f2727329d94acc894d17d2_2_1380x850.jpeg 2x" data-dominant-color="534C4B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-07-16 a la(s) 12.04.11 p. m.</span><span class="informations">1920×1184 41.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2024-07-16 18:30 UTC)

<p>STL file cannot save surface normals, so you would need to reorient triangles if you want to turn the surface inside out. You could do that by applying <a href="https://vtk.org/doc/nightly/html/classvtkReverseSense.html">vtkReverseSense</a> filter (by running a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#apply-vtk-filter-on-a-model-node">couple of lines of Python code</a>).</p>
<p>But it is probably better to fix the root cause of having an inverted surface.</p>
<p>What file format was the input image stored in? If NIFTI then you have a chance of getting into issues with image orientation. Using the latest Slicer Preview Release contain some error mitigation mechanisms that can help with NIFTI files.</p>
<p>How have you created the STL file? Have you applied any transforms? Are all the segments inverted? If you smooth the inverted segment a bit does the surface orientation gets fixed?</p>
<p>Why is it a problem that the triangles are oriented? What processing do you want to do in what software?</p>

---

## Post #6 by @Romulo_Alfaro (2024-07-16 18:39 UTC)

<p>This is the second time I have used DentalSegmentator. The first time the meshes were oriented normally.<br>
This second time all the meshes are inverted.<br>
I haven’t done any transformations, this is how DentalSegmentation generated the segments.<br>
Or is this how DentalSegmentator usually generates segmentation?</p>
<p>No specific program, it’s just my curiosity to be able to correct this orientation.</p>
<p>Thank you for reading.</p>
<p>PD. I’m afraid that Python code is something very complex for me.</p>

---

## Post #7 by @lassoan (2024-07-16 18:43 UTC)

<p>Did you load the image from DICOM, NIFTI, NRRD, or other file format?</p>
<p>If you don’t have any specific task in mind then a simple option is to ignore the polygon ordering. Most software that can process meshes can also reorient the polygons automatically or when it is needed.</p>

---

## Post #8 by @Romulo_Alfaro (2024-07-16 18:48 UTC)

<p>They were loaded from DICOM (CBCT).</p>
<p>The first time I did it through CT and this second time through CBCT.</p>
<p>I will continue testing. I still hope to correct the orientation.</p>

---

## Post #9 by @Thibault_Pelletier (2024-07-17 15:01 UTC)

<p>Hi <a class="mention" href="/u/romulo_alfaro">@Romulo_Alfaro</a>,</p>
<p>For the cases where you have the inverted mesh problem, could you test the following :</p>
<ul>
<li>Load the data</li>
<li>Go to the segment editor</li>
<li>Add segment</li>
<li>Select brush + Sphere brush</li>
<li>Paint a sphere in a 2D view</li>
<li>Export to files in STL (see screen capture below)</li>
<li>Check if the inversion is present in the exported sphere STL file</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c8ed0094fdc08ab02bef95eba56312733ed1998.png" data-download-href="/uploads/short-url/1N5HFp9R2DUVQjF97gtwCxXVT1S.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c8ed0094fdc08ab02bef95eba56312733ed1998_2_690x163.png" alt="image" data-base62-sha1="1N5HFp9R2DUVQjF97gtwCxXVT1S" width="690" height="163" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c8ed0094fdc08ab02bef95eba56312733ed1998_2_690x163.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c8ed0094fdc08ab02bef95eba56312733ed1998.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c8ed0094fdc08ab02bef95eba56312733ed1998.png 2x" data-dominant-color="D8DEE8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">960×228 44.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>From my tests, an inversion case was coming from the input data frame of reference which didn’t match the expected one in 3D Slicer.</p>
<p>I implemented a tentative fixe for that in  (<a href="https://github.com/Slicer/Slicer/pull/7627" rel="noopener nofollow ugc">#7627</a>) which was successively patched by <a class="mention" href="/u/lassoan">@lassoan</a> for regressions by (<a href="https://github.com/Slicer/Slicer/pull/7773" rel="noopener nofollow ugc">#7773</a>, <a href="https://github.com/Slicer/Slicer/pull/7746" rel="noopener nofollow ugc">#7746</a>).</p>
<p>If the same behavior is still present in your data, we may have to see why it’s not properly taken into account.</p>
<p>Best,<br>
Thibault</p>

---

## Post #10 by @Romulo_Alfaro (2024-07-17 15:10 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96d9123226f43e5169731aeac1255b8b4bde1e1b.jpeg" data-download-href="/uploads/short-url/lwsGYGxbGMIjP6TvGCVlrelLiLp.jpeg?dl=1" title="Captura de pantalla 2024-07-17 a la(s) 10.08.06 a. m." rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96d9123226f43e5169731aeac1255b8b4bde1e1b_2_500x500.jpeg" alt="Captura de pantalla 2024-07-17 a la(s) 10.08.06 a. m." data-base62-sha1="lwsGYGxbGMIjP6TvGCVlrelLiLp" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96d9123226f43e5169731aeac1255b8b4bde1e1b_2_500x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96d9123226f43e5169731aeac1255b8b4bde1e1b_2_750x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96d9123226f43e5169731aeac1255b8b4bde1e1b_2_1000x1000.jpeg 2x" data-dominant-color="4E4947"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-07-17 a la(s) 10.08.06 a. m.</span><span class="informations">1542×1540 97 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @Thibault_Pelletier (2024-07-17 15:19 UTC)

<p>Thanks for your test!</p>
<p>If you have not already done so, could you do the same test using the latest 3D Slicer 5.7 preview version?</p>
<p>If the problem is still present, could you share one of the data you experience this problem?</p>

---

## Post #12 by @Romulo_Alfaro (2024-07-17 15:22 UTC)

<p>I am using version 5.7 for Mac</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15dbfe06ea23238b85e16b2f1cdc06264cee7534.jpeg" data-download-href="/uploads/short-url/37nmcTwGblmRt54B6xZcVBpooCM.jpeg?dl=1" title="Captura de pantalla 2024-07-17 a la(s) 10.21.07 a. m." rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15dbfe06ea23238b85e16b2f1cdc06264cee7534_2_690x467.jpeg" alt="Captura de pantalla 2024-07-17 a la(s) 10.21.07 a. m." data-base62-sha1="37nmcTwGblmRt54B6xZcVBpooCM" width="690" height="467" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15dbfe06ea23238b85e16b2f1cdc06264cee7534_2_690x467.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15dbfe06ea23238b85e16b2f1cdc06264cee7534_2_1035x700.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15dbfe06ea23238b85e16b2f1cdc06264cee7534_2_1380x934.jpeg 2x" data-dominant-color="85857D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-07-17 a la(s) 10.21.07 a. m.</span><span class="informations">1486×1006 81.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @lassoan (2024-07-17 19:06 UTC)

<aside class="quote no-group" data-username="Romulo_Alfaro" data-post="12" data-topic="37408">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/romulo_alfaro/48/77327_2.png" class="avatar"> Romulo_Alfaro:</div>
<blockquote>
<p>I am using version 5.7 for Mac</p>
</blockquote>
</aside>
<p>Which version exactly?</p>

---

## Post #14 by @Romulo_Alfaro (2024-07-17 19:16 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a0386ee3aae7564084895e66f14c95a6768307c.png" data-download-href="/uploads/short-url/8hdfv10jaQVuLd6Mf5DDKlPSTA8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a0386ee3aae7564084895e66f14c95a6768307c_2_690x434.png" alt="image" data-base62-sha1="8hdfv10jaQVuLd6Mf5DDKlPSTA8" width="690" height="434" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a0386ee3aae7564084895e66f14c95a6768307c_2_690x434.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a0386ee3aae7564084895e66f14c95a6768307c_2_1035x651.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a0386ee3aae7564084895e66f14c95a6768307c.png 2x" data-dominant-color="535258"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1338×842 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I just used DentalSegmentator on other DICOM file (CT) and the orientation was correct. Apparently and so far, it only happens with CBCT files.</p>

---

## Post #15 by @lassoan (2024-07-17 21:00 UTC)

<p>Could you take a screenshot of the IJK to RAS direction matrix in Volumes module?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a5dd35cd96e8777530f91c8e9bbe32d71c2f4ac.png" data-download-href="/uploads/short-url/faXDcObPdhXQFDurJarXeVw4ln6.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a5dd35cd96e8777530f91c8e9bbe32d71c2f4ac_2_562x500.png" alt="image" data-base62-sha1="faXDcObPdhXQFDurJarXeVw4ln6" width="562" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a5dd35cd96e8777530f91c8e9bbe32d71c2f4ac_2_562x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a5dd35cd96e8777530f91c8e9bbe32d71c2f4ac_2_843x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a5dd35cd96e8777530f91c8e9bbe32d71c2f4ac.png 2x" data-dominant-color="3F3E3C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1015×903 49.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is the volume under a transform? (In Data module, if you right-click on the transform column in the volume’s row then is the “None” option is selected or some transform?)</p>

---

## Post #16 by @Romulo_Alfaro (2024-07-18 04:20 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f16543bf09f3df2d38fc9e898f2b2f0857ba0d30.png" data-download-href="/uploads/short-url/yru1MV4dgst1rI3OA2mRPzwXJPq.png?dl=1" title="Captura de pantalla 2024-07-17 a la(s) 11.17.23 p. m." rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f16543bf09f3df2d38fc9e898f2b2f0857ba0d30_2_690x462.png" alt="Captura de pantalla 2024-07-17 a la(s) 11.17.23 p. m." data-base62-sha1="yru1MV4dgst1rI3OA2mRPzwXJPq" width="690" height="462" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f16543bf09f3df2d38fc9e898f2b2f0857ba0d30_2_690x462.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f16543bf09f3df2d38fc9e898f2b2f0857ba0d30_2_1035x693.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f16543bf09f3df2d38fc9e898f2b2f0857ba0d30_2_1380x924.png 2x" data-dominant-color="343434"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-07-17 a la(s) 11.17.23 p. m.</span><span class="informations">1452×974 50.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5f548a72cf6538dd2ab7583a144d15d0c0452f2.jpeg" data-download-href="/uploads/short-url/uwLdB5nVeWRkB5pu7mISRrZBYTE.jpeg?dl=1" title="Captura de pantalla 2024-07-17 a la(s) 11.19.45 p. m." rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5f548a72cf6538dd2ab7583a144d15d0c0452f2_2_690x299.jpeg" alt="Captura de pantalla 2024-07-17 a la(s) 11.19.45 p. m." data-base62-sha1="uwLdB5nVeWRkB5pu7mISRrZBYTE" width="690" height="299" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5f548a72cf6538dd2ab7583a144d15d0c0452f2_2_690x299.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5f548a72cf6538dd2ab7583a144d15d0c0452f2_2_1035x448.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5f548a72cf6538dd2ab7583a144d15d0c0452f2_2_1380x598.jpeg 2x" data-dominant-color="404545"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-07-17 a la(s) 11.19.45 p. m.</span><span class="informations">1930×838 185 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #17 by @lassoan (2024-07-18 04:35 UTC)

<p>Why do you have two segmentations and images?</p>
<p>Where/how did you use NIFTI? (The .nii suffix suggests that it may have been used)</p>
<p>Can you share an anonymized scene file (saved as a single .mrb file) so that we can investigate further?</p>

---

## Post #18 by @Romulo_Alfaro (2024-07-18 04:52 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://wetransfer.com/downloads/c8f3b78021f3df4b437c7aa17ddec82f20240718045151/5b1000">
  <header class="source">
      <img src="https://wetransfer.com/favicon.ico" class="site-icon" width="64" height="64">

      <a href="https://wetransfer.com/downloads/c8f3b78021f3df4b437c7aa17ddec82f20240718045151/5b1000" target="_blank" rel="noopener nofollow ugc">wetransfer.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://wetransfer.com/downloads/c8f3b78021f3df4b437c7aa17ddec82f20240718045151/5b1000" target="_blank" rel="noopener nofollow ugc">Archivo.zip</a></h3>

  <p>1 file sent via WeTransfer, the simplest way to send your files around the world</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #19 by @mohammed_alshakhas (2024-07-18 07:45 UTC)

<p>i had couple of volume having distortion / compression issues with same module . i tried mona and had a good outcome .</p>

---

## Post #20 by @lassoan (2024-07-18 16:50 UTC)

<p>Thanks for the example file, it helped a lot confirming what was happening. The <code>479068 AXIAL.nrrd</code> file uses left-handed coordinate system (<code>space directions: (0.39999999999999997,0,0) (0,0.39999999999999997,0) (0,0,-0.40000000000000191)</code>), which causes the segmentation to be turned inside out.</p>
<p>Have you used the DICOM browser to load the CBCT image (<code>DICOM import</code> in Data module)? Or you forced loading using the legacy image reader (<code>Volume</code> option in Data module)?</p>
<p>I’ve submitted a fix that should properly reorient the image when it is loaded using the DICOM browser. It will be probably integrated within a couple of days:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7858">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7858" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7858" target="_blank" rel="noopener">BUG: Force loading images from DICOM using right-handed coordinate system</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:dicom-read-right-handed-ijk</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-07-18" data-time="16:48:14" data-timezone="UTC">04:48PM - 18 Jul 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 3 files with 21 additions and 7 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7858/files" target="_blank" rel="noopener">
            <span class="added">+21</span>
            <span class="removed">-7</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Automatically flip left handed volumes when loading into 3D Slicer from DICOM to<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7858" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> make them compatible with all algorithms. Fixes flipped normals in segmentation node for left handed volumes.

Renamed FlipIJKCoordinateSystemHandedness method to ReverseSliceOrder to make it explicit that flipping of handedness is achieved by reversing slice order. The method was introduced recently (no Slicer Stable Release has been created since then), therefore the old name was not deprecated but removed.

See related commit that applies this regularization when the image is read using volume storage node: https://github.com/Slicer/Slicer/commit/3802d812b1a5d855399d8a19cea0bd1705715d52

See discussion at https://discourse.slicer.org/t/dentalsegmentator-result-mesh-is-inverted/37408/9</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #21 by @Romulo_Alfaro (2024-07-19 01:04 UTC)

<p>Is true. I just opened it by force loading using the legacy image reader and this time the orientation was correct. Only that Segmentation had some flaws.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19f28b0bf63e1a48e0df90697b0469743cc71219.jpeg" data-download-href="/uploads/short-url/3HxA9j0MDh6N5gAq4ThxKsxAQo9.jpeg?dl=1" title="Captura de pantalla 2024-07-18 a la(s) 8.05.33 p. m." rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19f28b0bf63e1a48e0df90697b0469743cc71219_2_367x499.jpeg" alt="Captura de pantalla 2024-07-18 a la(s) 8.05.33 p. m." data-base62-sha1="3HxA9j0MDh6N5gAq4ThxKsxAQo9" width="367" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19f28b0bf63e1a48e0df90697b0469743cc71219_2_367x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19f28b0bf63e1a48e0df90697b0469743cc71219_2_550x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19f28b0bf63e1a48e0df90697b0469743cc71219_2_734x998.jpeg 2x" data-dominant-color="B9AD94"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-07-18 a la(s) 8.05.33 p. m.</span><span class="informations">852×1160 95.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
