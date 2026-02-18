# Can 3D slicer support other languages? Or how to add additional language libraries, such as Chinese?

**Topic ID**: 14751
**Date**: 2020-11-24
**URL**: https://discourse.slicer.org/t/can-3d-slicer-support-other-languages-or-how-to-add-additional-language-libraries-such-as-chinese/14751

---

## Post #1 by @Aitekk (2020-11-24 02:12 UTC)

<p>Is there any way to make slicer support other languages? Such as add an extra language library. We need to translate slicer to Chinese. Slicer is an excellent tool for medical image. If it is compatible with more languages, its generalization will be greatly increased. Can you give me some suggestions？Thanks!</p>

---

## Post #2 by @lassoan (2020-11-24 02:53 UTC)

<p>There are ongoing efforts for translation to Spanish and Arabic and there have been previous work on Chinese that could be .</p>
<p>Some parts of the application can be translated already, while other parts require some software development work. See some more information here:</p>
<aside class="quote quote-modified" data-post="4" data-topic="579">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/ec9cab/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-internationalization/579/4">Slicer Internationalization</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Thanks for the information <a class="mention" href="/u/jcfr">@jcfr</a> 
I have compiled the slicer with  Slicer_BUILD_I18N_SUPPORT enabled in cmake gui but cannot see the language combobox and international panel in general settings, do I miss something to make it works? 
cmake settings 
[image] 
I also check with visual studo, seems Slicer_BUILD_I18N_SUPPORT is not really enable in codes? 
[image] 
Ted
  </blockquote>
</aside>

<aside class="quote" data-post="1" data-topic="1829">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/timeanddoctor/48/5839_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/is-there-any-tutorial-how-to-translate-the-english-language-to-another/1829">Is there any tutorial "how to translate the English language to another"?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: 
Slicer version: 
Expected behavior: 
Actual behavior: 
I was deeply attracted by the powerful function of 3DSlicer. And I think that If there was no language barrier, it could spread more widely. If there are any open program like that “Change Language” and I am very interesting to translate the English to Chinese. As a doctor, however, I donot know how to deal with that. So dose anyone could give a video tutorial to do.
  </blockquote>
</aside>

<p>I think right now what we miss is software engineering effort to review/update <a href="https://github.com/Slicer/SlicerGitSVNArchive/pull/898/files">this pull request</a> for the latest Slicer version and get it integrated into Slicer core. It could be done either by finding a volunteer (preferably by someone who speaks Chinese) or by giving a contract to Kitware.</p>

---
