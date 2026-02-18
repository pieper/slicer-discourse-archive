# Problem importing a Volumen With a Phillips affinity 50

**Topic ID**: 5065
**Date**: 2018-12-13
**URL**: https://discourse.slicer.org/t/problem-importing-a-volumen-with-a-phillips-affinity-50/5065

---

## Post #1 by @Rodolfo_Antonio_Gurr (2018-12-13 00:26 UTC)

<p>Hi. I’ve been practicing with the 3dSlicer and My 3d ultrasound volumes. I have a phillips Affinity 50 but I’m having a problem when I import the dicom volume into the program, the sagital and coronal images seems smaller in the FOV dimensions not like the axial volume.<br>
That happens in the 3d slicer because in the ultrasound machine seems the same size.<br>
Any ideas?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21828a79c5e09ad062492797869f079a7fbc0c51.jpeg" data-download-href="/uploads/short-url/4Mrre7uonCfb0amVX4HxSPHTc2d.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21828a79c5e09ad062492797869f079a7fbc0c51_2_690x387.jpeg" alt="image" data-base62-sha1="4Mrre7uonCfb0amVX4HxSPHTc2d" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21828a79c5e09ad062492797869f079a7fbc0c51_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21828a79c5e09ad062492797869f079a7fbc0c51_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21828a79c5e09ad062492797869f079a7fbc0c51_2_1380x774.jpeg 2x" data-dominant-color="75787B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1077 305 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2018-12-13 00:30 UTC)

<p>How did you import the image? Did you install SlicerHeart extension? Did you use the DICOM module to import and load the image? Are there any warnings or errors in the application log?</p>

---

## Post #3 by @Rodolfo_Antonio_Gurr (2018-12-13 00:58 UTC)

<p>I used this…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e5dbae4773b80219c53f4ea44de71f32643a1ab.png" data-download-href="/uploads/short-url/6CaMjNpFJWAUAyZalKuaEvx5vh9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e5dbae4773b80219c53f4ea44de71f32643a1ab_2_690x388.png" alt="image" data-base62-sha1="6CaMjNpFJWAUAyZalKuaEvx5vh9" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e5dbae4773b80219c53f4ea44de71f32643a1ab_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e5dbae4773b80219c53f4ea44de71f32643a1ab_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e5dbae4773b80219c53f4ea44de71f32643a1ab_2_1380x776.png 2x" data-dominant-color="A4A4AB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 197 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I already installed the SlicerHeart extensions. I think that I used the DICOM module to import and load the image. And I didn’t get any warnings or errors.</p>
<p>Here is the DICOM file of the volume.</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1C9V569EYgiqe209opeiUdz-gUQKFgVtN/view?usp=drive_open">
  <header class="source">

      <a href="https://drive.google.com/file/d/1C9V569EYgiqe209opeiUdz-gUQKFgVtN/view?usp=drive_open" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1C9V569EYgiqe209opeiUdz-gUQKFgVtN/view?usp=drive_open" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1C9V569EYgiqe209opeiUdz-gUQKFgVtN/view?usp=drive_open" target="_blank" rel="noopener nofollow ugc">IM_0013</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2018-12-13 21:32 UTC)

<p>Thank you for sharing the image. I’ve found the root cause of the issue (slice spacing is not stored in public DICOM fields but only in private ones) and update SlicerHeart module to be able to load the images with correct spacing.</p>
<p>Reinstall SlicerHeart extension tomorrow or later to get the updated version. When you import the data, drag-and-drop the folder that contains the file (not the file) to Slicer and choose DICOM import. Then load the data set from the DICOM browser.</p>
<p>Load the data using DICOM browser:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/540c93a5730d5a7986f3a30a46ede54c5834008d.png" data-download-href="/uploads/short-url/bZx3hZ6PZqbkZlF6pomMsdA0Aqh.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/540c93a5730d5a7986f3a30a46ede54c5834008d_2_690x472.png" alt="image" data-base62-sha1="bZx3hZ6PZqbkZlF6pomMsdA0Aqh" width="690" height="472" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/540c93a5730d5a7986f3a30a46ede54c5834008d_2_690x472.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/540c93a5730d5a7986f3a30a46ede54c5834008d_2_1035x708.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/540c93a5730d5a7986f3a30a46ede54c5834008d.png 2x" data-dominant-color="E0E5EA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1213×831 78.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Volume rendered result (image is not distorted anymore):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e1dc598bd74fb1e98c4022b4b6b587471852631.jpeg" data-download-href="/uploads/short-url/b931LZJID2U1OttD3Zs3Bj9D5ux.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e1dc598bd74fb1e98c4022b4b6b587471852631_2_690x449.jpeg" alt="image" data-base62-sha1="b931LZJID2U1OttD3Zs3Bj9D5ux" width="690" height="449" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e1dc598bd74fb1e98c4022b4b6b587471852631_2_690x449.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e1dc598bd74fb1e98c4022b4b6b587471852631_2_1035x673.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e1dc598bd74fb1e98c4022b4b6b587471852631.jpeg 2x" data-dominant-color="A09BA9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1210×788 220 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Rodolfo_Antonio_Gurr (2018-12-15 21:08 UTC)

