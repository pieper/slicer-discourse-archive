# Creating a module for electron bolus

**Topic ID**: 37766
**Date**: 2024-08-08
**URL**: https://discourse.slicer.org/t/creating-a-module-for-electron-bolus/37766

---

## Post #1 by @sima (2024-08-08 08:49 UTC)

<p>Hi professors</p>
<p>I manually designed individual electron bolus using 3D slicer software for my thesis a year ago.</p>
<p>Now I have written Python codes to have electron bolus in 3D slicer automatically. and I am eager to add these codes as a module in the <strong>SlicerRT extension</strong>. I should add that note in writing these codes, I have used the SlicerSkinMouldGenerator module codes as recommended by Professor Lasso.</p>
<p>Unfortunately, I don’t have any experience with modules, and GUI development.</p>
<p>I hope developers and experts can help me convert these codes into a usable module</p>
<p>This module will be able to design a bolus on the top of the skin to match a desired isodose level to the distal surface of the PTV. So we can spare more normal tissue.</p>
<p>In the following, I will give a summary of the function of my Python scripted codes:</p>
<ul>
<li>
<p>First I import the CT, RT structure (skin and ptv), RT Plan and RT dose.</p>
</li>
<li>
<p>The desired isodose model is made using the isodose module in the SlicerRT extension.</p>
</li>
<li>
<p>The RT plan metadata is accessed to obtain the <em>isocenter</em> and <em>gantry</em> angle for marking the source.</p>
</li>
<li>
<p>The points of the PTV are separated in each slice, and the source above each slice (<em>Source_coordinate_m</em>) is considered.</p>
</li>
<li>
<p>The farthest point of the PTV on each side (R-L coordinate) from its center is found, and a margin is applied to account for the length of bolus in each slice (mL &amp; mR).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03dc123d425ba03ca880088d87cd4bc767dd6790.png" alt="image" data-base62-sha1="y8VQ0nNI3VRBoRFJH5Gu8AjkgU" width="624" height="318"></p>
</li>
<li>
<p>The mL and mR points are connected to Source_coordinate_m to form two lines, and then angle between two lines is found<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac77e89b2661cfb4b1a113ad2f913b9df336ad44.png" alt="image" data-base62-sha1="oBJ1Jq7yuuCjljByo5HGOyRloZS" width="623" height="418"></p>
</li>
<li>
<p>The angle is divided into small angles with a step of 0.1 degree.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/959a5551053fb2df8e1a0c8e4456b84f1f005250.png" alt="image" data-base62-sha1="llrNDuPcQWr9QLzP7n1xLW0IDcI" width="384" height="259"></p>
</li>
<li>
<p>In each step, consideration is given to the line passing through the <em>skin</em>, <em>PTV</em>, and <em>isodose</em>.</p>
</li>
<li>
<p>putting a dot above the skin along the line equal to the distance of the intersection of the line with ptv and isodose. These dots are the border of the bolus<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9b0182506aae7b83d1251108354293d6279631f.jpeg" alt="image" data-base62-sha1="od7YjzZtJXEwtNkV3FEVRXm0e0D" width="624" height="371"></p>
</li>
<li>
<p>Dots are converted into poly data and then transformed into image data.</p>
</li>
<li>
<p>The image data from each slice is merged into one labelmap volume</p>
</li>
<li>
<p>Now I have a bolus with labelmap volume format<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7601b43864c2e63f17c07819dc0e0fe97b3bb1fc.jpeg" data-download-href="/uploads/short-url/gPVZwljL1RW0IuLIymluoc8oVMU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7601b43864c2e63f17c07819dc0e0fe97b3bb1fc.jpeg" alt="image" data-base62-sha1="gPVZwljL1RW0IuLIymluoc8oVMU" width="690" height="289" data-dominant-color="8E8B8C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">719×302 41.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>I can convert it to a segment or model by using 3d slicer’s capabilities.</p>
</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1fa1930fe207e5f9393c5b2f575d9e37c2c1a328.png" alt="image" data-base62-sha1="4vOYlfz7ndmJnRw5QDr2rQ4zdeE" width="506" height="304"></p>
<p>I checked the bolus in Isogray TPS. (you can see figures in <a href="https://drive.google.com/drive/folders/1xsUBrsGfH_dx6ig36cGzN2YpsJXr4iN0?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">file 1 - Google Drive</a>)<br>
Its performance was appropriate and desired isodose surface approached the distal surface of PTV. However, in some cases at the edge of the field, it may need further handling<br>
You can see other bolus designed for another PTV below and its performance in TPS in (<a href="https://drive.google.com/drive/folders/1c8FhGCGIgF6UvVHMzoMlXsLZqqK-UHua?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">file 2 - Google Drive</a>)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7f751eb87a827a5219947f71f4343bc82eb359d.png" alt="image" data-base62-sha1="nXTCkrv5j6AAucC5bheLvLPe89L" width="352" height="250"></p>
<p>.I think by these codes we can have an elementary shape of the electron bolus but it must be checked in TPS before using it<br>
I am eager to provide you with the code I have collected and hope you can help me convert this code into a usable module.<br>
I’m requesting help from developers and other experts to convert my codes into a usable module and integrate it into the SlicerRT extension. Additionally, I’m willing to provide the codes to anyone willing to assist me further in collaboration.</p>
<p>I eagerly await feedback and responses.</p>

---

## Post #2 by @cpinter (2024-08-08 10:40 UTC)

<p>Hi Sima,</p>
<p>Thanks a lot for the nice detailed description! It looks good to me, but I’d like to have a better understanding of certain parts (e.g. “The points of the PTV are separated in each slice, and the source above each slice (<em>Source_coordinate_m</em> ) is considered”).</p>
<p>In any case you say that you have some Python scripts for this. Are they available in any place? Not sure if you want to add them to a temporary GitHub repository. An alternative could be to create a Git jist for the scripts.</p>
<p>After being able to reproduce the steps and understanding the code, we can discuss making it a proper module. I am happy to help with this.</p>

---

## Post #3 by @sima (2024-08-10 08:44 UTC)

