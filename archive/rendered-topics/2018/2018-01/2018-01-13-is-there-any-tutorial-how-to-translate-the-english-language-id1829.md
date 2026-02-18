# Is there any tutorial "how to translate the English language to another"?

**Topic ID**: 1829
**Date**: 2018-01-13
**URL**: https://discourse.slicer.org/t/is-there-any-tutorial-how-to-translate-the-english-language-to-another/1829

---

## Post #1 by @timeanddoctor (2018-01-13 10:09 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:<br>
I was deeply attracted by the powerful function of 3DSlicer. And I think that If there was no language barrier, it could spread more widely. If there are any open program like that “Change Language” and I am very interesting to translate the English to Chinese. As a doctor, however, I donot know how to deal with that. So dose anyone could give a video tutorial to do.</p>

---

## Post #2 by @chir.set (2018-01-13 10:32 UTC)

<p>Some information relative to i18n is here :<br>
<a href="https://www.slicer.org/wiki/Documentation/Labs/I18N" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Labs/I18N</a></p>
<p>It might still be possible to translate the UI strings only  and start Slicer with LC_NUMERIC=C as environment variable, so that engine libraries like VTK and so on don’t bother about locale specific settings. Then it becomes a huge work requiring widespread man power and big sustained funding.</p>

---

## Post #3 by @lassoan (2018-01-13 15:34 UTC)

<p>Adding language switching feature to Slicer would require some software development, probably a couple of months of work of a Slicer core developer ($30-60k). Considering that Slicer can replace software that costs tens of thousands of dollars for a single license, this cost is quite low, but current funding sources of Slicer are mostly North-American, so developing this feature has not been a priority.</p>
<p>I would recommend to apply for Chinese grant funding, starting a crowdfunding campaign, and/or team up with groups in other countries to get funding. I know that there are Spanish-speaking and African groups who would be very interested in having this feature, too.</p>

---

## Post #4 by @jruiz (2018-01-13 16:58 UTC)

<p>Hi, you’re right Andras,</p>
<p>we’re in fact very interested in adding multilingual functionality to Slicer. Our group from the University of Las Palmas de Gran Canaria (Spain) will be happy to collaborate and allocate some time of our developers for the internationalization of Slicer. Of course, we’d also be interested in participating in some new grant application with this specific goal. I think some of our African partners will also be very interested. We have Spanish, French, Portuguese and Arabic native speakers.</p>
<p>Looking forward, Juan</p>

---

## Post #5 by @lassoan (2018-01-13 20:50 UTC)

<p>Anybody else who would be interested in joining these efforts, by contributing funding, software development, or translation work - please add a note here.</p>

---

## Post #6 by @fedorov (2018-01-14 03:51 UTC)

<p>I can contribute to translation to Russian, although I think it would need more than one person, as I think finding good matching words might not be straightforward in all cases and ideally should involve at least some discussion.</p>

---

## Post #7 by @timeanddoctor (2018-02-12 08:03 UTC)

<p>I try to set up a  3D Slicer-China forum,the temporary web site is: <em>(dead link removed)</em>, for communication more convenient. But I still not sure the permission of 3D Slicer developers will stand with me.</p>
<p>So, I write some reasons here:<br>
1, Bypass the “internet great-wall” in China. Most people in my country can not browse google/youtube websites, while such areas seems to be very important to get the knowlege of 3dslicer.<br>
2, A low-cost method to the workers of programming or medical to participate in the translation project.<br>
3, All works will be doing under 3dslicer related license: <a href="https://www.slicer.org/wiki/License" class="inline-onebox" rel="noopener nofollow ugc">License - Slicer Wiki</a><br>
<a href="https://en.wikipedia.org/wiki/Open-source_model" class="inline-onebox" rel="noopener nofollow ugc">Open source - Wikipedia</a><br>
4, As a doctor, from Binzhou Medical University Hospital, I think there is no conflict with others…<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2903501c9f95920bb0d45623a8af6a35a35c813.png" alt="" data-base62-sha1="u2JejVW8K8RmLqDErJUGZ16qSv9" role="presentation" width="400" height="117">.<br>
<a href="http://en.byfy.cn/" rel="noopener nofollow ugc">http://en.byfy.cn/</a></p>
<p>sincerely,<br>
Li</p>

