# problem of importing .ply files

**Topic ID**: 21972
**Date**: 2022-02-15
**URL**: https://discourse.slicer.org/t/problem-of-importing-ply-files/21972

---

## Post #1 by @J_Jang (2022-02-15 03:26 UTC)

<p>Hello. My name is Jang.</p>
<p>Recently, I used the 3D slicer and Auto3dgm with 3D images of the human teeth.<br>
3D images are laser-scanned 3D images and the file format is ply and stl.<br>
I tried to import the ply file (I clicked the Load Data button on the toolbar) and waited about 10 minutes.<br>
However, the 3D images did not pop up on the 3D slicer program as well as Auto3dgm.</p>
<p>Moreover, I downloaded example data from the 3D slicer (<a href="https://toothandclaw.github.io/how-to-use/" class="inline-onebox" rel="noopener nofollow ugc">How to use - Slicer Auto3dgm</a>), and loaded the ply file of the example data.<br>
Any 3D images were not imported.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4c4665d6a358700fac6088471d4dbaef87b758c.png" data-download-href="/uploads/short-url/nvB5zEhgSTlMtM9oPkLISAFpHl2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a4c4665d6a358700fac6088471d4dbaef87b758c_2_690x476.png" alt="image" data-base62-sha1="nvB5zEhgSTlMtM9oPkLISAFpHl2" width="690" height="476" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a4c4665d6a358700fac6088471d4dbaef87b758c_2_690x476.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a4c4665d6a358700fac6088471d4dbaef87b758c_2_1035x714.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4c4665d6a358700fac6088471d4dbaef87b758c.png 2x" data-dominant-color="2D2D39"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1305×902 12.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>When I loaded the DICOM file a year ago, the software worked well.<br>
I am very confused…And I do not know what I should do to import the ply file.<br>
Please somebody help me <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>
<p>I re-downloaded the software, but the ply file wasn’t still imported.<br>
The slicer version is 3D slicer 4.11.20210226.</p>

---

## Post #2 by @muratmaga (2022-02-15 05:23 UTC)

<p>I have successfully loaded the sample data from auto3dgm into Slicer (see screenshot below). A common issue with these models is that the physical scale is unknown and/or reported incorrectly. Clearly these teeth are not only a few micron long, but that’s what the units are reported in. So you have the hit the “center FOV” button (red highlight) and zoom in quite a while for the models to be visible.</p>
<p>I suspect your data suffer from a similar problem. There is no special way to load PLY files, you can drag and drop them, and they will be listed in the Data module, if they are loaded (even though they may not be visible initially like this case). If there is indeed an error, you can hit CTRL+0 to open the application log and see what the error is.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b71d7048b70257fb1f58160c234ad9ebbfae0987.png" data-download-href="/uploads/short-url/q7UrQ2zoyybTrK4qWSExRvAMZNl.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b71d7048b70257fb1f58160c234ad9ebbfae0987_2_690x384.png" alt="image" data-base62-sha1="q7UrQ2zoyybTrK4qWSExRvAMZNl" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b71d7048b70257fb1f58160c234ad9ebbfae0987_2_690x384.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b71d7048b70257fb1f58160c234ad9ebbfae0987_2_1035x576.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b71d7048b70257fb1f58160c234ad9ebbfae0987_2_1380x768.png 2x" data-dominant-color="BDC0C3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2121×1181 508 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @J_Jang (2022-02-15 14:19 UTC)

<p>Ah!!! Thank you for your help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
I could load the tooth image in the 3D slicer.<br>
If you don’t mind, can I ask one more thing?<br>
Although I could load it in the 3D slicer, the ply file has not appeared in the Auto3dgm mode.<br>
I downloaded Auto3dgm via the extensions and I put the mosek file in the appropriate place (under lib file).<br>
I set the input path and output path. Then I clicked the load button, but no images were loaded.<br>
This is the example image from the 3D slicer (<a href="https://toothandclaw.github.io/how-to-use/" class="inline-onebox" rel="noopener nofollow ugc">How to use - Slicer Auto3dgm</a>)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/219ebd5b3bd7f96eade66cfe6d6dc17621f9c22d.jpeg" data-download-href="/uploads/short-url/4NpQZuuib8ALiOm2q8XRu4tjaGx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/219ebd5b3bd7f96eade66cfe6d6dc17621f9c22d_2_689x445.jpeg" alt="image" data-base62-sha1="4NpQZuuib8ALiOm2q8XRu4tjaGx" width="689" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/219ebd5b3bd7f96eade66cfe6d6dc17621f9c22d_2_689x445.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/219ebd5b3bd7f96eade66cfe6d6dc17621f9c22d_2_1033x667.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/219ebd5b3bd7f96eade66cfe6d6dc17621f9c22d.jpeg 2x" data-dominant-color="B9BAD4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1237×798 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And this one is mine.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86a52c195e084ff84b3ee924590550270ee775f7.png" data-download-href="/uploads/short-url/jd7RnBxIVT9TCHUPbbYKPUC7taL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86a52c195e084ff84b3ee924590550270ee775f7_2_690x342.png" alt="image" data-base62-sha1="jd7RnBxIVT9TCHUPbbYKPUC7taL" width="690" height="342" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86a52c195e084ff84b3ee924590550270ee775f7_2_690x342.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86a52c195e084ff84b3ee924590550270ee775f7_2_1035x513.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86a52c195e084ff84b3ee924590550270ee775f7_2_1380x684.png 2x" data-dominant-color="B8B9DF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1895×942 51 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried to click the center FOV button and zoom in to find the images, but there is nothing.<br>
Could you help me one moretime?</p>

---

## Post #4 by @muratmaga (2022-02-15 15:29 UTC)

<p>That image is after running the whole pipeline of auto3dgm. Did you set your input folders etc and run everything,?</p>

---

## Post #5 by @J_Jang (2022-02-15 15:38 UTC)

<p>Oh God… I thought an image would appear as soon as it was loaded and then an additional landmark would be created.<br>
I run the whole process, and I get the final images <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
I really appreciate your help<br>
You’re a lifesaver</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3690ae57f50fc7fbbffb4bd8a48fd956d14e8c1.png" data-download-href="/uploads/short-url/wrLrbosPoewIoCOrrItKUGfQkql.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3690ae57f50fc7fbbffb4bd8a48fd956d14e8c1_2_690x335.png" alt="image" data-base62-sha1="wrLrbosPoewIoCOrrItKUGfQkql" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3690ae57f50fc7fbbffb4bd8a48fd956d14e8c1_2_690x335.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3690ae57f50fc7fbbffb4bd8a48fd956d14e8c1_2_1035x502.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3690ae57f50fc7fbbffb4bd8a48fd956d14e8c1_2_1380x670.png 2x" data-dominant-color="BAB9D2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1908×929 194 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
