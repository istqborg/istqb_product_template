# metadata
lo: 1.1.1
k-level: K2
points: 1
correct: a

## question
A website provides all navigation and product information only through images without alternative text descriptions. What accessibility concept is being violated in this situation?

## answers
a) The system fails to provide equal access to information for all users
b) The system lacks sufficient graphical design consistency across the user interface
c) The system prevents users from completing their tasks with efficiency
d) The system limits the overall emotional satisfaction of the target user base

## justification
a) Correct. Digital accessibility requires equal access to information for users with disabilities.
b) Incorrect. Visual design consistency is not the core accessibility issue.
c) Incorrect. Efficiency relates more to usability than accessibility.
d) Incorrect. Emotional satisfaction is related to user experience rather than accessibility.

# metadata
lo: 1.1.2
k-level: K2
points: 1
correct: c

## question
A test team is observing lived-experience experts performing typical tasks to ensure they are not blocked from using the core functionality. What is the primary objective of this specific type of evaluation?

## answers
a) To assess general usability efficiency and learnability for all users
b) To measure overall emotional satisfaction with the product experience
c) To identify accessibility barriers affecting users with disabilities
d) To verify that the software meets standard performance metrics

## justification
a) Incorrect. Assessing general efficiency and learnability is a usability evaluation activity.
b) Incorrect. Emotional response relates to user experience (UX) evaluation.
c) Correct. Observing users with disabilities directly helps identify specific accessibility barriers, which is the primary objective of accessibility evaluation.
d) Incorrect. Performance testing addresses system scalability, not accessibility.

# metadata
lo: 1.1.3
k-level: K2
points: 1
correct: d

## question
During the project initiation phase, a development team officially decides that their new software must meet WCAG 2.2 Level AA requirements before it can be released to the public. Which accessibility testing principle does this decision demonstrate?

## answers
a) Creating and adapting internal guidelines for accessible UI design
b) Training the development teams on accessibility tools and techniques
c) Executing focused accessibility testing on specific areas of concern
d) Defining the ambition level for accessibility based on a standard

## justification
a) Incorrect. They are adopting an external standard, not yet creating internal guidelines.
b) Incorrect. Training occurs after the target is set.
c) Incorrect. Test execution happens much later in the lifecycle.
d) Correct. Establishing a specific WCAG conformance level (Level AA) is the practical application of defining the target accessibility ambition level.

# metadata
lo: 1.2.1
k-level: K2
points: 1
correct: a

## question
A user is attempting to activate extremely small buttons on a mobile app but struggles due to hand tremors. Which disability category is most relevant?

## answers
a) Mobility or physical disability affecting motor control
b) Visual disability affecting perception of screen content
c) Cognitive disability affecting the understanding of tasks
d) Situational disability caused by the user's direct environment

## justification
a) Correct. Hand tremors and the inability to activate small touch targets are related to mobility and physical disabilities affecting motor control.
b) Incorrect. The user can perceive the buttons, but cannot physically interact with them.
c) Incorrect. The barrier is physical interaction, not mental processing or comprehension.
d) Incorrect. Hand tremors are a personal physical condition, not an environmental situational barrier (such as attempting to use a phone with one hand while holding a baby).

# metadata
lo: 1.2.2
k-level: K2
points: 1
correct: b

## question
A software development team adopts a philosophy that users are not limited by their physical conditions, but rather by poorly designed interfaces. Consequently, they build software that proactively supports various assistive technologies. Which disability paradigm does this approach reflect?

## answers
a) The Charity model
b) The Social model
c) The Medical model
d) The Rehabilitation model

## justification
a) Incorrect. The charity model frames disability as a tragedy requiring pity, which is irrelevant to accessible software design.
b) Correct. The social model argues that systemic and environmental barriers (like inaccessible software) disable people, and emphasizes adapting the environment to the user.
c) Incorrect. The medical model focuses on “fixing” the individual's impairment rather than adapting the environment.
d) Incorrect. This is not a recognized model in the syllabus.

# metadata
lo: 1.3.1
k-level: K2
points: 1
correct: d

