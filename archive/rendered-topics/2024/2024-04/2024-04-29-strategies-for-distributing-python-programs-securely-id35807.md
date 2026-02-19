---
topic_id: 35807
title: "Strategies For Distributing Python Programs Securely"
date: 2024-04-29
url: https://discourse.slicer.org/t/35807
---

# Strategies for Distributing Python Programs Securely

**Topic ID**: 35807
**Date**: 2024-04-29
**URL**: https://discourse.slicer.org/t/strategies-for-distributing-python-programs-securely/35807

---

## Post #1 by @park (2024-04-29 15:44 UTC)

<p>Hello all,</p>
<p>I’m looking to develop a commercial program using a slicer. However, I’ve discovered that when I package and distribute this custom program, the source code remains exposed in the scripted model folder.</p>
<p>After searching the community, I found a solution suggesting converting .py files to .pyc files for distribution.<br>
<a href="https://discourse.slicer.org/t/how-to-hide-the-code-of-the-script-module/26135/16">https://discourse.slicer.org/t/how-to-hide-the-code-of-the-script-module/26135/16</a></p>
<p>Considering the time that has passed, is this still a viable option? Furthermore, I’m planning to encrypt .py files using tools like pyarmor before converting them to .pyc. Is this plan reasonable?</p>
<p>If anyone has experience distributing programs with Python code, I’d appreciate some advice. Any insight would be valuable to me.</p>

---

## Post #2 by @pieper (2024-04-29 22:50 UTC)

<p>I tried the chatbot on this question and I think the answer is a good summary (do others agree?).</p>
<aside class="quote quote-modified" data-post="7" data-topic="34811">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/semantic-search-for-this-forum/34811/7">Semantic search for this forum</a> <a class="badge-category__wrapper " href="/c/forum-feedback/10"><span data-category-id="10" style="--category-badge-color: #B3B5B4; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="Discussion about this site, its organization, how it works, and how we can improve it."><span class="badge-category__name">Forum and website feedback</span></span></a>
  </div>
  <blockquote>
    Here’s what the chatbot said in response to this question: 


<a href="https://discourse.slicer.org/u/claude_3_opus_bot">claude_3_opus_bot</a>Forum Helper 
<a href="https://discourse.slicer.org/t/untitled-ai-bot-pm/35822/2">1m</a> 
Search 
Based on my search of the Slicer forum, it looks like converting .py files to .pyc files is still a reasonable approach for distributing Slicer extensions while hiding the original Python source code: 
<a href="https://discourse.slicer.org/t/how-to-hide-the-code-of-the-script-module/26135/13">How to hide the code of the script module?</a> 
In that post from early 2024, it was suggested to write a short Python script that compiles your .py files to .pyc and then replaces the .py files wi…
  </blockquote>
</aside>


---

## Post #3 by @park (2024-05-07 08:48 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> ,</p>
<p>Thank you for your reply!</p>
<p>Regarding this issue, we would like to test whether we can put our script module on the server and have it readable without downloading it (due to security concerns in the code).</p>
<p>After examining the slicer application, it seems that extension modules are defined and read in<code> slicer.org/slicer-####.ini (in my case, 32438)</code> under <code>AdditionalPaths</code>. However, it was difficult to find out how they are read in what manner. Can we gain insight into this?</p>
<p>In particular, it would be helpful to know how the modules in <code>AdditionalPaths</code> are loaded into slicer and in what order, and how access is possible from <code>slicer.module</code> (for example, <code>slicer.modules.mymodule</code>).</p>

---

## Post #4 by @pieper (2024-05-07 19:10 UTC)

<p>Hi <a class="mention" href="/u/park">@park</a> -</p>
<p>Those <code>AdditionalPaths</code> describe places where the application searches for code to load and they all must be on the client machine as things currently exist.  If the code matches what Slicer expects, the code is loaded as a module.  The details are a bit complex but the idea is simple.</p>
<p>In the end if you have code running on a client computer it will need to be read and loaded, even if the code is fetched from the server at run time.  If they are .pyc files they will be hard to understand, but in theory someone could decompile or even just call your functions themselves.</p>
<p>You could put in a wrapper that downloads the actual code at runtime and then deletes it after using it, but this seems a bit fragile and wouldn’t stop a really dedicated adversary.</p>
<p>I think the best way to truly isolate your code would be to never put it on the client machine, but instead use it via a web api with encryption and a license key so you know exactly who is calling it.</p>

---

## Post #5 by @park (2024-05-08 07:28 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>  Thank you for the advice.</p>
<p>I would like to repost the article regarding this matter for more specific implementation.</p>
<p>Thank you for always responding kindly.</p>

---
