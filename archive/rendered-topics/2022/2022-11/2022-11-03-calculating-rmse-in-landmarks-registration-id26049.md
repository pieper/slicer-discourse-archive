# Calculating RMSE in Landmarks Registration

**Topic ID**: 26049
**Date**: 2022-11-03
**URL**: https://discourse.slicer.org/t/calculating-rmse-in-landmarks-registration/26049

---

## Post #1 by @domP (2022-11-03 10:45 UTC)

<p>Hi,<br>
Could I ask if anyone has a code to calculate RMSE obtained from “Fiducial Registration Wizard” module?<br>
I have read the repository’s code linked below:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/Logic/vtkSlicerFiducialRegistrationWizardLogic.cxx#L480">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/Logic/vtkSlicerFiducialRegistrationWizardLogic.cxx#L480" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/Logic/vtkSlicerFiducialRegistrationWizardLogic.cxx#L480" target="_blank" rel="noopener nofollow ugc">SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/Logic/vtkSlicerFiducialRegistrationWizardLogic.cxx#L480</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="470" style="counter-reset: li-counter 469 ;">
          <li>//------------------------------------------------------------------------------</li>
          <li>double vtkSlicerFiducialRegistrationWizardLogic::CalculateRegistrationError(vtkPoints* fromPoints, vtkPoints* toPoints, vtkAbstractTransform* transform)</li>
          <li>{</li>
          <li>  // Transform the from points</li>
          <li>  vtkSmartPointer&lt;vtkPoints&gt; transformedFromPoints = vtkSmartPointer&lt;vtkPoints&gt;::New();</li>
          <li>  transform-&gt;TransformPoints(fromPoints, transformedFromPoints);</li>
          <li>
          </li>
<li>  // Calculate the RMS distance between the to points and the transformed from points</li>
          <li>  double sumSquaredError = 0;</li>
          <li>  for (int i = 0; i &lt; toPoints-&gt;GetNumberOfPoints(); i++)</li>
          <li class="selected">  {</li>
          <li>    double currentToPoint[3] = { 0, 0, 0 };</li>
          <li>    toPoints-&gt;GetPoint(i, currentToPoint);</li>
          <li>    double currentTransformedFromPoint[3] = { 0, 0, 0 };</li>
          <li>    transformedFromPoints-&gt;GetPoint(i, currentTransformedFromPoint);</li>
          <li>
          </li>
<li>    sumSquaredError += vtkMath::Distance2BetweenPoints(currentToPoint, currentTransformedFromPoint);</li>
          <li>  }</li>
          <li>
          </li>
<li>  return sqrt(sumSquaredError / toPoints-&gt;GetNumberOfPoints());</li>
          <li>}</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>but when I have tried to replicate it on Matlab I have got the wrong result.</p>
<p>Below my data and results:<br>
Fixed points:  [61.8616132503630; 48.4552443635927; 42.4899670291801]<br>
[29.4899390311330; 48.4552443635927; 23.5335812251265]<br>
[77.9016320076391; 48.4552443635927; 35.1990494122364]</p>
<p>Moving points transformed: [61.9137516947608; 48.4552459716797; 43.5304726392767]<br>
[27.5809622469604; 48.4552459716797; 22.7209879790148]<br>
[79.7584735999537; 48.4552459716797; 34.9711363721714]</p>
<p>RMSE from Slicer:  1.7214<br>
RMSE from Matlab: 0.8654</p>
<p>Fixed and moving points are expressed in RAS coordinates.</p>
<p>Below my Matlab code:</p>
<p>euclideanDistance= zeros(3,1);<br>
for i= 1:3<br>
euclideanDistance(i)= ((norm(points_moving{i} - points_fixed{i})));<br>
end<br>
RMSE= sqrt(mean(euclideanDistance));</p>

---

## Post #2 by @lassoan (2022-11-03 15:56 UTC)

<p>You need compute the mean of the <code>error^2</code> (<code>vtkMath::Distance2BetweenPoints</code> provides distance^2). In your matlab code you computed the mean of <code>error</code> instead.</p>

---
