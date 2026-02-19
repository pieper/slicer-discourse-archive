---
topic_id: 21737
title: "Inserting An Image Under The Interactive Plot"
date: 2022-02-01
url: https://discourse.slicer.org/t/21737
---

# Inserting an image under the interactive plot

**Topic ID**: 21737
**Date**: 2022-02-01
**URL**: https://discourse.slicer.org/t/inserting-an-image-under-the-interactive-plot/21737

---

## Post #1 by @armandanesh (2022-02-01 19:01 UTC)

<p>Hello,</p>
<p>I was wondering if there would be a way in order to get the interactive plot to work over an image. For example, to have a cartesian grid overlay a particular image such that we can plot points on particular positions on the image? Thank you in advance for your response.</p>
<p>Best,<br>
Arman</p>

---

## Post #2 by @lassoan (2022-02-02 02:49 UTC)

<p>Can you draw a sketch that shows what you would like to get as an end result?</p>

---

## Post #3 by @armandanesh (2022-02-02 06:35 UTC)

<p>So this is just a rough image I pulled off google but essentially I am asking if it would be possible to have an interactive scene where instead of having a white background, the background is actually an image of our choice with the cartesian grid on top of it. For example, can it be an ultrasound image as the background of the interactive scene and we plot points on top of it?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d499aa9df62ce2f5b72bf21057241036a3bddaa2.jpeg" data-download-href="/uploads/short-url/ukKs3VxMegrYvCnuACfacdTalbA.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d499aa9df62ce2f5b72bf21057241036a3bddaa2_2_690x388.jpeg" alt="image" data-base62-sha1="ukKs3VxMegrYvCnuACfacdTalbA" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d499aa9df62ce2f5b72bf21057241036a3bddaa2_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d499aa9df62ce2f5b72bf21057241036a3bddaa2_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d499aa9df62ce2f5b72bf21057241036a3bddaa2.jpeg 2x" data-dominant-color="CBCDCE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×720 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2022-02-02 13:23 UTC)

<p>You need to add an actor to the VTK renderer for this.</p>
<p>For augmented reality applications you can display a background planar image as siren in this example: <a href="https://kitware.github.io/vtk-examples/site/Python/Images/BackgroundImage/">https://kitware.github.io/vtk-examples/site/Python/Images/BackgroundImage/</a></p>
<p>For displaying the 3D content in immersive environment you can display a skybox: <a href="https://kitware.github.io/vtk-examples/site/Cxx/Rendering/PBR_Skybox">https://kitware.github.io/vtk-examples/site/Cxx/Rendering/PBR_Skybox</a></p>
<p>See how to access the VTK renderer here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>
<p>Alternatively, you can add lines over the 3D content using 2D actors.</p>

---

## Post #5 by @armandanesh (2022-02-02 16:37 UTC)

<p>Hello,</p>
<p>Thank you so much!!! Just to confirm, this allows me to insert a 2d image as the background of the 2d interactive scene containing the cartesian grid, correct?</p>

---

## Post #6 by @armandanesh (2022-02-02 21:31 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0da7e3c5d6e88274a2a434daf8cfa8dcd9011b5e.png" data-download-href="/uploads/short-url/1WNUn2uaKbQxezrkHoUZu7k9QHc.png?dl=1" title="Screen Shot 2022-02-02 at 4.27.31 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0da7e3c5d6e88274a2a434daf8cfa8dcd9011b5e_2_560x500.png" alt="Screen Shot 2022-02-02 at 4.27.31 PM" data-base62-sha1="1WNUn2uaKbQxezrkHoUZu7k9QHc" width="560" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0da7e3c5d6e88274a2a434daf8cfa8dcd9011b5e_2_560x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0da7e3c5d6e88274a2a434daf8cfa8dcd9011b5e_2_840x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0da7e3c5d6e88274a2a434daf8cfa8dcd9011b5e_2_1120x1000.png 2x" data-dominant-color="3C3C3A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-02-02 at 4.27.31 PM</span><span class="informations">1283×1145 20.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
For reference, I am talking about changing the background on the top right scene.</p>

---
