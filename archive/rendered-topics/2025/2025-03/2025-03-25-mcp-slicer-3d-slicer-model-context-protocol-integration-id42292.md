# MCP-Slicer: 3D Slicer Model Context Protocol Integration

**Topic ID**: 42292
**Date**: 2025-03-25
**URL**: https://discourse.slicer.org/t/mcp-slicer-3d-slicer-model-context-protocol-integration/42292

---

## Post #1 by @zhaoyouj (2025-03-25 12:40 UTC)

<h1><a name="p-123734-hello-everyone-1" class="anchor" href="#p-123734-hello-everyone-1" aria-label="Heading link"></a>Hello everyone!</h1>
<p>Try mcp-slicer and provide feedback~</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/zhaoyouj/mcp-slicer">
  <header class="source">

      <a href="https://github.com/zhaoyouj/mcp-slicer" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/fb0520c7c73b924f561e38b58959feed/zhaoyouj/mcp-slicer" class="thumbnail">

  <h3><a href="https://github.com/zhaoyouj/mcp-slicer" target="_blank" rel="noopener nofollow ugc">GitHub - zhaoyouj/mcp-slicer: A Model Context Protocol server for 3D Slicer...</a></h3>

    <p><span class="github-repo-description">A Model Context Protocol server for 3D Slicer integration</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Model Context Protocol (MCP) has become very popular recently, as it enables language models to extend their capabilities by using various tools, such as controlling web browsers, file systems, and more.</p>
