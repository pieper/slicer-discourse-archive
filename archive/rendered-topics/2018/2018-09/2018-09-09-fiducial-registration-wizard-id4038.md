# Fiducial Registration wizard

**Topic ID**: 4038
**Date**: 2018-09-09
**URL**: https://discourse.slicer.org/t/fiducial-registration-wizard/4038

---

## Post #1 by @tomas (2018-09-09 23:24 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.9.0</p>
<p>Hi,</p>
<p>I have some query regarding “Fidutial Registration wizard”.</p>
<p>I am using the ‘fiducial registration wizard’ module transform type “rigid” and “Similarity"  Registration for my master thesis. I need some extra information about it:</p>
<ol>
<li>Is the registration algorithm ICP method? or what is the mathematical model?</li>
<li>How can I quantify or compare the performance of registration by this module?</li>
<li>Does exist a way to calculate an error after the registration (for qualitative assessment and visualization options)?</li>
</ol>
<p>Thanks<br>
Tomas</p>

---

## Post #2 by @Andinet_Enquobahrie (2018-09-10 10:10 UTC)

<p>Hi Thomas,</p>
<p>I am assuming you are referring to the the Fiducial Registration Module in SlicerIGT.</p>
<blockquote>
<ol>
<li>Is the registration algorithm ICP method? or what is the mathematical model?</li>
</ol>
</blockquote>
<p>This module uses <a href="https://www.vtk.org/doc/nightly/html/classvtkIterativeClosestPointTransform.html#details" rel="noopener nofollow ugc">vtkIterativeClosestPointTransform</a></p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/Logic/vtkPointMatcher.cxx#L369">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/Logic/vtkPointMatcher.cxx#L369" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/Logic/vtkPointMatcher.cxx#L369" target="_blank" rel="noopener nofollow ugc">SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/Logic/vtkPointMatcher.cxx#L369</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="359" style="counter-reset: li-counter 358 ;">
          <li></li>
          <li>vtkSmartPointer&lt; vtkPolyData &gt; unmatchedSourcePointsPolyData = vtkSmartPointer&lt; vtkPolyData &gt;::New();</li>
          <li>vtkPointMatcher::GeneratePolyDataFromPoints( this-&gt;InputSourcePoints, unmatchedSourcePointsPolyData );</li>
          <li></li>
          <li>vtkSmartPointer&lt; vtkTransformPolyDataFilter &gt; initialRegistrationTransformFilter = vtkSmartPointer&lt; vtkTransformPolyDataFilter &gt;::New();</li>
          <li>initialRegistrationTransformFilter-&gt;SetTransform( initialRegistrationTransform );</li>
          <li>initialRegistrationTransformFilter-&gt;SetInputData( unmatchedSourcePointsPolyData );</li>
          <li>initialRegistrationTransformFilter-&gt;Update();</li>
          <li></li>
          <li>vtkPolyData* initiallyRegisteredSourcePointsPolyData = vtkPolyData::SafeDownCast( initialRegistrationTransformFilter-&gt;GetOutput() );</li>
          <li class="selected">if ( initiallyRegisteredSourcePointsPolyData == NULL )</li>
          <li>{</li>
          <li>  vtkWarningMacro( "Initially registered source points poly data is null." );</li>
          <li>  return false;</li>
          <li>}</li>
          <li></li>
          <li>vtkSmartPointer&lt; vtkPolyData &gt; unmatchedTargetPointsPolyData = vtkSmartPointer&lt; vtkPolyData &gt;::New();</li>
          <li>vtkPointMatcher::GeneratePolyDataFromPoints( this-&gt;InputTargetPoints, unmatchedTargetPointsPolyData );</li>
          <li></li>
          <li>// Do some ICP to refine the result</li>
          <li>vtkSmartPointer&lt; vtkIterativeClosestPointTransform &gt; icpTransform = vtkSmartPointer&lt; vtkIterativeClosestPointTransform &gt;::New();</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<blockquote>
<ol start="2">
<li>How can I quantify or compare the performance of registration by this module?</li>
</ol>
</blockquote>
<p>The module returns RMS error.</p>
<ol start="3">
<li>Does exist a way to calculate an error after the registration (for qualitative assessment and visualization options)?</li>
</ol>
<p>You can use <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/CheckerBoardFilter" rel="noopener nofollow ugc">Checkerboard</a> or subtract image modules to evaluate the registration visually.</p>
<p>HTH,<br>
Andinet</p>

---

## Post #3 by @tomas (2018-09-11 17:03 UTC)

<p>Thank you very much.</p>

---

## Post #4 by @lassoan (2018-09-11 18:28 UTC)

<p>Note that ICP is only used as an optional pre-processing step for automatic matching of out-of-order or missing points. Transform is computed using vtkLandmarkTransform class:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/Logic/vtkSlicerFiducialRegistrationWizardLogic.cxx#L360" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/Logic/vtkSlicerFiducialRegistrationWizardLogic.cxx#L360" target="_blank">SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/Logic/vtkSlicerFiducialRegistrationWizardLogic.cxx#L360</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="350" style="counter-reset: li-counter 349 ;">
<li>  return false;</li>
<li>}</li>
<li>
</li>
<li>// compute registration</li>
<li>int registrationMode = fiducialRegistrationWizardNode-&gt;GetRegistrationMode();</li>
<li>if (registrationMode == vtkMRMLFiducialRegistrationWizardNode::REGISTRATION_MODE_RIGID ||</li>
<li>  registrationMode == vtkMRMLFiducialRegistrationWizardNode::REGISTRATION_MODE_SIMILARITY)</li>
<li>{</li>
<li>  // Compute transformation matrix. We don't set the landmark transform in the node directly because</li>
<li>  // vtkLandmarkTransform is not fully supported (e.g., it cannot be stored in file).</li>
<li class="selected">  vtkNew&lt;vtkLandmarkTransform&gt; landmarkTransform;</li>
<li>  landmarkTransform-&gt;SetSourceLandmarks(fromPointsOrdered);</li>
<li>  landmarkTransform-&gt;SetTargetLandmarks(toPointsOrdered);</li>
<li>  if (registrationMode == vtkMRMLFiducialRegistrationWizardNode::REGISTRATION_MODE_RIGID)</li>
<li>  {</li>
<li>    landmarkTransform-&gt;SetModeToRigidBody();</li>
<li>  }</li>
<li>  else</li>
<li>  {</li>
<li>    landmarkTransform-&gt;SetModeToSimilarity();</li>
<li>  }</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>vtkLandmarkTransform class implements Horn’s method:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Kitware/VTK/blob/master/Common/Transforms/vtkLandmarkTransform.cxx#L79-L82" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/VTK/blob/master/Common/Transforms/vtkLandmarkTransform.cxx#L79-L82" target="_blank">Kitware/VTK/blob/master/Common/Transforms/vtkLandmarkTransform.cxx#L79-L82</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="79" style="counter-reset: li-counter 78 ;">
<li>The solution is based on</li>
<li>Berthold K. P. Horn (1987),</li>
<li>"Closed-form solution of absolute orientation using unit quaternions,"</li>
<li>Journal of the Optical Society of America A, 4:629-642</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @tomas (2018-09-11 21:08 UTC)

<p>Thank you very much.</p>

---
