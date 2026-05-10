# Accessibility Testing Life Cycle – 210 minutes {#4}

#### Keywords

test planning

#### Domain specific keywords

accessibility conformance report (ACR) / VPAT, remediation

#### Learning Objectives for Chapter 4: {.learning-objectives}

1. Preparing an Accessibility Test
    1. (K2) Explain accessibility in test planning
    1. (K2) Explain the configuration requirements for accessibility tests
1. Executing Accessibility Tests
    1. (K2) Identify the applicable accessibility test tasks
1. Analyze and Communicate Findings
    1. (K4) Analyze the accessibility test results
    1. (K2) Explain typical criteria associated with findings
    1. (K3) Apply a given list of good practices to report and communicate test results
    1. (K2) Understand the purpose and structure of a formal accessibility report

## Preparing an Accessibility Test

To build truly inclusive digital products, accessibility testing should start as early as possible along with any other testing activity in the Software Development Life Cycle (SDLC). This chapter explores the practical application of accessibility testing, from initial planning and environment configuration through to test execution and stakeholder reporting. It will cover the preparation needed for digital accessibility testing, the core tasks of execution, and the vital process of turning test findings into actionable improvements.

### Factors to be considered in accessibility test planning

Integrating digital accessibility into test planning from the very beginning is crucial for efficiency and effectiveness. Rather than treating accessibility as a final separate check or phase, it should be a consideration throughout the entire project or product journey. While Chapter 3 outlines the high-level testing strategy and methods, this section focuses on creating the specific, actionable test plan for a given project or release.

A number of factors need to be considered when planning digital accessibility testing. These include the following:

* Identifying accessibility requirements
* Defining scope and objectives
* Determining test approach
* Planning resources and environments
* Defining roles and responsibilities
* Scheduling and integration

**Identifying accessibility requirements**

An accessibility requirement is a requirement regarding the accessibility of a component or system. It provides the basis for evaluating whether a digital product meets the needs of users with disabilities. Accessibility requirements typically come from a variety of sources:

* Explicit requirements. Clearly stated in requirements documentation, acceptance criteria, or a user story (e.g., “As a keyboard-only user, I must be able to navigate the checkout form without getting stuck”).
* Standard-based requirements. Included in adopted legal or international standards (e.g., “The application must conform to WCAG 2.2 Level AA”).
* Implicit requirements. Undocumented but widely accepted user expectations based on standard assistive technology behaviors (e.g., A screen reader user implicitly expects a website to use semantic HTML landmarks like \\<main\\> and \\<nav\\> to allow for quick page navigation, even if no user story explicitly asked for them).

**Defining scope and objectives**

* Conformance goals. Clearly state the target accessibility standard (e.g., WCAG 2.1, WCAG 2.2) and the desired conformance level (A, AA, AAA).
* Jurisdictional requirements. Identify any specific legal or regulatory requirements (e.g., Section 508 in the U.S., EN 301 549 in Europe).
* In-scope/Out-of-scope. Define which parts of the application, platform, or user journeys will be tested. This may involve prioritizing critical user paths, such as registration, core functionality, and contact forms.

**Determining test approach**

* Manual testing. Plan for checks that require human judgment, such as keyboard navigation, color contrast perception, and logical content flow.
* Assistive Technology (AT) testing. Planning for testing with specific screen readers that are integrated into operating systems or external ones, screen magnifiers, or voice control software.
* Automated testing. Integrating automated tools into CI/CD pipelines to catch common issues early (e.g., missing alt text, incorrect ARIA roles). It's important to acknowledge the limitations of automation (typically finding only ~30-50% of issues, e.g. limited vision-related tests are hard to test).
* End-user/user testing. Involve people with disabilities into testing activities to gain real-world feedback on usability and accessibility.

**Planning resources and environments**

* Team skills. Assess the team's knowledge of accessibility and planning for training, if needed. Awareness of disabilities is important.
* Tools and software. Allocate budget and time for necessary manual accessibility testing, automated tools and licenses for assistive technologies, as well as potential external resources for accessibility evaluation (e.g., user with disabilities)
* Test environment. Ensuring the test environment is configured to support accessibility testing, e.g. it is accessible for assistive technologies, test automation, etc.

**Defining roles and responsibilities**

Identifying who will conduct which parts of the testing and remediation process to ensure comprehensive coverage. Examples include:

* Tester / QA engineer. To execute routine automated and manual accessibility tests, log defects, and verify fixes (this is the core role executing the test plan).
* Developer. To consult on technical feasibility and implement accessible code and structural fixes.
* UX/UI Designer. To ensure visual and interactive elements (e.g., color contrast, focus states) meet accessibility standards prior to development.
* Accessibility expert / consultant. To act as a Subject Matter Expert (SME), resolve complex WCAG interpretations, guide the team, and conduct formal compliance audits.
* Product Owner / Business Analyst. To define explicit accessibility requirements, user stories, and acceptance criteria.
* User with disabilities (lived experience expert/end-user). To provide unique accessibility perception, validate real-world usability, and identify barriers that technical compliance alone might miss.

**Scheduling and integration**

* Entry and exit criteria. Define what must be ready before accessibility testing can begin (e.g., stable code, dedicated environment) and what defines completion (e.g., a certain percentage of issues resolved, accessibility conformance report (ACR) is created).
* Milestones. Integrating accessibility testing activities into project sprints and project milestones, from design reviews to pre-release and post-release checks.

### Explaining the configuration requirements for accessibility tests

A well-configured test environment is the foundation of reliable and repeatable accessibility testing. The setup must reflect the technology used by the target audience, as support for assistive technology can vary significantly across platforms.

A typical test environment configuration includes:

| Operating systems (OS) and Browsers | Identify and prepare the most common combinations of operating system & browser for your user base (e.g., Windows / Chrome, macOS / Safari, iOS / Safari, Android / Chrome, etc.) |
| :-- | --- |
| Assistive technologies (AT) | Screen readers: Install the primary screen readers for your target platforms. Tests should be performed using default AT settings to mirror a typical user's experience as the custom setups are not known. / Screen magnifiers: Be prepared to use built-in tools as well as the most popular software solutions in the market. / Voice control software: Configure native tools on various OS to test for hands-free interaction. / Other AT: You may also need to consider switch controls or Braille displays / keyboards. |
| Browser extensions | Install trusted accessibility-checking extensions to support rapid inspection during development and testing. |
| Device requirements | Testing on actual smartphones and tablets is crucial. Emulators cannot fully replicate the interaction between an operating system and its native AT. |
| Test data | Make sure user accounts and data sets cover all relevant application states and user roles (e.g., guest vs. authenticated user, admin vs. standard user) |

## Executing Accessibility Tests

Test execution is where planning meets practice. It requires an approach, which combines the speed of automated tools to find common issues as well as methodical and structured manual testing supported by digital accessibility testing practices to uncover the complex issues that automation cannot detect.

Accessibility test execution is not a single event but a series of activities that occur at different stages of the development process. A modern “shift-left” approach integrates accessibility checks early to catch issues before they become complex and expensive to fix. All the rest of human-led testing happens on a scheduled manner by following development practices and agreements.

### Identifying the applicable accessibility test tasks

The execution tasks listed below map directly to the testing methods (Automated, Manual, and AT testing) introduced in Section 3.2.2, applying them sequentially across the different stages of the CI/CD pipeline and testing lifecycle:

1. Build-time automated checks
2. UI-based automated scanning
3. Structured manual testing

**Build-time automated checks**

This is the first line of defense, executed automatically whenever new code is committed or a new build is created (e.g., within a CI/CD pipeline). These checks use static analysis tools (linters) to scan source code for known accessibility rule violations, such as a missing \\<alt\\> attribute on an \\<img\\> tag. The goal is to provide immediate feedback to developers, preventing basic accessibility defects from ever reaching the test environment. This is a highly efficient way to enforce foundational accessibility practices.

**UI-based automated scanning**

Once the code is deployed to a development or test environment and a user interface (UI) can be present, a second layer of automated testing is performed. This involves running various helpers and tools or other automated frameworks against the deployed solution. These tools analyze the rendered Document Object Model (DOM) to find issues that are only apparent once the UI is built. This scan provides a quick overview of common violations on a functional interface and establishes a baseline for the more in-depth manual testing that follows next.

**Structured manual testing**

This is a planned testing phase that requires human judgment to uncover the major accessibility issues that specialized software cannot detect. On a stable build, a tester systematically performs the following checks:

* Keyboard-only navigation testing
  Unplugging the mouse to ensure there is a visible focus indicator, a logical focus order, no keyboard traps, and that all interactive elements (buttons, links, form fields, menus) can be operated using only standard keystrokes (e.g., Enter, Spacebar, Arrow keys).

