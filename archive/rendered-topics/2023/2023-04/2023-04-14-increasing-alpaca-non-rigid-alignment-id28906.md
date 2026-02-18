# Increasing ALPACA Non-Rigid Alignment

**Topic ID**: 28906
**Date**: 2023-04-14
**URL**: https://discourse.slicer.org/t/increasing-alpaca-non-rigid-alignment/28906

---

## Post #1 by @evaherbst (2023-04-14 10:11 UTC)

<p>Hello,</p>
<p>I am currently testing ALPACA to transfer muscle attachment landmarks from one scapula to another for patient specific modeling.</p>
<p>The rigid alignment seems to work pretty well, but the deformable alignment is not working very well.</p>
<p>I have tried changing the alpha value but no success.</p>
<p>The meshes only have 4,000 vertices unfortunately so I was not able to test higher point densities.</p>
<p>Here are some screenshots. I am trying to deform the original mesh with the landmark (orangey red) to the yellow scapula. The red mesh is the rigidly transformed source model.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14ac2e83b2b3921e290894f9ed31afea8ee1cb0d.png" alt="image" data-base62-sha1="2WSrIf5jG2dS58qZA2nGoPGnHR3" width="428" height="403"></p>
<p>In green is the warped source mode - especially the medial border is not warping enough to align well with the yellow mesh:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/1527d511e8fb0667c2e2e7f0904ba3088d37d6b3.png" alt="image" data-base62-sha1="319mLvDEOvA09csGVcNWZtAoEkr" width="329" height="472"></p>
<p>Thank you very much,<br>
Eva</p>

---

## Post #2 by @evaherbst (2023-04-14 13:53 UTC)

<p>I also noticed I get this warning/error, but not sure if that has anything to do with it:</p>
<pre><code class="lang-auto">[VTK] Generic Warning: In D:\D\S\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx, line 3663

[VTK] vtkMRMLSubjectHierarchyNode::GetSubjectHierarchyNode: Invalid scene given

[Qt] void __cdecl qSlicerSubjectHierarchyPluginLogic::onNodeAboutToBeRemoved(class vtkObject *,class vtkObject *) : Failed to access subject hierarchy node

[VTK] GetReferencingNodes: null node or referenced node

[Qt] class QList&lt;class qSlicerFileWriter *&gt; __cdecl qSlicerCoreIOManagerPrivate::writers(const class QString &amp;,const class QMap&lt;class QString,class QVariant&gt; &amp;,class vtkMRMLScene *) const warning: Unable to find node with ID "" in the given scene.
</code></pre>

---

## Post #3 by @muratmaga (2023-04-14 15:30 UTC)

<aside class="quote no-group" data-username="evaherbst" data-post="1" data-topic="28906">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar"> evaherbst:</div>
<blockquote>
<p>The meshes only have 4,000 vertices unfortunately so I was not able to test higher point densities.</p>
</blockquote>
</aside>
<p>How many points are you left with during the pointcloud conversion? (ALPACA should report the number of points). If it is too few, that might be the problem.</p>
<aside class="quote no-group" data-username="evaherbst" data-post="1" data-topic="28906">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar"> evaherbst:</div>
<blockquote>
<p>I have tried changing the alpha value but no success.</p>
</blockquote>
</aside>
<p>Try changing both alpha and beta values together. Increasing CPD iterations will probably be useful as well.</p>
<p>Finally, the current ALPACA module will be deprecated soon, and we will switch to an ITK based implementation (instead of open3d we are currently using). Make sure you start using, it is already available with SlicerMorph (it is called ALPACA-preview), but it is hidden.</p>
<p>Go to <strong>Application Setting-&gt;Developer-&gt;Enable developer mode.</strong><br>
then, open the module finder, and check Testing.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/560648f84e96392ff7b4ab542d6f1eb02bf6c9c5.png" alt="image" data-base62-sha1="ch0wJZaZmUncRFH5p4pyZHzVSDP" width="665" height="198"></p>

---

