---
topic_id: 8644
title: "Error While Running Gradqc"
date: 2019-10-01
url: https://discourse.slicer.org/t/8644
---

# Error while running GradQC

**Topic ID**: 8644
**Date**: 2019-10-01
**URL**: https://discourse.slicer.org/t/error-while-running-gradqc/8644

---

## Post #1 by @nabin (2019-10-01 21:11 UTC)

<p>Dear Slicer team,</p>
<p>I am trying to run the module GradQC to check the quality of my diffusion data and it’s supposed to be a simple process which should work by giving input as my dwi.nii.gz file and run it but it throws an error as follow. Your support will be highly appreciated.<br>
Thank you.<br>
Nabin</p>
<p><strong>Error:</strong></p>
<p>diffusionQC standard error:</p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-28257/DiffusionQC/lib/Slicer-4.10/cli-modules/diffusionQC.py”, line 57, in<br>
QC.run()<br>
File “/Applications/Slicer.app/Contents/Extensions-28257/DiffusionQC/lib/python2.7/site-packages/plumbum/cli/application.py”, line 572, in run<br>
retcode = inst.main(*tailargs)<br>
File “/Applications/Slicer.app/Contents/Extensions-28257/DiffusionQC/lib/Slicer-4.10/cli-modules/diffusionQC.py”, line 53, in main<br>
process(self.dwi, self.mask, self.out, self.autoMode)<br>
File “/Applications/Slicer.app/Contents/Extensions-28257/DiffusionQC/lib/python2.7/site-packages/diffusionqclib/gradient_process.py”, line 197, in process<br>
hdr, mri, grad_axis, slice_axis, b_value, gradients = dwi_attributes(dwiPath)<br>
File “/Applications/Slicer.app/Contents/Extensions-28257/DiffusionQC/lib/python2.7/site-packages/diffusionqclib/dwi_attributes.py”, line 8, in dwi_attributes<br>
dwi= nrrd.read(file_name)<br>
File “/Applications/Slicer.app/Contents/Extensions-28257/DiffusionQC/lib/python2.7/site-packages/nrrd/reader.py”, line 503, in read<br>
header = read_header(fh, custom_field_map)<br>
File “/Applications/Slicer.app/Contents/Extensions-28257/DiffusionQC/lib/python2.7/site-packages/nrrd/reader.py”, line 247, in read_header<br>
header_size += _validate_magic_line(magic_line)<br>
File “/Applications/Slicer.app/Contents/Extensions-28257/DiffusionQC/lib/python2.7/site-packages/nrrd/reader.py”, line 183, in _validate_magic_line<br>
raise NRRDError(‘Invalid NRRD magic line. Is this an NRRD file?’)<br>
nrrd.errors.NRRDError: Invalid NRRD magic line. Is this an NRRD file?</p>

---

## Post #2 by @tbillah (2019-10-02 02:43 UTC)

<p>Hi <a class="mention" href="/u/nabin">@nabin</a>,</p>
<p>Our tool is NRRD only. As you might already know, Slicer can load only NRRD 4D image, not NIFTI 4D image.</p>
<p>For future reference, here is the Tutorial for GradQC:</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="15" height="15">
      <a href="https://github.com/pnlbwh/SlicerDiffusionQC" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars0.githubusercontent.com/u/3407942?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/pnlbwh/SlicerDiffusionQC" target="_blank" rel="nofollow noopener">pnlbwh/SlicerDiffusionQC</a></h3>

<p>Quality checking of DWMRI. Contribute to pnlbwh/SlicerDiffusionQC development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>However, you can use my NIFTI–&gt;NRRD conversion tool, obtain an NHDR for the NIFTI image you are trying to GradQC and then load the NHDR header seamlessly to perform GradQC on it.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/pnlbwh/conversion/blob/master/conversion/nhdr_write.py" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/pnlbwh/conversion/blob/master/conversion/nhdr_write.py" target="_blank" rel="nofollow noopener">pnlbwh/conversion/blob/master/conversion/nhdr_write.py</a></h4>
<pre><code class="lang-py">#!/usr/bin/env python

import numpy as np
import argparse
import os, warnings, sys
# with warnings.catch_warnings():
#     warnings.filterwarnings("ignore", category=FutureWarning)
import nibabel as nib

PRECISION= 17
np.set_printoptions(precision= PRECISION, suppress= True, floatmode= 'maxprec')

from conversion.bval_bvec_io import read_bvecs, read_bvals, bvec_scaling

def matrix_string(A):
    # A= np.array(A)
    
    A= str(A.tolist())
    A= A.replace(', ',',')
    A= A.replace('],[',') (')
</code></pre>

  This file has been truncated. <a href="https://github.com/pnlbwh/conversion/blob/master/conversion/nhdr_write.py" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Let me know if you need more help.</p>
<p>-Tashrif</p>

---

## Post #3 by @nabin (2019-10-02 12:45 UTC)

<p>Thanks a lot Tashrif. I will try with this converting it to nrrd format.</p>
<p>Best,</p>
<p>Nabin</p>

---
