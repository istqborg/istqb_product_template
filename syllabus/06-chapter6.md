# Tools for accessibility testing – 120 minutes {#6}

#### Keywords

static analysis

#### Domain specific keywords

artificial intelligence (AI), CI/CD pipeline, document object model (DOM), linter

#### Learning Objectives for Chapter 6: {.learning-objectives}

1. Types of test automation tools
    1. (K2) Understand test automation and its limitations in accessibility testing
    1. (K2) Understand how to integrate test automation tools in software development lifecycle for accessibility testing
    1. (K2) Understand the role and risks of Artificial Intelligence (AI) in accessibility testing
1. Typical tools
    1. (K2) Understand the categories of tools available
    1. (K2) Explain the use of Category 1: Static Analysis & CI/CD Tools
    1. (K2) Explain the use of Category 2: Automated UI-Based Scanners & Manual Helpers
    1. (K2) Explain the use of Category 3: Assistive Technologies (AT)
    1. (K2) Explain the use of Category 4: Cognitive and Readability Tools

## Types of automation tools for accessibility testing

Tools are essential for efficient accessibility testing, but they cannot replace human judgment. This chapter explores the role of automation within the software development life cycle, identifies its inherent limitations, explores the emerging role of Artificial Intelligence, and classifies the typical categories of tools available to the digital accessibility tester.

### Test automation and its limitations in accessibility testing

In digital accessibility, “automation” refers to software engines that programmatically evaluate code or rendered Document Object Models (DOM) against predefined accessibility rulesets. While automation is a core pillar of a modern testing strategy, it is characterized by a “low ceiling” of detection capability.

This “low ceiling” exists because automated tools operate on binary logic. They can verify the existence of technical attributes (e.g., “Does this image have an \\<alt\\> attribute?”), but they cannot evaluate the *quality* or *intent* of the user experience (e.g., “Is this \\<alt\\> text meaningful to a blind user?”). Because accessibility is fundamentally about human perception and interaction, automation is limited by its inability to apply subjective judgment or understand context.

**Main benefits**

The main benefits of automation for digital accessibility:

* Efficiency and scale. Automated tools can crawl thousands of pages or evaluate complex component libraries in a fraction of the time required for manual inspection. in seconds to find “low-hanging fruits” (e.g., missing alternative text, contrast errors).
* Consistency and repeatability. Automation eliminates human fatigue, ensuring that, e.g. a missing \\<alt\\> text or invalid ARIA attribute is caught every time a check is run, regardless of the tester's experience level or any other situational circumstances.
* Instant feedback. Integrated tools provide developers with “just-in-time” alerts, allowing defects to be resolved before the code is shared or integrated.

**Capabilities vs. limitations**

To understand the limitations of automation, it is important to distinguish differences between “Technical conformance” (what a machine can see) and “Functional usability” (what a human can experience).

| Feature | What automation can check? | What manual testing can verify? |
| :-- | --- | --- |
| Images | Does the \\<img\\> tag have an alt attribute? | Is the description meaningful and helpful in context? |
| Forms | Is there a \\<label\\> associated with the \\<input\\>? | Does the label clearly describe the expected input? |
| Headings | Is the heading structure (h1-h6) numerically sequential? | Do the headings logically describe the content sections? |
| Keyboard | Is an element technically focusable in the code? | Is there a visible focus indicator? Is there a keyboard trap? |
| Color | Is the mathematical contrast ratio sufficient? | Does the design rely *only* on color to convey meaning? |

**Limitations of automation for digital accessibility:**

* The “30-50% rule”. Current industry-standard automated tools can only detect approximately 30% to 50% of total WCAG violations. A “clean” automated report is not evidence of an accessible product.
* The noise of false positives. Automated tools may flag violations that are not actually barriers (e.g., reporting a contrast error on text that is positioned over a complex gradient or image background that the tool cannot parse). High rates of false positives can lead to “alert fatigue”, causing teams to ignore valid findings.
* False sense of security. Stakeholders might misinterpret a high “accessibility score” from an automated tool as a guarantee of legal compliance, leading to the neglect of essential user testing and assistive technology validation. Significant barriers (like keyboard traps or illogical tab order) often go undetected by automation.

