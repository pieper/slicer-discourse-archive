# ConvertToGridTransform returns vtkMRMLTransformNode instead of vtkMRMLGridTransformNode

**Topic ID**: 18467
**Date**: 2021-07-01
**URL**: https://discourse.slicer.org/t/converttogridtransform-returns-vtkmrmltransformnode-instead-of-vtkmrmlgridtransformnode/18467

---

## Post #1 by @simonoxen (2021-07-01 18:08 UTC)

<p>Is there a reason why the ConvertToGridTransform method outputs a vtkMRMLTransformNode instead of a vtkMRMLGridTransformNode?</p>
<p><a href="https://github.com/Slicer/Slicer/blob/aaa9f918a4ee4f35bf09e05c5d7e53d083b2e4e3/Modules/Loadable/Transforms/Logic/vtkSlicerTransformLogic.h#L112" rel="noopener nofollow ugc">Slicer/Modules/Loadable/Transforms/Logic/vtkSlicerTransformLogic.h</a></p>
<p>I’m developing a <a href="https://github.com/netstim/SlicerNetstim/tree/master/WarpDrive" rel="noopener nofollow ugc">module</a> that takes grid transforms as input. When implementing I tried to strictly take vtkMRMLGridTransformNode as input and this way might be more straightforward for the user.</p>
<p>I usually load non linear transforms that are loaded as grid transforms so there’s no problem. But I realised that if I wanted to this from within Slicer, vtkMRMLTransformNode are generated (and therefore not recognised as possible input).</p>
<p>Of course, this is easy to change on my side, but I wonder if there’s a reason for this. If not, I can also try to contribute a change.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2021-07-02 04:43 UTC)

<p>This is a very good question.</p>
<p>There is a bit of history behind this: When MRML library was initially designed, different classes were added for linear, b-spline, and grid transforms. However, about 5-10 years ago when we implemented support for composite transforms (that can store an arbitrary set of concatenated transforms, each of them potentially inverted) then we realized that we cannot dynamically split and merge transforms if a transform object is statically assigned to a specific transform class. Therefore, we made the <code>vtkTransformNode</code> class to be a universal transform container, which can store linear, b-spline, grid, thin-plate-spline, and composite transforms. However, we did not remove the old classes because the class names were used for filtering in MRML node selectors in the user interfaces in many modules.</p>
<p>In the future, we’ll remove these classes and use node attributes to filter for transform types in node selectors - see this ticket:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5718">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5718" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5718" target="_blank" rel="noopener">Retire linear, bspline, grid transform node subclasses</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-07-02" data-time="04:40:32" data-timezone="UTC">04:40AM - 02 Jul 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When MRML library was initially designed, different classes were added for linea<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">r, b-spline, grid, and thin-plate-spline transforms. However, when we implemented support for composite transforms (that can store an arbitrary set of concatenated transforms each of them potentially inverted) we realized that we cannot dynamically split and merge transforms if a transform object is statically assigned to a specific transform class. Therefore, we made the `vtkTransformNode` class to be a universal transform container, which can store linear, b-spline, grid, thin-plate-spline, and composite transforms. However, we did not remove the old classes because the class names were used for filtering in MRML node selectors. This causes confusion for developers (see for example [here](https://discourse.slicer.org/t/converttogridtransform-returns-vtkmrmltransformnode-instead-of-vtkmrmlgridtransformnode/18467/2)).

We should remove the vtkMRMLLinearTransformNode, vtkMRMLBSplineTransformNode, and vtkMRMLGridTransformNode classes and set transform type into a custom attribute (Transforms.type = linear, bspline, grid, tps, composite; maybe also Transforms.linear = 0/1; and potentially Transforms.toWorldType, Transforms.toWorldLinear), which node selectors could use as filter criteria.

A slight difficulty is that determining transform type (especially transform type all the way up to the world coordinate system) may be expensive if the transform is changing frequently.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Until this is implemented, I would recommend to use vtkMRMLTransformNode class everywhere, and only use child classes if it is absolutely necessary.</p>

---

## Post #3 by @simonoxen (2021-07-02 06:19 UTC)

<p>Thanks for the clarification! Will adopt this then</p>

---
