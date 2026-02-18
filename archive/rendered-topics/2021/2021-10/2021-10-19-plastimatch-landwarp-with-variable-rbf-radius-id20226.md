# Plastimatch landwarp with variable rbf radius

**Topic ID**: 20226
**Date**: 2021-10-19
**URL**: https://discourse.slicer.org/t/plastimatch-landwarp-with-variable-rbf-radius/20226

---

## Post #1 by @simonoxen (2021-10-19 10:24 UTC)

<p>Hi, I’ve been developing a module for manual refinement of normalization (WarpDrive - <a href="https://github.com/netstim/SlicerNetstim/tree/master/WarpDrive" rel="noopener nofollow ugc">github</a>, <a href="https://www.youtube.com/watch?v=VcBXu5BURVI" rel="noopener nofollow ugc">video</a>).</p>
<p>This module runs plastimatch landwarp based on source and target fiducials set by the user via different tools accessed in the module.</p>
<p>The module allows the user to set a radius specific for each point, but the current implementation of plastimatch takes one fixed radius. I recently added the possibility to set the radius as a vector (<a href="https://github.com/simonoxen/SlicerRT/commit/c1e9e4613b390d6708b4a82788dbf33344fb8962" rel="noopener nofollow ugc">commit</a>), and a modification in platimatch to allow this input (<a href="https://github.com/simonoxen/plastimatch/commit/a1c1e6fa700f8a2b2421bb146075b67ab43457dc" rel="noopener nofollow ugc">commit</a>).</p>
<p>Would there be interest in adding these changes (or something of the sort)?</p>
<p>Also (perhaps should post this on a separate topic), would it make sense to have a <em>SlicerPlastimatch</em> extension instead of having it inside <em>SlicerRt</em>? Then the dependency of this module would be more straightforward (as well as people in general that would be interested in it).</p>
<p>I’ve also seen some activity by platimatch developers here. I would be very interested to hear their thoughts on the module <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @pieper (2021-10-19 12:36 UTC)

<p>Really nice!  <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"></p>
<p>Yes, I think a SlicerPlastimatch makes a lot of sense.  Maybe <a class="mention" href="/u/gregsharp.geo">@gregsharp.geo</a> can chime in?</p>
<p>There’s some similarity to the <a href="https://github.com/Slicer/LandmarkRegistration">LandmarkRegistration</a> (although I haven’t worked on that for a while) and also the FiducialRegistration in SlicerIGT.  Maybe we should try to harmonize or unify these approaches somehow.</p>

---

## Post #3 by @lassoan (2021-10-20 04:45 UTC)

<p>It would not be trivial to expose all of Plastimatch features via a public module interface. As far as I remember Plastimatch is not even built as a dynamically loadable module in Slicer due to some issues in the build system. Therefore it would take some effort to move out Plastimatch to a separate extension.</p>
<p>Also, main focus of Plastimatch is radiation therapy and so it makes sense for it to depend on SlicerRT, and SlicerRT to depend on Plastimatch, which the easiest to achieve if they are in the same extension.</p>
<p>What would make a lot of sense is to move out independent features from Plastimatch to separate libraries to make the core library smaller and more focused. For example, the <a href="https://gitlab.com/plastimatch/plastimatch/-/tree/master/src/plastimatch/register">registration library</a> could be a nice independent, Python-wrapped, ITK remote module that could be used in Slicer extensions but could be also easily pip-installed and used in any Python environment. Similarly, DRR, CBCT reconstruction, segmentation, could be all carved out into separate ITK remote modules. Those basic features that are now widely available in ITK, SimpleITK, VTK, and other toolkits (such as image and vector field conversion and manipulation), could be probably retired. This reorganization would result in a much smaller, more cohesive, RT-oriented Plastimatch library that could be kept with SlicerRT; while general-purpose features could be made available in separate extensions.</p>
<p>These decisions of course all completely up to <a class="mention" href="/u/gcsharp">@gcsharp</a>, who developed and maintains the entire code base.</p>

---
