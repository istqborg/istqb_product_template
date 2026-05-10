# Accessibility testing activities – 105 minutes {#3}

#### Keywords

compliance, shift left

#### Domain specific keywords

(none)

#### Learning Objectives for Chapter 3: {.learning-objectives}

1. Introduction and Approach
    1. (K2) Explain the planning activities for establishing an accessibility test
1. Accessibility testing activities
    1. (K2) Describe the benefits of shift left in accessibility testing
    1. (K2) Understand how to perform accessibility testing
    1. (K2) Understand the process of accessibility audits as a method for evaluating compliance
    1. (K2) Explain the relevance of end-user testing in achieving a usable product
1. Step-By-Step Approach to End-User Testing
    1. (K2) Understand the purpose and approach adopted in end-user testing
1. Challenges and Frequent Errors in Accessibility Testing
    1. (K2) Understand the most frequent and serious errors in accessibility testing

## Approach to Accessibility Testing

![The image illustrates a circular diagram with key concepts such as Proactive A11Y Testing, Shift Left, Collaboration, Validation, Experience, Testing, and Expert User Testing, suggesting a process or workflow for enhancing accessibility and quality assurance. AI-generated content may be incorrect.](image2){width=8cm} This chapter defines the core activities required to ensure a product is accessible. It moves beyond simple defect hunting to discuss strategic iterative approaches as per the diagram (see below), including the importance of early intervention (shift left), the specific role of formal audits, and the critical necessity of involving people with disabilities in the testing process.

In the diagram, A11y is a numeronym for “accessibility.” The “a” and “y” bookend the word, while the 11 represents the letters in between.

### Planning activities for accessibility testing

Principal activities in accessibility test planning include:

* Prioritizing functionality and coverage
* Selecting tools
* Defining accessibility acceptance criteria
* Building know-how

**Functionality prioritization and coverage**

Determining which areas of the application has the highest risk to users with disabilities. High-traffic areas (e.g., homepages), critical paths (e.g., checkout, login), and complex interactive components (e.g., carousels, modals) are to be prioritized.

**Selecting tools**

Deciding on the set of tools. This involves selecting automated linting tools as part of the static code analysis for code-level checks, considering browser extensions for rapid page scanning and analysis, assistive technologies for screen reading, and other tools relative to the supported assistive peripherals.

**Defining Acceptance Criteria for digital solution accessibility**

Establishing clear acceptance criteria. For accessibility, “Done” usually means zero critical/blocking accessibility issues against the targeted WCAG conformance level (e.g., AA).

**Building know-how for accessibility testing**

Identifying if external consultants are needed and at what phase of the project, or if the internal quality assurance team requires training on specific accessibility testing.

## Accessibility testing activities

This section describes the primary activities involved in testing for accessibility, from integrating testing early in the development lifecycle to performing formal audits and involving end-users to ensure genuine accessibility.

### Benefits of shift left in accessibility testing

Shift-left is the practice of moving testing activities to earlier stages in the Software Development Lifecycle (SDLC). Traditionally, testing, including accessibility testing, was often performed late in the cycle, just before release. Shifting left means integrating accessibility considerations and testing from the very beginning and continuously during requirements, design, and development phases.

The benefits of adopting a shift-left approach for accessibility testing are significant:

* Reduced cost and effort**.** Identifying and fixing an accessibility defect during the design or early development phase is substantially cheaper and faster than remediating it in a fully developed product. Late-stage fixes can require architectural changes, regression testing, and redeployment, which increases costs. For example, ensuring correct color contrast in a design mockup costs less compared to changing colors in a live application, that can be a major change.
* Improved product quality and innovation. When accessibility is considered from the start, this leads to a more robust, higher-quality, and seamlessly accessible user experience with a built-in accessibility solution. It encourages the team to think inclusively, which can spark innovation and result in solutions that benefit all users, not just those with disabilities.
* Enhanced team awareness and culture. Integrating accessibility into daily activities (e.g., design reviews, code reviews, test case reviews) fosters a culture where accessibility is a shared responsibility. It builds knowledge and empathy across the entire team, making accessibility assurance a standard part of the definition of ready and definition of done.
* Faster time-to-market. By catching and resolving accessibility issues early and continuously, teams can avoid accessibility-related high-severity defects that can delay a product launch, and allows for more predictable and faster release schedules.
* Proactive risk mitigation. Addressing accessibility continuously reduces the legal risk associated with non-compliance with regulations such as the Americans with Disabilities Act (ADA) or the European Accessibility Act (EAA) (see chapter 2.2). It also mitigates the risk of reputational damage that can result from releasing an inaccessible product.

### How to perform accessibility testing

Performing accessibility testing is not a single activity but a multi-faceted process that combines automated, manual, and assistive technology testing techniques. A comprehensive strategy utilizes all three to achieve broad coverage.

**Automated testing**

This involves using specialized software tools to automatically scan a website or application's source code to find accessibility issues. These tools are excellent at detecting certain types of WCAG violations, such as missing alternative text (alt attribute in HTML) for images, missing form labels, insufficient color contrast, or incorrect ARIA attribute usage.

Automated tools can be run as imported into automation solution 3rd party libraries or browser extensions for quick checks, integrated into the Continuous Integration/Continuous Deployment (CI/CD) pipeline to catch issues automatically with every code change, or used for site-wide scans.

Automated tools can only detect a limited amount of all possible accessibility issues. For example, current technologies cannot assess the quality of alternative text, determine if the reading order is logical, or evaluate the overall usability of a process for someone using assistive technology. They are a starting point, not a complete solution, but they keep improving along with technologies.

**Manual testing**

This involves a tester systematically checking for accessibility issues that automated tools cannot identify. It requires a deep understanding of accessibility guidelines and how users interact with digital content.

Key manual checks include:

* Keyboard-only navigation. Testing that all interactive elements (e.g., links, buttons, forms) can be reached and operated using only certain keyboard keys (e.g., Tab, Shift+Tab, Enter, and arrow keys) and that the focus order is logical.
* Content magnification. Zooming in the page to a required percentage (depending on requirements) to ensure that content reflows correctly without requiring horizontal scrolling.
* Code inspection. Manually reviewing the HTML to check for semantic structure (e.g., correct use of headings, lists, landmarks, etc.) and proper ARIA implementation.
* Forms and error handling. Verifying that all form fields are properly labeled, assuring that error messages are clear, descriptive, and programmatically associated with the correct field.

**Assistive Technology (AT) testing**

This is a specialized form of manual testing where the tester uses the same assistive technologies that people with disabilities rely on. The goal is to evaluate the actual user experience when interacting with the product via AT.

This typically involves testing with the most common screen readers (e.g., commercial tools, OS built-in tools, open-source tools) to check if content is read out logically, if interactive elements are announced correctly, and if the user can navigate and complete tasks efficiently. It can also include testing with other AT like speech recognition software or screen magnifiers.

**Artificial Intelligence (AI) analysis**

AI usage is possible to detect complex pattern violations (e.g., verifying if \\<alt\\> text matches the image content) that standard automated testing tools might miss, and to save manual verification time. However, AI output requires thorough and rigorous human verification to avoid false positives or even false negative results.

### The process of accessibility audits as a method for evaluating compliance

An accessibility audit is a formal and comprehensive evaluation of a digital product (e.g., a website or mobile application) to determine its level of conformance with a specific set of accessibility standards, most commonly the Web Content Accessibility Guidelines (WCAG). Unlike ongoing testing, an audit is a structured, point-in-time assessment that results in a formal report.

The primary purpose of an audit is to provide a definitive statement on compliance and a clear, actionable roadmap for remediation.

The process of conducting an accessibility audit typically involves the following:

* Scope definition. This is to clearly define what will be audited. This includes:
  * The specific website, application, solution, or platform.
  * The targeted accessibility standard and version (e.g., WCAG 2.1, WCAG 2.2).
  * The targeted conformance level (A, AA, or AAA).
* Representative sample of pages/screens. It is based on business requirements and decisions. It can be that all pages/screens are candidates for audit. In some cases, it is impractical to audit every single page/screen of a large solution. Instead, a representative sample is selected. This sample should include:
  * The homepage and other high-traffic pages/screens.
  * Pages/Screens representing key user flows (e.g., login, search, checkout process, etc.).
  * Pages/Screens that contain a wide variety of content and components (e.g., forms, tables, multimedia, complex widgets, etc.).
  * Pages/Screens containing legal information and policies.
* Conformance evaluation. The audit team performs a thorough evaluation of the selected sample using a combination of automated, manual, and assistive technology testing methods (as described in Section 3.2.2). Every applicable success criterion from the target standard is checked against the sample pages/screens.
* Logging findings and prioritization of issues. Every identified issue is meticulously documented. Each finding should include:
  * A clear description of the issue and its location.
  * The specific WCAG success criterion that is violated.
  * The impact of the issue on users with different types of disabilities.
  * Recommendations for remediation.
  * Issues are often prioritized by severity (e.g., critical, serious, moderate) to help development teams address the most impactful problems first.
* Audit report generation. The final deliverable is a formal report that summarizes the findings. This report typically contains:
  * An executive summary stating the overall level of conformance.
  * The scope and methodology of the audit.
  * A detailed list of all identified issues and recommendations for fixing them.
  * A concluding statement on the product's overall accessibility.

### The relevance of end-user testing in achieving a usable product

End-user testing, also known as usability testing with people having disabilities, involves observing actual users with disabilities as they attempt to complete tasks on a product using their own assistive technologies. While an accessibility audit is critical for verifying technical conformance, end-user testing is essential for evaluating true usability.

Automated tools are heavily limited and typically only detect 30% to 50% of WCAG violations. A system can technically meet WCAG criteria but still be confusing and frustrating for a person with a disability to use it effectively. Therefore, end-user testing is not an optional add-on - it is the definitive method to bridge the gap between technical compliance and human-centered accessibility.

The relevance of end-user testing is rooted in its ability to bridge this gap:

* Reveal real-world barriers. End-user testing uncovers usability issues that automated tools and expert-led manual testing can miss. It provides insight into the practical challenges users face, which are influenced by their specific disability, their chosen assistive technology, and their personal interaction patterns. For example, a data table might be technically compliant, but a screen reader user might find it impossible to understand the relationships between headers and cells during a real-world task.
* Provides authentic context and empathy. Watching a real user struggle with a product provides invaluable context and builds empathy within the development team. Such direct feedback is far more powerful than a list of defects and helps teams to understand the “why” behind accessibility guidelines.
* Ensures solutions are effective. When a team implements a solution for an accessibility issue, end-user testing can validate whether the solution is genuinely effective and intuitive for the intended users.

End-user testing is necessary for moving beyond technical compliance to create products that are not only accessible but also genuinely usable and empowering for people with disabilities. It is the ultimate measure of whether a product delivers a desired experience for all users.

## Step-By-Step Approach to End-User Testing

### The purpose and approach adopted in end-user testing

The purpose of end-user testing is to validate the user experience (UX) with the people for whom the accessibility features are designed. It follows the principle “Nothing about us without us”.

The approach considers the following topics:

* Recruitment. Recruit participants with a diverse range of disabilities (visual, auditory, motor, cognitive) and different levels of technical proficiency.
* Protocol Design. Create tasks that focus on real user goals (e.g., “Find a product and buy it”) rather than specific accessibility checks. Allow users to use their own devices and setup.
* Facilitation:
  * Moderated: A facilitator observes the user (remotely or in-person) and asks questions. This provides the deepest insights.
  * Unmoderated: Users record themselves performing tasks. This is faster but offers less context on why a user struggled.
