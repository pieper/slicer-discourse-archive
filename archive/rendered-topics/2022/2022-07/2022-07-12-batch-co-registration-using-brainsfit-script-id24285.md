---
topic_id: 24285
title: "Batch Co Registration Using Brainsfit Script"
date: 2022-07-12
url: https://discourse.slicer.org/t/24285
---

# Batch co-registration using BRAINSfit (script)

**Topic ID**: 24285
**Date**: 2022-07-12
**URL**: https://discourse.slicer.org/t/batch-co-registration-using-brainsfit-script/24285

---

## Post #1 by @dokay1 (2022-07-12 13:08 UTC)

<p>For those looking for a script for Batch co-reg. You still have to add the string “FIXED” (case sensitive) to the name of the volume you want to use as the reference/fixed volume for co-registration.</p>
<pre><code class="lang-auto">PoolOfVolumes = getNodesByClass('vtkMRMLScalarVolumeNode')
FixedVol = getNode('*FIXED*')
for MovingVol in PoolOfVolumes:
    slicer.util.selectModule('BRAINSFit')
    brainsFit = slicer.modules.brainsfit   
    parametersRigid = {}
    parametersRigid["fixedVolume"] = FixedVol.GetID()
    parametersRigid["movingVolume"] = MovingVol.GetID()
    parametersRigid["outputVolume"] = MovingVol.GetID()
    parametersRigid["useRigid"] = True
    parametersRigid["initializeTransformMode"] = "useGeometryAlign"
    parametersRigid["samplingPercentage"] = 0.02
    cliBrainsFitRigidNode = slicer.cli.run(brainsFit, None, parametersRigid)

</code></pre>
<p>Tested and works on Slicer 5.0.2 r30822 / a4420c3 on MacOS 12.4 using brain MRIs.</p>
<p>Cheers,</p>
<p>Dave</p>

---

## Post #2 by @koeglfryderyk (2024-09-09 08:05 UTC)

<aside class="quote no-group" data-username="dokay1" data-post="1" data-topic="24285">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/b4bc9f/48.png" class="avatar"> dokay1:</div>
<blockquote>
<p><code>brainsfit</code></p>
</blockquote>
</aside>
<p>Where can I find all the parameter names (like samplingPercentage etc)?</p>

---

## Post #3 by @pieper (2024-09-09 14:36 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/brainsfit.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/brainsfit.html</a></p>
<p>and</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/BRAINSia/BRAINSTools/blob/main/BRAINSFit/BRAINSFit.xml">
  <header class="source">

      <a href="https://github.com/BRAINSia/BRAINSTools/blob/main/BRAINSFit/BRAINSFit.xml" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/BRAINSia/BRAINSTools/blob/main/BRAINSFit/BRAINSFit.xml" target="_blank" rel="noopener">BRAINSia/BRAINSTools/blob/main/BRAINSFit/BRAINSFit.xml</a></h4>


      <pre><code class="lang-xml">&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;executable&gt;
  &lt;category&gt;Registration&lt;/category&gt;
  &lt;title&gt;General Registration (BRAINS)&lt;/title&gt;
  &lt;description&gt;Register a three-dimensional volume to a reference volume (Mattes Mutual Information by default). Method described in BRAINSFit: Mutual Information Registrations of Whole-Brain 3D Images, Using the Insight Toolkit, Johnson H.J., Harris G., Williams K., The Insight Journal, 2007. http://hdl.handle.net/1926/1291&lt;/description&gt;
  &lt;documentation-url&gt;https://slicer.readthedocs.io/en/latest/user_guide/modules/brainsfit.html&lt;/documentation-url&gt;
  &lt;license&gt;https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt&lt;/license&gt;
  &lt;contributor&gt;Hans J. Johnson (hans-johnson -at- uiowa.edu, http://www.psychiatry.uiowa.edu), Ali Ghayoor&lt;/contributor&gt;
  &lt;acknowledgements&gt;&lt;![CDATA[Hans Johnson(1,3,4); Kent Williams(1); Gregory Harris(1), Vincent Magnotta(1,2,3);  Andriy Fedorov(5); Ali Ghayoor(4) 1=University of Iowa Department of Psychiatry, 2=University of Iowa Department of Radiology, 3=University of Iowa Department of Biomedical Engineering, 4=University of Iowa Department of Electrical and Computer Engineering, 5=Surgical Planning Lab, Harvard]]&gt;  &lt;/acknowledgements&gt;
  &lt;version&gt;5.8.0&lt;/version&gt;

  &lt;parameters advanced="false"&gt;
    &lt;label&gt;Input Images&lt;/label&gt;
    &lt;image&gt;
      &lt;name&gt;fixedVolume&lt;/name&gt;
      &lt;longflag&gt;fixedVolume&lt;/longflag&gt;
      &lt;label&gt;Fixed Image Volume&lt;/label&gt;
      &lt;description&gt;Input fixed image (the moving image will be transformed into this image space).&lt;/description&gt;
      &lt;channel&gt;input&lt;/channel&gt;
      &lt;default&gt;&lt;/default&gt;
</code></pre>



  This file has been truncated. <a href="https://github.com/BRAINSia/BRAINSTools/blob/main/BRAINSFit/BRAINSFit.xml" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
