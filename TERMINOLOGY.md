*Testing*
	- system execution with the intend of finding defects.
*Debugging*
	- locating of erroneous code, design, requirements etc.
*Fixing*
	- correcting a discovered defect.
*Fault (error, bug)*
	- defect that causes or can potentially cause the failure when executed
	(developer oriented concept).
*Failure*
	- manifestation of defect when system is run (user oriented concept).
*Verification*
	- „are we building the product right?”
*Validation*
	- „are we building the right product?”, „Does system meets the expectations of the
	user?”
*Good Test*
	- this which has high probability to reveal yet-undiscovered defects.
*Clean (Positive) Test*
	- test to demonstrate correct working.
*Dirty (Negative) Test*
	- test to break the system.
*Exhaustive Testing*
	- testing all elements of program domain in all possible states.
*Coincidental Correctness*
	- for some input data system may produce correct output in spite of
	existing defects.
*Blindness*
	- every testing method is blind to specific defects (because of Coincidental Correctness).
*Test*
	- set of one or more test cases and associated test procedures.
*Test Item*
	- a software item which is an object of testing.
*Test Case*
	- specification of required setup, input data, and expected output.
*Test Procedure*
	- specification of steps needed to execute a test.
*Test Suite*
	- a series of tests and the environment(s) necessary to run them.
*Test Execution Log*
	- a chronological record of relevant details about the execution of tests.
*Test Report*
	- a document summarizing testing activities and results.

*Test Group Independence*
	- practices that ensures the testers are not
	inappropriately influenced by the design and implementation decisions made by
	the software developers or maintainers.
*Verification*
	- the process of evaluating software to determine whether the
	products of a **given development phase** satisfy the conditions imposed at the start
	of the phase [8]:
	- „Are we building the product right?”;
	- Example: inspections, walk-through, technical review, testing.
*Validation*
	- the process of evaluating software during or at the **end of the development** process to determine whether it satisfies specified requirements [8]:
	- „Are we building the right product?”;
	- Conclusion that system (software) is validated is highly dependent upon verification tasks
	performed at each stage of the system (software) development life cycle.
*Reliability*
	- the probability that a given system (software) operates for some given
	period without defects.

**Testing Terminolgy Ilustrated**

* >>> The goal of testing is to make the system fail. <<<*


*** WYKŁAD 2 ***

*• What is Control System?*

*• Intended Functionality*
	- The intended functionality of the control system is the
	desired behavior specified for the system
*• Performance*
	- Performance is the degree to which a system
	accomplishes its designated functions within given
	constraints regarding processing time and throughput
	rate.
*• Reliability*
	- Reliability is the ability of the system to perform its
	required functions under stated conditions for a
	specific period of time, or for a specific number of
	operations. (systems, that might depend on a precise clock, or wear over time.)
*• Robustness*
	- Robustness is the ability of a control system to cope
	with errors, disturbances and uncertainties during
	execution.
*• Safety*
	- Safety refers to the control of recognized hazards in
	order to achieve an acceptable level of risk.
	- *ASIL - Automotive Safety Integrity Level*
*• Security*
	- Security of the system is characterized by attributes
	that bear on its ability to prevent unauthorized access,
	whether accidental or deliberate, to program and data.
*• Portability / Installability*
	- Portability is the case with which the software product
	can be transferred from one hardware or software
	environment to another.
*• Usability*
	- Usability is the capability of the system to be
	understood, learned, used and attractive to the user
	when used under specific conditions.
*• Recoverability*
	- Recoverability is the capability of the system to reestablish
	a specified level of performance and recover
	the data directly affected in case of failure.

*** WYKŁAD 3 ***
*• Textual Representation*
	- Textual representation is a description of the expected system behavior
	written in natural language and it is usually provided by the customer
		- unambiguous, testable or measurable, and necessary for
		product or process acceptability (ISO/IEC 2007)
*Traceability*
	- establishing and documenting the bilateral
	relationships between primary requirements and derived
	requirements, designs, implementation and tests.*

	TC1.1.1 ; TC 1.1.2 etc.
*• Formula-Based Representation*
	- Formula-based representation is a description of the system
	using a mathematical concept and language.
*• Graphic Representation*
	- Graphic representation is a description of the system where a
	graph expresses the dependency between system variables and
	parameters.