### How to integrate test automation tools in software development lifecycle for accessibility testing

Effective accessibility testing is not a single event, but a continuous process integrated into the SDLC. The shift-left approach ensures that accessibility is treated as a core quality attribute from the very start of the project.

These are the following phases within the SDLC:

1. Requirements and Design phase
2. Implementation phase
3. Build and Integration phase
4. System Testing and Maintenance phase

**Requirements and Design phase**

Tools are mostly used by designers themselves

Accessibility testing begins before any code is written. During this phase, Design-system check tools are used to validate the “accessibility blueprint” of the application. These tools automatically audit color palettes and typography for contrast compliance within the design software. Additionally, annotation tools help designers document the intended focus order, heading hierarchy, and ARIA roles preventing potential accessibility “debt” from being designed into the product.

**Implementation phase**

The focus is on catching programmatic errors at the earliest possible moment)

* IDE extensions and Linters. These analyze source code in real-time, providing immediate warnings (similar to a spell-checker) that allow developers to correct errors while they are still working on the specific line of code;
* Unit and component tests. Automated accessibility engines can be integrated into unit tests to identify accessibility regressions in reusable components (such as buttons or navigation bars) before they are integrated into the larger system. For example, a test can be written to “fail” if a reusable modal component does not contain a specific ARIA role.

**Build and Integration phase:**

Automated checks are integrated into the deployment pipeline to ensure that new changes do not break existing accessibility features. This is achieved through two distinct types of enforcement:

* Commit and Push Hooks. There are local scripts that run baseline scans on the developer’s machine. If a scan identifies a critical error (e.g., a linter detects an image without an alternative text attribute), the hook literally stops the commit or push from happening. This prevents the defective code from ever reaching the server. This is a cheap and effective way to detect accessibility violations early.
* Quality Gates. These act as the “enforcer” on the server side (remote). When a Pull Request (PR) is raised, automated status checks evaluate the code in the development branch. There, games prevent the merging of that code into a protected branch (e.g., the main branch), if it fails to meet predefined accessibility criteria.

**System Testing and Maintenance phase** (possible once the UI is fully rendered and interactive)

Once the user interface is fully rendered and interactive, testers use full-page scanners to establish a baseline. These tools analyze the Document Object Model (DOM), including dynamic states that static analysis might miss. Furthermore, regular automated “crawls” of the production environment (automated scripts that navigate through internal links to audit every page of a site) are conducted to ensure that content updates (often performed by non-technical editors) haven't introduced new barriers.

**Strategic criteria for accessibility tool selection:**

When selecting and integrating tools for SDLC, the test team (often in collaboration with developers and accessibility specialists) should ensure that the chosen tools provide Technical Guidance for Remediation. Good integration does not just find a problem; it provides the project team with a clear path to resolution. This guidance typically includes:

* Technical context. The exact location of the issue in the code or DOM (e.g., line number or CSS selector).
* User impact. An explanation of the user barrier and the consequence of the defect (e.g., “Because this button lacks an accessible name, screen reader users are unable to identify its purpose and are blocked from completing the checkout process”). This information provides the necessary rationale for prioritizing remediation.
* Standards mapping. Clear reference to the specific WCAG Success Criterion that is being violated.
* Remediation advice. Specific technical recommendations for fixing the issue, which may include code snippets, ARIA implementation patterns, or links to verified developer documentation.

A tool that lacks *actionable guidance* often creates a “knowledge gap”, where developers know there is a problem but lack the accessibility expertise to solve it, leading to delayed remediation or incorrect fixes.

### The role and risks of Artificial Intelligence (AI) in accessibility testing

Artificial Intelligence (AI) and Machine Learning (ML) are increasingly integrated into accessibility tools to address the limitations of traditional, rule-based automation. While AI can “raise the ceiling” of what is detectable, it introduces unique challenges as well.

The role of AI in accessibility testing is constantly increasing. AI tools can use visual analysis (“computer vision”) to detect issues that code-based tools miss, such as missing focus indicators, poor visual grouping, or content that overlaps when zoomed.