## question
A company releases a critical update to its e-commerce website. A week later, they receive a formal complaint stating that the new checkout flow cannot be navigated using a screen reader, violating national accessibility regulations. Which category of risk does this specific situation represent?

## answers
a) Technical risk related to the use of non-standard UI components
b) Operational risk related to insufficient management attention to defects
c) Usability risk related to significantly increased frustration for all users
d) Legal and regulatory risk resulting from accessibility non-compliance laws

## justification
a) Incorrect. While non-standard UI components might be the source, the scenario specifically describes a formal complaint under regulations, which is the legal impact.
b) Incorrect. This is an organizational project risk, not the business impact described.
c) Incorrect. While usability is impacted, a formal regulatory complaint elevates this directly to a legal risk.
d) Correct. Formal complaints and non-compliance with accessibility laws directly represent legal and regulatory risks.

# metadata
lo: 2.1.1
k-level: K2
points: 1
correct: c

## question
A development team is creating a mobile banking application. They review accessibility guidelines recommending touch targets of at least 44×44 pixels and avoiding the use of color to convey information. What is the primary purpose of applying such accessibility guidelines?

## answers
a) To establish the mandatory legal penalties for accessibility violations across all jurisdictions
b) To replace formal accessibility audits performed by external compliance evaluators
c) To provide objective criteria and practical recommendations for creating accessible software
d) To guarantee automatic WCAG Level AAA compliance strictly for mobile devices

## justification
a) Incorrect. Laws establish legal penalties, not technical design guidelines.
b) Incorrect. Guidelines support testing and audits but do not replace the need to perform them.
c) Correct. Guidelines provide criteria and practical recommendations for accessible design.
d) Incorrect. Guidelines cannot guarantee automatic compliance, and 44x44px is an AA, not AAA, requirement.

# metadata
lo: 2.2.1
k-level: K2
points: 1
correct: b

## question
An organization developing software for the European market must comply with EN 301 549 accessibility requirements. What role does this standard play?

## answers
a) It defines specific financial penalties organizations face for failing accessibility audits
b) It defines technical accessibility requirements for digital products in the public sector
c) It acts as a direct substitute, entirely replacing global accessibility guidelines like WCAG
d) It applies exclusively to private sector software organizations operating on a global scale

## justification
a) Incorrect. The standard provides technical requirements, not legal or financial penalties.
b) Correct. EN 301 549 defines the accessibility requirements for ICT products and services, primarily in the European public sector.
c) Incorrect. The standard explicitly references WCAG 2.1, it does not replace it.
d) Incorrect. The European Accessibility Act (EAA) targets the private sector, EN 301 549 is primarily for the public/semi-public sector.

# metadata
lo: 2.2.2
k-level: K2
points: 1
correct: c

## question
A guideline in ISO 9241-171 recommends that interface element names should be available to assistive technologies. What is the goal of this guidance?

## answers
a) Ensuring the software automatically passes all WCAG Level AA automated code scans
b) Reducing the overall number of complex interface components used in the application
c) Ensuring assistive technologies can programmatically interpret and announce the interface elements
d) Replacing the need to use standard structural HTML landmarks during web development

## justification
a) Incorrect. Naming elements is necessary, but it does not automatically guarantee a pass for all Level AA criteria.
b) Incorrect. The guideline ensures elements are identifiable, it does not aim to reduce their quantity.
c) Correct. Assistive technologies (like screen readers) rely on accessible, programmatic names to correctly interpret and announce elements to the user.
d) Incorrect. Accessible names do not replace the need for structural landmarks.

# metadata
lo: 2.2.3
k-level: K2
points: 1
correct: b

## question
A guideline states that users must be able to interact with all interface functions through keyboard input. Which WCAG principle does this requirement primarily support?

## answers
a) Perceivable
b) Operable
c) Understandable
d) Robust

## justification
a) Incorrect. Perceivable focuses on perceiving information.
b) Correct. Operable means users must be able to interact with interface components.
c) Incorrect. Understandable relates to clarity of information.
d) Incorrect. Robust concerns compatibility with assistive technologies.

# metadata
lo: 2.2.4
k-level: K2
points: 1
correct: b