* Live observations and demonstrations. Make it as easy as possible for developers, designers, and managers to observe these sessions. Schedule them at convenient times or host live demonstrations where the team observes a user navigating the product with their assistive technologies. Witnessing real barriers first-hand is the fastest way to dissolve skepticism and secure team buy-in.
* Analysis. Distinguish between accessibility bugs (code errors) and usability issues (design flaws).
* Compensation. Always compensate participants fairly for their time and expertise.
* Privacy and data protection. Strict care must be taken to respect the privacy of participants. Because information regarding a person's disability can be considered sensitive medical or personal data (subject to regulations like GDPR), participants must be anonymized in all shared notes, videos, and reports.

## Challenges and Frequent Errors in Accessibility Testing

Even with good intentions, testing teams often fall into traps that undermine the quality of accessibility verification. These errors generally fall into two categories:

* Methodological errors (flaws in the process)
* Technical oversights (missing specific types of defects)

### The most frequent and serious errors in accessibility testing

The most frequent Methodological errors in accessibility evaluation are:

| Type of mistake | Description |
| :-- | --- |
| Over-reliance on test automation | Believing that a passing score on an automated tool means the site is accessible. This is the most common and dangerous error. Automation cannot detect issues like logical tab order, keyboard traps, or meaningful alt text. Although with the ongoing progress in AI, there are potential areas that could be better covered by automation in the future. |
| “Works on my machine” syndrome | Testing only with one screen reader / browser combination (e.g., TalkBack on Chrome) and assuming it works on others (e.g., VoiceOver on Safari). Various operating system combinations might have a big difference in overall accessibility as assistive technologies behave differently across platforms. |
| Ignoring focus management | Failing to test where the keyboard focus goes when a modal closes or a page updates dynamically. This is the biggest frustration for keyboard users. |
| “Overlay” solutions | Believing that installing a third-party “accessibility overlay” widget solves accessibility problems. These often interfere with assistive technology and do not fix the underlying code. |
| Late-stage testing | Treating accessibility as a final “checkbox” activity before release. This often leads to the discovery of fundamental architectural issues that are too expensive or risky to fix, resulting in “waivers” or known defects in production. |
| Allowing opinions to override facts | Treating accessibility as a subjective design choice (e.g., “The contrast looks fine to me” or “Nobody uses a keyboard here”). Valid accessibility problems may be dismissed because strong opinions dominate the discussion. Testing must be grounded in objective WCAG criteria and validated by real-world feedback from users with disabilities. |

The most frequent technical mistakes in accessibility evaluation are:

| Type of mistake | Description |
| :-- | --- |
| Misunderstanding ARIA | A common error is assuming “more ARIA is better”. Testers often miss that developers use ARIA to patch bad HTML (e.g., role=“button” on a \<div\>) instead of fixing the HTML itself. Excessive or incorrect ARIA can override native semantics and break functionality for screen reader users. |
| Ignoring focus management | Failing to test where the keyboard focus goes when a modal closes or a page updates dynamically. If focus is lost (reset to the top of the page), the user loses their place. This is the biggest frustration for keyboard users. |
| Dynamic Content Blindspots | In a single page application, content often updates without a page reload. Testers frequently forget to verify if these status changes (e.g., “Item added to cart”) are announced to screen readers. |
| Vague alternative (alt) text | Checking that images have an alt text, but not checking if the text is meaningful (e.g., accepting “image123.jpg”, “picture”, or redundant text like “Image of logo” as valid). |
| Zoom and reflow neglection | Forgetting to test the page at 200% or 400% zoom. Testers often miss that content may overlap, disappear, or require horizontal scrolling (which is a failure) at high zoom levels. |
| Testing without audio | Forgetting to test that visual cues (like error borders) are also conveyed programmatically or via text for those who cannot see color or the screen. |
