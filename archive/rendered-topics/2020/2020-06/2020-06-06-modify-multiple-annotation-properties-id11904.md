# Modify Multiple Annotation Properties

**Topic ID**: 11904
**Date**: 2020-06-06
**URL**: https://discourse.slicer.org/t/modify-multiple-annotation-properties/11904

---

## Post #1 by @justo (2020-06-06 14:15 UTC)

<p>Hello everyone,</p>
<p>I’m working with multiple annotations in the same scene, all of them are AnnotationRuler and I want them all to have same properties. But the only way I’ve found to edit the properties is by clicking on the icon below (in the image) and changing the annotation properties one by one.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20c11ea8fba7a98321e195cad773d20fea8e863c.png" data-download-href="/uploads/short-url/4FL2fk8y8xgt1WJ5YirVt76Onda.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20c11ea8fba7a98321e195cad773d20fea8e863c_2_547x499.png" alt="image" data-base62-sha1="4FL2fk8y8xgt1WJ5YirVt76Onda" width="547" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20c11ea8fba7a98321e195cad773d20fea8e863c_2_547x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20c11ea8fba7a98321e195cad773d20fea8e863c_2_820x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20c11ea8fba7a98321e195cad773d20fea8e863c.png 2x" data-dominant-color="E7EBEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">950×868 59 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there a way to change the properties of all the Annotations at once?</p>
<p>Thanks in advance!</p>
<p>Operating system: macOS Catalina 10.15.3<br>
Slicer version: 4.10.1<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @pieper (2020-06-06 14:46 UTC)

<p>No, I think you’d need to write a python script for that.</p>

---

## Post #3 by @lassoan (2020-06-06 14:57 UTC)

<p>Annotations are being replaced by the much more powerful Markups module (in Slicer-4.11). Markups allows you to set display properties (color and visibility) of all markups in a folder at once.</p>
<p>Go to Markups or Data module, create a folder, drag-and-drop markups (lines, angles, fiducial lists, planes, curves, etc.) into that folder, and right-click on the folder’s eye icon to enable “Apply color to all children” to apply folder’s color and visibility options to all markups in that folder.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bc44d9e41524ba433f76dc127cc37c1b8a65a05.jpeg" data-download-href="/uploads/short-url/fnlFlVMZY0Md7UUzDc6QkScF5pH.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bc44d9e41524ba433f76dc127cc37c1b8a65a05_2_690x327.jpeg" alt="image" data-base62-sha1="fnlFlVMZY0Md7UUzDc6QkScF5pH" width="690" height="327" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bc44d9e41524ba433f76dc127cc37c1b8a65a05_2_690x327.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bc44d9e41524ba433f76dc127cc37c1b8a65a05_2_1035x490.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bc44d9e41524ba433f76dc127cc37c1b8a65a05_2_1380x654.jpeg 2x" data-dominant-color="A9B7BE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1069 374 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
