# Some menu items not being sorted alphabetically?

**Topic ID**: 30956
**Date**: 2023-08-03
**URL**: https://discourse.slicer.org/t/some-menu-items-not-being-sorted-alphabetically/30956

---

## Post #1 by @jhlegarreta (2023-08-03 15:01 UTC)

<p>Hi,<br>
wondering why in some menus the items are not sorted alphabetically:</p>
<p>e.g.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cea6f480eb2a9833ed583e03f55bb6a77ad0db7.png" data-download-href="/uploads/short-url/aYqyPr2jmgiWJ9PWuNTyXqwUpYb.png?dl=1" title="Slicer_diffusion_menu_sorting_not_alphabetically_closeup" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4cea6f480eb2a9833ed583e03f55bb6a77ad0db7_2_517x180.png" alt="Slicer_diffusion_menu_sorting_not_alphabetically_closeup" data-base62-sha1="aYqyPr2jmgiWJ9PWuNTyXqwUpYb" width="517" height="180" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4cea6f480eb2a9833ed583e03f55bb6a77ad0db7_2_517x180.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4cea6f480eb2a9833ed583e03f55bb6a77ad0db7_2_775x270.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cea6f480eb2a9833ed583e03f55bb6a77ad0db7.png 2x" data-dominant-color="B5B8BA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_diffusion_menu_sorting_not_alphabetically_closeup</span><span class="informations">819×287 36.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>or</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a0c61740dadad9823a4e26845abd4ff6eda0d97.png" alt="Slicer_filtering_menu_sorting_not_alphabetically_closeup" data-base62-sha1="1qTiBTY4nkjcFEWWzkeeyif1chx" width="422" height="202"></p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2023-08-03 15:11 UTC)

<p>It is a feature. You can specify “index” in the module description of CLI modules. You can also set <code>index</code> property in the module object of any other modules, but I think this mechanism is only used for CLI modules now. Modules in the menu are sorted based on index (if not specified then default is 65535), and then modules that have the same index are sorted alphabetically.</p>
<p>This sorting mechanism has become somewhat irrelevant since there are more modules that could be practically browsed using the hierarchical menu. It is easier to just hit Ctrl-F and start typing. You can find modules not just by its name but all text (full description, extension name, developers, etc.), so the module finder is generally an easier and faster way of locating modules.</p>

---

## Post #3 by @jhlegarreta (2023-08-03 21:50 UTC)

<p>OK, thanks for the info Andras <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20">.</p>

---
