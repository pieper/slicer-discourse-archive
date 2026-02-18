# Create a data probe for slicelet

**Topic ID**: 13478
**Date**: 2020-09-14
**URL**: https://discourse.slicer.org/t/create-a-data-probe-for-slicelet/13478

---

## Post #1 by @Chintha_Siva_Prasad (2020-09-14 11:28 UTC)

<p>How to create a data probe for a slicelet that has no main window?<br>
I had tried code given in nightly scripted modules,but it is only working in presence of main window only,</p>

---

## Post #2 by @lassoan (2020-09-14 11:36 UTC)

<p>Behavior of application without a main window would be so different that we do not support this option anymore. There wouls be a huge additional cost in review, testing, and maintenance, for very little the benefits.</p>
<p>Instead, you can have a main window and hide (or do not create) any elements that you don’t need. This is how all the custom applications work now.</p>

---