<p>I already reinstalled the SliceHeart and keeps happening the same thing.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7ea2920f8eea538b3c52459b0145619b5d8cc109.jpeg" data-download-href="/uploads/short-url/i4gsXqF5PnLUPNZNcpTkpY0zW1X.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ea2920f8eea538b3c52459b0145619b5d8cc109_2_690x388.jpeg" alt="image" data-base62-sha1="i4gsXqF5PnLUPNZNcpTkpY0zW1X" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ea2920f8eea538b3c52459b0145619b5d8cc109_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ea2920f8eea538b3c52459b0145619b5d8cc109_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ea2920f8eea538b3c52459b0145619b5d8cc109_2_1380x776.jpeg 2x" data-dominant-color="84808B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 399 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>When I’m trying to load the volume in the DICOM browser it says this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8243286d382a3f7514ea3387ac9f60beebb1d6cb.png" data-download-href="/uploads/short-url/iAlXi8sh0YgZVL7OhSZJX6zwsjh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8243286d382a3f7514ea3387ac9f60beebb1d6cb_2_690x388.png" alt="image" data-base62-sha1="iAlXi8sh0YgZVL7OhSZJX6zwsjh" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8243286d382a3f7514ea3387ac9f60beebb1d6cb_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8243286d382a3f7514ea3387ac9f60beebb1d6cb_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8243286d382a3f7514ea3387ac9f60beebb1d6cb_2_1380x776.png 2x" data-dominant-color="C4C6CA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1917×1079 345 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks in advance…</p>

---

## Post #6 by @lassoan (2018-12-16 01:06 UTC)

<p>SlicerHeart did not get built for Windows last night (see <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerHeart" rel="nofollow noopener">dashboard</a>), maybe due to moving of Kitware’s headquarter. Hopefully the build will be completed tomorrow. If there is no SlicerHeart update in a few days then let us know and we’ll investigate.</p>

---

## Post #7 by @Rodolfo_Antonio_Gurr (2018-12-17 09:36 UTC)

<p>lassoan thanks a lot. I had to install linux in another partition to do this but finally worked!! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> I’ll keep you posted I have some projects to do some simulators for fetal surgery training.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1dca68acc0c6ebef3b78496e3e331d299ec9b3f4.jpeg" data-download-href="/uploads/short-url/4fxvlQ0kcAde4xOA0ZGY8I9qz8U.jpeg?dl=1" title="Captura%20de%20pantalla%20de%202018-12-17%2002-35-24" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dca68acc0c6ebef3b78496e3e331d299ec9b3f4_2_690x388.jpeg" alt="Captura%20de%20pantalla%20de%202018-12-17%2002-35-24" data-base62-sha1="4fxvlQ0kcAde4xOA0ZGY8I9qz8U" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dca68acc0c6ebef3b78496e3e331d299ec9b3f4_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dca68acc0c6ebef3b78496e3e331d299ec9b3f4_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dca68acc0c6ebef3b78496e3e331d299ec9b3f4_2_1380x776.jpeg 2x" data-dominant-color="8D888E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura%20de%20pantalla%20de%202018-12-17%2002-35-24</span><span class="informations">1920×1080 473 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks again <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #8 by @Florin (2018-12-19 13:10 UTC)

<p>Hi Antonio,</p>
<p>I can’t get the 3D volume file out of my affinity 50. On DICOM-Export only the pictures and videos are copied. The 3D files are simply ignored and not copied to USB stick.</p>
<p>Can you tell me how you do it?</p>
<p>Thanks a lot!</p>

---

## Post #9 by @Florin (2018-12-19 13:27 UTC)

<p>I found it. The check mark in the settings was not set for 3D export.</p>

---

## Post #10 by @emanuel_ozcoidi (2024-01-12 00:47 UTC)

<p>Hello, I have a question, to export the images from the Philips Affinity do I have to configure something special? greetings</p>
<details>
<summary>
Original in Spanish</summary>
<p>hola , tengo una duda, para exportar las imagenes desde el Philips Affinity hay que configurar algo en especial? saludos</p>
</details>

---

## Post #11 by @lassoan (2024-01-12 04:22 UTC)

<p>This question has been already asked here:</p>
<aside class="quote quote-modified" data-post="1" data-topic="33744">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/emanuel_ozcoidi/48/67018_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/import-3d-images-from-philips-affinity-70/33744">Import 3D images from Philips Affinity 70</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Translated by Google Translate: 

Help, please! When following the recommended sequence for loading 3D ultrasounds into slicer, I get the following banner “Warnings detected during load.  Examine data in Advanced mode for details.  Load anyway?” with the detail of 1: US [50] [Image sequence]: Image spacing may need to be calibrated for accurate size measurements. How can I fix this error? Could it be the problem that I’m exporting the files from the Philips Affinity 70 and not from the QLAB? BES…
  </blockquote>
</aside>

<p><a class="mention" href="/u/emanuel_ozcoidi">@emanuel_ozcoidi</a> Ii would like to ask two things for the future for making your participation on this forum a bit moreefficient for everyone:</p>
<ul>
<li>Please avoid posting the same question to multiple places. It increases the work for people to answer it and you may even start parallel discussions, which lead to even more wasted efforts. If you wanted to hear from specific people then you can <span class="mention">@mention</span> them in your post.</li>
<li>If you are not confident in writing in English then please take the time to copy your native language text to Google Translate (or any of the freely available automated translation services) and paste the translated text into your forum post. You can also add your original text as a reference, using the “Hide Details” feature of the Discourse text editor to make the text hidden by default. It takes 1-2 minutes for you to do this and with that you save 1 minute for every reader of your post.</li>
</ul>

---
