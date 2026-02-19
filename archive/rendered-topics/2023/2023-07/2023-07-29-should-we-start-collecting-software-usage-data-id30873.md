---
topic_id: 30873
title: "Should We Start Collecting Software Usage Data"
date: 2023-07-29
url: https://discourse.slicer.org/t/30873
---

# Should we start collecting software usage data?

**Topic ID**: 30873
**Date**: 2023-07-29
**URL**: https://discourse.slicer.org/t/should-we-start-collecting-software-usage-data/30873

---

## Post #1 by @lassoan (2023-07-29 19:52 UTC)

<p>Several extension developers asked about and toying with the idea of starting to collect software usage data. I completely agree that such data can be useful for prioritizing developments and can be a good motivator for developers to devote more of their time to a project. However, I also see a huge risk of eroding users’ trust if extension developers start to implement some home-made mechanisms for phoning home from their modules to collect such data.</p>
<p>I believe there is a way to fulfill this request of developers while also respecting user privacy, because it has become standard practice in many software to opt in into sharing usage data. If we develop such feature carefully and do everything very transparently then it should not have a negative impact. <strong>What do you think?</strong></p>
<p>For example, what I could imagine to be acceptable is an opt-in feature that would allow collecting some counter values (e.g., how many times a certain features is used) and reporting to a Slicer-community-maintained server, with the results publicly available. The mechanism could be used by both Slicer core and extensions. Module developers could specify what events they want to count. Users could inspect what data is sent and they could opt out anytime.</p>

---

## Post #2 by @mau_igna_06 (2023-07-29 23:25 UTC)

<p>In <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner#bonereconstructionplanner" rel="noopener nofollow ugc">BoneReconstructionPlanner</a>, the Mandible Reconstruction extension, we would like to collect at least a metric related to ‘a unique Virtual Surgical Plan and Personalized Surgical Guide design per patient per case’. I guess this could involve detecting when a 3D model (tagged as surgical guide) is saved as a file (to be 3D printed later). Maybe also distinguish per patient <a href="https://stackoverflow.com/a/9316461" rel="noopener nofollow ugc">by converting the patient MRN or other personal data to an encrypted SHA string</a>. Maybe also detect between scene created/imported and scene closed events.</p>

---

## Post #3 by @lassoan (2023-07-30 13:28 UTC)

<p>Thanks for the feedback. So, it seems that a few event counters specific to your module would suffice. I guess the counts should be accumulated per day.</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="2" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>Maybe also distinguish per patient <a href="https://stackoverflow.com/a/9316461">by converting the patient MRN or other personal data to an encrypted SHA string </a>.</p>
</blockquote>
</aside>
<p>This is a good point, we should decide if fingerprinting user or patient data is acceptable and describe some guidelines for module developers.</p>

---

## Post #4 by @jamesobutler (2023-07-30 14:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>However, I also see a huge risk of eroding users’ trust if extension developers start to implement some home-made mechanisms for phoning home from their modules to collect such data.</p>
</blockquote>
</aside>
<p>Extension developers could do this today which is a concern that has to be accepted with the current use of the Slicer Extensions Index. For extensions to make it into the Slicer Extensions Index, there is an approval process which implies that Slicer leadership has put their stamp of approval on the extension and that it is safe to use. However this may not be the intention.</p>
<ul>
<li>Is there any funding to moderate the content on the Slicer extensions index to enforce a Slicer defined privacy policy? This is to provide confidence in the First Party App Store solution.
<ul>
<li>If minimal funding, maybe the Slicer extensions index has to set all extensions to a specific git hash, so that every update of the extension can be reviewed to confirm compliance. This would certainly reduce convenience, but the value gain would be increased trust of the first party App Store. Maybe compliance review could be semi-automated instead of fully manual?</li>
<li>If no specific funding, maybe finding a way for extensions to self-publish their extension where they don’t have to follow the Slicer Extensions Index privacy policy. This would be the Third Party App Store solution. The Extensions Manager could point to a web address to the third party location of the extension.</li>
</ul>
</li>
<li>What might be the process of Slicer Custom Applications that use extensions to verify that their use of the extension is not sending data to an outside source? To make sure the extensions are not breaking their custom app’s privacy policy?</li>
</ul>
<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>and reporting to a Slicer-community-maintained server, with the results publicly available.</p>
</blockquote>
</aside>
<ul>
<li>Would the user have any rights to request deletion of data that they submitted (not just opting out of future sending of data)? This request might originate when the user accidentally submitted details when using Slicer in a shared computing environment like an academic lab computer. A shared user might have accepted the policy, but not the current end user.
<ul>
<li>To avoid accidental submission, indicating a pop-up at startup whenever opt-in behavior is on could be a possible solution.</li>
</ul>
</li>
</ul>

---

## Post #5 by @lassoan (2023-07-30 17:35 UTC)

<p>Thank you, these are all interesting points.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Extension developers could do this today which is a concern that has to be accepted with the current use of the Slicer Extensions Index.</p>
</blockquote>
</aside>
<p>They can do it because we have not set rules to explicitly forbid this. We could simply say that extensions must not collect and transfer usage data. However, I feel that it could be a fair request from developers to get some feedback, so we should consider not simply reject this request but find a controlled way to do it.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>For extensions to make it into the Slicer Extensions Index, there is an approval process which implies that Slicer leadership has put their stamp of approval on the extension and that it is safe to use. However this may not be the intention.</p>
</blockquote>
</aside>
<p>The extension approval process is an interesting topic, too, but I think it can be discussed separately from the software telemetry rules. We may bring it up later, when we decide on mechanisms to enforce rules. However, since we allow usage of PyPI for installing extensions, it does not make sense to be more strict than PyPI, which means that you need to trust the maintainers of the packages that you install.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>What might be the process of Slicer Custom Applications that use extensions to verify that their use of the extension is not sending data to an outside source?</p>
</blockquote>
</aside>
<p>Most important mechanism is trusting the developers of the extension. For further guarantees, the custom application developer could provide its own extensions catalog that only contains a set of reviewed and approved extension packages.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Would the user have any rights to request deletion of data that they submitted</p>
</blockquote>
</aside>
<p>I think we should only submit anonymized data. This way we would not need to worry about GDPR either. It would clearly provide more accurate and robust data if individual users were identified, but I don’t think it is worth the enormous amount of extra complexity of handling such data. I’m not sure about recording location (e.g., country or city) to submissions, as it would be extremely useful, but it may be considered as personal data.</p>

---

## Post #6 by @rbumm (2023-07-31 09:01 UTC)

<p>Having access to anonymous usage data for 3D Slicer and all its extensions would be incredibly beneficial. Since May 2023, I have been compiling such data for my extension. It has proven enlightening to understand which components of my extension are utilized more frequently, enabling me to focus my developmental efforts appropriately.</p>
<p>It would be fantastic to establish a universal counter mechanism for 3D Slicer, thus simplifying data collection. I posit that an opt-in may not be necessary as long as we ensure the data transmission is strictly anonymous (no IP or time tracking) and solely conducted via a 3D Slicer-specific mechanism.</p>
<p>In fact, I would even advocate for an automatic crash reporting feature within 3D Slicer and its extensions, this one of course, contingent on explicit user consent.</p>
<p>If an extension would collect outcome-related data (quality of airway sementation such as numbers of branches generated, resolution of CT used, time used for AI analysis, CPU or GPU used for AI etc) there should be a clear Opt-IN for that kind of data transfer.</p>

---

## Post #7 by @lassoan (2023-07-31 15:58 UTC)

<p>Any kind of non-networking task (e.g., starting a segmentation task) initiating network communication without explicit user approval could be interpreted by some users as spying. Users that are sensitive about tracking their activities install firewalls that immediately notify them about all network requests and they are upset if they find out that a software attempted to send information without consent, may start a smear campaign, etc. that we should all absolutely avoid. I think allowing sending network request without explicit approval of network communication could be acceptable only for operations of that the main goal is to request information from a server (e.g., update check).</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> as far as I remember you have been asking about more detailed usage data some time ago. Could you comment about this discussion and describe your needs?</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> do you have anything to add?</p>

---

## Post #8 by @pieper (2023-07-31 18:39 UTC)

<p>I’m very curious to hear from Slicer users, particularly those with privacy concerns, about their levels of concern for various options that have been discussed here.</p>
<p>For example, is opt-in required or could we have a default setting to collect and share anonymous data as long as the user is notified at least on the first use?  Do you want to be able to inspect the data that is being sent to our servers?</p>
<p>I also think it’s important to keep in mind that Slicer is a community project and we benefit most from those community members who share the most, be it through code, forum posts, or spreading the word to their colleagues.  Without dismissing the concerns of those who prefer to remain private, I think it’s fair to prioritize the needs and opinions of those who are active in improving the community.  From this point of view I favor collecting and sharing user data that will benefit developers in making Slicer better.</p>

---

## Post #9 by @fedorov (2023-07-31 20:58 UTC)

<p>For the sake of transparency and accountability, I would suggest that every extension should clearly declare to the user whether any information is collected, and this declaration should be available in the extension UI, and populated in the extension template.</p>
<p>Since the resources available for the review of extensions will always be limited, similar to license considerations, users will have to rely on the declarations made by the extension developers. While it is ok to communicate license details in the code repository, an equivalent to the privacy statement should be readily available to the non-developer users. Whether opt-in is implemented or not could be the choice of the developer and may depend on various considerations. But it should be the choice of the user to use the extension or not given the privacy statement declaration.</p>
<p>I think it is potentially a dangerous situation at the moment, where (as it appears from the discussion above), some extensions already are collecting and communicating certain usage information without users necessarily being aware of this.</p>

---

## Post #10 by @rbumm (2023-08-01 05:56 UTC)

<p>Good suggestion <a class="mention" href="/u/fedorov">@fedorov</a>, it is implemented in the help text of the LungCTAnalyzer now.</p>

---

## Post #11 by @jcfr (2023-08-01 15:24 UTC)

<p>Related resources we found while <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a>, <a class="mention" href="/u/lassoan">@lassoan</a> and I were discussing during the weekly meeting:</p>
<ul>
<li><a href="https://community.kde.org/Policies/Telemetry_Policy" class="inline-onebox">Policies/Telemetry Policy - KDE Community Wiki</a></li>
</ul>

---

## Post #12 by @lassoan (2023-08-02 04:22 UTC)

<p>We also talked a bit about possible implementations. It seems that adding a <code>Telemetry</code> extension could be a good idea, as this way we could avoid adding any tracking related code to Slicer core, we could make more frequent changes to the telemetry infrastructure, and any extensions that need to track software usage would need to declare that by depending on the Telemetry extension.</p>

---

## Post #13 by @pieper (2023-08-02 21:43 UTC)

