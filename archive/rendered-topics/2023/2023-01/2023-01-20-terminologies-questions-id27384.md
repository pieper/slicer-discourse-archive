# Terminologies questions

**Topic ID**: 27384
**Date**: 2023-01-20
**URL**: https://discourse.slicer.org/t/terminologies-questions/27384

---

## Post #1 by @muratmaga (2023-01-20 19:59 UTC)

<p>As part of our training, we want to encourage the use of terminology feature of Slicer to name segments. This will provide better data reuse for downstream tasks. As I am getting more familiar myself, I noticed a few issues:</p>
<ol>
<li>
<strong>Terminology is incomplete</strong>. I am not sure where the terms are coming from (it satys DICOM master list), but as it is it is incomplete, even for humans. (E.g., it is missing Maxilla, Mandible, Nasal, Sphenoid, Zygomatic bones in skull, includes none of the ossicles -stapes, incus, malleolus, none of the post-cranial bones femur, tibia etc are listed). While I am not a radiologist, it is hard for me to believe DICOM terminology does not include these human bones.</li>
</ol>
<p>For slicermorph, the plan is to build a terminology that is usable across vertebrates using Uberon ontology. However, I believe, at the minimum core Slicer terminology should support the whole human skeleton.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f1e1aeaf37baf747a070d01fb7f51e4e8b4997c.png" data-download-href="/uploads/short-url/90mzZTSCV1q5Md3UF9zxqDkJKUY.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f1e1aeaf37baf747a070d01fb7f51e4e8b4997c_2_517x353.png" alt="image" data-base62-sha1="90mzZTSCV1q5Md3UF9zxqDkJKUY" width="517" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f1e1aeaf37baf747a070d01fb7f51e4e8b4997c_2_517x353.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f1e1aeaf37baf747a070d01fb7f51e4e8b4997c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f1e1aeaf37baf747a070d01fb7f51e4e8b4997c.png 2x" data-dominant-color="EBEAE9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">756×517 45.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol start="2">
<li>
<p><strong>Segment renaming doesn’t encourage terminology usage</strong>. Currently terminology only pops up if the color of a segment is clicked. Since it is possible to rename the segment in the terminology module, I would suggest double clicking the segment name also brings the terminology window, with the Name field activated.</p>
</li>
<li>
<p><strong>There are bugs in the behavior:</strong> Create an empty segment, double click color to bring the terminology window, search for Frontal and assign it and done, notice that even though Frontal is assigned a yellowish brown. The color shows up as gray.</p>
</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05b473808f6f9ce92435cca1a694d86c829d1f28.png" alt="image" data-base62-sha1="Ot08xRzOCpGy61r3AuBbrbNL1C" width="589" height="425"></p>

---

## Post #2 by @robertf (2023-01-20 23:58 UTC)

<p>For the record, the name of the first middle-ear ossicle is ‘malleus’, not ‘malleolus’.</p>
<ul>
<li>Robert</li>
</ul>

---

## Post #3 by @muratmaga (2023-01-21 02:10 UTC)

<p>Thanks for the correction. Still doesn’t exist in the terminology.</p>

---

## Post #4 by @rkikinis (2023-01-21 02:31 UTC)

<p>[</p>
<p><a href="https://ta2viewer.openanatomy.org/?id=881" rel="noopener nofollow ugc">TA2 Viewer</a><br>
<a href="https://ta2viewer.openanatomy.org/?id=881" rel="noopener nofollow ugc">ta2viewer.openanatomy.org</a></p>
<p><a href="https://ta2viewer.openanatomy.org/?id=881" rel="noopener nofollow ugc"><img width="36" height="36" alt="apple-touch-icon.png" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49377266fff8fa85038a7f62817a2cdec07fe8fa.png" data-base62-sha1="arHEhCeHDvUP3tPmJeaBtZRxV2O"></a></p>
<p>](<a href="https://ta2viewer.openanatomy.org/?id=881" class="inline-onebox" rel="noopener nofollow ugc">TA2 Viewer</a>)</p>
<p>This email is intended for non-work related messages</p>

