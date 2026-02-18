# Slicer does not accept certain transform values

**Topic ID**: 41398
**Date**: 2025-01-31
**URL**: https://discourse.slicer.org/t/slicer-does-not-accept-certain-transform-values/41398

---

## Post #1 by @TheZappie (2025-01-31 11:26 UTC)

<p>3d slicer does not import volumes that I create with the python code below.<br>
What constraint in 3D slicer is causing this?</p>
<pre data-code-wrap="python"><code class="lang-python">import numpy as np

import nibabel as nib
from nibabel import affines

data = np.random.normal(size=(100, 100, 100))

# this works, imports into 3D Slicer:
rotation = 4.683045966258175
translation = np.round(np.array([364049.08509937, 5991031.44814528, 0.]))

# this works, imports into 3D Slicer:
rotation = 4.69
translation = np.round(np.array([364049.08509937, 5991031.44814528, 0.]))

# this does not import into 3D Slicer:
rotation = 4.683045966258175
translation = np.array([364049.08509937, 5991031.44814528, 0.])

dxv = 0.05
dyv = 0.05
affine = np.array([[np.cos(rotation) * dxv, -np.sin(rotation) * dyv, 0],
                   [np.sin(rotation) * dxv, np.cos(rotation) * dyv, 0],
                   [0, 0, 1]]
                  )


nii_matrix = affines.from_matvec(affine, translation)

nifti_img = nib.Nifti1Image(data, nii_matrix)
nib.save(nifti_img, r"D:\TEST\test.nii")
</code></pre>
<p>I suspect it might have to do with units within 3D slicer. I tested with these settings:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba7046b9687066b5076e69d548d4789ab73fcae2.png" data-download-href="/uploads/short-url/qBjmkYsx3b0LA0c6WbbkNNr9V62.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba7046b9687066b5076e69d548d4789ab73fcae2.png" alt="image" data-base62-sha1="qBjmkYsx3b0LA0c6WbbkNNr9V62" width="683" height="239"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">683×239 8.32 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2025-02-03 08:24 UTC)

<p>Probably the non-normalized image position values cause the problem.</p>
<p>Units are not causing the problem: support in Slicer is added to be able to avoid such extreme position values by choosing the most appropriate coordinate system. However, current units implementation has many limitations, so it cannot yet automatically fix such files yet.</p>
<p>I see that you added an issue for this, let’s continue the discussion there:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/8203#issuecomment-2630222560">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/8203#issuecomment-2630222560" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/8203#issuecomment-2630222560" target="_blank" rel="noopener">Slicer does not accept certain transform values in NIFTI file</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-02-03" data-time="07:23:53" data-timezone="UTC">07:23AM - 03 Feb 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/TheZappie" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/82385093?v=4" class="onebox-avatar-inline" width="20" height="20">
          TheZappie
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

3d slicer does not import volumes that I create with the python code<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> below. Posting this here because I believe this is closer to a bug report than a usage question. 
What constraint in 3D slicer is causing this issue?

## Steps to reproduce

On importing the files, the volume is not loaded, and a error is produced. [Error.txt](https://github.com/user-attachments/files/18638632/Error.txt)
Produced by the code below

```python
import numpy as np

import nibabel as nib
from nibabel import affines

data = np.random.normal(size=(100, 100, 100))

# this works, imports into 3D Slicer:
rotation = 4.683045966258175
translation = np.round(np.array([364049.08509937, 5991031.44814528, 0.]))

# this works, imports into 3D Slicer:
rotation = 4.69
translation = np.round(np.array([364049.08509937, 5991031.44814528, 0.]))

# this does not import into 3D Slicer:
rotation = 4.683045966258175
translation = np.array([364049.08509937, 5991031.44814528, 0.])

dxv = 0.05
dyv = 0.05
affine = np.array([[np.cos(rotation) * dxv, -np.sin(rotation) * dyv, 0],
                   [np.sin(rotation) * dxv, np.cos(rotation) * dyv, 0],
                   [0, 0, 1]]
                  )


nii_matrix = affines.from_matvec(affine, translation)

nifti_img = nib.Nifti1Image(data, nii_matrix)
nib.save(nifti_img, r"D:\TEST\test.nii")
```


## Environment
- Slicer version: 5.8.0 r33216 / d20ee94
- Operating system: Windows10</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