<p>I started something like this a few years ago:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pieper/SlicerAnalytics">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pieper/SlicerAnalytics" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/18a4ce47cdd3c2da1d9cab06c759442e31919245059ec8ad4e25da18befbeefd/pieper/SlicerAnalytics" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/pieper/SlicerAnalytics" target="_blank" rel="noopener">GitHub - pieper/SlicerAnalytics: a site and extension for collecting google...</a></h3>

  <p>a site and extension for collecting google analytics about Slicer usage - GitHub - pieper/SlicerAnalytics: a site and extension for collecting google analytics about Slicer usage</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I was using Google Analytics for the back end, but I think now it’s not a good fit.  Still the basic idea could be adapted to a different backend.</p>

---

## Post #14 by @muratmaga (2023-08-02 22:37 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> as far as I remember you have been asking about more detailed usage data some time ago. Could you comment about this discussion and describe your needs?</p>
</blockquote>
</aside>
<p>We do have not very specific needs. As a grant funded project, it would be nice to have some kind of an independent way of assessing the user counts/activity beyond raw extension download stats, that’s the primary motivation. I think our usage would be like what modules were activated, for how long etc… We already have a sense of this through user interactions and workshops, but would be nice to get a bit more quantitative.</p>
<p>As for how to handle this, I have mixed feeling about a separate telemetry extension. As a user, I wouldnt go into the hassle of installing yet another extension to allow the devs to collect data (just seems too cumbersome). I would be OK with a very explicit message at the end of the installation process that asks my permission to do background telemetry about usage (with the default setting set to not to collect), and even provide a link to the github repo for that section of the code for the inquisitive ones to review, as well as info about what info being collected.</p>
<p>The issue, as it has been pointed out, institutions like where I work, which has very tight internet security policies. The key I think as i said, is to make this very explicit (and opt-in by actively selecting an option), and directly pointing out to the code of telemetry (for people to review, if they want to).</p>

---

## Post #15 by @jamesobutler (2023-08-03 02:01 UTC)

<p>Also a heads up that maintainers of Slicer extensions such as SlicerTotalSegmentor will need to be aware of associated python packages (TotalSegmentor) that contain telemetry where it is ON by default. SlicerTotalSegmentor currently uses TotalSegmentor v1.5.3, but starting in v1.5.4 there is telemetry.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/wasserth/TotalSegmentator/tree/87560f329b3bd97543f975ebd47ba269933f43ee#other">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/wasserth/TotalSegmentator/tree/87560f329b3bd97543f975ebd47ba269933f43ee#other" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/wasserth/TotalSegmentator/tree/87560f329b3bd97543f975ebd47ba269933f43ee#other" target="_blank" rel="noopener nofollow ugc">GitHub - wasserth/TotalSegmentator at 87560f329b3bd97543f975ebd47ba269933f43ee - Other</a></h3>

  <p><a href="https://github.com/wasserth/TotalSegmentator/tree/87560f329b3bd97543f975ebd47ba269933f43ee#other" target="_blank" rel="noopener nofollow ugc">87560f329b3bd97543f975ebd47ba269933f43ee</a></p>

  <p><span class="label1">Tool for robust segmentation of 104 important anatomical structures in CT images</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #16 by @lassoan (2023-08-03 03:29 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="14" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>As a user, I wouldnt go into the hassle of installing yet another extension to allow the devs to collect data</p>
</blockquote>
</aside>
<p>By default, extension dependencies are installed automatically, so users would not need to do anything extra.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="15" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>SlicerTotalSegmentor currently uses TotalSegmentor v1.5.3, but starting in v1.5.4 there is telemetry.</p>
</blockquote>
</aside>
<p>This is very useful information. TotalSegmentator offers huge value, so asking a little favor in return could be fair. However, phoning home without user consent violates <a href="https://community.kde.org/Policies/Telemetry_Policy#Control">Control rule</a> of KDE.</p>
<p>Maybe a solution could be to add a global telemetry kill switch to the Slicer application, which would apply the setting to all extensions and external dependencies that otherwise would not behave properly (e.g., would do silent opt-in by default). This would address the issue with both TotalSegmentator and LungCTAnalyzer.</p>

---

## Post #17 by @cpinter (2023-08-09 11:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="16" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>By default, extension dependencies are installed automatically, so users would not need to do anything extra.</p>
</blockquote>
</aside>
<p>I like the idea of the Telemetry extension, and I think it’s a good approach that the extensions collecting such data must depend on it. But if the user does not install any such extension, Telemetry would not be collected for Slicer core either, until the user installs the Telemetry extension manually. My feeling is that this way almost no usage information would be collected about Slicer core (&lt;1% of the users would have this enabled, unless a very popular extension depends on it).</p>
<p>Have you discussed this use case at the dev meeting, when the user only uses Slicer core or only extensions that do not collect usage data? For example a popup on first start offering to install the Telemetry extension (which could be an annoyance)…</p>

---

## Post #18 by @lassoan (2023-08-09 12:25 UTC)

<p>I agree, for collecting usage data about Slicer core, the user would need to opt in in the installer or in the welcome dialog and this would need to be in Slicer core. If user consented then Slicer would install the telemetry extension.</p>
<p>It would be nice if even the question about telemetry was implemented outside Slicer core, but I don’t think it is possible. We can put telemetry configuration into a separate module and include it in the build depending on some CMake flag.</p>

---

## Post #19 by @pieper (2023-08-10 14:18 UTC)

<p>Since we know that many people will opt out of tracking and telemetry, why don’t we try to make sharing of usage information fun and easy for people who do want to share?</p>
<p>I’m thinking we could track usage locally and generate badges for users that pass a certain number of hours of usage, or try certain modules or extensions.  Then we could offer a button to post these achievements on social media or discourse where we would get statistics automatically.  This could also be a place where people could opt-in to automatically posting their progress.</p>
<p>Badges could be for things we want to collect usage information on like “Loaded 10 dicom studies”, “Loaded 1000 dicom studies”, “Saved and reloaded an MRB scene file”, “Installed an extension”, “Used the Python console”, etc.  Even seeing the list of potential badges might encourage people to explore features they didn’t know about.  This approach would be very transparent and might encourage community building.</p>

---

## Post #20 by @mau_igna_06 (2023-08-10 14:46 UTC)

<p>I would suggest we make a quick and very simple implementation.</p>
<p>We could infer the <em>opt-out number of users</em> from the number of downloads of Slicer and the number of users that sent telemetry data on a given day (e.g. the only collected variable could be the boolean <em>opted-in</em>).</p>
<p>After we do that, then we may take other long-term telemetry design decisions. Or do other small experiments.</p>
<p>Hope this opinion is favorable for the discussion</p>

---

## Post #21 by @mau_igna_06 (2023-08-15 19:31 UTC)

<p>Without the ability to collect user metrics from Slicer that would let me gain knowledge about the user base or gather use-cases data to try to seek funding in the future, I’ve chosen to stop developing <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner" rel="noopener nofollow ugc">BoneReconstructionPlanner</a> (apart from addressing bugs).</p>
<p>Therefore, I’ll be using my next weekends with free-time to make an Slicer analytics (i.e. telemetry) extension.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> suggested to learn from:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pieper/SlicerAnalytics">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pieper/SlicerAnalytics" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/18a4ce47cdd3c2da1d9cab06c759442e31919245059ec8ad4e25da18befbeefd/pieper/SlicerAnalytics" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/pieper/SlicerAnalytics" target="_blank" rel="noopener nofollow ugc">GitHub - pieper/SlicerAnalytics: a site and extension for collecting google...</a></h3>

  <p>a site and extension for collecting google analytics about Slicer usage - GitHub - pieper/SlicerAnalytics: a site and extension for collecting google analytics about Slicer usage</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>And to try to implement with GoatCounter:<br>
<a href="https://www.goatcounter.com/" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.goatcounter.com/</a></p>
<p>I’ll post about my advances here</p>
<p>Mauro</p>

---

## Post #22 by @lassoan (2023-08-16 14:06 UTC)

<p>Thanks for the information and considering working on analytics features. The highest priority is to implement the ability to opt in to telemetry. We cannot have extensions collecting data without explicit user consent.</p>
<p>The opt in could be obtained by displaying a widget in the Welcome dialog (and also make it possible to change the choice later in the application settings, and maybe also allow an extension to make a consent dialog appear). The widget could contain some text that explains why enabling telemetry is important and display some options (probably we could start with a single checkbox to globally enable/disable telemetry, but later there may be more refined options). Since the widget could appear at different places, it would be nice to implement it as a reusable widget (similarly to the qSlicerSettingsUserInformationPanel).</p>
<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> if you want to have telemetry in your module then please work on this consent dialog first. If you are unsure about the implementation then you can start with drafting a text that explain the user why he should consent.</p>

---

## Post #23 by @lassoan (2023-08-20 05:48 UTC)

<p>3 posts were split to a new topic: <a href="/t/using-mailing-list-for-communicating-with-users/31245">Using mailing list for communicating with users</a></p>

---

## Post #24 by @jcfr (2023-10-05 04:16 UTC)

<h3><a name="p-101388-example-renderdoc-tool-1" class="anchor" href="#p-101388-example-renderdoc-tool-1" aria-label="Heading link"></a>Example: <code>renderdoc</code> tool</h3>
<p>After installing <code>renderdoc</code>, I was presented with the following popup:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e031b4d9d07882c3b7902d68ebb5b3f56cf3cb0.png" data-download-href="/uploads/short-url/fHdb1akeYNH8xtHYLaBktHTvmFi.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e031b4d9d07882c3b7902d68ebb5b3f56cf3cb0_2_517x288.png" alt="image" data-base62-sha1="fHdb1akeYNH8xtHYLaBktHTvmFi" width="517" height="288" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e031b4d9d07882c3b7902d68ebb5b3f56cf3cb0_2_517x288.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e031b4d9d07882c3b7902d68ebb5b3f56cf3cb0_2_775x432.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e031b4d9d07882c3b7902d68ebb5b3f56cf3cb0_2_1034x576.png 2x" data-dominant-color="CBCBCB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1749×978 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The analytics infrastructure description along with the collected data are also publicly reported on the associated <a href="https://renderdoc.org/analytics">analytics page</a>.</p>
<p>References:</p>
<ul>
<li><a href="https://github.com/baldurk/renderdoc">https://github.com/baldurk/renderdoc</a></li>
<li><a href="https://renderdoc.org/analytics">https://renderdoc.org/analytics</a></li>
<li><a href="https://renderdoc.org/analytics/trends">https://renderdoc.org/analytics/trends</a></li>
</ul>

---

## Post #25 by @mau_igna_06 (2023-10-05 19:58 UTC)