## Post #4 by @evaherbst (2023-04-15 16:41 UTC)

<p>Hi Murat,</p>
<p>Thank you so much.<br>
The vertices ended up being 3969 and 4693.</p>
<p>Increasing the iterations seemed to make the biggest difference.</p>
<p>Just to confirm, increasing both alpha and beta will enable more transformation, or did I get this wrong? I  read the Alpaca documentation but still not entirely sure what these values are - it sounded like a lower alpha enables more deformation but I wasn’t sure if this means between deformed target and source or more deformations allowed in the transformation of the target.</p>
<p>When I compare alpha and beta set at 2 vs 4, 4 is generally more aligned except at the coracoid.</p>
<p>Here is the output with 1000 CPD iterations and alpha and beta set at 4, in the testing mode:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d55c223ff439cf34a8022bdb01dacb3c3066db2a.png" data-download-href="/uploads/short-url/urt60CLcaLKxCRjJQg2nH25erbQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d55c223ff439cf34a8022bdb01dacb3c3066db2a_2_382x500.png" alt="image" data-base62-sha1="urt60CLcaLKxCRjJQg2nH25erbQ" width="382" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d55c223ff439cf34a8022bdb01dacb3c3066db2a_2_382x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d55c223ff439cf34a8022bdb01dacb3c3066db2a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d55c223ff439cf34a8022bdb01dacb3c3066db2a.png 2x" data-dominant-color="9195BF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">389×508 46.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What is odd to me is that the transformed source mesh is <em>smaller</em> than the target although the source itself is <em>larger</em> than the target. But maybe this is due to not using landmarks to align the</p>
<p>If I decrease alpha to 2 and keep beta at 4 then the size marches better but the spine is less aligned<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12ab77933b33b58343d80607cd9f053f2bfce632.png" data-download-href="/uploads/short-url/2F9XA8JRtIuOdkbjoxVvGEMfIRA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12ab77933b33b58343d80607cd9f053f2bfce632_2_501x500.png" alt="image" data-base62-sha1="2F9XA8JRtIuOdkbjoxVvGEMfIRA" width="501" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12ab77933b33b58343d80607cd9f053f2bfce632_2_501x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12ab77933b33b58343d80607cd9f053f2bfce632.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12ab77933b33b58343d80607cd9f053f2bfce632.png 2x" data-dominant-color="959FC2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">692×690 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I also tried changing the CPD tolerance but it made only a slight difference and wasn’t clear if better or worse (some parts better aligned, some worse).</p>
<p>Is there any way I can make deform even more to match the target better? Or do I need higher resolution meshes?</p>
<p>Thank you so much,<br>
Eva</p>

---

## Post #5 by @muratmaga (2023-04-16 04:22 UTC)

<p>In our tests, 4000-6000 pts seemed to work well. So I don’t think lack of points is concerning at this point.</p>
<p>Both alpha and beta control the deformable registration. Alpha controls the fluidity (lower values) vs rigidity (higher values), while motion coherence makes sure the resultant vector field is smooth. Higher beta values will ensure more smooth vector field (such that deformation vectors from nearby points will be parallel), whereas low smoothing values will allow more disparate vectors. So, try reducing them both slowly and experiment. Couple suggestions to make your experiments a bit more easy to interpret.</p>
<ol>
<li>
<p>Annotate about 4-6 landmarks both on your source and target model in regions you care. If you input the optional target LMs, in the interactive mode, ALPACA will calculate a RMSE (root mean square error) between landmarks. As you change parameters, you want to reduce this value from the previous iteration.</p>
</li>
<li>
<p>Try “skip scaling”, if your scapula are of the similar sizes. Scaling is done by the bounding box, so if the samples are not in similar orientations, scaling may not be ideal. You can also try rotating the sample in similar orientations, and then keep scaling.</p>
</li>
<li>
<p>If you are on windows, use the Bayesian CPD, which is very slightly less accurate then default CPD we included, but 10 times faster. When you are running parameter sweeps like this, one usually wants to obtain results faster. You can find the bayesian CPD here: <a href="https://github.com/ohirose/bcpd" class="inline-onebox">GitHub - ohirose/bcpd: Bayesian Coherent Point Drift (BCPD/BCPD++/GBCPD/GBCPD++)</a>. Just clone (or download) the repository, check the acceleration option in advanced settings, and point out to the location of the bcpd.exe in the cloned repository location.</p>
</li>
</ol>

