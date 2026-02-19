---
topic_id: 43584
title: "How To Incorporate Fixedparameters In Manual Calculation Of"
date: 2025-07-02
url: https://discourse.slicer.org/t/43584
---

# How to incorporate FixedParameters in manual calculation of affine linear transformation

**Topic ID**: 43584
**Date**: 2025-07-02
**URL**: https://discourse.slicer.org/t/how-to-incorporate-fixedparameters-in-manual-calculation-of-affine-linear-transformation/43584

---

## Post #1 by @spichardo (2025-07-02 17:26 UTC)

<p>Hi,</p>
<p>I just noticed that sometime between release 5.6.2 and 5.8.1 some changes were made how the linear transform text files were saved. In particular, now FixedParameters have values different from 0. I used this original snip from the official documentation to obtain an affine matrix (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/transforms.html#convert-between-itk-and-slicer-linear-transforms" class="inline-onebox" rel="noopener nofollow ugc">Transforms — 3D Slicer documentation</a>)</p>
<pre><code class="lang-auto">def read_itk_affine_transform(filename):
    with open(filename) as f:
        tfm_file_lines = f.readlines()
    # parse the transform parameters
    match = re.match("Transform: AffineTransform_[a-z]+_([0-9]+)_([0-9]+)", tfm_file_lines[2])
    if not match or match.group(1) != '3' or match.group(2) != '3':
        raise ValueError(f"{filename} is not an ITK 3D affine transform file")
    p = np.array( tfm_file_lines[3].split()[1:], dtype=np.float64 )
    # assemble 4x4 matrix from ITK transform parameters
    itk_transform = np.array([
        [p[0], p[1], p[2], p[9]],
        [p[3], p[4], p[5], p[10]],
        [p[6], p[7], p[8], p[11]],
        [0, 0, 0, 1]])
    return itk_transform
</code></pre>
<p>you can see FixedParameters were not considered in building the affine matrix. But now I saw the exported linear transformation in 5.8.1 have values in FixedParameters different from 0, and I can’t find an example how to incorporate it in the calculation of the affine matrix. For example, I have this transformation file:</p>
<pre><code class="lang-auto">#Insight Transform File V1.0
#Transform 0
Transform: AffineTransform_double_3_3
Parameters: -0.9673983954721169 0.005242446734459156 -0.25320517607311555 -0.01635075985776062 0.9964070799946877 0.08309984108611503 0.25273107662108657 0.08453074995940893 -0.9638368924362907 19.64370704805952 -10.678323249250239 188.5045069754522
FixedParameters: -1.1877449844514136 5.3974515452055405 -63.54885348036633
</code></pre>
<p>that should produce this affine matrix as shown in the GUI (after doing the LPS-&gt;RAS conversion):</p>
<pre><code class="lang-auto">-0.967398 -0.0163508 -0.252731 15 
0.00524245 0.996407 -0.0845307 0 
0.253205 -0.0830998 -0.963837 62 
0 0 0 1 
</code></pre>
<p>Can someone point me how to do the calculations of the afine matrix (using generic Python/Numpy code) when FixedParameters have values different to 0?</p>
<p>Thanks for any help,</p>
<p>Sam</p>

---

## Post #2 by @spichardo (2025-07-04 15:43 UTC)

<p>I figured out, after some search , the use of FixedParameters is about a recentered rotation, the code to obtain the correct affine transformation is as follows</p>
<pre><code class="lang-auto">def read_itk_affine_transform(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Extract Parameters
    params_line = next(line for line in lines if line.startswith('Parameters:'))
    params = list(map(float, params_line.replace('Parameters:', '').strip().split()))
    matrix_values = params[:9]
    translation = np.array(params[9:12])

    # Extract FixedParameters (center of rotation)
    fixed_line = next(line for line in lines if line.startswith('FixedParameters:'))
    fixed_params = np.array(list(map(float, fixed_line.replace('FixedParameters:', '').strip().split())))

    # Reshape matrix and compute adjusted translation
    M = np.array(matrix_values).reshape((3, 3))
    C = fixed_params
    T = translation
    
    adjusted_translation =M @ (-C) + C + T

    # Construct 4x4 matrix
    transform = np.eye(4)
    transform[:3, :3] = M
    transform[:3, 3] = adjusted_translation

    return transform
</code></pre>
<p>then when using the recipe in the official documentation to convert to RAS convention (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/transforms.html#convert-between-itk-and-slicer-linear-transforms" class="inline-onebox" rel="noopener nofollow ugc">Transforms — 3D Slicer documentation</a>), and you obtain back the affine matrix as shown in the GUI. It would be good if the official documentation could shown the modified code, hoping I didn’t miss something else.</p>

---

## Post #3 by @pieper (2025-07-04 16:24 UTC)

<p>Thanks for reporting back.  Maybe you can do a pull request to the documentation to add this to the script repository?</p>

---

## Post #4 by @lassoan (2025-07-04 17:34 UTC)

<p>Excellent, thank you!</p>
<p>I’ve touched up the code a bit and submitted a PR to update the documentation:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8534">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8534" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8534" target="_blank" rel="noopener">Update transforms.md</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>doc-transform-computation-example</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-07-04" data-time="17:34:22" data-timezone="UTC">05:34PM - 04 Jul 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 28 additions and 35 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8534/files" target="_blank" rel="noopener">
            <span class="added">+28</span>
            <span class="removed">-35</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">ITK affine transforms compute the translation part of the homogeneous transforma<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8534" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">tion matrix from the transform parameters and fixed parameters.

The example worked only for cases when the fixed parameters were all zeros.

Implementation is based on ITK and user feedback on the Slicer Forum (https://discourse.slicer.org/t/how-to-incorporate-fixedparameters-in-manual-calculation-of-affine-linear-transformation/43584).</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
