# Exporting file to .nii and .nii.gz changes the transform in the header

**Topic ID**: 24981
**Date**: 2022-08-29
**URL**: https://discourse.slicer.org/t/exporting-file-to-nii-and-nii-gz-changes-the-transform-in-the-header/24981

---

## Post #1 by @koeglfryderyk (2022-08-29 16:06 UTC)

<p>I have an .mrb with multiple files, from which I export one to .nii.gz</p>
<p>When I load the file again, it doesn’t match the original file because it’s affine is changed (I loaded both files in Python with SimpleITK and saw that the voxel values were identical, only the origin and direction have changed)</p>
<p>This does not happen when I export this file to .nrrd.</p>
<p>I tried this with multiple versions of Slicer and it always kept happening.</p>
<p>Unfortunately I’m not allowed to share the file.</p>
<p>There are also no errors or warnings when exporting this file. Is there a way to debug this?</p>

---

## Post #2 by @pieper (2022-08-29 16:34 UTC)

<p>We’ve noticed this with other data too.  The nifti1 headers that are used by default use 32bit floats for orientation and there can be rounding error.  Avoid nifti if you can.</p>
<p>Here’s a related discussion:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/OHIF/Viewers/issues/2869">
  <header class="source">

      <a href="https://github.com/OHIF/Viewers/issues/2869" target="_blank" rel="noopener">github.com/OHIF/Viewers</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/OHIF/Viewers/issues/2869" target="_blank" rel="noopener">Segmentations converted from nii to dcm not rendered in OHIF Viewer</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-08-12" data-time="17:45:12" data-timezone="UTC">05:45PM - 12 Aug 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/ccosmin97" target="_blank" rel="noopener">
          <img alt="ccosmin97" src="https://avatars.githubusercontent.com/u/72577931?v=4" class="onebox-avatar-inline" width="20" height="20">
          ccosmin97
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Community: Report <img src="https://emoji.discourse-cdn.com/twitter/bug.png?v=12" title="bug" class="emoji" alt="bug" width="20" height="20">
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Awaiting Reproduction
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Triage <img src="https://emoji.discourse-cdn.com/twitter/white_flag.png?v=12" title="white_flag" class="emoji" alt="white_flag" width="20" height="20">
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          IDC:priority
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Hello,

