---
topic_id: 29868
title: "Slicer 3D Line Widget"
date: 2023-06-06
url: https://discourse.slicer.org/t/29868
---

# Slicer 3d Line Widget

**Topic ID**: 29868
**Date**: 2023-06-06
**URL**: https://discourse.slicer.org/t/slicer-3d-line-widget/29868

---

## Post #1 by @mazurkin (2023-06-06 15:39 UTC)

<p>Hello, I built the 3D Slicer tool using Webassembly and received the following error. What could be the cause of it? It works fine on Desktop.</p>
<p>Cone.js:1 vtkShaderProgram (0x2a9f90): ERROR: 0:130: ‘/’ : wrong operand types - no operation ‘/’ exists that takes a left-hand operand of type ‘highp float’ and a right operand of type ‘const int’ (or there is no acceptable conversion)<br>
Cone.js:1 ERROR: In vtkOpenGLPolyDataMapper.cxx, line 2590<br>
vtkOpenGLGlyph3DHelper (0x2a3c78): Could not set shader program.</p>

---

## Post #2 by @pieper (2023-06-06 19:10 UTC)

<p>Did you really build <a href="https://github.com/Slicer/Slicer">3D Slicer</a> for webassembly?  That would be quite a feat and we’d love to hear more about it.</p>
<p>Or maybe you mean some other code?  The error you posted looks like it comes from a vtk.js example and if so you could post on the <a href="https://discourse.vtk.org/c/web/9">vtk web forum</a>.</p>

---

## Post #3 by @mazurkin (2023-06-07 02:09 UTC)

<p>Hello, I’ve created a build for just one 3D Slicer widget in web-assembly. You can check out both the build code and the code itself at the following link: <a href="https://github.com/danielmazurkin/example-web-assembly/tree/master" class="inline-onebox" rel="noopener nofollow ugc">GitHub - danielmazurkin/example-web-assembly: This is repository for research building 3D Slicer to web assembler</a>. However, I’m getting a black screen after launching the widget in the browser, but when building in Desktop C++, the ruler widget from 3D Slicer is displayed for me.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9571f958d52651c8ccd5646a657775e7beb02dc.jpeg" data-download-href="/uploads/short-url/v0GgRNioBv60hDwiZ93N9GjcqWo.jpeg?dl=1" title="c_example_webassembly" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9571f958d52651c8ccd5646a657775e7beb02dc_2_690x328.jpeg" alt="c_example_webassembly" data-base62-sha1="v0GgRNioBv60hDwiZ93N9GjcqWo" width="690" height="328" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9571f958d52651c8ccd5646a657775e7beb02dc_2_690x328.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9571f958d52651c8ccd5646a657775e7beb02dc_2_1035x492.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9571f958d52651c8ccd5646a657775e7beb02dc.jpeg 2x" data-dominant-color="82827A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">c_example_webassembly</span><span class="informations">1280×609 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1058a4511059119447a84ceb09335b0e703cc87.jpeg" data-download-href="/uploads/short-url/tP5EYLhFZ8AG0qWD4uXl7HNLyar.jpeg?dl=1" title="c_example_linear" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1058a4511059119447a84ceb09335b0e703cc87_2_637x499.jpeg" alt="c_example_linear" data-base62-sha1="tP5EYLhFZ8AG0qWD4uXl7HNLyar" width="637" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1058a4511059119447a84ceb09335b0e703cc87_2_637x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1058a4511059119447a84ceb09335b0e703cc87.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1058a4511059119447a84ceb09335b0e703cc87.jpeg 2x" data-dominant-color="121212"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">c_example_linear</span><span class="informations">843×661 12.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95617cc11d2cfcc41420e99b1157c54d51a60759.png" data-download-href="/uploads/short-url/lju0xwiHluSXXFAjfBLjffnrlkR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95617cc11d2cfcc41420e99b1157c54d51a60759_2_690x248.png" alt="image" data-base62-sha1="lju0xwiHluSXXFAjfBLjffnrlkR" width="690" height="248" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95617cc11d2cfcc41420e99b1157c54d51a60759_2_690x248.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95617cc11d2cfcc41420e99b1157c54d51a60759_2_1035x372.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95617cc11d2cfcc41420e99b1157c54d51a60759_2_1380x496.png 2x" data-dominant-color="989ACA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1414×509 16.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @pieper (2023-06-07 14:17 UTC)

<p>That’s a very interesting project, and I can see a lot of value in being able to share code across browser and desktop.  It’s all very new though, so it may be hard to get help.  I know you are starting with a fairly simple example, but perhaps starting with an even simpler test could help.  Also it could help if you could provide very explicit instructions on your project readme about how people can set up a developer environment to replicate what you have done.</p>

---