* Screen reader testing
  Launching a screen reader to simulate the experience of a user who is blind. This verifies that semantic HTML (headings, lists, landmarks) is used correctly, dynamic content updates (alerts, notifications) are announced without interrupting the user, and that images, form labels, and controls are announced accurately.

* Visual and content checks
  * Color contrast. Using analyzers to verify required contrast ratios based on the target conformance level (e.g., typically 4.5:1 for normal text at Level AA, and stricter ratios like 7:1 for Level AAA).
  * Zoom and reflow. Testing text resizing and viewport reflow against the target standard (e.g., scaling text to 200% or zooming the page to 400%). Testers must ensure content reflows into a single column without requiring horizontal scrolling, and that text spacing adjustments do not break the layout.
* Multimedia and safety checks
  Checking that audio/video content has accurate captions and audio descriptions/transcripts. Ensuring no content flashes more than three times per second to prevent seizures.

## Analyzing and Communicating Findings

The analysis and communication of test results effectively is paramount to ensure the correct changes are made. To do this a tester should apply good practices for reporting findings, analysis of accessibility test results, an explanation of common criteria associated with identified issues, and the development of an accessibility test plan.

### Analyzing the accessibility test results

Accessibility analysis at this stage involves a deep, critical evaluation of test findings which involves more than just listing findings. It requires investigating test results to understand the overall accessibility situation/status of the product, deconstruct complex standards, identify patterns, perform root cause analysis, and translate policy into actionable technical insights.

Key analysis activities include:

| Consolidating and verifying results | Gather raw findings from all testing methods (automated, manual, AT, user feedback) into a single location. The tester must critically evaluate automated results to filter out false positives and ensure manual findings are reproducible. |
| :-- | --- |
| Navigating and mapping to WCAG | Testers must be highly proficient in reading, interpreting, and applying the WCAG. / Deconstructing the standard / Testers must understand the WCAG hierarchy: Principles (POUR) -> Guidelines -> Success Criteria (SC) -> Sufficient / Advisory Techniques and Documented Failures. / Accurate mapping: For every defect found, the tester must analytically determine the most specific and accurate Success Criterion that has been violated. Misattributing an issue (e.g., logging a missing button role as a color contrast failure) leads to confusion and improper fixes. / Using supplemental resources: The normative WCAG text can be concise and legally binding. A skilled digital accessibility testing specialist should be aware they must actively consult the “Understanding WCAG” documents to grasp the underlying intent of a criterion and use the “How to meet WCAG” (Quick Reference) to find specific, acceptable technical implementations and known failures. |
| Formulating actionable developer guidance | WCAG is often policy-driven and can be difficult for developers to interpret directly. The digital accessibility testing specialist should act as a translator and supporter. / Guidance must be crystal clear regarding what the barrier is, why it fails the standard, and exactly how it should be fixed in the code. / Digital accessibility testing specialists should point development teams to specific, verified industry resources for solutions, such as the W3C's WAI-ARIA Authoring Practices Guide (APG) for complex widgets, or specific WCAG HTML / CSS techniques. |
| Root cause analysis | Not only identify the patterns in the issues found but identify systemic patterns in the issues found and not view them in isolation. / Examples of analytical thinking: / Is a missing ARIA label isolated to one page, or is it baked into a reusable component used across the entire application? / Is the issue caused by bad code (developer error), poor color choices (design error), or missing alt text on an uploaded image (content editor error)? / A recurring problem with form labels might point to a systemic issue in a shared component library rather than individual developer errors. / Pinpointing the root cause ensures the issue is routed to the correct team and fixed at the source and helps to propose more effective, long-term solutions. |
| Impact and severity assessment | Evaluate the impact of each issue on users. Severity is influenced by frequency (how often the problem occurs) and impact (how badly it blocks the user). / A serious issue might completely prevent a screen reader user from completing a critical task (e.g., making a payment), while another issue might be a minor annoyance (e.g., a slightly low-contrast decorative image). / A common severity assessment includes: / Critical / Blocker. Prevents a user from accessing core content or completing a critically important task. / High. Causes significant barriers or frustration for users but may have a workaround. / Medium. Creates an inconvenience or a sub-optimal experience. / Low. A minor issue that does not significantly impede the user experience (often caused by a technical best practice violation). |
| Trend analysis | Comparing current findings with previous accessibility test reports to detect trends and frequently occurring accessibility problems across releases. |
| Mapping to accessibility standards | For each issue, map it directly to the specific WCAG Success Criterion it violates. This is essential for formal reporting, but not less important for providing clear guidance and reasoning to developers. This requires the ability to properly read and understand the WCAG which enables us to apply WCAG to the solution that is being developed. |

