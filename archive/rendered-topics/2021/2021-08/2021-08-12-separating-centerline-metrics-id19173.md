# Separating centerline metrics

**Topic ID**: 19173
**Date**: 2021-08-12
**URL**: https://discourse.slicer.org/t/separating-centerline-metrics/19173

---

## Post #1 by @som1197 (2021-08-12 18:18 UTC)

<p>Hello,</p>
<p>I want to isolate parameters such as <strong>Tortuosity, Curvature, Torsion, Length, Radius etc.</strong> for the centerlines. The current vmtk version groups these centerlines based on Centerline Ids, Group Ids etc.</p>
<p>But it still calculates all the metrics for the centerlines based on <strong>CenterlineIds</strong> and not based on <strong>GroupIds</strong> as it should have for parent and daughter branches in the vasculature.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b2e7beec99eb94d7f899633a0586e75da647379.jpeg" data-download-href="/uploads/short-url/1AUQk3hpybAWDCa76uWFDPnCO6t.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b2e7beec99eb94d7f899633a0586e75da647379_2_690x342.jpeg" alt="image" data-base62-sha1="1AUQk3hpybAWDCa76uWFDPnCO6t" width="690" height="342" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b2e7beec99eb94d7f899633a0586e75da647379_2_690x342.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b2e7beec99eb94d7f899633a0586e75da647379_2_1035x513.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b2e7beec99eb94d7f899633a0586e75da647379.jpeg 2x" data-dominant-color="F6F5F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1121×556 75.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Should I use the Blanking arrays to separate the values along the centerline curves? In that case I would lose out on the centerline metrics for the blanked regions of the arteries.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/860a0d1e883f3095d1d0f7b1eb7962cc7df141d0.jpeg" data-download-href="/uploads/short-url/j7LvYuLDNmDQU5Zlmy9lPI6DFhC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/860a0d1e883f3095d1d0f7b1eb7962cc7df141d0_2_690x411.jpeg" alt="image" data-base62-sha1="j7LvYuLDNmDQU5Zlmy9lPI6DFhC" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/860a0d1e883f3095d1d0f7b1eb7962cc7df141d0_2_690x411.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/860a0d1e883f3095d1d0f7b1eb7962cc7df141d0.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/860a0d1e883f3095d1d0f7b1eb7962cc7df141d0.jpeg 2x" data-dominant-color="ECECEB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">990×591 69.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The other option is to use the Centerline tree which contains the merged network of centerlines near the bifurcations. However this is just an approximation and is not the true representation of the centerlines.</p>
<p>Could you <a class="mention" href="/u/lassoan">@lassoan</a> suggest a better way to isolate centerline data without using the merged version?</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2021-08-12 18:38 UTC)

<p>I’m not that familiar with the VMTK metric computation classes. It may be easy to change them or add some more options about how to group centerlines. You can send a pull request if you have any specific suggestion.</p>
<p>While using VMTK filters for computing metrics can be convenient, it may be similarly easy to get all point and cell attributes as numpy arrays, filter them using numpy indexing and compute statistics on them using standard numpy functions.</p>
<aside class="quote no-group" data-username="som1197" data-post="1" data-topic="19173">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/som1197/48/14945_2.png" class="avatar"> som1197:</div>
<blockquote>
<p>The other option is to use the Centerline tree which contains the merged network of centerlines near the bifurcations. However this is just an approximation and is not the true representation of the centerlines.</p>
</blockquote>
</aside>
<p>Do you mean that vtkvmtkPolyDataNetworkExtraction result is more accurate than vtkvmtkPolyDataCenterlines? I find the centerline extraction result much more anatomically accurate than the network extraction result. For example, in network extraction result, small side branches perturb the centerline of the main branch, which does not happen in reality.</p>

---

## Post #3 by @som1197 (2021-08-12 19:13 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>vtkvmtkPolyDataCenterlines is definitely more robust (3D Slicer implementation) than the current vmtk implementation of the centerlines and also represents the true centerline data as compared to the data obtained from the vtkvmtkPolyDataNetworkExtraction class.</p>
<p>I have used centerlines generated using the vtkvmtkPolyDataCenterlines class in 3D slicer in my code for post processing. But I wanted to categorize different centerline metrics according to different arteries. This is only possible using the vtkvmtkPolyDataNetworkExtraction class since it removes the blanked portions of the centerlines and is easier to use as a 1D graph. But in doing so we lost the information near the bifurcations. Hence I wanted to know if there would be any alternative way of separating information related to the centerline metrics using vtkvmtkPolyDataCenterlines rather than vtkvmtkPolyDataNetworkExtraction?</p>
<p>I have a few ideas in mind for this. I will send out some pull requests along with some previous other requests related to obtaining more metrics from the centerline data that I had raised earlier.</p>
<p>Thanks…</p>

