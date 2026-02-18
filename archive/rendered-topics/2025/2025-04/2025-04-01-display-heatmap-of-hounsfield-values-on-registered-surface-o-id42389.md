# Display heatmap of Hounsfield values on registered surface object for cortical bone contact

**Topic ID**: 42389
**Date**: 2025-04-01
**URL**: https://discourse.slicer.org/t/display-heatmap-of-hounsfield-values-on-registered-surface-object-for-cortical-bone-contact/42389

---

## Post #1 by @LindenRB (2025-04-01 06:35 UTC)

<p>Hi all,</p>
<p>I’m looking at a project to map the intensity (in HU) of a CT scan where it contacts a registered surface (STL) model, so I can quantify the cortical vs cancellous bone contact zones in different regions along a THA stem. I would be looking to produce something like the attached image, which I can then break into particular zones of interest (Gruen zones).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e0704888f12cd665ae5245d7c1d6dd0eb343e65.png" data-download-href="/uploads/short-url/6zaZWcAIUruC4F94MACMHXotRn7.png?dl=1" title="Five-patterns-of-cortical-contact" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e0704888f12cd665ae5245d7c1d6dd0eb343e65_2_690x300.png" alt="Five-patterns-of-cortical-contact" data-base62-sha1="6zaZWcAIUruC4F94MACMHXotRn7" width="690" height="300" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e0704888f12cd665ae5245d7c1d6dd0eb343e65_2_690x300.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e0704888f12cd665ae5245d7c1d6dd0eb343e65.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e0704888f12cd665ae5245d7c1d6dd0eb343e65.png 2x" data-dominant-color="37422C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Five-patterns-of-cortical-contact</span><span class="informations">850×370 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Source DOI: <a href="https://link.springer.com/article/10.1007%2Fs00402-021-04273-5" rel="noopener nofollow ugc">10.1007%2Fs00402-021-04273-5</a></p>
<p>Before I go re-inventing the wheel, I thought I would see if anyone is aware of any open source extension or feature which already achieves this goal. From some preliminary searching, I believe the Pedicle Screw Simulator extension that Andrew Lasso has mentioned in this forum several times may already be doing the a lot of what I want to do:<br>
<a href="https://discourse.slicer.org/t/how-to-measure-the-boundary-ct-value-of-a-circular-section/27104">https://discourse.slicer.org/t/how-to-measure-the-boundary-ct-value-of-a-circular-section/27104</a><br>
<a href="https://github.com/lassoan/PedicleScrewSimulator/blob/master/PedicleScrewPlanner/PedicleScrewPlannerWizard/PlanningGradeStep.py" rel="noopener nofollow ugc">https://github.com/lassoan/PedicleScrewSimulator/blob/master/PedicleScrewPlanner/PedicleScrewPlannerWizard/PlanningGradeStep.py</a></p>
<p>As a rough approach I’d be planning to try and measure the Hounsfield units of the nearest voxel to each vertex on my surface model (after remeshing to create a more uniform mesh size), and break these into specific regions of interest. Planned outputs would be to visually display a heatmap across the surface of the STL model, and to measure the min/max/avg etc. HU values across regions of vertices.</p>
<p>Mostly just hoping to get feedback whether:<br>
A) This has already been done, and there’s already some sort of extension available<br>
B) If not, whether it’s feasible and a reasonably achievable goal for someone with some (but not extensive) experience coding in Slicer<br>
C) If there are any existing extensions or functions that would give me access to vertex points on a registered surface model, and allow me to then probe the nearest voxel for its intensity (HU) values</p>
<p>Cheers,<br>
Linden</p>

---

## Post #2 by @Heiko_Stark (2025-04-01 07:34 UTC)

<p>Dear Linden,</p>
<p>unfortunately I don’t know it for 3D Slicer, but it should work with my free tool:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://stark-jena.de/research-interests/software/imagexd/mesh-measurement-imagexd/">
  <header class="source">
      <img src="https://stark-jena.de/wp-content/uploads/cropped-back-icon-32x32.png" class="site-icon" width="32" height="32">

      <a href="https://stark-jena.de/research-interests/software/imagexd/mesh-measurement-imagexd/" target="_blank" rel="noopener nofollow ugc">stark-jena.de</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://stark-jena.de/research-interests/software/imagexd/mesh-measurement-imagexd/" target="_blank" rel="noopener nofollow ugc">Star k ratS	
   »   Biopsie measurement (ImageXd)</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Best regards,<br>
Heiko</p>

---

## Post #3 by @pieper (2025-04-01 13:10 UTC)