## question
A web application provides a visible button that allows users to pause a rotating image carousel. According to typical WCAG criteria, what is the primary accessibility purpose of this specific requirement?

## answers
a) To guarantee that the application automatically passes all automated accessibility source code evaluations
b) To allow users with cognitive or reading disabilities adequate time to process the provided information
c) ​​To ensure that assistive technologies can programmatically determine the default language of the application
d) To reduce the overall server processing load generated by continuously rendering dynamic screen graphics

## justification
a) Incorrect. Implementing a pause button does not guarantee that the rest of the application will automatically pass an automated scan.
b) Correct. WCAG requires that moving, blinking, or scrolling information can be paused, stopped, or hidden so that users with reading or cognitive disabilities have enough time to process the content.
c) Incorrect. Programmatically determining language is a completely separate WCAG requirement that relies on HTML tags (like *lang=”en”*), not a pause button.
d) Incorrect. Reducing server processing load is a performance optimization concern, not a digital accessibility requirement.

# metadata
lo: 3.1.1
k-level: K2
points: 1
correct: b

## question
During planning, the team decides to test login, checkout, and high-traffic landing pages first. What is the main reason for this decision?

## answers
a) These specific components are significantly easier to evaluate using automated accessibility scanning tools
b) These critical user flows represent a higher risk and impact if they remain inaccessible
c) These informational sections require far less manual testing effort than standard static content pages
d) These selected components contain far fewer dynamic content updates than the rest of the site

## justification
a) Incorrect. Ease of automation is not the main reason for prioritization.
b) Correct. High-traffic and critical flows create greater risk for users with disabilities.
c) Incorrect. Critical flows often require more testing effort.
d) Incorrect. Dynamic content is not the primary prioritization factor.

# metadata
lo: 3.2.1
k-level: K2
points: 1
correct: d

## question
A design team corrects color contrast issues in mockups before development begins. Which shift-left benefit does this best demonstrate?

## answers
a) Legal compliance is guaranteed without requiring any further testing activities
b) Automated scanning tools can be completely removed from later test phases
c) Accessibility validation becomes an optional step during final user testing
d) Early issue resolution significantly reduces subsequent remediation cost and rework

## justification
a) Incorrect. Compliance still requires verification.
b) Incorrect. Automation remains necessary throughout development.
c) Incorrect. Accessibility must be validated continuously.
d) Correct. Fixing issues early is significantly less costly than fixing them later.

# metadata
lo: 3.2.2
k-level: K2
points: 1
correct: b

## question
An automated scan reports no errors, but a keyboard user cannot close a modal dialog. What does this situation demonstrate?

## answers
a) Automated accessibility tools can fully evaluate and verify all user interaction logic
b) Manual accessibility testing is necessary to detect complex keyboard-related interaction issues
c) Standard WCAG accessibility guidelines do not explicitly address keyboard navigation requirements
d) Commercial accessibility overlays can automatically resolve these specific interaction logic problems

## justification
a) Incorrect. Automation cannot fully evaluate interaction behavior.
b) Correct. Keyboard navigation traps and issues require manual verification.
c) Incorrect. WCAG includes strict keyboard accessibility requirements.
d) Incorrect. Overlays do not fix underlying code defects.

# metadata
lo: 3.2.3
k-level: K2
points: 1
correct: d

## question
Why might an audit team select a representative sample instead of every page?

## answers
a) Automated scanning tools are technologically incapable of evaluating entire websites
b) Official WCAG guidelines explicitly permit auditors to skip critical journeys
c) Formal documentation requirements decrease significantly when page sampling is utilized
d) Large systems require an efficient evaluation strategy across diverse templates

## justification
a) Incorrect. Tools can scan widely but do not replace the need for manual audits.
b) Incorrect. Critical user journeys must always be included.
c) Incorrect.
d) Correct. Documentation for the sample must still remain comprehensive.

# metadata
lo: 3.2.4
k-level: K2
points: 1
correct: a

## question
A screen reader user struggles to interpret a technically compliant data table. What does this situation highlight?