---

## Post #5 by @muratmaga (2023-01-21 02:33 UTC)

<p>I meant in the Terminology bundled with Slicer’s segment editor. Otherwise, of course it exists in ontologies.</p>

---

## Post #6 by @muratmaga (2023-01-21 02:37 UTC)

<p>I am also confused how these two panel supposed to work together. For example, if you search for sphenoid in the left panel no result is returned. There is a sphenoid bone in the right panel, but it cannot be used for selection (AFAIK tell).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/7778244d46d8831e274b8b8e0b49e49786fda533.png" data-download-href="/uploads/short-url/h2SdJSgVM1DsDhee7opuWiZR9HZ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7778244d46d8831e274b8b8e0b49e49786fda533_2_690x404.png" alt="image" data-base62-sha1="h2SdJSgVM1DsDhee7opuWiZR9HZ" width="690" height="404" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7778244d46d8831e274b8b8e0b49e49786fda533_2_690x404.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7778244d46d8831e274b8b8e0b49e49786fda533_2_1035x606.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/7778244d46d8831e274b8b8e0b49e49786fda533.png 2x" data-dominant-color="EAEFF3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1222×717 21.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @rkikinis (2023-01-21 12:12 UTC)

<p>Hi Murat,<br>
you are right. I am sorry that I misunderstood your comment.<br>
Best<br>
Ron</p>

---

## Post #8 by @pieper (2023-01-21 17:02 UTC)

<p>Thanks for raising these issues <a class="mention" href="/u/muratmaga">@muratmaga</a> .  The use of consistent terms is also important for creating ground truth for machine learning.   I don’t know that anyone has dedicated funding to improve the current implementation.</p>

---

## Post #9 by @muratmaga (2023-01-21 17:32 UTC)

<aside class="quote no-group" data-username="pieper" data-post="8" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I don’t know that anyone has dedicated funding to improve the current implementation.</p>
</blockquote>
</aside>
<p>I am not sure if the current implementation needs entirely revamped. The first thing to do is to bring a more complete set of human terms to the terminology. Then, as opposed to listing a huge list, may be breakdown down by the anatomical systems (skeleton, connective tissue, organs, vasculature etc), which is I think the intention of the right panel. And the rest, as I said is to encourage the use of terminology.</p>
<p>We (SlicerMorph) will take a crack at vertebrate skeletal terms as a list as a separate effort, but given the clinical imaging focus of Slicer, I thought a more complete human terms would be necessary to include from get go.</p>

---

## Post #10 by @juanmaverde (2023-01-23 05:34 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a> and <span class="mention">@all</span>, happy to see that there’s people around understanding the value of terminology as a way to improve communication. I have been worked in the field of Gross Anatomy for the last 15 years, and I would strongly suggest (and will be happy to support) to follow the last version of “<em>Terminologia Anatomica</em>” <a href="https://fipat.library.dal.ca/TA2/" rel="noopener nofollow ugc">source</a>. It addresses miscommunication problems through the implementation of common terms based on ~clear rules and practices. Hope this helps, and do not hesitate to ping me in case you want/need details/support.</p>

---

## Post #11 by @cpinter (2023-01-23 10:08 UTC)

<p>I cannot comment on the incompleteness of the larger terminology. I also noticed that some basic looking objects are missing.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<ul>
<li><strong>Segment renaming doesn’t encourage terminology usage</strong>. Currently terminology only pops up if the color of a segment is clicked. Since it is possible to rename the segment in the terminology module, I would suggest double clicking the segment name also brings the terminology window, with the Name field activated.</li>
</ul>
</blockquote>
</aside>
<p>We have talked about this earlier (with <a class="mention" href="/u/lassoan">@lassoan</a> I think), but then haven’t taken any further steps. It would make sense to use the terminology selector for renaming, I agree.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p><strong>There are bugs in the behavior:</strong> Create an empty segment, double click color to bring the terminology window, search for Frontal and assign it and done, notice that even though Frontal is assigned a yellowish brown. The color shows up as gray.</p>
</blockquote>
</aside>
<p>I noticed this as well, that the colors turn grey sometimes (like exactly in a comment I sent to you just now, coincidentally with one of these very terms). This seems to be a bug simply that needs to be fixed.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I am also confused how these two panel supposed to work together. For example, if you search for sphenoid in the left panel no result is returned.</p>
</blockquote>
</aside>
<p>The documentation helps here I think.<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/terminologies.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/terminologies.html</a></p>
<p>The right panel is to give an “anatomic context” to generic items like cyst or mass. You can specify the body part where it appears. At least this is how I understood the basic idea.</p>

