---
topic_id: 13888
title: "Not Finding Median Values In Cip"
date: 2020-10-06
url: https://discourse.slicer.org/t/13888
---

# Not finding Median values in CIP

**Topic ID**: 13888
**Date**: 2020-10-06
**URL**: https://discourse.slicer.org/t/not-finding-median-values-in-cip/13888

---

## Post #1 by @Saffana (2020-10-06 13:22 UTC)

<p>Hello</p>
<p>I am Saffana a PhD researcher in the UK working on COPD CT scans. I am currently using CIP extension to perform lung segmentation using parenchymal analysis</p>
<p>I am wondering if there is any way I can have median values, not just the mean values</p>
<p>Please can you help me with this?</p>
<p>Thank you</p>

---

## Post #2 by @raul (2020-10-06 13:42 UTC)

<p>Hi Saffana,</p>
<p>The module does not provide median values but it could be easily modify to do so.<br>
This are the lines in the SlicerCIP where the computation of the different phenotypes are performed:<br>
</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/acil-bwh/SlicerCIP/blob/develop/Scripted/CIP_ParenchymaAnalysis/CIP_ParenchymaAnalysis.py#L650-L670" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/acil-bwh/SlicerCIP/blob/develop/Scripted/CIP_ParenchymaAnalysis/CIP_ParenchymaAnalysis.py#L650-L670" target="_blank" rel="noopener nofollow ugc">acil-bwh/SlicerCIP/blob/develop/Scripted/CIP_ParenchymaAnalysis/CIP_ParenchymaAnalysis.py#L650-L670</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="650" style="counter-reset: li-counter 649 ;">
<li>self.labelStats['LAA%-950', tag] = 100.0 * (data &lt; -950).sum() / float(data.size)</li>
<li>self.labelStats['LAA%-925', tag] = 100.0 * (data &lt; -925).sum() / float(data.size)</li>
<li>self.labelStats['LAA%-910', tag] = 100.0 * (data &lt; -910).sum() / float(data.size)</li>
<li>self.labelStats['LAA%-856', tag] = 100.0 * (data &lt; -856).sum() / float(data.size)</li>
<li>self.labelStats['HAA%-700', tag] = 100.0 * (data &gt; -700).sum() / float(data.size)</li>
<li>self.labelStats['HAA%-600', tag] = 100.0 * (data &gt; -600).sum() / float(data.size)</li>
<li>self.labelStats['HAA%-500', tag] = 100.0 * (data &gt; -500).sum() / float(data.size)</li>
<li>self.labelStats['HAA%-250', tag] = 100.0 * (data &gt; -250).sum() / float(data.size)</li>
<li>self.labelStats['HAA%-600-250', tag] = 100.0 * (numpy.logical_and(data &gt; -600,</li>
<li>                                                                  data &lt; -250)).sum() / float(data.size)</li>
<li># self.labelStats[cycle,'Perc10',tag]=self.percentile(data,.1)</li>
<li># self.labelStats[cycle,'Perc15',tag]=self.percentile(data,.15)</li>
<li>self.labelStats['Perc10',tag]=numpy.percentile(data,10)</li>
<li>self.labelStats['Perc15',tag]=numpy.percentile(data,15)</li>
<li>self.labelStats['Mean', tag] = mean_data</li>
<li>self.labelStats['Std', tag] = std_data</li>
<li>self.labelStats['Kurtosis', tag] = self.kurt(data, mean_data, std_data)</li>
<li>self.labelStats['Skewness', tag] = self.skew(data, mean_data, std_data)</li>
<li>self.labelStats['Ventilation Heterogeneity', tag] =  self.vh(data)</li>
<li>self.labelStats['Mass',tag] = self.mass(data,cubicMMPerVoxel)</li>
<li>self.labelStats['Volume', tag] = data.size * cubicMMPerVoxel * litersPerCubicMM</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
You could extend this list of phenotypes with your own operation.
<p>An alternative approach, it is directly used the mask to build your own module that computes the quantities that you want to explore.</p>
<p>I hope this helps</p>
<p>Raul</p>

---

## Post #3 by @Saffana (2020-10-06 14:10 UTC)

<p>Hi Raul</p>
<p>Thank you for your reply</p>
<p>Unfortunately, I don’t have any programming background I am from the medical field only to perform CT scan analysis</p>
<p>can you please tell me if there is any way in the software without coding or programming?</p>
<p>Thank you</p>
<p>Saffana</p>

---