<p>Hello Dear Csaba</p>
<p>I am very pleased to see your message. I apologize for my delayed response; I was outside the city and had limited internet access.</p>
<p>I have uploaded the code to Gist for further review, and I provide the link here</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/simaaz/aebb31ba5060c58a97c51db1ccc1878b">
  <header class="source">

      <a href="https://gist.github.com/simaaz/aebb31ba5060c58a97c51db1ccc1878b" target="_blank" rel="noopener nofollow ugc">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/simaaz/aebb31ba5060c58a97c51db1ccc1878b" target="_blank" rel="noopener nofollow ugc">https://gist.github.com/simaaz/aebb31ba5060c58a97c51db1ccc1878b</a></h4>

  <h5>electron_bolus.py</h5>
  <pre><code class="Python">import numpy as np
import slicer
import math
import vtk
import pydicom


def calculate_distance(x, y, m, b):

    A = -m</code></pre>
   This file has been truncated. <a href="https://gist.github.com/simaaz/aebb31ba5060c58a97c51db1ccc1878b" target="_blank" rel="noopener nofollow ugc">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I have also uploaded the files I used to Google Drive</p>
<p><a href="https://drive.google.com/drive/folders/1aLHAig9APZxupwi0To-rrPZDxj2iEr9N?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1aLHAig9APZxupwi0To-rrPZDxj2iEr9N?usp=sharing</a></p>
<p>I would appreciate it if you could take a look at it whenever you have time</p>
<p>Please let me know if you need any further explanation on any part of it, and I’d be happy to explain</p>
<p>I eagerly await your feedback</p>
<p>thanks<br>
Sima</p>

---

## Post #4 by @cpinter (2024-08-12 10:44 UTC)

<p>Excellent, thank you! I think in order to get started with the module development it would be really useful to also have some kind of sketch of the user interface that the new module will have. Can you please provide such a sketch (drawing)?</p>
<p>Another thing to decide in the beginning is where this module will live. Can you confirm that you would like this to be part of the SlicerRT extension?</p>

---

## Post #5 by @sima (2024-08-13 09:10 UTC)

<p>Hi<br>
Thank you a lot for your answer<br>
If I have understood your intention correctly, considering the theme maintained across all modules in 3d slicer software, I can suggest the following image as a sketch of the user interface.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d52255f5adf705dc74fb87d9b2c7add5e12e3ebc.jpeg" alt="sketch" data-base62-sha1="uptgrItBpMiGueGuMPD3DcPkx3K" width="393" height="408"></p>
<p>In response to your second question, since the individual electron bolus is an accessory used in radiotherapy, my colleagues and I are very interested in integrating this work as a module within the <strong>SlicerRT extension</strong>.<br>
Additionally, there are many ongoing projects within our department at Mashhad University of Medical Sciences (such as DRR dosimetry) that, could also be included in the SlicerRT extension. I would be happy to discuss these projects with you in more detail in the future.</p>
<p>I am currently eagerly awaiting your feedback on the electron bolus module.</p>
<p>thanks</p>

---

## Post #6 by @cpinter (2024-08-13 09:16 UTC)

<p>This is excellent, thank you! This week is very busy for me, but I’ll try to get started as soon as possible.</p>
<p>Is there a reason you want the bolus as a labelmap volume and not a segment? Labelmaps cannot easily be displayed in 3D, and most of the computations regarding “labelmaps” are available for segmentation nodes in modern Slicer.</p>
<p>Same goes for PTV and Skin, for which I don’t see an obvious reason why we should convert them from segments to model nodes.</p>

---

## Post #7 by @sima (2024-08-13 15:12 UTC)

<p>Thank you very much. I will wait as long as you have the opportunity.<br>
Regarding your question, I must say that there is no specific reason; rather, the code guided me in this direction. As I mentioned initially, after obtaining the label map, I manually converted it to a segment and model by right-clicking it to view the output in 3D on the body. If you believe it would be better for the production to be in segment form, I would appreciate your assistance in modifying this part.</p>
<p>In my experience with Slicer, I found that modules typically work with models. Therefore, I started developing the code with the model and proceeded accordingly and I cannot currently predict what would happen to the code and its output if it were to work with segments instead.</p>
<p>I should also mention that I have been searching, assembling, and modifying codes step by step through research on Slicer Forum, GitHub, and other sources. Wherever you, with your expertise, see the need for improvements, I will gladly accept your suggestions.</p>

---

## Post #8 by @cpinter (2024-08-13 15:38 UTC)

<aside class="quote no-group" data-username="sima" data-post="7" data-topic="37766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sima/48/67638_2.png" class="avatar"> sima:</div>
<blockquote>
<p>In my experience with Slicer, I found that modules typically work with models</p>
</blockquote>
</aside>
<p>Well, in the past there were only models and labelmaps, so there might be a historic bias in the available modules. However, now that the segmentations are stored in segmentation nodes, also if loaded from RTSTRUCT, including the PTV and all other structures you need, it makes more sense to use that format than converting back and forth (this was the main motivation behind creating the segmentations infrastructure, to prevent the need for manual conversions).</p>
<p>I have one more request if you don’t mind. Since I cannot really judge the algorithmic correctness of your method, can you please describe the theory behind your solution (that you already explained in detail above)? I mean I know <em>what</em> you do, but I don’t know <em>why</em>. I asked this before but you may have not seen it:</p>
<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="37766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>It looks good to me, but I’d like to have a better understanding of certain parts (e.g. “The points of the PTV are separated in each slice, and the source above each slice (<em>Source_coordinate_m</em> ) is considered”).</p>
</blockquote>
</aside>
<p>Please do not restrain yourself to this one question but describe the different steps in your algorithm. We will make this part of the documentation, so this will be useful later as well. And it will allow me to create the module with more confidence in what it does. Thank you!</p>

---

## Post #9 by @sima (2024-08-14 09:52 UTC)