<p>Nice example <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>Thanks for sharing</p>
<p>Although I’m not so sure users would go through such a verbose dialog (maybe add <em>href</em>s instead?)</p>
<p>I don’t know what others think <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #26 by @mau_igna_06 (2023-10-24 21:42 UTC)

<p>Hi</p>
<p>I was able to do a “Hello World” example:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/mauigna06/SlicerGoatCounter/tree/main#readme">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/mauigna06/SlicerGoatCounter/tree/main#readme" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/mauigna06/SlicerGoatCounter/tree/main#readme" target="_blank" rel="noopener nofollow ugc">GitHub - mauigna06/SlicerGoatCounter</a></h3>

  <p><a href="https://github.com/mauigna06/SlicerGoatCounter/tree/main#readme" target="_blank" rel="noopener nofollow ugc">main</a></p>

  <p><span class="label1">Contribute to mauigna06/SlicerGoatCounter development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Feedback is welcomed</p>

---

## Post #27 by @lassoan (2023-10-26 19:04 UTC)

<p>GoatCounter looks like a nice project, but I would prefer something more established and longer-term solution, such as an <a href="https://opentelemetry.io/">OpenTelemetry</a> server hosted by Kitware. Probably something simpler would be sufficient, too, but it should be open-source, using open standards, and preferably with an option of either self-hosting or inexpensive hosting.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Does Kitware use (or plan to use) telemetry for its projects?</p>

---

## Post #28 by @mau_igna_06 (2023-11-02 21:53 UTC)

<h1><a name="p-102757-with-the-help-of-chatgpt-gpt-35-1" class="anchor" href="#p-102757-with-the-help-of-chatgpt-gpt-35-1" aria-label="Heading link"></a>With the help of ChatGPT (GPT-3.5)</h1>
<pre><code class="lang-auto">My humble prompting trial
</code></pre>
<p><em>What’s a dark pattern? What’s a deceptive pattern?</em></p>
<blockquote>
<p>Dark patterns and deceptive patterns are both terms used to describe unethical or manipulative practices used in user interface design and online marketing to trick or deceive users into taking actions they might not want to take. These practices are designed to benefit the business or website at the expense of the user’s best interests. While they may be effective in the short term, they can harm the user experience and damage a company’s reputation in the long run.</p>
<pre><code>Dark Patterns:
Dark patterns refer to user interface design choices that intentionally mislead or deceive users. These patterns are typically used to trick users into making decisions or taking actions that they might not otherwise choose if they had full and clear information. Dark patterns can take various forms, including:
    Misdirection: Steering users towards a particular action by making it more prominent or attractive while downplaying other options.
    Hidden Costs: Concealing additional charges or fees until late in the transaction process.
    Forced Continuity: Making it difficult for users to cancel subscriptions or memberships.
    Trick Questions: Using confusing language or design to manipulate user choices.
    Urgency and Scarcity: Creating a false sense of urgency or scarcity to pressure users into taking immediate action.

Deceptive Patterns:
Deceptive patterns refer to a broader range of practices that go beyond just user interface design and include any deceptive tactics or strategies employed by a company or marketer to manipulate or mislead consumers. This can include not only design elements but also misleading advertisements, false claims, or any practice that involves dishonesty. Deceptive patterns can take many forms, such as:
    False Advertising: Making false or misleading claims about a product or service.
    Bait-and-Switch: Advertising one product but substituting it with a different, often lower-quality, product.
    Phishing: Attempting to trick users into revealing personal information by posing as a legitimate entity.
    Fake Reviews: Posting fabricated positive reviews to artificially boost a product's reputation.
    Disguised Ads: Making advertisements look like regular content to deceive users.
</code></pre>
<p>Both dark and deceptive patterns are considered unethical and can damage a company’s reputation when discovered. Many countries have laws and regulations in place to protect consumers from such practices, and companies that engage in these behaviors may face legal consequences or fines. Ethical design and transparent marketing practices are generally recommended to build trust and maintain a positive relationship with customers.</p>
</blockquote>
<p><em>What’s Slicer biomedical research software?</em></p>
<blockquote>
<p>3D Slicer is not specific to biomedical research but is widely used in the field due to its versatility and capabilities. It’s an open-source software platform used for medical image analysis, visualization, and 3D image reconstruction. Biomedical researchers, clinicians, and engineers often use 3D Slicer for a variety of tasks, including but not limited to:</p>
<ol>
<li><strong>Medical Imaging Research:</strong> Researchers can use 3D Slicer to process and analyze medical images from various modalities such as MRI, CT, ultrasound, and more. It allows for segmentation (identifying and outlining specific structures or regions of interest), registration (aligning images from different scans or time points), and advanced visualization.</li>
<li><strong>Surgical Planning:</strong> Surgeons use 3D Slicer to plan and simulate procedures. They can visualize patient-specific anatomical structures in 3D, helping them make more informed decisions before surgeries.</li>
<li><strong>Image-Guided Interventions:</strong> 3D Slicer supports real-time navigation during medical procedures. It can register preoperative images with the patient’s current anatomy, aiding in guidance and precision during surgeries.</li>
<li><strong>Radiomics and Radiogenomics:</strong> Researchers use 3D Slicer to extract quantitative features from medical images, allowing for the analysis of large datasets to identify correlations between image-based metrics and clinical outcomes.</li>
<li><strong>Diffusion Imaging:</strong> It’s widely used in the analysis of diffusion-weighted imaging (DWI) and diffusion tensor imaging (DTI) data, which can provide insights into the microstructure of tissues in the brain and other organs.</li>
<li><strong>Custom Module Development:</strong> 3D Slicer is highly extensible, and researchers can create custom modules and extensions to tailor it to their specific research needs.</li>
<li><strong>Education and Training:</strong> It’s used in medical education and training, providing a platform for students and professionals to learn and practice medical image analysis and 3D visualization.</li>
</ol>
<p>3D Slicer is a powerful and flexible tool, and its open-source nature means that it has a large and active user community, which contributes to its development and supports its use in various applications, including biomedical research. It is often used in conjunction with other software and tools to enable a wide range of medical image analysis and research applications.</p>
</blockquote>
<p><em>Write a non dark-pattern, non deceptive-pattern telemetry collection statement for 3D Slicer</em></p>
<blockquote>
<p>Certainly, here’s a straightforward and transparent telemetry collection statement for 3D Slicer:</p>
<p>"At 3D Slicer, we are committed to improving our software and providing a better user experience. To achieve this, we collect limited telemetry data to help us understand how our software is being used and identify areas for enhancement. We value your privacy and are dedicated to being transparent about our data collection practices.</p>
<p><strong>What data is collected:</strong></p>
<ul>
<li>Usage statistics: We collect information about the features and tools used within 3D Slicer, helping us understand which functionalities are most valuable to our users.</li>
<li>Error reports: In the event of a software error or crash, we may collect diagnostic information to diagnose and address issues more effectively.</li>
<li>Basic system information: We may gather data about the operating system and hardware configuration to optimize compatibility and performance.</li>
</ul>
<p><strong>How we use the data:</strong> The collected data is exclusively used for improving 3D Slicer. It helps us identify and prioritize software enhancements, address technical issues promptly, and enhance the user experience.</p>
<p><strong>Data Protection:</strong> Your privacy is important to us. The data we collect is anonymized and aggregated to ensure that it cannot be used to identify individual users. We do not collect any personal or sensitive information.</p>
<p><strong>Opting out:</strong> Participation in telemetry data collection is entirely optional. You can easily opt out of telemetry data sharing during the installation process or within the software’s settings.</p>
<p>We are dedicated to maintaining transparency and respecting your privacy. Your feedback and usage data play a crucial role in our efforts to make 3D Slicer a more valuable tool for the biomedical research community. Thank you for your support."</p>
<p>This telemetry collection statement is designed to inform users about the purpose of data collection, how it’s used, and how they can opt out if they wish, without resorting to dark patterns or deceptive practices.</p>
</blockquote>
<hr>
<p>As discussed on <a href="https://discourse.slicer.org/t/2023-10-31-weekly-meeting/32496" class="inline-onebox">2023.10.31 Weekly Meeting</a>, a <em>telemetry collection statement</em> is proposed.</p>
<p>What do you think? <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>NOTE: <a href="https://github.com/baldurk/renderdoc/blob/aec25cfcaa9f608f47ace166459e0916d51b740d/qrenderdoc/Code/Interface/Analytics.cpp#L588-L604" rel="noopener nofollow ugc">This OSS example of implementation</a> was also mentioned on that meeting.</p>

---

## Post #29 by @pieper (2023-11-02 22:06 UTC)

<p>That’s actually pretty good. I’d take out the part about error reports though.  I don’t want to collect those automatically since there’s a good chance they would have PII (personally identifying information) or even PHI (protected health information).  Better if people only share those when they are sure they are safe.</p>

---

## Post #30 by @mikebind (2023-11-02 22:16 UTC)

<p>That seems like a good start.  I agree with <a class="mention" href="/u/pieper">@pieper</a> that the error reports part should be dropped. In addition, I think the sentence “The collected data is exclusively used for improving 3D Slicer” should be thought about carefully. Might this data also be used to try to obtain funding, for example?</p>
<p>More generally, once the exact mechanism and scope of data collection is decided on, I think it would be better to include some more specifics. For example, perhaps the module names and number of times opened is being collected? If the variety is too great to include in a short statement of consent, there should be a link to a page which goes in depth about what is collected and how.</p>

---

## Post #31 by @lassoan (2023-11-02 23:52 UTC)

<p>I agree that the Chatgpt output is pretty good, but I would rather use a large open-source software organization’s policy as a basis. For example, the KDE telemetry policy is quite good. I could accept it for Slicer as is:</p>
<p><a href="https://community.kde.org/Policies/Telemetry_Policy" class="onebox" target="_blank" rel="noopener">https://community.kde.org/Policies/Telemetry_Policy</a></p>

---

## Post #32 by @mau_igna_06 (2023-11-15 12:33 UTC)

<p>Just to have in mind, this appears in Qt installation:</p>
<blockquote>
<p>telemetry-question : Contribute to Qt Development : Help us improve Qt and Qt Creator by allowing tracking of pseudonymous usage data in Qt Creator. The tracking can be disabled at any time. Read the Qt Company data collection privacy statement <a href="https://www.qt.io/terms-conditions/#privacy" class="inline-onebox" rel="noopener nofollow ugc">Legal | Terms &amp; Conditions - Qt</a>. Yes|No</p>
</blockquote>

---

## Post #33 by @mau_igna_06 (2023-11-20 19:29 UTC)

<p>Hi Rudolf,</p>
<p>Have you gotten any other insights on past months?</p>
<p>What have been the most direct benefits of setting up those counters?</p>

---

## Post #34 by @rbumm (2023-11-20 19:56 UTC)

