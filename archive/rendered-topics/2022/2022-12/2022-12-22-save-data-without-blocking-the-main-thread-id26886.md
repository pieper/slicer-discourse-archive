# Save data without blocking the main thread

**Topic ID**: 26886
**Date**: 2022-12-22
**URL**: https://discourse.slicer.org/t/save-data-without-blocking-the-main-thread/26886

---

## Post #1 by @Osspoor (2022-12-22 14:43 UTC)

<p>Hello! How can I save a certain data in the scene or the whole scene without blocking the main thread (I can do anything else during the save)</p>

---

## Post #2 by @pieper (2022-12-22 15:26 UTC)

<p>Not currently as far as I know.  Implementing this feature would require changes at the C++ level which are not impossible but would require some work by someone with the right skillset.</p>

---

## Post #3 by @lassoan (2022-12-22 22:45 UTC)

<p>You can make saving really fast if you only save what is changed and don’t use compression.</p>

---
