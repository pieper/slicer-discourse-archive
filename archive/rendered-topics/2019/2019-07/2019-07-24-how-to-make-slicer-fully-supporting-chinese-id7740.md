# How to make Slicer fully supporting Chinese?

**Topic ID**: 7740
**Date**: 2019-07-24
**URL**: https://discourse.slicer.org/t/how-to-make-slicer-fully-supporting-chinese/7740

---

## Post #1 by @xgongx (2019-07-24 13:14 UTC)

<p>In Slicer, an user can’t rename a node with Chinese name, load a NRRD file with Chinese file name, make a comment with Chinese, save scene with Chinese characters, show Chinese characters in views. All Chinese characters in Slicer UI will be shown as “??”.</p>
<p>After reading source code, the reason of issue is that programmers used QString::toLatin() and QString::fromLatin to convert a UI input string to char* or vice versa. The two methods will convert all none Latin character to “?”. It seems the programmers has used this coding pattern for a quite long time. However, QString::toLocal8Bit() and QString::fromLocal8Bit() are better choice. This two methoda will convert none Latin character to  a multibytes character base on OS default code page.</p>
<p>To correct this problem, I wrote a compiler tool to auto detect and change hurdreds pieces of code with Latin pattern since Slicer 4.9.1 release. However, it didn’t put things right once and for all. When a new Slicer release, I have to do code scanning again.</p>
<p>So I suggest to all programmer, please don’t use toLatin/fromLatin, instead of toLocal8Bit/fromLocal8Bit. Also don’t use QString(char*), instead of fromLocal8Bit. This coding pattern will make Slicer supporting multiple languages all over world.</p>

---

## Post #2 by @cpinter (2019-07-24 13:38 UTC)

<p>This is an issue that tends to come up quite often. As you say Latin1 encoding is assumed at a number of places in Slicer, but further than that, also in CTK and other toolkits Slicer is based on. So it is major work making sure that all unicode characters are handled correctly in every place, and since there has been no explicit funding for this so far, it has not been done yet.</p>
<p>You say that you have a more-or-less working implementation for 4.9.1. I think it would be a great first step adapting it to the latest version, and creating a pull request. Since we are an open-source community, we always welcome contributions, and actually try to encourage the community to contribute in exchange for the help they are given.</p>

---

## Post #3 by @lassoan (2019-07-24 14:02 UTC)

<p>Fully agree, pull requests are welcome. It is important to submit pull requests in several steps so that each pull request can be reviewed, discussed, and merged more easily. If we get one huge pull request then it might be very hard to put it through the review process.</p>

---

## Post #4 by @pieper (2019-07-24 22:06 UTC)

<p>Hi Xiaoyan -</p>
<p>Thank you for bringing this up – we have wanted to correct this for a long time but as Csaba and Andras have pointed out, it’s a big job and there are some very tricky parts (for instance making sure that files that mix text and numbers are correctly handled by some legacy C code).  As you point out, providing guidelines for best practices for new code is a great way to start.</p>
<p>One of the biggest things we need to have is people who can test on non-US-English operating systems and data files.  It would be great if you can share the work you have done, both the source code and any generated binaries so that we can all work together on this.</p>
<p>In case you hadn’t seen it here are some links to ongoing work:</p>
<p><a href="https://na-mic.org/wiki/2011_Summer_Project_Week_Internationalization_of_Slicer" class="onebox" target="_blank" rel="nofollow noopener">https://na-mic.org/wiki/2011_Summer_Project_Week_Internationalization_of_Slicer</a></p>
<p><a href="https://discourse.slicer.org/t/slicer-internationalization/579">https://discourse.slicer.org/t/slicer-internationalization/579</a></p>
<p>Best,<br>
Steve</p>

---

## Post #6 by @xgongx (2019-07-25 02:03 UTC)

<p>Yes, it will be a 700+ pieces of code modification, huge.</p>

---

## Post #7 by @xgongx (2019-07-25 02:04 UTC)

<p>Yes, I enabled multi-bytes string support in Slicer 4.9.1. The modification included changing ‘toLatin/fromLatin’ coding pattern in Slicer and CTK code, VTK text rendering code.</p>
<p>Unfortunately, these achievements were make during my working for my ex-employer. So I can’t contribute them to community. However, I also can’t contribute code to community util March, 2020. Because I have signed the NDA with my ex-employer, he owned exclusivity IP of all my Slicer related achievements being make during one year after I quit my ex-employer company.</p>
<p>So I will contribute my code to community after March, 2020.</p>

---

## Post #8 by @xgongx (2019-07-25 02:06 UTC)

<p>Testing will be a problem. I don’t know whether community have QC team or not, but I am sure even yes, the QC team is able to only work on English language. Right?</p>

---

## Post #9 by @pieper (2019-07-25 11:52 UTC)

<p>I think testing would need to involve the community somehow - people who routinely use non-English data and operating systems.  <a class="mention" href="/u/xgongx">@xgongx</a> are you active with <a href="https://www.slicercn.com/" rel="nofollow noopener">slicercn.com</a> and / or the <a href="https://discourse.slicer.org/t/slicer-resources-in-chinese/2077">slicer wechat channel</a>?  I know of them but of course it’s hard for non-Chinese speakers to understand the conversations.</p>

---

## Post #10 by @cpinter (2019-07-25 14:27 UTC)

<aside class="quote no-group" data-username="xgongx" data-post="7" data-topic="7740">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/x/f19dbf/48.png" class="avatar"> xgongx:</div>
<blockquote>
<p>signed the NDA</p>
</blockquote>
</aside>
<p>Fair enough, thank you for the update! It is always sad if useful features that are not specific to the product/application are shielded from the community. I personally don’t think that a generic feature like this would harm a company in any way, but the companies have their cultures and experiences and expectations which we have to live with… March 2020 sounds great too <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #11 by @xgongx (2020-03-06 14:17 UTC)

<p>When I want to keep my promises to make Slicer using UTF8 inside, I am surprised that your guys already have changed most toLatin1/fromLatin1 to toUtf8/fromUtf8. Amazing!!</p>
<p>Did your guys complete the task manually or leverage llvm/clang syntax checker? My method is the last one. I can contribute the checked code in case community need it.</p>

---

## Post #12 by @lassoan (2020-03-06 14:30 UTC)

<p>I have manually reviewed all Latin1 conversions. If you compare the results with automated results and you find anything suspicious then let me know.</p>

---

## Post #13 by @pieper (2020-03-06 14:44 UTC)

<p>By the way <a class="mention" href="/u/xgongx">@xgongx</a>, can you try the latest Slicer preview builds and see how they work on non-English files and directories?  It would be great to know for sure that these changes are working in practice.</p>

---
