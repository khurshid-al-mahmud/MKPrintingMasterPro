# MKPrintingMasterPro ERP

# Dynamic Product Specification Engine (DPSE)

Version : 1.0

Status : Design Phase

---

# Purpose

Every printing product has different specifications.

Instead of creating a separate fixed form for every product, the ERP will generate the specification form dynamically.

This makes the ERP future-proof.

No programming will be required when adding a new product.

---

# Overall Architecture

Product

↓

Product Category

↓

Specification Template

↓

Specification Section

↓

Specification Field

↓

Dropdown Values

↓

Quotation

↓

Job Order

---

# Layer 1

## Product

Examples

Book

Memo

Visiting Card

Leaflet

Poster

Banner

Sticker

Packaging

Digital Print

Others

---

# Layer 2

## Product Category

Every product may contain multiple categories.

Example

Book

Paperback

Hardcover

Magazine

Diary

Notebook

Question Bank

---

Memo

Single

Duplicate

Triplicate

Four Part

Five Part

---

Banner

PVC

Flex

Vinyl

Canvas

Backlit

One Way Vision

---

# Layer 3

## Specification Template

Each category owns one template.

Example

Paperback Template

Hardcover Template

Triplicate Memo Template

PVC Banner Template

---

# Layer 4

## Specification Section

Fields are grouped into logical sections.

Example

General Information

Paper Information

Printing Information

Binding Information

Finishing Information

Packing Information

Delivery Information

Others

---

# Layer 5

## Specification Field

Each section contains multiple fields.

Examples

Finished Size

Flat Size

Page

Paper GSM

Paper Brand

Paper Type

Printing Side

Printing Color

Binding

Lamination

Foil

Spot UV

Numbering

Carbon Copy

Perforation

Packing

Delivery Date

Remarks

---

# Layer 6

## Dropdown Values

Every dropdown value is editable.

Examples

Binding

Center Pin

Perfect

Thread

Hard Cover

Glue

---

Carbon Copy

Single

Duplicate

Triplicate

4 Part

5 Part

---

Lamination

None

Gloss

Matt

Soft Touch

Thermal

---

# Field Types

Supported field types

Text

Textarea

Number

Decimal

Date

Checkbox

Radio

Dropdown

Multi Select

File

---

# Field Behaviour

Every field supports

Required

Optional

Hidden

Read Only

Default Value

Validation Rule

Display Order

Help Text

---

# Dynamic Rendering

ERP will generate the complete form automatically.

Example

Product

↓

Book

↓

Paperback

↓

System loads Paperback Template

↓

User fills data

↓

Quotation created

---

# Future Expansion

Without programming the ERP must support

Digital Printing

Large Format Printing

Packaging

Screen Printing

Garments

Laser Cutting

CNC

Sublimation

Offset Printing

---

# Design Principle

Nothing is hardcoded.

Everything is configurable.

Everything is reusable.

Everything is scalable.

---

# Goal

A new printing product should be added entirely from the Admin Panel.

No developer should be required.