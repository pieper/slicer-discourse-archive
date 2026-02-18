# Simple Filters: node selector doesn't accept Scalar Volume child nodes

**Topic ID**: 22571
**Date**: 2022-03-17
**URL**: https://discourse.slicer.org/t/simple-filters-node-selector-doesnt-accept-scalar-volume-child-nodes/22571

---

## Post #1 by @keri (2022-03-17 22:45 UTC)

<p>Hi,</p>
<p>Is there any reasons why SimpleFilters I/O node selectors don’t accept volume nodes inherited from <code>vtkMRMLScalarVolumeNode</code> (child nodes)?</p>
<p>For example I just tried to set <a href="https://github.com/SimpleITK/SlicerSimpleFilters/blob/92e8db0030f6f9d9ea99dd5d8d1425b6b2189a68/SimpleFilters/SimpleFilters.py#L893" rel="noopener nofollow ugc">inputSelector.showChildNodeTypes = True</a> and it works fine with my custom volume node, I wa able to calculate <code>CosImageFilter</code></p>

---

## Post #2 by @pieper (2022-03-18 12:55 UTC)

<p>This was probably done because some <a href="http://apidocs.slicer.org/master/classvtkMRMLScalarVolumeNode.html">subclasses</a> wouldn’t work with SimpleITK.  But since some would work and because this is sort of an advanced module anyway it might make sense to relax the requirement.</p>

---

## Post #3 by @keri (2022-03-18 13:04 UTC)

<p>Thank you, it would be good</p>

---

## Post #4 by @pieper (2022-03-18 13:10 UTC)

<p>You could submit a PR and then if anyone sees a downside they could comment there.</p>

---

## Post #5 by @keri (2022-03-18 14:41 UTC)

<p>Just in case the PR is <a href="https://github.com/SimpleITK/SlicerSimpleFilters/pull/24" rel="noopener nofollow ugc">ready</a></p>

---
