---
topic_id: 2243
title: "Retiring Midas Kitware Com Data Repository"
date: 2018-03-05
url: https://discourse.slicer.org/t/2243
---

# Retiring midas.kitware.com data repository

**Topic ID**: 2243
**Date**: 2018-03-05
**URL**: https://discourse.slicer.org/t/retiring-midas-kitware-com-data-repository/2243

---

## Post #1 by @jcfr (2018-03-05 19:45 UTC)

<p>Hi Slicers,</p>
<p>Slicer4 community that was hosted on that server has been removed.</p>
<p>For now, associated datasets have been moved to <a href="http://slicer.kitware.com/midas3/folder/4539">http://slicer.kitware.com/midas3/folder/4539</a></p>
<p>These includes:</p>
<ul>
<li><a href="http://slicer.kitware.com/midas3/item/347107">blocks-fruit-phones.tar.gz</a></li>
<li><a href="http://slicer.kitware.com/midas3/folder/5038">CTHeadAxialDicom</a></li>
<li><a href="http://slicer.kitware.com/midas3/folder/5037">DicomToNrrdTestBaselineData</a></li>
<li><a href="http://slicer.kitware.com/midas3/folder/5039">DWIDicom</a></li>
<li><a href="http://slicer.kitware.com/midas3/folder/5044">EMSegmentTestData</a></li>
<li><a href="http://slicer.kitware.com/midas3/folder/5040">Miscellaneous</a></li>
<li><a href="http://slicer.kitware.com/midas3/folder/5042">vhp2</a></li>
<li><a href="http://slicer.kitware.com/midas3/folder/5043">WMQL Testing Dataset</a></li>
</ul>
<h3>Questions</h3>
<p>Does anyone have more information or details about the following ones ?  And if there are currently used in any tests ?</p>
<ul>
<li>
<p><code>vhp2</code></p>
</li>
<li>
<p><code>blocks-fruit-phones.tar.gz</code></p>
</li>
<li>
<p><code>DWIDicom</code></p>
</li>
<li>
<p><code>DicomToNrrdTestBaselineData</code></p>
</li>
</ul>
<h3>Detailed list of files</h3>
<h4>CTHeadAxialDicom</h4>
<pre><code class="lang-nohighlight">CTHead1.dcm
[...]
CTHead93.dcm
</code></pre>
<h4>DWIDicom</h4>
<pre><code class="lang-nohighlight">MR_0004_0028.dcm
[...]
MR_0004_1800.dcm
</code></pre>
<h4>DicomToNrrdTestBaselineData</h4>
<pre><code class="lang-nohighlight">219d9bd6d755fab0acf2a908db496cde
GeSignaHDx.bval
GeSignaHDx.nii.gz
GeSignaHDx.nrrd
GeSignaHDxTest.bvec
PhilipsAchieva1.nrrd
PhilipsAchieva2.nrrd
PhilipsAchieva3.nrrd
PhilipsAchieva4.nrrd
PhilipsAchieva5.nrrd
PhilipsAchieva6.nrrd
PhilipsAchieva7.nrrd
SiemensTrio-Syngo2004A-1.nrrd
SiemensTrio-Syngo2004A-2.nrrd
SiemensTrioTim1.nrrd
SiemensTrioTim2.nrrd
SiemensTrioTim3.nrrd
SiemensVerio.nrrd
</code></pre>
<h4>EMSegmentTestData</h4>
<p><em>Datasets related to Primal are missing from this list. These will be uploaded shortly</em></p>
<pre><code class="lang-nohighlight">./CT_Hand_Bone/CT_Hand_Bone_Subject_2.nrrd
./CT_Hand_Bone/CT_Hand_Bone_Subject_1.nrrd
./CT_Hand_Bone/CT_Hand_Bone_Subject_3.nrrd

./MRI-Human-Brain-Parcellation /RESULT_very_small_MRIHumanBrainParcellation_T1.nrrd
./MRI-Human-Brain-Parcellation /RESULT_small_MRIHumanBrainParcellation_T1.nrrd

./MRI-Human-Brain-Full-Parcellation/RESULT_small_MRIHumanBrainFullParcellation_T1.nrrd
./MRI-Human-Brain-Full-Parcellation/RESULT_very_small_MRIHumanBrainFullParcellation_T1.nrrd

