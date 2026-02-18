# Cannot download extension from http://slicer.kitware.com or https://extensions.slicer.org

**Topic ID**: 19798
**Date**: 2021-09-22
**URL**: https://discourse.slicer.org/t/cannot-download-extension-from-http-slicer-kitware-com-or-https-extensions-slicer-org/19798

---

## Post #1 by @Gao_Zhenyu (2021-09-22 01:02 UTC)

<p>I am working at a hospital environment. Since the hospital environment is internal, the 3d slicer cannot access to Internet. Therefore, 3D Slicer cannot download and consume extension  immediately.</p>
<p>I try to download the externsion from <a href="http://slicer.kitware.com" rel="noopener nofollow ugc">http://slicer.kitware.com</a> but this website was unused. Then I goto <a href="https://extensions.slicer.org/catalog/all/29738/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a> and hit the similar issue. I cannot download it from those websites.</p>
<p>Please, help!</p>

---

## Post #2 by @lassoan (2021-09-22 01:04 UTC)

<p>Slicer applications and all extensions are fully portable. You can download and install Slicer and extensions on any computer that has internet access, then copy the entire installation folder to another computer and everything will work.</p>
<p>Alternatively, you can use the new extension download site as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#download-extension-packages">here</a>.</p>

---

## Post #3 by @Gao_Zhenyu (2021-09-22 01:10 UTC)

<p>Thanks for the reply ! but my workmate told me he had try to copy the entire installation folder to other machine, but it doesn’t work.</p>
<p>You had memtion about <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#download-extension-packages" class="inline-onebox" rel="noopener nofollow ugc">Extensions Manager — 3D Slicer documentation</a> . I had found it a few days ago and it says I can download extension  in <a href="https://extensions.slicer.org/catalog/All/30117/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a> . But I cannot download it with chrome. (click download button did not trigger downloading)</p>

---

## Post #4 by @lassoan (2021-09-22 01:13 UTC)

<aside class="quote no-group" data-username="Gao_Zhenyu" data-post="3" data-topic="19798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gao_zhenyu/48/12494_2.png" class="avatar"> Gao_Zhenyu:</div>
<blockquote>
<p>but my workmate told me he had try to copy the entire installation folder to other machine, but it doesn’t work</p>
</blockquote>
</aside>
<p>It works. You may need to use a recent Slicer Preview Release. If you have any problems then describe what you did, what you expected to happen, and what happened instead.</p>
<aside class="quote no-group" data-username="Gao_Zhenyu" data-post="3" data-topic="19798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gao_zhenyu/48/12494_2.png" class="avatar"> Gao_Zhenyu:</div>
<blockquote>
<p>But I cannot download it with chrome. (click download button did not trigger downloading)</p>
</blockquote>
</aside>
<p>This is a known issue, you can track the progress of fixing the problem <a href="https://github.com/Slicer/Slicer/issues/5863">here</a>. You can use the new extension download site as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#download-extension-packages">here</a>.</p>

---

## Post #5 by @Gao_Zhenyu (2021-09-22 01:21 UTC)

<p>Thanks a lot! We will try again.</p>

---

## Post #6 by @muratmaga (2021-09-22 22:51 UTC)

<p>We are in a hospital environment and encountered issues installing extensions. Working with IT security, it turned out a problem with the corporate firewall (this is explained by IT to me. Review of the traffic to <a href="http://slicer-packages.kitware.com" rel="noopener nofollow ugc">slicer-packages.kitware.com</a> indicated that it was hitting the SSL inspection of the traffic. The site appears to be breaking due to the SSL inspection). They ended up implementing a SSL inspection bypass, which fixed the problem for us.</p>
<p>This may not be your issue, but at some point you may need to get your IT team involved.</p>

---
