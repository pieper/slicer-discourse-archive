---
topic_id: 45118
title: "3D Slicer And Trame Slicer Framework"
date: 2025-11-17
url: https://discourse.slicer.org/t/45118
---

# 3D Slicer and trame-slicer framework

**Topic ID**: 45118
**Date**: 2025-11-17
**URL**: https://discourse.slicer.org/t/3d-slicer-and-trame-slicer-framework/45118

---

## Post #1 by @claudiney (2025-11-17 15:35 UTC)

<p><strong>Project Title: Building an Interactive 3D Slicer Tool for Global Clinical Training</strong></p>
<p><strong>[Quick Project Summary]</strong> I’m looking for a specialized Python/Web developer to help me build a secure, cloud-hosted training tool using the <strong>trame-slicer</strong> framework. The user will practice medical segmentation (like contouring an organ), and the system will give them instant, quantitative feedback (DICE/Hausdorff scores) so they can correct their work right away.</p>
<p><strong>1. Mission and Platform Background</strong></p>
<p>My online learning platform focuses onbringing clinical knowledge to everyone in the medical community but especially to those who need it the most: professionals in developing countries. To truly make learning stick, I would like to integrate an interactive, web-based simulation right into our courses. This tool will bridge the gap between reading about a technique and actually performing it.</p>
<p><strong>2. The Core Technical Challenge</strong></p>
<p>I need an experienced developer to build a specialized, web-based training module. The tech backbone? <strong>3D Slicer</strong> and the <strong>trame-slicer</strong> framework.</p>
<p>This module's main job is to let remote users practice critical clinical skills, like <strong>contouring (segmentation) specific anatomical organs or targets</strong>, all from a simple web browser.</p>
<p><strong>3. Required Functionality and Solution Architecture</strong></p>
<p>Here’s a breakdown of how the tool needs to work:</p>
<table>
    <tbody>
        <tr>
            <td>
                <p><strong>Component</strong></p>
            </td>
            <td>
                <p><strong>Description</strong></p>
            </td>
        </tr>
        <tr>
            <td>
                <p><strong>Server Setup</strong></p>
            </td>
            <td>
                <p><strong>3D Slicer</strong> will be installed and run on a dedicated cloud server (we can figure out the specifics together).</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><strong>Web Interface (trame-slicer)</strong></p>
            </td>
            <td>
                <p>You'll build a custom web interface using <strong>trame-slicer</strong> that’s streamlined and easy to use. It should only show a <strong>curated, simplified selection of 3D Slicer tools</strong> needed for the task (e.g., specific brushes, views, and a big "Submit" button).</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><strong>Data Loading</strong></p>
            </td>
            <td>
                <p>The app needs to automatically load a specific, pre-selected medical dataset when the user starts a specific task. Basically I need a ‘web link’ for each studyset I want to use for a certain task.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><strong>User Task</strong></p>
            </td>
            <td>
                <p>The user performs the instructed task (e.g., contouring a specific organ) using the simplified tools.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><strong>Submission &amp; Evaluation</strong></p>
            </td>
            <td>
                <p>When the user hits "Submit," a process runs in the background on the 3D Slicer server to: &lt;ul&gt;&lt;li&gt;Compare their segment against a hidden, ground-truth reference segment.&lt;/li&gt;&lt;li&gt;Calculate two key metrics: <strong>DICE Coefficient</strong> and <strong>Hausdorff Distance</strong>.&lt;/li&gt;&lt;/ul&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><strong>Feedback Display</strong></p>
            </td>
            <td>
                <p>The calculated metrics (DICE and Hausdorff values) need to pop up instantly. At the same time, the reference segment must be loaded and displayed in the 3D view right next to the user's contour for visual comparison.</p>
            </td>
        </tr>
    </tbody>
</table>
<p><strong>4. Essential Technical Expertise</strong></p>
<p>This project is specialized, so you'll need experience in <strong>all three</strong> of these areas:</p>
<ol start="1" type="1">
    <li><strong>3D Slicer Development:</strong> Writing Python scripted modules and working deep within the Slicer MRML scene.</li>
    <li><strong>Python Development:</strong> Strong Python skills for managing the server logic and integrating with the Slicer APIs.</li>
    <li><strong>trame/trame-slicer Framework:</strong> Hands-on experience building, deploying, and styling interactive web apps using the trame framework, especially its integration with 3D Slicer.</li>
</ol>
<p><strong>5. Next Steps</strong></p>
<p>If you're excited to use your skills for this high-impact global health project, here's what we need from you:</p>
<ul>
    <li><strong>Experience Summary:</strong> Tell me about specific projects where you used <strong>trame</strong> and <strong>3D Slicer</strong> to build a web application.</li>
    <li><strong>Availability &amp; Quote:</strong> Let me know your availability and a project-based quote.</li>
    <li><strong>Portfolio Link:</strong> Your professional profile (like LinkedIn or GitHub).</li>
</ul>
<p>I can't wait to hear from you and discuss how to make this educational tool happen!</p>
<p>&nbsp;</p>

---

## Post #2 by @finetjul (2025-11-17 23:03 UTC)

<aside class="quote no-group quote-modified" data-username="claudiney" data-post="1" data-topic="45118">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/58956e/48.png" class="avatar"> claudiney:</div>
<blockquote>
<p>This module’s main job is to let remote users practice critical clinical skills, like <strong>contouring (segmentation) specific anatomical organs or targets</strong>, all from a simple web browser.</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/claudiney">@claudiney</a> , we, at Kitware, have created “trame Slicer” with the workflow you detail in mind. We therefore should be able to help you <img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=15" title=":grin:" class="emoji" alt=":grin:" loading="lazy" width="20" height="20">.<br>
Let me reach out to you in private to move forward.</p>

---
