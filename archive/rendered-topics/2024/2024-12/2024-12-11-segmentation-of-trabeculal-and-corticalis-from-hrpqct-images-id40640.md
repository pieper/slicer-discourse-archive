# Segmentation of trabeculal and corticalis from HRpQCT images

**Topic ID**: 40640
**Date**: 2024-12-11
**URL**: https://discourse.slicer.org/t/segmentation-of-trabeculal-and-corticalis-from-hrpqct-images/40640

---

## Post #1 by @nikkos (2024-12-11 17:09 UTC)

<p>Hello dear Slicer Community,</p>
<p>I wonder if there is an extension that allows me to automatically segment the corticalis of the femur and the trabeculae ?</p>
<p>Best regards<br>
Niklas</p>

---

## Post #2 by @jamesobutler (2024-12-11 20:16 UTC)

<p>The following are likely relevant to what you are interested in however the mentioned Slicer <a href="https://github.com/Kitware/BoneTextureExtension" rel="noopener nofollow ugc">BoneTextureExtension</a> has had issues recently. <a class="mention" href="/u/muratmaga">@muratmaga</a> whenever you reached out about this extension what was the conclusion about whether it would be updated to work with latest Slicer?</p>
<aside class="quote" data-post="1" data-topic="19049">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/manav_kothari/48/11104_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/separating-cortical-and-trabecular-region-of-talus-bone/19049">Separating Cortical and trabecular region of Talus bone</a> <a class="badge-category__wrapper " href="/c/support/feature-requests/9"><span data-category-id="9" style="--category-badge-color: #F1592A; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="11" data-drop-close="true" class="badge-category --has-parent" title="This category is for submitting ideas about what enhancements or new features should be added to 3D Slicer. Make your voice heard by voting on feature requests - by opening the topic and clicking the Vote button or by creating a new topics. Slicer developers will make it a priority to work on feature requests that have more votes."><span class="badge-category__name">Feature requests</span></span></a>
  </div>
  <blockquote>
    I am interested in separating cortical and trabecular region of Talus bone and generate individual STL file. There is one add-on in Analyze Direct software named Bone Microarchitecture Analysis (BMA). Is there any similar function in Slicer as well? 
Thanking You
  </blockquote>
</aside>

<aside class="quote" data-post="1" data-topic="39711">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/is-bonetexture-extension-abandoned/39711">Is BoneTexture Extension abandoned?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    A colleague of mine needs to use this extension, and it appears that it hasn’t been functioning since v5.0.3. I tried to download that specific release, but the extension catalogue is empty (no extensions are shown). 
There are bunch of issues on the repo, some of which are couple years old. This is listed under Kitware, so I am not sure who is responsible for it…
  </blockquote>
</aside>


---

## Post #3 by @muratmaga (2024-12-12 02:18 UTC)

<p>I think the major blocking issues of expecting labelmaps as input (as opposed to segmentation) are fixed now. Though I haven’t tried it personally. <a class="mention" href="/u/bpaniagua">@bpaniagua</a> is the person who knows best.</p>

---
