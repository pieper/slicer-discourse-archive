# Statistical shape Model based segmentation

**Topic ID**: 21623
**Date**: 2022-01-25
**URL**: https://discourse.slicer.org/t/statistical-shape-model-based-segmentation/21623

---

## Post #1 by @scarpma (2022-01-25 14:43 UTC)

<p>Hello everyone.</p>
<p>I would like to use a <strong>statistical shape model</strong> that I created in order to <strong>segment new structures</strong> from dicom files.</p>
<p>Basically I have a shape model (vtk polydata) modifiable through 26 scalar parameters. The mathematical operations are very simple. Each parameter w_i is just a weight to be multiplied to a basis vector v_i of 20000 elements. The operation sum_i (w_i * v_i) = X is used to compute the positions of the points of the mesh (20000 points).</p>
<p><strong>I would like to adapt this model to a dicom file by doing an optimization process on these 26 parameters</strong>.</p>
<p>Do you know something ready to use to do this ? The metric to optimize could be based on the gradient of the dicom images, highligthing edges on the images and trying to bring surface mesh and these edges as close as possible.</p>
<p>I would like to implement this into slicer in order to actively watch the superposition between the model and the dicom file, but I have never used slicer with the python interprer.</p>

---

## Post #2 by @stevenagl12 (2022-01-25 19:06 UTC)

<p>The only methods to do this right now, are outside of the realm of 3D Slicer, to my knowledge. you need to create both an intensity based statistical model and a morphometric based model. You can do this in deformetrica, shapeworks, Scalismo (Scala programming), RvtkStatismo (R programming), and now on Matlab if you search for the Active Appearance or Shape model code.</p>

---

## Post #3 by @mau_igna_06 (2022-01-26 09:45 UTC)

<p>Hi Martino.</p>
<p>Your question is very interesting.</p>
<p>Did you make the SSM with itk? With which class? Do you have a code sample?</p>
<blockquote>
<p>Do you know something ready to use to do this ?</p>
</blockquote>
<p>I think you could do it with itk. See below</p>
<p>Here are some useful resourses for you I found online that might answer your questions:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://slideplayer.com/amp/15454038/">
  <header class="source">

      <a href="https://slideplayer.com/amp/15454038/" target="_blank" rel="noopener nofollow ugc">slideplayer.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slideplayer.com/amp/15454038/" target="_blank" rel="noopener nofollow ugc">Lecture 15 Active Shape Models -  ppt download</a></h3>

  <p>Active Shape Models (ASM) &amp; Active Appearance Models (AAM) We’ll cover mostly the original active shape models. TF Cootes, CJ Taylor, DH Cooper, J Graham, Computer Vision and Image Understanding, Vol 61, No 1, January, pp , 1995 Conceptually an...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slideplayer.com/slide/2428478/">
  <header class="source">

      <a href="https://slideplayer.com/slide/2428478/" target="_blank" rel="noopener nofollow ugc">slideplayer.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slideplayer.com/slide/2428478/" target="_blank" rel="noopener nofollow ugc">Active Shape Models Suppose we have a statistical shape model –Trained from...</a></h3>

  <p>Building Shape Models Given aligned shapes, { } Apply PCA P – First t eigenvectors of covar. matrix b – Shape model parameters</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p><a href="https://munch.paap.cup.edu.uy/w/index.php/ContributedCode:ITKShapeGuidedSegmentation" class="onebox" target="_blank" rel="noopener nofollow ugc">https://munch.paap.cup.edu.uy/w/index.php/ContributedCode:ITKShapeGuidedSegmentation</a><br>
<a href="https://itk.org/ItkSoftwareGuide.pdf" rel="noopener nofollow ugc">https://itk.org/ItkSoftwareGuide.pdf</a> → search for Model Based Registration</p>
<p>Please keep me posted of your advances with this method. I would be very interested on seeing preliminar results.</p>
<p>Mauro</p>

---

## Post #4 by @scarpma (2022-01-26 09:58 UTC)

<p>Thank you for the answer. I’m looking into what you suggested. I did not know shapeworks, but it seems very powerful. About the other frameworks, I have worked with some of them, but I felt they were a little bit too “narrow”. I would like to get my hands dirty with some code, but for example deformetrica does not allow much elasticity.</p>

---

## Post #5 by @stevenagl12 (2022-01-26 12:47 UTC)

<p>So RvtkStatismo and Scalismo both offer much more elasticity. By that I mean Scalismo allows you to build your own kernels such as point change kernels and symmetry based kernels to do parametric non-rigid registration, and allows you to do markov chain monte carlo shape completion. RvtkStatismo appears to not need an a priori or a posteriori shape based off from any gaussian kernels to do it. Scalismo is the best performer between the two and can allow you to visualize your models way better than RvtkStatismo, as that was something you were interested in, and has innate functions for AAS and ASM.</p>