---

## Post #12 by @muratmaga (2023-01-23 16:05 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="11" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>The documentation helps here I think.<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/terminologies.html">https://slicer.readthedocs.io/en/latest/user_guide/modules/terminologies.html </a></p>
<p>The right panel is to give an “anatomic context” to generic items like cyst or mass. You can specify the body part where it appears. At least this is how I understood the basic idea.</p>
</blockquote>
</aside>
<p>Interesting. I read it but didn’t understand. I thought it is from higher organization to lower organization (systems on the left, specific names/organs on the right).</p>

---

## Post #13 by @cpinter (2023-01-24 10:28 UTC)

<p>Yes it is a bit confusing, because there is the terminology context, and the anatomic context in its separate json file. In terminology you have categories and within them types (so this part of the higher to lower organization stands). Certain categories allow specifying anatomic context, while others don’t (like optic lens only can occur in a specific place, unlike a tumor where you can and should give more details about where it is). This is stored in the <code>showAnatomy</code> tag of the category element.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff45a93ecea1e8d85e2dc969ab58ad732dbd2cdb.png" data-download-href="/uploads/short-url/Aqf0cm2EoBH08OX8EwppNM8aNOb.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff45a93ecea1e8d85e2dc969ab58ad732dbd2cdb_2_284x500.png" alt="image" data-base62-sha1="Aqf0cm2EoBH08OX8EwppNM8aNOb" width="284" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff45a93ecea1e8d85e2dc969ab58ad732dbd2cdb_2_284x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff45a93ecea1e8d85e2dc969ab58ad732dbd2cdb_2_426x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff45a93ecea1e8d85e2dc969ab58ad732dbd2cdb_2_568x1000.png 2x" data-dominant-color="1D1D23"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">615×1082 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As you see in the Slicer general anatomy list (I think btw this is a typo instead of generic which is the name of the corresponding color table), we have Tissue with show anatomy on, Anatomical Structure (off), Physical object (on), Morphologically Altered Structure (on), and Body Substance (off). So for Tissue, Physical object, and Morphologically Altered Structure you can specify the anatomic region, which I think makes sense.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="12" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I read it but didn’t understand</p>
</blockquote>
</aside>
<p>Suggestions for improvements in the documentation are welcome if you have any concrete ideas how to make it more understandable.</p>

---

## Post #14 by @muratmaga (2023-01-26 00:17 UTC)

<p>Looks like instead of one grand terminology for skeletal terms  for all vertebrates, we will probably opt out to organize for each class of vertebrates (mammals, birds, lizards/snakes etc) separately…</p>
<aside class="quote no-group" data-username="cpinter" data-post="13" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>As you see in the Slicer general anatomy list (I think btw this is a typo instead of generic which is the name of the corresponding color table), we have Tissue with show anatomy on</p>
</blockquote>
</aside>
<p>For example, I am compiling a small list for lizards and snakes as a test in this manner:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/513524b109b9317b72aa300db3c6b6685b7e280c.png" data-download-href="/uploads/short-url/bAox7iOH7K0M6FsflqcKnBnGbHS.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/513524b109b9317b72aa300db3c6b6685b7e280c_2_413x500.png" alt="image" data-base62-sha1="bAox7iOH7K0M6FsflqcKnBnGbHS" width="413" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/513524b109b9317b72aa300db3c6b6685b7e280c_2_413x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/513524b109b9317b72aa300db3c6b6685b7e280c_2_619x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/513524b109b9317b72aa300db3c6b6685b7e280c_2_826x1000.png 2x" data-dominant-color="CFCBC5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1119×1352 65.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So if I understand you correctly, my <strong>Lower Jaw</strong>, <strong>Braincase</strong>, <strong>Splanchnocranium</strong>, <strong>Forelimb</strong>, <strong>Vertebral Column</strong> are going to be equivalent of the Tissue, Anatomical Structure, Physical categories (so that I can turn them on/off as I choose). But I am still somewhat unclear where the terms associated with each of those categories go. Is the under the Type part that’s collapsed in your screenshot, or is a separate json file?</p>
<p>Finally, do you have tool to build the json file correctly, or have a custom script?</p>

