# New Arabic translation of 3D Slicer

**Topic ID**: 31665
**Date**: 2023-09-12
**URL**: https://discourse.slicer.org/t/new-arabic-translation-of-3d-slicer/31665

---

## Post #1 by @Shadin_Omari (2023-09-12 22:20 UTC)

<p>Hello, I’ve finished translating the project from English to Arabic language,  the 3D Slicer…now what’s next, how are you going to pay for me??</p>

---

## Post #2 by @lassoan (2023-09-12 22:37 UTC)

<p>Thank you for your contribution! We have noticed the new translation and just asked our Arabic-speaking colleagues to check it out. It is good that you showed up here because we do not get any contact information via Weblate.</p>
<p>How have you translated it? Using fully automatic translator? Have you reviewed the translations?</p>
<p>While we were translating to other languages, we have run into <em>many</em> difficult questions about what is the best way to translate certain terms and often found that we need to improve the original English source text instead of doing a literal translation. Have you run into similar issues?</p>
<p>Some modules, especially CLI modules of low-level processing algorithms contain information that is only understandable by domain experts. How have you translated such strings?</p>
<p>Have you checked the “Arabic (Saudi Arabia)” translation that our collaborators in Senegal has been working on? Have you found it useful? How does it compare to your translation?</p>
<aside class="quote no-group" data-username="Shadin_Omari" data-post="1" data-topic="31665">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shadin_omari/48/67513_2.png" class="avatar"> Shadin_Omari:</div>
<blockquote>
<p>how are you going to pay for me??</p>
</blockquote>
</aside>
<p>We are grateful for your work and we’ll pay you the same amount that you’ve paid for the development of Slicer. Thank you!</p>

---

## Post #3 by @lassoan (2023-09-19 16:25 UTC)

<p><a class="mention" href="/u/shadin_omari">@Shadin_Omari</a> We have noticed that you have translated Python string placeholders (that are replaced by actual values or text at runtime) to Arabic. For example: <code>Checking {what}</code> was translated to <code>فحص (ماذا )</code>, while the correct translation is <code>(what) فحص</code>. If placeholders are not found in the translated text then the Python script execution stops and the software does not work correctly. For example, currently you cannot load a DICOM file if your Arabic translation is used.</p>
<p>Fortunately, it is easy to fix this. If you open <a href="https://hosted.weblate.org/translate/3d-slicer/3d-slicer/ar/?q=check:python_brace_format">this URL</a> then you will get a list of all strings where placeholders got removed so you can quickly go through them and fix them. Thank you!</p>

---

## Post #4 by @Shadin_Omari (2023-10-01 13:20 UTC)

<p>Hello sir<br>
I’ve just reviewed the translation,  and did what you told me about, i’ve corrected them, i think now all the strings have been translated and its 100% for all of them…<br>
Is that correct??</p>

---

## Post #5 by @lassoan (2023-10-02 02:49 UTC)

<p>Correct, you have completed the translation for both Slicer core (<a href="https://hosted.weblate.org/projects/3d-slicer/3d-slicer/ar/">Slicer</a> and <a href="https://hosted.weblate.org/projects/3d-slicer/ctk/ar/">CTK</a> components). There are a handful of strings with failing checks in each component that you might want to check.</p>
<p>ow have you translated it? Using fully automatic translator? Have you reviewed the translations?</p>
<p>While we were translating to other languages, we have run into <em>many</em> difficult questions about what is the best way to translate certain terms and often found that we need to improve the original English source text instead of doing a literal translation. Have you run into similar issues?</p>
<p>Some modules, especially CLI modules of low-level processing algorithms contain information that is only understandable by domain experts. How have you translated such strings?</p>
<p>Have you checked the “Arabic (Saudi Arabia)” translation that our collaborators in Senegal has been working on? Have you found it useful? How does it compare to your translation?</p>

---

## Post #6 by @Shadin_Omari (2023-10-02 13:19 UTC)

<p>Good afternoon sir…<br>
Now i think I’ve completed all of the strings, right? It was a completely new experience for me …<br>
Anything left?? And what’s the next step?</p>

---

## Post #7 by @Shadin_Omari (2023-10-03 19:46 UTC)

<p>Hello sir<br>
Did you read my last message???</p>

---

## Post #8 by @lassoan (2023-10-03 20:23 UTC)