<p>Hi Csaba<br>
I saw your question about ‘Source_coordinate_m’ but assumed that when you saw the code, your question was answered. That’s why I didn’t explain further. Now I’ll try to provide a more detailed explanation.</p>
<p>We have a <strong>point</strong> source located 100 centimeters away from the skin.</p>
<p>The basis of my work is that I have performed the calculations in 2D instead of 3D. That is, I first obtained a bolus for each slice and finally merged the boluses of each slice to arrive at a 3D bolus.</p>
<p>To calculate the bolus for one slice, I set the third component of the source equal to the third component of that slice (in effect, I have moved the source to the top of the slice).</p>
<p>In radiotherapy, it is assumed that the radiation beams from the <strong>point source</strong> are parallel and strike the surface perpendicularly, especially when the source is located at a significant distance from the skin. When the source is assumed above each slice, the assumption of perpendicularity to the surface remains valid. This means that small changes in the source position should not result in significant errors in the distribution of the radiation dose. Therefore, it can be said that, in practice, these small movements of the source above each slice generally do not introduce significant errors.</p>
<p>In the calculations for each slice: each beam (with an accuracy of 0.1) from the source strikes the skin, PTV (Planning Target Volume), and isodose surface. The distance from the point of intersection to the PTV and the isodose surface is calculated, and a point is placed at the same distance in the same direction as the beam (this point is one of the bolus points in that slice). These calculations are performed for all beams considered in that slice, and the resulting points form the 2D bolus in that slice.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9ff450c56d92593cae78d33f3bcfc7e4afac71b.jpeg" data-download-href="/uploads/short-url/zFzNMHQTl7bZRT0mQonMlLS7WUr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9ff450c56d92593cae78d33f3bcfc7e4afac71b_2_690x393.jpeg" alt="image" data-base62-sha1="zFzNMHQTl7bZRT0mQonMlLS7WUr" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9ff450c56d92593cae78d33f3bcfc7e4afac71b_2_690x393.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9ff450c56d92593cae78d33f3bcfc7e4afac71b_2_1035x589.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9ff450c56d92593cae78d33f3bcfc7e4afac71b.jpeg 2x" data-dominant-color="786E6D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1322×754 38.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f9515c441f30707e2a269aab605ea8d14367334.jpeg" data-download-href="/uploads/short-url/bm18gDvqjChJ3jcBMPt8mqatSPa.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f9515c441f30707e2a269aab605ea8d14367334_2_690x381.jpeg" alt="image" data-base62-sha1="bm18gDvqjChJ3jcBMPt8mqatSPa" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f9515c441f30707e2a269aab605ea8d14367334_2_690x381.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f9515c441f30707e2a269aab605ea8d14367334_2_1035x571.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f9515c441f30707e2a269aab605ea8d14367334_2_1380x762.jpeg 2x" data-dominant-color="6B6C69"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1523×843 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/405dd7ba03c7f17c245a0bdcc0ea2274b0ec70a3.jpeg" data-download-href="/uploads/short-url/9bpC8ycsMvxi1KbF1Uh0R1TDQqL.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/405dd7ba03c7f17c245a0bdcc0ea2274b0ec70a3_2_690x378.jpeg" alt="image" data-base62-sha1="9bpC8ycsMvxi1KbF1Uh0R1TDQqL" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/405dd7ba03c7f17c245a0bdcc0ea2274b0ec70a3_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/405dd7ba03c7f17c245a0bdcc0ea2274b0ec70a3_2_1035x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/405dd7ba03c7f17c245a0bdcc0ea2274b0ec70a3_2_1380x756.jpeg 2x" data-dominant-color="6D6F6C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1536×842 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73693ec67e918b4ac71a95404f620187e150e16e.jpeg" data-download-href="/uploads/short-url/gsYoxZ0XbQM9Y6UKr5AbFw568yO.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73693ec67e918b4ac71a95404f620187e150e16e_2_690x355.jpeg" alt="image" data-base62-sha1="gsYoxZ0XbQM9Y6UKr5AbFw568yO" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73693ec67e918b4ac71a95404f620187e150e16e_2_690x355.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73693ec67e918b4ac71a95404f620187e150e16e_2_1035x532.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73693ec67e918b4ac71a95404f620187e150e16e_2_1380x710.jpeg 2x" data-dominant-color="6F6F6E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1549×799 32.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Finally, the images of each slice are merged, resulting in the formation of a 3D bolus.<br>
I acknowledge that my assumptions may have a few errors, especially at the edges of the field (Maybe) However, this approach can create an initial shape of the bolus, which can be checked in TPS and refined as needed before being used.<br>
I believe this method can serve as an initial version of the module, and in later versions, it can be further refined for improved performance.</p>

---

## Post #10 by @cpinter (2024-08-22 10:27 UTC)

