---
topic_id: 25153
title: "Measure Surface Area Of A Trait From The Model"
date: 2022-09-08
url: https://discourse.slicer.org/t/25153
---

# Measure surface area of a trait from the model

**Topic ID**: 25153
**Date**: 2022-09-08
**URL**: https://discourse.slicer.org/t/measure-surface-area-of-a-trait-from-the-model/25153

---

## Post #1 by @sridhar (2022-09-08 12:14 UTC)

<p>Slicer Version: 5-0.2<br>
I am trying to develop a pipeline to measure the eye surface area of butterflies from the entire head segment. Segmenting only the eye surface is extremely difficult, so I am using the following steps. I was hoping I could get some feedback on the pipeline which I am going to adopt for my upcoming project.</p>
<ol>
<li>Imported tiff stacks and segmented the whole out and convert his segment to model (data module → right-click on the segment and export the visible segment to the model)</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53c2beba1a0e1d02cee1e0e7ff4e23186b431676.jpeg" data-download-href="/uploads/short-url/bWYRTKX7cls6KaIvtidl0s2Kb6C.jpeg?dl=1" title="head segmentation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53c2beba1a0e1d02cee1e0e7ff4e23186b431676_2_690x491.jpeg" alt="head segmentation" data-base62-sha1="bWYRTKX7cls6KaIvtidl0s2Kb6C" width="690" height="491" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53c2beba1a0e1d02cee1e0e7ff4e23186b431676_2_690x491.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53c2beba1a0e1d02cee1e0e7ff4e23186b431676_2_1035x736.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53c2beba1a0e1d02cee1e0e7ff4e23186b431676_2_1380x982.jpeg 2x" data-dominant-color="4A4D53"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">head segmentation</span><span class="informations">1920×1368 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol start="2">
<li>Create a close curve from the ‘Markups module’ and place the points to demarcate the outline of the eye. I chose the following options in the curve settings tab (curve type= Spline, constrain to model= model I just created). Also, not sure why the curve in 2D slices looks out of place and if that is a problem.</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/456ff686f5ce5504532cdf82771e4c796b5d8ba7.jpeg" alt="image" data-base62-sha1="9UgP9Az0n0Txbby7q6eP0l4XYTt" width="574" height="408"></p>
<ol start="3">
<li>Chose a curve cut from the ‘Dynamic Modeller’ module. I will then find the surface area of this curve in the ‘Models’ module.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/264cd554fd382b4fcf2971b75f0cfb19b7b29e52.jpeg" data-download-href="/uploads/short-url/5sOL1LkU0cUnULxOouFV5niscJs.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/264cd554fd382b4fcf2971b75f0cfb19b7b29e52_2_690x347.jpeg" alt="image" data-base62-sha1="5sOL1LkU0cUnULxOouFV5niscJs" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/264cd554fd382b4fcf2971b75f0cfb19b7b29e52_2_690x347.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/264cd554fd382b4fcf2971b75f0cfb19b7b29e52.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/264cd554fd382b4fcf2971b75f0cfb19b7b29e52.jpeg 2x" data-dominant-color="9392B5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">750×378 53.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
</ol>
<p>Do these steps make sense? There are a large number of scans that I need to process.  Any input will be extremely helpful. Thank you very much in advance.</p>

---

## Post #2 by @lassoan (2022-09-08 13:06 UTC)

<p>You workflow looks OK, but you can make it a bit simpler and more efficient.</p>
<ul>
<li>You don’t need to use “Markups to model” module. Instead, you can place a closed curve on the surface using Markups module.</li>
<li>You can reduce the number of points that you need to add (from 30-40 to 5-15) if you constrain the curve to the model surface, using Markups module → Curve settings → Constrain to model.</li>
</ul>
<div class="youtube-onebox lazy-video-container" data-video-id="Ai-ICGimai4" data-video-title="Surface segmentation demo" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=Ai-ICGimai4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/Ai-ICGimai4/maxresdefault.jpg" title="Surface segmentation demo" width="" height="">
  </a>
</div>

<ul>
<li>You can further reduce the number of points that you need to add (from 5-15 to 6-8) and make the placement more reproducible by snapping the curve to high-curvature area. You can do that by computing curvature on the model by copy-pasting the code snippet below into the Python console, and then in Markups module → Curve settings → Curve type, choose “Shortest distance on surface” and as cost function select “Inverse squared”. You can add a small constant to the active scalar to make the line a bit smoother (e.g., <code>activeScalar + 0.02</code>).</li>
</ul>
<pre><code class="lang-python">inputModeNode = getNode('Segment_1')
curv=vtk.vtkCurvatures()
curv.SetInputData(inputModelNode.GetPolyData())
slicer.modules.models.logic().AddModel(curv.GetOutputPort())
</code></pre>
<ul>
<li>If you need to process hundreds of data sets then you can further reduce the processing time by writing a few code snippets for automating trivial steps (sementation by thresholding, setting up the curve node, cutting the model using Dynamic modeler, computing surface area, add result to a csv file, save the scene). You can assign shortcuts to run these code snippets or add a module that has a simple GUI to select input and output data sets and parameters. To get started with Python scripting in Slicer you can check out the “SlicerProgramming” <a href="https://github.com/PerkLab/PerkLabBootcamp/tree/master/Doc">PerkLab bootcamp tutorial</a>.</li>
</ul>