*- Cause Effect Graphs*
	- The specification is analyzed and causes (inputs, stimuli etc.) and effects (outputs) are identified.
	The causes and effects are put into decision table.
	- *independently testable features (ITF)*
	- **This model is not suitable for systems which include timing aspects**
	- causes on left, results on the rigth.
*- Finite State Machine*
	- Finite State machine is a mathematical model of the state driven aspects of a system.
		- trasnitions consist of actions or events
		 - a. Mealy FSM - associates *actions* with the
		*transitions* between states.
		- b. Moor FSM - associates *actions* with the
		*states* themselves.
*- UML Charts*
	- Universal Modelling Language
	- Action are specified after ‘/’.
		- Action can be associated with states:
	- UML defines some special states:
		- Initial pseudostate:
			- ‘C’ or a small diamond:
		- Termination pseudostate
			- ‘T’ or by dot in a circle
		- History Pseudostate
			- History pseudostate is used to
			define that last acitive substate
			is entered on subsequent re-entry
			to the superstate.
*- Data Flow Diagrams*
	- A program variable is defined whenever its value is
		modified:
		- On the left hand side of an assignment statement
			• x=2
		- In an input statement
			• read(x)
		- As an call-by-reference parameter in a subroutine call
			• update(&x)
	- A program variable is used whenever its value is
	read:
		- On the right hand side of an assignment statement
			• y = x + 1
		- As an call-by-value parameter in a subroutine or function
		call
			• y=sqrt(x)
		- In the predicate of a branch statement
			• if (x > 0) { }
	- *A use of a variable is a predicate-use or p-use*
	- *A use of a variable is a computation-use or c-use*
	- *Predicate*
		- is a statement that can evaluate to true or false
	- *Definition Clear path:*
		 definition-clear path (def-clear) for a variable 𝑥 not contain the definition of 𝑥
	- *Definition-C-Use Associations*
		- presence of a *definition-clear* path for 𝑥
		(1, 4, x)
	- *Definition-P-Use Associations*
		- the presence of a definition-clear path for 𝑥 (for true of false)
		(1, (5, t), x)
		(1, (5, f), x)
	- *DU-Paths*
		- du-path for a variable 𝑥 if 𝑛1 contains a definition of 𝑥
		- is a definition-clear loop-free path for 𝑥.
		- (1, 2, 4)
		- (1, 2, 3, 5)
*• Data-Driven Representation*
	- Data-driven representation is based on the analysis of
	the data about a specific system.
	- find relationships between the system inputs and outputs without explicit knowledge
*• Computer-Based Representation*
	- Computer-based representation refers to using computer technology to describe the expected system behavior in virtual reality.
*• General Concept*
	- State Space Representation

***WYKŁAD 4***

*• Basic Definitions*
	- *Development „process”* is a sequence of steps performed for a given
	development purpose.
	- *Development „model”* is a theoretical construction that represents the
	way how the system is developed, with a set of variables and a set of
	logical and quantitative relationship between them.
	- *Development „framework”* is a particular set of rules, ideas, or beliefs
	which you use in order to deal with problems or to decide what to do.
	- *Development „methodology”* is a contextual framework, a coherent
	and logical scheme based on views, beliefs, and values, that guides the
	choices developers make.
	- *"Approach"*:
		• A way of dealing with the system development;
		• A route that leads to the system as a product;
		• An act of communicating with project team members.
*• Waterfall Development*
	- Requirement analysis
	- Design
	- Implementation
	- Testing
	- Deployment
	- Works well for smaller projects where requirements are very
	well understood
*• Spiral Development*
	- Swtiching between:
		- Determination of objectives, alternatives, constrains
		- Risk analysis and alternatives evaluation
		- Development
		- Next iteration planning
	- Projects with unclear business needs or too
	ambitious/innovative requirements.
	- Research and development (R&D)
*• V-Model*
	- Requirement analysis
	- System design
	- Architectre design
	- Module desgin
	- Coding
	- Unit Testing
	- Integration testing
	- System Testing
	- Acceptance testing
	Projects where *failures* and *downtimes* are
	**unacceptable**
*• Agile Development*
	- IT simply sometimes skippes some stages from V-model.
*• Incremental Development*