<p>First of all, it is interesting and motivating how many runs (&gt;23000 since May 2023, 88371 uses per month, 3156 per week and 450 per day) were done.</p>
<p>People almost double use the segmenter over the analyzer.<br>
I can see that most people use AI techniques for the lungs now and that TotalSegmentator use is not as prominent as I thought, maybe because lungmask is faster and less complicated to install (inbuild).<br>
Few people use airway seg and vessel segmentation, probably because it is just not good enough yet or not needed in their studies. All in all interesting information for development. So here is room for development. I stored IP in the very beginning but now the counting is IP-less. Still, I could make IP-less segmentation statistics over weeks, months, and years.starting in September 2023. There was not one complaint concerning the counters yet. But they are really non-personal technical counters.</p>

---

## Post #35 by @cpinter (2023-11-22 11:18 UTC)

<p>Would it make sense to hash the IPs and store only the hashes to see how many runs were from the same user? Then there would be no personal information stored but the benefit preserved.</p>

---

## Post #36 by @lassoan (2023-11-22 12:43 UTC)

<p>Such fingerprinting of users based on IP (and potentially based on additional parameters of the computer) requires prior consent and probably other mechanisms as well (allow users to view/erase data that is maintained about them?). I would feel more comfortable adopting telemetry policy (and perhaps tooling) from a large, well-established project (e.g., the KDE) than handcrafting our own.</p>

---

## Post #37 by @mau_igna_06 (2023-11-22 13:16 UTC)

<p>Rudolf, could you get an average of number of uses per download using the <a href="https://slicer-packages.kitware.com/api/v1/app/5f4474d0e1d8c75dfc705482/downloadstats" rel="noopener nofollow ugc">download stats</a>?</p>

---

## Post #38 by @rbumm (2023-11-22 15:53 UTC)

<p>This link does not work in my chrome - but I have no individual user indications that could indicate the number of program runs per download … sry</p>

---

## Post #39 by @mau_igna_06 (2023-11-22 16:58 UTC)

<p>It’s a JSON file that may have a size of 500MB since it has a long history of Slicer versions and Slicer extension download count, that maybe the reason it appears to not render anything</p>
<p>Otherwise you could install <a href="https://extensions.slicer.org/view/DeveloperToolsForExtensions/31382/win" rel="noopener nofollow ugc">DeveloperToolsForExtensions</a> on latest Slicer Stable release and check “Extension Download Statistics” module, write “LungCTAnalyzer” and click “Get download statistics”.</p>
<p>With those numbers you can sum the total number of installs of your extension, and the total extension use cases (or of a particular feature). Then divide the latter by the former and you get a “use cases per extension download” number</p>
<p>I would do it if I had the data myself, hope this is interesting for you as well</p>

---

## Post #40 by @jcfr (2023-11-30 17:32 UTC)

<blockquote>
<p>re: Visual Studio</p>
</blockquote>
<p>An here is what is displayed in the context of the NVIDIA Nsight / Visual Studio integration:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0667151c2242eb66479c7c1126f444965a96d4d.png" alt="image" data-base62-sha1="tJANmHa61X1kdyeeBKa43iai8zz" width="476" height="309"></p>

---

## Post #41 by @mau_igna_06 (2024-01-05 10:32 UTC)

<blockquote>
<p>re: VLC</p>
</blockquote>
<p>Here is what appears while opening VLC for the first time:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b6d83bc8ea3a20165859c4405d082fa236a747f.png" alt="image" data-base62-sha1="6cbaeUnn3nDxLSxKE9p5MnVIbv1" width="468" height="446"></p>

---

## Post #42 by @BerDom.Ing (2024-02-26 22:20 UTC)

<p>I’ve been working on the redaction of the pop-up where the user can agree to opt in. I think it needs to be clear and easy to understand. The following text is the draft:</p>
<p>Short version:</p>
<p>Opt-in for anonymous data collection in Slicer software. We collect non-personal data on usage frequency, hours, and UI button interactions to improve the user experience. Your privacy is protected; no personal data is collected or transmitted over the network. Select your preference below:</p>
<p>(•) Do not collect any data.<br>
( ) Allow anonymous data collection.</p>
<p>[Accept]</p>
<p>Long Version:</p>
<p>Dear Slicer User,</p>
<p>At Slicer, we strive to enhance your experience and improve our software continually. To achieve this, we rely on anonymous software usage data to understand how you interact with our platform and where we can focus our efforts effectively.</p>
<p>The data we collect is strictly limited to non-personal information, ensuring your privacy and confidentiality are paramount. We do not gather any data that could identify you personally, nor do we track your individual installations.</p>
<p><strong>What Data is Collected?</strong></p>
<ol>
<li><strong>Number of Runs:</strong> We collect data on the frequency of software usage to gauge overall engagement.</li>
<li><strong>Usage Hours:</strong> Understanding the duration of your sessions helps us optimize performance and usability.</li>
<li><strong>UI Button Interactions:</strong> Data regarding the usage of UI buttons provides insights into feature popularity and usability.</li>
</ol>
<p>Rest assured, all collected data remains anonymized and is stored locally on your device. No information is transmitted over the network without your explicit consent.</p>
<p>To review the implementation details of our data collection process, please refer to the code available here.</p>
<p>Please select your preference below:</p>
<p>(•) Do not collect any data.<br>
( ) Allow anonymous data collection.</p>
<p>[Accept]</p>
<p>Thank you for helping us improve Slicer!</p>

---

## Post #43 by @pieper (2024-02-27 20:08 UTC)

<p>I like the short wording.  In addition to designing this dialog, it would be great if you could also make a mock up of the usage data display.  How we present the data we’ve collected will be important for convincing people that it’s okay for them to share it.</p>

---

## Post #44 by @lassoan (2024-02-28 04:33 UTC)

<p><a class="mention" href="/u/berdom.ing">@BerDom.Ing</a> missed the most important part: he will work on this topic for a few months (as part of fulfilling requirements for his degree).</p>
<p>I like the short version, too. It is somewhat repetitive (“anonymous data collection”, “collect non-personal data”, “no personal data is collected”, “allow anonymous data collection”), so we could simplify things a bit.</p>
<p>We also need to agree on what data we would like to collect.</p>
<p><a class="mention" href="/u/berdom.ing">@BerDom.Ing</a> could you clarify a bit what you mean?</p>
<ul>
<li>Number of runs: How many times Slicer is started? How many times the user switched to a module? Or how many times some feature of a module was used? Or all these?</li>
<li>Usage hours: Time elapsed between starting and stopping Slicer? Time elapsed between entering and exiting a module? Should we extract idle time (when the user does not interact with Slicer)? The <a href="https://github.com/PerkLab/SlicerSandbox/tree/master/UserStatistics">User Statistics module in Sandbox</a> determines idle time and collects timing data - so it could be useful if we want to exclude idle time.</li>
<li>UI button interactions: Most things are UI button interactions. Could you clarify?</li>
</ul>
<p><strong>Question for everyone:</strong> What other information should we consider collecting? (any ideas are welcome and we can sort them out later)</p>
<p>I’m thinking about potentially collecting information about the computer (operating system, available memory, CPU model, GPU, screen resolution) and data (image modality, size), as these information could be useful when we make design decisions.</p>
<p>For reference, telemetry in other software:</p>
<ul>
<li><a href="https://support.mozilla.org/en-US/kb/telemetry-clientid">Firefox</a></li>
<li><a href="https://www.videolan.org/privacy.html">VLC</a></li>
<li><a href="https://community.kde.org/Telemetry_Use">KDE</a></li>
<li><a href="https://linuxiac.com/gnome-info-collect-telemetry-data-collection-tool/">GNOME</a> - includes telemetry variables and explanation why they are collected</li>
<li><a href="https://musescore.org/en/telemetry">MuseScore</a></li>
<li><a href="https://discussion.fedoraproject.org/t/f40-change-request-privacy-preserving-telemetry-for-fedora-workstation-system-wide/85320/322">Fedora workstation</a></li>
<li>The <a href="https://hackaday.com/2021/05/17/telemetry-debate-rocks-audacity-community-in-open-source-dustup/">Audacity scandal</a></li>
</ul>

---

## Post #45 by @BerDom.Ing (2024-03-19 13:44 UTC)

<p>After reading about the Audacity scandal, I realized it’s crucial to opt-in for data collection and ensure anonymity. Also, allowing time for the community to embrace the new system, rather than feeling it’s imposed upon them, is essential. We should consider conducting a survey among Slicer users to gauge their concerns about telemetry usage, explain procedures, and emphasize not rushing the technology. Empowering users, providing a dedicated folder for collected data, and a link to the telemetry code repository could help. I’ve noticed that users express concerns about software safety when telemetry implementation is discussed.</p>
<aside class="quote no-group" data-username="lassoan" data-post="44" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/berdom.ing">@BerDom.Ing</a> could you clarify a bit what you mean?</p>
</blockquote>
</aside>
<p>Number of runs: Tracking how many times Slicer is started. I believe it would also be beneficial to count how often users switch modules, although implementing this might require some time and a deep understanding of Slicer’s source code.</p>
<p>Usage hours: Measuring the time elapsed between starting and stopping Slicer.</p>
<p>I aim to implement the User Statistics module mentioned earlier. Line 25 of the module’s description reads: “This module measures user statistics and stores them in a table. Some of the statistics measured include the active module, active segment editor effect, selected segment, duration, application status (active, wait, idle), etc. Tables from different scenes can be merged into a single table.”</p>
<p>UI button interactions: Each interaction should trigger an event handler. It might be feasible to increase a counter in a table for each invoked event of this type, providing insights into UI redesign or creating shortcuts for frequently used interactions.</p>
<p>I agree that collecting information about the user’s computer could prove valuable.</p>

---

## Post #46 by @BerDom.Ing (2024-03-26 15:27 UTC)

<p>I’ve been working on finishing the Slicer extension tutorial, but I keep encountering errors. I think implementing computer information collection into the module will be the first step. I’ll try to accomplish this using only Qt and VTK to avoid installing extra libraries. I’ve researched that Qt provides a class called ‘QOpenGLContext,’ which can create an OpenGL context, and VTK provides a class called ‘vtkOpenGLRenderWindow,’ which can create a window with an OpenGL context. This can be used to retrieve graphics card information.</p>

---

## Post #47 by @lassoan (2024-03-26 16:14 UTC)

<p><a class="mention" href="/u/berdom.ing">@BerDom.Ing</a> would it be possible for you to attend the weekly Slicer developer meetings?<br>
At each meeting you could give an update in a few minutes and we could discuss any questions that may arise.</p>

---

## Post #48 by @BerDom.Ing (2024-03-26 17:41 UTC)

<p>Of course, I’ll be glad to join the meetings.</p>