---

## Post #4 by @som1197 (2021-08-12 19:15 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/061bb3383363c0b50c1bbbc975a406aac64802d4.jpeg" alt="image" data-base62-sha1="S2d8MAHYpu05ITI6Ubsv4vUa0Y" width="601" height="493"><br>
Here is what I meant to say previously</p>

---

## Post #5 by @lassoan (2021-08-12 19:55 UTC)

<p>I’m not sure if that is exactly what you are after or not, but “Centerline properties” table that Extract centerline module creates contains radius, length, curvature, torsion, tortuosity values for each branch.</p>
<p>I would also add that in recent Slicer Preview Releases, curves can store any number of point data associated with control points of the curve. Currently, we only store radius value there, but we could add all other metrics as well. You can get these measurements as numpy arrays and compute statistics like this (get average and 15th percentil of the radius of branch <code>Centerline curve (0)</code>):</p>
<pre><code class="lang-python">&gt;&gt;&gt; r = arrayFromMarkupsControlPointData(getNode('Centerline curve (0)'), 'Radius')
&gt;&gt;&gt; r.mean()
9.720431177360679
&gt;&gt;&gt; np.percentile(r, 15)
6.983462575318652
</code></pre>

---

## Post #6 by @som1197 (2021-08-12 20:18 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a> ,</p>
<p>Yes, I am aware of this table which provides detailed quantification of different metrics. However it is based on the input obtained from the merged centerlines which does this to the original centerlines extracted using vtkvmtkPolyDataCenterlines.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46c338bf86163e737722bc22faad25400041f83f.png" alt="image" data-base62-sha1="a5ZGn7Q2A8DkjoxJszZnHp2l2Q7" width="206" height="203"></p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/blob/ba692afa8f20aacbfa424f1d4bbfa9fe90bc4349/ExtractCenterline/ExtractCenterline.py#L826-L917">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/ba692afa8f20aacbfa424f1d4bbfa9fe90bc4349/ExtractCenterline/ExtractCenterline.py#L826-L917" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/ba692afa8f20aacbfa424f1d4bbfa9fe90bc4349/ExtractCenterline/ExtractCenterline.py#L826-L917" target="_blank" rel="noopener nofollow ugc">vmtk/SlicerExtension-VMTK/blob/ba692afa8f20aacbfa424f1d4bbfa9fe90bc4349/ExtractCenterline/ExtractCenterline.py#L826-L917</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="826" style="counter-reset: li-counter 825 ;">
          <li>def createCurveTreeFromCenterline(self, centerlinePolyData, centerlineCurveNode=None, centerlinePropertiesTableNode=None, curveSamplingDistance=1.0):
</li>
          <li>
</li>
          <li>    import vtkvmtkComputationalGeometryPython as vtkvmtkComputationalGeometry
</li>
          <li>
</li>
          <li>    branchExtractor = vtkvmtkComputationalGeometry.vtkvmtkCenterlineBranchExtractor()
</li>
          <li>    branchExtractor.SetInputData(centerlinePolyData)
</li>
          <li>    branchExtractor.SetBlankingArrayName(self.blankingArrayName)
</li>
          <li>    branchExtractor.SetRadiusArrayName(self.radiusArrayName)
</li>
          <li>    branchExtractor.SetGroupIdsArrayName(self.groupIdsArrayName)
</li>
          <li>    branchExtractor.SetCenterlineIdsArrayName(self.centerlineIdsArrayName)
</li>
          <li>    branchExtractor.SetTractIdsArrayName(self.tractIdsArrayName)
</li>
          <li>    branchExtractor.Update()
</li>
          <li>    centerlines = branchExtractor.GetOutput()
</li>
          <li>
</li>
          <li>    mergeCenterlines = vtkvmtkComputationalGeometry.vtkvmtkMergeCenterlines()
</li>
          <li>    mergeCenterlines.SetInputData(centerlines)
</li>
          <li>    mergeCenterlines.SetRadiusArrayName(self.radiusArrayName)
</li>
          <li>    mergeCenterlines.SetGroupIdsArrayName(self.groupIdsArrayName)
</li>
          <li>    mergeCenterlines.SetCenterlineIdsArrayName(self.centerlineIdsArrayName)
</li>
          <li>    mergeCenterlines.SetTractIdsArrayName(self.tractIdsArrayName)
