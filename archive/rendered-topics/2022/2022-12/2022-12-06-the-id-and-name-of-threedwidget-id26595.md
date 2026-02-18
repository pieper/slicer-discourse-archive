# The id and name of ThreeDWidget

**Topic ID**: 26595
**Date**: 2022-12-06
**URL**: https://discourse.slicer.org/t/the-id-and-name-of-threedwidget/26595

---

## Post #1 by @f1oNae (2022-12-06 08:14 UTC)

<p>I have created several 3dwidgets,and now I need to get ThreeDWidget.<br>
I can’t get ThreeDWidget in order.<br>
I get the name of ThreeDWidget first.The name doesn’t correspond to the ID.<br>
But when I try to get qMRMLThreeDWidget through names,it  has no return value.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e53e37946e3650ea2ecbec10f2666c19f4c4878.png" data-download-href="/uploads/short-url/baUYkH84Popsn1QeziEgVAB9YQE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e53e37946e3650ea2ecbec10f2666c19f4c4878.png" alt="image" data-base62-sha1="baUYkH84Popsn1QeziEgVAB9YQE" width="690" height="188" data-dominant-color="EFEFF6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">864×236 12.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The related source code of slicer as follows:<br>
<a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Widgets/qMRMLLayoutManager.h#:~:text=///%20Get%203D,id" class="inline-onebox" rel="noopener nofollow ugc">Slicer/Libs/MRML/Widgets/qMRMLLayoutManager.h at main · Slicer/Slicer · GitHub</a>)const%3B</p>

---

## Post #2 by @RafaelPalomar (2022-12-06 09:07 UTC)

<p><a class="mention" href="/u/f1onae">@f1oNae</a>, have you tried with some of the snippets in the python script repository (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>)? More precisely, the snippets in this section may help you: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-vtk-rendering-classes" rel="noopener nofollow ugc">Access VTK rendering classes</a>.</p>
<p>Let us know if this does not help you.</p>

---

## Post #3 by @f1oNae (2022-12-06 09:20 UTC)

<p>yeah,I Iterate through all 3D views in current layout,finally find that the real name of the 3DWidget is “View1”-“View16” instead of “ThreeDWidgetX”!!!<br>
Thanks for your help!</p>

---
