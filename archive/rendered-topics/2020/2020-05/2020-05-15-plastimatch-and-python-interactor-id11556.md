---
topic_id: 11556
title: "Plastimatch And Python Interactor"
date: 2020-05-15
url: https://discourse.slicer.org/t/11556
---

# Plastimatch and Python Interactor

**Topic ID**: 11556
**Date**: 2020-05-15
**URL**: https://discourse.slicer.org/t/plastimatch-and-python-interactor/11556

---

## Post #1 by @user1 (2020-05-15 13:47 UTC)

<p>Hello Community,</p>
<p>I have a (maybe easy) basic question to the Python Interactor in 3D Slicer/ SlicerRT. I want to know, which kind of the average Hausdorff-Distance the SlicerRT extension calculate (e.g. directed average or undirected average or undirected max average Hausdorff-distance).<br>
Therefore I try to calculate the HD with the Python Interactor in 3D Slicer with the commands of Plastimatch (and compare with my manual calculation), but it doesn’t work. May somebody show me, how can I use the Plastimatch-commands in the Interactor (e.g. get_avg_average_hausdorff)?</p>
<p>Thank you very much!</p>

---

## Post #2 by @gcsharp (2020-05-15 14:32 UTC)

<p>Unfortunately you can’t call plastimatch functions from python.  Those functions are not python wrapped.  But you can see which functions are called here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkSlicerSegmentComparisonModuleLogic.cxx#L471" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkSlicerSegmentComparisonModuleLogic.cxx#L471" target="_blank" rel="nofollow noopener">SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkSlicerSegmentComparisonModuleLogic.cxx#L471</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="461" style="counter-reset: li-counter 460 ;">
<li>// Compute Hausdorff distances
</li>
<li>double checkpointHausdorffStart = timer-&gt;GetUniversalTime();
</li>
<li>UNUSED_VARIABLE(checkpointHausdorffStart); // Although it is used later, a warning is logged so needs to be suppressed
</li>
<li>Hausdorff_distance hausdorff;
</li>
<li>hausdorff.set_reference_image(plmRefSegmentLabelmap-&gt;itk_uchar());
</li>
<li>hausdorff.set_compare_image(plmCmpSegmentLabelmap-&gt;itk_uchar());
</li>
<li>hausdorff.set_volume_boundary_behavior(ZERO_PADDING);
</li>
<li>hausdorff.run();
</li>
<li>
</li>
<li>double maximumHausdorffDistanceForBoundaryMm = hausdorff.get_boundary_hausdorff();
</li>
<li class="selected">double averageHausdorffDistanceForBoundaryMm = hausdorff.get_avg_average_boundary_hausdorff();
</li>
<li>double percent95HausdorffDistanceForBoundaryMm = hausdorff.get_percent_boundary_hausdorff();
</li>
<li>parameterNode-&gt;SetMaximumHausdorffDistanceForVolumeMm(hausdorff.get_hausdorff());
</li>
<li>parameterNode-&gt;SetMaximumHausdorffDistanceForBoundaryMm(maximumHausdorffDistanceForBoundaryMm);
</li>
<li>parameterNode-&gt;SetAverageHausdorffDistanceForVolumeMm(hausdorff.get_avg_average_hausdorff());
</li>
<li>parameterNode-&gt;SetAverageHausdorffDistanceForBoundaryMm(averageHausdorffDistanceForBoundaryMm);
</li>
<li>parameterNode-&gt;SetPercent95HausdorffDistanceForVolumeMm(hausdorff.get_percent_hausdorff());
</li>
<li>parameterNode-&gt;SetPercent95HausdorffDistanceForBoundaryMm(percent95HausdorffDistanceForBoundaryMm);
</li>
<li>parameterNode-&gt;HausdorffResultsValidOn();
</li>
<li>
</li>
<li>// Set results to table node
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @user1 (2020-05-15 15:01 UTC)

<p>Thanks for the quick answer.</p>
<p>So did I understood it right, that the average HD in Slicer represent the sum of all minimum distances from the <strong>external contour</strong>-pixels/ voxels of one contour/ segment to the pixel/ voxel of the external border of the other contour divided by the number of pixels from the <strong>first</strong> contour (or sum of all pixels of both contours?)? = directed average HD<br>
After that the same steps are repeated for the other contour and the sum of both (directed) distances divided by 2 or did Slicer take the maximum of the two directed distances? = undirected average HD</p>
<p>Thanks in advance!</p>