<p>I and my colleague spent several hours in the past days analyzing the algorithm and the code, trying to run it etc. We have reached the conclusion that the algorithm is too fragile and inaccurate to be integrated in such a widely used toolkit as SlicerRT. It works with many assumptions, and based on our test runs it does not work perfectly either (e.g. the bolus does not reach all the way to the edge of the dose deposition area).</p>
<p>Please consider that most of the modules integrated into SlicerRT have a published article providing evidence that the algorithm under the module works as expected (validation). In contrast, this algorithm is in the prototype phase and needs serious rework. For example, the code uses many hardcoded values and looks into the DICOM files, instead of getting the information from Slicer (angles, SAD, file paths, node names, etc.). Only after making it usable without so many manual intervention can the work begin to validate it, which is necessary in order to publish it in a quasi standard RT toolkit.</p>
<p>Besides the concerns about accuracy and robustness, one problem of the algorithm is that it works in 2D, which poses limitations in its accuracy, and its performance as well (it runs very slow).</p>
<p>I am not a radiation physicist, but came up with a possible alternative that seems more robust, faster, and achievable with standard Slicer tools.</p>
<p>The idea is basically to treat every object in 3D and use simple operations to achieve the same result. Let’s consider the same scenario as you did.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef8b5c8051734001ca33b03b3671e0ceca1ce12b.jpeg" data-download-href="/uploads/short-url/yb6H8kEgmNlGenyQwjqZVjMDdEv.jpeg?dl=1" title="1"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef8b5c8051734001ca33b03b3671e0ceca1ce12b_2_627x500.jpeg" alt="1" data-base62-sha1="yb6H8kEgmNlGenyQwjqZVjMDdEv" width="627" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef8b5c8051734001ca33b03b3671e0ceca1ce12b_2_627x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef8b5c8051734001ca33b03b3671e0ceca1ce12b_2_940x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef8b5c8051734001ca33b03b3671e0ceca1ce12b_2_1254x1000.jpeg 2x" data-dominant-color="868971"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1321×1053 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What we need is to keep the distal part of the isodose volume. We could achieve this by subtracting the PTV from the isodose, and do this all the way towards the source until there is no change in the isodose. We could potentially use the extrusion filter in VTK but out of experience I know it does not work for closed surfaces such as in this case. Instead, like in another application where I needed to do the same thing, I translated successively copies of the PTV towards the source, and kept subtracting them from the isodose labelmap.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/435b32c6fc0967b8f90a383a49e5c8f9c118891b.jpeg" data-download-href="/uploads/short-url/9BRnGIDOyDNRyOmBt0M3LUCnYWT.jpeg?dl=1" title="2"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/435b32c6fc0967b8f90a383a49e5c8f9c118891b_2_690x377.jpeg" alt="2" data-base62-sha1="9BRnGIDOyDNRyOmBt0M3LUCnYWT" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/435b32c6fc0967b8f90a383a49e5c8f9c118891b_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/435b32c6fc0967b8f90a383a49e5c8f9c118891b_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/435b32c6fc0967b8f90a383a49e5c8f9c118891b_2_1380x754.jpeg 2x" data-dominant-color="A3A79A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1920×1051 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then we get this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e380d93cb9032cfeffc0b120a0d7da936dd34f0a.jpeg" data-download-href="/uploads/short-url/wsArrnKaaQxGbgekPU1VS6XJ6Xw.jpeg?dl=1" title="3"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e380d93cb9032cfeffc0b120a0d7da936dd34f0a_2_639x500.jpeg" alt="3" data-base62-sha1="wsArrnKaaQxGbgekPU1VS6XJ6Xw" width="639" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e380d93cb9032cfeffc0b120a0d7da936dd34f0a_2_639x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e380d93cb9032cfeffc0b120a0d7da936dd34f0a_2_958x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e380d93cb9032cfeffc0b120a0d7da936dd34f0a_2_1278x1000.jpeg 2x" data-dominant-color="828B85"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1314×1027 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My question is: can this be usable as the bolus already?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8baa3d5f4a89c84e631b57531a60090b9134fda3.jpeg" data-download-href="/uploads/short-url/jVx6wWd4Ad51b9k3ufRQlQWDInV.jpeg?dl=1" title="5"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8baa3d5f4a89c84e631b57531a60090b9134fda3_2_672x500.jpeg" alt="5" data-base62-sha1="jVx6wWd4Ad51b9k3ufRQlQWDInV" width="672" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8baa3d5f4a89c84e631b57531a60090b9134fda3_2_672x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8baa3d5f4a89c84e631b57531a60090b9134fda3_2_1008x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8baa3d5f4a89c84e631b57531a60090b9134fda3_2_1344x1000.jpeg 2x" data-dominant-color="96A78A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">5</span><span class="informations">1346×1001 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It absorbs the same amount of dose as the output of your algorithm, the only difference is that it does not perfectly fit the skin. However, we can come up with solutions for this, such as support elements all around (where there is no dose anyway).</p>
<p>This is a much cleaner and simpler algorithm, and I could implement it way faster than fixing up your algorithm. If this is a possibility (you tell me as again, I’m not working in the field), would you accept this solution? It could be validated in your center and we could publish the result. Please let me know!</p>

---

## Post #11 by @sima (2024-08-24 18:07 UTC)

<p>Dear Professor,</p>
<p>I have read your message thoroughly and have a few comments on it. In fact, the idea you proposed was our initial approach to the issue, and we had already taken similar steps. However, before I can provide you with a complete response, I need to consult with my supervisors. One of my supervisors, who is a senior radiation physicist at the hospital, is currently on vacation. Therefore, I must wait for his return before proceeding.</p>
<p>I felt it was important to give you feedback and assure you that I will respond to your message as soon as possible.</p>

---

## Post #12 by @sima (2024-09-09 11:27 UTC)

<p>I sincerely apologize for the considerable delay in responding to you.<br>
Some of the concerns you raised about the algorithm are acceptable to me.<br>
For example, the code was written as a script (not as a class) and I reviewed its performance step-by-step by running in the Python console, so I used file paths and node names. I assumed these would be modified and adapted once the code is converted into a module format. (I have previously asked for help in my messages because I lack experience and I am not very professional in programming)<br>
To ensure that the code works correctly in all radiation beam positions (from 0 to 180 degrees), I implemented certain conditions. In fact, to fix the bugs I encountered and generalize the code for use in all spaces, additional assumptions were made.<br>
Regarding the issue where ‘the bolus does not reach to the edge of the dose deposition area,’ the problem generally occurs at the edges of the field. The solution is to use a larger bolus (for instance, in the axial direction, two or three slices larger than the PTV boundary, and in the lateral direction, a few centimeters larger than the PTV boundary)<br>
The idea you proposed was our initial concept (moving the normal tissue under the PTV as a bolus to the skin surface along the beam direction). However, over time, we arrived at the current solution (this algorithm).<br>
The goal is to shift the isodoses closer to the distal surface of the PTV, so the bolus must be placed directly on the skin without any air gaps.<br>
The model you suggested should, after the last stage, be able to automatically calculate the distance between the bolus and the body (air gap) and fill it in. Then it should also reduce the thickness from the top of the bolus along the same axis to ensure that the thickness remains consistent.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b11ac5648052d8c3f604ae1417313a2cdb91097.jpeg" data-download-href="/uploads/short-url/m7NS66Yd4wT92A0asJEKNqxEYbJ.jpeg?dl=1" title="Picture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b11ac5648052d8c3f604ae1417313a2cdb91097.jpeg" alt="Picture1" data-base62-sha1="m7NS66Yd4wT92A0asJEKNqxEYbJ" width="670" height="500" data-dominant-color="96A688"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture1</span><span class="informations">972×725 31.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
One fundamental problem we might encounter is that if the height of the air gap that needs to be filled is greater than the thickness above it, it is not possible to reduce it. In such cases, the bolus effectively gets removed from that location. So, we aimed to place the required distance directly on the skin.<br>
I believe that if you have an idea for this problem, it could serve as an alternative to my algorithm.<br>
I eagerly await your feedback</p>

---

## Post #13 by @cpinter (2024-09-10 08:49 UTC)

