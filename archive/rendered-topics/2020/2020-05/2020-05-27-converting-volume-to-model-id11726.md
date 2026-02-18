# Converting "Volume" to "Model"

**Topic ID**: 11726
**Date**: 2020-05-27
**URL**: https://discourse.slicer.org/t/converting-volume-to-model/11726

---

## Post #1 by @Joao_L (2020-05-27 00:27 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.5, 4.10 and 4.11<br>
Hello. Is it possible to convert a radiography (volume file) to a model file using Slicer?</p>

---

## Post #2 by @lassoan (2020-05-27 00:28 UTC)

<p>Yes, you can do that by <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">segmenting the volume</a>. It can be as simple as defining a threshold value.</p>

---

## Post #3 by @Joao_L (2020-05-27 19:00 UTC)

<p>Even a radiography (2D image with one cut only)? I don’t want to transform it in 3D, of course. But I would like to load it into the “blue camp” so I can mark points e calculate angles.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d280e78504d5a7bc84d65a3d61629b9ab412bf5.png" data-download-href="/uploads/short-url/hRbvhleKOcTqAnN8YNYI3hd5xWt.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d280e78504d5a7bc84d65a3d61629b9ab412bf5_2_690x485.png" alt="Capture" data-base62-sha1="hRbvhleKOcTqAnN8YNYI3hd5xWt" width="690" height="485" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d280e78504d5a7bc84d65a3d61629b9ab412bf5_2_690x485.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d280e78504d5a7bc84d65a3d61629b9ab412bf5_2_1035x727.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d280e78504d5a7bc84d65a3d61629b9ab412bf5.png 2x" data-dominant-color="5F6077"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1058×745 88.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2020-05-27 19:21 UTC)

<p>You can choose to show a slice view in 3D (by clicking the “eye” icon in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">slice view controller</a>).</p>
<p>But this should not be necessary, as you can mark points and measure angle directly in the slice view, too.</p>

---

## Post #5 by @Joao_L (2020-05-27 19:42 UTC)

<p>When clicking the “eye”, I see this black square, not the radiographic image. And in the slice view controller it would be difficult to mark points because it is small and we are working with teeths.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3ed0e668e9991fbbeb1b572c204b19f856318c0.png" data-download-href="/uploads/short-url/wwkh8KCrBZS4PesA9vIq7wiS5Da.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3ed0e668e9991fbbeb1b572c204b19f856318c0_2_690x494.png" alt="image" data-base62-sha1="wwkh8KCrBZS4PesA9vIq7wiS5Da" width="690" height="494" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3ed0e668e9991fbbeb1b572c204b19f856318c0_2_690x494.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3ed0e668e9991fbbeb1b572c204b19f856318c0_2_1035x741.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3ed0e668e9991fbbeb1b572c204b19f856318c0.png 2x" data-dominant-color="56566E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1036×742 84.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2020-05-27 20:07 UTC)

<p>Make sure you click the eye icon of the red slice and you look at the red slice in the 3D view.</p>
<p>In the screenshot above, you visualize an axial slice. Red slice is sagittal, so you need to rotate the 3D view a bit to see it.</p>

---

## Post #7 by @Joao_L (2020-05-27 20:32 UTC)

<p>Yes, it is the eye of the red slice. And the 3D view was rotated as well.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e48a830628ab932ced7a0b8362e00a45e3a8b85e.png" data-download-href="/uploads/short-url/wBLCEybJP8caheaoOhDHozwoPOm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e48a830628ab932ced7a0b8362e00a45e3a8b85e_2_690x326.png" alt="image" data-base62-sha1="wBLCEybJP8caheaoOhDHozwoPOm" width="690" height="326" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e48a830628ab932ced7a0b8362e00a45e3a8b85e_2_690x326.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e48a830628ab932ced7a0b8362e00a45e3a8b85e_2_1035x489.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e48a830628ab932ced7a0b8362e00a45e3a8b85e_2_1380x652.png 2x" data-dominant-color="8E8E9E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1599×756 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2020-05-27 23:55 UTC)

<p>Thank you, I was able to reproduce the issue with a color (RGB) image. This is a bug that we’ll fix soon - you can track the progress here:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/4939" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4939" target="_blank">Slice view of RGB volume does not appear in 3D view</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-05-27" data-time="23:53:36" data-timezone="UTC">11:53PM - 27 May 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank">
          <img alt="lassoan" src="https://avatars0.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">Load an RGB image, click "eye" icon in slice view controller to show the slice in 3D view. The image is...</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:bug</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Did converted the original DICOM image with some software to TIFF or PNG and loaded that?</p>
<p>You may avoid this problem if you load the DICOM image directly in Slicer. Or, as a workaround, if you only have an RGB image then you can convert the image to scalar image using “Vector to scalar volume” module.</p>

---

## Post #9 by @Joao_L (2020-05-28 16:58 UTC)

<p>Actually, what we need to do from the radiography is measuring angles using “Q3DC Extension”, wich only accepts models. For this, we would mark points through “surface registration”, but it only accepts models as well. In theory, it would be necessary to transform volume in model, but when I tried it, none of the tools recognized the radiography as a model.</p>
<p>Is there a way to mark points and measure angles directly from volume or from the model generated from volume - using another extension maybe?</p>
<p>By the way, I haven’t tried using “vector to scalar volume” yet. It worked - after converting the image to scalar using “vector to scalar volume” I got the image in 3D view.</p>

---

## Post #10 by @lassoan (2020-05-28 17:35 UTC)

<p><a class="mention" href="/u/james_hoctor">@James_Hoctor</a> can you advise?</p>

---

## Post #11 by @James_Hoctor (2020-05-28 18:21 UTC)

<p>Thanks for the mention <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p><a class="mention" href="/u/joao_l">@Joao_L</a>, I would discourage use of Q3DC here. The markups module contains an angle measuring tool that may be more appropriate. You can click on the red slice view to place the parts of the angle markup.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df14ceadbf6204e74d9826f80c7c82dd35355d8f.png" alt="Screenshot from 2020-05-28 14-15-46" data-base62-sha1="vPt3r3XGOQt21fSBTGEoCTzlRYb" width="656" height="359"></p>
<p>the Q3DC module is not really designed for this, you can try the following: Add fiducial points to your scene using the markups module, and click directly on the red slice view where you want to place them.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0361f7ba8965cf7d92bd15aef3cd648e91e2fe80.png" alt="Screenshot from 2020-05-28 13-53-27" data-base62-sha1="tVkhPwqjfEWZ6APAWGyH4lTzS8" width="656" height="344"></p>
<p>Now add any model to your scene. It doesn’t matter what you pick, so you can hide it in order to see the other scene elements. In Q3DC, select that model and uncheck the “On Surface” box as shown below.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83a12367021a52914375780a25cdf87553630679.png" alt="Screenshot from 2020-05-28 14-01-30" data-base62-sha1="iMrMIHSvwPZsfxIP2AIiNJfHKmR" width="656" height="461"></p>
<p>Use the “Connected Landmarks” drop-down menus to select each of your markups in turn, then use the “Calculate angle between two lines” functionality of Q3DC as normal. Be aware that Q3DC calculates roll, pitch, and yaw, not angle. For your use case, two of these numbers should be zero.</p>

---

## Post #12 by @Joao_L (2020-05-28 18:40 UTC)

<p>Thank you very much for your explication.<br>
Just to know if I got it: you gave me two options - 1) using the angle measuring tool or 2) using Q3DC (adding a model to the scene). Right?</p>

---

## Post #13 by @James_Hoctor (2020-06-04 12:32 UTC)

<p>Yes, that’s exactly it. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---