---

## Post #4 by @gcsharp (2020-05-15 19:45 UTC)

<p>It works like this:</p>
<ol>
<li>For each boundary point of the compare image, find the closest boundary point on the reference image.  Then take the average of these distances.</li>
<li>For each boundary point of the reference image, find the closest boundary point on the compare image.  Then take the average of these distances.</li>
<li>Take the average of the numbers computed in step 1 and step 2.</li>
</ol>

---

## Post #5 by @lassoan (2020-05-16 04:26 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="2" data-topic="11556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>Unfortunately you can’t call plastimatch functions from python</p>
</blockquote>
</aside>
<p>All computations that Slicer can perform are accessible from Python, too.</p>
<p>For example, you can compute metric by calling <a href="https://github.com/SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkSlicerSegmentComparisonModuleLogic.h#L48-L54">SegmentComparison module logic</a> and retrieve results from the associated <a href="https://github.com/SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkMRMLSegmentComparisonNode.h">vtkMRMLSegmentComparisonNode</a>.</p>

---

## Post #6 by @user1 (2020-05-16 08:07 UTC)

<p>Thanks for the information.</p>
<p>Unfortunately I can’t call these SegmentComparison module logic’s (“std::string ComputeHausdorffDistances(vtkMRMLSegmentComparisonNode* parameterNode);”) in the Python-Interactor. First I included the “slicer includes”, after that I created a segmentation from a LabelMap-volume (created in segmentations-module) as you showed in a thread before: “<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_segmentation_from_a_labelmap_volume_and_display_in_3D" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_segmentation_from_a_labelmap_volume_and_display_in_3D</a>” (is the “parameterNode” == this segmentation?).</p>
<p>May you can give me an example how I can input the syntax for this, please?</p>
<p>Thank you!</p>

---

## Post #7 by @cpinter (2020-05-17 10:26 UTC)

<p>Please note the signature of the function. It takes a vtkMRMLSegmentComparisonNode, which is a parameter set node containing the parameters of a segment comparison run. Now if you look at this class<br>
</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkMRMLSegmentComparisonNode.h#L58-L176" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkMRMLSegmentComparisonNode.h#L58-L176" target="_blank">SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkMRMLSegmentComparisonNode.h#L58-L176</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="58" style="counter-reset: li-counter 57 ;">
<li>/// Get reference segmentation node
</li>
<li>vtkMRMLSegmentationNode* GetReferenceSegmentationNode();
</li>
<li>/// Set reference segmentation node
</li>
<li>void SetAndObserveReferenceSegmentationNode(vtkMRMLSegmentationNode* node);
</li>
<li>
</li>
<li>/// Get compare segmentation node
</li>
<li>vtkMRMLSegmentationNode* GetCompareSegmentationNode();
</li>
<li>/// Set compare segmentation node
</li>
<li>void SetAndObserveCompareSegmentationNode(vtkMRMLSegmentationNode* node);
</li>
<li>
</li>
<li>/// Get rasterization reference volume node
</li>
<li>vtkMRMLScalarVolumeNode* GetRasterizationReferenceVolumeNode();
</li>
<li>/// Set rasterization reference volume node
</li>
<li>void SetAndObserveRasterizationReferenceVolumeNode(vtkMRMLScalarVolumeNode* node);
</li>
<li>
</li>
<li>/// Get Dice table node
</li>
<li>vtkMRMLTableNode* GetDiceTableNode();
</li>
<li>/// Set Dice table node
</li>
<li>void SetAndObserveDiceTableNode(vtkMRMLTableNode* node);
</li>
<li>
</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkMRMLSegmentComparisonNode.h#L58-L176" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
then you’ll see what inputs you can set to it and what outputs you gan get after the calculation.

---

## Post #8 by @user1 (2020-05-19 12:25 UTC)