---

## Post #6 by @lassoan (2022-01-27 06:40 UTC)

<p><a class="mention" href="/u/scarpma">@scarpma</a> Do you want to use SSM only to have a baseline for comparison to deep learning based methods, or you would like to use SSM for image segmentation? I’m just curious because what I see is that researchers that invested decades in developing SSM-based image segmentation methods have mostly switched to deep learning. However, it is hard to tell if this is because deep learning is so much better or it is because nowadays you need to do “AI” to get research funding.</p>

---

## Post #7 by @scarpma (2022-01-27 11:56 UTC)

<p>Hello Mauro, thanks for your very rich reply. I did my statistical shape model by non-rigidly aligning the various polygonal meshes that I have and then by doing a PCA. I did this in python, and also tried scalismo for reference. The code I used is very sparse, but it is really something not special. The most difficult part is the non rigid registration. For that I implemented a gradient descent based approach in pytorch and pytorch 3d.</p>
<p>Thank you very much for the reference. I will look into it for both the theoretical and technical part. I will keep this post updated in the future.</p>
<p>By the way, so you are suggesting itk ? I have zero experience with it, but I read of it many times. I imagine it would be easily integrated into slicer3d, no ?</p>

---

## Post #8 by @scarpma (2022-01-27 12:06 UTC)

<p>Thanks for the reply. In fact I’ve seen some active shape models done in some scalismo tutorial. I should give it a try because it does not require much effort, at least to begin with some simple test.</p>
<p>My main concerns with scalismo are:</p>
<ol>
<li>
<p>I have 0 confidence with the scala language and I don’t know if I want to invest in learning it (maybe that could be useful, I don’t know)</p>
</li>
<li>
<p>Scalismo framework seems useful, but I don’t know how much it is scalable and for how long it will be maintained. My doubt is if maybe Slicer3d is more flexible being python / c++ based and having a bigger community (I’m not completely sure of this, maybe you can confirm… )</p>
</li>
</ol>

---

## Post #9 by @scarpma (2022-01-27 12:13 UTC)

<p>Hello Andras, your point is really interesting.</p>
<p>Actually I have an already working deep learning pipeline for segmentation. It’s based on Unet networks and works pretty well.</p>
<p>First, let me say that an active shape model could also be deep learning based. So I wouldn’t completely see it as a ASM vs DL  battle.</p>
<p>Secondly, I would like to have a comparison with the “standard deep learning” pipeline that I have.</p>
<p>Lastly, my hopes are that an ASM would give result with:</p>
<ul>
<li>stronger topology constraints;</li>
<li>better mesh quality (no smoothing / remeshing needed since it is not a volumetric segmentation).</li>
</ul>
<p>For reference, I read this <a href="https://ieeexplore.ieee.org/document/7024128" rel="noopener nofollow ugc">article</a> which seems to have very nice results.</p>

---

## Post #10 by @pieper (2022-01-27 13:20 UTC)

<p><a class="mention" href="/u/scarpma">@scarpma</a> can you describe your segmentation goals?  The article you reference is about vertebrae and this is something of interest to several of us as well, and there is <a href="https://projectweek.na-mic.org/PW36_2022_Virtual/Projects/SpineSegmentation/">work going on</a> to make a robust segmenter in Slicer so perhaps we can join forces on that.</p>

---

## Post #11 by @scarpma (2022-01-27 13:31 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> actually i’m working with thoracic aortas. I would like to build a workflow similar to the one in the article for the aorta. Aorta is a bit complicated because I want to segment the main body of the thoracic aorta (ascending, arch and descending) as well as the first piece of the supraortic vessels.</p>
<p>Here is an example:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fff812a60ecb8045f873c861cfdd0a69024e8b6.jpeg" data-download-href="/uploads/short-url/kxRH2IcqVEMFwJnGU5GATWUNlNc.jpeg?dl=1" title="ideal output of the ASM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8fff812a60ecb8045f873c861cfdd0a69024e8b6_2_210x250.jpeg" alt="ideal output of the ASM" data-base62-sha1="kxRH2IcqVEMFwJnGU5GATWUNlNc" width="210" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8fff812a60ecb8045f873c861cfdd0a69024e8b6_2_210x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8fff812a60ecb8045f873c861cfdd0a69024e8b6_2_315x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8fff812a60ecb8045f873c861cfdd0a69024e8b6_2_420x500.jpeg 2x" data-dominant-color="A4A3A0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ideal output of the ASM</span><span class="informations">519×615 30.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @mau_igna_06 (2022-01-27 14:46 UTC)