## answers
a) Technical compliance with standards may not always ensure practical usability
b) Strict WCAG compliance automatically guarantees an intuitively usable interface design
c) Qualitative end-user testing completely replaces the need for structured audits
d) Automated accessibility testing should be avoided entirely in modern development

## justification
a) Correct. Real-world usability testing may reveal barriers that technical compliance missed.
b) Incorrect. Compliance ensures access, but does not guarantee ease of use.
c) Incorrect. Audits and end-user testing complement each other.
d) Incorrect. Automation remains highly valuable for baseline checks.

# metadata
lo: 3.3.1
k-level: K2
points: 1
correct: c

## question
Why should participants use their own assistive technologies during end-user testing?

## answers
a) It significantly reduces the need for facilitator involvement during testing sessions
b) It guarantees a much faster completion time for the assigned usability tasks
c) It accurately reflects authentic user interaction patterns and realistic software configurations
d) It completely eliminates functional differences between various hardware operating systems

## justification
a) Incorrect. Facilitation is still necessary to gather insights.
b) Incorrect. Speed is not the primary objective of accessibility testing.
c) Correct. Authentic setups reveal realistic interaction behaviors and user preferences.
d) Incorrect. Platform and OS differences still exist and must be accounted for.

# metadata
lo: 3.4.1
k-level: K2
points: 1
correct: d

## question
A developer adds multiple ARIA roles to a `div` instead of using semantic HTML elements. Why is this problematic?

## answers
a) ARIA attributes automatically correct underlying improper HTML structure within the application
b) ARIA implementations completely replace the need for strict keyboard accessibility requirements
c) ARIA attributes must be strictly applied to every single interactive component
d) Excessive ARIA usage may override native semantics and confuse assistive technology

## justification
a) Incorrect. ARIA does not fix DOM structural problems.
b) Incorrect. Keyboard accessibility is still required even if ARIA is used.
c) Incorrect. ARIA should only be used when native HTML is insufficient.
d) Correct. Incorrect or excessive ARIA use breaks expected screen reader behavior.

# metadata
lo: 4.1.1
k-level: K2
points: 1
correct: a

## question
During accessibility planning, the team defines WCAG 2.2 AA as the target conformance level and identifies registration and checkout as priority user flows. Which planning activities are illustrated?

## answers
a) Defining the overall accessibility testing scope and the target conformance objectives
b) Configuring the assistive technology software and the necessary test browser combinations
c) Performing automated accessibility scanning of the underlying application source code
d) Conducting the final formal accessibility audits required for standard legal certification

## justification
a) Correct. Planning explicitly includes defining the scope (flows) and conformance targets (WCAG).
b) Incorrect. Environment configuration occurs later during setup.
c) Incorrect. Automated scanning is part of execution, not planning.
d) Incorrect. Audits occur at the end of testing activities.

# metadata
lo: 4.1.2
k-level: K2
points: 1
correct: a

## question
A tester prepares an environment with Windows/Chrome, macOS/Safari, and Android/Chrome combinations. What is the main reason for preparing these configurations?

## answers
a) Assistive technology behavior and compatibility vary significantly across operating systems and browsers
b) Different hardware operating systems are governed by completely separate accessibility legislation
c) Automated accessibility testing tools require separate, dedicated databases for each platform
d) Standard performance testing metrics must run simultaneously on all supported test environments

## justification
a) Correct. Assistive technology compatibility varies by OS and browser combination.
b) Incorrect. Legislation applies to the service, not the OS.
c) Incorrect. Databases are unrelated to accessibility environment setup.
d) Incorrect. Performance testing is not the primary reason for these setups.

# metadata
lo: 4.2.1
k-level: K2
points: 1
correct: c

## question
After deploying the application to a test environment, the team runs a tool that analyzes the rendered DOM to detect accessibility violations. Which accessibility testing task does this represent?

## answers
a) Structured manual accessibility evaluation executed directly by testers with lived experience
b) Build-time static accessibility code analysis run systematically within the developer IDE
c) UI-based automated accessibility scanning analyzing the fully rendered user interface
d) Formal accessibility compliance reporting activities conducted right before the final release.

