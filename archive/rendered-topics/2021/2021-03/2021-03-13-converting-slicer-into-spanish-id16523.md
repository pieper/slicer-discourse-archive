---
topic_id: 16523
title: "Converting Slicer Into Spanish"
date: 2021-03-13
url: https://discourse.slicer.org/t/16523
---

# Converting Slicer into Spanish

**Topic ID**: 16523
**Date**: 2021-03-13
**URL**: https://discourse.slicer.org/t/converting-slicer-into-spanish/16523

---

## Post #1 by @muratmaga (2021-03-13 17:55 UTC)

<p>We have some strong interest for Slicer and slicermorph from the spanish speaking countries, particular in SA. One of the ideas that was bounced during the workshop was converting menus into Spanish (or at least for some selected subset of extensions or modules).</p>
<p>Forum threads show there was at least one discussion of Spanish version of Slicer from couple years back. Did that ever reach into a usable state?</p>
<p>And more importantly, how does the language changes happen? Does that mean maintaining a completely separate build for that language in all three platforms (which I dont think we will be very appealing to the people who wants to help with the process)</p>

---

## Post #2 by @lassoan (2021-03-13 20:59 UTC)

<p>Qt has very good translation infrastructure and tools for maintaining translations, so all Qt resources and strings in Qt classes in Slicer can be translated relatively easily. However, we need to figure out how to make strings in VTK classes, CLI modules, and Python scripted modules translatable (preferably using the same Qt translation tools).</p>
<p>We have been considering about applying for CZI essential software project for developing localization of Slicer and create French (and maybe Spanish) translation and documentation. Once the infrastructure is in place, anyone can create translations for any language. All languages will be built into the Slicer package and you can change the language any time in application settings.</p>

---

## Post #3 by @cpinter (2021-03-15 10:28 UTC)

<p>There have been efforts to internationalize at least parts of Slicer primarily to Spanish, French, and Arabic in terms of the <a href="https://mt4sd.ulpgc.es/en/macbioidi-project/">MacBiolDi project</a>, but I’m not sure how far it has gotten.</p>
<p><a class="mention" href="/u/carlos-luque">@carlos-luque</a> <a class="mention" href="/u/jruiz">@jruiz</a> can you please give an update to <a class="mention" href="/u/muratmaga">@muratmaga</a> ?</p>

---

## Post #4 by @sofroniewn (2021-03-17 00:53 UTC)

<p>Hi all, we’ve just begun working on localization and internationalization at napari. You can see this issue with some of our initial discussions <a href="https://github.com/napari/napari/issues/2195" class="inline-onebox" rel="noopener nofollow ugc">Localization and internationalization · Issue #2195 · napari/napari · GitHub</a>. We plan to use the crowdin site to help with the actual translation. It’s also been used by the Jupyter team <a href="https://crowdin.com/project/jupyterlab" rel="noopener nofollow ugc">https://crowdin.com/project/jupyterlab</a>. Hope this helps!!</p>

---

## Post #5 by @lassoan (2021-03-17 04:39 UTC)

<p>Thanks for the tips, these are all very relevant, because we are in a very similar situation as napari - having lots of plugins implemented in Python by various groups and we would need a way to provide translations for them.</p>

---