### Typical criteria associated with findings

Each finding reported should be documented with a consistent set of criteria to ensure it is clear, understandable, and actionable.

Typical criteria for documenting an accessibility finding include:

| Title | A concise summary of the issue. (e.g., “Checkout button is not keyboard accessible”). |
| :-- | --- |
| Description | A clear, non-technical explanation of the issue and why it is a barrier accessibility-wise. |
| Environment | The OS, browser and assistive technology used during the test (including version numbers and any additional digital solution-related detail). |
| Steps to reproduce | A numbered list of steps that a developer can follow to replicate and observe the issue. |
| Evidence | A visual evidence demonstrating the issue. A short video is often invaluable for demonstrating screen reader behavior or problems with focus order. / Note about privacy requirements: if evidence includes recordings of users with disabilities, the participant must be anonymized to protect sensitive personal and medical data. |
| Actual result | A description of the observed, incorrect behavior. |
| Expected result | A description of the correct behavior. |
| WCAG Success Criterion | The specific WCAG guideline and success criterion that is violated. |
| Impact on users | A brief explanation of how this issue affects people with specific disabilities (e.g., "This prevents keyboard-only users and screen reader users from completing their purchase."). |
| Suggested remediation | A clear recommendation on how to fix the issue. This could include code snippets, links to design patterns (like ARIA), or specific technical guidance. If the remediation is not obvious and needs deeper analysis and / or investigation, links to the development guidelines on how to meet the WCAG would be recommended. |

### Good practices in reporting and communicating test results

Effective communication is key to ensuring that accessibility issues are understood and addressed. The goal is to be a collaborative partner, the enabler to overcome the issues, not just a defect finder.

A digital accessibility tester should be able to apply good reporting practices:

* Foster collaboration and empathy
* Manage defensive reactions with objective facts
* Adapt to the organization's accessibility maturity
* Tailor defect report to different audiences
* Be constructive and educational
* Use a combination of reporting formats
* Focus on solutions, not just problems
* Report positive findings
* Track and measure progress

**Foster collaboration and empathy**

Involve cross-functional team members (developers, designers, product managers) directly in the testing activities. Inviting them to observe live testing sessions - especially end-user testing - is a highly effective way to build empathy and a shared understanding of the barriers users face. Make it easy for them to participate by organizing informal live observation sessions, scheduling them at convenient times, and emphasizing that even observing a partial session is valuable. Communicate clearly and tailor the terminology to the audience, avoiding overly dense accessibility jargon when discussing user impact with non-technical stakeholders.

**Manage defensive reactions with objective facts**

In situations involving conflict or pushback, the tester must wear the hat of Objective Auditor. Stakeholders who are not accessibility professionals often need to be convinced to take findings seriously. Some developers or designers may view the user interface as an extension of their own work and react defensively when faults are found. When communicating defects, care must be taken to manage the exchange of opinions. If stakeholders have strong subjective opinions (e.g., “Nobody uses a keyboard for this menu”), the tester must skillfully shift the conversation from subjective opinions to objective facts. Mitigate these risks by relying heavily on normative WCAG criteria and video recordings of actual users struggling with the barrier.

**Adapt to the organization's accessibility maturity**

The W3C Accessibility Maturity Model (see section 2.2.3) defines how well an organization integrates accessibility into its culture and processes. A tester must understand this maturity level to communicate effectively. In organizations with low accessibility maturity, the tester will need to spend more time advocating, explaining the “why” behind accessibility, and educating the team on legal or business risks. In high-maturity organizations, stakeholders already have buy-in, allowing the tester to focus strictly on technical compliance and advanced UX improvements.

**Tailor defect report to different audiences**

In the defect report for Developers, provide detailed technical defect report with code-level issues and, ideally, suggestions or guidelines on how to fix them. Provide the exact accessibility success criterion that is not being met so that Developers could get into more details when applying good accessibility development practices.
When reporting to Product Managers or executive level audiences, present a high-level summary dashboard with key metrics, risk assessments, and prioritization.
In the early phase of accessibility evaluation for Designers, focus on visual issues like color contrast, focus indicators, landmarks, and overall logical layout. It is expected though that designers will do an early design accessibility evaluation during the design phase.

**Be constructive and educational**