<p>Thanks for the help! Sorry, that I have to ask again to this…</p>
<p>First, I get every time an error message, when I want to get my reference segmentation node (segmentation* GetReferenceSegmentationNode();). Do I understood it right, that my “vtkMRMLSegmentationNode” = my active Segmentation (which contains the two segments for calculation of Hausdorff/ Dice…)?<br>
Furthermore I get the error message, that the name “SetAndObserveReferenceSegmentationNode” is not  defined, when I want to set my reference segmentation node…</p>
<p>May you show me my mistake or are there any special packages necessary, which I have to include/ install/ import?</p>

---

## Post #9 by @cpinter (2020-05-19 13:07 UTC)

<p>This function from an actual working module should help:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SegmentRegistration/blob/master/ProstateMRIUSContourPropagation/ProstateMRIUSContourPropagation.py#L1085-L1126" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SegmentRegistration/blob/master/ProstateMRIUSContourPropagation/ProstateMRIUSContourPropagation.py#L1085-L1126" target="_blank">SlicerRt/SegmentRegistration/blob/master/ProstateMRIUSContourPropagation/ProstateMRIUSContourPropagation.py#L1085-L1126</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="1085" style="counter-reset: li-counter 1084 ;">
<li>def calculateSegmentSimilarity(self):
</li>
<li>  logging.info('Calculating prostate similarity')
</li>
<li>  if self.usSegmentationNode is None or self.mrSegmentationNode is None:
</li>
<li>    logging.error('Failed to get segmentations')
</li>
<li>    return False
</li>
<li>
</li>
<li>  # Calculate Dice, Hausdorff
</li>
<li>  if self.segmentComparisonNode is None or self.segmentComparisonNode.GetScene() is None:
</li>
<li>    self.segmentComparisonNode = slicer.vtkMRMLSegmentComparisonNode()
</li>
<li>    self.segmentComparisonNode.SetName(slicer.mrmlScene.GenerateUniqueName('MRI-US_SegmentComparison'))
</li>
<li>    slicer.mrmlScene.AddNode(self.segmentComparisonNode)
</li>
<li>  if self.diceTableNode is None:
</li>
<li>    self.diceTableNode = slicer.vtkMRMLTableNode()
</li>
<li>    self.diceTableNode.SetName('Dice comparison results table')
</li>
<li>    slicer.mrmlScene.AddNode(self.diceTableNode)
</li>
<li>  if self.hausdorffTableNode is None:
</li>
<li>    self.hausdorffTableNode = slicer.vtkMRMLTableNode()
</li>
<li>    self.hausdorffTableNode.SetName('Hausdorff comparison results table')
</li>
<li>    slicer.mrmlScene.AddNode(self.hausdorffTableNode)
</li>
<li>  self.segmentComparisonNode.SetAndObserveDiceTableNode(self.diceTableNode)
</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/SlicerRt/SegmentRegistration/blob/master/ProstateMRIUSContourPropagation/ProstateMRIUSContourPropagation.py#L1085-L1126" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #10 by @user1 (2020-05-19 15:57 UTC)

<p>OK, I think I got it, thank you very much!</p>
<p>I just have one more question to the segmentation node. May you explain me, what the “usSegmentationNode” or “mrSegmentationNode” is in your code:<br>
self.segmentComparisonNode.SetAndObserveReferenceSegmentationNode(self.usSegmentationNode)<br>
I thought this are the segments in the active segmentation…</p>

---

## Post #11 by @cpinter (2020-05-20 09:21 UTC)

<p>This particular module compares segments from two different segmentations, one done on ultrasound (US) and the other on MR.</p>

---

## Post #12 by @user1 (2020-05-20 09:41 UTC)

<p>ok, I mean what is the input of this module.<br>
So how I get a “usSegmentationNode” and a “mrSegmentationNode”?<br>
Do I need two different segmentations or is it enough to have two segments to compare in one segmentation?</p>

---

## Post #13 by @cpinter (2020-05-20 10:09 UTC)

<p>You can find information about this module here</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerRt/SegmentRegistration">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerRt/SegmentRegistration" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/d59aea3b2e136dd0ea7910870d2d99a1c2387b6f629ff2952c0be55b41b16d5a/SlicerRt/SegmentRegistration" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerRt/SegmentRegistration" target="_blank" rel="noopener">GitHub - SlicerRt/SegmentRegistration: 3D Slicer extension for segment...</a></h3>

  <p>3D Slicer extension for segment registration (aka fusion, contour propagation) - GitHub - SlicerRt/SegmentRegistration: 3D Slicer extension for segment registration (aka fusion, contour propagation)</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
