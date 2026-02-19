---
topic_id: 22787
title: "To Add Widget On Slice Views"
date: 2022-04-01
url: https://discourse.slicer.org/t/22787
---

# To add Widget on Slice Views

**Topic ID**: 22787
**Date**: 2022-04-01
**URL**: https://discourse.slicer.org/t/to-add-widget-on-slice-views/22787

---

## Post #1 by @joanne40226 (2022-04-01 04:44 UTC)

<p>Hi, I am now working on placing my button group widget on the side of the Slice View.<br>
I did it by placing a toolButton on the sliceController.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c627a86f7044dcc1188ca896cc6ce8e9847a2929.png" data-download-href="/uploads/short-url/sgXvmJU867rn1teiguirUe1VgIV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c627a86f7044dcc1188ca896cc6ce8e9847a2929_2_690x291.png" alt="image" data-base62-sha1="sgXvmJU867rn1teiguirUe1VgIV" width="690" height="291" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c627a86f7044dcc1188ca896cc6ce8e9847a2929_2_690x291.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c627a86f7044dcc1188ca896cc6ce8e9847a2929_2_1035x436.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c627a86f7044dcc1188ca896cc6ce8e9847a2929_2_1380x582.png 2x" data-dominant-color="070907"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1392×588 11 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, the question here is that I want it place on the view forever, which means that I should not use a toolButton which will make my button list disappear as long as the toolButton  is not triggered.<br>
I wish to add widget on the Slice View but I still cannot fix this problem, hope someone can help. Thank you.</p>

---

## Post #2 by @mau_igna_06 (2022-04-01 09:07 UTC)

<p>The button of the sliceWidget that does not dissapear when is pinned it’s implemented with a ctkPopUpWidget <a href="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkPopupWidget.cpp" class="inline-onebox">CTK/ctkPopupWidget.cpp at master · commontk/CTK · GitHub</a></p>
<p>You can check if that is useful for you. I have used them for the exact purpose you describe</p>
<p>Hope this helps</p>

---

## Post #4 by @joanne40226 (2022-04-01 10:14 UTC)

<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a><br>
Hi, thank you for the quick reply!<br>
I did what you suggest, it works. However, I encountered a problem which the width of the popupWidget is to large and I could not fix it by now. Do you have any suggestion? Thank you so much.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8460e8064f4f2ae5ab2f5ce3e18093c832c8056c.png" data-download-href="/uploads/short-url/iT4E71vziub4N5GZyEs2SAnfWiM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/8460e8064f4f2ae5ab2f5ce3e18093c832c8056c_2_690x394.png" alt="image" data-base62-sha1="iT4E71vziub4N5GZyEs2SAnfWiM" width="690" height="394" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/8460e8064f4f2ae5ab2f5ce3e18093c832c8056c_2_690x394.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/8460e8064f4f2ae5ab2f5ce3e18093c832c8056c_2_1035x591.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/8460e8064f4f2ae5ab2f5ce3e18093c832c8056c_2_1380x788.png 2x" data-dominant-color="737171"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1386×792 76.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @mau_igna_06 (2022-04-01 10:32 UTC)

<p>I think the size of the popup is controlled by the widget that is inside it</p>

---

## Post #6 by @joanne40226 (2022-04-01 10:34 UTC)

<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a><br>
I did it by this way<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97b49df5ce98d330e3b569e07e24cf0c53fc1ecb.png" data-download-href="/uploads/short-url/lE34ektTBi1BR9W64u3ItQNrcUj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97b49df5ce98d330e3b569e07e24cf0c53fc1ecb.png" alt="image" data-base62-sha1="lE34ektTBi1BR9W64u3ItQNrcUj" width="690" height="169" data-dominant-color="262727"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1075×264 14.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
So I think the horizontal size is fixed by the sliceController horizontal size?</p>

---

## Post #7 by @lassoan (2022-04-02 01:34 UTC)

<p>You have chosen the <code>qt.QVBoxLayout</code> = vertical box layout, which puts all widgets in a column. If you want to display widgets in a row you can use <code>qt.QHBoxLayout</code>.</p>

---

## Post #8 by @joanne40226 (2022-04-03 02:39 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Hello, Thanks for your reply.<br>
I did what you suggest and it looks great as the image below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2b7636bf4d618199114abb526dffd31c9c9ec53.png" data-download-href="/uploads/short-url/ndsfZEDQkF5joFVETEVTEjGK8N5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2b7636bf4d618199114abb526dffd31c9c9ec53_2_330x500.png" alt="image" data-base62-sha1="ndsfZEDQkF5joFVETEVTEjGK8N5" width="330" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2b7636bf4d618199114abb526dffd31c9c9ec53_2_330x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2b7636bf4d618199114abb526dffd31c9c9ec53_2_495x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2b7636bf4d618199114abb526dffd31c9c9ec53.png 2x" data-dominant-color="34342F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">529×800 13.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, I still wish it to be a vertical button table. Which looks like<br>
the image below but with a narrow width<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/985efa796ce70e8eafdcf5a333c7cfcfe3a171b1.png" data-download-href="/uploads/short-url/lJW451PNuco2ySDrot0ZbEYlqNj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/985efa796ce70e8eafdcf5a333c7cfcfe3a171b1_2_690x344.png" alt="image" data-base62-sha1="lJW451PNuco2ySDrot0ZbEYlqNj" width="690" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/985efa796ce70e8eafdcf5a333c7cfcfe3a171b1_2_690x344.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/985efa796ce70e8eafdcf5a333c7cfcfe3a171b1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/985efa796ce70e8eafdcf5a333c7cfcfe3a171b1.png 2x" data-dominant-color="858483"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">869×434 40.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The problem is that as long as the popupWidget is added under the sliceController().layout(), the width will be as large as the slice Controller layout. Which I want the white blank to disappear as the above image shows.</p>

---

## Post #9 by @lassoan (2022-04-03 14:25 UTC)

<p>If you want to get vertical button layout then I would recommend the solution that <a class="mention" href="/u/ungi">@ungi</a> described above.</p>

---

## Post #10 by @joanne40226 (2022-04-04 02:59 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I see, I will try it later.<br>
Thank you so much for the reply.</p>

---