*• Iterative Development*
*• Scrum*
	- ROLES
		Product Owner
			The person represents interests of stakeholders, writes user stories,
			prioritize them and place in the Product Backlog.
		Scrum Master
			Resolves problems and obstacles of the Team (Scrum Meeting issues),
			assure Scrum process and its roles are in place.
		Team
			Typically 5-9 people with cross-functional skills
			(architectures, designers, developers...)
			who are during actual development work.
	- ARTIFACTS
		Product Backlog
			High level prioritized functional description (what?)
			document with estimates.
		Sprint Backlog
			Portfolio of detail tasks (detail how document)
			for upcoming sprint.
		Burn Down Chart
			Publicly available chart showing tasks (effort)
			remaining for current sprint.
*• Kanban*
	Kanban approach is used frequently in projects on *software
	support and evolution*
*• Extreme Programming*
	- Four stages indluding
	- Planning,
	- Programming,
	- Acceptance test
	- release.
*• Rational Unified Process*
	- Large and high-risk projects, especially, use-case
	based development and fast development of highquality
	software.
*• Chaos Model*
	- „always resolve the most important issue first”
*• Model-Based Development*
	- Model-Based Development is a process that provides the ability to graphically
	represent requirements, specification and designs using domain-specific notations
	and simulate the resultant behavior for validation purposes.
*• Test Driven Development*
	- Test Driven Development (TDD) is a software engineering
	practice that requires unit tests to be written before the
	code they are supposed to validate.                          *
	- There are commercial on the shelf tools (COTS) suitable for Model-Based Development and
	Testing in the embedded software development world.'
	- *Book:*
	Beck, K.: „Test-Driven Development”,
	Addison-Wesley Professional, 2002.
	- KISS principle
		- Keep it simple, stupid
	- YAGNI principle
		- You ain’t gonna need it
	- DRY principle
		- Don’t repeat yourself
*• Meta Development Approaches*
 - MDD is rather recommended for traditional
	development model that is based on
	Waterfall approach
*- Software Process Improvement and Capability Determination*
		- SPICE (Software Process Improvement and Capability dEtermination)
*- Systems and Software Engineering - Software Life Cycle Processes*
		- Software life cycle processes is an international standard for software lifecycle processes
*- Systems and Software Engineering - System Life Cycle Processes*
		- Systems and software engineering - System life cycle processes is a system engineering standard covering processes and lifecycle stages.
*- Capability Maturity Model Integration*

- ***WYKŁAD 5*** (234)

*• Requirement Analysis*
*• Test Planning*
	- During planning, we also try to identify metrics, the
	method of gathering and tracking those metrics.
	- This phase is driven by selected test strategy!
*• Test Design*
	- • Detail the test condition;
	- • Identify and get the test data;
	- • Identify and set up the test environment;
	- • Create the test coverage metrics.
*• Test Environment Setup*
	- Test environment configuration must mimic the
	production environment
*• Test Implementation*
*• Test Execution*
	- Manual,
	- Auto,
	- Semi Auto
*• Test Result Analysis and Reporting*
	- No report means no tests done!
*• Test Maintenance*
	- Test maintenance is the modification of tests after
	finishing test execution to correct errors in test cases,
*Test harness*
	- is a part of the test environment comprised of stubs and drivers
	needed to execute a test. Test harness may include also test comparator.

*Test stub*
	- is a software module that acts as temporary replacement for a
called module and gives the same output as that of the actual system.
*Test driver*
	- is a software component or test tool that replaces a component
that takes care of the control and/or the calling

- *** WYKŁAD 6 *** (265)

*• Test*
	- • Test Step
	- • Test Case
	- • Test Suite
	- • Test Procedure
	- • Test
	- • Accurate
		- It shall reflect exactly the purpose of the test
	- • Economical
		- It shall not contain unnecessary steps or words
	- • Traceable
		- Capable of being traced to requirements
	- • Repeatable
		- It can be used to perform the test over and over
	- • Reusable
		- It can be reused if necessary