---

## Post #49 by @BerDom.Ing (2024-04-09 16:14 UTC)

<p>Today, in the weekly Slicer meeting, we discussed what to use for creating mock-ups, collecting error events, using JSON to store the data, and creating schemas for user-stored data. I believe it will be easy to migrate from JSON to an SQL schema.</p>

---

## Post #50 by @lassoan (2024-04-09 16:29 UTC)

<p>Thanks for the summary. Could you please describe the full list of values that were considered for collection?</p>

---

## Post #51 by @BerDom.Ing (2024-04-09 16:44 UTC)

<p>The values I considered are as follows:</p>
<p>Number of Slicer runs: numberOfSlicerRuns<br>
Times a module is loaded: moduleName + number of load times<br>
GPU Information<br>
CPU Information<br>
Operating System<br>
Window Resolution: width X height<br>
Idle elapsed time in hours: idleTime<br>
Active elapsed time in hours: activeTime</p>

---

## Post #52 by @muratmaga (2024-04-09 16:53 UTC)

<p>If you are collecting the display information, maybe consider collecting “display scaling” parameters. I occasionally (and almost never consistently) find some strange case of text scaling issues…</p>

---

## Post #53 by @BerDom.Ing (2024-04-09 16:58 UTC)

<p>I’ll add the scaling information to the collected values now that I know it might cause some issues.</p>

---

## Post #54 by @lassoan (2024-04-09 18:28 UTC)

<blockquote>
<p>Number of Slicer runs</p>
</blockquote>
<p>It is not clear what a “run” means. We need to define it. For example, Slicer starts and runs for longer than 1 minute.</p>
<blockquote>
<p>Times a module is loaded</p>
</blockquote>
<p>All modules are loaded when Slicer starts, so I guess you mean number of times a module is activated (each time the user switches to that module). This would be very low-level information and since module names may give away information (especially when the modules are not publicly released), we should carefully consider if we really want to do collect such information. Maybe modules could opt in to be logged.</p>
<blockquote>
<p>GPU Information<br>
CPU Information<br>
Operating System</p>
</blockquote>
<p>Need to specify enumerated values, because strings may identify some rare configurations. Make sure that available memory is included.</p>
<blockquote>
<p>Window Resolution: width X height</p>
</blockquote>
<p>Need to specify bins to make sure we don’t make systems identifiable that use rare resolutions. Also add scaling as Murat suggested.</p>
<p>We probably don’t need resolution of all screens, just the one where the Slicer main window is displayed on and the total number of screens.</p>
<blockquote>
<p>Idle elapsed time in hours: idleTime</p>
</blockquote>
<p>I’m not sure if this is relevant. Why do we need to know if people leave their Slicer running on their computer?</p>
<blockquote>
<p>Active elapsed time in hours: activeTime</p>
</blockquote>
<p>What would be the sufficient resolution? 5 minutes? 10 minutes?<br>
We would probably write the usage statistics to disk at this time interval (to make sure the information is captured even if Slicer crashes or terminated).</p>
<hr>
<p>It could be also nice to count number of uncaught C++ exceptions, application crashes.</p>
<p>It would be important that extension developers should be able to specify custom events that they want to count. We should limit the allowed event names to make sure that no information is leaked through that (e.g., the Extensions Catalog Entry json file could contain the list of event names that the extension can count and we would not record or transmit anything else).</p>
<p>We also need to think about recording location of the user with some granularity. We could do this at server level from the IP address, but we would need to make sure that the location does not reveal too much information about a user. For example, it may not be desirable to be able to identify that a certain hospital uses Slicer for planning or guiding certain procedures. It would be nice to know for sure, but would violate the users’ privacy.</p>
<p>Ideally, we should not store IP addresses so that we don’t need to deal with strict data handling regulations. However, then it is not clear how we can detect and mitigate trivial data manipulation attempts.</p>

---

## Post #55 by @BerDom.Ing (2024-04-10 19:14 UTC)

<blockquote>
<p>It is not clear what a “run” means. We need to define it. For example, Slicer starts and runs for longer than 1 minute.</p>
</blockquote>
<p>I was going to define run as each time the application is opened, but now I consider that your approach is better. We should start counting when slicer runs for more than 1 minute so we know that it wasn’t opened on error, or simultaneous windows by clicking the icon so many times.</p>
<blockquote>
<p>All modules are loaded when Slicer starts, so I guess you mean number of times a module is activated (each time the user switches to that module). This would be very low-level information and since module names may give away information (especially when the modules are not publicly released), we should carefully consider if we really want to do collect such information. Maybe modules could opt in to be logged.</p>
</blockquote>
<p>Yes, I mean times a module is activated, thanks for the correction, i agree that we should be careful collecting information. I find this to be valuable and not too intrusive, but I want to hear more opinions about it.</p>
<blockquote>
<p>Need to specify enumerated values, because strings may identify some rare configurations. Make sure that available memory is included.</p>
</blockquote>
<p>I will specify the GPU,CPU and operating system information once I can retrieve it and test it in a couple of computers so I know what form the information has, and this could differ between different providers and operating systems, I will make sure that the available memory is included.</p>
<blockquote>
<p>Need to specify bins to make sure we don’t make systems identifiable that use rare resolutions. Also add scaling as Murat suggested.</p>
</blockquote>
<p>I’m not sure what you mean with specific bins, a brief explanation could help me. Scaling will be added.</p>
<blockquote>
<p>I’m not sure if this is relevant. Why do we need to know if people leave their Slicer running on their computer?</p>
</blockquote>
<p>Idle time is relevant to know how much time slicer was running in total, idle time in combination of the active time is equal to the total time slicer was running.</p>
<blockquote>
<p>What would be the sufficient resolution? 5 minutes? 10 minutes?<br>
We would probably write the usage statistics to disk at this time interval (to make sure the information is captured even if Slicer crashes or terminated).</p>
</blockquote>
<p>I think that a good resolution to save the active time it’s 10 minutes.</p>
<blockquote>
<p>It could be also nice to count number of uncaught C++ exceptions, application crashes.</p>
</blockquote>
<p>I agree that it would be nice to count uncaught c++ exceptions and application crashes, I will surely need time, help, and guidance.</p>
<blockquote>
<p>We also need to think about recording location of the user with some granularity. We could do this at server level from the IP address, but we would need to make sure that the location does not reveal too much information about a user.</p>
</blockquote>
<p>I agree that we should not store IP addresses, but i think it would be okay to collect the location with a big granularity.</p>
<blockquote>
<p>However, then it is not clear how we can detect and mitigate trivial data manipulation attempts.</p>
</blockquote>
<p>To detect and mitigate trivial data manipulation attempts we could use <a href="https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction" rel="noopener nofollow ugc">Reed–Solomon error correction</a>. This is another value to store, but ensures that the other parts of the message are being transmitted without an error.</p>

---

## Post #56 by @lassoan (2024-04-10 19:31 UTC)

<aside class="quote no-group" data-username="BerDom.Ing" data-post="55" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/berdom.ing/48/69496_2.png" class="avatar"> BerDom.Ing:</div>
<blockquote>
<p>I’m not sure what you mean with specific bins, a brief explanation could help me. Scaling will be added.</p>
</blockquote>
</aside>
<p>Instead of storing any individual resolution (there are many <a href="https://en.wikipedia.org/wiki/List_of_common_resolutions">standard resolutions</a>), you would specify bins, such as:</p>
<ul>
<li>&lt; 960×540</li>
<li>960×540 … 1280×720</li>
<li>1280×720 … 1920x1080</li>
<li>1920x1080 … 2048×1080</li>
<li>…</li>
</ul>
<p>Or maybe you would specify bins for horizontal resolution and aspect ratio.</p>
<aside class="quote no-group" data-username="BerDom.Ing" data-post="55" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/berdom.ing/48/69496_2.png" class="avatar"> BerDom.Ing:</div>
<blockquote>
<p>I will specify the GPU,CPU and operating system information once I can retrieve it and test it in a couple of computers</p>
</blockquote>
</aside>
<p>You can use the same methods that are used for logging system information in the application log at startup.</p>
<aside class="quote no-group" data-username="BerDom.Ing" data-post="55" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/berdom.ing/48/69496_2.png" class="avatar"> BerDom.Ing:</div>
<blockquote>
<p>To detect and mitigate trivial data manipulation attempts we could use <a href="https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction">Reed–Solomon error correction</a>. This is another value to store, but ensures that the other parts of the message are being transmitted without an error.</p>
</blockquote>
</aside>
<p>I’m not worried about data corruption, but that we should not make it extremely easy to manipulate statistics by submitting manipulated content to the server.</p>

---

## Post #57 by @jamesobutler (2024-04-10 22:10 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="54" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This would be very low-level information and since module names may give away information (especially when the modules are not publicly released), we should carefully consider if we really want to do collect such information.</p>
</blockquote>
</aside>
<p>Yes do not collect information of modules being used that are not publicly included in the Slicer extensions index. Developers that create Slicer custom applications for commercial purposes (not open-source) will not want their module names leaked to the Slicer open-source. Developers may be creating new modules against their Slicer custom application, but may also be testing against a regular Slicer version, so application name wouldn’t be a valid way to exclude module name logging.</p>

---

## Post #58 by @BerDom.Ing (2024-04-11 15:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="56" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’m not worried about data corruption, but that we should not make it extremely easy to manipulate statistics by submitting manipulated content to the server.</p>
</blockquote>
</aside>
<p>With the Reed-Solomon algorithm, you obtain a value that correlates with all the previous information in the message. Every time the usage statistics are saved on disk, running the algorithm ensures that all previous parts of the message (the usage statistics) remain unchanged. If a change were to occur, when decoding the Reed-Solomon value against the message, it would indicate that the message has changed. This value could be stored in the same storage as the user statistics and made available to the user if they wish to view it. If users want to manipulate the information on the usage statistics after altering one part of the message, they would need to run the Reed-Solomon algorithm, which would be publicly available. Then, they could save the result in the control value stored with the usage statistics. It’s not bulletproof, but it’s not as trivial as simply changing the number in the available user statistics file.</p>
<aside class="quote no-group" data-username="lassoan" data-post="56" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Instead of storing any individual resolution (there are many <a href="https://en.wikipedia.org/wiki/List_of_common_resolutions" rel="noopener nofollow ugc">standard resolutions</a>)</p>
</blockquote>
</aside>
<p>Thank you for the clarification. Saving only the standard resolutions is indeed the best solution.</p>
<aside class="quote no-group" data-username="lassoan" data-post="56" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can use the same methods that are used for logging system information in the application log at startup.</p>
</blockquote>
</aside>
<p>I will look into that. Thanks for the help.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="57" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Developers that create Slicer custom applications for commercial purposes (not open-source) will not want their module names leaked to the Slicer open-source. Developers may be creating new modules against their Slicer custom application, but may also be testing against a regular Slicer version, so application name wouldn’t be a valid way to exclude module name logging.</p>
</blockquote>
</aside>
<p>Then we should enable modules to opt in to be logged.</p>

