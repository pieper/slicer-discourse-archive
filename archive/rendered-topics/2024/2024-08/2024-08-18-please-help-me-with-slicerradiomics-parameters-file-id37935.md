---
topic_id: 37935
title: "Please Help Me With Slicerradiomics Parameters File"
date: 2024-08-18
url: https://discourse.slicer.org/t/37935
---

# Please help me with SlicerRadiomics parameters file

**Topic ID**: 37935
**Date**: 2024-08-18
**URL**: https://discourse.slicer.org/t/please-help-me-with-slicerradiomics-parameters-file/37935

---

## Post #1 by @hongneo55 (2024-08-18 23:22 UTC)

<aside class="onebox githubblob" data-onebox-src="https://github.com/AIM-Harvard/pyradiomics/blob/master/examples/exampleSettings/Params.yaml">
  <header class="source">

      <a href="https://github.com/AIM-Harvard/pyradiomics/blob/master/examples/exampleSettings/Params.yaml" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/AIM-Harvard/pyradiomics/blob/master/examples/exampleSettings/Params.yaml" target="_blank" rel="noopener nofollow ugc">AIM-Harvard/pyradiomics/blob/master/examples/exampleSettings/Params.yaml</a></h4>


      <pre><code class="lang-yaml"># This is an example of a parameters file
# It is written according to the YAML-convention (www.yaml.org) and is checked by the code for consistency.
# Three types of parameters are possible and reflected in the structure of the document:
#
# Parameter category:
#   Setting Name: &lt;value&gt;
#
# The three parameter categories are:
# - setting: Setting to use for preprocessing and class specific settings. if no &lt;value&gt; is specified, the value for
#   this setting is set to None.
# - featureClass: Feature class to enable, &lt;value&gt; is list of strings representing enabled features. If no &lt;value&gt; is
#   specified or &lt;value&gt; is an empty list ('[]'), all features for this class are enabled.
# - imageType: image types to calculate features on. &lt;value&gt; is custom kwarg settings (dictionary). if &lt;value&gt; is an
#   empty dictionary ('{}'), no custom settings are added for this input image.
#
# Some parameters have a limited list of possible values. Where this is the case, possible values are listed in the
# package documentation

# Settings to use, possible settings are listed in the documentation (section "Customizing the extraction").
setting:
</code></pre>



  This file has been truncated. <a href="https://github.com/AIM-Harvard/pyradiomics/blob/master/examples/exampleSettings/Params.yaml" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I am having difficulty creating a parameter file. Struggling to make a file capable of → <br>
filter types: original, square, logarithm, exponential, wavelet<br>
feature types: first order, texture, shape</p>
<p>It would be greatly thankful if you give me a file capable of this. Want to extract radiomics as much as possible</p>

---
