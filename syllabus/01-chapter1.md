# Basic Concepts – 90 minutes {#1}

#### Keywords

accessibility, usability, user experience

#### Domain specific keywords

assistive technology (AT), medical model (of disability), social model (of disability), universal design

#### Learning Objectives for Chapter 1: {.learning-objectives}

1. Fundamentals
    1. (K2) Explain the concept digital accessibility
    1. (K2) Explain the objectives of digital accessibility evaluation
    1. (K2) Understand the design principles for accessibility testing
1. Disabilities
    1. (K2) Explain the different categories of disabilities
    1. (K2) Explain the importance of accessible software
1. Risks
    1. (K2) Understand the legal risks and impact of not applying accessibility to software

## Fundamentals

This section considers the concepts of Digital Accessibility and its relationship with Usability and User experience.

### Accessibility

Accessibility is the degree to which a product or system can be used by people with the widest range of characteristics and capabilities to achieve a specified goal in a specified context of use (reference: ISO 9241-171 Ergonomics of human-system interaction, part 171: Guidance on software accessibility).

Digital accessibility means that websites, tools, and technologies are designed and developed so that people with disabilities can use them. All users are afforded the same experience and information whether or not they have a disability and no one is excluded due to development choices.

The level of accessibility of a software product can be defined by the compliance to set guidelines and criteria, such as Web Content Accessibility Guidelines (WCAG). The four pillars on which WCAG is based are the Perceivability, Operability, Understanding and Robustness of the product (POUR principle).

Accessibility has significant overlaps with usability and user experience, as accessibility is fundamentally the effort to ensure the product is usable by people with the widest range of capabilities. A user with a disability may not enjoy or have a perfectly efficient experience, yet still be able to achieve their goal if basic accessibility is met. However, accessibility pertains specifically to the inability of use due to a failure to meet accessibility specifications. Together, accessibility and usability create a truly inclusive digital product. (Note: for a comprehensive understanding of usability evaluation methodologies, learners should refer to the ISTQB Specialist Syllabus, Usability Testing \[ISTQB_SYL_UT\]).

Examples of accessibility defects:

* A website uses text in an image to portray information, without alternative text available or with alternative text that does not match the information in the image. A screen reader user therefore does not have access to the same information as other users.
* A software product does not support navigation via keyboard, only via mouse. Users unable to use a mouse can therefore not interact with the software product.
* An online banking application has a strict, unadjustable 60-second timeout for security. A user with limited mobility or hand tremors cannot complete the transaction in this short timeframe, effectively locking them out of their account.

### Explain the objectives of digital accessibility evaluation

Accessibility evaluation includes the following principal activities:

* Accessibility testing
* User testing

Accessibility evaluation focuses on the direct interaction between a user with disabilities and the software product. It addresses barriers that specifically block access to information or functionality.

The key objectives of accessibility evaluation, usability evaluation, and user experience evaluation are compared in the following table and discussed in more detail in subsequent sections.

| Type of evaluation | Target group | Key objective |
| :--- | --- | --- |
| Accessibility evaluation | Users with disabilities | Evaluate the direct interaction between users and the software product, focusing on understanding problems related to accessibility barriers, rather than general efficiency or satisfaction. |
| Usability evaluation | All users | Evaluate the direct interaction between users and the software product. |
| User experience evaluation | All users | Evaluate the services received prior to, during, and after the use of the software product to measure overall satisfaction and emotional response. |

The principal techniques applied in these evaluations are shown in the following table:

| Technique | Users involved? | Key characteristic | Type |
| :--- | --- | --- | --- |
| Accessibility testing | Optionally | Lived experience experts are observed while they perform typical tasks with the software product, or they perform accessibility evaluation independently and provide feedback. | Qual, Quant |
| Usability review | Optionally | Experts and users evaluate the user interface of a software product for usability problems / the evaluation is based on their experience. | Qual |
| Usability testing | Yes | Users are observed while they perform typical tasks with the software product. | Qual, Quant |
| User surveys | Yes | Users fill out questionnaires regarding their satisfaction with the software product. | Qual, Quant |

Qual = Qualitative evaluation

Quant = Quantitative evaluation

### Understand the design principles for accessibility testing

Accessibility evaluation is a specialized form of evaluation that focuses strictly on the accessibility of a software product (direct interaction between a user with disabilities and the software product). To successfully implement accessibility testing, the following principles and practices apply:

The following advice applies specifically to accessibility evaluation:

1\. Define the ambition level to be achieved for accessibility, based on a standard or guideline.

2\. Review the guidelines to establish their suitability

3\. Implement preventative measures so that development teams can avoid implementing software which has accessibility problems. This is particularly important for applicable legal requirements.

Accessibility evaluation is like usability evaluation which in a specialized form of evaluation focuses strictly on the accessibility of a software product (direct interaction between a user with disabilities and the software product). To successfully implement accessibility testing, the following principles and practices apply:

1\. Define the ambition level for accessibility

