# Assistive Technology – 75 minutes {#5}

#### Keywords

(none)

#### Domain specific keywords

accessibility API, accessibility tree, ARIA / WAI-ARIA, screen magnifier, screen reader, semantic markup, speech recognition, switch access, voice control

#### Learning Objectives for Chapter 5: {.learning-objectives}

1. Learning Objectives
    1. (K2) Explain assistive technologies
    1. (K3) Apply assistive technologies in accessibility testing

**Assistive technology**

## Assistive technologies

### Explain assistive technologies

To understand accessibility testing, one must first understand how users with disabilities interact with digital environments. Assistive Technology (AT) refers to any piece of equipment, software program, or product system that is used to increase, maintain, or improve the functional capabilities of persons with disabilities.

For a user who cannot see a screen, cannot hear the audio, or cannot use the standard mouse and keyboard, AT acts as a bridge. It translates the digital interface into a format the user can perceive (such as speech or magnification) and allows the user to send commands back to the system (such as voice commands or specialized keyboard inputs).

It is important to emphasize that we are not testing the AT itself, but rather a digital solution that use AT. In example, the goal is not to find bugs in how a specific screen reader operates, but to verify that the software product is built in a way that the screen reader can understand. While we are not testing the assistive technology itself, we must apply it as an instrument during accessibility testing to simulate the user experience and validate compatibility.

**Main categories of testing with Assistive Technologies**

Assistive technologies encompass a broad range of tools designed to support individuals in accessing digital content. Major categories include:

* **Screen readers**, which converts digital text, interface elements, and structural code into synthesized speech or output on a refreshable braille display. They are primarily used by individuals who are blind or have severely low vision.
* **Screen magnifiers and display adjustments**, which enlarge content and enhance contrast. They are crucial for users with low vision.
* **Speech recognition** systems (voice control), which enable navigation and text entry through spoken voice commands. Used by individuals with motor or mobility impairments.
* **Alternative input devices** such as switch controls, eye-tracking systems, sip-and-puff devices, or adaptive keyboards that provide access for people with limited mobility.

Understanding these categories is essential because each represents distinct interaction patterns and accessibility needs across different hardware (desktop vs. mobile).

**The technical bridge between Accessibility API and Accessibility Tree**

Assistive technologies cannot “look” at a screen the way a human user does. Instead, they interface with digital systems primarily through platform accessibility APIs provided by operating systems (e.g., Microsoft UI Automation, Apple Accessibility API, Android Accessibility Framework, AT-SPI on Linux). These APIs act as a bridge between applications and assistive technologies by exposing a programmatic representation of the user interface.

When an application loads, the operating system uses these APIs to construct a logical Accessibility Tree. This tree contains semantic information about every element on the screen, including:

* role of a control (e.g., button, heading, checkbox),
* current state (e.g., selected, expanded, disabled),
* relationships between elements (e.g., label-input associations, table row-column structures),
* user-facing metadata (e.g., accessible names, descriptions, keyboard shortcuts).

Screen readers query this accessibility tree to render speech or braille. Similarly, screen magnifiers use the exposed properties to track keyboard/touch focus and caret position, while speech recognition software relies on predictable and accessible control names to map a user's voice command to the correct UI element.

The accuracy and completeness of this accessibility tree depend entirely on how well developers implement standard semantic markup. For web applications it means native HTML and ARIA (Accessible Rich Internet Applications) attributes. For mobile and desktop applications this means utilizing UI components and accessibility properties specific to their frameworks (e.g., SwiftUI for iOS, Compose for Android, WPF for Windows).

If an application fails to provide meaningful metadata, exposes custom widgets without accessibility support (like using a simple generic container to act as a button), or misuses semantic roles, the accessibility tree becomes incomplete or misleading. In such cases, assistive technologies may announce incorrect information, fail to expose essential controls, or prevent users from completing tasks altogether, creating critical accessibility barriers.

### Apply assistive technologies in accessibility testing

For accessibility testing it is not sufficient to rely only on automated tools, testers must apply assistive technologies directly to simulate real-world experiences. This involves navigating a site or application with a screen reader to verify logical reading order and meaningful alternative text, using a magnifier to check for proper scaling without loss of functionality, or testing with voice control to ensure that interactive elements can be activated by spoken commands.

Through this hands-on testing, usability barriers become evident, such as unlabeled buttons, inaccessible dynamic content, or tasks that require complex mouse or touch gestures without accessible alternatives. To successfully apply AT in testing, testers must use specific techniques tailored to the interaction model of the technology and the device being used.

**Practical application of AT in testing**

When using AT in testing, testers should structure their approach using following methods:

| Methods | Description |
| :-- | --- |
| Testing with screen reader | Navigating a site or application using only a keyboard and a screen reader to verify a logical reading order, ensure alternative text for images is meaningful, and confirm that dynamic changes (like error messages appearing) are announced properly. |
| Testing with screen magnifier | Zooming the interface to simulate low-vision usage, checking for proper scaling without loss of functionality, and ensuring that users do not have to scroll both horizontally and vertically to read a single block of text. |
| Testing with voice control | Navigating the application using spoken commands to ensure that interactive elements have accessible names that match their visible labels, allowing them to be activated by voice. |

***Testing with screen readers***

Testing with a screen reader involves more than simply listening to a page read from top to bottom. A tester must actively apply different navigation strategies to uncover structural and interactive defects across web, desktop, and mobile environments:

* Structural navigation testing. Testers use AT-specific commands (e.g., keyboard shortcuts on desktop, or the “rotor/menu” touch gestures on mobile) to navigate the interface. The goal is to verify that the underlying semantic markup creates a logical document outline that matches the visual hierarchy.
* Interaction and state testing. When interacting with complex widgets (like tabs, accordions, or custom toggles), the tester must verify that the AT announces not just the element's name, but its dynamic state (e.g., “Tab, Expanded” versus “Tab, Collapsed”) as it changes in real-time.
* Browse mode vs. Focus mode verification (Desktop). Desktop screen readers typically switch between reading content (browse mode) and interacting with forms (focus mode). Testers must verify that custom interactive widgets correctly trigger the screen reader to switch modes so the user can type or interact without triggering standard reading shortcuts.

***Testing with screen magnifier***

Zooming the interface to simulate low-vision usage requires evaluating how the software handles extreme scaling (often up to 400%):

* Focus tracking verification. When the screen is highly magnified, only a smaller part of the interface is visible. The tester must navigate via keyboard or touch to ensure the magnifier automatically shifts/slides to keep the currently focused element visible on screen.
* Hover and proximity testing. The tester verifies that tooltips, dropdowns, or sticky banners triggered by mouse hover or keyboard focus do not obscure the very same content the user is trying to magnify and read.

***Testing with voice control***

Navigating the application using spoken commands requires checking the mapping between visual design and programmed code.

“Label in Name” verification. Testers apply voice commands by speaking the visible text on the screen (e.g., saying “Tap Submit”). If the developer gave the button a different, hidden accessible name (e.g., a programmatic label of “Send Form”), the voice command will fail. The tester must practically verify that the visible text is always included within the programmatic name for accessibility.

**Verifying standard interactive behaviors**

Standard digital platform technologies provide correct roles, states, and behaviors to accessibility APIs by default, enabling assistive technologies to interact reliably. Non-standard or custom implementations often break these interactions, creating barriers for users. In accessibility testing, it’s vital to ensure interactive elements follow web standards, especially when using non-standard implementations.

It is important to understand and be able to apply AT in testing when AT is device dependent. Interaction methods differ significantly depending on the operating system and device. While basic keys (like TAB and Enter) are universal across desktop OSs (Windows, macOS, Linux), specific modifier keys vary (e.g., Alt on Windows vs. Option on macOS). Furthermore, on mobile devices (iOS, Android), physical keyboards are typically replaced by standardized touch gestures (e.g., swiping right to move focus to the next element, double tapping to activate an element) when a screen reader is active.

A tester must practically verify the behaviors listed in the table below, adapting to the input method of the platform being tested:

| Element / Action | Standard Desktop Keyboard Interaction | Standard Mobile Screen Reader Gesture | Expected behavior to verify |
| :-- | --- | --- | --- |
| Navigate focusable items | TAB (or Shift + TAB to go backward) | Swipe Right (or Swipe Left to go backward) | Focus moves sequentially through interactive elements. A visible focus indicator must clearly show which element is currently active without getting trapped. |
| Activate a button | Enter (or sometimes Spacebar) | Double tap anywhere on the screen | The button's primary action triggers immediately and the AT announces any resulting context change. |
| Select a checkbox | Spacebar | Double tap | The checkbox state toggles between checked and unchecked. Enter should not be needed to check the box. |
| Select a radio button | Arrow Keys (Up / Down / Left / Right) | Swipe to navigate, Double tap to select | Navigates through the group of radio buttons and simultaneously selects the focused item. Enter or Spacebar should not be needed. |
| Interact with a dropdown list | Down Arrow / Alt (or Option) + Down Arrow | Double tap to open, Swipe to browse items | Navigating to the field allows the user to expand the list and browse available options. |

By combining technical knowledge of Assistive Technology categories, awareness of how they integrate with platforms, and practical testing techniques, software testers can more effectively identify and address accessibility issues, ensuring a more inclusive digital experience.

------------------------------------------------------------------------