There is a tutorial as well that shows you how it is used.</p>
<aside class="quote no-group" data-username="user1" data-post="12" data-topic="11556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/u/5daacb/48.png" class="avatar"> user1:</div>
<blockquote>
<p>Do I need two different segmentations or is it enough to have two segments to compare in one segmentation?</p>
</blockquote>
</aside>
<p>You can compare any two segments.</p>

---

## Post #14 by @user1 (2020-05-20 12:21 UTC)

<p>Ah ok it is this module. Is there any way to compute the Hausdorff-distances with the “Segment Comparison” - module in the python interactor as you can see here:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f4d4f3e4840ae9bd2f9933bf17f7c007d8696fce.png" data-download-href="/uploads/short-url/yVSKC8Cb6xDX5Le7MjwUijCEIVg.png?dl=1" title="Bildschirmfoto 2020-05-20 um 14.11.04" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4d4f3e4840ae9bd2f9933bf17f7c007d8696fce_2_690x389.png" alt="Bildschirmfoto 2020-05-20 um 14.11.04" data-base62-sha1="yVSKC8Cb6xDX5Le7MjwUijCEIVg" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4d4f3e4840ae9bd2f9933bf17f7c007d8696fce_2_690x389.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4d4f3e4840ae9bd2f9933bf17f7c007d8696fce_2_1035x583.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4d4f3e4840ae9bd2f9933bf17f7c007d8696fce_2_1380x778.png 2x" data-dominant-color="DBDAD8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2020-05-20 um 14.11.04</span><span class="informations">1682×950 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I want to calculate the Hausdorff-distances for volume and not for boundary which is the default one in SlicerRT (in my example segment it would be probably the same as boundary HD, but I want to use the volume HD for an other case). Therefore I tried to do this with the python-interactor…</p>

---

## Post #15 by @cpinter (2020-05-20 12:55 UTC)

<p>You have all the information for this above. Please take a look at the settings vtkMRMLSegmentComparisonNode offers.</p>

---

## Post #16 by @lassoan (2020-05-20 14:12 UTC)

<aside class="quote no-group" data-username="user1" data-post="14" data-topic="11556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/u/5daacb/48.png" class="avatar"> user1:</div>
<blockquote>
<p>I want to calculate the Hausdorff-distances for volume and not for boundary</p>
</blockquote>
</aside>
<p>By definition, Hausdorff distance is between boundary surfaces, so you have to provide them as inputs. Even if you think that the boundary is a trivial one, such as bone surface or skin surface, you still need to specify it (for example, by creating a segment with thresholding).</p>

---

## Post #17 by @gcsharp (2020-05-20 16:16 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="16" data-topic="11556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>By definition, Hausdorff distance is between boundary surfaces</p>
</blockquote>
</aside>
<p>As I understand, Hausdorff distance is defined between two sets.  Surface boundary is most common, but it is not the only choice.</p>

---

## Post #18 by @Spiros_Karkavitsas (2023-02-24 14:23 UTC)

<p>Hello everyone</p>
<p>I came across your discussion since I have a relative easy question to ask: I dowloaded the Plastimatch in 3D slicer and I would like to ask how I can use it to compare segmentations using the mean surface distance ?</p>
<p>I was trying to find a script online but I could not find any script which I can trust totally…</p>
<p>Thank you for your time reading my message:)</p>

---

## Post #19 by @cpinter (2023-02-24 15:18 UTC)

<aside class="quote no-group" data-username="Spiros_Karkavitsas" data-post="18" data-topic="11556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/spiros_karkavitsas/48/18224_2.png" class="avatar"> Spiros_Karkavitsas:</div>
<blockquote>
<p>dowloaded the Plastimatch in 3D slicer</p>
</blockquote>
</aside>
<p>I assume this means that you installed the SlicerRT extension. I suggest you use the Segment Comparison module and use the mean Hausdorff metric to achieve the same result.</p>

---

## Post #20 by @Spiros_Karkavitsas (2023-02-24 15:40 UTC)

