============================
Gitflow Workflow
============================

As a general rule, commits should be small and frequent - don't let your changes pile up into one big commit!

We use the Gitflow Workflow to manage this project.  For detailed instructions, please reference the following article.

https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow

We recommend using the SourceTree app which streamlines the Gitflow Workflow for you.

https://www.sourcetreeapp.com

A summary of the Gitflow Workflow is provided here for convenience.

develop
============================

The `develop` branch is the default branch that developers should work in and branch from.

This branch is often deployed to the test/staging server for testing.

master
============================

The `master` branch stores the official release history that is deployed to the production server.

In most cases, you should not need to work with the `master` branch directly.  Work off of the `develop` branch instead.

feature branches
============================

Each new feature should reside in its own branch and branch off of `develop`.

When a feature is complete, it gets merged back into `develop`.

release branches
============================

Once `develop` has acquired enough features for a release, fork a release off of `develop`.

Once the release is ready to ship, it gets merged into master and tagged with a version number.

hotfix branches
============================

Only use this to quickly patch production releases.  This is the only branch that should fork directly of `master`.


============================
Git Best Practices
============================

Commits should be small and frequent - commit whenever you make a single logical change.