Establish the target level based on a standard or guideline. The Web Content Accessibility Guidelines (WCAG) define three conformance levels: A, AA, and AAA. It is highly recommended to adopt conformance level AA, which satisfies the fundamental requirements for digital accessibility and resolves the biggest barriers for users with disabilities (see section 2.2.3).

2\. Create or adapt guidelines for accessible design

Guidelines must comply with legal requirements and align with the chosen ambition level. It is recommended to establish a dedicated support channel or network of accessibility Subject Matter Experts (SMEs) where accessibility questions from the development teams can be answered competently within an agreed timeframe.

3\. Train development teams in order to prevent as many accessibility problems as possible. This includes factors such as:

* Legal requirements for accessibility
* Guidelines for accessible design and how to interpret and apply them
* Tools and techniques to use when evaluating accessibility
* The relationship between usability and accessibility

4\. Accessibility testing focuses on the following aspects:

* Focus on understanding the tools, techniques, and practices
* Focus on understanding mistakes related to accessibility barriers, rather than on efficiency or satisfaction
* Use tasks that concentrate on specific areas of concern for potential accessibility problems, and follow the accessibility plan

Accessibility evaluation should consider relevant accessibility standards, which are listed in Chapter 2.

## Disabilities

### Categories of disabilities

There are many forms of disabilities which can be permanent, temporary, situation or progressive. They are generally grouped into the following main functional categories:

1. Visual Disabilities
2. Hearing Disabilities
3. Mobility/Physical Disabilities
4. Cognitive and Learning Disabilities
5. Speech Disabilities
6. Temporary or Situations Disabilities
7. Progressive disabilities

The main disability models include:

1. Medical model
2. Social model
3. Charity model (Note: this one is irrelevant for accessibility testing)

See below for details.

**1. Visual Disabilities**

Visual disabilities are sensory disabilities with a range of variations based on visual acuity and field of vision. Vision loss, or blindness, is considered a disability if vision cannot be fully corrected with standard glasses, contact lenses, medication, or surgery.

Types of blindness can range between total loss of vision (very rare) to seeing shapes. Visual disabilities also include color blindness, or color deficiency, in which colors are perceived in a different way.

Additionally, disabilities can be progressive, growing stronger or more severe over time. An example is Retinitis Pigmentosa, a progressive visual condition that slowly worsens vision, often starting with difficulty seeing at night and a gradual narrowing of the visual field (tunnel vision).

Examples of barriers:

* Software that does not support keyboard use
* Correct usage of semantic mark-up for integration with assistive technology such as screen readers.
* Platforms reliant solely on visuals without text alternatives
* Unresponsive software that doesn’t support zoom or enlargement of text without loss of content
* Semantic mark-up that strays from standard convention e.g. arrow keys to enter a dropdown menu
* System states that rely exclusively on color to convey the meaning (e.g., a form where incorrect fields are only indicated by a red border without an accompanying error icon or text message).

**2. Hearing Disabilities**

Hearing disabilities comprise a form of hearing loss, in which it can be difficult or impossible to hear sounds such as speech. Hearing ability can range from partially impaired hearing to full hearing loss in one or both ears. Auditory processing disorder (APD) is a neurodevelopmental disorder that causes difficulty to process sounds such as speech.

Examples of barriers:

* Videos without closed captions
* Audio without a written transcript
* Transcripts that do not match what is said in the recorded fragment, causing a disbalance in shared information

**3. Mobility/Physical Disabilities**

A mobility disability refers to a physical condition that limits a person’s ability to move. Mobility impairment includes limb loss or disability, reduced manual dexterity such as fine motor control, difficulties with coordination between body systems such as organs, or issues affecting the skeletal structure. It may result from a genetic condition, an illness or injury, or the natural effects of aging.

Examples of barriers:

* Software that doesn’t support interaction with software products via keyboard, mouse, or assistive technology such as a mouth stick.
* Difficulty clicking small buttons due to tremors or use of assistive technology such as a customized mouse or mouth stick

**4. Cognitive and Learning Disabilities**

Cognitive disabilities concern the brain and can be caused by traumatic injuries or can occur by themselves. Cognitive disabilities concern a wide range of disabilities and disorders, with each experience unique to the affected person. This makes designing for cognitive disabilities particularly difficult, as what helps one person with a certain diagnosis may not help another with the same diagnosis.

Examples of barriers:

* Sole use of written language without supporting visuals such as icons
* Sole indication via symbols without supporting text
* Use of complex language, such as figure of speech, without supporting visuals or plain text
* Time limits
* Elements that stray from internet convention, such as dropdown menus that are activated via “Enter” instead of the down/up arrow key
* Use of flashing or animations that cannot be turned off
* Complex layout and navigation

**5. Speech Disabilities**

Speech disorders can range from mild slurring to a complete inability to speak. They may result from damage to the brain or muscles, emotional or psychological factors, be associated with another disability, or arise from a combination of these causes.

Examples of barriers:

* A software product relies solely on voice activation
* An IVR (Interactive Voice Response) with voice as sole form of input

**6. Temporary or Situational Disabilities**

