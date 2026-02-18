# Registration of two objects

**Topic ID**: 34353
**Date**: 2024-02-16
**URL**: https://discourse.slicer.org/t/registration-of-two-objects/34353

---

## Post #1 by @labixin (2024-02-16 03:11 UTC)

<p>Hello everyone,</p>
<p>I want to register two objects. One is an ellipsoid represented as a model (Figure 1). It was created using “Create Models” and “Surface Toolbox” modules with specific dimensions (4.5×4.0×1.0). The other one is a few high density markers represented as segment (labelled in green on Figure 2). It was segmented using “Segment Editor” module within breast region.</p>
<p>I would like to register the two objects and make the markers as close to the surface of the ellipsoid as possible. Theoretically, the markers represented the margin/edge of the tumor resection cavity (modelled by ellipsoid). And I want to determine the location of ellipsoid through registration (rigid, translate or rotate).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ed43d823b696374071945439f9e06abad382841.png" data-download-href="/uploads/short-url/fOrf9zSKx8TVyszVJXLJ64TtPCV.png?dl=1" title="used_ask2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ed43d823b696374071945439f9e06abad382841_2_517x253.png" alt="used_ask2" data-base62-sha1="fOrf9zSKx8TVyszVJXLJ64TtPCV" width="517" height="253" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ed43d823b696374071945439f9e06abad382841_2_517x253.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ed43d823b696374071945439f9e06abad382841_2_775x379.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ed43d823b696374071945439f9e06abad382841_2_1034x506.png 2x" data-dominant-color="73748E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">used_ask2</span><span class="informations">1322×649 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there any registration tool useful for achieving this? And do I need to change the markers segment into fiducials or models? Hope for some advice.</p>
<p>Thanks in advance. Your help is highly appreciated.</p>
<p>Best regards,</p>
<p>Crayon</p>

---

## Post #2 by @muratmaga (2024-02-17 01:06 UTC)

<p>I don’t think there is any registration tool that will do this automatically for you. However, if you can place 4-5 manual landmarks on each of the structures that you will like to register, you can use the Fiducial Registration Wizard in the SlicerIGT extension. It can create rigid, similarity, affine or warping transforms.</p>

---

## Post #3 by @Matteboo (2024-02-19 10:13 UTC)

<p>Hello,<br>
One thing that I did in the past that could work for you is to transform your segmentation in a volume by exporting it to a labelmap. I guess that you can do the same thing with you model.<br>
This way you can use all the toolbox made to register volumes on them.<br>
Once you have your registration, you can just apply it to the model.</p>

---

## Post #4 by @labixin (2024-02-19 15:47 UTC)

<p>Thanks for your advice. I have tried “Fiducial Registration Wizard” and the result is pretty good. I would like to know more about the registration algorithm. And I wonder what to reference if the work is prepared for research paper.</p>
<p>Hope for your reply. Thank you very much again.</p>
<p>Best regards,</p>
<p>Crayon</p>

---

## Post #5 by @labixin (2024-02-19 16:01 UTC)

<aside class="quote no-group" data-username="Matteboo" data-post="3" data-topic="34353">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matteboo/48/66548_2.png" class="avatar"> Matteboo:</div>
<blockquote>
<p>This way you can use all the toolbox made to register volumes on them.</p>
</blockquote>
</aside>
<p>Thanks for your inspiring suggestions. I wonder what registration module did you use in your task. I could only perform “General Registration (BRAINS)” and “General Registration (ANTs)” for registration of the two labelmap volume. Is there any other registration module that I could have a try?</p>
<p>Hope for your reply. Thank you very much again.</p>
<p>Best regards,</p>
<p>Crayon</p>

---

## Post #6 by @muratmaga (2024-02-19 16:24 UTC)

