# Compliance with IBSI

**Topic ID**: 12062
**Date**: 2020-06-17
**URL**: https://discourse.slicer.org/t/compliance-with-ibsi/12062

---

## Post #1 by @Bassam (2020-06-17 02:54 UTC)

<p>Hello team,</p>
<p>I got a promising imaging biomarkers and I have to check their compliance with their reference values identified by IBSI. To do that, I have to specify the following settings in the parameter file (yaml file), so kindly, how can I specify all of them in the parameter file ?</p>
<p>Interpolation: Yes<br>
resampled voxel spacing (mm): 2 x 2 x 2<br>
interpolation method: trilinear<br>
intensity rounding: nearest integer<br>
ROI interpolation method: trilinear<br>
ROI partial mask volume: 0.5</p>
<p>Thanks</p>

---

## Post #2 by @fedorov (2020-06-18 02:48 UTC)

<p>I don’t think ROI interpolation is supported, but setting image interpolation will be done by the following lines in the settings file:</p>
<pre><code class="lang-auto">  interpolator: 'sitkBSpline'
  resampledPixelSpacing: [2,2,2]
</code></pre>
<p>You can find example settings here: <a href="https://github.com/Radiomics/pyradiomics/tree/master/examples/exampleSettings">https://github.com/Radiomics/pyradiomics/tree/master/examples/exampleSettings</a></p>
<p>You may also find this discussion relevant:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Radiomics/pyradiomics/issues/498" target="_blank">github.com/Radiomics/pyradiomics</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Radiomics/pyradiomics/issues/498" target="_blank">Comparison with IBSI features on phantoms</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2019-06-19" data-time="16:54:55" data-timezone="UTC">04:54PM - 19 Jun 19 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/samulic" target="_blank">
          <img alt="samulic" src="https://avatars0.githubusercontent.com/u/22645162?v=4" class="onebox-avatar-inline" width="20" height="20">
          samulic
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">Hello, I'm doing a project on radiomics and I've been trying to compare the results of the features calculated with pyradiomics...</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">question</span>
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">waiting</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @JoostJM (2020-06-30 10:28 UTC)

<p>The linear interpolation for the image in PyRadiomics can be achieve using <code>sitkLinear</code> interpolation. ROI interpolation is always forced to nearest neighbor, as PyRadiomics supports multiple mask values, which can result in unintended change of label value when using linear interpolation with thresholding.</p>

---
