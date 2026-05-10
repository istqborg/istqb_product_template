# Accessibility Standards – 75 minutes {#2}

#### Keywords

(none)

#### Domain specific keywords

POUR, Success Criterion, Web Content Accessibility Guidelines (WCAG), WCAG2ICT

#### Learning Objectives for Chapter 2: {.learning-objectives}

1. Accessibility Standards and Manufacturer Guidelines
    1. (K2) Explain the general content and applicability of global guidelines to particular types of projects/applications
1. Accessibility Regulations and Standards
    1. (K2) Explain standards and legislation
    1. (K2) Explain the general content and applicability of the ISO 9241-171 Standard
    1. (K2) Explain the structure of the Web Content Accessibility Guidelines (WCAG) and other applicable guidelines for software accessibility
    1. (K2) Explain typical criteria described in the WCAG

Please note that only the information explicitly provided in this chapter is examinable and not the entire contents of the standards themselves.

## Accessibility Guidelines

Accessibility guidelines are a collection criteria that must be met to ensure that a software product is accessible.

National legislation determines which set of guidelines are mandatory to adhere to. These guidelines usually have a set of criteria that must be met and other criteria that are recommended. The set criteria are helpful in detecting and reporting accessibility problems. These criteria are also used by independent parties that carry out accessibility audits, in order to create a report of findings. Accessibility guidelines not only set criteria but often give helpful suggestions and examples on how to meet these criteria.

Examples of universal accessibility guidelines:

* For mobile applications, provide large touch targets (at least 44x44px)
* Use short sentences and familiar words (plain language)
* Provide color-blind friendly design (don’t rely only on color to convey information)

Although each country may have their own legislation, most are based on or refer to the WCAG.

## Accessibility Regulations and Standards

### Explain standards and legislation

An accessibility standard is a collection of guidelines that ensure digital products - like websites, mobile apps, software, and electronic documents - are usable by everyone, including people with disabilities.

A number of countries have passed laws aimed at reducing discrimination against people with disabilities. These laws provide a scope of accessibility per country where applicable. Examples are:

#### EN 301 549 and the European Accessibility Act (EU)

The European Union standards for the (semi) public and commercial sectors.

EN 301 549 (semi-public)

The Web Accessibility Directive, or WAD, is set by the European Union and transposed into local legislation by all EU member states. A product of the WAD, the EN 301 549 is the European Union standard of requirements used to measure the accessibility of websites, digital documents and non-web software of (semi) public organizations.

The European Standard has adopted WCAG 2.1 as set requirements, directly referring to the WCAG and using the same structure of principles: Perceivability, Operability, Understandability, and Robustness.

##### **European Accessibility Act (EAA) (commercial)**

It is important to distinguish the Web Accessibility Directive from the European Accessibility Act (EAA - Directive 2019/882), which expands on accessibility requirements for products and services to the private sector. These products and services include:

* computers and operating systems
* ATMs, ticketing and check-in machines
* smartphones
* TV equipment related to digital television services
* telephony services and related equipment
* access to audio-visual media services such as television broadcast and related consumer equipment
* services related to air, bus, rail and waterborne passenger transport
* banking services
* e-books
* e-commerce

The EAA is set by the European Union and was mandated to be transposed into the national laws of all 27 EU member states by June 28, 2022, with compliance required by June 28, 2025.

#### Equality Act (UK)

The Equality Act 2010 legally protects people from discrimination in the workplace and in wider society.

While the Equality Act does not expressly refer to websites, a Statutory Code of Practice explicitly states that websites are included under the ambit of the Equality Act for the provision “of services”. Websites which provide access to services and goods may in themselves constitute a service, for example, where they deliver information or entertainment to the public.

On the 23rd of September in 2018 “The Public Sector Bodies (Websites and Mobile Applications) Accessibility Regulations of 2018” came into effect. These regulations state that the requirement of making a website or mobile application accessible must be met by making it: “perceivable”, “operable”, “understandable”, and “robust”. The service must also publish an accessibility statement explaining the accessibility of the software product.

WCAG 2.2 AA is the criteria used as the accessibility standard for the regulations mentioned above. For UK products and services this means that testing is done with these requirements.

#### Americans with Disabilities Act (USA)

