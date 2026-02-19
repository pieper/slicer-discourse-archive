---
topic_id: 7198
title: "Macos Python Problem"
date: 2019-06-17
url: https://discourse.slicer.org/t/7198
---

# MacOS Python Problem

**Topic ID**: 7198
**Date**: 2019-06-17
**URL**: https://discourse.slicer.org/t/macos-python-problem/7198

---

## Post #1 by @iPsych (2019-06-17 10:29 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38ae37d375aac065672d80defe682f4aaabff257.png" data-download-href="/uploads/short-url/85pZVxplnmvvKjHGXNbZd25BwG3.png?dl=1" title="46%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38ae37d375aac065672d80defe682f4aaabff257_2_400x500.png" alt="46%20PM" data-base62-sha1="85pZVxplnmvvKjHGXNbZd25BwG3" width="400" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38ae37d375aac065672d80defe682f4aaabff257_2_400x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38ae37d375aac065672d80defe682f4aaabff257_2_600x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38ae37d375aac065672d80defe682f4aaabff257.png 2x" data-dominant-color="FCF6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">46%20PM</span><span class="informations">659×822 46.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The nightly version (1.1) 2019-06-14 doesn’t work in Mac.<br>
It can display .vtk files when imported, but Can’t process ANY SPHARM process.<br>
I also tested stable (1.0) version, but same issue.<br>
It’s weird since SlicerSalt seems embed it’s own python.</p>
<p>Any successful test is existing in Mac environment?</p>

---

## Post #2 by @bpaniagua (2019-06-18 20:49 UTC)

<p>Hi <a class="mention" href="/u/ipsych">@iPsych</a></p>
<p>Does this also happen with input volumes? i.e. nrrd type data?</p>
<p>Thanks,<br>
Bea</p>
<p>cc. <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #3 by @jcfr (2019-06-18 20:52 UTC)

<p>This is related to transition of Slicer to Python3 and should be reproducible in any environment.</p>
<p>Could you provide an example dataset along with the steps allowing to reproduce the problem ? Thanks</p>

---

## Post #4 by @iPsych (2019-06-24 01:58 UTC)

<p>I thought that it may possible interruption by Anaconda  python environments.<br>
I found python3.6m in the package, and it should work properly.<br>
However, the same error happens when<br>
1)run SPHARM-PDM generator<br>
2)Set input and output directory (input directory contains segmented .nii file.)</p>
<p>Tested in both system with and without anaconda environment. Same error happens.</p>

---

## Post #6 by @iPsych (2019-06-27 05:46 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a><br>
I found the errors.<br>
Please refer the comment of link below.<br>
<a href="https://tickets.metabrainz.org/browse/PICARD-1328" rel="nofollow noopener">https://tickets.metabrainz.org/browse/PICARD-1328</a></p>
<p>In MacOS, to run the python codes, all the strings seem to change to byte as below.</p>
<pre><code>exts = [".gipl", ".gipl.gz", ".mgh", ".mgh,gz", ".nii", ".nii.gz",".nrrd", ".vtk", ".vtp", ".hdr", ".mhd"]
</code></pre>
<p>to</p>
<pre><code>exts = [b'.gipl', b'.gipl.gz', b'.mgh', b'.mgh,gz', b'.nii', b'.nii.gz',b'.nrrd', b'.vtk', b'.vtp', b'.hdr', b'.mhd']
</code></pre>
<p>and</p>
<pre><code>SPHARMMeshRootname = SPHARMMeshOutputDirectory + "/" + self.inputRootname + "_flip" + flipName[i - 1] + "_pp_surf"
</code></pre>
<p>to</p>
<pre><code>SPHARMMeshRootname = SPHARMMeshOutputDirectory + b'/' + self.inputRootname + b'_flip' + flipName[i - 1] + b'_pp_surf'
</code></pre>
<p>(and all the lines like above).</p>
<p>I believe there might be a smart way to resolve it.<br>
Currently, it seems the Python part will work in Windows but not in the MacOS.</p>

---
