# OpenDose 3D Extension

**Topic ID**: 20953
**Date**: 2021-12-07
**URL**: https://discourse.slicer.org/t/opendose-3d-extension/20953

---

## Post #1 by @Michel_Atieh (2021-12-07 17:45 UTC)

<p>Hello, I have installed the extension OpenDose3D. On windows it has all the features, however, on ubuntu there were missing features. I was able to solve the problem by updating the scipy library thorugh the Python interactor by typing pip_install(‘scipy -U’).</p>
<p>Just to let you know that there is this problem.</p>
<p>Thank you and kind regards.</p>

---

## Post #2 by @jamesobutler (2021-12-07 18:28 UTC)

<p>Thanks for the report! I’m assuming you are using Slicer stable 4.11.20210226? A fix was issued in early March 2021 so you shouldn’t have this issue when using the latest Slicer preview build.</p>
<aside class="quote" data-post="3" data-topic="20501">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/error-loading-gpa-module-slicermorph/20501/3">Error loading GPA module (Slicermorph)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    This was resolved in <a href="https://github.com/Slicer/Slicer/commit/fef09b54bd55a5b6bd5870f6f05cde988f8691e3" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix import of python modules on Linux selectively stripping libr… · Slicer/Slicer@fef09b5 · GitHub</a>. It shouldn’t be a problem if you use latest Slicer Preview as that commit came a few days after the latest Stable release back in February.
  </blockquote>
</aside>


---

## Post #3 by @Michel_Atieh (2021-12-07 18:39 UTC)

<p>Yes I am using Slicer stable 4.11.20210226.<br>
The problem only existed on linux and not on windows.<br>
Many of my colleagues had this issue today as we tried using it, so it wasn’t only on my computer.</p>

---

## Post #4 by @jamesobutler (2021-12-07 18:44 UTC)

<p>Yes the issue was a problem only for Linux builds using Slicer 4.11.20210226.</p>

---

## Post #5 by @Alex_Vergara (2021-12-08 09:30 UTC)

<p>Hello, I am the developer of OpenDose3D. First of all, thank you very much for using this extension. The issue you describe is already explained in the documentation present in the <a href="https://gitlab.com/opendose/opendose3d/-/blob/develop/User_Manual.md" rel="noopener nofollow ugc">user manual</a>. This is already solved in latest slicer versions, so next release will have no problems. You can find a full presentation here <a href="https://insermfrance-my.sharepoint.com/:p:/g/personal/alex_vergara-gil_inserm_eu/EcZFakMIx2ZLtDDF52yQuHABfTVs3fsgbrG1YBjMo-qXxw" rel="noopener nofollow ugc">https://insermfrance-my.sharepoint.com/:p:/g/personal/alex_vergara-gil_inserm_eu/EcZFakMIx2ZLtDDF52yQuHABfTVs3fsgbrG1YBjMo-qXxw</a></p>
<p>Please report any issue in the <a href="https://gitlab.com/opendose/opendose3d/-/boards" rel="noopener nofollow ugc">issue tracker</a></p>
<p>Regards<br>
Alex Vergara</p>

---