Large Language Models (LLMs) and Generative AI (GenAI) can evaluate page context to suggest meaningful alternative text for images or more descriptive labels for form fields. Furthermore, GenAI “auto-fix” capabilities can accelerate remediation by generating suggested code corrections for common violations. AI tools can also analyze complex text and suggest simpler alternatives, supporting the “understandable” principle of WCAG. (Note: for a comprehensive understanding of testing AI systems and using AI in testing, learners should refer to the ISTQB Specialist Syllabus, Generative AI \[ISTQB_SYL_AI_GEN\] and AI Testing \[ISTQB_SYL_AI_TEST\]).

**Risks and challenges of AI-driven tools:**

| Probabilistic vs. deterministic results | While traditional automation is deterministic (if rule A is broken, then report B), AI is probabilistic, meaning it provides a “best guess” in a given situation. This can lead to unpredictable results or inconsistencies between accessibility scans. |
| :-- | --- |
| Hallucinations and inaccuracies | AI may generate incorrect descriptions (e.g., describing a “submit” button as a “search” button) or provide remediation code that is technically invalid or introduces new accessibility barriers. |
| Data privacy | Using AI tools often requires sending code or content to a third-party model, which can raise significant security and data privacy concerns for an organization. |
| The “experience” gap | AI lacks the lived experience of people with disabilities. It can simulate a technical check, but it cannot truly replicate the frustration or barriers encountered during real-world assistive technology usage. |

## Tools for accessibility testing

To execute a comprehensive accessibility testing strategy, testers must be aware of a broad range of specialized software. While automation provides a baseline of efficiency, a professional toolkit incorporates a Layered Tooling Strategy. This involves using different types of tools to evaluate different layers of the application, from the raw source code and design tokens to the final rendered interface and the actual user experience as perceived through assistive technology.

This section defines these tools by their technical purpose and implementation within the SDLC.

### Understanding the categories of tools available

To build a robust accessibility testing strategy, a tester must understand how to classify tools based on their technical capabilities rather than just their brand names. Classification is essential for identifying “coverage gaps” and ensuring the team is not over-relying on one type of check while neglecting others.

Accessibility tools are typically classified according to three primary criteria:

| Where it runs? | How it works? | Who uses it? |
| :-- | --- | --- |
| The environment | The nature of the check | The user persona |
| Tools range from source-code analyzers (linters) used by developers, to browser-based scanners used by QA, and system-level software like screen readers that interact with the entire operating system. | This distinguishes between: / Fully automated engines that follow binary rules / / Guided tools that provide visual aids to help a human make a judgment call / / Manual tools that require the tester to observe the interaction directly. | Tools are optimized for specific roles, including: / Designer-focused: Used during the Requirements and Design phase to ensure accessible foundations (e.g., contrast plugins, annotation tools). / Developer-focused: Integrated into coding environments to support shift-left technical fixes and automated remediation. / QA-focused: Designed for comprehensive audits, assistive technology validation, and defect management. / Content-focused: Focused on linguistic clarity and media accessibility (e.g., readability checkers). / End-user-focused: While primarily assistive in nature (e.g., screen readers), these tools are the primary interface for users with disabilities and are utilized by testers to validate real-world functional usability. |

Note: While these are the primary technical criteria for classification, other factors such as cost, licensing, platform compatibility, and reporting features are also considered when selecting tools for an organization.

**The Four Tool Categories**

Accessibility tools are organized into four categories to support a layered tooling strategy, which provides maximum defect detection and comprehensive coverage. This approach ensures that accessibility is verified at every technical level, from design through to production:

| Category 1 | Static Analysis & CI/CD tools | Ensuring the technical foundation is robust | Code/Source level |
| :-- | --- | --- | --- |
| Category 2 | Automated UI-based scanners & manual helpers | Evaluating the rendered User Interface | UI level |
| Category 3 | Assistive Technologies (AT) | Validating the real-world functional user experience | Operating system level |
| Category 4 | Cognitive and Readability tools | Verifying that content is clear and understandable | Content level |

**Mapping Criteria and POUR Principles to Categories**