The Americans with Disabilities Act (1990) prohibits discrimination based on disability. In particular, it requires that private websites be accessible to blind and visually impaired Internet users. The Americans with Disabilities Act generally dictates that all “places of public accommodation” and all “goods, services, facilities, privileges, advantages, or accommodations” of places of public accommodation, must be made accessible to disabled citizens.

In addition, the Rehabilitation Act of 1973 requires Federal agencies to make their electronic and information technology accessible to people with disabilities. The law applies to all Federal agencies when they develop, procure, maintain, or use electronic and information technology. Under Section 508, agencies must give disabled employees and members of the public access to information that is comparable to access available to others.

### General content and applicability of the ISO 9241-171 Standard

**ISO 9241-171 – Guidance on software accessibility**

This standard provides guidance on the design of the software for interactive systems to achieve as high a level of accessibility as possible.

The standard provides the following information:

* Definitions of accessibility related terms. For example, the term “Screen reader” is defined as “assistive technology that allows users to operate software without needing to view the visual display”.
* Guidelines for accessible software products. In this main body of the standard over 140 guidelines are provided, together with additional notes and examples. An example guideline is “8.1.4 Make names available to assistive technology: Each name of a user interface element and its association shall be made available by the software system to assistive technology in a documented and stable fashion”.

### The Web Content Accessibility Guidelines (WCAG)

The Web Content Accessibility Guidelines \[Web-7\] are a part of a series of web accessibility guidelines published by the Web Accessibility Initiative (WAI) of the World Wide Web Consortium (W3C), the main international standards organization for the internet. They consist of a set of guidelines for making content accessible, primarily for people with disabilities.

These guidelines are built upon the following four principles:

* Perceivable (Information and components must be presented to users in a way they can be perceived, or taken in, by all)
* Operable (users must be able to operate, or interact, with components and navigation so that all information and functions are available to all users)
* Understandable (the information and functionalities must be understandable, or clear, for all users)
* Robust (the components and content must be robust enough to be used by a wide variety of client applications, or user agents, such as assistive technology)

Each principle has set guidelines, each with criteria supplying the accessibility requirements used for compliance.

The following tables show the three WCAG conformance levels and examples:

**Level A**

| Description | Examples |
| :--- | --- |
| Guidelines that will have a high impact on a broad array of user populations and therefore don’t focus on a single type of disability. The guidelines have the lowest impact on the presentation logic and business logic of the site, but their implementation will typically be the easiest. | Text Alternatives (Guideline 1.1.1): / All non-text content that is presented to the user has an equivalent text alternative. / Example: Images should include equivalent alternative text in the markup / code. / Keyboard Accessible (Guideline 2.1.1): / All functionality of the content is operable through a keyboard interface, without requiring specific timings for individual keystrokes. Example: An accessible website does not rely on mouse input because some people cannot use a mouse. All functionality is available via a keyboard or assistive technologies that mimic the keyboard, such as speech input. |

**Level AA**

| Description | Example |
| :--- | --- |
| Guidelines that will also have a high impact on users. Sometimes only specific user populations will be impacted, but the impact is important. Adherence to these guidelines may impose changes to a system’s presentation logic or business logic. | Distinguishable: (Guideline 1.4.4): / Except for captions and text images, text can be resized up to 200 percent without assistive technology and without loss of content or functionality. |

**Level AAA**

| Description | Example |
| :--- | --- |
| Guidelines that are often focused on improvements for specific user populations. They may be difficult or expensive to adhere to, depending on platform limitations. The cost-benefit ratio may be low enough to reduce the priority of these items. | Keyboard accessible (Guideline 2.1.3): / All functionality of the content is operable through a keyboard interface without requiring specific timings for individual keystrokes. |

**Applying WCAG to non-web technologies**

While WCAG was originally designed for web content, modern legislation, such as the European Accessibility Act (EAA), mandates accessibility for non-web software, mobile applications, and closed-system hardware like ATMs and ticketing machines. Testers evaluating these systems should refer to the WCAG2ICT (Guidance on Applying WCAG to Non-Web Information and Communications Technologies). This guidance helps translate web-specific criteria (like HTML parsing) into universal requirements for native software and operating systems.
