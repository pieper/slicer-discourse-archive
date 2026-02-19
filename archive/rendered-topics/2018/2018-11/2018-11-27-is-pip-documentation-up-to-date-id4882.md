---
topic_id: 4882
title: "Is Pip Documentation Up To Date"
date: 2018-11-27
url: https://discourse.slicer.org/t/4882
---

# Is pip documentation up to date

**Topic ID**: 4882
**Date**: 2018-11-27
**URL**: https://discourse.slicer.org/t/is-pip-documentation-up-to-date/4882

---

## Post #1 by @muratmaga (2018-11-27 04:33 UTC)

<p>On windows instructions at <a href="https://www.slicer.org/wiki/Documentation/Labs/Pip" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Labs/Pip</a><br>
work for 4.8.1, but not for the latest stable 4.10.0. I get this</p>
<p>&gt;&gt;&gt; import pip</p>
<p>&gt;&gt;&gt; pip.main([‘install’, ‘pygments’])</p>
<p>Traceback (most recent call last):</p>
<p>File "&lt;console&gt;", line 1, in &lt;module&gt;</p>
<p>AttributeError: ‘module’ object has no attribute ‘main’</p>

---

## Post #2 by @jamesobutler (2018-11-27 05:18 UTC)

<p>There’s another Slicer forum post with a lot of good information on this topic. See <a href="https://discourse.slicer.org/t/pip-in-nightly-build-not-working/3325">Pip in nightly build not working</a>. Essentially a newer version of pip has changed where <code>main()</code> is located.</p>

---

## Post #3 by @jamesobutler (2018-11-27 05:31 UTC)

<p>That being said, that Pip wiki page should probably be updated with the information found in that forum thread. I currently don’t have access to edit the wiki.</p>
<p>However that Pip wiki page is also under the “Labs” category which I don’t believe has all of its subpages up-to-date. I think it is more a dumping ground of notes by developers when trying to plan a project. I think that’s why keeping those pages up-to-date isn’t a priority since users won’t need to read them as part of the actual primary Slicer documentation.</p>

---

## Post #4 by @muratmaga (2018-11-27 05:56 UTC)

<p>Thanks <a class="mention" href="/u/jamesobutler">@jamesobutler</a>. Provided example in the thread worked for me.</p>

---

## Post #5 by @lassoan (2018-11-27 06:26 UTC)

<p>Which example worked?</p>
<p>I think pip main is not supposed to be accessed manually (as when you launch a Python interpreter, some packages may not be possible to update because they are already loaded).</p>
<p>Instead you can run pip as <code>PythonSlicer -m pip install something</code>.<br>
<a class="mention" href="/u/muratmaga">@muratmaga</a> can you confirm that this works?</p>

---

## Post #6 by @muratmaga (2018-11-27 17:09 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I meant this method from <a class="mention" href="/u/patrickcox3">@patrickcox3</a> worked:</p><aside class="quote" data-post="6" data-topic="3325">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/patrickcox3/48/1463_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/pip-in-nightly-build-not-working/3325/6">Pip in nightly build not working</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    pip.main can be found in pip._internal 
I was able to utilize it in my project as shown: 
from pip._internal import main as pipmain
pipmain(['install', 'scipy'])

However, using pip within your program <a href="https://pip.pypa.io/en/stable/user_guide/#using-pip-from-your-program" rel="nofollow noopener">is strongly discouraged</a>. 
An alternative method, such as spoken to in this thread, would be extremely helpful.
  </blockquote>
</aside>

<p>Scipy installed successfully as far as I can tell. It didn’t work with Rpy2. I will try your suggestion in the other thread.</p>

---

## Post #7 by @jcfr (2018-11-28 07:00 UTC)

<p>Developer FAQ has been updated with a new entry. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_run_pip_.3F" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_run_pip_.3F</a></p>

---