---

## Post #59 by @BerDom.Ing (2024-04-14 18:18 UTC)

<p>I’ve been working on the mock-ups for presenting the information to the users. I don’t know what the scaling values are like, so I left them out for now.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5fa66db65dcda15dd560ebd3bf91748922103ad.png" data-download-href="/uploads/short-url/sfoxN5HofVDTFAqKKDBRjExNxi5.png?dl=1" title="Captura de pantalla 2024-04-14 142804" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5fa66db65dcda15dd560ebd3bf91748922103ad_2_580x500.png" alt="Captura de pantalla 2024-04-14 142804" data-base62-sha1="sfoxN5HofVDTFAqKKDBRjExNxi5" width="580" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5fa66db65dcda15dd560ebd3bf91748922103ad_2_580x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5fa66db65dcda15dd560ebd3bf91748922103ad_2_870x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5fa66db65dcda15dd560ebd3bf91748922103ad_2_1160x1000.png 2x" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-04-14 142804</span><span class="informations">1274×1097 41.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02f35877ab8e8a0e0d16e2b40478654d1fa82fa5.png" data-download-href="/uploads/short-url/q6jRK9R0vU8HYKaJQeuc1nZGzr.png?dl=1" title="Captura de pantalla 2024-04-14 145741" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02f35877ab8e8a0e0d16e2b40478654d1fa82fa5_2_690x241.png" alt="Captura de pantalla 2024-04-14 145741" data-base62-sha1="q6jRK9R0vU8HYKaJQeuc1nZGzr" width="690" height="241" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02f35877ab8e8a0e0d16e2b40478654d1fa82fa5_2_690x241.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02f35877ab8e8a0e0d16e2b40478654d1fa82fa5_2_1035x361.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02f35877ab8e8a0e0d16e2b40478654d1fa82fa5.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-04-14 145741</span><span class="informations">1365×477 29.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfabdd17372eabc5eef182216f8b060233cf2102.png" data-download-href="/uploads/short-url/tD93fTTj45fmviT601BIjQPrT2i.png?dl=1" title="Captura de pantalla 2024-04-14 150722" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfabdd17372eabc5eef182216f8b060233cf2102_2_690x269.png" alt="Captura de pantalla 2024-04-14 150722" data-base62-sha1="tD93fTTj45fmviT601BIjQPrT2i" width="690" height="269" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfabdd17372eabc5eef182216f8b060233cf2102_2_690x269.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfabdd17372eabc5eef182216f8b060233cf2102_2_1035x403.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfabdd17372eabc5eef182216f8b060233cf2102.png 2x" data-dominant-color="FCFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-04-14 150722</span><span class="informations">1345×526 15.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #60 by @BerDom.Ing (2024-04-16 15:48 UTC)

<p>In the weekly meeting, regarding the telemetry module, we discussed:</p>
<ul>
<li>
<p>Asking developers more specific questions about the data that needs to be gathered.</p>
</li>
<li>
<p>Exploring methods to prevent the collection of fake data. We cannot use a hash because the code is open source. An anonymization approach could involve replacing IPs with geolocation data (opt-in is needed).</p>
</li>
<li>
<p>Recognizing the potential usefulness of telemetry for compiling a census of the compute hardware used for Slicer.</p>
<p>My upcoming tasks include developing a Python data collector, setting up a server with a database, processing server logs, creating graphics, and implementing an endpoint to confirm successful receipt of data.<br>
I  will need a function in python like slicer.util.getHardwareInformation() that does the same as <a href="https://github.com/Slicer/Slicer/blob/98e542e9c52012157a31d7ff84cd424e05d988f8/Base/QTGUI/qSlicerApplication.cxx#L1084-L1322" rel="noopener nofollow ugc">qSlicerApplication::logApplicationInformation()</a></p>
</li>
</ul>

---

## Post #61 by @lassoan (2024-04-17 03:18 UTC)

<p>There are many things to do, I would recommend to start with setting up a similar system as used for getting Slicer download statistics:</p>
<ul>
<li>Set up an nginx the server (based on Kitware’s recommendation) that returns success (200 OK) and an empty page whenever it receives a valid web request and it logs the request into a file.</li>
<li>You can run a simple flask application to check the validity of the request (similar to <a href="https://github.com/Slicer/slicer_download/tree/main/slicer_download_server">this</a> but much simpler as you don’t need to return any real content)</li>
<li>The request format is something like <a href="https://example.com/telemetry?app=Slicer&amp;app_version=5.6.2&amp;collection_start_date=20240402&amp;collection_end_date=20240415&amp;app_startup=28&amp;module_DICOM_activate=12&amp;module_SampleData_activate=3&amp;extension_LungCTAnalyzer_AISegmentation=18&amp;extension_LungCTAnalyzer_ClassicSegmentation=2">https://example.com/telemetry?app=Slicer&amp;app_version=5.6.2&amp;collection_start_date=20240402&amp;collection_end_date=20240415&amp;app_startup=28&amp;module_DICOM_activate=12&amp;module_SampleData_activate=3&amp;extension_LungCTAnalyzer_AISegmentation=18&amp;extension_LungCTAnalyzer_ClassicSegmentation=2</a></li>
<li>Implement a script (almost the same as <a href="https://github.com/Slicer/slicer_download/tree/main/etc/slicer_parselogs">this</a>) that parses the server logs and saves results into a database and/or json file</li>
<li>Implement web frontend that can display statistics (almost the same as <a href="https://github.com/Slicer/slicer_download_stats">this</a>) - we would want the same kind of filtering based on geography, maybe operating system, display of graph; but instead of download count, we could select any of the events (module_DICOM_activate, module_SampleData_activate, extension_LungCTAnalyzer_AISegmentation, extension_LungCTAnalyzer_ClassicSegmentation, etc.)</li>
</ul>

---

## Post #62 by @BerDom.Ing (2024-04-17 14:13 UTC)

<p>Thanks for your guidance. I’ll be working on it.</p>

---

## Post #63 by @Bob5 (2024-04-18 10:04 UTC)

<p>“Should we start collecting user data?”</p>
<p>My answer is a big NO !</p>
<p>And I have this on offline machine, if it wont work offline its garbage. If it collects data and I have to agree to that - its garbage.</p>
<p>Have a nice day.</p>

---

## Post #64 by @lassoan (2024-04-18 12:10 UTC)

<p>Great, thanks for the feedback! We discuss this topic very openly for complete transparency and to make sure that everyone’s point of view is taken into account.</p>
<p>As you can see from the detailed discussion above, we absolutely don’t want to change Slicer to some online-only service. That would not make sense and you do not need to worry about that.</p>
<p>The main motivation for collecting feedback from users automatically is that most extension developers don’t get any financial compensation for their work; and their enthusiasm is only kept alive by seeing that people use their extensions. Of course everyone is busy, so people do not take the time to give feedback, which often causes developers to lose interest and give up maintaining and improving their extensions. The idea is that we could collect information about how many people use an extension and make it available to its developer, without requiring any efforts from the user. Of course users can opt out, or we could make reporting disabled by default (but then users would need to take an effort to enable reporting if they want to keep their beloved modules alive).</p>
<p>If you have any specific concerns or have ideas on how to do this well then let us know.</p>

---

## Post #65 by @Bob5 (2024-04-18 12:38 UTC)

<p>Thanks for replay, my answer was a bit ‘shizo’ but backed by many years and many similar examples from past. Just keep an eye on this ‘future’ and how it is used. It can be beneficial or dangerous for end user and even for project.</p>
<p>I cant demand and I dont demand anything (because I didnt contributed yet to project), I was only opinion. Thanks for reading and taking this biased opinion into account.</p>
<p>Thanks for great software (I dont use it commercially, I use it 100% as hobbyst) <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #66 by @jamesobutler (2024-04-18 14:13 UTC)

<p>Hi <a class="mention" href="/u/bob5">@Bob5</a> thanks for the feedback:</p>
<aside class="quote no-group" data-username="Bob5" data-post="65" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/c57346/48.png" class="avatar"> Bob5:</div>
<blockquote>
<p>It can be beneficial or dangerous for end user and even for project.</p>
</blockquote>
</aside>
<p>Can you help describe in specifics the types of dangers that you are most concerned about? That will help guide the progress on this topic. Thanks!</p>

---

## Post #67 by @Bob5 (2024-04-19 00:36 UTC)

<p>Like … Spying on users? How could it be bad? I have no idea.</p>
<p>For projects like audacity (audio editor) - it had to drop the idea of telemetry but still have a bad PR to this day. But it was big project with lots of people using it, and after announcing telemetry to improve this program - it headed stright to /dev/null. So they have no choice and revert the idea of telemetry.</p>
<p>So, why its bad and why people dont like it?<br>
-the way the data is sent is not transparent, its different than making a text file, that user can read and sending it via email attachment or similar mean.<br>
-data collection dont really improve the software, like really, some of them are getting worse, and use more resources to just collect the data.<br>
-(CubeIDE - for ARM microcontrollers).<br>
-its slippery slope to collect more and more so called ‘telemetry’ data<br>
-if you want to improve software - first improve bug/issue reporting, is it easy to ‘normal’ user, how its managed, what is the outcome?</p>
<p>Just a couple fast thoughts, thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #68 by @lassoan (2024-04-19 02:07 UTC)

<p>“Spying” sounds bad. But would you call data collection spying if it is all done with the explicit consent and full understanding of the user?</p>

---

## Post #69 by @Bob5 (2024-04-19 05:05 UTC)

<p>From legal point of view - NO !</p>
<p>From practical point of view - YES of course !</p>
<p>Nobody really reads that stuff, and this fact can be used against user. Its user fault - but still can be used against user (that can assume that nobody will abuse him).</p>
<ol>
<li>Does program provide a clear and easy way to view all data that will be sent (not only data type but FULL data) before sending?</li>
<li>can user say yes/no before each data send? Decide when, what and how this data will be sent?</li>
<li>can user easily without consequences (that program still works 100% as before), at any time disable / enable telemetry?</li>
</ol>

---

## Post #70 by @lassoan (2024-04-19 11:26 UTC)

<p>These specifics are very useful. We can very easily implement telemetry so that we can answer Yes to all these 3 questions.</p>
<p>Is there any information that you would be comfortable with sharing and any specific data that you would not want to share? (number of times Slicer is started, specific modules or features used; CPU, GPU, RAM, operating system, screen size information, …)</p>

---