</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/ba692afa8f20aacbfa424f1d4bbfa9fe90bc4349/ExtractCenterline/ExtractCenterline.py#L826-L917" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I want to obtain these same metrics based on this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b000c668e7543051540c16435340b75b7a6e694.png" alt="image" data-base62-sha1="fgzbYlUrmfxcfmbQjVoOajHyoD2" width="207" height="202"></p>
<p>Thank you.</p>

---

## Post #7 by @som1197 (2021-08-12 21:55 UTC)

<p>To add to what I was previously addressing, on comparing different metrics for centerlines generated using the <strong>vtkvmtkCenterlineBranchGeometry()</strong> with 2 inputs one being the merged centerlines <strong>vtkvmtkMergeCenterlines()</strong> and the other being centerlines extracted using the <strong>vtkvmtkCenterlineBranchExtractor()</strong> class, we can see the sharp variations in <strong>Curvature</strong> since its computation involves first, second and third order derivatives.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecd9f2f7d821b0014f2e0e6a1a29cd8a41429afb.jpeg" data-download-href="/uploads/short-url/xNhDtSVvTKhU3qEZzF4Ek0IH5qP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ecd9f2f7d821b0014f2e0e6a1a29cd8a41429afb_2_690x325.jpeg" alt="image" data-base62-sha1="xNhDtSVvTKhU3qEZzF4Ek0IH5qP" width="690" height="325" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ecd9f2f7d821b0014f2e0e6a1a29cd8a41429afb_2_690x325.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ecd9f2f7d821b0014f2e0e6a1a29cd8a41429afb_2_1035x487.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecd9f2f7d821b0014f2e0e6a1a29cd8a41429afb.jpeg 2x" data-dominant-color="F7F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1243×587 95.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Hence the choice of using a merged centerlines as an input as used in 3D slicer versus using the branched centerlines as an input does play an important role in obtaining correct metrics.</p>
<p>Thanks.</p>

---

## Post #8 by @lassoan (2021-08-13 04:04 UTC)

<p>I haven’t noticed the difference between the bifurcations shape introduced by vtkvmtkMergeCenterlines but I see it now:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32a812175a7d1f246bf9fb1e99c9879a461b412a.png" alt="image" data-base62-sha1="7e7XIO9jttLUQqifhjQOsCzRRay" width="369" height="489"></p>
<p>Slicer can search for a path in the non-merged centerline tree, which could be used instead of vtkvmtkMergeCenterlines:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="WJQexDTiRRc" data-video-title="Transform markups between original and straightened vessel" data-video-start-time="28" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=WJQexDTiRRc&amp;t=28" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/WJQexDTiRRc/maxresdefault.jpg" title="Transform markups between original and straightened vessel" width="" height="">
  </a>
</div>

<p>Currently, we just get the point coordinates and not copy point data from the centerline model into curve node, but it would not be hard to implement this.</p>
<p>If you are interested in computing the curvature, it is one of the built-in measurements of curve nodes. I’ve tested this curvature measurement on the non-merged centerline curve and got very noisy results:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/123a53f2c7a19dcdd8a11c27f1bedfe53ded6f1c.jpeg" data-download-href="/uploads/short-url/2BfyOhomyNyoOOWEsU2P20EjQXq.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/123a53f2c7a19dcdd8a11c27f1bedfe53ded6f1c_2_465x499.jpeg" alt="image" data-base62-sha1="2BfyOhomyNyoOOWEsU2P20EjQXq" width="465" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/123a53f2c7a19dcdd8a11c27f1bedfe53ded6f1c_2_465x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/123a53f2c7a19dcdd8a11c27f1bedfe53ded6f1c_2_697x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/123a53f2c7a19dcdd8a11c27f1bedfe53ded6f1c.jpeg 2x" data-dominant-color="8D91C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">851×914 65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Most probably it is due to noisy centerline (points are not along a smooth curve, probably distance between points varies, too). If I fit a spline to the curve (by resampling the curve using 50 control points and then setting curve type to spline) then curvature measurement becomes correct:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a8c4d458c09ecd84c3dac92b539aff2b63b4590.jpeg" data-download-href="/uploads/short-url/64oEf1ycofTMioJVBd8lNeFkNVe.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2a8c4d458c09ecd84c3dac92b539aff2b63b4590_2_444x500.jpeg" alt="image" data-base62-sha1="64oEf1ycofTMioJVBd8lNeFkNVe" width="444" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2a8c4d458c09ecd84c3dac92b539aff2b63b4590_2_444x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2a8c4d458c09ecd84c3dac92b539aff2b63b4590_2_666x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a8c4d458c09ecd84c3dac92b539aff2b63b4590.jpeg 2x" data-dominant-color="8C92C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">839×943 62.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Most likely in the noisy measurements you have the same issue, i.e., the centerline is not smoothed and resampled at equal distances.</p>
<p>About other metrics:</p>
<ul>
<li>Radius values should have no issues, as they are not changing quickly and not sensitive to any resampling or smoothing.</li>
<li>Length computation is trivial.</li>
<li>Tortuosity is not a metric that makes sense for a few long line segments like you have in your images. I think it is a very poor metric overall, which I only see making any sense if computed for hundreds of short line segments in a dense tree with lots of branching.</li>
</ul>

