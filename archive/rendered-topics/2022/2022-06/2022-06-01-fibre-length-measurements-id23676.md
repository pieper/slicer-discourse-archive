---
topic_id: 23676
title: "Fibre Length Measurements"
date: 2022-06-01
url: https://discourse.slicer.org/t/23676
---

# Fibre length measurements

**Topic ID**: 23676
**Date**: 2022-06-01
**URL**: https://discourse.slicer.org/t/fibre-length-measurements/23676

---

## Post #1 by @njeffery (2022-06-01 18:47 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0830d648bec096afe29555a95fa4c06049600d14.jpeg" data-download-href="/uploads/short-url/1ass40qSnX96JgKpJxYjpUJ7Tww.jpeg?dl=1" title="BundleNJ" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0830d648bec096afe29555a95fa4c06049600d14_2_690x385.jpeg" alt="BundleNJ" data-base62-sha1="1ass40qSnX96JgKpJxYjpUJ7Tww" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0830d648bec096afe29555a95fa4c06049600d14_2_690x385.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0830d648bec096afe29555a95fa4c06049600d14_2_1035x577.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0830d648bec096afe29555a95fa4c06049600d14_2_1380x770.jpeg 2x" data-dominant-color="929CD1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">BundleNJ</span><span class="informations">1427×797 203 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Hi 3Dslicer community</p>
<p>Hoping someone has a solution out there. I have a vtk file with about 300 fibres in it. I need the length of each fibre. Seems a trivial task but I cannot find a solution.</p>
<p>Diffusion&gt;quantify&gt;tractography measurements will give the mean but there are lots of outliers, so its not representative. Need the median.</p>
<p>PS. I have tried the whitematteranalysis as well and cannot get it to work.</p>
<p>Do I need to use a different DTI package?</p>
<p>Any suggestions greatly appreciated.<br>
cheers<br>
NJ</p>
<p>Operating system:Windows 10<br>
Slicer version:5.02<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @zhangfanmark (2022-06-01 19:03 UTC)

<p>Hi <a class="mention" href="/u/njeffery">@njeffery</a></p>
<p>You can WMA to do this. Here is the function:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerDMRI/whitematteranalysis/blob/8dc9674e125971ff039b38a1911444550049cf0e/whitematteranalysis/filter.py#L99">
  <header class="source">

      <a href="https://github.com/SlicerDMRI/whitematteranalysis/blob/8dc9674e125971ff039b38a1911444550049cf0e/whitematteranalysis/filter.py#L99" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerDMRI/whitematteranalysis/blob/8dc9674e125971ff039b38a1911444550049cf0e/whitematteranalysis/filter.py#L99" target="_blank" rel="noopener nofollow ugc">SlicerDMRI/whitematteranalysis/blob/8dc9674e125971ff039b38a1911444550049cf0e/whitematteranalysis/filter.py#L99</a></h4>



    <pre class="onebox">      <code class="lang-py">
        <ol class="start lines" start="89" style="counter-reset: li-counter 88 ;">
            <li>        pd2 = downsample(pd, fibers_per_bin,verbose=False)</li>
            <li>        if verbose:</li>
            <li>            print(pd2.GetNumberOfLines(), "fibers in length range:", [bin_low, bin_hi])</li>
            <li>        if (vtk.vtkVersion().GetVTKMajorVersion() &gt;= 6.0):</li>
            <li>            appender.AddInputData(pd2)</li>
            <li>        else:</li>
            <li>            appender.AddInput(pd2)</li>
            <li>    appender.Update()</li>
            <li>    return(appender.GetOutput())</li>
            <li>
            </li>
<li class="selected">def compute_lengths(inpd):</li>
            <li>    """Compute length of each fiber in polydata. Returns lengths and step size.</li>
            <li>
            </li>
<li>    Step size is estimated using points in the middle of a fiber with over 15 points.</li>
            <li>
            </li>
<li>    """</li>
            <li>
            </li>
<li>    # Make sure we have lines and points.</li>
            <li>    if (inpd.GetNumberOfLines() == 0) or (inpd.GetNumberOfPoints() == 0):</li>
            <li>        print("&lt;filter.py&gt; No fibers found in input polydata.")</li>
            <li>        return 0, 0</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It seems you have tried WMA. Wonder what you meant that you cannot get it to work. Is it an installation problem?</p>
<p>Thanks,<br>
Fan</p>

---
