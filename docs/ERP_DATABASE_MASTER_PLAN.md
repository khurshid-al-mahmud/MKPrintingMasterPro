# MKPrintingMasterPro
## ERP DATABASE MASTER PLAN

Version : 1.0
Build : 012
Status : Master Architecture

---

# ERP Philosophy

MKPrintingMasterPro is a Product Driven ERP.

Every business transaction starts from Product Definition.

Product decides—

• Required Specification Fields

• Required Calculation Formula

• Required Cost Components

• Required Printing Layout

• Required Workflow

• Required Approval Process

• Required Inventory Behaviour

Therefore,

No module will contain hard-coded business fields.

Everything must be configurable through Master Tables.

---

# ERP Design Rules

Rule-1

No duplicated data.

Rule-2

Master Tables store definitions.

Transaction Tables store activities.

Rule-3

Every module must support future expansion.

Rule-4

No business logic inside API.

Business logic only inside Service Layer.

Rule-5

Database design must remain stable for future builds.

Rule-6

Every Product Category owns its own Specification Template.

Rule-7

Quotation, Invoice, Job Order and Production all read from the same Product Definition.

Rule-8

Nothing will be hardcoded if it can be configured.

Rule-9

Every permission must be Role Based.

Rule-10

Every important action must be Audit Logged.
# MASTER TABLE ARCHITECTURE

MKPrintingMasterPro will be divided into two major parts.

--------------------------------------------

PART-1

MASTER DATABASE

--------------------------------------------

Purpose

Stores Definitions.

No business transaction stored here.

Only configuration.

Examples

Company

Branch

User

Role

Permission

Customer Category

Supplier Category

Employee Designation

Product Category

Product

Product Specification Template

Product Dynamic Fields

Paper Brand

Paper GSM

Paper Type

Paper Size

Printing Machine

Binding Type

Lamination Type

Foil Type

Emboss Type

Varnish Type

UV Type

Color Type

Ink Type

Plate Type

Currency

Tax

VAT

Discount Policy

Adjustment Policy

Quotation Layout

Invoice Layout

Print Template

Document Number Sequence

Approval Workflow

Notification Rules

Audit Rules

--------------------------------------------

PART-2

TRANSACTION DATABASE

--------------------------------------------

Purpose

Stores Business Activities.

Examples

Quotation

Quotation Item

Quotation Specification

Quotation Approval

Sales Order

Production Order

Production Cost

Production Process

Purchase

Purchase Item

Goods Receive

Inventory Movement

Stock Ledger

Sales Invoice

Payment Receive

Supplier Payment

Expense Voucher

Journal

Cash Book

Bank Book

General Ledger

Customer Ledger

Supplier Ledger

Employee Ledger

Production Ledger

Audit Log

Notification Log

Document History
# PRODUCT CATEGORY DRIVEN ERP

Every Product Category owns its own Specification Template.

Example

Book

↓

Needs

Book Size

Pages

Paper GSM

Paper Brand

Binding

Cover GSM

Cover Lamination

Cover Color

Inside Color

Plate

Machine

Quantity

--------------------------------------------

Visiting Card

↓

Needs

Card Size

Paper GSM

Paper Brand

Lamination

Spot UV

Foil

Emboss

Corner Cut

Quantity

--------------------------------------------

Poster

↓

Needs

Poster Size

Paper

GSM

Printing Color

Machine

Quantity

--------------------------------------------

Packaging Box

↓

Needs

Length

Width

Height

Board Type

Board GSM

Lamination

UV

Foil

Die Cutting

Pasting

Quantity

--------------------------------------------

Medicine Box

↓

Needs

Length

Width

Height

Board

GSM

Printing Color

Lamination

Foil

Emboss

Glue

Quantity

--------------------------------------------

Magazine

↓

Needs

Size

Pages

Inside Paper

Inside GSM

Cover Paper

Cover GSM

Binding

Lamination

Quantity

--------------------------------------------

Therefore

Product Category decides

• Which fields will appear.

• Which fields remain hidden.

• Which calculation formula will run.

• Which print template will be used.

• Which production workflow will be used.
# DYNAMIC PRODUCT SPECIFICATION ENGINE
Every Product in MKPrintingMasterPro will use a Dynamic Specification Engine.

No Product will have fixed input fields inside the software.

Instead—

Each Product Category owns a Specification Template.

Each Specification Template owns multiple Dynamic Fields.

Example

Book
│
├── Book Size
├── Pages
├── Cover Paper
├── Cover GSM
├── Inside Paper
├── Inside GSM
├── Binding
├── Lamination
├── Quantity

Medicine Box
│
├── Length
├── Width
├── Height
├── Board
├── GSM
├── Printing Color
├── Foil
├── Emboss
├── Glue
├── Quantity

Visiting Card
│
├── Size
├── Paper
├── GSM
├── Lamination
├── Spot UV
├── Foil
├── Emboss
├── Corner Cut
├── Quantity

-------------------------------------------------

Each Dynamic Field contains

• Field Name

• Display Name

• Field Type

• Required / Optional

• Default Value

• Display Order

• Validation Rule

• Unit

• Calculation Rule

• Visibility Rule

-------------------------------------------------

Field Types

Text

Number

Decimal

Dropdown

Checkbox

Radio Button

Date

Yes / No

Auto Calculation

-------------------------------------------------

Visibility Rules

Visible

Hidden

Read Only

Calculated

Optional

Mandatory

-------------------------------------------------

The Specification Engine must generate input forms automatically.

No programmer will manually create Product Forms.

All forms will be generated dynamically from the Specification Template stored in the database.

-------------------------------------------------

Future Benefits

✓ Unlimited Product Categories

✓ Unlimited Dynamic Fields

✓ Unlimited Future Expansion

✓ No Code Change Required

Only Master Configuration will change.