<aside class="quote no-group" data-username="sima" data-post="12" data-topic="37766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sima/48/67638_2.png" class="avatar"> sima:</div>
<blockquote>
<p>should, after the last stage, be able to automatically calculate the distance between the bolus and the body (air gap) and fill it in. Then it should also reduce the thickness from the top of the bolus along the same axis to ensure that the thickness remains consistent.</p>
</blockquote>
</aside>
<p>This could be very difficult without using “tricks”. I made this suggestion because it is very simple and thus robust, as opposed to a complex but fragile algorithm. That’s why I was asking about the consequences of the air gap, as I’m not a physicist.</p>
<aside class="quote no-group" data-username="sima" data-post="12" data-topic="37766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sima/48/67638_2.png" class="avatar"> sima:</div>
<blockquote>
<p>the bolus must be placed directly on the skin without any air gaps.</p>
</blockquote>
</aside>
<p>It would facilitate the discussion if you gave an objective explanation of the reason for this. Thank you.</p>

---

## Post #14 by @sima (2024-09-11 10:42 UTC)

<p>One of the persistent challenges in creating custom boluses for patients in electron therapy, as discussed in various articles, is achieving conformity between the bolus and the irregular, curved surface of the patient’s skin. Many studies have also measured the air gap between the bolus and the body, investigating its impact on dose distribution, treatment accuracy, and precision.<br>
In electron therapy due to the physical properties of electrons (which have lower energy and less penetration depth compared to photons), the bolus must be as close as possible to the surface of the skin. Electrons are very sensitive to distance with their energy dropping by 2 MeV per centimeter. Even a small air gap can significantly affect the dose distribution. In practice, if the bolus is positioned with a gap from the skin, the effective dose in the target area will decrease, leading to inadequate treatment.</p>

---

## Post #15 by @cpinter (2024-09-11 10:48 UTC)

<p>Thank you! What I neglected was the fact that it is electrons not photons. I will be thinking on how to “collapse” the proximal (to the source) part of the bolus towards the skin in an elegant way.</p>
<p>In the meantime maybe you could do some cleanup of your script in case you decide it to publish your algorithm. I mentioned several concrete things to fix besides the point you reacted to in your last post.</p>

---

## Post #16 by @sima (2024-09-13 11:16 UTC)

<p>As I have mentioned before, I am very eager for the algorithm I have developed to be incorporated as a module in the 3D Slicer software with your help, and to include this experience in my CV. Additionally, after this, I would like to discuss other tasks being carried out in our department that have the potential to be transformed into modules.<br>
Right now, I feel a bit confused and unsure about my role moving forward. Could you please clarify the next steps? You mentioned that you are working on your own idea. Will I have a role in that idea, and will I be of any help?</p>
<p>In previous messages, you mentioned that my algorithm works in 2D and is slow. I ran the algorithm on 3 PTVs (which were designed in a phantom with somewhat <strong>exaggerated</strong> shapes) and estimated the execution time of the code. On average, it took about 2 minutes (1:43, 1:56, 2:06 ) for the code to run completely and the bolus to be generated. Is this time too long to be unacceptable? (My computer is an ordinary system with a core i5 CPU and 16GB of RAM).</p>
<p>I plan to extract the data of several patients who are candidates for electron therapy from the hospital’s TPS this week, design boluses for them with my code, and share the dosimetric information and the code’s runtime with you.</p>
<p>I am very keen to understand the roadmap you have in mind and my role in this path. Could you provide me with more details?<br>
thanks.</p>

---

## Post #17 by @cpinter (2024-09-13 12:27 UTC)

<p>It’s ultimately up to you how we proceed. I have a general interest in RT, but bolus generation is not on the immediate roadmap.</p>
<p>Given the difficulty of fixing the simple approach I suggested in order to fulfill the dosimetric requirements, I think we can discard it for now. This approach would basically be to implement a function that collapses a segment against another using a given direction vector (<a class="mention" href="/u/lassoan">@lassoan</a> Do we have anything similar? Maybe SOFA could do it but probably an overkill). So I suggest continuing with the prototype you have.</p>
<p>I can help you make this script into a module, but I think it would be best to start it in its own GitHub repository, and later integrate it into SlicerRT after the validation is done.</p>
<p>A possible approach:</p>
<ol>
<li>You create a GitHub repository in your institution. Let me know if this is problematic, in that case I’ll create one for you, but considering ownership (control, attribution, visibility for your team, etc) you probably want to have your own</li>
<li>Make sure both of us has write access to the repo</li>
<li>I create an extension framework and one module in it for the bolus generation with the appropriate GUI</li>
<li>I provide you guidance on how to integrate your code into the module</li>
</ol>
<p>How does this sound?</p>

---

## Post #18 by @cpinter (2024-09-13 12:33 UTC)

<aside class="quote no-group" data-username="sima" data-post="16" data-topic="37766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sima/48/67638_2.png" class="avatar"> sima:</div>
<blockquote>
<p>design boluses for them with my code, and share the dosimetric information and the code’s runtime with you</p>
</blockquote>
</aside>
<p>This is great! This will be the validation I’ve mentioned. I assumed that you’ll want to write a journal paper about this, given that you need it for your thesis. I think it’s worthy of a full paper in a technically oriented medical physics journal (MedPhys, PESM, etc.). Once you have the module and the validation, it’s just to  one step to write it.</p>

---

## Post #19 by @sima (2024-09-13 17:59 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="17" data-topic="37766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>A possible approach:</p>
</blockquote>
</aside>
<p>that is a great approach.<br>
I am trying to create GitHub repository and I put the script there<br>
I will share with you if there is a problem with the repository construction (I don’t have experience with GitHub repository, but I will try my best to make it as I made the Gist before)</p>
<p>At the same time, I am working on the data of several patients for validation, and after the investigations, I will share the results with you.</p>
<p>It is a great honor for me to work with you.</p>

---

## Post #20 by @cpinter (2024-09-13 18:44 UTC)

<aside class="quote no-group" data-username="sima" data-post="19" data-topic="37766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sima/48/67638_2.png" class="avatar"> sima:</div>
<blockquote>
<p>and I put the script there</p>
</blockquote>
</aside>
<p>Please don’t put the script there. Let’s follow the steps accurately. Thanks!</p>

---

## Post #21 by @sima (2024-09-14 03:18 UTC)