I am having issues rendering dcm segmentations in OHIF Viewer(version <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">number : 4.12.30).
The segmentations come from [ProstateX IDC collection](https://portal.imaging.datacommons.cancer.gov/explore/filters/?collection_id=prostatex), converted to nii using dcmqi, then converted back to dcm using dcmqi(v 1.2.5) again.

The dcm file originating from IDC buckets is rendered properly into OHIF, however the dcm file from dcmqi conversion from nii format is not rendered properly.

Here is the error reported by the OHIF Viewer :
![error_dcm_seg_ohif (1)](https://user-images.githubusercontent.com/72577931/184412717-a8b74022-3cd5-4ba8-bfec-5b2f88d6204e.jpg)

![ohif_console (1)](https://user-images.githubusercontent.com/72577931/184412763-39d38b8c-8fd3-42c4-9e32-70f205ec2af7.jpg)

To reproduce this issue, please see this [ipynb](https://github.com/ccosmin97/IDC-Prostate_segmentation/blob/main/prostateX_patID0004_dcmqi_test.ipynb).

Additional info :

- IDC bucket dcm
  -  [metadata](https://www.dropbox.com/s/6ewb178mjujzidz/1.2.276.0.7230010.3.1.4.1070885483.15960.1599120307.702_dcm_stats?dl=0) 
  - [dcm file](https://www.dropbox.com/s/2fxtsd2blwwcop2/1.2.276.0.7230010.3.1.4.1070885483.15960.1599120307.702.dcm?dl=0)
- DCMQI converted dcm(nii -&gt; dcm)
  - [metadata](https://www.dropbox.com/s/l1rdu2315aks3xt/test_gt_0004_dcm_stats?dl=0)  
  - [dcm file](https://www.dropbox.com/s/xakvc4o4zg03ln2/test_gt_0004.dcm?dl=0)
- [Diff between two dcm metadata files](https://www.dropbox.com/s/9jszt3aa7ao5m95/diff-dcm-metadata?dl=0)

Thank you!

@fedorov</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @koeglfryderyk (2022-08-29 17:20 UTC)

<p>ok. I have three follow-up questions</p>
<ol>
<li>Is there a way of determining when the mismatch might occur?</li>
<li>Would it make sense to export to nifti2?</li>
<li>Could you elaborate on ‘Avoid nifti if you can?’</li>
</ol>

---

## Post #4 by @dzenanz (2022-09-19 15:57 UTC)

<p><a href="https://github.com/Slicer/Slicer/pull/6454" rel="noopener nofollow ugc">PR 6454</a> should fix this. Give it a try and report whether the problem still occurs.</p>

---

## Post #5 by @dzenanz (2022-09-19 16:02 UTC)

<p>PR 6454 is now part of <a href="https://download.slicer.org/" rel="noopener nofollow ugc">preview release</a>.</p>

---

## Post #6 by @koeglfryderyk (2022-10-16 12:32 UTC)

<p>The problem persists.</p>
<p>I also wrote a simple Python script that uses the newest SimpleITK version (2.2.0) to export the .nrrds in question to .nii and the same change happens.</p>
<p>From what I understood from discussions with <a class="mention" href="/u/pieper">@pieper</a>, the problem is rather with the NIFTI standard that doesn’t support shear in the affine matrix - and the files that I have problems have a non-zero shear component.</p>

---

## Post #7 by @pieper (2022-10-16 16:02 UTC)

<p><a class="mention" href="/u/koeglfryderyk">@koeglfryderyk</a> would you be able to make an example file using the header information and synthetic pixel data?  It would simplify the discussion if you provided a shareable example.  Also provide a simple example script that demonstrates the exact issue (you can be inspired by <a href="http://sscce.org/">this advice</a>.</p>
<aside class="quote no-group" data-username="koeglfryderyk" data-post="6" data-topic="24981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar"> koeglfryderyk:</div>
<blockquote>
<p>NIFTI standard that doesn’t support shear in the affine matrix</p>
</blockquote>
</aside>
<p>As I understand it the <a href="https://nifti.nimh.nih.gov/pub/dist/src/niftilib/nifti1.h">nifti reference</a> is open to interpretation here.  There are both a quaternion (no shear) and an affine matrix (could have shear) but ITK’s logic has many special cases to work with such data (e.g. see <a href="https://discourse.itk.org/t/saving-non-orthogonal-volume-in-nifti-format/2760">this discussion</a>.  This logic may or may not match the logic used by other programs, which is why I suggest avoiding the format.  If you read the nifti reference above you can see how it is very neuroimaging specific and has many special cases that have proven problematic in practice.</p>

---

## Post #8 by @koeglfryderyk (2022-10-19 14:46 UTC)

<p>Here are a few lines that will create an .nrrd with noise as data and with the header copied from one of the problematic files (you need to have numpy and pynrrd installed to run this) - the noise is big enough to visually see how the file changes after it was exported to .nii</p>
<pre><code class="lang-auto">from collections import OrderedDict
import numpy as np
import nrrd

# path to where the .nrrd file will be saved
path = "dummy.nrrd"

# the header is copied from one of the problematic .nrrd files
header = OrderedDict([('type', 'unsigned short'),
             ('dimension', 3),
             ('space', 'left-posterior-superior'),
             ('sizes', np.array([256, 256,  80])),
             ('space directions',
              np.array([[-0.82093026, -0.03815682, -0.03294253],
                     [-0.03818959,  0.81657389,  0.06732129],
                     [ 0.09523261,  0.14437391, -1.9763117 ]])),
             ('kinds', ['domain', 'domain', 'domain']),
             ('endian', 'little'),
             ('encoding', 'gzip'),
             ('space origin',
              np.array([ 110.19170784, -173.7526922 ,  101.14669097]))])

# the data array has the same size as the the file from which the header was copied, but it's just noise
data = np.random.rand(256, 256, 80)

nrrd.write(path, data, header)
</code></pre>

---

## Post #9 by @lassoan (2022-10-19 16:52 UTC)

<p>Please spread the word: do not use Nifti in non-neuroimaging applications. The much simper NRRD file format can be used instead.</p>
<p>By using Nifti file format, people maintain a continuous drain of our resources via requiring lots of user support (keep explaining issues with Nifti and what to do about it) and trying to implement and maintain complex mechanisms (to deal with redundancies and ambiguities in the Nifti format), and in general by distracting our attention from more impactful work.</p>

---

## Post #10 by @pieper (2022-10-19 17:28 UTC)

<p>Thanks for providing the concrete example <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> This does help further the investigation.</p>
<p><a class="mention" href="/u/koeglfryderyk">@koeglfryderyk</a> this matrix does have a non-trivial shear component.  Is that intended?</p>
<pre><code class="lang-auto">array([[-0.82093026, -0.03815682, -0.03294253],
       [-0.03818959,  0.81657389,  0.06732129],
       [ 0.09523261,  0.14437391, -1.9763117 ]])
&gt;&gt;&gt; numpy.dot(a[0], a[1])
-0.0020246065049000987
&gt;&gt;&gt; numpy.dot(a[0], a[2])
-0.018583473117743804
&gt;&gt;&gt; numpy.dot(a[1], a[2])
-0.01879278211341301
</code></pre>
<p>As noted in some of the links above ITK may not be consistent in handling this case (e.g. shear may be silently dropped, and that may be what’s happening in the nifti case, so the issue might not even be related to the 32 bit precision issue).</p>
<p>Shear should be handled well for viewing in Slicer but some of the ITK or VTK based filters may ignore the shear.</p>
<p>Seeing this data makes me think we should remove the ambiguity at the Slicer level.  An option could be to give users the option to factor out shear into a separate transform when loading so that the <code>vtkMRMLVolume*Node</code> classes can always expect orthogonal direction vectors.  Users could resample through the transform at the desired resolution if needed to incorporate the shear.</p>
<p>As a general rule, I suggest that people doing any kind of non-rigid registration save the transform somewhere other than the image header whenever possible.</p>

---

## Post #11 by @koeglfryderyk (2022-10-24 09:21 UTC)

<p>I’m not sure I would use the word ‘intended’ - that’s the data that we received from Brainlab and we only sometimes applied rigid transformations to it.</p>
<p>But I’ll keep saving non-rigid transformations elsewhere in mind</p>

---
