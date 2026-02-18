# An extension contains common functions for different extensions

**Topic ID**: 7143
**Date**: 2019-06-12
**URL**: https://discourse.slicer.org/t/an-extension-contains-common-functions-for-different-extensions/7143

---

## Post #1 by @brhoom (2019-06-12 18:22 UTC)

<p>Dear all,</p>
<p>I have two different extension1 and extension2 for two different users user1 and user2. These extensions are using the same functions. I created a common scripted module that both extensions can use. My question: <strong>Is it ok to add pull request for this extension as it does not do anything by itself?</strong></p>
<p>If I add it to one of the two extensions, one of the users will have to install both extensions. If I add it to both extensions, this produce redundancy.</p>
<p>Best regards!<br>
Ibraheem</p>

---

## Post #2 by @lassoan (2019-06-12 18:27 UTC)

<p>There are a few examples for utility extensions (SlicerOpenCV, SlicerIGSIO), but in general these are larger extensions that many other unrelated extensions use. It is better to avoid introducing very small utility extensions, as they increases maintenance workload.</p>
<p>Instead of introducing a new utility extension, can you make one extension depend on the other?</p>

---

## Post #3 by @brhoom (2019-06-12 19:39 UTC)

<p>Thanks Andras!</p>
<blockquote>
<p>Instead of introducing a new utility extension, can you make one extension depend on the other?</p>
</blockquote>
<p>Yes, but as I mentioned a user will have to install an extension even if he does not need it.OK, I think I got an idea. I will just download the comoon module file to the current module path.</p>

---

## Post #4 by @lassoan (2019-06-12 19:51 UTC)

<p>If you list the extension as a dependency then it will be installed automatically (user just need to click OK). I would not recommend  separate manual download and install of a module.</p>

---

## Post #5 by @brhoom (2019-06-12 19:55 UTC)

<blockquote>
<p>I would not recommend separate manual download and install of a module.</p>
</blockquote>
<p>I just figure out this may complicate things. OK, I go for this approach but it would be nice if Slicer offers such thing e.g. an extension that does not appear in the extension manager.</p>

---
