# Averaging Model To Model Distances & Getting Value

**Topic ID**: 8211
**Date**: 2019-08-28
**URL**: https://discourse.slicer.org/t/averaging-model-to-model-distances-getting-value/8211

---

## Post #1 by @stevenagl12 (2019-08-28 16:56 UTC)

<p>Does anyone know if there is a straightforward way to average the calculated model to model distance models from several samples? This way you can show the average deformation? Also, can you use model to model distance to calculate the total distance between models as a single value?</p>

---

## Post #2 by @lassoan (2019-08-29 00:17 UTC)

<p>You can retrieve displacement values as a numpy array using <code>slicer.util.arrayFromModelPointData</code> and average it using standard numpy operations.</p>

---

## Post #3 by @ytaneja (2019-09-11 21:42 UTC)

<p>Would it be possible for you to elaborate on this a bit? I’m confused as to what the “numpy array” is and where it is outputted after running that command in the Python Interactor</p>
<p>Thank you!</p>

---

## Post #4 by @bpaniagua (2019-09-12 14:35 UTC)

<p>Yash,</p>
<p>Could you please let us know your experimental set up?<br>
i.e. i have X models with Y points, I want to do Z</p>
<p>Thanks,<br>
Bea</p>

---

## Post #5 by @ytaneja (2019-09-12 18:03 UTC)

<p>Yes <a class="mention" href="/u/bpaniagua">@bpaniagua</a>, I have two models through which I successfully performed the ModelToModelDistance module and this outputted a third model which I have been analyzing using the ShapePopulationViewer module. Though viewing the results using a colormap generated through this process is helpful, I would like to access the numbers behind the colormap to perform further quantitative processing.</p>
<p>Thank you,<br>
Yash</p>

---

## Post #6 by @lassoan (2019-09-12 18:23 UTC)

<aside class="quote no-group" data-username="ytaneja" data-post="3" data-topic="8211">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/bbe5ce/48.png" class="avatar"> ytaneja:</div>
<blockquote>
<p>Would it be possible for you to elaborate on this a bit? I’m confused as to what the “numpy array” is and where it is outputted after running that command in the Python Interactor</p>
</blockquote>
</aside>
<p><code>distances = slicer.util.arrayFromModelPointData(modelNode,'someArrayName')</code> returns a numpy array that you can process any way you want. You can get point coordinates by calling <code>point_coords = slicer.util.arrayFromModelPoints(modelNode)</code>.</p>
<aside class="quote no-group" data-username="ytaneja" data-post="5" data-topic="8211">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/bbe5ce/48.png" class="avatar"> ytaneja:</div>
<blockquote>
<p>I would like to access the numbers behind the colormap to perform further quantitative processing</p>
</blockquote>
</aside>
<p>Lots of analysis tools are available in VTK, SlicerSALT, Slicer, numpy, and various Python packages. We can help more if you can be more specific about what you want to compute.</p>

---

## Post #7 by @ytaneja (2019-09-12 18:51 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thank you for your response. The code still does not work in the Python Interactor – it keeps saying that modelNode is not defined. Maybe the modelNode variable is not accessible just by the Interactor. What do you think?</p>
<p>Also, I am aware of the other modules, but I think that all the analysis I wish to perform can be done if we can get this numpy array to output properly</p>
<p>Thank you!<br>
Yash</p>

---

## Post #8 by @ytaneja (2019-09-12 19:07 UTC)

<p>Another question I had about the Model To Model Distances module is what units does it measure distance in for the colorbar? I’m thinking pixels or micrometers, are either of these correct?</p>

---

## Post #9 by @ytaneja (2019-09-12 19:34 UTC)

<p>Update: I was able to generate an array by importing my .vtk file into ParaView and exporting as .csv. However, now I am confused as to what the array means. There are 3 columns and the amount of rows correspond to the amount of points in my vtk. I’m thinking they mean x, y, z but I am not sure, could you confirm this for me? <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/2176432d034025bc72d1fbfa4f6518bb8b6e309f.png" data-download-href="/uploads/short-url/4M18dyOApuyAY0utDjfkWICILVl.png?dl=1" title="Snapshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/2176432d034025bc72d1fbfa4f6518bb8b6e309f.png" alt="Snapshot" data-base62-sha1="4M18dyOApuyAY0utDjfkWICILVl" width="169" height="500" data-dominant-color="E7E7E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snapshot</span><span class="informations">189×556 4.39 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @ytaneja (2019-09-16 19:11 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/bpaniagua">@bpaniagua</a> Could you please refer to my questions above? I just need to confirm units and the meanings behind each column of data. Thank you!</p>

---

## Post #11 by @lassoan (2019-09-17 04:37 UTC)

<aside class="quote no-group" data-username="ytaneja" data-post="7" data-topic="8211">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/bbe5ce/48.png" class="avatar"> ytaneja:</div>
<blockquote>
<p>The code still does not work in the Python Interactor – it keeps saying that modelNode is not defined</p>
</blockquote>
</aside>
<p>Replace <code>modelNode</code> with the variable that refers to your model node. In the Python interactor you typically get is using <code>modelNode = slicer.util.getNode('Put your model node name here')</code>, while in a scripted module you usually get it from a node selector widget.</p>
<aside class="quote no-group" data-username="ytaneja" data-post="10" data-topic="8211">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/bbe5ce/48.png" class="avatar"> ytaneja:</div>
<blockquote>
<p>I just need to confirm units and the meanings behind each column of data.</p>
</blockquote>
</aside>
<p>Distances are computed in the same units as you used for point coordinates. In medical image computing, physical coordinate system unit is typically millimeter.</p>
<p>I don’t know what data you found in ParaView. You can get point coordinates, distances, etc. as I described above.</p>

---