---

## Post #8 by @pieper (2018-02-12 15:10 UTC)

<p>Hi Li -</p>
<p>This sounds very good and we appreciate your help.  You don’t need any special permission from us for your site.  Of course we do want to continue to collaborate.</p>
<p>Regarding point 1, I hope creators of tutorial videos can also provide download links for the original videos so they can be uploaded to appropriate sites accessible in China.</p>
<p>By coincidence I just learned this morning about some very interesting training material in Chinese that’s hosted on WeChat.  I’ve added links to the slicer wiki in the 4.8 and Nightly sections:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Training#Resources_for_Chinese_users" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Training#Resources_for_Chinese_users</a></p>
<p>(Even non-Chinese speakers will be interested in seeing these - they are quite detailed and well illustrated).</p>
<p>-Steve</p>

---

## Post #9 by @lassoan (2018-02-12 22:39 UTC)

<p>Very nice effort, thank you! Translation would require some core development, as described above.</p>
<p>It is interesting to note that the number of Chinese users has surpassed US and Canadian combined (based on last 12 months download statistics). It would make sense to try to get some Chinese government grant funding channeled into Slicer core development - at least for features like internationization, which will not likely to get any support from North American funding sources.</p>

---

## Post #10 by @timeanddoctor (2018-04-07 03:42 UTC)

<p>Many doctors including myself, who are interested in 3d-slicer, want to traslate it to a Chiese now, <a href="https://forum.slicercn.com/t/topic/223" rel="nofollow noopener">https://forum.slicercn.com/t/topic/223</a>.<br>
However, we have some troubles for that.<br>
Who can tell me more detail meaning about the word “Volume”, which is meanging of “size” in Chinese…<br>
and “Transform”…</p>

---

## Post #11 by @pieper (2018-04-07 13:25 UTC)

<p>Hi - it’s great to see the activity on the Chinese forum.  When I view it in Google Chrome the automatic translation is pretty good to give me a sense of what’s going on.</p>
<p>Regarding the two terms:</p>
<p>We use “Volume” in Slicer to refer to data regularly sampled over a spatial extent.  Each sample is a ‘voxel’ In practice this typically corresponds to a 3D medical image acquisition, often a DICOM “series” from a CT or MR study (but this isn’t always a one-to-one mapping).  A Scalar Volume has one quantity per voxel, where a Vector Volume may have many values and a Tensor Volume has a 3x3 matrix of values at each voxel.</p>
<p>A “Transform” is a representation of a mathematical function that maps one space to another space.  In Slicer these are 3D mappings in patient space (in the right-anterior-superior reference frame convention).  Transforms can be linear (represented by a 4x4 matrix) or general nonlinear functions.</p>
<p>Hope that helps.</p>
<p>Also I see on the <a href="http://forum.slicercn.com">forum.slicercn.com</a> forum the question about foo bar, which comes from <a href="https://en.wikipedia.org/wiki/List_of_military_slang_terms#FUBAR">fubar</a> and is used as a joke.  <img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=5" title=":rofl:" class="emoji" alt=":rofl:"></p>

---

## Post #12 by @timeanddoctor (2018-04-08 10:27 UTC)

<p>Thank you very much！<br>
It is very usfull.<br>
Thanks.<br>
Li Zhenzhu</p>

---

## Post #13 by @fedorov (2018-05-02 22:21 UTC)

<p>Note that at least some of the concepts used in Slicer are broadly applicable across medical imaging domain. DICOM standard probably includes definitions (or at least mentions!) for a subset of those. According to <a href="https://www.dicomstandard.org/translation/">this article</a>, back in 2015, NEMA granted the permission to someone to translate the DICOM standard text to Chinese. Maybe you can find that resource, and then you could cross-reference paragraphs to find mapping for the terms?</p>
<p>I also found this repository that seems to be translating some parts of DICOM to Chinese: <a href="https://github.com/zssure-thu/DICOM-Chinese">https://github.com/zssure-thu/DICOM-Chinese</a>.</p>
<p>Just a few resources I could find quickly. DICOM is an international standard, so it can help you.</p>