<p>Oh sorry !</p>
<p>The GitHub repository must be empty and first, a suitable framework should be built in it<br>
I apologize for misunderstanding <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---

## Post #22 by @sima (2024-09-15 10:16 UTC)

<p>I have created a repository on GitHub and invited you.  I would be glad if you accepted the invitation</p>

---

## Post #23 by @cpinter (2024-09-16 08:38 UTC)

<p>Thank you! Can you please rename it to SlicerElectronBolus? You’d need to do that anyway during the acceptance process for extension.</p>
<p>Please see this for the list of requirements (I only found this list in actual PRs so this is of another extension). Some of which are basic settings of the GitHub repo, you can do some of these now</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/pull/2084">
  <header class="source">

      <a href="https://github.com/Slicer/ExtensionsIndex/pull/2084" target="_blank" rel="noopener">github.com/Slicer/ExtensionsIndex</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/ExtensionsIndex/pull/2084" target="_blank" rel="noopener">Add SegmentationVerification extension</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>cpinter:segmentation-verification</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-08-26" data-time="15:13:45" data-timezone="UTC">03:13PM - 26 Aug 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/cpinter" target="_blank" rel="noopener">
            <img alt="cpinter" src="https://avatars.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
            cpinter
          </a>
        </div>

        <div class="lines" title="2 commits changed 1 files with 8 additions and 0 deletions">
          <a href="https://github.com/Slicer/ExtensionsIndex/pull/2084/files" target="_blank" rel="noopener">
            <span class="added">+8</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">&lt;!--
Thank you for contributing to 3D Slicer!
- To add a new extension with th<span class="show-more-container"><a href="https://github.com/Slicer/ExtensionsIndex/pull/2084" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">is pull request: Please keep content of "New extension" section and put an 'x' in the brackets for each todo item to indicate that you have accomplished that prerequisite.
- To update an existing extension with this pull request: Please delete all text in this template and just describe which extension is updated and optionally tell us in a sentence what has been changed. To make extension updates easier in the future you may consider replacing specific git hash in your json file by a branch name (for example: `main` for Slicer Preview Releases; `(majorVersion).(minorVersion)` such as `5.6` for Slicer Stable Releases).
--&gt;

# New extension



