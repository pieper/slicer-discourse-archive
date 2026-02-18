# Generate tubes with markups to model

**Topic ID**: 33542
**Date**: 2023-12-28
**URL**: https://discourse.slicer.org/t/generate-tubes-with-markups-to-model/33542

---

## Post #1 by @SANTIAGO_PENDON_MING (2023-12-28 10:24 UTC)

<p>Hi to everyone. At this moment I’m struggling with markupstomodel  module, which implements some handsome functions as could be generate tubes from markups.</p>
<p>In my first attemp I achieve a fancy solution touching the parameters in:</p>
<p><code>markupsToModel.UpdateOutputCurveModel(guideListNode, guideModel,interpolationType, False, 0.18, 50,15,True, 1, slicer.vtkMRMLMarkupsToModelNode.RawIndices, None, polynomialFitType)</code></p>
<p>Obtaining this perfected fitted and smooth tube:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37d57cad5461ac4d5eec4753ccfca84ff9a255ec.png" data-download-href="/uploads/short-url/7XVEAGz9FnrxAlLmqsL63VBrv1q.png?dl=1" title="Captura de pantalla 2023-12-28 093520" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37d57cad5461ac4d5eec4753ccfca84ff9a255ec_2_257x500.png" alt="Captura de pantalla 2023-12-28 093520" data-base62-sha1="7XVEAGz9FnrxAlLmqsL63VBrv1q" width="257" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37d57cad5461ac4d5eec4753ccfca84ff9a255ec_2_257x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37d57cad5461ac4d5eec4753ccfca84ff9a255ec.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37d57cad5461ac4d5eec4753ccfca84ff9a255ec.png 2x" data-dominant-color="665A88"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2023-12-28 093520</span><span class="informations">355×690 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But when I try to do the same with a fiducial list much more dense as could be next pic, I obtain:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f01934344d7077a577b85a4a0548b9d112b3437a.png" data-download-href="/uploads/short-url/yg0AHTpkS5wNVctKUkR6vlkFd90.png?dl=1" title="Captura de pantalla 2023-12-28 111957" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f01934344d7077a577b85a4a0548b9d112b3437a_2_690x132.png" alt="Captura de pantalla 2023-12-28 111957" data-base62-sha1="yg0AHTpkS5wNVctKUkR6vlkFd90" width="690" height="132" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f01934344d7077a577b85a4a0548b9d112b3437a_2_690x132.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f01934344d7077a577b85a4a0548b9d112b3437a_2_1035x198.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f01934344d7077a577b85a4a0548b9d112b3437a.png 2x" data-dominant-color="353544"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2023-12-28 111957</span><span class="informations">1253×241 25.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As you can see this curve is non-well fitted with data points and also is non-smooth (I can see the small cylinders that composes the structure)</p>
<p>I guess that the problem here are the parameters in UpdateOutputCurveModel. I try to find documentation about it, but only find this <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorDrawTube/SegmentEditorDrawTubeLib/SegmentEditorEffect.py" class="inline-onebox" rel="noopener nofollow ugc">SlicerSegmentEditorExtraEffects/SegmentEditorDrawTube/SegmentEditorDrawTubeLib/SegmentEditorEffect.py at master · lassoan/SlicerSegmentEditorExtraEffects · GitHub</a>  in lines:</p>
<pre><code class="lang-auto">    markupsToModel = slicer.modules.markupstomodel.logic()
    # Create tube from points
    markupsToModel.UpdateOutputCurveModel( inputMarkup, outputModel,
      interpolationType, False, self.radius, 8, NumberOfLineSegmentsBetweenControlPoints, True, 3,
      slicer.vtkMRMLMarkupsToModelNode.RawIndices, self.curveGenerator,
      polynomialFitType )

</code></pre>
<p>Can somebody explain the parameters and what make each of them.</p>
<p>Thanks a lot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @chir.set (2023-12-28 10:45 UTC)

<p>If you want a regular tube, you can use the ‘Draw tube’ effect of the SegmentEditorExtraEffects extension.</p>
<p>If you want a tube with varying radius, you can use the ‘Shape’ custom markups of the ExtraMarkups extension.</p>
<p>You can install both using the ‘Extensions manager’. You would get more controllable tubes.</p>

---

## Post #3 by @SANTIAGO_PENDON_MING (2023-12-28 10:51 UTC)

<p>Hi chir.set, thanks.</p>
<p>Can you provide me an example of how to use the method to do regular tubes with segment editor? I’m doing it coding, not manually. Also, you know how works the function I mention in the original question?</p>
<p>Thanks for your help!</p>

---

## Post #4 by @chir.set (2023-12-28 18:07 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="3" data-topic="33542">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>the method to do regular tubes with segment editor</p>
</blockquote>
</aside>
<p>This can be done using the <a href="https://vtk.org/doc/nightly/html/classvtkTubeFilter.html" rel="noopener nofollow ugc">vtkTubeFilter</a> class. The VTK project has many many<br>
<a href="https://examples.vtk.org/site/Python/PolyData/TubeFilter/" rel="noopener nofollow ugc">example</a> pages.</p>

---