<p>For me, as a maintainer of 3D Slicer, it would be important to know how <a href="https://hosted.weblate.org/projects/3d-slicer/3d-slicer/ar/">your Arabic translation</a> compares to the <a href="https://hosted.weblate.org/projects/3d-slicer/3d-slicer/ar_SA/">other Arabic translation</a>. Keeping two separate translations would increase the maintenance efforts and in the long term it would result in lower quality translations. Please answer the following questions so that I can have a better idea of what the translation file contains and whether it should be consolidated with the other translation (and if yes, how).</p>
<p>While we were translating to other languages, we have run into <em>many</em> difficult questions about what is the best way to translate certain terms and often found that we need to improve the original English source text instead of doing a literal translation. Have you run into similar issues?</p>
<p>Some modules, especially CLI modules of low-level processing algorithms contain information that is only understandable by domain experts. How have you translated such strings?</p>
<p>Have you checked the “Arabic (Saudi Arabia)” translation that our collaborators in Senegal has been working on? Have you found it useful? How does it compare to your translation?</p>

---

## Post #9 by @Shadin_Omari (2023-10-03 20:58 UTC)

<p>Well, i found some of the english  terms need to be improved so i dont have to translate them literally,  and about the Arabic (Saudi Arabia), i didnt read all of files, i just had a quick look,  and founf it useful that helped me to translate some strings, also i used the gogle translation  and asked a friend for help in some other strings that is only understandable by domain experts,  but still i cant compare the Arabic (Saudi Arabia) to mine .</p>

---

## Post #10 by @Shadin_Omari (2023-10-04 11:25 UTC)

<p>I woul like to add something,  im a native Arabic Speaker,   and i have a bachelor degree in English language</p>

---

## Post #11 by @Shadin_Omari (2023-10-08 19:30 UTC)

<p>??? Any answer??,<br>
Have you read my messages?</p>

---

## Post #12 by @rbumm (2023-10-08 22:54 UTC)

<p>I think the way to go is using AI for that.<br>
I just created my second medical brain in <a href="https://www.quivr.app/" rel="noopener nofollow ugc">quivr</a> and can now chat with it in any language, e.g Chinese or Russian or  Arabic (peace), on the webpage.<br>
Ask English question on my German contents, and translate.<br>
It has a growing Slicer brain, too.</p>

---

## Post #13 by @lassoan (2023-10-09 05:35 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> Thanks for the information, I would be ld be interested interested to see hear more about things that you can do.</p>
<p>Machine translation has definitely plays an important role. <a class="mention" href="/u/shadin_omari">@Shadin_Omari</a> seems to have used Google Translate, while the CZI Africa team is using Weblate’s built-in machine translation suggestions (from Microsoft, Google, and a few other engines) as a starting point for all translations.</p>
<p>However, machine translations are still much, much lower quality than human translations. The choice of words is often suboptimal, but this is not the biggest problem. The most serious issue is that often we realize while we are translating that the original text, or even the software  appearance or behavior needs to be changed if we want to have a good translation that users can understand.</p>
<p><a class="mention" href="/u/shadin_omari">@Shadin_Omari</a> I appreciate your continued interest in the project and can understand that you are anxiously waiting for my answers. However, the tone of some of your messages (e.g., <code>??? Any answer??</code>) is not compatible with the friendly conversations that we are trying to have on this forum. You can certainly ask again if you don’t get a timely answer, but try to appear less demanding (drop the multiple question marks, etc.) and also describe what you did in the meantime on your side or any other potentially relevant details.</p>
<p>I’m not sure about next steps with the two Arabic translations. One translation would be much easier to maintain, but if they serve different purpose then we might keep both. Do you have any suggestions?</p>

---

## Post #14 by @Shadin_Omari (2023-10-09 09:59 UTC)

<p>Sir, please accept my apologies in case you thought my tone wasn’t compatible with the friendly conversations that we are trying to have on this forum… ( i had to translate the word " compatible " on google translation to make sure of right meaning) thats why i used google translation to do this project, to choose the exact correct meaning of the words, I didn’t use it randomly and just copied and pasted the  translation,  plus I appreciate your continued efforts to master your work and make sure you use the right words.<br>
Sir, i usually work as a translator, i mean in daily life, i translate  and proofread books for universities, also master’s and doctoral theses, and i use Google translate as an assistan, since English is my second language, to choose the most accurate words.<br>
I mean in case you liked my translation,  i will be honored to translate more projects with you …</p>

