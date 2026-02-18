# How to display the cropVolume fitted with the slice views?

**Topic ID**: 17698
**Date**: 2021-05-19
**URL**: https://discourse.slicer.org/t/how-to-display-the-cropvolume-fitted-with-the-slice-views/17698

---

## Post #1 by @jumbojing (2021-05-19 21:44 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7f875a8afb19d6830e813a893f8db5f93f4120f.jpeg" data-download-href="/uploads/short-url/x66Cjijic6FDRrpjEICrCPfGfeL.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7f875a8afb19d6830e813a893f8db5f93f4120f_2_690x227.jpeg" alt="image" data-base62-sha1="x66Cjijic6FDRrpjEICrCPfGfeL" width="690" height="227" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7f875a8afb19d6830e813a893f8db5f93f4120f_2_690x227.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7f875a8afb19d6830e813a893f8db5f93f4120f_2_1035x340.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7f875a8afb19d6830e813a893f8db5f93f4120f_2_1380x454.jpeg 2x" data-dominant-color="100F0F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1892×624 59.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>这个被截取后的volume,怎么能最大化在切片视图里显示呢?</p>
<blockquote>
<p>The volume  extracted from CropVolume module, how to display it fitted with the  slices( Maximize the volume to full <em>slices view</em>)? I want to python code.Like follow:</p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab2156c71dbbaf2b85676a5e077c25371f2ed010.jpeg" data-download-href="/uploads/short-url/opT4HEEfQoF4NU8pt8MuYfZLsWs.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab2156c71dbbaf2b85676a5e077c25371f2ed010_2_690x240.jpeg" alt="image" data-base62-sha1="opT4HEEfQoF4NU8pt8MuYfZLsWs" width="690" height="240" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab2156c71dbbaf2b85676a5e077c25371f2ed010_2_690x240.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab2156c71dbbaf2b85676a5e077c25371f2ed010_2_1035x360.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab2156c71dbbaf2b85676a5e077c25371f2ed010_2_1380x480.jpeg 2x" data-dominant-color="41403E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1902×664 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-05-20 01:32 UTC)

<p>In recent Slicer Preview Releases (that soon will become the current stable release), volumes are fit to views by default when you show them, but you can fit them manually anytime using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.setSliceViewerLayers"><code>setSliceViewerLayers</code></a> function as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-volume-from-vti-file">here</a>.</p>

---
