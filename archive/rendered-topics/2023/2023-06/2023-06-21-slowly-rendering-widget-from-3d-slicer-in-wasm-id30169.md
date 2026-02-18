# Slowly rendering widget from 3D Slicer in wasm

**Topic ID**: 30169
**Date**: 2023-06-21
**URL**: https://discourse.slicer.org/t/slowly-rendering-widget-from-3d-slicer-in-wasm/30169

---

## Post #1 by @mazurkin.daniel (2023-06-21 03:05 UTC)

<p>Hello, I have built a widget display from 3D Slicer in WebAssembly (you can check out the instructions at this link <a href="https://docs.google.com/document/d/1dXtK01DpxkANEJEbvwo1Dnph-B_XpNmor3kCTDFklp0/edit" rel="noopener nofollow ugc">Instruction by 3dSlicer - Google Docs</a>), but when rendering, it all happens quite slowly. Can you please suggest what could be the reason? Just to provide a direction for investigations, because for example, <a href="https://kitware.github.io/vtk-js/examples/TubeFilter.html" rel="noopener nofollow ugc">vtk.js</a> works correctly on vtk.js. 3D Slicer uses vtkTubeFilter under the hood.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10b2b14a56fdb798f886dfd23d90bb5c6f345a63.png" data-download-href="/uploads/short-url/2nIuadEAcarMRtDaavs9C95hAll.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10b2b14a56fdb798f886dfd23d90bb5c6f345a63_2_690x334.png" alt="image" data-base62-sha1="2nIuadEAcarMRtDaavs9C95hAll" width="690" height="334" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10b2b14a56fdb798f886dfd23d90bb5c6f345a63_2_690x334.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10b2b14a56fdb798f886dfd23d90bb5c6f345a63.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10b2b14a56fdb798f886dfd23d90bb5c6f345a63.png 2x" data-dominant-color="4D4D4E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">793×384 51.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2023-06-22 14:34 UTC)

<p>You should be able to use the developer tools in the browser to pause the code periodically and look at the stack.  This should give you an idea where the time is being taken.  If the stack isn’t readable for the wasm code you could instead instrument the C++ code with some kinds of counters to track how often different methods are being called in response to events.</p>
<p>Thank you for sharing the code and your document.  As you go forward with this project it would be helpful if you created a git repository to track the changes you make and so that others can more easily reproduce your configuration and help debug and/or contribute improvements.</p>

---