---

## Post #3 by @sridhar (2022-09-08 15:34 UTC)

<p>Hi Andras,</p>
<p>Thank you very much for your quick reply and input, this is extremely helpful. I have two quick questions:<br>
(1) I ran the code you provided, and what I got is this new model (image below). I am a bit confused at this step. So should I first run the code and then place the curve on this model choosing the curve settings you mentioned? Or should I place the curve first? Also, when I place the curve and choose these settings (curve type → shortest distance on surface, constrain to model → this new model I just got after running the code, cost function → inverse squared), the outline of the curve spill over the demarcated boundary. Not sure why happens.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/787c959dacb88440d3533a297a5ebc634aa208c4.jpeg" data-download-href="/uploads/short-url/hbSdtBCDGontJyG5hqIZ9icI6UY.jpeg?dl=1" title="New model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/787c959dacb88440d3533a297a5ebc634aa208c4_2_690x465.jpeg" alt="New model" data-base62-sha1="hbSdtBCDGontJyG5hqIZ9icI6UY" width="690" height="465" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/787c959dacb88440d3533a297a5ebc634aa208c4_2_690x465.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/787c959dacb88440d3533a297a5ebc634aa208c4_2_1035x697.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/787c959dacb88440d3533a297a5ebc634aa208c4_2_1380x930.jpeg 2x" data-dominant-color="75689F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">New model</span><span class="informations">1920×1295 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/133d3e4071aa70dceea5a9492bc8e33b144fec17.jpeg" data-download-href="/uploads/short-url/2KchESe2cZulUD2G23sKb7TxD0P.jpeg?dl=1" title="placing curve_inverse quared" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/133d3e4071aa70dceea5a9492bc8e33b144fec17_2_690x465.jpeg" alt="placing curve_inverse quared" data-base62-sha1="2KchESe2cZulUD2G23sKb7TxD0P" width="690" height="465" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/133d3e4071aa70dceea5a9492bc8e33b144fec17_2_690x465.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/133d3e4071aa70dceea5a9492bc8e33b144fec17_2_1035x697.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/133d3e4071aa70dceea5a9492bc8e33b144fec17_2_1380x930.jpeg 2x" data-dominant-color="573F76"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">placing curve_inverse quared</span><span class="informations">1920×1295 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>(2) Will the measurements differ if I use curve type →  spline &amp; curve type → shortest distance on the surface? However, I must admit that I am trying to understand what these different curve types actually mean and when one should use a particular curve type.</p>
<p>Thank you very much again.<br>
Sridhar</p>

---

## Post #4 by @lassoan (2022-09-08 15:42 UTC)

<aside class="quote no-group" data-username="sridhar" data-post="3" data-topic="25153">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9fc29f/48.png" class="avatar"> sridhar:</div>
<blockquote>
<p>this new model I just got after running the code, cost function → inverse squared), the outline of the curve spill over the demarcated boundary. Not sure why happens.</p>
</blockquote>
</aside>
<p>This is normal, it is because the path search between control points is too much controlled by the (always noisy) curvature computation result. Changing <code>activeScalar</code> to <code>activeScalar + 0.02</code> (or another small constant) will dampen the effect of the curvature. You can also add more control points if the path found between the points is not exactly where you want it (you can add more points on the curve by Ctrl + Left-click).</p>
<aside class="quote no-group" data-username="sridhar" data-post="3" data-topic="25153">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9fc29f/48.png" class="avatar"> sridhar:</div>
<blockquote>
<p>Will the measurements differ if I use curve type → spline &amp; curve type → shortest distance on the surface? However, I must admit that I am trying to understand what these different curve types actually mean and when one should use a particular curve type.</p>
</blockquote>
</aside>
<p>The length is always the length of the curve that you see. If the curve looks good then the measurement is good. I noticed that you placed the control points far away from the edge of the eye, which is not good. You still need to place the control points accurately, by making the path search between control points prefer high-curvature areas we just reduce the number of control points that are needed to guide the curve.</p>

---

## Post #5 by @sridhar (2022-09-08 16:43 UTC)