---

## Post #6 by @evaherbst (2023-04-21 14:01 UTC)

<p>Dear Murat,</p>
<p>Thank you so much for your help.<br>
I have tested various parameters and using the landmarks for checking RMSE is very useful.</p>
<p>I do use Windows and the Bayesian CPD was very useful.</p>
<p>Regarding scaling, the scapulae in this case are different sizes but oriented similarly, just translated. I also tested with different orientations and keeping the scaling seemed to work ok for all cases in terms of scaling and aligning fairly well for the rigid alignment.</p>
<p>After several other tests I could get better alignment by tweaking the rigid deformation parameters, and lower alpha and beta give sometimes give better alignment but sometimes higher values are better (depending on the case)</p>
<p>However, regardless of alpha and beta values, <strong>the rigidly transformed source mesh and the warped source mesh look like they are mostly translated from each other, and there is very little actually warping/bending going on.</strong></p>
<p>(target yellow transparent, rigidly deformed in red, warped in purple)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f24e0b879937b1c929fa39b3c4685486cd2ae32.png" data-download-href="/uploads/short-url/4rvOl5wQ8Plt7p5lwPyOYUaTCQq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f24e0b879937b1c929fa39b3c4685486cd2ae32_2_406x500.png" alt="image" data-base62-sha1="4rvOl5wQ8Plt7p5lwPyOYUaTCQq" width="406" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f24e0b879937b1c929fa39b3c4685486cd2ae32_2_406x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f24e0b879937b1c929fa39b3c4685486cd2ae32.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f24e0b879937b1c929fa39b3c4685486cd2ae32.png 2x" data-dominant-color="9486AF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">529×650 90.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dadf182d935ba7b6170b3c4fc2f0dac359d233cd.jpeg" data-download-href="/uploads/short-url/vee46tZ2Hw1YghSSjrwpr1NXkBL.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dadf182d935ba7b6170b3c4fc2f0dac359d233cd_2_369x500.jpeg" alt="image" data-base62-sha1="vee46tZ2Hw1YghSSjrwpr1NXkBL" width="369" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dadf182d935ba7b6170b3c4fc2f0dac359d233cd_2_369x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dadf182d935ba7b6170b3c4fc2f0dac359d233cd.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dadf182d935ba7b6170b3c4fc2f0dac359d233cd.jpeg 2x" data-dominant-color="A588AE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">530×717 76.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><strong>Another case with different meshes: the rigidly deformed model fits better to the source mesh than the warped mesh does</strong></p>
<p>(target yellow transparent, rigidly deformed in red, warped in green).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a54789eb38e585a17bc73db1f518bf5ad57861a.png" data-download-href="/uploads/short-url/jJIRUDswJVUfRBdDxXXvLXoUHs6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a54789eb38e585a17bc73db1f518bf5ad57861a_2_325x500.png" alt="image" data-base62-sha1="jJIRUDswJVUfRBdDxXXvLXoUHs6" width="325" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a54789eb38e585a17bc73db1f518bf5ad57861a_2_325x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a54789eb38e585a17bc73db1f518bf5ad57861a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a54789eb38e585a17bc73db1f518bf5ad57861a.png 2x" data-dominant-color="9F8CA8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">387×595 45.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><strong>Do you know what might be causing this, and how I can get a better fit?</strong><br>
I am already at alpha and beta .1 for case 1 (in case 2, higher alpha and betas seemed better for some reason)<br>
I am not sure why the warping is not doing much. Are the meshes too different?</p>
<p>If there is no solution, would it be possible to add the LDDMM framework to the ALPACA extension?</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.sciencedirect.com/science/article/abs/pii/S1053811914005205?via%3Dihub">
  <header class="source">
      <img src="https://sdfestaticassets-us-east-1.sciencedirectassets.com/shared-assets/13/images/favSD.ico" class="site-icon" width="" height="">

      <a href="https://www.sciencedirect.com/science/article/abs/pii/S1053811914005205?via%3Dihub" target="_blank" rel="noopener nofollow ugc">sciencedirect.com</a>
  </header>

  <article class="onebox-body">
    <img src="https://ars.els-cdn.com/content/image/1-s2.0-S1053811914005205-fx1.jpg" class="thumbnail" width="" height="">