---

## Post #15 by @cpinter (2023-01-26 15:58 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="14" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>So if I understand you correctly, my <strong>Lower Jaw</strong>, <strong>Braincase</strong>, <strong>Splanchnocranium</strong>, <strong>Forelimb</strong>, <strong>Vertebral Column</strong> are going to be equivalent of the Tissue, Anatomical Structure, Physical categories (so that I can turn them on/off as I choose)</p>
</blockquote>
</aside>
<p>Maybe I misunderstand the purpose of these terms but I think they should be types.<br>
You can create a separate terminology json file (i.e. context) for each animal, but you can create one and organize them into categories.<br>
Just for clarity in the expanded terminology widget the left column is category, middle one is type (with an optional modifier such as Left/Right), and the right one is anatomic context, enabled for the categories that have this flag on.</p>
<p>The anatomic context is independent of the terminology and is a different json file.</p>
<p>What I do personally for special cases where the main list does not cover the needs (cardiac, dental) is that I create a terminology context where I have just one category and within it all the types I need. Actually in the cardiac case we have multiple contexts for the different pediatric anatomy scenarios that may occur (see these as examples <a href="https://github.com/SlicerHeart/SlicerHeart/tree/master/ValveAnnulusAnalysis/Resources">here</a>). I hope this helps.</p>

---

## Post #16 by @muratmaga (2023-01-26 22:39 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="15" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>What I do personally for special cases where the main list does not cover the needs (cardiac, dental) is that I create a terminology context where I have just one category and within it all the types I need.</p>
</blockquote>
</aside>
<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a>. I am worried that a single category for all skeletal elements will be too long (100-300 depending on the organism). That;s why I am trying to create multiple categories for anatomical region.</p>
<p>I actually managed to generate valid JSON file (as indicated for the DCMQI validator), and can load it into Slicer, but for some reason contents of the 2nd category (Forelimb), doesn’t get displayed.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af4e58d1231828fafcdad9b55447d28b7e820e48.png" data-download-href="/uploads/short-url/p0PpIMxPmIMyDTll6ynyLIKf8XS.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af4e58d1231828fafcdad9b55447d28b7e820e48_2_690x266.png" alt="image" data-base62-sha1="p0PpIMxPmIMyDTll6ynyLIKf8XS" width="690" height="266" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af4e58d1231828fafcdad9b55447d28b7e820e48_2_690x266.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af4e58d1231828fafcdad9b55447d28b7e820e48.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af4e58d1231828fafcdad9b55447d28b7e820e48.png 2x" data-dominant-color="DDE8EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">905×349 15.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can find the JSON file here, if it helps: <a href="https://github.com/muratmaga/terms/blob/main/Murat.json">https://github.com/muratmaga/terms/blob/main/Murat.json</a></p>

---

## Post #17 by @cpinter (2023-02-01 12:22 UTC)

<p>I can look at it next week. In the meantime please double check that the IDs (codeValue) are unique.</p>

---

## Post #18 by @muratmaga (2023-02-01 16:05 UTC)

<p>That was the issue, thank you!</p>

---

## Post #19 by @muratmaga (2023-05-02 20:44 UTC)