- [x] Extension has a reasonable name (not too general, not too narrow, suggests what the extension is for)
- [x] Repository name is Slicer+ExtensionName
- [x] Repository is associated with `3d-slicer-extension` GitHub topic so that it is listed [here](https://github.com/topics/3d-slicer-extension). To edit topics, click the settings icon in the right side of "About" section header and enter `3d-slicer-extension` in "Topics" and click "Save changes". To learn more about topics, read https://help.github.com/en/articles/about-topics
- [x] Extension description summarizes in 1-2 sentences what the extension is usable (should be understandable for non-experts)
- [x] Any known related patents must be mentioned in the extension description.
- [x] LICENSE.txt is present in the repository root. MIT  (https://choosealicense.com/licenses/mit/) or Apache (https://choosealicense.com/licenses/apache-2.0/) license is recommended. If source code license is more restrictive for users than MIT, BSD, Apache, or 3D Slicer license then the name of the used license must be mentioned in the extension description.
- [x] Extension URL and revision (scmurl, scmrevision) is correct, consider using a branch name (main, release, ...) instead of a specific git hash to avoid re-submitting pull request whenever the extension is updated
- [x] Extension icon URL is correct (do not use the icon's webpage but the raw data download URL that you get from the download button - it should look something like this: https://raw.githubusercontent.com/user/repo/main/SomeIcon.png)
- [x] Screenshot URLs (screenshoturls) are correct, contains at least one
- [x] Homepage URL points to valid webpage containing the following:
  - [x] Extension name
  - [x] Short description: 1-2 sentences, which summarizes what the extension is usable for
  - [x] At least one nice, informative image, that illustrates what the extension can do. It may be a screenshot.
  - [x] Description of contained modules: at one sentence for each module
  - [x] Tutorial: step-by-step description of at least the most typical use case, include a few screenshots, provide download links to sample input data set
  - [x] Publication: link to publication and/or to PubMed reference (if available)
  - [x] License: We suggest you use a permissive license that includes patent and contribution clauses.  This will help protect developers and ensure the code remains freely available.  We suggest you use the [Slicer License](https://github.com/Slicer/Slicer/blob/main/License.txt) or the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Always mention in your README file the license you have chosen.  If you choose a different license, explain why to the extension maintainers. Depending on the license we may not be able to host your work. Read [here](https://opensource.guide/legal/#which-open-source-license-is-appropriate-for-my-project) to learn more about licenses.
  - [x] Content of submitted json file is consistent with the top-level CMakeLists.txt file in the repository (dependencies, etc. are the same)
- Hide unused features in the repository to reduce noise/irrelevant information:
  - [x] Click `Settings` and in repository settings uncheck `Wiki`, `Projects`, and `Discussions` (if they are currently not used)
  - [x] Click the settings icon next to `About` in the top-right corner of the repository main page and uncheck `Releases` and `Packages` (if they are currently not used)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I’ll generate the extension skeleton hopefully soon.</p>

---

## Post #24 by @sima (2024-09-16 15:36 UTC)

<p>Yes, definitely.<br>
Thank you for your guidance.<br>
I will thoroughly study this link to learn more.<br>
I am a beginner in Git and GitHub and have just started learning in this field. If I make any mistakes, I would appreciate it if you could guide me.<br>
Thank you in advance for your help.</p>

---

## Post #25 by @cpinter (2024-09-17 08:45 UTC)

<p>Thank you very much for the quick rename. For the record the repository is</p><aside class="onebox githubrepo" data-onebox-src="https://github.com/simaaz/SlicerElectronBolus">
  <header class="source">

      <a href="https://github.com/simaaz/SlicerElectronBolus" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/64c374f5791d13b4a05076d85211901e/simaaz/SlicerElectronBolus" class="thumbnail">

  <h3><a href="https://github.com/simaaz/SlicerElectronBolus" target="_blank" rel="noopener">GitHub - simaaz/SlicerElectronBolus</a></h3>

    <p><span class="github-repo-description">Contribute to simaaz/SlicerElectronBolus development by creating an account on GitHub.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #26 by @cpinter (2024-09-17 09:20 UTC)

<p>I generated the extension and the module skeleton. I think the user interface you suggested can be simplified, see<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b96322597583530835a39af9a744864f7e11db0d.png" data-download-href="/uploads/short-url/qs0J0R0UOPYwTT3W0yXGIP22w7H.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b96322597583530835a39af9a744864f7e11db0d_2_690x442.png" alt="image" data-base62-sha1="qs0J0R0UOPYwTT3W0yXGIP22w7H" width="690" height="442" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b96322597583530835a39af9a744864f7e11db0d_2_690x442.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b96322597583530835a39af9a744864f7e11db0d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b96322597583530835a39af9a744864f7e11db0d.png 2x" data-dominant-color="F3ECEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">843×541 71.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So we’d only have a selector for the RT plan, the isodose surface, and the skin segment.<br>
It will be important to describe in the documentation how this module expects the isodose surface to be generated (i.e. what dose level needs to be entered, and to keep only one value).</p>
<p>I’ll make this GUI soon and then I’ll give you instructions on how to fill the class with your code.</p>

---

## Post #27 by @sima (2024-09-18 07:47 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="26" data-topic="37766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I generated the extension and the module skeleton</p>
</blockquote>
</aside>
<p>Thanks a lot. I was so excited to see it !</p>
<aside class="quote no-group" data-username="cpinter" data-post="26" data-topic="37766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>So we’d only have a selector for the RT plan, the isodose surface, and the skin segment</p>
</blockquote>
</aside>
<p>I didn’t quite understand the point you mentioned about “Plan contains reference” and I may have misunderstood some of the concepts. When I add a patient’s Dicom data in 3d Slicer, I see that RTPlan, RTStructure, RTDose, and CT (reference volume) are each separate branches of the patient data. However, I don’t understand how the RTPlan contains a reference. This issue also applies to the PTV model. I used to import the PTV as a model from RTStructure.<br>
I also have another question regarding segment and model. Previously, you suggested using a segment instead of the model. What changes need to be made in the code for this? Also, regarding the output, the current code I have outputs the bolus as a labelmap volume. What changes are required to have the segment instead?</p>
<aside class="quote no-group" data-username="cpinter" data-post="26" data-topic="37766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>describe in the documentation how this module expects the isodose surface to be generated</p>
</blockquote>
</aside>
<p>Thank you for the reminder. Yes, this is an important point when working with the module</p>
<aside class="quote no-group" data-username="cpinter" data-post="26" data-topic="37766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>then I’ll give you instructions on how to fill the class with your code.</p>
</blockquote>
</aside>
<p>I’m very grateful and delighted to have your valuable assistance by my side.</p>

---

## Post #28 by @cpinter (2024-09-24 09:41 UTC)

<aside class="quote no-group" data-username="sima" data-post="27" data-topic="37766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sima/48/67638_2.png" class="avatar"> sima:</div>
<blockquote>
<p>I don’t understand how the RTPlan contains a reference. This issue also applies to the PTV model.</p>
</blockquote>
</aside>
<p>An RTPlan node, which is defined in SlicerRT, contains several properties and references. One of these references is the CT, and another one is the target segment. See the related module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e72f08d072ac7854f7e05df51b4ad4d7ab5dee0e.png" data-download-href="/uploads/short-url/wZ947xfIwUfnMCVm6PHe9h7QqIe.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e72f08d072ac7854f7e05df51b4ad4d7ab5dee0e.png" alt="image" data-base62-sha1="wZ947xfIwUfnMCVm6PHe9h7QqIe" width="401" height="500" data-dominant-color="F3EDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">471×587 30.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="sima" data-post="27" data-topic="37766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sima/48/67638_2.png" class="avatar"> sima:</div>
<blockquote>
<p>Previously, you suggested using a segment instead of the model. What changes need to be made in the code for this? Also, regarding the output, the current code I have outputs the bolus as a labelmap volume. What changes are required to have the segment instead?</p>
</blockquote>
</aside>
<p>This takes us to step 4 in the list <a href="https://discourse.slicer.org/t/creating-a-module-for-electron-bolus/37766/17">here</a>. I’ll give you guidance to do these changes, but let’s go step by step, I still need to create the module GUI.</p>

---

## Post #29 by @sima (2024-09-25 08:17 UTC)

<p>Thank you for your clear and insightful explanations.</p>

---

## Post #30 by @cpinter (2024-09-25 11:54 UTC)

<p>I made the UI. As we discussed, it is quite simple:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d9d4539641a804b67b6640134965a9735d7ca86.png" alt="image" data-base62-sha1="hVeDjtyN6NtgkrmDtlLcuD6OxPU" width="306" height="140"></p>
<p>The next steps are:</p>
<ul>
<li>Go through the <code>ElectronBolus.py</code> file and change the obvious things:
<ul>
<li>Module category, contributors, acknowledgement, etc.</li>
<li>Differences due to the sample module and yours
<ul>
<li>There is no <code>invertedOutputSelector</code></li>
<li>Argument list of the <code>process</code> function should be the list of inputs we need (see below)</li>
</ul>
</li>
</ul>
</li>
<li>Set the segmentation node from the RT plan to the skin segment selector widget (I think this can be done in <code>_checkCanApply</code>)</li>
<li>Modify <code>_checkCanApply</code> function to check all the inputs necessary:
<ul>
<li>RT plan plus the objects we need from its references:
<ul>
<li>CT</li>
<li>Target segment (segmentation node and segment)</li>
</ul>
</li>
<li>Isodose model</li>
<li>Skin segment</li>
</ul>
</li>
</ul>

---

## Post #31 by @sima (2024-10-13 18:35 UTC)

<p>hi Csaba<br>
I apologize for the considerable delay.</p>
<p>Unfortunately, I couldn’t do all the steps you mention<br>
I can just change categories, contributors, help and acknowledgment text. (very very obvious and easy things <img src="https://emoji.discourse-cdn.com/twitter/pensive.png?v=12" title=":pensive:" class="emoji" alt=":pensive:" loading="lazy" width="20" height="20">)</p>
<aside class="quote no-group" data-username="cpinter" data-post="30" data-topic="37766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<ul>
<li>
<ul>
<li>
<ul>
<li>Argument list of the <code>process</code> function should be the list of inputs we need (see below)</li>
</ul>
</li>
</ul>
</li>
<li>Set the segmentation node from the RT plan to the skin segment selector widget (I think this can be done in <code>_checkCanApply</code>)</li>
<li>Modify <code>_checkCanApply</code> function to check all the inputs necessary:</li>
<li>RT plan plus the objects we need from its references:
<ul>
<li>CT</li>
<li>Target segment (segmentation node and segment)</li>
</ul>
</li>
<li>Isodose model</li>
<li>Skin segment</li>
</ul>
</blockquote>
</aside>
<p>about these parts, I am confused! and I dont know how should apply changes</p>
<p>Could you please guide me more and in greater detail</p>

---

## Post #32 by @cpinter (2024-10-14 15:17 UTC)

<p>Please ask concrete questions and I will try to answer.</p>

---

## Post #33 by @sima (2024-10-15 10:50 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="30" data-topic="37766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>checkCanApply</p>
</blockquote>
</aside>
<p>You mentioned that you had created the UI according to the image, but I couldn’t figure out exactly where the definitions and inputs were made. (for example I couldn’t find the <strong>RT plan</strong> or <strong>isodose surface</strong> in the widget function <img src="https://emoji.discourse-cdn.com/twitter/roll_eyes.png?v=12" title=":roll_eyes:" class="emoji" alt=":roll_eyes:" loading="lazy" width="20" height="20">)</p>
<p>You asked me to modify the process and checkCanApply functions based on the inputs used in the code, but I don’t know how to define my inputs in these functions, especially since we agreed that only the RT plan would be described as a widget and that the CT and PTV would be extracted from the RT plan.</p>
<p>I haven’t worked with GUI codes and the functions used in them before, and my knowledge is very limited <img src="https://emoji.discourse-cdn.com/twitter/frowning_face.png?v=12" title=":frowning_face:" class="emoji" alt=":frowning_face:" loading="lazy" width="20" height="20"> . If there is an informational source that I could learn from, I’d appreciate it if you could introduce it to me.</p>

---

## Post #34 by @cpinter (2024-10-15 11:25 UTC)

<aside class="quote no-group" data-username="sima" data-post="33" data-topic="37766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sima/48/67638_2.png" class="avatar"> sima:</div>
<blockquote>
<p>If there is an informational source that I could learn from, I’d appreciate it if you could introduce it to me.</p>
</blockquote>
</aside>
<p>Here’s the programming tutorial</p><aside class="onebox githubrepo" data-onebox-src="https://github.com/Slicer/SlicerProgrammingTutorial">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerProgrammingTutorial" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/dfa4ed67c2b4264d1bddc0b330ba73ff/Slicer/SlicerProgrammingTutorial" class="thumbnail">

  <h3><a href="https://github.com/Slicer/SlicerProgrammingTutorial" target="_blank" rel="noopener">GitHub - Slicer/SlicerProgrammingTutorial: Introduction to Python scripting and module...</a></h3>

    <p><span class="github-repo-description">Introduction to Python scripting and module development for 3D Slicer</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Once you finish and understand that, and you still need to see how things are done, there are a lot of Python modules in Slicer and its extensions. Look at any of them for examples.</p>

---

## Post #35 by @sima (2024-11-01 19:30 UTC)

<p>According to your recommendation, I reviewed the file you sent. However, since it was in slide format, the explanations were brief, and it wasn’t a very comprehensive document. So, I attempted to gather more information from GitHub, the internet, and AI.  I did my best to implement the points you requested, however, I am uncertain about the success of my attempts. This was my first serious experience working with GitHub so I’d appreciate your feedback on my work and any corrections you suggest, as well as guidance on the next steps. I understand that the tasks you outlined were relatively straightforward, but as a beginner, they took me longer than expected. I apologize for any delay.</p>

---

## Post #36 by @sima (2024-11-14 07:46 UTC)

<p>Hello professor Pinter</p>
<p>I just wanted to follow up on my previous message to ensure it was seen. I am still looking forward to any feedback or guidance you could provide to me.</p>

---

## Post #37 by @cpinter (2024-11-14 12:02 UTC)

<p>I gave all the pointers that I could. The alternative is for us to do this for you, but I am extremely busy these days with funded projects and grant submissions. If you have some funding towards this development, please let me know, otherwise I suggest doing again the Slicer programming tutorial and understand the basics well. On this level it is really not that hard.</p>

---

## Post #38 by @sima (2024-11-15 06:32 UTC)

<p>Unfortunately, I don’t have any founding</p>
<p>That project was a part of my master’s thesis and I just wanted to continue my work by making it into a module for software that I have good memories with and I think, with the programming knowledge I had, I had good courage in taking this on. Now I have graduated and I’m on my own. Also, according to the Doller rate in my country, I can’t afford to pay.</p>
<p>I’m surprised to hear about funding from you after 37messages between us. I’ve always been honest in my messages and said that I’m a beginner in programming. My simple questions also showed that I’m not a Python programmer or a Slicer programmer. I can understand that I was slow in completing the tasks you asked of me, and this may have affected your opinion but I was completely sincere in my messages and requests for help.</p>
<aside class="quote no-group" data-username="cpinter" data-post="17" data-topic="37766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>A possible approach:</p>
</blockquote>
</aside>
<p>I was very happy that you gave me a roadmap</p>
<aside class="quote no-group" data-username="cpinter" data-post="28" data-topic="37766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>This takes us to step 4 in the list <a href="https://discourse.slicer.org/t/creating-a-module-for-electron-bolus/37766/17">here</a>. I’ll give you guidance to do these changes, but let’s go step by step, I still need to create the module GUI.</p>
</blockquote>
</aside>
<p>and I could learn many things with your guidance. (like that and many other things)</p>
<p>Anyway, I’ll make my effort to continue and solve the fourth step in the roadmap, but not now because I feel discouraged and need time to recover.</p>
<p>Thank you for the time you’ve spent helping me.</p>
<p>Best regard</p>

---

## Post #39 by @cpinter (2024-11-15 08:46 UTC)

<p>Please understand that you cannot expect university professors and company directors to actually implement Slicer modules for you. Maybe you will realize this at a later stage of your carreer. I spent a lot of time trying to help you (much more than usual), and it’s unfortunate that it is not enough. Your module is just a little bit more complicated than the example in the tutorial…</p>

---