<h3><a href="https://www.sciencedirect.com/science/article/abs/pii/S1053811914005205?via%3Dihub" target="_blank" rel="noopener nofollow ugc">Morphometry of anatomical shape complexes with dense deformations and sparse...</a></h3>

  <p>We propose a generic method for the statistical analysis of collections of anatomical shape complexes, namely sets of surfaces that were previously se…</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>A colleague uses the Deformetrica (<a href="http://www.deformetrica.org/" rel="noopener nofollow ugc">http://www.deformetrica.org/</a>) implementation of LDDMM with great success but unfortunately it does not support Windows, and ideally I would like to have my entire workflow in Slicer.<br>
I think it should be possible to add to Slicer since Deformetrica is written in Python, but I am not sure how time intensive it would be.</p>
<p>Ideally of course I could get the current Alpaca method to work better for the morphing.</p>
<p>Thank you so much,<br>
Eva</p>

---

## Post #7 by @muratmaga (2023-04-21 14:54 UTC)

<p>ALPACA works on point clouds, whereas LDDMM methods like deformetrica works on meshes. I haven’t checked them lately, but it tended to be rather slow. So they are not entirely comparable. I am not sure how involved porting deformatrika to Slicer would be, they seem to have a pip package. But then integration still takes time.</p>
<p>If you can share a few samples where things are not working as you expected, we can take a look and see if we can improve things with alpaca.</p>
<p><a class="mention" href="/u/agporto">@agporto</a> <a class="mention" href="/u/smrolfe">@smrolfe</a></p>

---

## Post #8 by @evaherbst (2023-04-21 15:46 UTC)

<p>Thank you so much Murat!</p>
<p>Ah, thanks for clarifying that difference.</p>
<p>Should I email you the meshes?</p>
<p>Thanks again,<br>
Eva</p>

---

## Post #9 by @muratmaga (2023-04-21 16:41 UTC)

<p>email is not the best way. Upload the files somewhere on the cloud and please provide the link here. If you cannot share publicly, you can DM the link (or email).</p>

---

## Post #10 by @smrolfe (2023-04-21 19:27 UTC)

<aside class="quote no-group" data-username="evaherbst" data-post="6" data-topic="28906">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar"> evaherbst:</div>
<blockquote>
<p>However, regardless of alpha and beta values, <strong>the rigidly transformed source mesh and the warped source mesh look like they are mostly translated from each other, and there is very little actually warping/bending going on.</strong></p>
</blockquote>
</aside>
<p>Can you tell me how many landmarks you are transferring? In the screenshot I can only see one. The deformed mesh is an approximation intended to help visualize the performance of the warped transform, using a TPS warping based on the source and transferred landmarks. If you are using a very small number of landmarks this will not provide a good approximation and it is best to rely on the RMSE between landmarks.</p>

---

## Post #11 by @agporto (2023-04-21 21:42 UTC)

<p>Hi Eva,<br>
So cool that you are trying ALPACA on your dataset. Since watching your talk at the FunkyMUG, I thought there was so much potential for an integration between your work and Slicer/SlicerMorph. I want to emphasize Sara’s answer, because I think it is an important aspect that it is not immediately clear from the output. Basically, in order to save the user’s time (since deformations of entire meshes can take quite some time), ALPACA takes a visualization shortcut. It uses the landmark points to calculate a tps transform and applies that transform to the entire mesh. This has one important consequence for its usage. If you want the <em>visual aspect</em> of the deformation to be an accurate description, you need to sample landmarks throughout the structure. For example, you can use the pseudolandmark generator to generate an evenly spaced set of semilandmarks to use during the ALPACA transfer. However, the fact that the visualization doesn’t work with few landmarks does not mean that the deformation was not accurate. I expect given the similarities between your structures that the deformation is quite accurate (what RMSE values are you getting?). You are just not seeing it because of the lack of landmarks being used to estimate the transform. If it is really important for you to get a complete deformation of the mesh, it is somewhat straightforward to modify ALPACA to do it. I am happy to chat about how this can be accomplished using the machinery of the module. However, I don’t think this is something we would want to use as an ALPACA default, since most users just want to quickly get the landmark positions (which was what the module was built for).</p>

---

## Post #12 by @evaherbst (2023-04-24 21:38 UTC)

<p>Hi all,</p>
<p>Thank you so much for clarifying!</p>
<p>So essentially the TPS transform created from the landmarks is for visualization purposes only, but the landmark transfer should be assessed via the RMSE?</p>
<p>I definitely misunderstood this method, I thought the whole mesh deformation was part of the process to transfer the landmarks.</p>
<p><a class="mention" href="/u/agporto">@agporto</a> That’s so nice to hear that you saw my FunkyMUG talk. I switched fields now to work on clinical shoulder biomechanics but still very much interested in optimizing and automating workflows for FE model generation. I just got started with Slicer and am blown away by all of the useful plugins I have found so far.<br>
My current goal is to transfer muscle attachment points from a muskuloskeletal model to other scapulae. Since the muscle attachment points are a bit subjective to place I plan to first use clearer anatomical landmarks to calculate the RMSE and find the best parameters for SlicerMorph, then once I identify these, I want to use them to transfer the muscle attachment points.</p>
<p><em>If it is really important for you to get a complete deformation of the mesh, it is somewhat straightforward to modify ALPACA to do it. I am happy to chat about how this can be accomplished using the machinery of the module.</em><br>
Thank you very much! Do you think this could improve the accuracy of the landmark transfer? (see below).<br>
It could also be very useful for another, more complex case I will have in the future -in our hospital CT scans, the distal humerus is missing, so ideally I would warp the generic model humerus mesh to the partial patient specific humerus (which would require whole mesh warping)</p>
<p>I have now tested the scapular morphing with more landmarks:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12c71f14364ff9bbb7db4c358c7408a8acfcc83e.png" data-download-href="/uploads/short-url/2G7d1DPs05cBM5EmfCu8jfrimom.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12c71f14364ff9bbb7db4c358c7408a8acfcc83e_2_578x500.png" alt="image" data-base62-sha1="2G7d1DPs05cBM5EmfCu8jfrimom" width="578" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12c71f14364ff9bbb7db4c358c7408a8acfcc83e_2_578x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12c71f14364ff9bbb7db4c358c7408a8acfcc83e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12c71f14364ff9bbb7db4c358c7408a8acfcc83e.png 2x" data-dominant-color="B5B7CD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">850×735 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Some of the landmarks transferred quite well (the ones I placed are in green, the ones that are transferred from the source are in pink).</p>
<p>However, some do not transfer well:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b40281d6b22521e3e790d67f791399844bea519f.png" alt="image" data-base62-sha1="pGrjBPIMyNBJlnNLRH22DF8Iz5t" width="335" height="210"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00d1e94cccd094c77e5430b8ac46ac0de65856c3.png" alt="image" data-base62-sha1="7fJrrDJNrGaPy4SRGjSSrOKwPp" width="315" height="155"><br>
This was with alpha and beta at .2 and CPD iterations at 1000.</p>
<p>Alpha and beta at 2 and CPD iterations at 1000 were a bit better (RMSE 0.007362 vs 0.008228), and closer matches, but still failing to identify certain landmarks such as the scapular notch. Note units are in meters - for reference, scapular blade height is about 15 cm).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b16b9948bd2b65d9f4b986513a6b1e64263da6e.png" alt="image" data-base62-sha1="1A5WhJB6AoiEbSUsQXUlscXm6qa" width="407" height="255"></p>
<p>and also showing a noticeable amount of variation near the scapular spine (an area that is important for muscle attachment points):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/747970e4b6576a16cd6c76cdb2cfaa34bbf021f3.jpeg" data-download-href="/uploads/short-url/gCnzvqL6bVnbltKlArKS3qfcezN.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/747970e4b6576a16cd6c76cdb2cfaa34bbf021f3.jpeg" alt="image" data-base62-sha1="gCnzvqL6bVnbltKlArKS3qfcezN" width="566" height="500" data-dominant-color="A4A685"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">586×517 91.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So I guess I should play around with increasing the alpha and beta values, and I will also test the different rigid transform options again tomorrow to see if I can get a better fit.</p>
<p>A quick note:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d147b417a6f751078b190a0212768dcb03edd27.png" alt="image" data-base62-sha1="49fJ8nl8B98B4KVq6hl6EmtvvYb" width="335" height="247"><br>
For this landmark, I think part of it is actually subjectivity in manually finding analogous points (in the source mesh, there are two angular points on the distal scapula, so there could be user disagreement where to place the point). If I had placed the source landmark here instead, that would probably give a better fit. I am just noting it here since I am sharing the files and want to note that maybe that landmark is better left out in future analyses because of lack of clarity in the manual reference landmark placement.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5514060bfaf14aeee6dfbf6ea80efd38bf481b42.png" alt="image" data-base62-sha1="c8Du5RErXp8G0qC18FQmSPLoxuG" width="414" height="332"></p>
<p>I also uploaded the files, they are available here:<br>
<a href="https://drive.google.com/drive/folders/1btfP33YO2Zd7aWBHRFySmuhhYCNGK0FZ?usp=share_link" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1btfP33YO2Zd7aWBHRFySmuhhYCNGK0FZ?usp=share_link</a></p>
<p>I am not sure if I can make it to the office hours tomorrow but I will try to.</p>
<p>Thanks again for your help,<br>
Eva</p>

