---
topic_id: 862
title: "Error Handling How To Do"
date: 2017-08-13
url: https://discourse.slicer.org/t/862
---

# Error handling, how to do?

**Topic ID**: 862
**Date**: 2017-08-13
**URL**: https://discourse.slicer.org/t/error-handling-how-to-do/862

---

## Post #1 by @Alexandre_Freitas_Du (2017-08-13 20:22 UTC)

<p>Hello everyone, is there any way to handle Exceptions in Loadable? Using “try catch” does not work, always generating the same log, and closing Slicer 3D.</p>
<p>" … exit abnormally - Report the problem. "</p>

---

## Post #2 by @lassoan (2017-08-14 01:09 UTC)

<p>In C++ errors are often not handled using exceptions. In Slicer, errors are handled by returning error codes/specific values indicating errors.</p>
<p>In your loadable modules, you may decide to use exceptions internally but you must catch all the exceptions that you throw.</p>

---