Disabilities often refer to permanent disabilities, which are expected to last indefinitely. These disabilities can be from birth or develop later in life.

However, barriers can be experienced by people without a permanent disability but with a temporary or situational disability.

Temporary disabilities are disabilities that are temporary in nature and expected to improve or disappear with time and/or treatment. For example, a broken arm that results in a mobility disability, or temporary blindness caused by LASIK surgery.

Situational disabilities are caused by the direct environment of a person, such as sunlight on a screen or eating a sandwich with one hand whilst using the other to navigate a website. These disabilities are expected to improve or disappear by changing the situation.

### The importance of accessible software

To understand the importance of accessible software, it is vital to understand the paradigms through which society views disability. The main Disability Models include:

1. Medical model

> This model views disability as an issue that exists within the person, caused by injury, illness, or health condition. The impairment is seen as the root of the problem, and the aim is to diagnose, treat, manage, or “fix” it. Under this model, solutions focus on the individual adapting to the world, rather than the world adapting to them. In this context, assistive technology is often viewed strictly as a medical tool or personal aid meant to compensate for the individual's “deficit”, placing the burden on the user to find and utilize personal adaptive strategies to interact with standard, unmodified software.

2. Social model

> Popular in the disabled community, this model shifts focus away from the impairment and places responsibility on society. It argues that people are disabled not by their conditions, but by the physical, attitudinal, and systemic barriers that prevent them from participating equally. For example, a wheelchair user is not inherently limited by their condition, but by buildings without ramps or elevators. The goal here is to redesign environments, laws, and digital interfaces so that everyone can participate fully. Digital accessibility is heavily rooted in the Social Model. In software development, this means building interfaces that proactively support a wide range of assistive technologies (like screen readers or switch devices) and enable users’ preferred adaptive strategies (such as zooming in, changing color contrast, or relying on keyboard navigation). The software adapts to the user, not the other way around.

## Risks of not testing Accessibility

### Legal risks and impact of not applying accessibility to software

A risk is a factor that could result in future events with negative consequences; usually expressed as the impact (the harm resulting from the event) and the likelihood of the event happening. Accessibility testing acts as a critical mitigation strategy to identify and resolve the sources of risk before they manifest into negative business impacts.

The risks associated with digital accessibility can be divided into two main categories: the sources of the risk (why the software fails) and the impacts of the risk (the consequences of releasing inaccessible software).

**Sources of accessibility risk (project & technical risks)**

The following root causes could introduce accessibility barriers into the software development lifecycle. By mitigating these sources through testing, teams prevent larger impacts downstream:

1\. Organizational risks

* Lack of qualified specialists in digital accessibility within the organization
* Insufficient knowledge of basic accessibility principles among designers, developers, and QA engineers
* Insufficient management attention to accessibility test results, often incorrectly dismissing them as edge cases
* Inappropriate release decisions by management, such as refusing to postpone a release even when critical accessibility blockers are found
* Poor, vague, or entirely missing non-functional requirements regarding accessibility
* Failing to allocate time and budget for accessibility in the project test plan

2\. Technical & Maintenance risks

* Using non-standard solutions (e.g., building custom UI components instead of using semantic, native HTML elements) that assistive technologies cannot interpret.
* Inaccessible design patterns that make future accessibility fixes complex and costly
* Software architecture that does not support accessibility principles
* Compatibility issues with assistive technologies
* Inconsistent accessibility support across platforms, devices, and browsers, leading to uneven user experiences
* No accessibility evaluation performed, in particular no accessibility test

3\. Supplier risks

* Third-party component suppliers or external vendors do not have the required qualifications in accessibility development or testing
* Suppliers do not follow agreed-upon accessibility guidelines (e.g., WCAG) when delivering code
* Accessibility evaluation results provided by external suppliers are inaccurate, delivered late, or missing entirely

**Impacts of inaccessible software (product & business risks)**

The following negative consequences could occur when accessibility risks are not mitigated, and inaccessible software reaches the end-user:

1\. Legal & Regulatory risks

* Non-compliance with accessibility laws, acts and standards (e.g., European Accessibility Act, ADA)
* Lawsuits, fines, or regulatory penalties in jurisdictions with strong accessibility requirements
* Increased legal exposure if competitors or users file formal complaints

2\. Usability & User Experience risks

* Complete exclusion of entire user groups from critical digital services
* Increased frustration for users relying on compatibility with assistive technologies
* Higher abandonment rates if people cannot complete core tasks

3\. Brand & Reputation risks

* Perception of the product/company as non-inclusive, discriminatory, or out of touch
* Negative publicity from accessibility advocacy groups, media, or social media campaigns
* Loss of customer trust and loyalty not only from disabled users, but also from allies and diversity-conscious consumers

4\. Market & Financial risks

* Missed market share - excluding users with disabilities means losing access to a large, often overlooked customer base
* Decreased Search Engine Optimization (SEO), as search engines rely on the same semantic structures as screen readers
* Increased retrofit costs if accessibility is added late in development instead of early
* Lost contracts with organizations that require accessibility compliance from vendors