<p>We have a python script that takes in a table like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dfbcc2b6e43b46049d6eefc61d6a1f2bbe5640e.png" data-download-href="/uploads/short-url/8QkBadSy5ulU9E3gbix608JpHhY.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dfbcc2b6e43b46049d6eefc61d6a1f2bbe5640e.png" alt="image" data-base62-sha1="8QkBadSy5ulU9E3gbix608JpHhY" width="690" height="328" data-dominant-color="F1F0EB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">716×341 30.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>and converts to a valid json that can be imported into terminologies</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/749df5c8864f207faea3ea2e05ca4855539b33a0.png" alt="image" data-base62-sha1="gDDOuXEmHQPNOIyvPoXWDjMr9gk" width="607" height="356"></p>
<p>We are facing an issue with elements that has L and R modifiers. If en element has left and right modifiers specified, the "no type modifier’ state always shows as a gray box.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e14caaab6e35f1dc84513357587e978c064a8ac7.png" alt="image" data-base62-sha1="w95GGpl1BbJyMCnFIUIPXtxvPSL" width="607" height="350"></p>
<p>While designated colors are shown for Left modifier, Right modifier. A possible solution to this is to have a third state “L &amp; R modifiers”, and designated color indeed shows up. Although this is less than ideal solution.</p>
<p>I know this is not a bug with our own JSON file, because the issue is there with the terminologies provided by Slicer as well (e.g., from 3D Slicer general anatomy list, choose anatomical object and navigate to Frontal Bone. You can see that No type modifier state is grayed, as opposed to brownish yellow color it is being shown).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f5633b68111874b2724aedef327576af4ae794b.png" alt="image" data-base62-sha1="4tduhT7L3F3uvWTW7t7HDwRKR1p" width="600" height="348"></p>
<p>Is this a restriction of the JSON schema or a bug in the terminologies module?</p>

---

## Post #20 by @cpinter (2023-05-04 08:38 UTC)

<p>I don’t understand the problem. In the screenshots the “No type modifier” combobox seems enabled.</p>
<p>When I do what you describe in Slicer, I can select the modifier without problems.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19681406bb8c424ef508bc4f18167866f56c6c24.png" alt="image" data-base62-sha1="3CKVfiL6tsUTfMStVjVpP7lcI0A" width="558" height="406"></p>
<p>Maybe it’s a confusion about the meaning of “No type modifier”. It means that none is currently selected. We want to allow the user to not select the modifier and leave it empty.</p>

---

## Post #21 by @muratmaga (2023-05-04 14:41 UTC)

<p>Hi Csaba. The issue is the color. İf you  proceed with no modifier state and assign this term to segment, you will get gray color (wrong) as opposed to yellow (correct one). İt is. About hard to see in the screenshot with the modifier drop down obscuring the actual color at the bottom, but try and you will see.</p>

---

## Post #22 by @muratmaga (2023-05-09 16:51 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a> any suggestions whether this is a bug or an intended behavior?</p>

---

## Post #23 by @lassoan (2023-05-09 18:38 UTC)

<p>Probably what happened is that in the first implementation selection of a modifier was enforced. Later this limitation was relaxed and the no “No type mofidier” option was added, but the change was not consistently made throughout the code. In summary, I think this is a bug. When no modifier is chosen then the basic, non-modified properties should be used.</p>

---

## Post #24 by @cpinter (2023-05-15 12:33 UTC)