## justification
a) Incorrect. Manual evaluation requires human interaction, not a DOM scanning tool.
b) Incorrect. Static analysis occurs on raw code before UI deployment.
c) Correct. UI-based scans analyze the DOM and rendered interface after deployment.
d) Incorrect. Reporting occurs after analysis is complete.

# metadata
lo: 4.3.1
k-level: K4
points: 1
correct: b

## question
You are analyzing the test results for a newly developed e-commerce platform: \* The automated scanner reports 50 missing *alt* attributes on product images; \* The manual keyboard test passes all focus and navigation checks; \* During screen reader testing, the user hears “image, unlabelled” on every product card. What is the most appropriate analytical conclusion?

## answers
a) The screen reader software is malfunctioning and incorrectly ignoring the provided alternative image text
b) A systemic defect in a shared UI product card component is causing missing alternative descriptions
c) The automated scanner generated false positives because all of the images are purely decorative
d) The manual keyboard testing phase was executed incorrectly and missed critical navigation barriers

## justification
a) Incorrect. The screen reader is not malfunctioning - the automated scanner confirms that the *alt* attributes are genuinely missing from the code.
b) Correct. Root cause analysis reveals that 50 identical errors on identical elements (“product cards”) indicate a systemic defect in a reusable UI component.
c) Incorrect. If coded as decorative, the AT would ignore them. Hearing “image, unlabeled” proves they are not properly coded as decorative.
d) Incorrect. Keyboard navigation testing focuses on tab order and interactive focus, which is completely unrelated to missing image descriptions.

# metadata
lo: 4.3.2
k-level: K2
points: 1
correct: d

## question
An accessibility defect report includes a short summary, environment details, reproduction steps, and the violated WCAG criterion. What is the main purpose of including these criteria?

## answers
a) To completely automate the subsequent process of fixing the reported accessibility defects
b) To significantly reduce the overall number of accessibility defects being generated and reported
c) To simplify the legal interpretation of complex national accessibility legislation and standards
d) To accurately ensure reported findings are clear, fully reproducible, and highly actionable

## justification
a) Incorrect. Fixing defects still requires manual developer work.
b) Incorrect. Reporting structure does not reduce the actual count of defects.
c) Incorrect. Legal interpretation is unrelated to standard defect reporting.
d) Correct. Structured criteria ensure findings can be accurately reproduced and resolved.

# metadata
lo: 4.3.3
k-level: K3
points: 1
correct: a

## question
A development team repeatedly rejects an accessibility defect related to keyboard focus management, claiming they cannot reproduce the issue using their standard `div`unit`div` testing tools. Which communication practice should the tester apply to resolve this situation?

## answers
a) Schedule a live demonstration using a screen reader to show the exact impact on user navigation
b) Update the formal defect report to include the specific financial penalties for non-compliance
c) Forward the automated accessibility scanner logs to the development `div`manager`div` for mandatory review
d) Close the defect in the tracking system and rely on an accessibility overlay software solution

## justification
a) Correct. Live demonstrations build developer empathy and prove the real-world impact of complex issues that unit tests might miss.
b) Incorrect. Financial threats are combative and contradict constructive communication practices.
c) Incorrect. Raw scanner logs rarely capture dynamic focus issues effectively.
d) Incorrect. Closing valid defects and relying on overlays violates core testing practices.

# metadata
lo: 4.3.4
k-level: K2
points: 1
correct: c

## question
Why are formal accessibility reports created after comprehensive testing activities?

## answers
a) To completely automate the technical remediation of the identified accessibility software defects
b) To completely replace the need for detailed defect tracking inside software development tools
c) To provide a structured, executive summary of accessibility compliance and standard testing findings
d) To permanently eliminate the future need to conduct ongoing, structured accessibility compliance audits

## justification
a) Incorrect. Reports document issues, they do not fix defects automatically.
b) Incorrect. Defect tracking systems are still actively required.
c) Correct. Formal reports summarize the compliance status and major findings for stakeholders.
d) Incorrect. Ongoing audits may still need to be conducted.

# metadata
lo: 5.1.1
k-level: K2
points: 1
correct: b

