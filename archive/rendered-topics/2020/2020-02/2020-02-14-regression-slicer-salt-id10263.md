# Regression slicer SALT

**Topic ID**: 10263
**Date**: 2020-02-14
**URL**: https://discourse.slicer.org/t/regression-slicer-salt/10263

---

## Post #1 by @JON (2020-02-14 17:18 UTC)

<p>Hi <a class="mention" href="/u/bpaniagua">@bpaniagua</a> and others,</p>
<p>I have a question regarding the regression tool in slicer SALT.  I have longitudinal data (2 timepoints) for a group of patients and controls. I want to see where and how much (and also preferably test for this) the shape changes from timepoint 1 to tp 2. When I use the regression tool in SlicerSALT, I can only specify a minimum of 10 timepoints, however in the timepoints range I can set it to 1 to 2, and in the setup of the model this is also possible. Does this mean that the regression computation tool computes a projection(regression) for 10 timepoints based on the two timepoints I input?</p>
<p>Thanks in advance, and looking forward to hearing from you!</p>
<p>Best,<br>
Jasper</p>

---

## Post #2 by @jfishbaugh (2020-03-05 17:54 UTC)

<p>Hi Jasper,</p>
<p>First, about the number of time points. This setting refers to the time discretization, that is the number of points between the earliest and latest observation. If number of time points is 20, your output will consist of a sequence of 20 shapes. I hope this explanation makes sense.</p>
<p>To address your main question, the regression module in SlicerSALT is intended for longitudinal data with at least 3 time points. There is a way to use the regression module for registration with only 2 timepoints, but it is currently not available through SALT.</p>
<p>You can still use the command line application <strong>shape4D</strong> which comes with SALT at the path lib/SlicerSALT-4.11/cli-modules (your directory may have a different version name). Here is an example driver xml file.</p>
<pre><code>&lt;?xml version="1.0"&gt;
&lt;experiment name="RegistrationExample"&gt;
  &lt;algorithm name="RegressionVelocity"&gt;
    &lt;source&gt;
      &lt;input&gt;
        &lt;shape&gt;/path/to/your/shape_timepoint_1.vtk&lt;/shape&gt;
      &lt;/input&gt;
      &lt;sigmaV&gt; 15.0 &lt;/sigmaV&gt;
      &lt;gammaR&gt; 0.01 &lt;/gammaR&gt;
      &lt;t0&gt; 0 &lt;/t0&gt;
      &lt;tn&gt; 1 &lt;/tn&gt;
      &lt;T&gt; 20 &lt;/T&gt;
      &lt;kernelType&gt; p3m &lt;/kernelType&gt;
      &lt;estimateBaseline&gt; 0 &lt;/estimateBaseline&gt;
      &lt;useFista&gt; 0 &lt;/useFista&gt;
      &lt;breakRatio&gt; 1e-8 &lt;/breakRatio&gt;
      &lt;maxIters&gt; 1000 &lt;/maxIters&gt;
      &lt;output&gt;
        &lt;saveProgress&gt; 100 &lt;/saveProgress&gt;
        &lt;dir&gt; /path/to/output-dir/ &lt;/dir&gt;
        &lt;prefix&gt;out_shape_&lt;/prefix&gt;
      &lt;/output&gt;
    &lt;/source&gt;
    &lt;targets&gt;
      &lt;target&gt;
        &lt;shape&gt;/path/to/shape_timepoint_2.vtk&lt;/shape&gt;
        &lt;type&gt;SURFACE&lt;/type&gt;
        &lt;tris&gt;0&lt;/tris&gt;
        &lt;sigmaW&gt;12&lt;/sigmaW&gt;
        &lt;timept&gt;1&lt;/timept&gt;
        &lt;weight&gt;1&lt;/weight&gt;
      &lt;/target&gt;
    &lt;/targets&gt;
  &lt;/algorithm&gt;
&lt;/experiment&gt;
</code></pre>
<p>You may have to change values of sigmaV, gammaR, and sigmaW to better suit your specific data.</p>
<p>Let me know if you are unfamiliar with running command line applications and need more assistance.</p>
<p>Cheers,<br>
James</p>

---