<p>Yes. I understand that for application (aorta segmentation) you need to non-rigidly aligning as preprocessing.</p>
<blockquote>
<p>By the way, so you are suggesting itk ? I have zero experience with it, but I read of it many times. I imagine it would be easily integrated into slicer3d, no ?</p>
</blockquote>
<p>yes, itk is available in Slicer’s python interpreter if you pip-install it, so it really easy to use I think. Although, most itk examples are on C++ so you need to port them yourself.</p>
<p>Also you can look at <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#running-an-itk-filter-in-python-using-simpleitk" rel="noopener nofollow ugc">this possibility</a> to use some itk filters (I’ve used them in the past)</p>
<p>I was thinking of doing a Statistical shape model of vertebraes from the VerSe dataset just for curiosity to see if I could achieve some good segmentation results. Although I do this on my free time only. <a class="mention" href="/u/pieper">@pieper</a> we could share results, a bounding box detection algorithm would be really useful if we would want to use the active shape model to do segmentation also.</p>
<p>I was thinking about an idea. I’m not sure is correct but it would be great if it was. If you have a SSM of the vertebrae (or any anatomy) then if you mark landmarks on the mean model and on the mean + each eigenVector models. You could get the landmarks positions for any registration you do. So this would be useful for automatic landmarking I think.</p>
<p>If you get your SSM before than I. I could help you test this hypothesis if you are interested <a class="mention" href="/u/scarpma">@scarpma</a>.</p>
<p>Mauro</p>

---

## Post #13 by @scarpma (2022-01-27 15:40 UTC)

<p>So, if I understand well, your idea is to know (in some way) how some landmarks move in real space while changing the shape in the pca space.</p>
<p>If i got this right, then it is really easy. Being the mesh always with the same connectivity, you can define landmarks on the mean shape and then you will always know where these points are (just by knowing their index in the mesh).</p>
<p>In fact we could cast this problem into an easier one by letting the user define some fixed landmark that must match with predefined landmarks on the active shape. This optimization would be carried in a far smaller space and could give a good initialization for the segmentation.</p>
<p>For my case, though, it is not very simple to define landmarks on the aorta. Maybe with vertebrae it is simpler (?)</p>

---

## Post #14 by @mau_igna_06 (2022-01-27 17:03 UTC)

<aside class="quote no-group" data-username="scarpma" data-post="13" data-topic="21623">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/scarpma/48/13161_2.png" class="avatar"> scarpma:</div>
<blockquote>
<p>If i got this right, then it is really easy. Being the mesh always with the same connectivity, you can define landmarks on the mean shape and then you will always know where these points are (just by knowing their index in the mesh).</p>
</blockquote>
</aside>
<p>I don’t know much about PCA on meshes but it should work too I think. The idea was about using images (labelmaps) for the PCA. I have seen same examples and references of it being done on itk so it’s possible.<br>
This is a schema of my idea:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a912fd835d485a2844efd3105c30aa8eebe0415.png" data-download-href="/uploads/short-url/jLOX32QWBx9giwqYCco7VJPg2Gh.png?dl=1" title="shapeModelsEquation2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a912fd835d485a2844efd3105c30aa8eebe0415_2_604x499.png" alt="shapeModelsEquation2" data-base62-sha1="jLOX32QWBx9giwqYCco7VJPg2Gh" width="604" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a912fd835d485a2844efd3105c30aa8eebe0415_2_604x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a912fd835d485a2844efd3105c30aa8eebe0415_2_906x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a912fd835d485a2844efd3105c30aa8eebe0415.png 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">shapeModelsEquation2</span><span class="informations">1086×899 39.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can check if it makes sense to you</p>
<blockquote>
<p>For my case, though, it is not very simple to define landmarks on the aorta. Maybe with vertebrae it is simpler (?)</p>
</blockquote>
<p>Yes, on the vertebrae is definitely simpler</p>

---

## Post #15 by @scarpma (2022-01-27 17:22 UTC)

<p>I think it is simpler than this.</p>
<p>What I mean is this:<br>
Let’s suppose that you have a landmark on the active model, say the point Y=(Y_x, Y_y, Y_z), which will have an index k_Y (with respect to all the points of the active shape). Since PCA acts as a deformation of the mean mesh, each point is moved through space, but the indexes remain the same ! So, after the deformation of the mesh, the new position of the landmark Y’ will be X’[K_Y] (if you see X as the array of coordinates of the points in the active shape). Here X’ = X_mean + P b’ (using the notation you used).</p>

---
