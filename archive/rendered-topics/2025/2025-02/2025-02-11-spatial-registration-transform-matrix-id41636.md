# Spatial registration transform matrix

**Topic ID**: 41636
**Date**: 2025-02-11
**URL**: https://discourse.slicer.org/t/spatial-registration-transform-matrix/41636

---

## Post #1 by @ramonemiliani93 (2025-02-11 22:30 UTC)

<p><strong>Hello!</strong></p>
<p>I’m trying to load a spatial registration into 3D Slicer, and I’ve run into a few questions:</p>
<hr>
<h3><a name="p-122427-h-1-multiple-frames-of-reference-1" class="anchor" href="#p-122427-h-1-multiple-frames-of-reference-1" aria-label="Heading link"></a>1. Multiple Frames of Reference</h3>
<p>Does 3D Slicer support multiple frames of reference in a single registration file? I’ve noticed that when I load a registration containing multiple items in the “Registration Sequence” attribute, only one transform matrix appears. How should multiple transforms be handled?</p>
<hr>
<h3><a name="p-122427-h-2-differences-in-sign-2" class="anchor" href="#p-122427-h-2-differences-in-sign-2" aria-label="Heading link"></a>2. Differences in Sign</h3>
<p>When I load a test matrix from a generated file, I see that some signs differ between the matrix values stored in the DICOM file and those displayed in Slicer. What might cause these discrepancies?</p>
<hr>
<h3><a name="p-122427-h-3-matrix-multiplication-order-3" class="anchor" href="#p-122427-h-3-matrix-multiplication-order-3" aria-label="Heading link"></a>3. Matrix Multiplication Order</h3>
<p>If multiple matrices are present in the “Matrix Sequence” attribute, the final transform matrix displayed seems to be calculated as (using NumPy notation):</p>
<pre><code class="lang-auto">m1 @ m2 @ m3
</code></pre>
<p>However, according to <em>Equation C.20.2-2</em> in the DICOM standard, it appears the multiplication order should be reversed. Could you clarify how Slicer applies these matrices and why the resulting order might differ from the standard?</p>
<p>Thank you in advance for your help!</p>

---

## Post #2 by @dpvaldes (2025-02-12 14:35 UTC)

<aside class="quote no-group" data-username="ramonemiliani93" data-post="1" data-topic="41636">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ramonemiliani93/48/79433_2.png" class="avatar"> ramonemiliani93:</div>
<blockquote>
<h3>2. Differences in Sign</h3>
<p>When I load a test matrix from a generated file, I see that some signs differ between the matrix values stored in the DICOM file and those displayed in Slicer. What might cause these discrepancies?</p>
</blockquote>
</aside>
<p>This is due to the different coordinate systems used to store and display. While information in dicom files is stored in the LPS system, Slicer displays coordinates as RAS, having to flip the signs of the first 2 axes when uploading data from a dice into the software.</p>

---

## Post #3 by @lassoan (2025-02-13 04:06 UTC)

<blockquote>
<p>Multiple Frames of Reference</p>
</blockquote>
<p>A transform node can store a sequence of transforms. But since linear transforms can be combined into a single matrix, we usually use a single transform.</p>
<blockquote>
<p>Matrix Multiplication Order</p>
</blockquote>
<p>You can find the full implementation here:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerRT/blob/169eed7b5dab2c3b0201fcf087664ae82d60033e/DicomSroImportExport/Logic/vtkSlicerDicomSroReader.cxx#L272">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/blob/169eed7b5dab2c3b0201fcf087664ae82d60033e/DicomSroImportExport/Logic/vtkSlicerDicomSroReader.cxx#L272" target="_blank" rel="noopener">github.com/SlicerRt/SlicerRT</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/169eed7b5dab2c3b0201fcf087664ae82d60033e/DicomSroImportExport/Logic/vtkSlicerDicomSroReader.cxx#L272" target="_blank" rel="noopener">DicomSroImportExport/Logic/vtkSlicerDicomSroReader.cxx</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerRt/SlicerRT/blob/169eed7b5dab2c3b0201fcf087664ae82d60033e/DicomSroImportExport/Logic/vtkSlicerDicomSroReader.cxx#L272" rel="noopener"><code>169eed7b5</code></a>
</div>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="262" style="counter-reset: li-counter 261 ;">
          <li>      vtkErrorMacro("vtkSlicerDicomSroReader::Update: error reading file");
</li>
          <li>    }
</li>
          <li>  } 
</li>
          <li>  else 
</li>
          <li>  {
</li>
          <li>    vtkErrorMacro("vtkSlicerDicomSroReader::Update: invalid filename: &lt;empty string&gt;");
</li>
          <li>  }