<p>Hello and thanks for your answer.</p>
<p>As you said,yes I installed the extension in Slicer.</p>
<p>So regarding your answer, why the mean Hausdorff distance is the same as the mean surface distance ? The answer might be obvious but since I have not searched it yet,that is why I am asking.<img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=12" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:" loading="lazy" width="20" height="20"></p>
<p>Στις Παρ, 24 Φεβ 2023, 16:18 ο χρήστης Csaba Pinter via 3D Slicer Community &lt;<a href="mailto:notifications@slicer.discoursemail.com">notifications@slicer.discoursemail.com</a>&gt; έγραψε:</p>

---

## Post #21 by @cpinter (2023-02-24 15:51 UTC)

<aside class="quote no-group" data-username="Spiros_Karkavitsas" data-post="20" data-topic="11556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/spiros_karkavitsas/48/18224_2.png" class="avatar"> Spiros_Karkavitsas:</div>
<blockquote>
<p>since I have not searched it yet</p>
</blockquote>
</aside>
<p>Please do, and ask if something is not clear.</p>

---

## Post #22 by @gcsharp (2023-02-24 20:37 UTC)

<p>Hi <a class="mention" href="/u/spiros_karkavitsas">@Spiros_Karkavitsas</a>.  The terminology “mean Hausdorff” was created many years ago, before “mean surface distance” became the standard.  Sorry for the confusion.</p>

---

## Post #23 by @Spiros_Karkavitsas (2023-02-24 21:05 UTC)

<p>Hey and thanks for the clarification <img src="https://emoji.discourse-cdn.com/twitter/smiling_face.png?v=12" title=":smiling_face:" class="emoji" alt=":smiling_face:" loading="lazy" width="20" height="20"></p>
<p>Actually,I did searched it and mean surface distance and mean Hausdorff distance seems to be indentical. Am I correct or not ?</p>
<p>Στις Παρ, 24 Φεβ 2023, 21:37 ο χρήστης Greg Sharp via 3D Slicer Community &lt;<a href="mailto:notifications@slicer.discoursemail.com">notifications@slicer.discoursemail.com</a>&gt; έγραψε:</p>

---

## Post #24 by @gcsharp (2023-02-24 21:50 UTC)

<p>There are literally (no kidding) more than 30 definitions of “mean surface distance”.  You need to look at the mathematical definition.</p>
<p>Let me see if I can find it, there was a recent article which did a good job summarizing the current state.  The basic idea is that comparing your result to literature is a mess.  But any of them can be used as a relative comparison.</p>

---

## Post #25 by @gcsharp (2023-02-24 22:10 UTC)

<p>Check out Vrtovec 2020 and Sherer 2021.  You may take a look at my AAPM 2022 slides as well.</p>
<aside class="onebox pdf" data-onebox-src="https://www.dropbox.com/s/f3qwpjgpw1pzkyh/2022-aapm.pdf">
  <header class="source">

      <a href="https://www.dropbox.com/s/f3qwpjgpw1pzkyh/2022-aapm.pdf" target="_blank" rel="noopener nofollow ugc">dropbox.com</a>
  </header>

  <article class="onebox-body">
    <a href="https://www.dropbox.com/s/f3qwpjgpw1pzkyh/2022-aapm.pdf" target="_blank" rel="noopener nofollow ugc"><span class="pdf-onebox-logo"></span></a>

<h3><a href="https://www.dropbox.com/s/f3qwpjgpw1pzkyh/2022-aapm.pdf" target="_blank" rel="noopener nofollow ugc">2022-aapm.pdf</a></h3>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #26 by @Spiros_Karkavitsas (2023-07-11 19:23 UTC)

<p>Hello again after a long time <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Finally I will use this tool to compare the fat segmentation between groundtruth volumes and predicted volumes.</p>
<p>When I say volume, I mean 25 axial MR Slices. The voxel size is 1.95 by 1.95 by 10 in mm.</p>
<p>I would like to ask if the segment comparison module, does the Similarity metric calculation voxel wise.</p>
<p>Thank you for your time reading this message and hope for an answer</p>

---

## Post #27 by @gcsharp (2023-07-11 19:35 UTC)

<p>Yes, it is voxelwise.  If the images are different size, both are padded.  If they are different voxel pitch, the compare image is resampled to the voxel pitch of the reference image.</p>

---

## Post #28 by @Spiros_Karkavitsas (2023-07-11 19:41 UTC)

<p>Good, thank you for the immediate answer <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
