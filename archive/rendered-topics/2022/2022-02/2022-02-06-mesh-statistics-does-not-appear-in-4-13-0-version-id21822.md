# Mesh Statistics does not appear in 4.13.0 version?

**Topic ID**: 21822
**Date**: 2022-02-06
**URL**: https://discourse.slicer.org/t/mesh-statistics-does-not-appear-in-4-13-0-version/21822

---

## Post #1 by @Moh_d_Al-Watary (2022-02-06 16:24 UTC)

<p>Dear 3D Slicer experts, I used to use 4.11.2 version and there is Mesh Statistics function in quantifications module , when used 4.13.0 version this function does not appear? how could this be solved?<br>
thank you in advance.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebc8dea847e0db5acb2d94d04229581b89329873.png" data-download-href="/uploads/short-url/xDQz9D4fFOeHW6bDjE3HR9t3e7N.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebc8dea847e0db5acb2d94d04229581b89329873_2_690x387.png" alt="image" data-base62-sha1="xDQz9D4fFOeHW6bDjE3HR9t3e7N" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebc8dea847e0db5acb2d94d04229581b89329873_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebc8dea847e0db5acb2d94d04229581b89329873_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebc8dea847e0db5acb2d94d04229581b89329873.png 2x" data-dominant-color="8B8C92"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-02-06 17:04 UTC)

<p>MeshStatistics extension packaing failed due to the very recent upgrade of Slicer’s Python version to 3.9. I’ve <a href="https://github.com/DCBIA-OrthoLab/MeshStatisticsExtension/pull/17">submitted a fix</a>, hopefully it’ll get integrated within a few days. In the meantime, you can download the fixed module .py file from <a href="https://github.com/lassoan/MeshStatisticsExtension/tree/master/MeshStatistics">here</a>.</p>
<p>I’ve also noticed that MeshStatistics module is included in two extensions:</p>
<ul>
<li>
<a href="https://github.com/DCBIA-OrthoLab/MeshStatisticsExtension:">https://github.com/DCBIA-OrthoLab/MeshStatisticsExtension:</a> this was updated to Python3 and just has a small issue with Python-3.9 (this is the version I’ve fixed up)</li>
<li>
<a href="https://github.com/jbvimort/ShapeQuantifierExtension:">https://github.com/jbvimort/ShapeQuantifierExtension:</a> this is an old, Python2 version of the module</li>
</ul>
<p>Since MeshStatistics extension is a tiny Python-scripted module, it is probably not worth maintaining it in a separate extension, so it would make sense to move the updated module into ShapeQuantifier extension and remove the MeshStatistics extension. <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> could you take care of this?</p>

---

## Post #3 by @allemangd (2022-02-07 18:10 UTC)

<blockquote>
<p>Since MeshStatistics extension is a tiny Python-scripted module, it is probably not worth maintaining it in a separate extension, so it would make sense to move the updated module into ShapeQuantifier extension and remove the MeshStatistics extension.</p>
</blockquote>
<p>Before I joined the project there was an effort to make these more modular, where each SlicerCMF component could be installed individually; the role that ShapeQuantifierExtension filled has since been replaced by the <a href="https://github.com/dcbia-ortholab/slicercmf" rel="noopener nofollow ugc">SlicerCMF</a> “extension bundle.”</p>
<p>We are preparing some refactoring of these extensions as they are not all stable in Slicer 4.13 as-is. I will bring this topic up for discussion at the next DCBIA meeting (this Thursday 02/10) to potentially be a part of this refactoring effort.</p>

---

## Post #4 by @lassoan (2022-02-07 18:36 UTC)

<p>It is hard to decide how to distribute modules across extensions, as there are several requirements that may be slightly contradicting (make it easy to discover and use for users; make it easy to develop, test, document, and maintain for developers, etc). Both extremes (putting all modules in a single extension; putting each module in a separate extension) are suboptimal.</p>
<p>A good approach can be to start with building a large extension with many modules and then factoring out groups of modules. For example:<br>
-You could move out a group of modules that are usually used together - such as “Mesh statistics” and “Model to model distance” modules could be moved together into one extension (something like “CompareModels”).</p>
<ul>
<li>You could decide to move mature infrastructural modules to Slicer core or SurfaceToolbox (freeing up your resources from maintaining these modules) - such as “Easy Clip”, “Pick and Paint”, “Angle Planes” could be moved to SurfaceToolbox, because their core features are now available via Dynamic Modeler module and you would just need to add a thin layer of convenient GUI.</li>
</ul>

---