<p>BlenderMCP, which “connects Blender to Claude AI through the Model Context Protocol (MCP), allowing Claude to directly interact with and control Blender. This integration enables prompt-assisted 3D modeling, scene creation, and manipulation,” has gained significant popularity, already accumulating 8.2k stars on GitHub.</p>
<p>I believe that Slicer should also have its own MCP server. Slicer has a flexible and user-friendly architecture, and large language models already have a decent understanding of it (and even if they don’t, we can simply provide them with documentation). This would allow us to write functional code and operate Slicer using natural language without significant overhead – which is really cool.</p>
<p>I’ve created a simple implementation called mcp-slicer that allows Claude, Cline, or other MCP-compatible clients to control a running instance of Slicer. You can check out this project on GitHub, try it out, and provide feedback.</p>
<p>Initially, I wanted to implement the server directly within Slicer using extensions and modules, but Slicer currently uses Python 3.9, while MCP Server development requires Python 3.10 or higher. Fortunately, I discovered the Slicer Web Server, which already implements many interfaces suitable for interaction with an MCP Server, so I utilized that approach.</p>
<p>Below is the README from the mcp-slicer project for your reference.</p>
<p><img src="https://github.com/zhaoyouj/mcp-slicer/blob/main/docs/images/logo.jpeg?raw=true" width="160" alt="logo" height="160"></p>
<h1><a name="p-123734-mcp-slicer-3d-slicer-model-context-protocol-integration-2" class="anchor" href="#p-123734-mcp-slicer-3d-slicer-model-context-protocol-integration-2" aria-label="Heading link"></a>MCP-Slicer - 3D Slicer Model Context Protocol Integration</h1>
<p><a>English</a> | <a>简体中文</a></p>
<p><a href="https://www.python.org/" rel="noopener nofollow ugc"><img src="https://img.shields.io/badge/python-3.13%2B-blue.svg" alt="Python Version" width="92" height="20"></a><br>
<a href="https://opensource.org/licenses/MIT" rel="noopener nofollow ugc"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" width="82" height="20"></a><br>
<a href="https://pypi.org/project/mcp-slicer/" rel="noopener nofollow ugc"><img src="https://img.shields.io/pypi/v/mcp-slicer.svg" alt="PyPI version" width="78" height="20"></a></p>
<p>MCP-Slicer connects 3D Slicer with model clients like Claude Desktop or Cline through the Model Context Protocol (MCP), enabling direct interaction and control of 3D Slicer. This integration allows for medical image processing, scene creation, and manipulation using natural language.</p>
<h2><a name="p-123734-features-3" class="anchor" href="#p-123734-features-3" aria-label="Heading link"></a>Features</h2>
<ol>
<li>
<p>list_nodes: List and filter Slicer MRML nodes and view their properties</p>
</li>
<li>
<p>execute_python_code: Execute Python code in the Slicer environment</p>
</li>
</ol>
<h2><a name="p-123734-installation-4" class="anchor" href="#p-123734-installation-4" aria-label="Heading link"></a>Installation</h2>
<h3><a name="p-123734-prerequisites-5" class="anchor" href="#p-123734-prerequisites-5" aria-label="Heading link"></a>Prerequisites</h3>
<ul>
<li>3D Slicer 5.8 or newer</li>
<li>Python 3.13 or newer</li>
<li>uv package manager</li>
</ul>
<p><strong>If you’re on Mac, please install uv as</strong></p>
<pre data-code-wrap="bash"><code class="lang-bash">brew install uv
</code></pre>
<p><strong>On Windows</strong></p>
<pre data-code-wrap="bash"><code class="lang-bash">powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
</code></pre>
<p>and then</p>
<pre data-code-wrap="bash"><code class="lang-bash">set Path=C:\Users\nntra\.local\bin;%Path%
</code></pre>
<p>Otherwise installation instructions are on their website: <a href="https://docs.astral.sh/uv/getting-started/installation/" rel="noopener nofollow ugc">Install uv</a></p>
<p><strong><img src="https://emoji.discourse-cdn.com/twitter/warning.png?v=15" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> Please install UV first</strong></p>
<h3><a name="p-123734-claude-for-desktop-integration-6" class="anchor" href="#p-123734-claude-for-desktop-integration-6" aria-label="Heading link"></a>Claude for Desktop Integration</h3>
<p>Go to Claude &gt; Settings &gt; Developer &gt; Edit Config &gt; claude_desktop_config.json to include the following:</p>
<pre data-code-wrap="json"><code class="lang-json">{
  "mcpServers": {
    "slicer": {
      "command": "uvx",
      "args": ["mcp-slicer"]
    }
  }
}
</code></pre>
<h3><a name="p-123734-cline-intergration-7" class="anchor" href="#p-123734-cline-intergration-7" aria-label="Heading link"></a>Cline Intergration</h3>
<pre data-code-wrap="json"><code class="lang-json">{
  "mcpServers": {
    "slicer": {
      "command": "uvx",
      "args": ["mcp-slicer"]
    }
  }
}
</code></pre>
<h2><a name="p-123734-usage-8" class="anchor" href="#p-123734-usage-8" aria-label="Heading link"></a>Usage</h2>
<h3><a name="p-123734-check-claude-settings-9" class="anchor" href="#p-123734-check-claude-settings-9" aria-label="Heading link"></a>Check Claude Settings</h3>
<p><img width="690" alt="Image" src="https://github.com/zhaoyouj/mcp-slicer/blob/main/docs/images/claude_check.png?raw=true" height="377"></p>
<p>Make sure you see the corresponding slicer tools added to the Claude Desktop App</p>
<p><img width="300" alt="Image" src="https://github.com/zhaoyouj/mcp-slicer/blob/main/docs/images/toolsButton.png?raw=true" height="114"><br>
<img width="300" alt="Image" src="https://github.com/zhaoyouj/mcp-slicer/blob/main/docs/images/tools_check.png?raw=true" height="199"></p>
<h3><a name="p-123734-open-slicer-web-server-10" class="anchor" href="#p-123734-open-slicer-web-server-10" aria-label="Heading link"></a>Open Slicer Web Server</h3>
<ol>
<li>Open the Slicer Web Server module,</li>
<li>ensure the required interfaces are checked,</li>
<li>then start the server</li>
</ol>
<p><img width="690" alt="Image" src="https://github.com/zhaoyouj/mcp-slicer/blob/main/docs/images/start_slicer_web_server.png?raw=true" height="429"></p>
<h2><a name="p-123734-examples-11" class="anchor" href="#p-123734-examples-11" aria-label="Heading link"></a>Examples</h2>
<h3><a name="p-123734-list_nodes-12" class="anchor" href="#p-123734-list_nodes-12" aria-label="Heading link"></a>- list_nodes</h3>
<blockquote>
<p>What Markups nodes are in the Slicer scene now, list their names, what is their length if it is a line, and what is its angle if it is an angle</p>
</blockquote>
<p><img width="690" alt="Image" src="https://github.com/zhaoyouj/mcp-slicer/blob/main/docs/images/example_list_nodes_en.png?raw=true" height="425"></p>
<h3><a name="p-123734-execute-python-code-13" class="anchor" href="#p-123734-execute-python-code-13" aria-label="Heading link"></a>- execute python code</h3>
<blockquote>
<p>Draw a translucent green cube of 8 cm in the Slicer scene, mark its vertices, and then draw a red sphere inscribed in it.</p>
</blockquote>
<p><img width="690" alt="example_code_execute_en" src="https://github.com/zhaoyouj/mcp-slicer/blob/main/docs/images/example_code_execute_en.png?raw=true" height="299"></p>
<h2><a name="p-123734-technical-details-14" class="anchor" href="#p-123734-technical-details-14" aria-label="Heading link"></a>Technical Details</h2>
<p>Utilizes existing Slicer Web Server interfaces. For technical details, please see <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html" rel="noopener nofollow ugc">Slicer web server user guide</a></p>
<h2><a name="p-123734-limitations-security-considerations-15" class="anchor" href="#p-123734-limitations-security-considerations-15" aria-label="Heading link"></a>Limitations &amp; Security Considerations</h2>
<ul>
<li>
<p>The <code>execute_python_code</code> tool allows running arbitrary Python code in 3D Slicer, which is powerful but potentially dangerous.</p>
<p><strong><img src="https://emoji.discourse-cdn.com/twitter/warning.png?v=15" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> Not recommended for production use.</strong></p>
</li>
<li>
<p>Complex operations may need to be broken down into smaller steps.</p>
</li>
</ul>
<h2><a name="p-123734-contributing-16" class="anchor" href="#p-123734-contributing-16" aria-label="Heading link"></a>Contributing</h2>
<p>Contributions are welcome! Feel free to submit Pull Requests.</p>
<h2><a name="p-123734-disclaimer-17" class="anchor" href="#p-123734-disclaimer-17" aria-label="Heading link"></a>Disclaimer</h2>
<p>This is a third-party integration project, not developed by the 3D Slicer team.</p>

