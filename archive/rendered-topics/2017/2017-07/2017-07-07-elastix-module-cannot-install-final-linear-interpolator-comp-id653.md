---
topic_id: 653
title: "Elastix Module Cannot Install Final Linear Interpolator Comp"
date: 2017-07-07
url: https://discourse.slicer.org/t/653
---

# Elastix module cannot install "Final Linear Interpolator" component

**Topic ID**: 653
**Date**: 2017-07-07
**URL**: https://discourse.slicer.org/t/elastix-module-cannot-install-final-linear-interpolator-component/653

---

## Post #1 by @Prashant_Pandey (2017-07-07 20:15 UTC)

<p>Hi all,</p>
<p>I’m using Elastix to do rigid registration in slicer. However, when I use the option (ResampleInterpolator “FinalLinearInterpolator”) in the elastix parameter file, I get an error (from the log file):</p>
<pre><code>Installing all components.
InstallingComponents was successful.

Error:
FinalLinearInterpolator(index 3) - This component is not installed!
ERROR: error occurred while creating ResampleInterpolator 0.

itk::ExceptionObject (000000000012EE58)
Location: "unknown"
File: C:\D\N\E-0\SlicerElastix-build\elastix\src\Core\Kernel\elxElastixMain.cxx
Line: 819
Description: itk::ERROR: ElastixMain(0000000003BCA930): The following component could not be created: FinalLinearInterpolator


ERROR:
One or more components could not be created.
Errors occurred!
vtkDebugLeaks has found no leaks.
Error: 
</code></pre>
<p>When I use this parameter file directly with elastix outside slicer, there are no errors and the registration is successful. Any reason why the linear resample interpolator does not work?</p>
<p>Thanks,<br>
Prash</p>

---

## Post #2 by @Prashant_Pandey (2017-07-07 20:17 UTC)

<p>In fact I have noticed that only the B-spline resample interpolator seems to work in Slicer.<br>
<code>(ResampleInterpolator "FinalBSplineInterpolator")</code></p>

---

## Post #3 by @lassoan (2017-07-07 20:18 UTC)

<p>It seems that you have a different installation of Elastix than the one bundled with 3D Slicer (it may be either newer or older, or built with different options). If you prefer to use your local installation then specify the path of your local Elastix in the Advanced section / Custom Elastix toolbox location.</p>

---

## Post #4 by @lassoan (2017-07-07 20:32 UTC)

<aside class="quote no-group" data-username="Prashant_Pandey" data-post="2" data-topic="653">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/c0e974/48.png" class="avatar"> Prashant_Pandey:</div>
<blockquote>
<p>In fact I have noticed that only the B-spline resample interpolator seems to work in Slicer.</p>
</blockquote>
</aside>
<p>B-spline gives higher quality results than linear resampling and typically it is not significantly slower. I would recommend to use that instead of linear.</p>

---

## Post #5 by @Prashant_Pandey (2017-07-07 20:32 UTC)

<p>I see, thanks. Is there documentation on the version of Elastix bundled with slicer and the available modules that can be configured in the parameter file?</p>
<p>Thanks,<br>
Prash</p>

---

## Post #6 by @lassoan (2017-07-07 20:45 UTC)

<p>It’s the latest Elastic version built with default options. If you have any specific request for enabling an additional option then modify the build options <a href="https://github.com/lassoan/SlicerElastix/blob/master/SuperBuild/External_elastix.cmake">here</a> and send a pull request.</p>
<p>Probably the linear interpolator is not included by default for a good reason - but you can double-check that with Elastix developers.</p>

---

## Post #7 by @Prashant_Pandey (2017-07-07 21:01 UTC)

<p>Okay, thanks for the advice!<br>
On a somewhat related note, I’ve noticed that the transform output by the elastix module is a displacement field. In the case of a rigid registration, it would be nice to get a homogeneous matrix composed of a rotation and translation. Is there a way in slicer to get this representation from the elastix output?</p>

---

## Post #8 by @lassoan (2017-07-07 21:31 UTC)

<p>Yes, it would be nice. Unfortunately, elastix cannot write registration result to an ITK transform. As soon as this feature will be added to Elastix, I can add it to SlicerElastix. I would recommend to submit a feature request at <a href="https://github.com/SuperElastix/elastix/issues">https://github.com/SuperElastix/elastix/issues</a>.</p>

---