## question
A tester explains that assistive technologies interact with applications through accessibility APIs that expose information such as element roles, states, and labels. What is the primary purpose of these APIs?

## answers
a) Dramatically improving system performance during the execution of automated accessibility software testing
b) Providing assistive technologies with the structured interface information needed to properly function
c) Replacing the need for developers to utilize semantic HTML and standard accessibility principles
d) Automatically generating comprehensive defect documentation during formal external accessibility compliance audits

## justification
a) Incorrect. Performance optimization is not the role of accessibility APIs.
b) Correct. APIs expose interface metadata that AT needs to interpret the application.
c) Incorrect. APIs depend heavily on semantic markup, they do not replace it.
d) Incorrect. APIs do not automatically generate audit defect reporting.

# metadata
lo: 5.1.2
k-level: K3
points: 1
correct: a

## question
A tester is evaluating a custom, expandable accordion menu. They have successfully verified that the menu expands and collapses when clicked with a mouse. To properly apply assistive technology testing for this interactive component, what must the tester do next?

## answers
a) Navigate to the menu using the keyboard and verify the screen reader announces the expanded state
b) Run a static code analyzer to ensure the CSS styling meets minimum visual contrast requirements
c) Utilize a magnification tool to confirm the text does not pixelate when zoomed to 200 percent
d) Measure the response time of the server to ensure the expansion animation does not cause lagging

## justification
a) Correct. For interactive components, the tester must verify the accessibility API exposes the programmatic state change (expanded/collapsed) to the AT.
b) Incorrect. Visual contrast is tested using manual helpers, not AT, and does not test interactive states.
c) Incorrect. Screen magnification verifies visual reflow, but it does not verify if the programmatic interactive state (expanded/collapsed) is exposed to non-visual users.
d) Incorrect. Measuring server response time and animation lag relates to system performance testing, not accessibility testing.

# metadata
lo: 6.1.1
k-level: K2
points: 1
correct: d

## question
A development team uses an automated accessibility scanner that reports no errors on a webpage. However, a screen reader user later reports that the image descriptions are confusing and not meaningful. What limitation of automation does this situation illustrate?

## answers
a) Automated tools strictly prevent development teams from adding any manual accessibility code attributes
b) Automated tools inherently cannot detect the presence of any basic accessibility attributes in code
c) Automated tools are designed to completely replace manual accessibility testing inside agile environments
d) Automated tools verify attribute existence but cannot evaluate the subjective quality of the text

## justification
a) Incorrect. Automation does not restrict developers from adding attributes.
b) Incorrect. Automated tools can detect the technical presence of attributes.
c) Incorrect. Automation complements, but does not replace, manual testing.
d) Correct. Tools can verify an *alt* attribute exists, but human judgment is required to verify if the text is actually meaningful.

# metadata
lo: 6.1.2
k-level: K2
points: 1
correct: d

## question
A CI/CD pipeline blocks code from being merged into the main branch because an automated accessibility check fails. Which mechanism is being applied?

## answers
a) Design validation checks executed within standardized accessibility UI design systems
b) Automated crawling tools evaluating accessibility compliance on live production servers
c) Screen reader validation checkpoints performed during manual accessibility testing phases
d) Quality gate mechanisms enforcing strict accessibility requirements during code integration

## justification
a) Incorrect. Design validation occurs earlier in the lifecycle.
b) Incorrect. Crawling tools scan deployed websites rather than blocking code merges.
c) Incorrect. Screen reader testing is a manual activity.
d) Correct. Quality gates automatically prevent code that fails checks from being merged.

# metadata
lo: 6.1.3
k-level: K2
points: 1
correct: c

## question
An AI accessibility tool generates a description that incorrectly identifies a “submit” button as a “search” button. Which AI risk does this situation illustrate?

## answers
a) The fundamental inability of standard automated tools to detect missing attributes
b) The complete failure of underlying accessibility APIs to expose interface elements
c) The generation of functional inaccuracies caused by probabilistic machine learning predictions
d) The inherent incompatibility between modern assistive technology software and operating systems