./MRI-Human-Brain/atlas_greymatter.nrrd
./MRI-Human-Brain/atlas_csf.nrrd
./MRI-Human-Brain/atlas_skulneck.nrrd
./MRI-Human-Brain/atlas_air.nrrd
./MRI-Human-Brain/atlas_t1.nrrd
</code></pre>
<h4>Miscellaneous</h4>
<p><em>Some of these data are already associated with module specific folder found in <a href="http://slicer.kitware.com/midas3/folder/298">Public/Slicer/Data/Modules</a> directory. We will consolidate and remove duplicated entries found in this folder at a later time.</em></p>
<pre><code class="lang-auto">ACPC.fcsv
ACPCTest.mrml
brainSliceCHAR.mha
brainSliceDOUBLE.mha
brainSliceFLOAT.mha
brainSliceINT.mha
brainSliceLONG.mha
brainSliceSHORT.mha
brainSliceUCHAR.mha
brainSliceUINT.mha
brainSliceULONG.mha
brainSliceUSHORT.mha
BSplineDisplacements3D_00.txt
CastTest.nrrd
CTHeadAxialDoubled.nhdr
CTHeadAxialDoubled.raw.gz
CTHeadAxialMask.nrrd
CTHeadAxial.nhdr
CTHeadAxial.raw.gz
CTHeadResampled.nhdr
CTHeadResampledOtsuSegmented.nhdr
CTHeadResampledOtsuSegmented.raw.gz
CTHeadResampled.raw.gz
ExecutionModelTourTest.mrml
he3mask.nii.gz
he3volume.nii.gz
itkAffineTransform00.txt
itkAffineTransform01.txt
itkAffineTransform02.txt
itkAffineTransform03.txt
itkAffineTransform04.txt
itkQuaternionRigidTransform00.txt
itkQuaternionRigidTransform01.txt
itkQuaternionRigidTransform02.txt
itkQuaternionRigidTransform03.txt
itkQuaternionRigidTransform04.txt
midsag.fcsv
ModelMakerTest.mrml
MRHeadResampledBSplineInterpolationTest.nrrd
MRHeadResampledBSplineTransform.tfm
MRHeadResampledBSplineWSInterpolationTest.nrrd
MRHeadResampledHField.nrrd
MRHeadResampledHFieldTest.nrrd
MRHeadResampled.nhdr
MRHeadResampled.raw.gz
MRHeadResampledRotationAndAffine.nrrd
MRHeadResampledRotationNN.nrrd
MRMeningioma01segmented.nrrd
MRMeningioma01.tfm
MRMeningioma0.nrrd
MRMeningioma1.nrrd
SparseFieldLevelSetContourTest.vtp
</code></pre>
<h4>vhp2</h4>
<pre><code class="lang-auto">0070.jpeg
[...]
0079.jpeg
</code></pre>
<h4>WMQL Testing Dataset</h4>
<pre><code class="lang-auto">IIT3mean_desikan_2009.nii.gz
IIT3mean_left_hemisphere_small.trk
IIT3mean_left_hemisphere_small.vtp
IIT3mean_left_hemisphere.vtp
IIT3mean.vtp
wmql_1_cst.qry
wmql_2_uf.qry
wmql_3_commissural.qry
WMQL_Testing_Dataset.tgz
wmql_testing.qry

</code></pre>

---

## Post #2 by @pieper (2018-03-05 20:14 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="1" data-topic="2243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>blocks-fruit-phones.tar.gz</p>
</blockquote>
</aside>
<p>This is a freely sharable CT scan of a collection of objects that can be used for segmentation or visualization experiments.  I do not believe any tests currently use it.</p>
<aside class="quote no-group" data-username="jcfr" data-post="1" data-topic="2243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>WMQL Testing Dataset</p>
</blockquote>
</aside>
<p>I believe this is for the <a href="https://www.ncbi.nlm.nih.gov/pubmed/26754839">White Matter Query Language</a>.  Maybe <a class="mention" href="/u/ihnorton">@ihnorton</a> knows if any SlicerDMRI work depends on it.</p>

---

## Post #3 by @ihnorton (2018-03-05 21:06 UTC)

