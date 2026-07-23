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

Controls both Screen Layout and Print Layout.

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
-----------------------------------------

11. Unit Master

Stores all measurement units.

Examples

Piece

Copy

Set

Kg

Rim

Packet

Meter

Square Feet

-----------------------------------------

12. Specification Dependency Rule

Controls field dependency.

Example

Construction Type = Hard Cover

↓

Show

Pustani

Jelly

Jacket

↓

Construction Type = Paper Back

↓

Hide

Pustani

Jelly

Jacket
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
             │                  ├── Unit Master
             │                  └── Template Field Mapping
             │
             ├── Specification Dependency Rule
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
The Dynamic Field Engine is the heart of the Dynamic Specification System.

Its responsibility is to generate Product Specification Forms automatically.

No field will be hard-coded inside the software.

Every visible field will come from the Master Database.

-----------------------------------------

Each Specification Field stores:

• Field Code

• Field Name

• Display Name

• Field Group

• Data Type

• Input Control

• Placeholder

• Default Value

• Required (Yes/No)

• Editable (Yes/No)

• Visible (Yes/No)

• Display Order

• Validation Rule

• Formula Reference (Optional)

-----------------------------------------

Supported Data Types

Text

Long Text

Integer

Decimal

Currency

Percentage

Boolean

Date

Time

Date & Time

Dropdown

Multi Select

Checkbox

Radio Button

File

Image

Dimension

Calculated Value

-----------------------------------------

Supported Input Controls

Textbox

Textarea

Dropdown

Searchable Dropdown

Checkbox

Radio Button

Date Picker

Time Picker

Number Box

File Upload

Image Upload

-----------------------------------------

Field Visibility Rules

A field may appear based on—

• Product Category

• Construction Type

• Template

• Selected Option

• User Role

• Workflow Stage

-----------------------------------------

Example

Product Category

Book

↓

Construction Type

Paper Back

↓

Visible Fields

Book Size

Pages

Paper GSM

Paper Brand

Printing Color

Binding

Quantity

-----------------------------------------

Product Category

Book

↓

Construction Type

Hard Cover

↓

Visible Fields

Book Size

Pages

Paper GSM

Paper Brand

Cover GSM

Pustani

Jelly

Jacket

Foil

Emboss

Binding

Quantity

-----------------------------------------

Changing Product Category or Construction Type immediately reloads the required fields automatically.

No software modification will be required.

Only Master Configuration controls the Dynamic Specification Engine.
-----------------------------------------

Unit Behaviour

Every Quantity field must reference Unit Master.

Examples

100 Piece

500 Copy

2 Rim

15 Kg

50 Meter
## 6. Formula Engine
The Formula Engine performs every business calculation inside MKPrintingMasterPro.

No calculation formula will be hard-coded.

Every calculation will be configurable from the Master Database.

-----------------------------------------

Formula Categories

Quotation Formula

Production Formula

Paper Consumption Formula

Ink Consumption Formula

Plate Formula

Binding Formula

Lamination Formula

Packaging Formula

Cost Formula

Selling Price Formula

-----------------------------------------

Formula Components

Raw Material Cost

Machine Cost

Labour Cost

Electricity Cost

Chemical Cost

Binding Cost

Finishing Cost

Packing Cost

Service Charge

Overhead Cost

Profit Margin

Tax (Optional)

VAT (Optional)

Discount (Optional)

Adjustment (Optional)
Rounding Rule

Transport Charge (Optional)

Loading / Unloading Charge (Optional)

-----------------------------------------

Formula Execution Order

Step-1

Read Product Specification

↓

Step-2

Read Formula Rule

↓

Step-3

Collect Required Cost Components

↓

Step-4

Calculate Material Consumption

↓

Step-5

Calculate Production Cost

↓

Step-6

Apply Service Charge

↓

Step-7

Apply Profit Margin

↓

Step-8

Apply Optional Tax / VAT

↓

Step-9

Apply Optional Discount

↓

Step-10

Apply Optional Adjustment

↓

Step-11

Generate Final Quotation Amount

-----------------------------------------

Formula Version Control

Every Formula Rule stores—

• Version Number

• Effective Date

• Active / Inactive Status

• Created By

• Approved By

• Last Modified Date

Previous formula versions remain stored for historical quotation accuracy.

-----------------------------------------

This design allows future modification of pricing policy without changing program source code.
-----------------------------------------

Narrative Layout Support

The Formula Engine supports two quotation styles.

Style-1

Narrative Description

(Full customer requirement in paragraph form.)

Style-2

Detailed Material Specification

(Item-wise technical specification.)

The Print Layout Rule decides which style will be printed.
## 7. Permission Structure
The Permission Structure controls who can configure the Dynamic Specification Engine.

Normal users will never be allowed to change ERP master definitions.

Only authorized roles can modify the Dynamic Engine.

-----------------------------------------

Permission Levels

Super Administrator

System Administrator

ERP Developer

Business Owner

Manager

Sales Executive

Production Manager

Operator

Viewer

-----------------------------------------

Dynamic Engine Permissions

Create Product Category

Edit Product Category

Delete Product Category

Create Construction Type

Edit Construction Type

Delete Construction Type

Create Specification Template

Edit Specification Template

Delete Specification Template

Create Specification Group

Edit Specification Group

Delete Specification Group

Create Specification Field

Edit Specification Field

Delete Specification Field

Create Field Option

Edit Field Option

Delete Field Option

Create Formula

Edit Formula

Delete Formula

Modify Print Layout

Modify Permission Rule

-----------------------------------------

Approval Policy

Any structural modification requires approval.

Developer

↓

System Administrator

↓

Business Owner

↓

Published

-----------------------------------------

Audit Log

Every modification stores—

• User ID

• Date & Time

• Previous Value

• New Value

• Reason for Change

No configuration change can occur without an Audit Record.

-----------------------------------------

Security Principle

Business Users may use the Dynamic Specification Engine.

Only authorized users may configure it.

This prevents accidental damage to ERP structure while keeping the system fully configurable.
## 8. Future Expansion
The Dynamic Specification Database has been designed for unlimited future expansion.

No source code modification should be required when introducing a new printing product.

Future products can be introduced only through Master Configuration.

-----------------------------------------

Examples

New Product

↓

Security Printing

↓

No programming required.

Only create—

• Product Category

• Construction Type

• Specification Template

• Specification Groups

• Specification Fields

• Formula Rules

• Print Layout Rules

-----------------------------------------

Future Expandable Modules

Label Printing

Barcode Printing

RFID Printing

Digital Printing

Offset Printing

Large Format Printing

Flex Printing

Screen Printing

Garments Printing

Packaging Industry

Medicine Industry

Food Packaging

Export Carton

Commercial Printing

Publishing

Government Tender Printing

-----------------------------------------

Future Expandable Technologies

AI Cost Estimation

AI Production Planning

AI Paper Optimization

AI Machine Scheduling

AI Quotation Assistant

AI Customer Recommendation

AI Inventory Prediction

AI Profit Analysis

AI Business Intelligence Dashboard

-----------------------------------------

Design Philosophy

Configure Once

Use Everywhere

Every future module will follow the same Dynamic Specification Architecture.

This ensures that MKPrintingMasterPro remains scalable, maintainable and future-proof for many years without redesigning the database.
-----------------------------------------

Print Output Modes

Future versions shall support—

• Full Header Printing

• Blank Header Printing

• Print from Serial Number Section

• Narrative Quotation

• Detailed Technical Quotation

• Government Tender Format

Print Layout Rules will control all print behaviours.