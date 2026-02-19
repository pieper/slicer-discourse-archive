---
topic_id: 18519
title: "Adjust Opacity Of Scalar Value"
date: 2021-07-05
url: https://discourse.slicer.org/t/18519
---

# Adjust opacity of scalar value

**Topic ID**: 18519
**Date**: 2021-07-05
**URL**: https://discourse.slicer.org/t/adjust-opacity-of-scalar-value/18519

---

## Post #1 by @seanchoi0519 (2021-07-05 14:19 UTC)

<p>Hello,</p>
<p>Just wondering if it’s possible to adjust the opacity of a model’s scalar (not the opacity of the model display node) programmatically?</p>
<p>For example, something like:<br>
model.GetDisplayNode().SetScalarOpacity(x)<br>
NOT model.GetDisplayNode().SetOpacity(x)</p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2021-07-09 05:09 UTC)

<p>You can specify opacity in the color node that you use for displaying the scalars. See complete example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-custom-color-table">here</a>. The last argument of <code>SetColor</code> method is the alpha (opacity) value.</p>

---