</li>
          <li>}
</li>
          <li>
</li>
          <li>//----------------------------------------------------------------------------
</li>
          <li class="selected">void vtkSlicerDicomSroReader::LoadSpatialRegistration(DcmDataset* dataset)
</li>
          <li>{
</li>
          <li>  this-&gt;LoadSpatialRegistrationSuccessful = false; 
</li>
          <li>  
</li>
          <li>  vtkSmartPointer&lt;vtkMatrix4x4&gt; invMatrix = vtkSmartPointer&lt;vtkMatrix4x4&gt;::New();
</li>
          <li>  invMatrix-&gt;Identity();
</li>
          <li>  invMatrix-&gt;SetElement(0,0,-1);
</li>
          <li>  invMatrix-&gt;SetElement(1,1,-1);
</li>
          <li>  vtkSmartPointer&lt;vtkMatrix4x4&gt; forMatrix = vtkSmartPointer&lt;vtkMatrix4x4&gt;::New();
</li>
          <li>  forMatrix-&gt;Identity();
</li>
          <li>  forMatrix-&gt;SetElement(0,0,-1);
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If you believe that this implementation is incorrect and you have a DICOM SRO file (created by a clinical software) that Slicer does not seem to load correctly then please submit a bug report to the SlicerRT repository.</p>

---

## Post #5 by @ramonemiliani93 (2025-02-13 15:12 UTC)

<p>Thanks for the clarification Daniela <img src="https://emoji.discourse-cdn.com/twitter/raised_hands.png?v=12" title=":raised_hands:" class="emoji" alt=":raised_hands:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @ramonemiliani93 (2025-02-13 15:26 UTC)

<p>Thanks a lot for the reply, Andras!</p>
<p>I was reviewing the Spatial Registration IOD, specifically the <code>RegistrationSequence</code> tag (0070,0308), which states:</p>
<blockquote>
<p><em>A Sequence of registration Items. Each Item defines a spatial registration of the images referenced in that Item to the Registered RCS established by this SOP Instance. All referenced images are in the same spatial Frame of Reference or atlas.</em><br>
<em>One or more Items shall be included in this Sequence.</em></p>
</blockquote>
<p>If I understand correctly, each registration item may have a different Frame of Reference UID. However, in the snippet you shared, it appears that the matrices from each registration item are multiplied together. This could cause issues when multiple Frames of Reference are involved.</p>
<p>Unfortunately, I don’t have a clinical software DICOM SRO file to share because I am creating one myself and trying to load it.</p>
<p>Regarding the matrix multiplication order, it seems that the first matrices are applied on the outer side, as shown here:</p>
<pre data-code-wrap="cpp"><code class="lang-cpp">vtkMatrix4x4::Multiply4x4(this-&gt;SpatialRegistrationMatrix, tempMatrix, tempMatrix2);
this-&gt;SpatialRegistrationMatrix-&gt;DeepCopy(tempMatrix2);
</code></pre>
<p>This suggests an order of M1 x M2 x M3, which might conflict with the description provided for the <code>FrameOfReferenceTransformationMatrix</code> in equation C.20.2-2 of the standard. I might be misunderstanding something from the code or the standards—any clarification would be appreciated.</p>

---

## Post #7 by @lassoan (2025-02-13 20:39 UTC)

<p>The current implementation was tested with DICOM SRO from a clinical system. Probably it was not tested with multiple frame of references.</p>
<p>Please check for examples at <a href="https://portal.imaging.datacommons.cancer.gov/explore/">https://portal.imaging.datacommons.cancer.gov/explore/</a> (you can filter for Modality=Registration) to test Slicer and your implementation. If you want to use some DICOM feature that is not implemented by anyone else then it is tough, as you may need to interpret the standard, implement, and test it on your own and hope that others will interpret and implement it the same way.</p>
<p>If you implement any improvements or fixes in SlicerRT that work well on clinical images then those will be very welcome. I’m not sure if anyone else currently has funding for improving DICOM SRO in SlicerRT - maybe <a class="mention" href="/u/cpinter">@cpinter</a> knows more.</p>

---

## Post #8 by @cpinter (2025-02-17 09:51 UTC)

<p>Thanks for the discussion. As <a class="mention" href="/u/lassoan">@lassoan</a> says this was implemented several years ago, but was tested with clinical data. The actual driver of the work I think was <a class="mention" href="/u/gcsharp">@gcsharp</a> . I am not aware of any project aiming to improve this part of SlicerRT. Finally there is some activity around SlicerRT, but unfortunately not touching the SRO support (that I am aware of, as of now).</p>

---