<p>Hi Andras,</p>
<p>Now it’s perfectly clear! I just ran the entire workflow again and just adding +0.02 to activeScalar makes the curve much smoother. I believe after processing scans, I’ll get a good idea of how many control points are adequate.</p>
<p>If I may just ask another question related to this topic (or I can create a new topic), how can I export the curve cut (which I obtained from Dynamic Modeller) as a high-resolution label? Now I simply created the label from the curve cut by right-clicking on this model (i.e. curve cut) and clicking on covert to segmentation label. However, it is clearly visible that the edges of the curve cut look quite jagged/pixelated. So I was wondering if there is a good way to export it as a high-resolution label (we may possibly use these labels as a training dataset for giving a shot at deep learning).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/973eea741f89a2dc3ca4484e2889edbd7fd667f5.jpeg" data-download-href="/uploads/short-url/lzYTsOa6V4SPOgYXF9oOqesRbVz.jpeg?dl=1" title="curve cut to segmentation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/973eea741f89a2dc3ca4484e2889edbd7fd667f5_2_690x363.jpeg" alt="curve cut to segmentation" data-base62-sha1="lzYTsOa6V4SPOgYXF9oOqesRbVz" width="690" height="363" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/973eea741f89a2dc3ca4484e2889edbd7fd667f5_2_690x363.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/973eea741f89a2dc3ca4484e2889edbd7fd667f5_2_1035x544.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/973eea741f89a2dc3ca4484e2889edbd7fd667f5_2_1380x726.jpeg 2x" data-dominant-color="49484D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">curve cut to segmentation</span><span class="informations">1920×1012 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks very much for your input! This has been really helpful.<br>
Sridhar</p>

---

## Post #6 by @muratmaga (2022-09-08 19:10 UTC)

<aside class="quote no-group" data-username="sridhar" data-post="5" data-topic="25153">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9fc29f/48.png" class="avatar"> sridhar:</div>
<blockquote>
<p>how can I export the curve cut (which I obtained from Dynamic Modeller) as a high-resolution label?</p>
</blockquote>
</aside>
<p>in Data module right click on the cut model and choose convert to Segmentation. Then after the conversion completed you can right click on the segmentation object and choose to export as a label map.</p>

---

## Post #7 by @sridhar (2022-09-09 07:36 UTC)

<p>Hi Murat,</p>
<p>Thanks for the reply! So I believe this is the only way to export the ‘cut model’ as a label map. The only slight issue is that when this label map is superimposed on the original scan, the edges look a bit jagged (example below). Can the edges of the label map be smoothened out perhaps by adding (resampling) more control points? I am trying to reduce this noise as much as possible.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c17e69b3a8e6313d70e8ab4480065bf82e480e9.png" data-download-href="/uploads/short-url/aR9uGLaZsjl1GrYYirQdqvn2bWN.png?dl=1" title="model to label map" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c17e69b3a8e6313d70e8ab4480065bf82e480e9_2_690x399.png" alt="model to label map" data-base62-sha1="aR9uGLaZsjl1GrYYirQdqvn2bWN" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c17e69b3a8e6313d70e8ab4480065bf82e480e9_2_690x399.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c17e69b3a8e6313d70e8ab4480065bf82e480e9_2_1035x598.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c17e69b3a8e6313d70e8ab4480065bf82e480e9_2_1380x798.png 2x" data-dominant-color="393231"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">model to label map</span><span class="informations">3336×1932 499 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you,<br>
Sridhar</p>

---

## Post #8 by @muratmaga (2022-09-10 03:30 UTC)

<aside class="quote no-group" data-username="sridhar" data-post="7" data-topic="25153">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9fc29f/48.png" class="avatar"> sridhar:</div>
<blockquote>
<p>the edges look a bit jagged (example below)</p>
</blockquote>
</aside>
<p>you can try that. Also check the geometry of the labelmap. If it is not very high, you can try to use the segmentation module and control the resolution of the created segmentation during the model to segmentation conversion (as I recall).</p>

---

## Post #9 by @lassoan (2022-09-10 12:07 UTC)

<p>I’ve been following your Japanese translation updates. Thanks for your fantastic work.</p>
<p>Thanks a lot for your</p>
<aside class="quote no-group" data-username="sridhar" data-post="5" data-topic="25153">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9fc29f/48.png" class="avatar"> sridhar:</div>
<blockquote>
<p>If I may just ask another question related to this topic (or I can create a new topic), how can I export the curve cut (which I obtained from Dynamic Modeller) as a high-resolution label?</p>
</blockquote>
</aside>
<p>Surface mesh segmentation (what I described, using Dynamic modeler) and image segmentation are two entirely different problems. If you want to label the CT image then specifying the outer surface of the eye is mostly useless.</p>
<p>If you want to do image segmentation then I would recommend to use Segment Editor to generate ground truth and MONAILabel to train a network.</p>
<p>If you want to segment surface meshes the you can use the workflow discussed above and experiment with <a href="https://link.springer.com/article/10.1007/s40304-021-00246-7">networks specifically designed for mesh processing</a>.</p>

---

## Post #10 by @sridhar (2022-09-12 07:24 UTC)

<p>Thanks very much for the inputs (and you and your colleagues for developing SlicerMorph)! I shall give this a try.</p>

---

## Post #11 by @sridhar (2022-09-12 08:11 UTC)

<p>Hi Andras,<br>
Thank you very much for your quick replies and input! I now have a good workflow to get the measurements out. This forum is just fantastic!<br>
Best,<br>
Sridhar</p>

---
