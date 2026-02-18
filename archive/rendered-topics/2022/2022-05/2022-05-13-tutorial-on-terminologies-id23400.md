# Tutorial on terminologies

**Topic ID**: 23400
**Date**: 2022-05-13
**URL**: https://discourse.slicer.org/t/tutorial-on-terminologies/23400

---

## Post #1 by @muratmaga (2022-05-13 05:13 UTC)

<p>How does one go about creating a custom segmentation terminology/colors and using that during the segmentation process (I.e., renaming segment_1 segment_2 with consistent names and colors)…</p>
<p>Linked sample json file in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/terminologies.html" rel="noopener nofollow ugc">terminologies documentation</a> is a bit too complex to understand.</p>
<p>Let’s say I want to make a terminology for all cranial bones (Left Nasal, Right Nasal, Occipital, Frontal so forth)</p>

---

## Post #2 by @cpinter (2022-05-13 08:29 UTC)

<p>There are simpler examples such as this: <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/ValveAnnulusAnalysis/Resources/SlicerHeartPDAVesselsCategoryTypeModifier_A_Normal.json" class="inline-onebox">SlicerHeart/SlicerHeartPDAVesselsCategoryTypeModifier_A_Normal.json at master · SlicerHeart/SlicerHeart · GitHub</a></p>
<p>Do you think it would solve the issue if we replaced one of the examples in the documentation page you linked with this? Or do you have more questions and a more comprehensive guide would be needed?</p>

---

## Post #3 by @muratmaga (2022-05-13 17:22 UTC)

<p>It is simpler, but I think a bit more guidance is needed. For example what does the nested levels means (section under “Type”), or what is the significance of Code Value field, why some are numeric and some alpha-numeric?</p>
<pre><code class="lang-auto">"Category": [
      {
        "CodeMeaning": "PDA adjacent vessels (A - Normal)",
        "CodingSchemeDesignator": "SlicerHeart",
        "CodeValue": "85756008",
        "Type": [
          {
            "CodeMeaning": "PDA",
            "CodingSchemeDesignator": "SlicerHeart",
            "CodeValue": "sh-pda-pda",
            "recommendedDisplayRGBValue": [128, 174, 128]
          },
          {
            "CodeMeaning": "Ascending aorta",
            "CodingSchemeDesignator": "SlicerHeart",
            "CodeValue": "sh-pda-ascending-aorta",
            "recommendedDisplayRGBValue": [216, 101, 79]
          },
</code></pre>

---

## Post #4 by @lassoan (2022-05-14 23:07 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="23400">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>For example what does the nested levels means (section under “Type”)</p>
</blockquote>
</aside>
<p><code>Type</code> list contains all the types you define in the file.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="23400">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>what is the significance of Code Value</p>
</blockquote>
</aside>
<p>In short:</p>
<ul>
<li><strong>coding scheme designator:</strong> specifies the terminology. For example, <code>TA2</code>, <code>FMA</code>, <code>MeSH</code>, …</li>
<li><strong>code value:</strong> specifies the identifier in that terminology. For example, <a href="https://en.wikipedia.org/wiki/Nasal_bone">identifier of <code>Nasal bone</code> in TA2 is <code>748</code></a>, so the code value is <code>748</code>.</li>
<li><strong>code meaning:</strong> human-readable string, just for convenience (for example, if an application does not know the used terminology then it can display this string) and debugging. For example, <code>nasal bone</code>.</li>
</ul>
<p>You can find detailed description of how <code>Coding scheme designator</code>, <code>Code value</code>, and <code>Code meaning</code> used in DICOM in the <a href="https://dicom.innolitics.com/ciods/general-ecg/patient-study/00101021/00080102">DICOM standard</a>.</p>
<p>Left/right can be specified using modifier. For example, for types specified using SNOMED Clinical Terms (SCT) we usually use this modifier: <code>{"CodingSchemeDesignator": "SCT", "CodeValue": "24028007", "CodeMeaning": "Right"}</code>. For TA2, you can find a convenient browser <a href="https://ta2viewer.openanatomy.org">here</a>, and according to that the <a href="https://ta2viewer.openanatomy.org/?id=7">code value of the <code>Right</code> is <code>7</code></a>.</p>

---
