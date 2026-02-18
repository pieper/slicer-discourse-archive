# qMRMLSubjectHierarchyTreeView Makes a column uneditable

**Topic ID**: 25038
**Date**: 2022-09-01
**URL**: https://discourse.slicer.org/t/qmrmlsubjecthierarchytreeview-makes-a-column-uneditable/25038

---

## Post #1 by @miniminic (2022-09-01 06:11 UTC)

<p>I created an extension, I want to make nameColumn uneditable, how should i do<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a4a2e507cb717c39df2f0960310bad6d8c2de5a.png" data-download-href="/uploads/short-url/1t1HO6zBBzDd9uHOFRXG0Pt2wz0.png?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a4a2e507cb717c39df2f0960310bad6d8c2de5a_2_690x481.png" alt="捕获" data-base62-sha1="1t1HO6zBBzDd9uHOFRXG0Pt2wz0" width="690" height="481" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a4a2e507cb717c39df2f0960310bad6d8c2de5a_2_690x481.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a4a2e507cb717c39df2f0960310bad6d8c2de5a_2_1035x721.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a4a2e507cb717c39df2f0960310bad6d8c2de5a.png 2x" data-dominant-color="505053"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">1204×840 79.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-09-02 03:37 UTC)

<p>You can use standard Qt API to make items non-editable. Maybe you can try clearing the Qt::ItemIsEditable flag in the tree view item.</p>

---

## Post #3 by @miniminic (2022-09-02 06:24 UTC)

<p>thanks, I rewrote the qMRMLSubjectHierarchyModel: : subjectHierarchyItemFlags method implements this function, but I don’t know where the model set to the treeview is correct<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80d637c75d9f364d333e855eb30e66e906d0ef23.png" data-download-href="/uploads/short-url/inK4HQ8HfxjVxv0CcDWaqRNR0MX.png?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80d637c75d9f364d333e855eb30e66e906d0ef23_2_690x240.png" alt="捕获" data-base62-sha1="inK4HQ8HfxjVxv0CcDWaqRNR0MX" width="690" height="240" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80d637c75d9f364d333e855eb30e66e906d0ef23_2_690x240.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80d637c75d9f364d333e855eb30e66e906d0ef23_2_1035x360.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80d637c75d9f364d333e855eb30e66e906d0ef23.png 2x" data-dominant-color="222423"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">1188×414 28.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42e7a99a07f93b4fdcaba3a7cf19a7ae4c27d159.png" data-download-href="/uploads/short-url/9xRQyu5Yki7DZ1zYXqbFfLZOp5v.png?dl=1" title="捕获1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42e7a99a07f93b4fdcaba3a7cf19a7ae4c27d159_2_690x415.png" alt="捕获1" data-base62-sha1="9xRQyu5Yki7DZ1zYXqbFfLZOp5v" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42e7a99a07f93b4fdcaba3a7cf19a7ae4c27d159_2_690x415.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42e7a99a07f93b4fdcaba3a7cf19a7ae4c27d159_2_1035x622.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42e7a99a07f93b4fdcaba3a7cf19a7ae4c27d159.png 2x" data-dominant-color="212322"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获1</span><span class="informations">1152×693 42.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2022-09-03 12:30 UTC)

<p>It looks good. Just to improve style and readability, I would add handle the editable flag in a separate <code>if</code> branch.</p>

---
