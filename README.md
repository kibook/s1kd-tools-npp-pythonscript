s1kd-tools PythonScript interface for Notepad++ - README
========================================================

![s1kd-tools PythonScript
menu](s1kd-tools/docs/ICN-S1KDNPP-A-000000-A-KHZAE-00001-A-001-01.PNG)

General
-------

These are a set of scripts for the
[PythonScript](http://npppythonscript.sourceforge.net) plugin which
provide an interface for using the
[s1kd-tools](https://github.com/kibook/s1kd-tools) within
[Notepad++](https://notepad-plus-plus.org).

Install
-------

Copy the `s1kd-tools` directory to the PythonScript user scripts folder,
typically `%APPDATA%\Notepad++\plugins\config\PythonScript\scripts`.

Functions
---------

-   **Acronyms**

    -   **List acronyms**

        Generate a list of acronyms in the data module.

    -   **Markup acronyms from file**

        Markup acronyms using the specified acronym definitions file.

    -   **Markup acronyms**

        Markup acronyms using the .acronyms file.

    -   **Remove acronym markup**

        Convert acronym markup back to plain text.

-   **Applicability**

    -   **Applicability filtering**

        Filter the CSDB object for a given set of conditions.

    -   **Check all applicability**

        Check the applicability of the CSDB object using all product
        attribute and condition values, as defined in the ACT and CCT.

    -   **Check applicability properties**

        Check that the product attributes, conditions, and values used
        for each are defined in the ACT and CCT.

    -   **Check nested applicability**

        Check that all product attribute and condition values used in
        nested applicability annotations are subsets of the values used
        in their parents.

    -   **Check product applicability**

        Check that the CSDB object is valid for all product instances
        defined in the PCT.

    -   **Check standalone applicability**

        Check the applicability of the CSDB object using only the
        product attribute and condition values explicitly used within
        the object.

    -   **Generate display text**

        Generate the display text for applicability annotations in the
        CSDB object.

-   **BREX**

    -   **Check against BREX DM**

        Check the CSDB object against a selected BREX data module.

    -   **Check against default BREX**

        Check the CSDB object against the appropriate S1000D Default
        BREX.

    -   **Check against referenced BREX**

        Check the CSDB object against the BREX data module it
        references.

-   **New**

    Create new types of CSDB objects.

-   **References**

    -   **Insert reference**

        Insert a reference to a selected CSDB object.

    -   **Synchronize references**

        Generate the References table for a data module.

    -   **Text-to-reference**

        Generate the XML for references from the currently selected
        text.

    -   **Update references**

        Update the titles of referenced CSDB objects.

-   **Transform**

    -   **Add neutral metadata**

        Add IETP neutral metadata to the CSDB object.

    -   **Apply XSL transformation**

        Apply an XSL transform script to the CSDB object.

-   **Add ICN**

    Add the NOTATION and ENTITY declarations for an ICN to the CSDB
    object.

-   **Validate**

    Validate the CSDB object against its schema.