---

## Post #14 by @cyufu (2018-06-26 07:45 UTC)

<p><a href="https://www.slicercn.com/" rel="noopener nofollow ugc">www.slicercn.com</a></p>
<p><a href="https://forum.slicercn.com/" rel="noopener nofollow ugc">forum.slicercn.com</a></p>
<p>Chinese test version</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb9afa207841473b3c0cc40ed23706ed551e9670.png" data-download-href="/uploads/short-url/qLDk4E3mnQ0R1lzLfDb6dbc0n1S.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb9afa207841473b3c0cc40ed23706ed551e9670_2_690x466.png" alt="image" data-base62-sha1="qLDk4E3mnQ0R1lzLfDb6dbc0n1S" width="690" height="466" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb9afa207841473b3c0cc40ed23706ed551e9670_2_690x466.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb9afa207841473b3c0cc40ed23706ed551e9670.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb9afa207841473b3c0cc40ed23706ed551e9670.png 2x" data-dominant-color="D1CFDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">994×672 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @pieper (2018-06-26 10:47 UTC)

<p><a class="mention" href="/u/cyufu">@cyufu</a> looks great!  Is there an installer people could test? (sorry maybe it’s available from the links you sent but I couldn’t read the Chinese <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=5" title=":smile:" class="emoji" alt=":smile:">)</p>

---

## Post #16 by @timeanddoctor (2018-06-26 11:06 UTC)

<p>Great, Thank you very much.</p>

---

## Post #17 by @cyufu (2018-06-26 11:07 UTC)

<p>Chinese version download link on Baidu cloud network disk：<a href="https://forum.slicercn.com/t/topic/447" class="inline-onebox" rel="noopener nofollow ugc">3DSlicer汉化辅助软件发布 - 社区公告 - 3DSlicer中文论坛</a></p>
<p>Developed a software for 3DSlicer internationalization by Doctor Jindan Xiong （浙江新安熊金丹医生）from Zhejiang Province, China.</p>
<p>Korean version：</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f10ba2f14d17150d4312601ad07eed073cff67ce.jpeg" data-download-href="/uploads/short-url/yoo05AcweX8POoWCQ3tEiKm06aG.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f10ba2f14d17150d4312601ad07eed073cff67ce_2_688x408.jpg" alt="image" data-base62-sha1="yoo05AcweX8POoWCQ3tEiKm06aG" width="688" height="408" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f10ba2f14d17150d4312601ad07eed073cff67ce_2_688x408.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f10ba2f14d17150d4312601ad07eed073cff67ce_2_1032x612.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f10ba2f14d17150d4312601ad07eed073cff67ce.jpeg 2x" data-dominant-color="98999F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1146×682 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Chinese version：</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d07fd30a10f3d788ca8bbbb07039fbb20734eec3.png" data-download-href="/uploads/short-url/tKtaVJa0zjpL0QLffazR8jYNTLJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d07fd30a10f3d788ca8bbbb07039fbb20734eec3_2_688x491.png" alt="image" data-base62-sha1="tKtaVJa0zjpL0QLffazR8jYNTLJ" width="688" height="491" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d07fd30a10f3d788ca8bbbb07039fbb20734eec3_2_688x491.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d07fd30a10f3d788ca8bbbb07039fbb20734eec3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d07fd30a10f3d788ca8bbbb07039fbb20734eec3.png 2x" data-dominant-color="B6B8BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">843×602 70.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #18 by @Liu-Huaqing (2018-09-18 03:11 UTC)

<p><em>[Translated from original using Google translate]</em> Thank you very much for the Chinese version, I am also very interested in 3D Slicer, convenient to add a micro-letter it? My micro Signal</p>
<details>
<summary>
Original</summary>
<p>非常感谢您的汉化版本，我对 3D Slicer 也非常感兴趣，方便加个微信吗？我微信号: 15117946626</p>
</details>

---

## Post #19 by @manjula (2020-04-22 22:26 UTC)

<p>Hi,</p>
<p>What is the current status of the 3D slicer internationalization ?</p>
<p>I would like to translate the 3D Slicer to Sinhalese if it is simple editing a .po file or similar.</p>
<p>From what I read i could not see that this effort has really taken of apart from  some great work from the Chinese teams but i suspect it is a isolated effort.</p>
<p>But i would very much appreciate a update on this.</p>

---

## Post #20 by @timeanddoctor (2020-04-23 05:20 UTC)

<p>The work of translation is an arduous task. We had translated the GUI and core modules of slicer and the Chinese version keeped in 4.7 untill now,while slicer is developing continuously.</p>

---

## Post #21 by @manjula (2020-04-23 07:17 UTC)

<aside class="quote no-group" data-username="timeanddoctor" data-post="20" data-topic="1829">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/timeanddoctor/48/5839_2.png" class="avatar"> timeanddoctor:</div>
<blockquote>
<p>arduous</p>
</blockquote>
</aside>
<p>That is what i could gather too… Is it not possible to move to a system like all other software where localization is simply a matter of editing the POT files… or does that process require lots of effort and funding…</p>

---

## Post #22 by @pieper (2020-04-23 11:43 UTC)

<p>There’s a lot of excellent information on this topic in the thread below.  Basically, yes it’s a complex project but achievable with effort.</p>
<aside class="quote quote-modified" data-post="1" data-topic="579">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/slicer-internationalization/579">Slicer Internationalization</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category --style-square " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
    </div>
  </div>
  <blockquote>
    <a name="overview-1" class="anchor" href="#overview-1"></a>Overview
Following conversation with <a class="mention" href="/u/marilola">@marilola</a> that took place during the 25th Slicer project week, I am summarizing here the current state of the Slicer internationalization framework. 
Prior discussion and description of the I18N framework can be found here: 

<a href="https://www.slicer.org/wiki/Documentation/Labs/I18N" class="inline-onebox">Documentation/Labs/I18N - Slicer Wiki</a>
<a href="https://www.slicer.org/wiki/Slicer4:Internationalization_of_Slicer" class="inline-onebox">Slicer4:Internationalization of Slicer - Slicer Wiki</a>

<a name="technology-2" class="anchor" href="#technology-2"></a>Technology
Since most of the user facing strings to translate are associated with user interface components implemented using Qt, we standardized…
  </blockquote>
</aside>


---

## Post #23 by @Melodicpinpon (2020-04-23 12:23 UTC)

<p>I could do the french translation if needed but have to consult my boss first.</p>

---

## Post #24 by @cpinter (2020-04-23 12:58 UTC)

<p>As far as I know Spanish and Arabic translations are already ongoing, although I’m not sure about their current status. If somebody is taking on any of these two, then please contact me so we can coordinate.</p>

---

## Post #25 by @manurare (2021-06-01 17:45 UTC)

<p>Hi,</p>
<p>Any update on the Spanish translation?  Is there any alpha/beta translation file in progress we can use?</p>

---

## Post #26 by @lassoan (2021-06-04 05:31 UTC)

<p>We have submitted a CZI Essential Software application for getting funding for developing infrastructure for internationalization of 3D Slicer (the full user interface, all kinds of modules, and their help an documentation). We’ll hear from the result in late July.</p>
<p>There have been preliminary work that <a class="mention" href="/u/cpinter">@cpinter</a> mentioned, which aimed for translation of specific parts of the application. However, without strong internationalization infrastructure in Slicer core, it is quite limited how far these efforts can go.</p>

---

## Post #27 by @cpinter (2021-06-04 10:48 UTC)

<p>I asked for the repositories of this previous effort I mentioned, here is the answer:</p>
<ul>
<li>I worked on the i10n of script modules, and it showed in the PW31_2019_Boston ( <a href="https://projectweek.na-mic.org/PW31_2019_Boston/Projects/Globalization3DSlicer_OHIF/">link</a> ) you can find the commits and next steps.</li>
<li>For more details see the pull request <a href="https://github.com/Slicer/SlicerGitSVNArchive/pull/1162">link</a>
</li>
</ul>
<p>Maybe some of this can be built upon.</p>

---

## Post #28 by @timeanddoctor (2021-06-04 14:33 UTC)

<p>That is a good news!</p>

---