<p>That’s the nice thing about open source, you can look under the hood to see what they are using. I am not familiar with technical aspects of Fiducial Registration Wizard module, but quick look to the source code, found this section ComputedPairedPointMapping:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerIGT/SlicerIGT/blob/20ff7abdb7fd0126f353337d3c90aed323f8b9eb/FiducialRegistrationWizard/Logic/vtkSlicerFiducialRegistrationWizardLogic.h#L92">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerIGT/blob/20ff7abdb7fd0126f353337d3c90aed323f8b9eb/FiducialRegistrationWizard/Logic/vtkSlicerFiducialRegistrationWizardLogic.h#L92" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerIGT/blob/20ff7abdb7fd0126f353337d3c90aed323f8b9eb/FiducialRegistrationWizard/Logic/vtkSlicerFiducialRegistrationWizardLogic.h#L92" target="_blank" rel="noopener">SlicerIGT/SlicerIGT/blob/20ff7abdb7fd0126f353337d3c90aed323f8b9eb/FiducialRegistrationWizard/Logic/vtkSlicerFiducialRegistrationWizardLogic.h#L92</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="82" style="counter-reset: li-counter 81 ;">
          <li>  virtual void UpdateFromMRMLScene() override;</li>
          <li>  virtual void OnMRMLSceneNodeAdded(vtkMRMLNode* node) override;</li>
          <li>  virtual void OnMRMLSceneNodeRemoved(vtkMRMLNode* node) override;</li>
          <li></li>
          <li>private:</li>
          <li>  vtkSlicerFiducialRegistrationWizardLogic(const vtkSlicerFiducialRegistrationWizardLogic&amp;); // Not implemented</li>
          <li>  void operator=(const vtkSlicerFiducialRegistrationWizardLogic&amp;);               // Not implemented</li>
          <li></li>
          <li>  // this function reorders the comparePoints such that they are matched geometrically to the referencePoints.</li>
          <li>  // the output is stored in comparePointsMatched.</li>
          <li class="selected">  static void   ComputePairedPointMapping( vtkPoints* referencePoints, vtkPoints* comparePoints, vtkPoints* comparePointsMatched );</li>
          <li></li>
          <li>  // helper function to compute a sum of squares</li>
          <li>  static double SumOfSquaredElementsInArray( vtkDoubleArray* array );</li>
          <li></li>
          <li>  // The ComputePairedPointMapping will iterate over all permutations on the order of comparePoints.</li>
          <li>  // The goal is to minimize a suitability metric.</li>
          <li>  // The metric is based on the distances between ordered pairs of points within the list.</li>
          <li>  // These distances act as a kind of fingerprint.</li>
          <li>  // In a 'good' mapping, there will be little difference seen in the reference and test distances</li>
          <li>  static double ComputeSuitabilityOfDistancesMetric( vtkPointDistanceMatrix* referenceDistanceMatrix, vtkPointDistanceMatrix* testDistanceMatrix );</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>which looks like traditional point correspondence algorithm that tries to minimize the total sum of squares between two sets of corresponding points. I am not sure if there is a specific paper you can cite.</p>

---

## Post #7 by @Matteboo (2024-02-19 16:27 UTC)

<p>I used <a class="hashtag-cooked" href="/tag/elastix" data-type="tag" data-slug="elastix" data-id="127"><span class="hashtag-icon-placeholder"><svg class="fa d-icon d-icon-square-full svg-icon svg-node"><use href="#square-full"></use></svg></span><span>elastix</span></a><br>
I prefer it because it’s very modulable but I don’t know the module that you used so they might be just as good.</p>

---

## Post #8 by @labixin (2024-02-20 08:08 UTC)

<p>Thanks for your reply. I have used Elastix before to register pre- and post-CT images in my previous research work. But now in this task there are two labelmap volume on the same CT image. As shown in Figure 1, the ellipsoid is labeled in yellow and the markers are labeled in green. And I don’t know where to put the two labelmap volume in Elastix. The GUI is presented in Figure 2.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76de081a3a0240fcbe5388f7b388a28e7df6669e.jpeg" data-download-href="/uploads/short-url/gXy2BWFbG4zZQOuLQ0ZDq5XkLa6.jpeg?dl=1" title="labelmap_ask3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76de081a3a0240fcbe5388f7b388a28e7df6669e_2_517x225.jpeg" alt="labelmap_ask3" data-base62-sha1="gXy2BWFbG4zZQOuLQ0ZDq5XkLa6" width="517" height="225" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76de081a3a0240fcbe5388f7b388a28e7df6669e_2_517x225.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76de081a3a0240fcbe5388f7b388a28e7df6669e_2_775x337.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76de081a3a0240fcbe5388f7b388a28e7df6669e_2_1034x450.jpeg 2x" data-dominant-color="777574"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">labelmap_ask3</span><span class="informations">1783×777 196 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Figure 1</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d4c050560383ae56224f23178848133601e809e.png" data-download-href="/uploads/short-url/b1NDsGy6NFT1QJea8s0hZYVJ1BY.png?dl=1" title="elastix_ask3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d4c050560383ae56224f23178848133601e809e_2_435x375.png" alt="elastix_ask3" data-base62-sha1="b1NDsGy6NFT1QJea8s0hZYVJ1BY" width="435" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d4c050560383ae56224f23178848133601e809e_2_435x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d4c050560383ae56224f23178848133601e809e_2_652x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d4c050560383ae56224f23178848133601e809e.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">elastix_ask3</span><span class="informations">850×731 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Figure 2</p>
<p>Hope for some advice. Your help is highly appreciated.</p>
<p>Best regards,</p>
<p>Crayon</p>

---

## Post #9 by @labixin (2024-02-20 08:42 UTC)

<p>Thanks for your time. I wonder if the algorithm still be effective when the fiducials are not paired correspondingly. I have placed 8 manual landmarks on markers (the geometric center). However, I could only randomIy choose 8 fiducials on the surface of the ellipsoid. That is, I could not ensure the exact correspondence of the two fiducial lists. Will the registration method still be effective?</p>
<p>Hope for your reply. Your help is highly appreciated.</p>
<p>Best regards,</p>
<p>Crayon</p>

---

## Post #10 by @Matteboo (2024-02-20 10:14 UTC)

<p>You need to convert the labelmap to a volume<br>
To do this you can use “Mask Scalar volume”<br>
From memory, you can put the labelmap as “input volume” and “Mask Volume”<br>
Then the output is the same that your labelisation but as a volume</p>

---