While many accessibility tools identify issues that overlap across multiple areas, each category is defined by its primary technical environment and its core alignment with the POUR (Perceivable, Operable, Understandable, Robust) principles.

| Category | Primary environment | Evaluation method | Primary Persona | POUR principle alignment |
| --- | --- | :-- | --- | --- |
| Category 1: / Static Analysis & CI/CD | Source Code / Design | Automated | Developer / Designer | Robust (Core), Perceivable, Operable |
| Category 2: / UI Scanners & Helpers | Rendered UI | Automated / Guided | QA / Designer | Perceivable (Core), Operable, Robust |
| Category 3: / Assistive Technology | Operating System | Manual | QA / End-User | Operable (Core), Perceivable, Understandable |
| Category 4: / Cognitive & Readability | Content / UI | Guided / Automated | Content Editor | Understandable (Core) |

**Cross-Category Functionality and Relationship to POUR principles:**

The alignments above are not strictly separate. Accessibility testing is holistic, and tool categories frequently overlap in their coverage. Common examples of such overlap include:

* Many-to-many relationships.
  A single tool in Category 2 (UI Scanner) might catch a missing alternative text (Perceivable), a missing form label (Operable), and a syntax error in ARIA code (Robust).

* Category 1 & 2 overlap.
  Both identify structural and technical defects. While Category 1 catches them in the source code, Category 2 catches the same issues in the rendered UI, often while simultaneously checking visual attributes.

* Category 3 as a cross-validator.
  While primarily used to test Operability, AT is essential for verifying Perceivability (ensuring content is actually announced or displayed) and Understandability (verifying that announcements are logical and instructions are clear).

* Category 4 overlap.
  While focused on Understandable content, readability tools often identify issues that require changes to the design (Perceivable) or the technical structure of the text (Robust) to improve clarity.

### Category 1: Static Analysis & CI/CD tools

Category 1 tools operate at the source-code level or within the design environment. Their primary purpose is to ensure the technical foundation of the software is structurally Robust before it is even rendered. By integrating these checks into the development workflow, teams can identify and resolve defects early, significantly reducing the cost and effort of remediation.

**The Strategic Value of Static Analysis**

The shift-left philosophy is the primary driver for Category 1 tools. The cost of fixing an accessibility barrier increases significantly as the project moves toward production. A missing form label identified by a linter takes seconds to fix. The same issue identified during a manual audit of a production site may require a full development sprint to resolve.

**Typical Implementation Methods**

To align with the SDLC phases, Category 1 tools typically support two methods of implementation:

* IDE Extensions and Linters (real-time). These tools run inside the developer's Integrated Development Environment (IDE). They act as a “spell-checker” for accessibility, highlighting violations as the code is typed. This facilitates immediate correction during the Implementation Phase.
* CI/CD Pipeline Integration (Quality Gates). These tools run as part of the automated build process during the Build and Integration Phase. If a violation of a critical accessibility rule is detected, the build is configured to fail, preventing the code from being merged. This mechanism is known as a Quality Gate.

**Example: Static Analysis vs. UI-based (dynamic) scanning**

To understand the necessity of a layered tool strategy, a tester must distinguish between testing the “structural intent” (Category 1) and the “rendered outcome” (Category 2).

Scenario: A developer adds an image to a webpage.

Static Analysis (Category 1) checks the code to see if the \\<img\\> tag contains an \\<alt\\> attribute. It validates that the intent to provide a description exists in the source code. UI-based scanning (Category 2) scans the page after it is rendered in a browser. It might find that while the alt attribute exists in the code, a CSS style has accidentally hidden the image from screen readers, or a JavaScript error has prevented the description from loading.

In this example, Category 1 ensures the technical “blueprint” is correct, while Category 2 ensures the “final build” actually works as intended when combined with styles and scripts.

**Common technical validations and Persona relevance**

Category 1 tools serve both Designers (using design-system plugins) and Developers (using linters) by enforcing the “accessibility blueprint” before the UI is built:

