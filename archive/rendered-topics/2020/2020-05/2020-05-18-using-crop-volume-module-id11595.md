# Using crop volume module

**Topic ID**: 11595
**Date**: 2020-05-18
**URL**: https://discourse.slicer.org/t/using-crop-volume-module/11595

---

## Post #1 by @Deepa (2020-05-18 05:17 UTC)

<p>This is a follow up to my previous post <a href="https://discourse.slicer.org/t/3d-reconstruction-from-2d-slices/9784">here</a><br>
After loading the data, I try to use the crop volume module to downsample the data and the error that is<br>
displayed in the snapshot occurs.<br>
Any suggestions on how to resolve this error will be really helpful.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db49342598976bdfae58dd0813d2b93cf1826752.png" data-download-href="/uploads/short-url/vhTp3RbDDy3lk4dekxAogAdjAgG.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db49342598976bdfae58dd0813d2b93cf1826752_2_690x369.png" alt="Untitled" data-base62-sha1="vhTp3RbDDy3lk4dekxAogAdjAgG" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db49342598976bdfae58dd0813d2b93cf1826752_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db49342598976bdfae58dd0813d2b93cf1826752_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db49342598976bdfae58dd0813d2b93cf1826752_2_1380x738.png 2x" data-dominant-color="878790"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1919×1029 92.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2020-05-18 06:18 UTC)

<p>Bad Allocation is the key, you are running out of memory.</p>
<p>You can try the <a href="https://github.com/SlicerMorph/W_2020/tree/master/Lab02_Slicer_2_Data_Import#import-non-dicom-image-sequences-using-imagestacks-module" rel="nofollow noopener">ImageStacks</a> module from SlicerMorph extension to downsample at the time of import.</p>

---

## Post #3 by @lassoan (2020-05-18 17:55 UTC)

<p>Alternatively, you can <a href="https://www.windowscentral.com/how-change-virtual-memory-size-windows-10">increase virtual memory size in your Windows system settings</a>.</p>

---

## Post #4 by @Deepa (2020-05-20 11:22 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="11595">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>SlicerMorph</p>
</blockquote>
</aside>
<p>Unfortunately, I am not able to find SlicerMorph in install extensions search while trying to install the extension on a remote server.</p>
<p><code>No extensions found for linux:64-bit, revision: '28257'. Please try a different combination</code></p>

---

## Post #5 by @muratmaga (2020-05-20 15:48 UTC)

<p>SlicerMorph is only available for preview versions (4.11)</p>

---