<p>I was just about to add the bug in the issue tracker with all the details, but when looking for the color specified in the json file, I found that no color is specified for the non-modified type. So this is a problem with the json terminology, and not the code (at least considering this example).</p>
<p>See here</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Terminologies/Resources/SegmentationCategoryTypeModifier-SlicerGeneralAnatomy.json#L1547-L1590">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Terminologies/Resources/SegmentationCategoryTypeModifier-SlicerGeneralAnatomy.json#L1547-L1590" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Terminologies/Resources/SegmentationCategoryTypeModifier-SlicerGeneralAnatomy.json#L1547-L1590" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Modules/Loadable/Terminologies/Resources/SegmentationCategoryTypeModifier-SlicerGeneralAnatomy.json#L1547-L1590</a></h4>



    <pre class="onebox"><code class="lang-json">
      <ol class="start lines" start="1547" style="counter-reset: li-counter 1546 ;">
          <li>{</li>
          <li>  "contextGroupName": "Craniofacial Anatomic Regions",</li>
          <li>  "cid": "4028",</li>
          <li>  "CodeMeaning": "Frontal bone",</li>
          <li>  "CodingSchemeDesignator": "SCT",</li>
          <li>  "UMLSConceptUID": "C0016732",</li>
          <li>  "CodeValue": "74872008",</li>
          <li>  "Modifier": [</li>
          <li>    {</li>
          <li>      "recommendedDisplayRGBValue": [</li>
          <li>        203,</li>
          <li>        179,</li>
          <li>        77</li>
          <li>      ],</li>
          <li>      "cid": "244",</li>
          <li>      "CodingSchemeDesignator": "SCT",</li>
          <li>      "3dSlicerLabel": "right frontal bone",</li>
          <li>      "CodeValue": "24028007",</li>
          <li>      "UMLSConceptUID": "C0205090",</li>
          <li>      "CodeMeaning": "Right",</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Terminologies/Resources/SegmentationCategoryTypeModifier-SlicerGeneralAnatomy.json#L1547-L1590" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
No <code>recommendedDisplayRGBValue</code> tag exists for the non-modified type, only its <code>Modified</code> children.</p>

---

## Post #25 by @muratmaga (2023-05-15 14:29 UTC)

<p>That’s what I was afraid. We tried decorating the Json with recommendedDisplayRGBValue for unmodified state (so just before the modifier group), but that didn’t have an effect either…</p>

---

## Post #26 by @cpinter (2023-05-15 14:45 UTC)

<p>You’re right. I just tried it too so it seems to be a real bug. I added an issue</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6972">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6972" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6972" target="_blank" rel="noopener">Correctly handle non-modified terminology type properties</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-05-15" data-time="14:45:39" data-timezone="UTC">02:45PM - 15 May 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/cpinter" target="_blank" rel="noopener">
          <img alt="cpinter" src="https://avatars.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
          cpinter
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

If selecting "No type modifier" for a terminology type that has mo<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">difiers, then the non-modified properties (e.g. color) should be correctly used instead of leaving them undefined/invalid.

See details https://discourse.slicer.org/t/terminologies-questions/27384/20

## Steps to reproduce

First, need to edit the terminology json to specify a color for the "non-modified" type. For example add this
```
            "recommendedDisplayRGBValue": [
              203,
              179,
              77
            ],
```
above this line
https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Terminologies/Resources/SegmentationCategoryTypeModifier-SlicerGeneralAnatomy.json#L1554
(the file can be found in Windows Slicer installations here: `c:\Users\[UserName]\AppData\Local\slicer.org\Slicer 5.3.0-2023-05-14\share\Slicer-5.3\qt-loadable-modules\Terminologies\SegmentationCategoryTypeModifier-SlicerGeneralAnatomy.term.json`)

* Load TinyPatient sample data (need to have Developer mode enabled)
* Go to Data module
* Double-click color of the `Body_Contour` segment
* Select `Frontal bone` terminology type

## Expected behavior

Color should be yellow instead of the undefined gray.

## Environment
- Slicer version: Slicer 5.3.0-2023-05-14
- Operating system: Windows 11</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #27 by @cpinter (2023-05-15 14:52 UTC)

<p>But even if we fix this, the colors will need to be added to the JSONs. Unless we define some heuristic behavior, like use the color of the first modifier if not specified in the basic type.</p>

---

## Post #28 by @smrolfe (2023-05-15 16:32 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="27" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Unless we define some heuristic behavior, like use the color of the first modifier if not specified in the basic type</p>
</blockquote>
</aside>
<p>I tested a version that does this and think this behavior makes sense. <a class="mention" href="/u/muratmaga">@muratmaga</a> would you agree?</p>
<p>I noticed that if the color selector is used to pick a new color, that color persists when you move to other modifiers/types. Is this expected behavior?</p>

---

## Post #29 by @muratmaga (2023-05-15 16:42 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="28" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>I tested a version that does this and think this behavior makes sense. <a class="mention" href="/u/muratmaga">@muratmaga</a> would you agree?</p>
</blockquote>
</aside>
<p>For our use cases, this is definitely an acceptable behavior. Alternatively, since we will not be using Slicer’s DICOM terminology and will be generating our custom JSON, decorating the no modifier state with proper RGB codes is also an option for us.</p>
<aside class="quote no-group" data-username="smrolfe" data-post="28" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>I noticed that if the color selector is used to pick a new color, that color persists when you move to other modifiers/types. Is this expected behavior?</p>
</blockquote>
</aside>
<p>I think that’s a bug too. Can’t imagine that being a default behavior.</p>

---

## Post #30 by @smrolfe (2023-05-16 00:54 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="29" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>For our use cases, this is definitely an acceptable behavior.</p>
</blockquote>
</aside>
<p>This color of the first modifier is also what is currently displayed in the property types viewer.</p>
<p>I have created a pull request with this change here: <a href="https://github.com/Slicer/Slicer/pull/6973/commits/94e80a3d304c39176660ad55ade12b509c909f50" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/pull/6973/commits/94e80a3d304c39176660ad55ade12b509c909f50</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/beb88b4f5c209cebd0877af3361ab07b01531f36.png" data-download-href="/uploads/short-url/rdc6pJ2gEE0O0ON944hjZTgQcfA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/beb88b4f5c209cebd0877af3361ab07b01531f36_2_690x452.png" alt="image" data-base62-sha1="rdc6pJ2gEE0O0ON944hjZTgQcfA" width="690" height="452" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/beb88b4f5c209cebd0877af3361ab07b01531f36_2_690x452.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/beb88b4f5c209cebd0877af3361ab07b01531f36_2_1035x678.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/beb88b4f5c209cebd0877af3361ab07b01531f36_2_1380x904.png 2x" data-dominant-color="E8E8E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1746×1144 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #31 by @cpinter (2023-05-16 12:01 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="28" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>I noticed that if the color selector is used to pick a new color, that color persists when you move to other modifiers/types. Is this expected behavior?</p>
</blockquote>
</aside>
<p>Yes, this is a feature. See attribute <code>ColorAutoGenerated</code> (<a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Terminologies/Widgets/qSlicerTerminologyNavigatorWidget.cxx#L1739-L1741">https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Terminologies/Widgets/qSlicerTerminologyNavigatorWidget.cxx#L1739-L1741</a>), and same concept for manually edited name (so that once the user spends time manually specifying a property it is not lost when you change the terminology type).</p>
<aside class="quote no-group" data-username="muratmaga" data-post="29" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I think that’s a bug too. Can’t imagine that being a default behavior.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> please confirm.</p>

---

## Post #32 by @muratmaga (2023-05-16 16:21 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="31" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Yes, this is a feature. See attribute <code>ColorAutoGenerated</code></p>
</blockquote>
</aside>
<p>But that’s not how most other properties work in Slicer (like color tables, volume property), in my experience. If you want to make a change, you either make a copy or save it to the disk.</p>
<p>Anyways, I think the button on lower right reverts the state to original color, so it is not a big issue, but I found the behavior a bit awkward first.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/2752fbe2daf30547e5b052e81427f26fd7e86611.png" data-download-href="/uploads/short-url/5BSpDS1IYTdW1HQpN1waJa4pnKp.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/2752fbe2daf30547e5b052e81427f26fd7e86611_2_690x440.png" alt="image" data-base62-sha1="5BSpDS1IYTdW1HQpN1waJa4pnKp" width="690" height="440" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/2752fbe2daf30547e5b052e81427f26fd7e86611_2_690x440.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/2752fbe2daf30547e5b052e81427f26fd7e86611.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/2752fbe2daf30547e5b052e81427f26fd7e86611.png 2x" data-dominant-color="E3E3E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1012×646 51.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #33 by @cpinter (2023-05-17 09:18 UTC)

<p>Yes, the small reset buttons also reset this property, and the manually fixed color will again change to the one defined by the current type. I don’t remember the details anymore, but I do remember that we struggled implementing this in a way that it was robust. We wanted to allow the user to set custom color/name, and also to be able to reset the color/name to the one defined by the type.</p>
<p>I wonder if we change behavior so that the <code>*AutoGenerated</code> properties are reset on changing the type (or modifier), would it cause any issues or not. As I understand this is the main issue right? For especially the name, it probably does not make sense to keep the user-defined one if the user realized they chose a wrong type and change the selection.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> do you have anything to add?</p>

---

## Post #34 by @lassoan (2023-05-17 16:29 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="30" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>This color of the first modifier is also what is currently displayed in the property types viewer.</p>
</blockquote>
</aside>
<p>It would be more appropriate to show default/gray color than copying the color of the first modifier. It should be no problem to add the missing colors to the json files.</p>
<aside class="quote no-group quote-modified" data-username="cpinter" data-post="31" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<aside class="quote no-group" data-username="muratmaga" data-post="29" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I think that’s a bug too. Can’t imagine that being a default behavior.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> please confirm.</p>
</blockquote>
</aside>
<p>If you manually pick a non-default color then it could be very frustrating to lose it. Manually set color and segment name is kept until you reset to default. We could make the behavior more obvious by displaying an “override” checkbox but then it would mean that the users need to do one more click to modify the name or color.</p>
<hr>
<p>Regarding the segment renaming issue (<a href="https://github.com/Slicer/Slicer/issues/6975" class="inline-onebox">Rename segments via Terminologies window · Issue #6975 · Slicer/Slicer · GitHub</a>), it seems that <a class="mention" href="/u/muratmaga">@muratmaga</a> suggests that we should open the terminology selector when double-clicking the name column. I think this could make sense, but then we would need to make it easier to add a new term (and probably to allow searching for terms in all the terminologies, to avoid re-adding a term just because it is defined in another terminology). Implementation might not be trivial, because we allow renaming in the subject hierarchy tree, too (we would need to define a mechanism that would control when name must be set via terminology).</p>

---

## Post #35 by @muratmaga (2023-05-18 04:14 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="34" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>but then we would need to make it easier to add a new term (and probably to allow searching for terms in all the terminologies, to avoid re-adding a term just because it is defined in another terminology). I</p>
</blockquote>
</aside>
<p>I am not sure I am following this. While I agree it would be nice to add new terms/colors to custom terminologies for people to reuse their own terms, I don’t think this is strictly necessary for renaming behavior I mentioned. Currently, if I click the color button next to the segment name, in the pop up terminology button, name comes automatically editable. All it is necessary is perhaps focus on the name field and highlight it.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecd7d4c1f1b094d43e596c27844a6ebb468e8830.png" alt="image" data-base62-sha1="xNd68wszrvRupo18XxiCaD1W6tO" width="558" height="406"></p>
<p>As for custom terminology, perhaps a button like “add to custom terminology”, and confirm name color selection and have them define file to write?</p>

---

## Post #36 by @cpinter (2023-05-22 09:30 UTC)

<p>Highlighting the name field should not be a problem. Showing the terminology picker when renaming would be a major change and I’m sure many people wouldn’t like it (including myself, I very often rename nodes and having to go through the terminology picker would be very heavy for a simple rename).</p>
<p>Should we maybe discuss this tomorrow at the developer hangout? Unless the agenda is full or anything, in which case we can set another meeting.</p>

---

## Post #37 by @muratmaga (2023-05-22 22:33 UTC)

<p>İ will try to make the call, but that was just a suggestion to build awareness for terminology module and encourage its usage.</p>

---

## Post #38 by @lassoan (2023-05-23 03:30 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="36" data-topic="27384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I very often rename nodes and having to go through the terminology picker would be very heavy for a simple rename</p>
</blockquote>
</aside>
<p>Exactly. That’s why I wrote that if we do something like this then we would need to make it much easier to add a new name (it should not require more clicks than by simply typing a new name). It would be great if we could pull it off, because then terminologies would be used much more frequently. However, I don’t know how we would name temporary segments, identify specific segments (e.g., tumor 1, tumor 2,…).</p>

---
