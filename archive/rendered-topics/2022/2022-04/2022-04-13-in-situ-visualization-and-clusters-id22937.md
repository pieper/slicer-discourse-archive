# In situ visualization and clusters

**Topic ID**: 22937
**Date**: 2022-04-13
**URL**: https://discourse.slicer.org/t/in-situ-visualization-and-clusters/22937

---

## Post #1 by @fbordignon (2022-04-13 12:59 UTC)

<p>Hello everyone. 3D Slicer has been great the past 3 years that we customized it to the O&amp;G industry. We did not release GeoSlicer to the market yet, but we’ve achieved great improvement over the traditional workflows on the industry. We’ve developed closed source extensions and had great support from the community. We’ve tried to give back as much as possible. We are super grateful to everyone that helped.<br>
Now we’ve come to a next step where a single workstation is simply not enough to render and process the workflows from the O&amp;G industry. I’ve came across the in situ visualizations capabilities of Paraview. With that I was able to render a 4TB volume using 32 cluster nodes in almost real time. I wonder how hard would it be to implement similar data/render server-client model into 3D Slicer. Since both platforms are based on vtk, how hard could it be, right?<br>
We have an opportunity to compete for an 18 months project. It would need to integrate the processing and rendering on a cluster. I guess what I am asking here is for input if that would be possible. If it is something that would need to completely revamp 3D Slicer core or it would be like a somewhat simpler adaptation. We would like to make this capabilities available to the community if we succeed in this endeavor. I appreciate any input on this matter. Thanks!</p>

---

## Post #2 by @lassoan (2022-04-13 13:50 UTC)

<p>One approach could be to combine ParaView and Slicer. Combination/integration could happen at many different levels.</p>
<p>Another approach would be to leverage modern Python-based tools for managing large data in Slicer. For example, store images in <a href="https://ngff.openmicroscopy.org/latest/">NGFF format</a> and retrieve image tiles in the appropriate resolution from the visible parts of the volume, process data using ITK out-of-core processing features.</p>

---

## Post #3 by @fbordignon (2022-04-13 14:03 UTC)

<p>Thanks, Andras. Thinking about the processing part, I believe can be done with the slicer cli system, so we can use almost the same python code to run things locally or on the cluster. But the visualization part is still a mystery for me. The integration of ParaView and Slicer you mentioned would aim to allow for something like Slicer to connect to a pvserver and show a ParaView rendering window inside Slicer?</p>

---

## Post #4 by @jcfr (2022-04-13 14:22 UTC)

<p><a class="mention" href="/u/fbordignon">@fbordignon</a> Thanks for the summary and for raising these questions.</p>
<p>From a high level, scaling up Slicer capabilities to support dealing if very large datasets makes sense.</p>
<p>As <a class="mention" href="/u/lassoan">@lassoan</a> pointed out, this could happen a many different level. To understand the “right” level of integration and how to prioritize the work, having a better idea of the bottle neck could make sense.</p>
<p>We could envision Slicer being a paraview catalyst <sup class="footnote-ref"><a href="#footnote-76676-1" id="footnote-ref-76676-1">[1]</a></sup> client, we would have to figure out which Slicer and VTK capabilities would need to be consolidated to support use in this scenario:</p>
<ul>
<li>segment editor effect and associated effect (could we narrow down the list ?)</li>
<li>update of <code>vtkSegmentationCore</code> to be a first class VTK &amp; Paraview module</li>
<li>…</li>
</ul>
<p><a class="mention" href="/u/fbordignon">@fbordignon</a> <a class="mention" href="/u/lassoan">@lassoan</a>  What do you think if I schedule a meeting with members of the Paraview team and us three to help sketch our a plan ?</p>
<p>I would also like to involve <a class="mention" href="/u/thewtex">@thewtex</a> working on the ITK side as scaling that part is also sensible.</p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-76676-1" class="footnote-item">
<p><a href="https://www.paraview.org/in-situ/" class="inline-onebox">In situ | ParaView</a> <a href="#footnote-ref-76676-1" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #5 by @fbordignon (2022-04-13 16:31 UTC)

<p>Hey <a class="mention" href="/u/jcfr">@jcfr</a> sure I will be happy to give my two cents on this subject. Reach me on fernando at ltrace.com.br<br>
Thanks!</p>

---

## Post #6 by @jcfr (2022-04-13 21:49 UTC)

<aside class="quote no-group" data-username="fbordignon" data-post="5" data-topic="22937">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fbordignon/48/5269_2.png" class="avatar"> fbordignon:</div>
<blockquote>
<p>will be happy to give my two cents on this subject</p>
</blockquote>
</aside>
<p>Great. I will follow up by email. Likely on Monday so that I can coordinate few things with the teams.</p>

---