Beyond simply reporting defects, the tester should also assume the role of Accessibility Coach and focus on team mentoring. To explain the reasoning, increase empathy and build long-term motivation, present findings as opportunities for improvement rather than failures. Explain the “why” behind each issue by linking it to the actual user impact. Provide links to reliable resources (e.g., WCAG documentation, WAI-ARIA Authoring Practices Guidelines or APG) to empower the team to learn and grow their own accessibility skills.

**Use a combination of reporting formats**

There are different ways to report the issues depending on the project phase and project need. The accessibility issues to be reported using the dedicated defect tracking system. Log individual, actionable tickets with all the criteria listed in Section 4.3.2 above.

For the formal accessibility report, prepare a Formal Test Report/ACR. Create a summary document that outlines the scope, methodology, overall conformance level, and a summary of key findings.
In various circumstances, live demonstrations are very practical. Schedule a meeting to walk through the key findings with the development and product teams. Demonstrating an issue with a screen reader or any other assistive technology live is often more impactful than a written report.

**Focus on solutions, not just problems/issues**

Work with developers and designers to brainstorm and validate solutions. Help to re-test fixes and provide positive feedback when issues are resolved correctly. Product Manager input is as important from the business side as the insights from developers and designers.

**Report positive findings**

Accessibility audits can often feel like a long list of failures for the development team. Always highlight features that work well in summaries and presentations (e.g., “The application's focus management and color contrast are excellent across all pages”). Including positive findings provides a balanced view, boosts team morale, and ensures developers know which accessible features and patterns should not be modified or deleted.

**Track and measure progress**

Use dashboards to track the number of open vs. closed accessibility issues over time. Monitor trends to see if the number of new issues being introduced is decreasing, indicating that the team is learning and improving.

### The purpose and structure of a formal accessibility report

While defect tracking systems manage the day-to-day resolution of individual accessibility issues, formal accessibility test reports serve a broader purpose. They provide a comprehensive, point-in-time snapshot of a product's overall compliance level. These reports are essential for communicating accessibility posture to stakeholders, meeting legal or regulatory requirements, and supporting procurement processes. Understanding the different types of formal reports and their structures ensures that the right information reaches the right audience.

**Formal Reporting Formats: Internal vs. External**

Unlike daily bug logging during active sprints, formal reporting is typically required for comprehensive evaluations conducted when a product (or a major version) reaches a stable phase, often preceding a final audit or release. It is crucial for testers to distinguish between internal reporting (used for remediation) and external reporting (used for compliance proof):

* Internal Accessibility Audit Report. Created for the product and engineering teams. This report contains the granular, detailed logging of issues (following the exact criteria outlined in DAT-4.3.2, including exact URLs, steps to reproduce, and code-level remediation guidance). This serves as the master backlog for developers to fix the remaining defects.
* Accessibility Conformance Report (ACR). Often created using the VPAT® template, this is a formal, high-level document used for procurement, legal compliance, and public transparency. Rather than detailed bug reproduction steps, it provides a summary of support (e.g., “Supports”, “Partially Supports”) alongside high-level remarks for each WCAG criterion. Because it often serves as a public-facing or legally significant document for procurement and compliance proof, the responsibility for creating the ACR typically falls to the Accessibility Expert / Consultant or a senior Tester / QA Engineer specializing in accessibility.

**Formal Accessibility Test Report (ACR) structure:**

To ensure clarity, transparency, and completeness for stakeholders and procurement, the formal Accessibility Conformance Report (ACR) typically contains:

* Executive summary. A high-level overview of the evaluation object, the standards targeted (e.g., WCAG 2.2 AA), the most important findings, and general recommendations for decision-makers.
* Scope and purpose. Explicitly state which URLs, applications, or user journeys were in-scope and the specific accessibility requirements evaluated.
* Evaluation method & environment. Detail the specific combinations used (e.g., NVDA + Chrome on Windows 11, physical iOS device with VoiceOver) and whether automated, manual, or user testing was performed.
* Roles and contacts. Name and contact details of the testers, accessibility experts, and any users with disabilities involved in the evaluation (referencing the roles defined in test planning).
* Privacy Requirement. Users with disabilities involved in testing must be anonymized to protect sensitive personal and medical data.
* Summary of Conformance (Findings). A high-level logging of support levels (e.g., “Supports”, “Partially Supports”, “Does Not Support”) for each WCAG criterion, accompanied by general remarks and explanations, rather than detailed developer bug logs.