<p>Yes, some of these files are used in the tests:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/demianw/tract_querier/blob/master/tract_querier/tests/datasets.py#L10-L26">
  <header class="source">

      <a href="https://github.com/demianw/tract_querier/blob/master/tract_querier/tests/datasets.py#L10-L26" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/demianw/tract_querier/blob/master/tract_querier/tests/datasets.py#L10-L26" target="_blank" rel="noopener">demianw/tract_querier/blob/master/tract_querier/tests/datasets.py#L10-L26</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="10" style="counter-reset: li-counter 9 ;">
          <li>FILES = {</li>
          <li>    'tract_file': (</li>
          <li>        'http://midas.kitware.com/bitstream/view/17631',</li>
          <li>        'IIT3mean_left_hemisphere_small.trk',</li>
          <li>        '\xe7\xec\xfd+\xd2n\xff\x96\xae\xb4\xdf+\x194\xdf\x81'</li>
          <li>    ),</li>
          <li>    'atlas_file': (</li>
          <li>        'http://midas.kitware.com/bitstream/view/17622',</li>
          <li>        'IIT3mean_desikan_2009.nii.gz',</li>
          <li>        'vx\x13\xbaE\x1dR\t\xcd\xc9EF\x17\xa66\xb7'</li>
          <li>    ),</li>
          <li>    'query_uf_file': (</li>
          <li>        'http://midas.kitware.com/bitstream/view/17627',</li>
          <li>        'wmql_2_uf.qry',</li>
          <li>        '\\+R\x8c&lt;B#\xea\xfc\x9aE\xbd\xb0(\xbdn'</li>
          <li>    )</li>
          <li>}</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I just posted an issue to let Demian know:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/demianw/tract_querier/issues/42">
  <header class="source">

      <a href="https://github.com/demianw/tract_querier/issues/42" target="_blank" rel="noopener">github.com/demianw/tract_querier</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/demianw/tract_querier/issues/42" target="_blank" rel="noopener">midas.kitware.com is being retired</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2018-03-05" data-time="21:05:24" data-timezone="UTC">09:05PM - 05 Mar 18 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/ihnorton" target="_blank" rel="noopener">
          <img alt="ihnorton" src="https://avatars.githubusercontent.com/u/327706?v=4" class="onebox-avatar-inline" width="20" height="20">
          ihnorton
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Steve just asked the following on the Slicer forum (coincidentally, 10 minutes a<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">fter you were in the office) -- whether WMQL is still using the test data on `midas.kitware.com`, because the server is being retired:

https://discourse.slicer.org/t/retiring-midas-kitware-com-data-repository/2243/2

~~The server is still up, currently~~. The data was backed up at slicer.kitware.com.

(although it looks like the [tests are disabled](https://github.com/demianw/tract_querier/blob/master/tract_querier/tests/datasets.py#L10-L31) right now)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @jcfr (2018-03-05 21:08 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="3" data-topic="2243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>Yes, some of these files are used in the tests:</p>
</blockquote>
</aside>
<p><strong>EDITED:</strong> <s>I will ask our sysadmins to setup redirects so that these tests still work as expected.</s> Following, <a class="mention" href="/u/ihnorton">@ihnorton</a> comment below, the test are updated and there is no need to set the redirects.</p>
<p>For reference, the new download URLs are the following:</p>
<p><em>Note that while we could have an equivalent URL associated with the <code>bitstream</code> endpoint, I suggest to use the <code>item</code> endpoint.</em></p>
<ul>
<li>
<p>IIT3mean_left_hemisphere_small.trk<br>
<code>http://midas.kitware.com/bitstream/view/17631</code><br>
 → <a href="http://slicer.kitware.com/midas3/download/item/347269/IIT3mean_left_hemisphere_small.trk">http://slicer.kitware.com/midas3/download/item/347269/IIT3mean_left_hemisphere_small.trk</a></p>
</li>
<li>
<p>IIT3mean_desikan_2009.nii.gz<br>
<code>http://midas.kitware.com/bitstream/view/17622</code><br>
 → <a href="http://slicer.kitware.com/midas3/download/item/347267/IIT3mean_desikan_2009.nii.gz">http://slicer.kitware.com/midas3/download/item/347267/IIT3mean_desikan_2009.nii.gz</a></p>
</li>
<li>
<p>wmql_2_uf.qry<br>
<code>http://midas.kitware.com/bitstream/view/17627</code><br>
 → <a href="http://slicer.kitware.com/midas3/download/item/347272/wmql_2_uf.qry">http://slicer.kitware.com/midas3/download/item/347272/wmql_2_uf.qry</a></p>
</li>
</ul>

---

## Post #5 by @ihnorton (2018-03-05 21:17 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="4" data-topic="2243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>I will ask our sysadmins to setup redirects so that these tests still work as expected.</p>
</blockquote>
</aside>
<p>For simplicity, just made a <a href="https://github.com/demianw/tract_querier/pull/43">PR</a> to update (though I think the test might actually be disabled).</p>

---
