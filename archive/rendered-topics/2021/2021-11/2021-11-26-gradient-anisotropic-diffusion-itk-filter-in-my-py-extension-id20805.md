# Gradient Anisotropic Diffusion itk filter in my .py extension

**Topic ID**: 20805
**Date**: 2021-11-26
**URL**: https://discourse.slicer.org/t/gradient-anisotropic-diffusion-itk-filter-in-my-py-extension/20805

---

## Post #1 by @aaregar (2021-11-26 19:57 UTC)

<p>Operating system: w10<br>
Slicer version: 4.11</p>
<p>Hi!!<br>
I’m trying to include in my in-house Extension the possibility to generate a filtered version of a selected volume using Gradient Anisotropic Diffusion itk filter. The parameters (conductance, iterations…) would be fixed in my .py, with no GUI, so my unique outcome after pushing the “Start” button would be generate the new filtered volume.<br>
I followed this notebook ( <a href="http://insightsoftwareconsortium.github.io/SimpleITK-Notebooks/Python_html/300_Segmentation_Overview.html" class="inline-onebox" rel="noopener nofollow ugc">300_Segmentation_Overview</a> ) but the arguments seems to fail.</p>
<p>Coul you please help me?<br>
Thanks!</p>

---

## Post #2 by @lassoan (2021-11-28 04:19 UTC)

<aside class="quote no-group" data-username="aaregar" data-post="1" data-topic="20805">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/6f9a4e/48.png" class="avatar"> aaregar:</div>
<blockquote>
<p>but the arguments seems to fail.</p>
</blockquote>
</aside>
<p>Please provide the code that you are running and the error message you get.</p>
<p>Alternatively, since these ITK filters are \available in CLI modules (“Curvature Anisotropic Diffusion” and “Gradient Anisotropic Diffusion” modules), you can perform this filtering from Python as described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-run-a-cli-module-from-python">here</a>.</p>

---

## Post #3 by @aaregar (2021-11-29 15:40 UTC)

<p>Thank you for your quick response!<br>
I tried what you put forward above using these lines:<br>
outputVolume = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLScalarVolumeNode”)<br>
outputVolume.SetName(’{}-GADFILTER’.format(inputVolume.GetName()))</p>
<pre><code>        parameters = {}
        parameters["inputVolume"] = inputVolume.GetID()
        parameters["outputVolume"] = outputVolume.GetID()
        parameters["useImageSpacing"] = True
        parameters["conductance"] = 0.9
        parameters["numberOfIterations"] = 7
        parameters["timeStep"] = 0.0625
        print(parameters)

        cliNode = slicer.cli.run(slicer.modules.gradientanisotropicdiffusion, None, parameters)
</code></pre>
<p>The output volume is created but as Invalid Volume, with no spatial information. Should I clone the  input and then apply the filter? I’m not sure in which step it is the trouble.</p>
<p>Thank you!</p>

---

## Post #4 by @lassoan (2021-11-29 16:07 UTC)

<p>You need to use <code>runSync</code> or wait for the execution to complete. See details at the link in my previous post.</p>

---