## justification
a) Incorrect. The issue is incorrect interpretation rather than missing attributes.
b) Incorrect. The problem is AI hallucination, not an API failure.
c) Correct. AI outputs are probabilistic and may generate confident but entirely incorrect results.
d) Incorrect. AT compatibility is unrelated to AI generation errors.

# metadata
lo: 6.2.1
k-level: K2
points: 1
correct: b

## question
A testing team uses multiple categories of accessibility tools across development, UI testing, and user validation. What strategy does this approach represent?

## answers
a) An automated testing strategy designed to completely replace all manual user evaluation
b) A layered tooling strategy ensuring robust coverage across different system architecture levels
c) A performance testing strategy focusing primarily on backend system load and scalability
d) A security testing strategy identifying critical application source code vulnerabilities and breaches

## justification
a) Incorrect. Manual testing remains essential.
b) Correct. Layered tooling ensures accessibility is evaluated holistically across multiple technical levels.
c) Incorrect. Scalability testing is unrelated to accessibility.
d) Incorrect. Security testing focuses on vulnerabilities, not on accessibility.

# metadata
lo: 6.2.2
k-level: K2
points: 1
correct: c

## question
A linter detects that a form input field is missing an associated label in the source code. Which role of Category 1 does this illustrate?

## answers
a) Accurately simulating real-world user experiences by utilizing specialized assistive technology
b) Evaluating dynamic user interface behavior during complex runtime user interactions
c) Detecting structural accessibility defects in code before the UI is fully rendered
d) Analyzing the complex linguistic tools readability of written interface text and content

## justification
a) Incorrect. AT simulation relates to Category 3 tools.
b) Incorrect. Runtime behavior is evaluated by Category 2 UI scanners.
c) Correct. Static analysis tools (Category 1) validate structure directly in the source code.
d) Incorrect. Readability analysis belongs to Category 4 tools.

# metadata
lo: 6.2.3
k-level: K2
points: 1
correct: a

## question
A tool scans a webpage in a browser and detects insufficient color contrast between text and its background. Which capability of Category 2 tools does this represent?

## answers
a) Runtime evaluation of visual accessibility directly within the rendered user interface
b) Static analysis of accessibility attributes found explicitly within the raw source code
c) Accurate simulation of screen reader software behavior during manual testing phases
d) Analysis of overall language complexity and readability within written web content

## justification
a) Correct. UI scanners analyze visual output on the fully rendered interface at runtime.
b) Incorrect. Static analysis operates strictly on source code.
c) Incorrect. Screen reader testing utilizes Category 3 AT.
d) Incorrect. Readability analysis belongs to Category 4 tools.

# metadata
lo: 6.2.4
k-level: K2
points: 1
correct: b

## question
A tester navigates a website using a screen reader to verify whether headings and buttons are announced correctly. What accessibility layer is primarily being evaluated?

## answers
a) The raw HTML structure utilized heavily by automated static code analysis
b) The programmatic accessibility tree evaluated heavily by assistive technology software
c) The visual DOM layout rendered and evaluated by automated UI scanners
d) The linguistic clarity and reading grade analyzed strictly by readability tools

## justification
a) Incorrect. Static analysis evaluates raw code rather than accessibility APIs.
b) Correct. Screen readers interact with the accessibility tree generated by the system.
c) Incorrect. UI scanners analyze the visual rendered interface.
d) Incorrect. Readability tools analyze language complexity.

# metadata
lo: 6.2.5
k-level: K2
points: 1
correct: c

## question
A content editor uses a tool that highlights long sentences and suggests simpler alternatives. What accessibility goal does this tool support?

## answers
a) Verifying strict software compatibility with native operating system assistive technology APIs
b) Detecting missing accessibility code attributes natively within the application source code
c) Improving linguistic clarity specifically for users with reading or cognitive disabilities
d) Measuring mathematical visual contrast ratios between foreground text and background elements

## justification
a) Incorrect. Assistive technology compatibility relates to Category 3 testing.
b) Incorrect. Source code analysis belongs to Category 1 tools.
c) Correct. Readability tools simplify language to reduce cognitive load.
d) Incorrect. Visual contrast analysis belongs to Category 2 tools.
