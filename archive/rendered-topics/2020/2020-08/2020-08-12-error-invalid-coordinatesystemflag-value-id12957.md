---
topic_id: 12957
title: "Error Invalid Coordinatesystemflag Value"
date: 2020-08-12
url: https://discourse.slicer.org/t/12957
---

# Error: Invalid coordinateSystemFlag value

**Topic ID**: 12957
**Date**: 2020-08-12
**URL**: https://discourse.slicer.org/t/error-invalid-coordinatesystemflag-value/12957

---

## Post #1 by @szhang (2020-08-12 03:58 UTC)

<p>Hello<br>
In Error log, there comes an error showing “VTK: Invalid coordinateSystemFlag value:0”, how to fix this, by coordinate system conversion?<br>
It looks like <em>coordinateSystemFlag</em>  = 0 for RAS system which is used by Slicer, then why is it problematic?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2020-08-12 18:45 UTC)

<p>Thanks for reporting this. <code>Invalid coordinateSystemFlag value</code> is reported when you run a CLI module that does not specify <code>coordinateSystem="lps"</code>. As long as you specify <code>lps</code> or <code>ras</code> as coordinate system, you can ignore this warning (and I’ll push a fix today to prevent displaying warning in this case).</p>

---

## Post #3 by @szhang (2020-08-12 19:21 UTC)

<p>Thank you, great to know!<br>
May I learn how to specify coordinate system in the module? doesn’t it depend on the configuration associated with the data being imported? or since mostly we import DICOM, by default it is set like this?</p>
<blockquote>
<p>int coordinateSystem = vtkMRMLStorageNode::CoordinateSystemLPS</p>
</blockquote>

---

## Post #4 by @lassoan (2020-08-12 19:23 UTC)

<p>See an example how to specify coordinate system for input points here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/ebc74c7ca99c28a395ebc099a14b002fb28decf1/Modules/CLI/ACPCTransform/ACPCTransform.xml#L15" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/ebc74c7ca99c28a395ebc099a14b002fb28decf1/Modules/CLI/ACPCTransform/ACPCTransform.xml#L15" target="_blank" rel="noopener">Slicer/Slicer/blob/ebc74c7ca99c28a395ebc099a14b002fb28decf1/Modules/CLI/ACPCTransform/ACPCTransform.xml#L15</a></h4>
<pre class="onebox"><code class="lang-xml"><ol class="start lines" start="5" style="counter-reset: li-counter 4 ;">
<li>&lt;index&gt;1&lt;/index&gt;</li>
<li>&lt;description&gt;&lt;![CDATA[&lt;p&gt;Calculate a transformation that aligns brain images to standard orientation based on anatomical landmarks.&lt;/p&gt;&lt;p&gt;The ACPC line extends between two points, one at the anterior commissure and one at the posterior commissure. The resulting transform will bring the line connecting the two points horizontal to the AP axis.&lt;/p&gt;&lt;p&gt;The midline is a series of points (at least 3) defining the division between the hemispheres of the brain (the mid sagittal plane). The resulting transform will result in the output volume having the mid sagittal plane lined up with the AS plane.&lt;/p&gt;&lt;p&gt;Use the Filtering module &lt;b&gt;Resample Scalar/Vector/DWI Volume&lt;/b&gt; to apply the transformation to a volume.&lt;/p&gt;]]&gt;&lt;/description&gt;</li>
<li>&lt;version&gt;1.0&lt;/version&gt;</li>
<li>&lt;documentation-url&gt;http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/ACPCTransform&lt;/documentation-url&gt;</li>
<li>&lt;license&gt;slicer3&lt;/license&gt;</li>
<li>&lt;contributor&gt;Nicole Aucoin (SPL, BWH), Ron Kikinis (SPL, BWH)&lt;/contributor&gt;</li>
<li>&lt;acknowledgements&gt;&lt;![CDATA[This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.]]&gt;&lt;/acknowledgements&gt;</li>
<li>&lt;parameters&gt;</li>
<li>  &lt;label&gt;Transform panel&lt;/label&gt;</li>
<li>  &lt;description&gt;&lt;![CDATA[Calculate a transform from midline and ACPC fiducial lists.]]&gt;&lt;/description&gt;</li>
<li class="selected">  &lt;point multiple="true" coordinateSystem="ras"&gt;</li>
<li>    &lt;name&gt;ACPC&lt;/name&gt;</li>
<li>    &lt;label&gt;ACPC Line&lt;/label&gt;</li>
<li>    &lt;longflag&gt;--acpc&lt;/longflag&gt;</li>
<li>    &lt;description&gt;&lt;![CDATA[ACPC line, a list of two fiducial points, one at the anterior commissure and one at the posterior commissure.]]&gt;&lt;/description&gt;</li>
<li>    &lt;default&gt;0,0,0&lt;/default&gt;</li>
<li>  &lt;/point&gt;</li>
<li>  &lt;point multiple="true" coordinateSystem="ras"&gt;</li>
<li>    &lt;name&gt;Midline&lt;/name&gt;</li>
<li>    &lt;label&gt;Midline&lt;/label&gt;</li>
<li>    &lt;longflag&gt;--midline&lt;/longflag&gt;</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