*-Elements of a Test Case*
	- • Test Case ID
		- The ID of the test case
	- • Test Suite ID
		- The ID of the test suite to which the test case belongs
	- • Test Case Summary
		- The summary or objective of the test case
	- • Related Requirements
		- The ID of the requirement the test case relates, covers or traces
		to
	- • Prerequisites
		- Any prerequisites or preconditions that must be fulfilled prior to
		executing the test
	- • Test Procedure
		- Step-by-step procedure to execute the test
	- • Test Data
		- The test data, or links to the test data, that are to be used while conducting the
		test
	- • Expected Result
		- Expected result of the system output in reaction to the applied input
	- • Actual Result
		- The actual result of the test; to be filled after executing the test
	- • Status
		- „Pass” or „Fail”, „OK” or „NOK”
		- Other statuses can be „Not Executed” if testing is not performed, „Blocked” if
		testing is blocked, „COK” - conditionally OK
	- • Information about System Under Test
		- Information about version of the hardware, software and configuration of the
		system under test
	- • Remarks
		- Any comments on the test case or test execution
	- • Created By
		- The name of the author of the test case
	- • Date of Creation
		- The date of creation of the test case
	- • Executed By
		- The name of the person who executed the test
	- • Date of Execution
		- The date of execution of the test
	- • Test Environment
		- The environment including hardware, software, network, infrastructure,
	- environmental conditions, etc. in which the test was executed
	- • List of Incident Reports
		- List of verification incident reports for each discovered error
*• Test Oracle*
	- is a mechanism to produce the predicted
	outcomes to compare with the actual outcomes of the
	system under test.
*• Test Comparator*
	- is a test tool that compares the actual
	outputs produced by the system under test with the
	expected outputs.
	- Can have speicified tolerances boundaries
*• Test Environment*
	- constitutes of software and hardware
	environment in which the test will be run, and any other software and
	hardware with which the system under test interacts
*• Test Harness*
	Test harness is a part of the test environment comprised of stubs and drivers
	needed to execute a test.

- *** WYKŁAD 7 *** (312)

*• Structural coverage*
	is the coverage measure based on
	the internal structure of the component. This type of the
	test coverage is mainly utilized in white-box testing.
*• Functional coverage*
	is a measure of what functionalities
	and features of the design have been exercised by the
	tests. This type of the test coverage is mainly utilized in
	black-box testing.

*• Code Coverage*
	- **check total usage of code**
	- Statement Coverage
	- Branch Coverage
	- Decision Coverage
	- Condition Coverage
	- Modified Condition Coverage
	- Modified Condition / Decision Coverage
	- LCSAJ Coverage
*• Data Flow Coverage*
	- **check total usage of variables**
	- All-Defs Coverage
	- All-C-Uses Coverage
	- All-C-Uses/Some-P-Uses Coverage
	- All-P-Uses Coverage
	- All-P-Uses/Some-C-Uses Coverage
	- All-Uses Coverage
	- All-Du-Paths Coverage
*Statement coverage*
	- is the percentage of executable statements in a
	component that have been exercised by a test case suite.
		• assignment;
		• for-loop;
		• if-else-statement;
		• switch-statement;
		• call;
		• return;
		• while-loop;
		• etc.
*Branch coverage*
	- is the percentage of branches that
	have been exercised by a test case suite.
	- (basically all of the possible logical combinationss)

**SIL** means **Safety Integrity Level.**

**LCSAJ** stands for **Linear Code Sequence And Jump.**
	- Basically listing the starts, ends, and jumps in terms of code lines.
	- ***HOW IS IT PERFORMABLE AUTOMATICALLY?***
* • Requirements                       *
	- is the percentage of the system requirements
	covered by a test suite. The requirement is considered as being
	covered if at least one test case is assigned to it.
* • Functions                          *
* • States in a finite state machines  *
* • Lines of code                      *
* • Machine code instructions          *
* • Code statements                    *
* • Branches                           *
* • Conditions                         *
* • Paths                              *
* • Entry/exit points                  *

- *** WYKŁAD 8 *** (345)

- *** WYKŁAD 9 *** (351)
* • Software System Testing Levels *
	- Component Testing              
	- Integration Testing            
	- System Testing                 
	- Acceptance Testing             
* • Testing Levels in V-Model      *
* • Testing Levels in Automotive   *

- *** WYKŁAD 10 *** (362)
*• Requirement Driven Testing*
	- is a testing approach in which
	test cases are designed based on test objectives and test
	conditions derived from requirements
*• Code Driven Testing*
	- that is, tests that execute
	specific control flow paths or use specific data items.
*• Risk Driven Testing*
	-It involves the identification of product
	risks and their use in guiding the test process.