* Structural Integrity. Verifying heading order and landmark presence (relevant to Designers for layout logic and Developers for semantic HTML).
* Attribute verification. Ensuring images have alt attributes and form inputs have associated \\<label\\> tags (relevant to Developers).
* ARIA validation. Checking roles and attributes against technical specifications (relevant to Developers).
* Duplicate identifiers. Detecting duplicate \<id\> attributes that break assistive technology associations.
* Visual baseline constraints. Checking color contrast and font sizes within design systems before implementation (relevant to Designers).

### Category 2: Automated UI-based scanners & manual helpers

Category 2 tools evaluate the rendered User Interface (UI). While Category 1 tools analyze the source code, Category 2 tools detect accessibility defects that occur when the application is fully rendered and interactive. This is critical for the Perceivable principle, as many barriers only become detectable once the final functional interface is generated.

**Capabilities of UI scanners**

UI scanners evaluate the interface at runtime, analyzing the Document Object Model (DOM) in browsers or the view hierarchy in native applications. This run-time evaluation identifies:

* Dynamic UI defects - accessibility errors in interactive elements (e.g., modals, menus, or dynamic screen updates) that are generated during usage and are absent from the static source code.
* Visual attribute validation - actual color contrast ratio and text visibility within the rendered UI, accounting for transparency, background images, or overlapping layers.
* State-dependent violations - defects that occur during specific user interactions, such as error messages that are displayed only after a failed input attempt.

**Guided testing with manual Helpers**

Manual Helpers are specialized tools that provide the tester with visual or technical data to support manual verification. They support human judgment rather than providing a binary pass/fail result.

* Color contrast analyzers - tools used to calculate the contrast ratio between foreground and background colors to ensure text, icons, and interactive components remain clearly distinguishable. These tools allow testers to verify conformance either by manually entering numerical color codes (e.g., HEX or RGB values) or by using a “dropper” tool to sample colors directly from the rendered interface. This ensures the Perceivable principle is met by verifying visual clarity against the actual background seen by the user.
* Visual inspection tools - they project technical metadata over the UI to assist the tester in verifying the heading hierarchy, the logical tab order, or the correct placement of accessibility landmarks.

Category 2 tools are practically applied as browser extensions for web-based testing or as platform-specific inspectors for native mobile and desktop applications. These tools are often integrated into staging environments as automated audit scripts. They establish the compliance baseline for the project by identifying programmatic defects that should be resolved before manual testing with Category 3 (Assistive Technology) begins.

### Category 3: Assistive Technologies (AT)

Assistive Technology (AT) refers to specialized software and hardware used to validate that a digital solution is Operable and Perceivable for users with disabilities. While automated tools evaluate technical code, AT testing is a manual process used to verify the functional user experience.

**The Accessibility Tree**

Automated scanners primarily evaluate the Document Object Model (DOM) or source code. In contrast, assistive technologies interact with the Accessibility Tree.

The Accessibility Tree is a specialized data structure generated by the browser or operating system from the underlying UI structure. It is a filtered version of the interface that contains only the information relevant to AT, such as names, roles, states, and properties of interactive elements. Visual-only information, such as purely decorative images or layout styles, is omitted to provide an efficient experience for the user. Testing with AT is required because browsers or operating systems may incorrectly map technical code to the accessibility layer, creating defects that automated scanners are unable to identify.

The following table explains the specific functional checks that testers perform using AT:

| Type of functional check | Description |
| :-- | --- |
| Structural and non-visual navigation | Verifying that the interface remains navigable using semantic structures (e.g., landmarks, headings) and logical focus order without relying on visual context. |
| Interactive control identification | Ensuring that interactive elements (buttons, links, form fields) correctly expose their name, role, and current state to the accessibility API for communication via AT. |
| Dynamic notifications and state changes | Confirming that background events, live updates, or programmatic state changes (e.g., a timer finishing, a file upload completion, or an element becoming expanded / collapsed) are correctly communicated to AT users. |
| Input methods and alternative devices | Validating that all functionality is triggerable using various interaction modes and devices (e.g., switch controls, voice commands, alternative keyboards) and ensuring no reliance on specific physical gestures or high-precision pointing. |
| Data entry and error management | Verifying that transactional feedback, such as field labels, instructions, and error messages triggered by user input, are correctly associated and communicated via AT to ensure users can complete tasks and recover from interaction mistakes. |
| Visual presentation and system settings | Verifying that the interface remains functional and readable when system-level accessibility settings are applied, such as high-contrast modes, large text scaling, or screen magnification. |
| Visual presentation and system settings | Verifying that the interface remains functional and readable when system-level accessibility settings are applied, such as high-contrast modes, large text scaling, or screen magnification. |