## Post #71 by @Bob5 (2024-04-19 13:46 UTC)

<p>I think its OK, anything above that can be considered “fingerprinting” like kernel compilation, more specyfic hardware details etc. and even more - like accesing files and usage of fule etc. is in my opinion not apropriate. Thank You <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #72 by @jamesobutler (2024-04-19 14:34 UTC)

<aside class="quote no-group" data-username="Bob5" data-post="71" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/c57346/48.png" class="avatar"> Bob5:</div>
<blockquote>
<p>more specyfic hardware details etc</p>
</blockquote>
</aside>
<p>Do you find the hardware details that Steam collects to be acceptable?<br>
<a href="https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam" class="onebox" target="_blank" rel="noopener nofollow ugc">https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam</a></p>

---

## Post #73 by @BerDom.Ing (2024-05-06 15:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="61" data-topic="30873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<ul>
<li>Set up an nginx the server (based on Kitware’s recommendation) that returns success (200 OK) and an empty page whenever it receives a valid web request and it logs the request into a file.</li>
<li>You can run a simple flask application to check the validity of the request (similar to <a href="https://github.com/Slicer/slicer_download/tree/main/slicer_download_server" rel="noopener nofollow ugc">this</a> but much simpler as you don’t need to return any real content)</li>
<li>The request format is something like <a href="https://example.com/telemetry?app=Slicer&amp;app_version=5.6.2&amp;collection_start_date=20240402&amp;collection_end_date=20240415&amp;app_startup=28&amp;module_DICOM_activate=12&amp;module_SampleData_activate=3&amp;extension_LungCTAnalyzer_AISegmentation=18&amp;extension_LungCTAnalyzer_ClassicSegmentation=2" rel="noopener nofollow ugc">https://example.com/telemetry?app=Slicer&amp;app_version=5.6.2&amp;collection_start_date=20240402&amp;collection_end_date=20240415&amp;app_startup=28&amp;module_DICOM_activate=12&amp;module_SampleData_activate=3&amp;extension_LungCTAnalyzer_AISegmentation=18&amp;extension_LungCTAnalyzer_ClassicSegmentation=2</a></li>
<li>Implement a script (almost the same as <a href="https://github.com/Slicer/slicer_download/tree/main/etc/slicer_parselogs" rel="noopener nofollow ugc">this</a>) that parses the server logs and saves results into a database and/or json file</li>
</ul>
</blockquote>
</aside>
<p>I started working on that here: <a href="https://github.com/BerDom-Ing/Telemetry" rel="noopener nofollow ugc">https://github.com/BerDom-Ing/Telemetry</a></p>

---

## Post #74 by @jcfr (2024-06-11 18:56 UTC)

<p>Following up <a href="https://discourse.slicer.org/t/2024-06-11-weekly-meeting/36652">this morning</a> weekly hangout, sources of the website that will be used to visualize the 3D Slicer application and extensions usage statistics will be organized in the following GitHub repository.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Slicer/slicer-usage-stats">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/slicer-usage-stats" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/0f7515e26ede0201102aaec80a3ee162ba5475185d7f52ee47154f36d7d335a4/Slicer/slicer-usage-stats" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Slicer/slicer-usage-stats" target="_blank" rel="noopener">GitHub - Slicer/slicer-usage-stats: Source code of the site allowing to...</a></h3>

  <p>Source code of the site allowing to visualize Slicer application and extension usage statistics. - Slicer/slicer-usage-stats</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #75 by @lassoan (2024-07-16 20:45 UTC)

<p>A pull request has been submitted that proposes to add <code>qSlicerCoreApplication::logUsageEvent(QString component, QString event)</code> method, which can be called by modules in Slicer core and extensions to indicate that certain software feature is used. The application itself does not process the event, just emits a <code>usageEventLogged(QString, QString)</code> signal, which can be connected to slots in external modules.</p>
<p>This API can be used for example for implementing an extension that collects usage data and computes usage statistics of various features. If no extensions are installed that processes software usage data then calling <code>qSlicerCoreApplication::logUsageEvent</code> has no effect.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7855">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7855" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7855" target="_blank" rel="noopener">ENH: Added API to log software usage events</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:add-usage-logging-api</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-07-16" data-time="20:34:58" data-timezone="UTC">08:34PM - 16 Jul 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 2 files with 26 additions and 0 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7855/files" target="_blank" rel="noopener">
            <span class="added">+26</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The new qSlicerCoreApplication::logUsageEvent can be called by modules in Slicer<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7855" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> core and extensions to indicate that certain software feature is used. The application itself does not process the event, just emits a 'usageEventLogged' signal, which can be connected to slots in external modules.

This API can be used for example for implementing an extension that collects usage data and computes usage statistics of various features. If no extensions are installed that processes software usage data then calling qSlicerCoreApplication::logUsageEvent has no effect.

How to test:

```
# Observe the usage event and print it if any is logged
slicer.app.connect("usageEventLogged(QString,QString)", lambda component, event: print(f"{component} -&gt; {event}"))

# Log an event
slicer.app.logUsageEvent("TotalSegmentator", "segmentation/ct/total")
```

See related discussions at https://discourse.slicer.org/t/should-we-start-collecting-software-usage-data/30873

---

This pull request deprecates https://github.com/Slicer/Slicer/pull/7788, as we do not want to put any actual usage data recording into Slicer core, just a hook that allows implementing extensions in the future (that the user can optionally install) that can collect usage data.

@jcfr @pieper @sjh26 @jamesobutler @cpinter</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Any questions and suggestions are welcome, preferably at the pull request, so that we have all the discussions related to this proposed change at one place.</p>

---

## Post #76 by @BerDom.Ing (2024-07-17 20:44 UTC)

<p>I’m working on a repo where I’m developing a website to visualize the usage statistics of the 3D Slicer application and its extensions. So far, I’ve managed to create a bar chart that displays modules and functions. When you click on a bar in the modules chart, it filters the functions chart to show only the functions from the selected module.</p>
<p>I would appreciate a review of the charts and would love to hear any ideas on how to improve them.</p>
<p>Here is the repo: <a href="https://github.com/BerDom-Ing/slicer-usage-stats" class="inline-onebox" rel="noopener nofollow ugc">GitHub - BerDom-Ing/slicer-usage-stats: Source code of the site allowing to visualize Slicer application and extensions usage statistics.</a></p>
<p>It looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e67302c1cdd3b1d8c62ba1addf632b460ead0470.png" data-download-href="/uploads/short-url/wSEe73dq9lXZdVPuP3CZdlny4ww.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e67302c1cdd3b1d8c62ba1addf632b460ead0470_2_690x403.png" alt="image" data-base62-sha1="wSEe73dq9lXZdVPuP3CZdlny4ww" width="690" height="403" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e67302c1cdd3b1d8c62ba1addf632b460ead0470_2_690x403.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e67302c1cdd3b1d8c62ba1addf632b460ead0470_2_1035x604.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e67302c1cdd3b1d8c62ba1addf632b460ead0470_2_1380x806.png 2x" data-dominant-color="CFDCE6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1565×916 46.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks in advance for your feedback!</p>

---

## Post #77 by @rbumm (2024-08-02 19:32 UTC)

<p>I recognize that many of you have had reservations about the use of counters in the Lung CT Analyzer extension. In response, I have removed all counters from the extension. Additionally, due to the mechanism being buggy, all related data have been deleted.</p>
<p>Let’s collaborate to develop a more intelligent solution for this issue.</p>
<p>Wishing everyone a wonderful, counter-free weekend!</p>

---

## Post #78 by @lassoan (2024-08-03 21:27 UTC)

<p>We are slowly making progress with this. We now have an API in Slicer Preview Release that extensions can use to log usage events:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7855">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7855" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7855" target="_blank" rel="noopener">ENH: Add API to log software usage events</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:add-usage-logging-api</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-07-16" data-time="20:34:58" data-timezone="UTC">08:34PM - 16 Jul 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 4 files with 57 additions and 0 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7855/files" target="_blank" rel="noopener">
            <span class="added">+57</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The new qSlicerCoreApplication::logUsageEvent can be called by modules in Slicer<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7855" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> core and extensions to indicate that certain software feature is used. The application itself does not process the event, just emits a 'usageEventLogged' signal, which can be connected to slots in external modules.

This API can be used for example for implementing an extension that collects usage data and computes usage statistics of various features. If no extensions are installed that processes software usage data then calling qSlicerCoreApplication::logUsageEvent has no effect.

How to test:

```
# Observe the usage event and print it if any is logged
slicer.app.connect("usageEventLogged(QString,QString)", lambda component, event: print(f"{component} -&gt; {event}"))

# Log an event
slicer.app.logUsageEvent("TotalSegmentator", "segmentation/ct/total")
```

See related discussions at https://discourse.slicer.org/t/should-we-start-collecting-software-usage-data/30873

---

This pull request deprecates https://github.com/Slicer/Slicer/pull/7788, as we do not want to put any actual usage data recording into Slicer core, just a hook that allows implementing extensions in the future (that the user can optionally install) that can collect usage data.

@jcfr @pieper @sjh26 @jamesobutler @cpinter</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The plan is that if the user installs the Telemetry extension and gives permission then the usage events can be recorded and aggregated on a server.</p>

---

## Post #79 by @mau_igna_06 (2024-09-09 20:35 UTC)

<p>NOTE: I think on first iterations of the Telemetry extension we should auto-exclude (or even forbid) telemetry from european citizens because General Data Protection Regulation (GDPR) is very strict. We can always support european users later.</p>

---

## Post #80 by @lassoan (2024-09-09 20:39 UTC)

<p>We don’t need to exclude European countries, as long as we don’t store any information that can identify individuals (such as email, IP address, hash created from fingerprinting the hardware components, etc.). Since many people would prefer not to be individually identified anyway, it is probably the best to just not store such information, only anonymous, aggregate data.</p>

---

## Post #81 by @BerDom.Ing (2024-09-26 19:55 UTC)

<p>I want to do a pull request to <a href="https://github.com/Slicer/SlicerTelemetry" rel="noopener nofollow ugc">Slicer/SlicerTelemetry</a>, the repository is empty and i cant fork it, i need to fork it to do the pull request</p>

---

## Post #82 by @lassoan (2024-09-27 14:44 UTC)

<p>I’ve added a few files. You should be able to fork the repository now.</p>

---

## Post #83 by @mau_igna_06 (2024-10-29 23:41 UTC)

<p>I would be nice if this extension arrived on the new stable release <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #84 by @BerDom.Ing (2024-11-25 19:03 UTC)

