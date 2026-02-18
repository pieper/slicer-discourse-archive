# How to instal old version of extension from file

**Topic ID**: 34212
**Date**: 2024-02-08
**URL**: https://discourse.slicer.org/t/how-to-instal-old-version-of-extension-from-file/34212

---

## Post #1 by @Matteboo (2024-02-08 14:55 UTC)

<p>Hello,<br>
I want to install the version of total segmentator of 3DSlicer 5.4 to have access to the “liver vessel” task<br>
I found a branch on the github repository named 5.4 and downloaded the code<br>
I then opened the extension manager on slicer 5.4 and clicked on “install from file”<br>
However I can’t find the “extension file” in the code.</p>
<p>I think there’s something to do to generate the “extension file” from the code but I don’t know what.<br>
I’ve never installed an extension from a file so I might be missing something obvious.</p>

---

## Post #2 by @muratmaga (2024-02-08 16:03 UTC)

<p>If you are installing from an extension from a cloned github repo, I find that <code>Extension Wizard</code> works better than “install from file”. Click Select Extension and then navigate to the root of the repo.</p>

---

## Post #3 by @Matteboo (2024-02-08 16:50 UTC)

<p>It worked thank you so much <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @Bahadir_OZDEMIR (2024-02-09 13:50 UTC)

<p>I wanted to try v2 while using totalsegmentator v1 and I couldn’t get rid of the “returned non-zero exit status 120” error. I want to try the old version like you did. I couldn’t find the old version on Github, I didn’t understand the solution here, where exactly is the extension wizard? I’m not very good at code but I think I can handle it with a little help, thank you</p>

---

## Post #5 by @Matteboo (2024-02-09 13:54 UTC)

<p>To try V2 you need Slicer 5.6<br>
I think that if you have this version and install total segmentator from the extension manager you will get V2<br>
On my computer, I have two slicer installed 5.4 for V1 and 5.6 for V2</p>

---

## Post #6 by @Bahadir_OZDEMIR (2024-02-09 13:56 UTC)

<p>I am using 5.4 slicer, how can I access v1?</p>

---

## Post #7 by @Matteboo (2024-02-09 14:07 UTC)

<p>The way I did it is that I downloaded the code of the extension for slicer 5.4 there <a href="https://github.com/lassoan/SlicerTotalSegmentator/tree/5.4" class="inline-onebox" rel="noopener nofollow ugc">GitHub - lassoan/SlicerTotalSegmentator at 5.4</a></p>
<p>Then I used the extension wizard to search for it and add it to my slicer set up</p>
<p>Be carefull to not stock the files with a path that contains special caracter (é, space, ö,…)</p>
<p>Even if this work, it’s not perfect and I would recommend to use total segmentator V2 with slicer 5.6 exept if you have a reason to do otherwise</p>

---

## Post #8 by @jamesobutler (2024-02-09 15:55 UTC)

<p>Is there a reason you all are not using the Extensions Manager in Slicer 5.4 to install SlicerTotalSegmentator? That will get the Slicer 5.4 version of extensions.</p>

---

## Post #9 by @Matteboo (2024-02-09 16:07 UTC)

<p>I tried but it wasn’t working<br>
Is it possible that some dependency of totalsegmentator are updated past version 5.4 which causes the issue ?</p>
<p>It may also be because of my set up since I have totalsegmentator already installed on my PC and use it outside of 3Dslicer. It has already been a source of issue.</p>

---

## Post #10 by @Bahadir_OZDEMIR (2024-02-09 19:01 UTC)

<p>thank you very much, I tried many things and somehow I succeeded. I can use totalsegmentator v1 in Slicer 5.4 as before</p>

---