---

## Post #15 by @lassoan (2023-10-09 11:51 UTC)

<p>Before translating more projects, it would be nice to somehow consolidate the two Arabic translations of Slicer. That would allow you to work together with the other translators. It would also reduce the work to n the future, as if we have two separate translations then after each change in the Slicer user interface the new/changed words would need to be translated twice.</p>
<p>Hiw do you think the two Arabic translations of Slicer could be merged?</p>

---

## Post #16 by @rbumm (2023-10-09 14:46 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> you can go <a href="https://www.quivr.app" rel="noopener nofollow ugc">https://www.quivr.app</a>, create a login, and subscribe to the 3D Slicer public brain. It contains the slicer.pdf, the redthedocs.pdf, and the publication numbers.</p>

---

## Post #17 by @Shadin_Omari (2023-10-17 10:36 UTC)

<p>Good Evening <a class="mention" href="/u/lassoan">@lassoan</a><br>
Sorry for being late…</p>
<p>What do you mean in consolidating the two Arabic translations? If you mean something technical,  then i would like to apologize since im not an expert in computer science…</p>
<p>Still you didn’t find out what the next step will be, so you will not pay for me??</p>

---

## Post #18 by @pieper (2023-10-17 14:00 UTC)

<aside class="quote no-group" data-username="Shadin_Omari" data-post="17" data-topic="31665">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shadin_omari/48/67513_2.png" class="avatar"> Shadin_Omari:</div>
<blockquote>
<p>Still you didn’t find out what the next step will be, so you will not pay for me??</p>
</blockquote>
</aside>
<p>Dear <a class="mention" href="/u/shadin_omari">@Shadin_Omari</a> - we appreciate your interest and efforts.  It’s important to be clear that Slicer is a free software project supported by people to want to make it available globally.  As far as I know nobody offered to pay for translations so you should not expect payment.</p>
<aside class="quote no-group" data-username="Shadin_Omari" data-post="17" data-topic="31665">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shadin_omari/48/67513_2.png" class="avatar"> Shadin_Omari:</div>
<blockquote>
<p>What do you mean in consolidating the two Arabic translations? If you mean something technical, then i would like to apologize since im not an expert in computer science…</p>
</blockquote>
</aside>
<p>What we would like is to have one Arabic translation of the highest possible quality so that everyone can benefit and work together to improve it.  That would mean reviewing the two and suggesting changes to the other so that we have the best of both.</p>

---

## Post #19 by @Shadin_Omari (2023-10-19 10:08 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/2922e2b0c59a0ca7a59419e6ec5954fa4c5d8d53.jpeg" data-download-href="/uploads/short-url/5RUjIXHd23WX7LzgEMzHUTQvWqT.jpeg?dl=1" title="Screenshot_20231019-130637_Chrome" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2922e2b0c59a0ca7a59419e6ec5954fa4c5d8d53_2_225x500.jpeg" alt="Screenshot_20231019-130637_Chrome" data-base62-sha1="5RUjIXHd23WX7LzgEMzHUTQvWqT" width="225" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2922e2b0c59a0ca7a59419e6ec5954fa4c5d8d53_2_225x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2922e2b0c59a0ca7a59419e6ec5954fa4c5d8d53_2_337x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2922e2b0c59a0ca7a59419e6ec5954fa4c5d8d53_2_450x1000.jpeg 2x" data-dominant-color="EEEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20231019-130637_Chrome</span><span class="informations">720×1600 209 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #20 by @pieper (2023-10-19 14:31 UTC)

<p><a class="mention" href="/u/shadin_omari">@Shadin_Omari</a> thank you for sending that screenshot.  I’m sorry if it was misinterpreted, but I interpret <a class="mention" href="/u/lassoan">@lassoan</a> as being sarcastic in that post.  Nobody pays to use Slicer, so we are not offering payment for translations either.</p>

---

## Post #21 by @lassoan (2023-10-19 15:08 UTC)

<p>Yes, sorry if I was not clear enough. What I meant indeed was that the amount you get = the amount you paid = $0. I did not want to be sarcastic, just wanted to explain that your contribution is valuable and 3D Slicer is valuable, yet we make it available for free.</p>

---
