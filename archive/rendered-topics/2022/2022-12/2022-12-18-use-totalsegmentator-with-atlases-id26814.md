# Use TotalSegmentator with atlases

**Topic ID**: 26814
**Date**: 2022-12-18
**URL**: https://discourse.slicer.org/t/use-totalsegmentator-with-atlases/26814

---

## Post #1 by @Melodicpinpon (2022-12-18 19:20 UTC)

<p>Wow, That is impressive.<br>
Congratulations and many thanks, Andras !<br>
Do you see some combination possible with pre-defined 3D meshes -named and organized- as the ones of ‘Z-Anatomy’? (<a href="https://www.z-anatomy.com/" rel="noopener nofollow ugc">https://www.z-anatomy.com/</a>)</p>

---

## Post #2 by @lassoan (2022-12-18 22:58 UTC)

<p>There could many ways to combine the result of patient-specific segmentation results with atlases. For example, you could use the segmented structures as landmarks to register the models and then either bring in additional segments from the atlas into the patient-specific model, or import patient-specific anatomic variations into the atlas.</p>
<p>The TotalSegmentator module labels each segment with standard terminology (SNOMED CT), which makes it easy to determine correspondence with structures in the atlas (which hopefully also uses standard terminology).</p>

---

## Post #3 by @mhalle (2022-12-19 03:09 UTC)

<p>Z-Anatomy actually uses Terminologia Anatomical (TA2). You can find a browser for it at <a href="https://ta2viewer.openanatomy.org/" rel="noopener nofollow ugc">https://ta2viewer.openanatomy.org/</a> I converted the TA2 label names to TA2 and sent them to the author; don’t know if they will consider using them. There are some ambiguous structures, in TotalSegmentator, such as in the back muscles. TA2 would help fix that</p>
<p>-Mike</p>

---

## Post #4 by @lassoan (2022-12-19 04:55 UTC)

<aside class="quote no-group" data-username="mhalle" data-post="3" data-topic="26814">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/50afbb/48.png" class="avatar"> mhalle:</div>
<blockquote>
<p>I converted the TA2 label names to TA2 and sent them to the author</p>
</blockquote>
</aside>
<p>Do you mean TotalSegmentator label names to TA2? It would be nice if all segmentation tools would switch to standard terms. TotalSegmentator would be a very influential example, so it would worth the effort.</p>
<p>I don’t see your pull request in the <a href="https://github.com/wasserth/TotalSegmentator/">TotalSegmentator repository</a>. It would be great if you work on this openly so that we can track the progress, show our support, and help out as needed.</p>
<aside class="quote no-group" data-username="mhalle" data-post="3" data-topic="26814">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/50afbb/48.png" class="avatar"> mhalle:</div>
<blockquote>
<p>You can find a browser for it at <a href="https://ta2viewer.openanatomy.org/">https://ta2viewer.openanatomy.org/</a></p>
</blockquote>
</aside>
<p>I’ve tried to find individual vertebrae in the TA2 browser, but I could not find any.</p>
<p>For example, FMA term for T5 vertebra is <a href="https://bioportal.bioontology.org/ontologies/FMA/?p=classes&amp;conceptid=http%3A%2F%2Fpurl.org%2Fsig%2Font%2Ffma%2Ffma9922">9922</a>. I’ve tried to search for <code>T5</code>, search for <code>9922</code> (FMA code), browse the tree (got no further than <a href="https://ta2viewer.openanatomy.org/?id=1059">thoracic vertebra</a>).</p>
<p>Is there a TA2 code for the T5 vertebra? Or you need to specify it using a modifier code?</p>
<aside class="quote no-group" data-username="mhalle" data-post="3" data-topic="26814">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/50afbb/48.png" class="avatar"> mhalle:</div>
<blockquote>
<p>There are some ambiguous structures, in TotalSegmentator, such as in the back muscles.</p>
</blockquote>
</aside>
<p>How TA2 can be used to address these issues? Is it easy to add a new term for custom group of terms or make other changes/additions initiated by the research community? That would be a major advantage compared to locked-down, heavily managed terminologies, such as SNOMED CT.</p>
<p>SNOMED CT has potential usage right issues as well (we started to discuss this <a href="https://github.com/Slicer/Slicer/pull/6728#issuecomment-1345347191">here</a>). It may be useful to switch to TA2 for all anatomical terms for better compatibility with open science. SNOMED CT is still required for DICOM import/export for clinical use, but we could implement that with a SNOMED CT ↔ TA2 translation table.</p>

---

## Post #5 by @mhalle (2022-12-19 16:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="26814" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I don’t see your pull request in the <a href="https://github.com/wasserth/TotalSegmentator/" rel="noopener nofollow ugc">TotalSegmentator repository</a>. It would be great if you work on this openly so that we can track the progress, show our support, and help out as needed.</p>
</blockquote>
</aside>
<p>I sent email to the author directly very early after publication. I can create an issue.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="26814" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’ve tried to find individual vertebrae in the TA2 browser, but I could not find any.</p>
<p>For example, FMA term for T5 vertebra is <a href="https://bioportal.bioontology.org/ontologies/FMA/?p=classes&amp;conceptid=http%3A%2F%2Fpurl.org%2Fsig%2Font%2Ffma%2Ffma9922" rel="noopener nofollow ugc">9922</a>. I’ve tried to search for <code>T5</code>, search for <code>9922</code> (FMA code), browse the tree (got no further than <a href="https://ta2viewer.openanatomy.org/?id=1059" rel="noopener nofollow ugc">thoracic vertebra</a>).</p>
</blockquote>
</aside>
<p>TA2 doesn’t necessarily go all the way down as far as some other nomenclatures, unfortunately. I will get some guidance from the editor about ways to extend it to include structures beyond its resolution.</p>
<aside class="quote no-group" data-username="mhalle" data-post="3" data-topic="26814">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/50afbb/48.png" class="avatar"> mhalle:</div>
<blockquote>
<p>There are some ambiguous structures, in TotalSegmentator, such as in the back muscles.</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="26814" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How TA2 can be used to address these issues?</p>
</blockquote>
</aside>
<p>For example, TS includes the term “autochthon” left and right. These structures is more commonly called the autochthonous muscles. In TA2, the closest correspondence is the erector spinae or the epaxial muscles. From the image in the TS paper, exactly which muscles are intend is not completely clear.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="26814" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is it easy to add a new term for custom group of terms or make other changes/additions initiated by the research community? That would be a major advantage compared to locked-down, heavily managed terminologies, such as SNOMED CT.</p>
</blockquote>
</aside>
<p>TA2 is standardized as well, but at least it isn’t licensed. One of the reasons it is standardized is because atlases like Netter are being moved to TA2 terminology. The advantage of it is that it does set standards for the exact Latin and English terms, so it’s easier to get new terms to be consistent.</p>
<p>This is an area we should pursue more, since we are working in collaboration with people who edit TA2.</p>

---

## Post #6 by @lassoan (2022-12-19 18:48 UTC)

<p>Thanks for the answers. We have lots of interesting topics to discuss further at the upcoming project week.</p>

---

## Post #7 by @Melodicpinpon (2022-12-22 17:23 UTC)

<p><a class="mention" href="/u/mhalle">@mhalle</a> <a class="mention" href="/u/lassoan">@lassoan</a> To be fair, After having to retro-engineer the whole lexicon from the locked .pdf because ‘Open Anatomy’ would not share it with me, I recently received a document -with the latest updates I guess-.</p>
<p>The FIPAT of the IFAA should re-think their way to share information in the first place, and so does Open-anatomy. Recreating and verifying manually all this information takes time.</p>
<p>Here is what we have (<a href="https://docs.google.com/spreadsheets/d/1Ee6rmpT-SBkcey_VMumNsyM9pOM8OoiEcY7-jVWhaDM/edit#gid=1807617850" class="inline-onebox" rel="noopener nofollow ugc">Terminologia Anatomica-Second Edition - Google Sheets</a>); the vertebrae and the discs are all named individually but the hierarchy had to be recreated afterwards in Blender and in Unity. If you want to improve it; you can just send an email address, receive an editor’s access and edit the content directly.</p>
<p>These things have to be done and shared in a collaborative way.<br>
We already have the whole industry to deal with; helping each other should not be so hard between ‘Open anatomy’, ‘3D Slicer’ and ‘Z-Anatomy’. And if somebody could convince Paul Gobee from the University of Leiden to share his modified version, that would also help a lot.</p>

---

## Post #8 by @lassoan (2022-12-22 18:08 UTC)

<p>I don’t know anything about locked pdf files or FIPAT or IFAA, but I am all for fully open communication and collaboration. I guess it just takes sometimes some time for people to let things go and hope that that you will get enough return on your investment of work in the long term.</p>
<p>By the way, I’ve noticed that <a href="https://www.z-anatomy.com/about">Z-anatomy license</a> seems to come with a non-permissive license. The problem is with “must distribute your contributions” obligation in its share-alike term:</p>
<blockquote>
<p>If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original</p>
</blockquote>
<p>I don’t plan to make improvements to any atlases that I would keep for myself but I rather invest time into things that I can use for any purpose in the future.</p>

---

## Post #9 by @Melodicpinpon (2022-12-23 19:29 UTC)

<p>Thank you for your answer.</p>
<p>Are you speaking about the basic vocabulary of anatomy when saying :</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="26814">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>hope that that you will get enough return on your investment of work in the long term</p>
</blockquote>
</aside>
<p>?</p>
<p>If so, I would argue that Education is not a speculative asset but rather a human right and a public service that the public money spent on education owes to the tax-payer and all the rest of the population. That being said, I do not expect anybody to participate in anything he does not want to, but calling a website ‘Open anatomy’ and refusing to share the basic vocabulary of anatomy is a bit hard to swallow.</p>
<p>The CC-BY-SA license is the license under which the models from ‘BodyParts3D’ are shared; therefor it is not only because I personally think that protecting the commons is necessary but also by legal necessity that this license has been chosen. I would not call it non-permissive since this license does not prevent any modification; it only makes sure that any further step will continue benefiting to the whole community.</p>

---

## Post #10 by @lassoan (2022-12-23 20:49 UTC)

<aside class="quote no-group" data-username="Melodicpinpon" data-post="9" data-topic="26814">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/melodicpinpon/48/3254_2.png" class="avatar"> Melodicpinpon:</div>
<blockquote>
<p>calling a website ‘Open anatomy’ and refusing to share the basic vocabulary of anatomy is a bit hard to swallow</p>
</blockquote>
</aside>
<p>This does not seem to make sense to me either. Probably I don’t know something, or it might have been just some misunderstanding or some external constraint. Maybe <a class="mention" href="/u/mhalle">@mhalle</a> can clarify.</p>
<aside class="quote no-group" data-username="Melodicpinpon" data-post="9" data-topic="26814">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/melodicpinpon/48/3254_2.png" class="avatar"> Melodicpinpon:</div>
<blockquote>
<p>I would not call it non-permissive</p>
</blockquote>
</aside>
<p>“Permissive license” refers to the group of licenses including BSD, MIT, Apache, etc. that practically do not impose any limitation on use. In contract, CC-BY-SA is a copyleft license, similar to GPL and AGPL. See some more information <a href="https://en.wikipedia.org/wiki/Permissive_software_license">here</a>.</p>
<aside class="quote no-group" data-username="Melodicpinpon" data-post="9" data-topic="26814">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/melodicpinpon/48/3254_2.png" class="avatar"> Melodicpinpon:</div>
<blockquote>
<p>The CC-BY-SA license is the license under which the models from ‘BodyParts3D’ are shared</p>
</blockquote>
</aside>
<p>This is really unfortunate, as an open anatomical atlas would require restriction-free collaboration, contributions from a wide range of groups, and a non-permissive license scares away many people.</p>
<p>Non-permissive license is fine if you just want to use something as is. For example, most people don’t want to modify infrastructural code, such as the linux kernel or Qt, or a commodity software, such as a password manager. But if you plan to work on a project a lot, build on it, etc. then you want to make sure you can use the result of your work any way you want.</p>
<aside class="quote no-group" data-username="Melodicpinpon" data-post="9" data-topic="26814">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/melodicpinpon/48/3254_2.png" class="avatar"> Melodicpinpon:</div>
<blockquote>
<p>I personally think that protecting the commons is necessary</p>
</blockquote>
</aside>
<p>This is a hard question. Some form of protection or guarantee that your hard work is rewarded would be nice, but I don’t think there is a perfect solution.</p>
<p>Over the years, restrictive open-source licensing (often paired with a paid commercial license) has proven to be very problematic and my perception is that the Stallman/FSF/copyleft is getting less and less popular.</p>
<p>Non-restrictive open-source licenses (often paired with paid consulting for custom development and training provided by core contributors) require a lot of trust from developers/maintainers that they will get eventually fairly compensated for their effort. This does not always happen, but there are good examples (see the whole Slicer/NAMIC ecosystem) and there are lots of initiatives that aim for helping with these, such as GitHub sponsors, OpenCollective, NumFocus, CZI, etc.</p>

---

## Post #11 by @Melodicpinpon (2022-12-26 16:59 UTC)

<p>It will probably sound silly but the biggest question mark in my point of view is:<br>
‘How did we manage to spend millions on Education every year and in every country without producing any learning material during several centuries?’.</p>
<p>If, as I think, this nearly complete sterility of the public investment on education is the central problem of the knowledge production of our society; then the first thing to do is to formulate the problem and then, if no satisfying answer is received from the competent authorities, we ought indeed to start searching for a turnaround.</p>
<p>What would help a lot at the moment would be to gather the strengths beginning with bridging the work made by the university of Leiden (+Utrecht, Maastricht and Leuven) to the other people willing to develop the atlas.</p>

---

## Post #12 by @fedorov (2023-01-03 16:44 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="26814">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>SNOMED CT has potential usage right issues as well (we started to discuss this <a href="https://github.com/Slicer/Slicer/pull/6728#issuecomment-1345347191">here </a>).</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> what are those potential usage right issues?</p>
<p>As discussed in the resources pointed out by <a class="mention" href="/u/pieper">@pieper</a> in the github issue you mentioned, and also in this dcmqi page: <a href="https://qiicr.gitbook.io/dcmqi-guide/opening/coding_schemes/existing_dicom_code">https://qiicr.gitbook.io/dcmqi-guide/opening/coding_schemes/existing_dicom_code</a>, which references this blog post by <a class="mention" href="/u/david_clunie">@David_Clunie</a> <a href="http://dclunie.blogspot.com/2016/03/dicom-and-snomed-back-in-bed-together.html:">http://dclunie.blogspot.com/2016/03/dicom-and-snomed-back-in-bed-together.html:</a></p>
<blockquote>
<p>Users and commercial and open source DICOM developers can be reassured that they may continue to use the subset of SNOMED concepts in the DICOM standard in their products and software, globally and without a fee or individual license.</p>
</blockquote>
<p>SNOMED CT codes that are not in DICOM can be contributed to the standard via a correction proposal process.</p>

---

## Post #13 by @lassoan (2023-01-03 23:39 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="12" data-topic="26814">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>what are those potential usage right issues?</p>
</blockquote>
</aside>
<p>I see a two issues with SNOMED CT’s DICOM license that may prevent universal adoption:</p>
<ul>
<li>The license may only valid for implementing the DICOM standard. It may not be applicable for software that has nothing to do with DICOM.</li>
<li>Need to go through the DICOM change proposal process to add new codes. In general, the DICOM standard is centralized and slowly changing by design, as these are desirable properties for a standard that is used for implementing clinical applications. However, these properties are not well suited for research and prototyping.</li>
</ul>
<p>That said, I don’t think we can or need to choose a single terminology and use it for everything. The requirements of various applications are just so different (even contradicting) that it is impossible to fulfill all of them at the same time. Instead, we should be able to use different terminologies for different purposes, and convert between them automatically as needed.</p>

---

## Post #14 by @fedorov (2023-01-04 03:04 UTC)

<p>Andras, I agree - these are valid points. And yet another issue is that the license covers only the codes - not the relationships between them.</p>
<p>It would be nice to be able to translate from one terminology to another, but I don’t think it can always be done.</p>
<p>One thing for sure, I strongly believe that if every developer of a tool that produces some output that needs to be labeled (in the general sense) gave at least a bit of thought to using some - even any! - existing lexicon or terminology instead of free text for those labels, we would be so much better off!</p>

---