---

## Post #9 by @som1197 (2021-08-13 18:44 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thanks for clarifying the curvature results! Could you tell me how you developed a tube representation of the centerline model to post process the curvature metric? Currently only radius is the scalar that is available to post process, following on my previous issue.</p><aside class="quote quote-modified" data-post="3" data-topic="18604">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/som1197/48/14945_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-convert-centerlines-to-a-graph-v-e/18604/3">Slicer - Convert centerlines to a graph {V,E}</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thank you <a class="mention" href="/u/lassoan">@lassoan</a>  for the piece of code. Yes I will send out a pull request with the proposed changes soon. 
Moreover, I also wanted to know if scalar values of ‘GroupIDsarray’, ‘TortuosityArray’ , ‘BlankingArray’ etc. can be incorporated in the centerline model. I generated the following plots by using the conventional vmtkscripts, but it does not always work correctly. 
[image] 
[image] 
Currently there are only 3 ways to postprocess the centerline data as shown here. 
[image] 


However, ca…
  </blockquote>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/997fdaddd0335ac5022fc10a2fc3bfc24d222beb.png" data-download-href="/uploads/short-url/lTUYOJm4RuhoDGkhKzLXPquXcE3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/997fdaddd0335ac5022fc10a2fc3bfc24d222beb_2_403x500.png" alt="image" data-base62-sha1="lTUYOJm4RuhoDGkhKzLXPquXcE3" width="403" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/997fdaddd0335ac5022fc10a2fc3bfc24d222beb_2_403x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/997fdaddd0335ac5022fc10a2fc3bfc24d222beb_2_604x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/997fdaddd0335ac5022fc10a2fc3bfc24d222beb.png 2x" data-dominant-color="F5F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">626×775 25.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I used the earlier method you mentioned in the video to coincide the merged centerlines (curves/splines) on the vtkpolydata surface representation of the centerline model but got this.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8e4b239a8e996cae6cf4a091ca9d051966b2859.jpeg" data-download-href="/uploads/short-url/sFbtlPJVeiuMQ40NPFZV1cTcSSt.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8e4b239a8e996cae6cf4a091ca9d051966b2859_2_690x237.jpeg" alt="image" data-base62-sha1="sFbtlPJVeiuMQ40NPFZV1cTcSSt" width="690" height="237" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8e4b239a8e996cae6cf4a091ca9d051966b2859_2_690x237.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8e4b239a8e996cae6cf4a091ca9d051966b2859.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8e4b239a8e996cae6cf4a091ca9d051966b2859.jpeg 2x" data-dominant-color="BAC9BA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">927×319 45 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there a way to obtain the curve/spline representation for the centerline model or the vtkpolydata?<br>
Basically I want a bifurcation point in the centerline model so that I can separate the vessels for the hemodynamic analysis later on.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94d93aabd6cc9a0ba321d733b2f8573b18df4d08.jpeg" alt="image" data-base62-sha1="leM4M18QPcmScMjEEUMAcfFVvQc" width="582" height="361"><br>
Thanks.</p>

---

## Post #10 by @Mudrika (2023-05-02 16:01 UTC)

<p>Hey!</p>
<p>Can you please elaborate on how you obtained the parameters for the whole vasculature? I am not able to figure this out!</p>

---

## Post #11 by @smoudour (2023-10-27 12:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="19173">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Tortuosity is not a metric that makes sense for a few long line segments like you have in your images. I think it is a very poor metric overall, which I only see making any sense if computed for hundreds of short line segments in a dense tree with lots of branching.</p>
</blockquote>
</aside>
<p>Could you elaborate a bit more one this? I aim to have a few hundred of coronary artery trees. Would it make sense to study tortuosity of each tree? Or tortuosity of each part of the coronary tree of each 3d model?</p>

---
