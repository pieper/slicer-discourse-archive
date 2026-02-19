---
topic_id: 24298
title: "Inline Documentation"
date: 2022-07-13
url: https://discourse.slicer.org/t/24298
---

# Inline documentation

**Topic ID**: 24298
**Date**: 2022-07-13
**URL**: https://discourse.slicer.org/t/inline-documentation/24298

---

## Post #1 by @muratmaga (2022-07-13 18:05 UTC)

<p>We have <a href="https://github.com/SlicerMorph/Tutorials/blob/main/README.md" rel="noopener nofollow ugc">tutorials for SlicerMorph community</a> on GH.</p>
<p>I would like to make a small utility module that we can bundle with SlicerMorph extension to provide this information to the users. Currently the plan is to have list of tutorials displayed in the module panel, and when clicked on, the internal web browser will display them.</p>
<p>Are there any better alternatives to this? Would it be possible to render the pages inside the module panel or Slicer application window for more close intergration?</p>

---

## Post #2 by @pieper (2022-07-13 20:17 UTC)

<p>I don’t see any technical limitations on this.  You can embed the web widget in the module panel or elsewhere in the main window, like where the python console is.  The main issue would be how to lay out the content so that users can easily follow the tutorial and access the Slicer controls at the same time.</p>

---
