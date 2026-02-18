# Bspline transform multiresolution type mismatch

**Topic ID**: 14185
**Date**: 2020-10-21
**URL**: https://discourse.slicer.org/t/bspline-transform-multiresolution-type-mismatch/14185

---

## Post #1 by @MachadoL (2020-10-21 13:50 UTC)

<p>Hello, everyone.</p>
<p>I am carrying a multistage and multi-resolution deformable registration pipeline.</p>
<p>I start with 3D rigid transform. The transform result I plug into the <code>CompositTransform</code> object.<br>
In the next stage I use the <code>BSpline</code> 3D transform. Instead of initiating the Bspline with some transform initializer I use the <code>SetInitialTransform(compositeTransform)</code>.</p>
<p>The problem is: When I start to configure the multi-resolution parameters of BSpline stage, specially the<br>
<code>TransformParametersAdaptors</code>, I face a problem when setting the adaptor:<br>
<code>bsplineAdaptor-&gt;SetTransform(compositeTransform)</code>.</p>
<p>I use the <code>CompositeTransform</code>, which is the initial transform of this stage,  and it <strong>displays and error</strong>. A mismatch transform type error. It was expecting a <code>BSplineTransform</code> and received a <code>CompositTransform</code>.</p>
<p>How can I solve it? I know that if I remove the whole multi-resolution deal for BSpline This could be solved. Although, I would like to maintain the multi-resolution for BSpline stage.</p>
<p>Any suggestions are welcomed.</p>

---
