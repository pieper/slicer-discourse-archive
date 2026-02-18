# Slicer usage in the closed commercial product

**Topic ID**: 14180
**Date**: 2020-10-21
**URL**: https://discourse.slicer.org/t/slicer-usage-in-the-closed-commercial-product/14180

---

## Post #1 by @a10227 (2020-10-21 09:25 UTC)

<p>Good day, could you please tell me, is it possible to write an extension for slicer and use it in the closed commercial product? Are there any requirements/restrictions for that?</p>
<p>I tried to figure it out myself but found several contradictions; on the one hand, <a href="https://www.slicer.org/wiki/License" rel="noopener nofollow ugc">it says that slicer is under BSD license</a>, and, as far as I understand, it allows commercial usage in the closed product. On the other hand, <a href="https://github.com/Slicer/Slicer/blob/master/License.txt" rel="noopener nofollow ugc">slicer license agreement</a> says that<br>
“You hereby grant to Brigham, with the right to sublicense, a perpetual, worldwide, non-exclusive, … license to use, reproduce, make derivative works of, display and distribute the Contribution.” (point 4)</p>
<p>“You acknowledge and agree that Brigham may incorporate your Contribution into Slicer and may make Slicer available to members of the public on an open source basis …” (point 5)</p>

---

## Post #2 by @pieper (2020-10-21 13:25 UTC)

<p>Thanks for asking, we want to be sure people have a good understanding of these points.</p>
<aside class="quote no-group" data-username="a10227" data-post="1" data-topic="14180">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/a10227/48/7657_2.png" class="avatar"> a10227:</div>
<blockquote>
<p>is it possible to write an extension for slicer and use it in the closed commercial product? Are there any requirements/restrictions for that?</p>
</blockquote>
</aside>
<p>Yes and yes.  You are free to take the Slicer code and use it in a commercial product.  When you do so, yes you are required to take total responsibility for that product to ensure it is safe and effective and meets the legal and ethical requirements of your jurisdiction, institution, or other authorities.  You also have a minor academic and copyright responsibility to mention the code you make use of, like in the About Box and in the copyright section of the documentation.</p>
<p>Note that if you use the Slicer factory machines to build and host your extension then of course it’s needs to be open source (or we wouldn’t be able to compile it!).  But you don’t need to make your extension or other re-use of Slicer code public.</p>
<aside class="quote no-group" data-username="a10227" data-post="1" data-topic="14180">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/a10227/48/7657_2.png" class="avatar"> a10227:</div>
<blockquote>
<p>“You hereby grant to Brigham, with the right to sublicense, a perpetual, worldwide, non-exclusive, … license to use, reproduce, make derivative works of, display and distribute the Contribution.” (point 4)</p>
</blockquote>
</aside>
<p>This addresses code or data contributed to the Slicer codebase itself (e.g. to the Slicer repository on github - see definition of “Contribution” in the license).  It doesn’t apply to code you keep for your own private extensions.</p>
<p>The main point here is that you hold the copyright to code you write, but when you contribute it to Slicer you agree that Brigham can share it under the same terms that it shares code contributed by Brigham employees or any other contributor.  You’ll note that the Brigham is also giving you the same rights to distribute its work under these terms.  The overall goal and result is to provide equal rights to anyone to use the code.</p>
<p>These license terms were designed explicitly to support commercialization of the Slicer codebase in support of innovative medical products that help patients (and in fact there are several examples on the market and in development).  It’s important to note that because of regulatory and reimbursement rules it’s essential that medical software be turned into commercial products in order to be integrated into routine standard of patient care.  Slicer and the license are designed to be a platform for such products.</p>
<p>Of course if you are investing resources to develop a commercial product you’ll want your own legal review of these issues.  We hope you’ll find, as several other companies have, that this is a good basis for product development.  Note we always say Slicer’s license is “BSD-style” because if practice most people can use it like BSD software.  There are some extra terms about excluding GPL code and declaiming patents on Slicer contributions that you should review carefully.  They are meant to protect everyone so I suspect they wouldn’t be a problem for you.</p>
<p>Also note that the Slicer project is careful to say that the code is “intended” for research.  This is true of the code and binaries we make available.  This does not prevent other entities from using the code with other intentions, such as intentions for clinical use (subject to the regulatory responsibilities discussed above).</p>
<p>We hope also that you’ll find the platform so beneficial to your work that you’ll help the community maintain and grow the core software so that it can support your application-specific commercial developments while at the same time helping others.</p>

---

## Post #3 by @a10227 (2020-10-21 13:41 UTC)

<p>Thank you for such a detailed answer. Could you please make sure that I understood you correctly: I can create my extension for 3D Slicer and use it in a closed commercial product; if this extension is built and hosted on my machine, it is not considered open source, and I do not have to grant any rights for this extension to other people/companies; all I have to do in this case is just place the copyright information somewhere noting I am using the code from 3D Slicer, am I right?</p>

---

## Post #4 by @pieper (2020-10-21 15:48 UTC)

<p>Yes, that sounds right to me.</p>

---

## Post #5 by @skyhsu (2020-11-12 06:33 UTC)

<p>Hello, I am very interested in this commercial product question.<br>
Please allow me to use this post to extend the ask. Thank you.</p>
<p>If  I can create my extension for 3D Slicer and use it in my mechine( just built and hosted on my machine) for  segmentation process and display in 3D space.<br>
And my mechine will connect with internal network, let 3D slicer to access database, just internal.</p>
<p>In this case, it is not considered open source, and I do not have to grant any rights for this extension to other people/companies; all I have to do is just place the copyright information somewhere noting I am using the code from 3D Slicer.<br>
Is this correct?</p>
<p>Thank you very much.</p>

---

## Post #6 by @pieper (2020-11-12 18:58 UTC)

<p>Hi <a class="mention" href="/u/skyhsu">@skyhsu</a> - yes, what you describe sounds fine.</p>
<p>To expand, code made available under the 3D Slicer license is okay to use in commercial projects even is you distribute them outside of your own machine or network.  You do not need to grant back any rights to your work if you don’t want to.</p>

---