---

## Post #13 by @muratmaga (2023-04-24 21:51 UTC)

<aside class="quote no-group" data-username="evaherbst" data-post="12" data-topic="28906">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar"> evaherbst:</div>
<blockquote>
<p>I definitely misunderstood this method, I thought the whole mesh deformation was part of the process to transfer the landmarks.</p>
</blockquote>
</aside>
<p>Yes, ALPACA is for transferring landmarks, and the deformation is calculated using reduced point clouds since it is very fast and offers enough accuracy. We will clarify the documentation to explain that visualization is only an approximation and limited to the points selected.</p>
<aside class="quote no-group" data-username="evaherbst" data-post="12" data-topic="28906">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar"> evaherbst:</div>
<blockquote>
<p><em>If it is really important for you to get a complete deformation of the mesh, it is somewhat straightforward to modify ALPACA to do it. I am happy to chat about how this can be accomplished using the machinery of the module.</em></p>
</blockquote>
</aside>
<p>We had been talking about having a separate mesh registration framework build on point clouds, but not sure what the timing of it would be. If <a class="mention" href="/u/agporto">@agporto</a> and you are interested in workign together, we can schedule a meeting.</p>

---

## Post #14 by @evaherbst (2023-04-26 08:47 UTC)

<p>Thank you very much Murat!</p>
<p><em>We had been talking about having a separate mesh registration framework build on point clouds, but not sure what the timing of it would be. If <a class="mention" href="/u/agporto">@agporto</a> and you are interested in working together, we can schedule a meeting.</em><br>
That would be fantastic. I will hopefully be recruiting some students in a few months, so maybe a student could also work with us on this.<br>
Regarding a meeting, should I email or message you?</p>
<p>Thanks again,<br>
Eva</p>

---