<p>Hello everyone,</p>
<p>I’d like to share my progress on the development of the telemetry extension for Slicer 3D.<br>
Here is what you need to know:</p>
<p><strong>For End Users:</strong></p>
<p>When there is data to be uploaded to the server this dialog will show up:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d9c88b020a379b0becc2a162a6b40508f54dc9b.png" data-download-href="/uploads/short-url/6vuReoJZMG585aiWo9txYKR9qif.png?dl=1" title="SendToServerPopUp" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d9c88b020a379b0becc2a162a6b40508f54dc9b.png" alt="SendToServerPopUp" data-base62-sha1="6vuReoJZMG585aiWo9txYKR9qif" width="466" height="113"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SendToServerPopUp</span><span class="informations">466×113 4.44 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Including the raw data<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/2062ce75dda80c908d2890284491b0889241332f.png" data-download-href="/uploads/short-url/4CuYcqmmNBgm7rppgSrzoWINXQP.png?dl=1" title="seeRawData" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/2062ce75dda80c908d2890284491b0889241332f.png" alt="seeRawData" data-base62-sha1="4CuYcqmmNBgm7rppgSrzoWINXQP" width="469" height="228"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">seeRawData</span><span class="informations">469×228 6.73 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And a visualization of the data collected<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87905993adbf73234dfc8646e9d96135b250771c.png" data-download-href="/uploads/short-url/jlfJ3GCngKiwEA24qNKd0R1vq7a.png?dl=1" title="dataVisualization" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87905993adbf73234dfc8646e9d96135b250771c.png" alt="dataVisualization" data-base62-sha1="jlfJ3GCngKiwEA24qNKd0R1vq7a" width="690" height="485" data-dominant-color="BCD4E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dataVisualization</span><span class="informations">967×680 12.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The data used in the following images was generated randomly to test the frontend.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/872ed38a4babe2322eb342dea3e7ce61031bc6b1.png" data-download-href="/uploads/short-url/jhSMzBV0ByX5M7NMImzGBSlfoNr.png?dl=1" title="mapAndTimeLine" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/872ed38a4babe2322eb342dea3e7ce61031bc6b1_2_641x500.png" alt="mapAndTimeLine" data-base62-sha1="jhSMzBV0ByX5M7NMImzGBSlfoNr" width="641" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/872ed38a4babe2322eb342dea3e7ce61031bc6b1_2_641x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/872ed38a4babe2322eb342dea3e7ce61031bc6b1_2_961x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/872ed38a4babe2322eb342dea3e7ce61031bc6b1.png 2x" data-dominant-color="EAEFF5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mapAndTimeLine</span><span class="informations">1108×863 80.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b94686ee69d656d7e217e31848867954b4ff278c.png" data-download-href="/uploads/short-url/qr1r0qxAzff7WQvBoicVCExYqRu.png?dl=1" title="ComponentAndEvent" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b94686ee69d656d7e217e31848867954b4ff278c.png" alt="ComponentAndEvent" data-base62-sha1="qr1r0qxAzff7WQvBoicVCExYqRu" width="690" height="485" data-dominant-color="E7EBEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ComponentAndEvent</span><span class="informations">1079×759 47.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can also select which extensions are allowed to collect information on the Telemetry Extension<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45cba3bc57e5becd80ed1a60451459ba711f1013.png" data-download-href="/uploads/short-url/9XreXsPTGRiCaWdTdysQv83CzAf.png?dl=1" title="selectExtensions" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45cba3bc57e5becd80ed1a60451459ba711f1013.png" alt="selectExtensions" data-base62-sha1="9XreXsPTGRiCaWdTdysQv83CzAf" width="476" height="211"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">selectExtensions</span><span class="informations">476×211 4.55 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The default configuration is asked on slicer start just once.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bbd271dc99b17f8860ff1f5243e642768d4e16e.png" data-download-href="/uploads/short-url/d5yHSPrRPHVII31b5pMjwOeth3U.png?dl=1" title="installedExtensionsPermission" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bbd271dc99b17f8860ff1f5243e642768d4e16e.png" alt="installedExtensionsPermission" data-base62-sha1="d5yHSPrRPHVII31b5pMjwOeth3U" width="298" height="125"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">installedExtensionsPermission</span><span class="informations">298×125 3.58 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h4><a name="p-119881-for-slicer-developers-1" class="anchor" href="#p-119881-for-slicer-developers-1" aria-label="Heading link"></a>For Slicer Developers:</h4>
<h4><a name="p-119881-telemetry-extension-workflow-2" class="anchor" href="#p-119881-telemetry-extension-workflow-2" aria-label="Heading link"></a>Telemetry Extension Workflow</h4>
<p>The <strong>Telemetry Extension</strong> is designed to log, organize, and upload usage data. Here’s a breakdown of its components and functionality:</p>
<ol>
<li><strong>Logging Events in Extensions:</strong></li>
</ol>
<ul>
<li>To log an event from an extension, use the following code snippet:</li>
</ul>
<p><em>slicer.app.logUsageEvent(“Component”, “Event”).</em></p>
<ul>
<li>This emits a <em>usageEventLogged</em> signal.</li>
<li>The signal is connected to the <em>onUsageEventLogged</em> function, which processes the event.</li>
</ul>
<ol start="2">
<li><strong>Event Logging with</strong> <em>onUsageEventLogged(component, event)</em>:</li>
</ol>
<ul>
<li>This method saves incoming events into a <em>.csv</em> file.</li>
<li>It verifies whether the event’s source component belongs to one of three categories:
<ul>
<li><strong>enabledExtensions:</strong> Telemetry is explicitly enabled.</li>
<li><strong>disabledExtensions:</strong> Telemetry is explicitly disabled.</li>
<li><strong>defaultExtensions:</strong> Telemetry depends on a default setting (e.g., whether telemetry is enabled by default for new installations).</li>
</ul>
</li>
<li>Only events from components with enabled telemetry (or default-enabled settings) are saved.</li>
<li>The method also:
<ul>
<li><strong>Adds timestamps</strong> to each event.</li>
<li><strong>Groups events by occurrence per day</strong> for aggregation and easier analysis.</li>
</ul>
</li>
</ul>
<p><strong>Extension Installation:</strong></p>
<ul>
<li>When an extension is installed, it is automatically added to the defaultExtensions category.</li>
</ul>
<p><strong>Data Upload Prompt:</strong></p>
<ul>
<li>A prompt asking for permission to upload data appears only if the following conditions are met:
<ul>
<li>More than <strong>7 days</strong> have passed since the last upload.</li>
<li>There is data in the <em>.csv</em> file waiting to be uploaded.</li>
</ul>
</li>
<li>If the user selects “Do not show again,” the preference is saved, and the prompt will not appear again.</li>
</ul>
<p><strong>Uploading and Request Handling:</strong></p>
<ul>
<li>Functions like <em>weeklyUsageUpload</em> and <em>handleQtReply</em> use <strong>QNetworkAccessManager</strong> for asynchronous handling of HTTP requests and responses. This avoids blocking the main application, unlike synchronous libraries such as <em>requests</em>.</li>
</ul>
<h4><a name="p-119881-server-side-implementation-3" class="anchor" href="#p-119881-server-side-implementation-3" aria-label="Heading link"></a>Server-Side Implementation</h4>
<p>The server is implemented using <strong>Flask</strong> and performs the following tasks:</p>
<ol>
<li><strong>Geolocation Mapping:</strong></li>
</ol>
<ul>
<li>The <em>get_location_from_ip</em> function:
<ul>
<li>Extracts the <strong>country, country code,</strong> and <strong>city</strong> based on the IP address in a POST request.</li>
<li>Uses the <strong>GeoIP2 database</strong> for geolocation mapping.</li>
<li>This data is appended to the event details (e.g., component, event, date, and aggregated times).</li>
</ul>
</li>
</ul>
<ol start="2">
<li><strong>Data Conversion:</strong></li>
</ol>
<ul>
<li>The <em>convert_alpha2_to_alpha3</em> function:
<ul>
<li>Converts two-letter country codes (ISO Alpha-2) to three-letter codes (ISO Alpha-3) for compatibility with the frontend.</li>
</ul>
</li>
</ul>
<ol start="3">
<li><strong>Data Handling:</strong></li>
</ol>
<ul>
<li>Event data from POST requests is appended to a <em>data.csv</em> file located in the <em>static</em> folder.</li>
<li>This <em>.csv</em> file is used by the frontend for generating statistics.</li>
</ul>
<ol start="4">
<li><strong>Frontend Hosting:</strong></li>
</ol>
<ul>
<li>The Flask application serves the frontend content, also stored in the <em>static</em> folder.</li>
</ul>
<h4><a name="p-119881-nginx-server-4" class="anchor" href="#p-119881-nginx-server-4" aria-label="Heading link"></a>Nginx Server</h4>
<ul>
<li>An <strong>Nginx server</strong> is used as a reverse proxy for the Flask application, offering several advantages:
<ul>
<li>Handles incoming traffic and forwards it to the Flask application.</li>
<li>Efficiently manages a high volume of concurrent connections.</li>
<li>Provides faster response times and a smoother user experience compared to Flask handling requests directly.</li>
</ul>
</li>
</ul>
<h4><a name="p-119881-frontend-visualization-5" class="anchor" href="#p-119881-frontend-visualization-5" aria-label="Heading link"></a>Frontend Visualization</h4>
<p>The frontend provides a user-friendly interface for visualizing telemetry data:</p>
<ol>
<li><strong>Charts with <em>stats.js</em></strong>:</li>
</ol>
<ul>
<li>Uses <strong>D3.js</strong> and <strong>Crossfilter</strong> libraries to:
<ul>
<li>Create interactive charts.</li>
<li>Establish linkages between dimensions, allowing charts to filter and update based on user interactions.</li>
</ul>
</li>
</ul>
<ol start="2">
<li><strong>World Map:</strong></li>
</ol>
<ul>
<li>The map, defined in <em>world.geojson:</em>
<ul>
<li>Is an SVG file containing country names and codes.</li>
<li>Links to the event data for geographic visualization.</li>
</ul>
</li>
</ul>
<p>Thank you for taking the time to read about my progress. I welcome any feedback or suggestions from the community as I continue to develop this Slicer 3D extension!</p>
<p>Best regards,<br>
Bernardo Dominguez</p>

---

## Post #85 by @BerDom.Ing (2025-04-22 01:42 UTC)

<p>Here is a demo of the front end handling 1 million rows of generated (not real) data. It’s hosted on Amazon Lightsail with a dynamic IP <a href="http://44.204.140.26/" rel="noopener nofollow ugc">http://44.204.140.26/</a> (it may change). To skip the loading, go to 00:46.<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31f1210eb2ac5607be4b893fd5eaea6415d17260.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c52895690880e238fa8a1d5702e296507ab99d5.png" data-video-base62-sha1="77O0Nk76WuYz8VLxOWXtI1f4PyE.mp4">
  </div><p></p>

---
