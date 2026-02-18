# Geodesic Slicer

**Topic ID**: 17071
**Date**: 2021-04-13
**URL**: https://discourse.slicer.org/t/geodesic-slicer/17071

---

## Post #1 by @Antonio_Giulio_Genna (2021-04-13 18:25 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11.20210226<br>
Expected behavior: Extract mesh<br>
Actual behavior: Create a mesh of the whole volume and not of the patient</p>
<p>Dear Support Team,</p>
<p>I recently approached the Geodesic Slicer extension. Its usage seems really straightforward. However, after loading the volume and clicking on “Create a mesh” the output diverges from the expected (please see the file attached). It should create a mesh outlining the patient’s head, but it generated a mesh of the entire volume, forming a rectangle.</p>
<p>Could you please help me solve this problem?</p>
<p><a href="/uploads/short-url/zII4rlWdirtZPqMiFeJCaOK0euT.jpeg">problems|592x500</a></p>

---

## Post #2 by @lassoan (2021-04-14 04:26 UTC)

<p>If you don’t get an answer here in a few days then I would recommend to contact the authors in email and ask them to answer the question here. If they help you in email then update this topic with what you have learned.</p>

---

## Post #3 by @Frederic (2021-04-14 08:12 UTC)

<p>Hi <a class="mention" href="/u/antonio_giulio_genna">@Antonio_Giulio_Genna</a>, and thanks for the feedback.<br>
No worries <a class="mention" href="/u/lassoan">@lassoan</a>, I am still here <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"> .</p>
<ol>
<li>It works well on my slicer version: 4.11.20200903 . You can find this previous one <a href="https://slicer.kitware.com/midas3/folder/274" rel="noopener nofollow ugc">here</a>.</li>
<li>With your version (4.11.20210226), after a try, it works like a charm too.</li>
</ol>
<p>Perhaps it is due to the intensity of your image. Could you try the extension with the example on my github (<a href="https://github.com/FredericBr/SlicerGeodesic/tree/master/Example_template" rel="noopener nofollow ugc">here</a>) please?</p>
<p>Looking forward to your reply,</p>
<p>Fred</p>

---

## Post #4 by @Antonio_Giulio_Genna (2021-04-14 16:11 UTC)

<p>Dear Fred,</p>
<p>Thank you for replying to me. Today, I have not been able to test the extension with your example. I will do it tomorrow and inform you whether it works or not.</p>
<p>Since it could also be related to intensity issue, how can I solve the latter?</p>
<p>Looking forward to your reply,</p>
<p>Antonio</p>

---

## Post #5 by @Antonio_Giulio_Genna (2021-04-15 10:12 UTC)

<p>Dear Fred,</p>
<p>As you suggested I used the template and everything went smoothly. Also, I loaded both my image and the template in the Volume rendering module and the two 3D recostruction were completely different. The template 3D reconstruction easily displayed the patient’s face, while my image the face is hidden by the background. I think, this confirms it is an intensity issue. Do you have any advice or tutorial to solve it without cropping the image’s volume?</p>
<p>All the best,</p>
<p>Antonio</p>

---

## Post #6 by @Frederic (2021-04-15 14:36 UTC)

<p>Hi <a class="mention" href="/u/antonio_giulio_genna">@Antonio_Giulio_Genna</a><br>
This is a good news, the bug is thus due to your file and not my software <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=9" title=":sweat_smile:" class="emoji" alt=":sweat_smile:">.<br>
Several way exist to change the intensity of your image, but one seems to be approved in Slicer itself (<a href="https://discourse.slicer.org/t/is-it-possible-to-rescale-intensity-of-a-volume/2543">here, solution by HamburgerFinger</a>). Could you try it?<br>
Best,<br>
Fred</p>

---

## Post #7 by @Antonio_Giulio_Genna (2021-04-16 21:40 UTC)

<p>Dear Fred,</p>
<p>Thank you for aiding me. I finally manage to complete the analysis. However, compared to your template, my image still has minor distortion, mainly due to inadequate intensity thresholding. Anyhow, what bothers me most is the 3D mesh output is colored in green. On the contrary, with your template, the final output is skin-colored. Does it mean the mesh creation is not 100% completed?</p>
<p>All the best,<br>
Antonio</p>

---

## Post #8 by @Frederic (2021-04-17 09:35 UTC)

<p>Hi <a class="mention" href="/u/antonio_giulio_genna">@Antonio_Giulio_Genna</a></p>
<p>You are welcome!<br>
When you go in the Data module (cf. image), do you have the same thing as me?<br>
The green color correspond to the “skin segmentation”, but the most important thing is the file stored after the mesh generation (for me: "moi.nii-&gt; create a mesh → moi.nii.stl), after you can change the color of this stl object in the Data module (skin-colored or other).</p>
<p>Best,<br>
Fred</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2cc14e62c66bcce8bbe2c5ae587fdf9fbda7bca0.jpeg" data-download-href="/uploads/short-url/6nVafsqOIENSXF958bNLHlIVck0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2cc14e62c66bcce8bbe2c5ae587fdf9fbda7bca0_2_690x388.jpeg" alt="image" data-base62-sha1="6nVafsqOIENSXF958bNLHlIVck0" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2cc14e62c66bcce8bbe2c5ae587fdf9fbda7bca0_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2cc14e62c66bcce8bbe2c5ae587fdf9fbda7bca0_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2cc14e62c66bcce8bbe2c5ae587fdf9fbda7bca0_2_1380x776.jpeg 2x" data-dominant-color="4E4F59"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 306 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @Antonio_Giulio_Genna (2021-04-22 13:54 UTC)

<p>Dear Fred,</p>
<p>I am sorry for my late reply, but I had some problems related to the project I had to solve. Yes the data module shows me the same thing as you so I will change the skin colour using this tool.</p>
<p>Thank you so much and sorry for dealing with such a unexperienced user.</p>
<p>All the best,</p>
<p>Antonio</p>

---

## Post #10 by @Frederic (2021-04-22 14:42 UTC)

<p>No worries Antonio!<br>
Feel free to accept one of my post as solution.</p>
<p>Best,<br>
Fred</p>

---
