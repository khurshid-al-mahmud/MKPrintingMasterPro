# DYNAMIC SPECIFICATION DATABASE

## 1. Purpose
The Dynamic Specification Database is the core engine of MKPrintingMasterPro.

Its purpose is to eliminate hard-coded product specifications.

Instead of programming different fields for every product category, the ERP will dynamically generate product specification screens based on configurable database definitions.

This engine controls—

• Which specification fields appear

• Which fields remain hidden

• Which fields are mandatory

• Field sequence

• Field groups

• Dropdown values

• Calculation formulas

• Quotation Layout

• Job Order Layout

• Production Layout

• Invoice Layout

The same engine will support all current and future printing products without changing source code.

Future products can be introduced simply by configuring master data.

## 2. Master Tables
The Dynamic Specification Engine consists of the following Master Tables.

-----------------------------------------

1. Product Category

Stores all printable product categories.

Examples

Book

Magazine

Brochure

Visiting Card

Poster

Packaging Box

Medicine Box

Sticker

Envelope

Calendar

Diary

-----------------------------------------

2. Construction Type

Stores physical construction method.

Examples

Paper Back

Hard Cover

Center Pin

Perfect Binding

Thread Sewing

Case Binding

Spiral

Glue Binding

-----------------------------------------

3. Specification Template

Defines which template belongs to which Product Category and Construction Type.

Example

Book + Hard Cover

Book + Paper Back

Magazine + Center Pin

Magazine + Perfect Binding

-----------------------------------------

4. Specification Group

Groups specification fields.

Examples

General Information

Paper

Printing

Binding

Cover

Finishing

Packaging

Costing

-----------------------------------------

5. Specification Field

Stores every dynamic field.

Example

Book Size

Pages

Paper GSM

Cover GSM

Binding

Foil

Emboss

Spot UV

Machine

Quantity

-----------------------------------------

6. Field Option

Stores Dropdown values.

Example

A4

A5

300 GSM

350 GSM

Gloss Lamination

Matt Lamination

-----------------------------------------

7. Formula Rule

Stores calculation logic.

Quotation Formula

Cost Formula

Production Formula

Paper Consumption Formula

-----------------------------------------

8. Print Layout Rule

Controls which fields appear in

Quotation

Invoice

Job Order

Production Sheet

-----------------------------------------

9. Permission Rule

Controls who can

Add Field

Edit Field

Delete Field

Hide Field

Change Formula
-----------------------------------------

10. Template Field Mapping

Defines which Field belongs to which Specification Template.

Also controls

• Required

• Optional

• Visible

• Hidden

• Display Order

• Default Value
## 3. Table Relationship
Product Category
    │
    ├── Construction Type
    │
    └── Specification Template
             │
             ├── Specification Group
             │        │
             │        └── Specification Field
             │                  │
             │                  ├── Field Option
             │                  └── Template Field Mapping
             │
             ├── Formula Rule
             └── Print Layout Rule
## 4. Specification Template Flow
Step-1

User selects Product Category.

Example:

Book

↓

Step-2

User selects Construction Type.

Example:

Paper Back

↓

Step-3

ERP automatically loads the correct Specification Template.

↓

Step-4

ERP automatically displays only the required Specification Groups.

↓

Step-5

ERP automatically displays only the required Specification Fields.

↓

Step-6

User enters values.

↓

Step-7

ERP automatically runs Formula Rules.

↓

Step-8

ERP automatically prepares

• Quotation

• Job Order

• Production Sheet

• Invoice

using the same specification data.
## 5. Dynamic Field Engine

## 6. Formula Engine

## 7. Permission Structure

## 8. Future Expansion