---
topic_id: 12075
title: "Markups Module Confusion Suggestions To Improve"
date: 2020-06-17
url: https://discourse.slicer.org/t/12075
---

# Markups module confusion - suggestions to improve

**Topic ID**: 12075
**Date**: 2020-06-17
**URL**: https://discourse.slicer.org/t/markups-module-confusion-suggestions-to-improve/12075

---

## Post #1 by @ddrobny (2020-06-17 17:19 UTC)

<p>Hi,<br>
I’d like to describe my experience with the Slicer markups module and suggest some improvements.</p>
<p>I wanted to place some fiducials and export them as a list. I opened the Markups module and click the first icon “Create Fiducial Markup” and place it in the viewer. The markup appears in the list and I repeat this for a bunch of landmarks. Then I want to save the list of fiducials/markups but seem to be only able to save them individually.<br>
I asked my walking slicer reference aka Fernando for help and he explained to me that I was creating markup nodes/lists with one element rather than adding new elements to an existing list. The fact that I need to use the icon in the menu bar to place individual fiducials is not very intuitive and as the icons are virtually the same I did not expect different behaviour. It is especially confusing as the viewer shows what I expect: every time I click the icon I can place a fiducial but the creation of a list on top is not transparent.</p>
<p>Within the markup module, I would suggest to have a button to add a markup node/list with appropriate description and then separate buttons to add elements to this node/list. It might also be reasonable to move the functionality to add elements into the “control points” sub module (which I didn’t look at initially because I thought I found the function I needed). I would also expect to have the same buttons within the module window as in the menu bar (I did not expect that some functionality is only available outside the relevant module).</p>
<p>I hope this is understandable and that it could be used to improve Slicer.</p>
<p>Thanks!</p>
<p>PS I am using Slicer 4.11.0-2020-01-30 r28751</p>

---

## Post #2 by @muratmaga (2020-06-17 17:36 UTC)

<p>Yes, you are correct that those two icons are very very similar causing confusion with people starting with the Slicer. The little “+” sign in the Markups module is meant to imply that you are creating a new MarkupsFiducialNode (or others) as oppose to adding fiducials to an existing one.</p>
<p>If you have any suggestions or can help us with an icon design, your contribution will be highly welcomed.</p>

---

## Post #3 by @ddrobny (2020-06-17 17:53 UTC)

<p>Is it necessary that those buttons create a MarkupsFiducialNode <em>and</em> change the mode of the cursor (e.g. to placing fiducials)? This confused me into thinking that the button has the same function as I ended in the same cursor mode.<br>
Why not have a simple “new” button to create a node. And then have the same icons and same functions as in the menu bar for placing the fiducials? Maybe I would put the buttons to add fiducials in the “Control Points” submenu to separate them from the node/list.<br>
Also a clearer mouse-hover text for the buttons could clarify things.</p>

---

## Post #4 by @muratmaga (2020-06-17 18:08 UTC)

<p>The behavior is there to make it consistent with the other Markups node actions (e.g., you can create a line Markup, or angle Markup), I believe.</p>
<p>The challenge is you never add to those markup nodes (like line always have two points, angle would have three). Whereas, you can keep  adding new fiducials to MarkupFiducialNodes…</p>
<p>I recognize the problem, I just don’t have a good solution to it. <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>

---

## Post #5 by @pieper (2020-06-17 23:09 UTC)

<p>That’s very good feedback - thanks for taking the time to explain <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>Fiducials and Curve markups are conceptually a bit different than the other Markup types because they don’t have predefined number of points, so maybe we should handle them as a special case in the Markups module too.  Currently when you enter Fiducial or a Curve mode in the toolbar you add to the most recent (or selected) node, while the markup modes add a new node.</p>
<p>Perhaps the easiest would be to just add a row of buttons for Fiducial, Open Curve, and Closed Cure with the label “Add” to the Markups module below the “Create” row.  Those would behave like the toolbar buttons.</p>
<p>Or maybe there’s a better way to unify so we use the same widget in both the module and toolbar.</p>

---

## Post #6 by @muratmaga (2020-06-18 20:34 UTC)

<p>Yes, perhaps moving the toolbar button down to the markups and having two rows of buttons (one to create new nodes, and one to add to) might be the way to do. That way it is more clear that they have different functionality (even though the icons look similar).</p>

---