*• Reliability Driven Testing*
	- is a testing approach that
	shows the growth in reliability over time during
	continuous testing
*• Model Driven Testing*
	- is a testing approach in which test cases are derived in
	whole or in part from a model
*• Error Guessing Testing*
	- is a testing approach in which the
	experience of the tester is used to postulate what faults
	might occur,
*• Exploratory Testing*
	- is a testing approach where the
	tester actively controls the design of the tests
*• Ad-Hoc Testing*      
	- is a testing approach carried out informally, that is:
	• no formal test preparation takes place;
	• no recognized test design technique is used;
	• there are not expectations for results;
	• arbitrariness guides the test execution activity;
	• „playing with the system”.
	- limited time to do
	elaborative testing.

- *** WYKŁAD 11 *** (381)
*• Functional Testing*
	- is a testing type that based on an analysis of the
	specification of the functionality
*• Performance Testing*
	- proesssing and thrououtput time
*• Configuration Testing*
	-
*• Sanity & Smoke Testing*
*• Regression Testing*
	- means retesting of a previously tested system following
	modification to ensure that faults have not been
	introduced
*• Alpha Testing*
	- potential users or customers or independent test team at the developers’
	site
*• Beta Testing*
	- potential and/or existing
	users/customers
*• Integration Testing*
	- interactions between integrated
	components
*• Usability Testing*
	- understood, learned, used and attractive
*• Acceptance Testing*
*• Installation Testing*
*• Security Testing*
	- unauthorized access, whether accidental or deliberate
*• Statistical Testing*
	- statistical distribution of the input
*• Recovery/Error Handling Testing*

- *** WYKŁAD 12 *** (403)

*Testing Method*
	- description how to create test data,
	test cases and test procedure.
*• Testing Methods Classification*
	* - White-Box Testing*
*• Static Methods*
*• Dynamic Methods*
	* - Black-Box Testing*
	* - Gray-Box Testing*
*• Exhaustive Testing*
	- Exhaustive Testing is a test case design technique in
	which a set of test cases comprises all combinations of
	input values and preconditions.
*• Equivalence Partitioning*
	- The basis for this method is the idea to divide up the input domain into finite number of
	equivalence classes (partitions) of data which, according to the specification, *are treated
	inside the system identically.*
	- This method is applicable for testing when inputs are independent of each other
*• Boundary Value Analysis*
	- The basis for this method is the idea that most errors apears on the edges of equivalence partitions. This method relies on identified equivalence partitions of the input domain and then derives test
	- This method is applicable for testing when inputs are independent of each other.
	data by examining the edges of each partition.
*• Random Testing*
	- is a black-box testing method where the test
	inputs are generated randomly. Expected test outputs shall be
	calculated using test oracle.
*• State Chart (Finite State Machine) Testing*
	- a. *Stateless* - when current behavior is not a function of the past.
		For example: computational systems like this which calculates y=SQRT(x)
	- b. *Continuous* - behavior which do rely on the past feedback values (feedback loop)
		but do not have evident distinguishable states and can assume infinite number
		of values. For example PID controller, digital filter etc.
	- c. *State-driven* - when behavior can be characterized by distinct states
		and for which current behavior is the function of the past.

	- a. State coverage.
		State Coverage Strategy:
		Create a set of tests in that way that all states are visited at least once.
	- b. Events coverage.
		Event Coverage Strategy:
		Create a set of tests in that way that all events are triggered at least once.
	- c. Actions coverage.
	- d. Transition coverage.
		Transition Coverage Strategy:
		Create a set of tests in that way that all transitions are triggered and checked
		at least once.
	- e. Paths coverage
		Path Coverage Strategy:
		Create a set of tests in that way that all paths within the state machine
		are executed at least once.
		For a state machine which has some loops this leads to infinite number
		of tests.
*• Cause-Effect Graphic*
	 - Byyyło
*• All Pairs*
	- During testing there is often a need to test several input variables together.
	This is named combination testing.
*• Metamorphic Testing*
*• Data Flow Testing*
	- uses the control flow graph to explore the
	unreasonable things that can happen to data, that is, data flow
	anomalies.
	- • Variables are used without being initialized
	- • Initialized variables are not used even once
	- • Deleting an object leaving its members inaccessible