---

## Post #2 by @pieper (2025-03-25 14:48 UTC)

<p>Sounds great!</p>
<p>Thanks for including the warning about possible security issues, particularly if PHI is involved.  Safety first <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=14" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>That said I can’t wait to try this out of a virtual machine with public data.</p>

---

## Post #3 by @lassoan (2025-03-25 16:55 UTC)

<p>This is awesome! I wanted to try how capable MCP for Slicer is and your work makes this much easier. Also, the example that you show here is really promising!</p>
<p>We’ll update Slicer’s Python version hopefully in a couple of weeks, which will simplify the installation process. It would be also interesting to try to extend the interface to allow more functionality without exposing the python exec API. For example, getting information about the currently loaded image, get image data, set image data, drawing markups on the image, etc. These would be pretty safe to use (so we might run it without sandboxing the application) and could allow some really cool use cases.</p>

---

## Post #4 by @pieper (2025-03-25 17:11 UTC)

<p>FYI, I was able to try this out using DeepSeek-R1 in cline in vscode using <a href="https://docs.jetstream-cloud.org/inference-service/api-examples/?h=cline#using-with-cline-extension-for-vscode-or-vscodium-from-jetstream2-instance-or-tunnelled-connection">these instructions</a> and I was able to replicate the examples, so that’s cool.  (Results where a bit oddly different and incorrect, like when I pasted in the example prompt to make the red sphere inscribed in the green cube, it make a green cube inscribed in the sphere).</p>
<p>I tried asking it do a few other things like downloading sample data, scrolling through slices and it was interesting to see that it was making reasonable guesses and using the error messages to come up with better solutions.  I think there’s a lot of potential in this.</p>

---

## Post #5 by @zhaoyouj (2025-03-27 03:29 UTC)

<p>It is delightful to hear the news that the Python version will be updated in the near future. This indeed can bring a great deal of convenience.<br>
Yes, there are many Web Server interfaces that can be utilized, and they are safer than python exec API. I will gradually add them later.<br>
Moreover, it would be very cool if Slicer had its own chatbot module, I would like to try whether bidirectional communication with the LLM client is possible and transfer the prompt input in Slicer to it. Having Claude and Slicer open simultaneously is a bit cumbersome.</p>

---

## Post #6 by @zhaoyouj (2025-03-27 03:46 UTC)

<p>Thank you for trying it out. happy to hear that mcp-slicer is working properly. <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=14" title=":blush:" class="emoji" alt=":blush:" loading="lazy" width="20" height="20"> I haven’t tested it in many environments yet.</p>
<p>In my experience, using different language models has a significant impact on the results. Generally, I think Claude 3.7 or 3.5 can also yield excellent results.</p>
<p>Mcp-slicer can not only execute code but also return execution results and error messages to the client. This is very promising. Nowadays, large-model clients can determine whether they are on the right path based on the returned results and correct their methods. By interacting several more times, one can often obtain the correct results.</p>
<p>Moreover, if everyone wants to try it out for free, the Vscode Cline plugin is an excellent choice. It can utilize the free usage in GitHub Copilot. You can use Claude 3.5 Sonnet for FREE<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/235e06629dab2fa13447c17b3f54cbaefc52fbd2.png" data-download-href="/uploads/short-url/52S9R6ix2dVvX9gTYZWqiRCyiCC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/235e06629dab2fa13447c17b3f54cbaefc52fbd2.png" alt="image" data-base62-sha1="52S9R6ix2dVvX9gTYZWqiRCyiCC" width="587" height="222"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">587×222 10.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
