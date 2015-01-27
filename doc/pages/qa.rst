QA Plan
=======

Overview
--------

Our quality assurance plan covers both code and documentation components.

While we do have clear roles determining who is responsible for quality control
at each step of the process, we also hope to have a culture in which any member
of the team feels comfortable stepping in at any point and improving our
artifacts. Our rule is that any member can contribute to any part of the
project at any time; however, there is always a member whose duty it is to make
sure that part is finished on time.


Testing
-------

The user interface will be tested manually. These manual tests should cover
key use cases to make sure both that these use cases are working properly and
that they are exposed to the user through the user interface.

Every other code component should be tested in an automatic fashion so as to
avoid regressions when new code is tested. This will also guarantee that code
is tested in a consistent manor by eliminating the possibility of human error
in the testing process.

We will be using Travis-CI to run our test suite every time code is checked in.
The build status will be visible on Travis' website as well as in the README on
our GitHub page. We will also keep track of our test suite's coverage of our
code, based on lines executed during testing. We will be using the tool
`coverage` along with the software as a service provided by coveralls.io. Our
code coverage will be visible on coveralls.io as well as in the README on our
GitHub page.

Code will not be considered thoroughly tested until coverage is above 80%.
Furthermore, all use cases must be manually tested using the user interface.


Reviews
-------

For non-code artifacts, we must consider how to ensure the quality of all documents produced.
For each piece of documentation produced for the project, we will have a primary and secondary writing assignee.
Who is assigned for each document is based on the roles we have each selected.
The duty of the primary assignee is to make sure that the document is thorough where necessary, concise where possible, and completed on time.
After this time, it is the duty of the secondary assignee is to review the document thoroughly.
The reviewer should eliminate typos, make grammar corrections, clarify vague sections, and guarantee the completeness of the document.
After the initial completion of the document, the secondary assignee will have one week or until the project is due, whichever is less, to complete the review.

Once a review is complete, the artifact should be in a completed state. Due to
this constraint, we recommend our reviewers to begin their review early since
it is ultimately their responsibility to make sure that any flaws in the
artifact are corrected within the allotted time.