<p><a class="mention" href="/u/lindenrb">@LindenRB</a> an option would be to convert the stl to a segmentation, use the margin effect to grow it by some amount, convert the grown segment to a model, and then use the probe volume with model module to get a scalar field of the CT values per vertex.</p>

---

## Post #4 by @LindenRB (2025-04-08 05:27 UTC)

<p>Many thanks for your reply Heiko, I will look into your ImageXd tool</p>

---

## Post #5 by @LindenRB (2025-04-08 05:27 UTC)

<p>Man thanks Steve, I will give this approach a try and see how it goes, appreciate the help!</p>

---

## Post #6 by @lassoan (2025-04-08 15:08 UTC)

<blockquote>
<p>This has already been done, and there’s already some sort of extension available</p>
</blockquote>
<p>Yes, the Pedicle Screw Simulator extension does exactly this:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="XN3Tp8jaYdQ" data-video-title="3D Slicer - Pedicle Screw Surgical Simulator" data-video-start-time="121" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=XN3Tp8jaYdQ&amp;t=121" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/XN3Tp8jaYdQ/maxresdefault.jpg" title="3D Slicer - Pedicle Screw Surgical Simulator" width="690" height="388">
  </a>
</div>

<p>I don’t think you need to use this extension for your project, because your models are different, you position them differently (in current Slicer versions it is very easy to position models using <a href="https://discourse.slicer.org/t/new-feature-interactive-transformation-adjustable-center-of-rotation/36974">interactive transformation handles</a>) and it takes just a few clicks to copy CT values to the model points.</p>
<blockquote>
<p>If not, whether it’s feasible and a reasonably achievable goal for someone with some (but not extensive) experience coding in Slicer</p>
</blockquote>
<p>You don’t need any coding to get started. If you want to streamline the processing (minimize number of clicks) or fully automate it then you can do that with Python scripting. If you have specific questions you can ask questions here, or for getting more substantial help or developing complete solutions you can contact <a href="https://www.slicer.org/commercial-use.html#commercial-partners">Slicer Commercial Partners</a>.</p>
<blockquote>
<p>If there are any existing extensions or functions that would give me access to vertex points on a registered surface model, and allow me to then probe the nearest voxel for its intensity (HU) values</p>
</blockquote>
<p><code>Probe volume with model</code> module does exactly this.</p>

---

## Post #7 by @LindenRB (2025-04-11 08:03 UTC)

<p>Thank you so much for the reply Andras!</p>
<p>I’ve already created a few basic scripts and extensions for Slicer and really enjoy the process of scripting and GUI design within slicer, so I think I’ll have a go at building something myself for this. Appreciate your help and the resources you have provided!</p>
<p>Having a quick play around with the Probe volume with model is showing me exactly what I’d like to see (stem placed poorly deliberately to see cortical bone contrast)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5ba47ede060bec3926e55f5387a992c6c1c57ec3.jpeg" data-download-href="/uploads/short-url/d4HSyy3i8XmqOSZPs54dN9CoqgX.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5ba47ede060bec3926e55f5387a992c6c1c57ec3.jpeg" alt="image" data-base62-sha1="d4HSyy3i8XmqOSZPs54dN9CoqgX" width="690" height="428" data-dominant-color="9497C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1039×645 28.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you know if its easy to export something like a point map of the intensity values at each vertex to CSV or similar? If not I will go digging in the module code for the Probe model tool</p>
<p>Again much appreciate the help!</p>

---

## Post #8 by @lassoan (2025-04-11 17:19 UTC)

<aside class="quote no-group" data-username="LindenRB" data-post="7" data-topic="42389">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lindenrb/48/76674_2.png" class="avatar"> LindenRB:</div>
<blockquote>
<p>Do you know if its easy to export something like a point map of the intensity values at each vertex to CSV or similar?</p>
</blockquote>
</aside>
<p>Yes, it is a single command to get all point scalars as a numpy array, and another single command is to write to csv.</p>
<p>One important thing is that your model seem to have highly irregular triangles. For quantitative analysis, you probably want to have points distributed evenly on the whole implant surface. To achieve that, you can use the Surface Toolbox module’s uniform resampling tool.</p>

---

## Post #9 by @LindenRB (2025-04-14 02:19 UTC)

<p>Many thanks once again Andras!</p>
<p>Yes the stem models we have come out of Solidworks with highly non-uniform mesh geometry (apparently optimised…), was planning to remesh the models to something much more uniform before import, but if that can be done natively within slicer that makes my life even easier!</p>

---