Assistive Technology supports the following areas:

* Visual support: screen readers (translating text to speech or Braille), refreshable Braille displays, and screen magnifiers.
* Motor support: switch Access (peripherals for step-by-step navigation), voice control software, and alternative keyboards.
* Auditory support: hearing aid compatibility tools, system-level visual notifications for sound, and software for managing captions/transcripts.
* Cognitive and learning support: reading assistants (to reduce visual clutter or highlight text), text-to-speech software (for auditory reinforcement of text), and simplified navigation interfaces.
* Speech support: augmentative and alternative communication (AAC) devices and software that allow users to produce speech via text or symbols.

A digital solution that conforms to automated checks but fails to function correctly when tested with Category 3 tools is considered *inaccessible*.

### Category 4: Cognitive and Readability tools

Category 4 tools focus on WCAG Principle 3: “Understandable”. These analyze written content for linguistic complexity, figurative language (metaphors/idioms), and clarity of instructions. Their primary goal is to ensure that information is accessible to users with cognitive disabilities, dyslexia, limited literacy, or those who are non-native speakers.

Category 4 tools primarily assist content authors/editors in performing specific types of checks (Linguistic and Readability Analysis) by utilizing linguistic metrics and automated evaluation methods. While these tools also provide value during the testing phase, they help to perform the following checks:

| Content analysis metrics | Description |
| :-- | --- |
| Syntactic and lexical complexity analysis | Tools analyze sentence structure and word choice. They identify syntactic issues, such as overly long or nested sentences, and lexical issues, such as the use of high-level jargon instead of plain language, providing suggestions for simpler synonyms to reduce the cognitive effort required to process information. |
| Readability metrics | Automated applications of established formulas (e.g., Flesch-Kincaid) provide an objective, numerical grade level for the content. This helps verify if the text matches the recommended reading level for the target audience (typically Grade 8 or lower). |
| Figurative language testing | Diagnostic tools identify non-literal language such as metaphors, idioms, or sarcasm. Tool users may also use automated translation as a manual diagnostic technique: if a phrase loses its intended meaning when translated into another language, it likely represents a cognitive barrier for neurodivergent users (who may interpret language literally) or non-native speakers. |

Category 4 tools also help to perform the evaluation of the interface through Content Simplification and Sensory Support. These tools modify the visual or auditory presentation of content to help users with ADHD, autism, or dyslexia focus on information and reduce cognitive load without distraction:

| Sensory and focus support | Description |
| :-- | --- |
| Focus assistants | Software that strips away “visual noise” such as advertisements, navigation menus, and sidebars, presenting only the core text in a clean, high-contrast format. |
| Visual anchoring | Tools that guide the eye through gradients or by highlighting specific lines or “parts of speech” (e.g., nouns vs. verbs) to improve reading comprehension and tracking. |
| Auditory reinforcement | “Read aloud” features that provide synchronized audio and visual tracking of text, supporting users who benefit from multi-sensory information delivery. |

**Consistency and predictability**

To support the Understandable principle, Category 4 tools assist in ensuring the interface remains predictable across the entire application by helping to perform specific checks:

* Terminology consistency. Ensuring the same terms are used for the same actions (e.g., consistently using “Purchase” rather than switching between “Buy”, “Checkout”, and “Order”).
* Instructional clarity. Analyzing instructions to ensure they do not rely on visual-only cues (e.g., “Press the circle to continue”) which can be confusing for those using cognitive support tools that modify layout.

**Target Personas**

While useful for testers, Category 4 tools are primarily optimized for Content Authors, UX Writers, and Marketing teams. By integrating these tools into the content creation process, organizations can ensure that “clear writing” is treated as a fundamental accessibility requirement.
