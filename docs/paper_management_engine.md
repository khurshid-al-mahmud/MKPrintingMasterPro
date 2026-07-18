# MKPrintingMasterPro ERP

# Paper Management Engine

Version : 1.0

Status : Design Phase

---

# Purpose

Paper is the most important raw material in a printing press.

The Paper Management Engine will be the single source of paper information for the entire ERP.

Every module must use this engine.

---

# Design Principle

Nothing is hardcoded.

Everything is configurable.

Paper information should never be duplicated.

---

# Overall Architecture

Paper

↓

Paper Type

↓

Paper Brand

↓

Paper GSM

↓

Paper Sheet Size

↓

Paper Rate History

↓

Paper Stock

↓

Quotation

↓

Purchase

↓

Inventory

↓

Production

---

# Master Tables

## Paper

Represents one paper item.

Example

Offset Paper

Art Paper

Art Card

Duplex Board

Ivory Board

Sticker Paper

Kraft Paper

Newsprint

Synthetic Paper

Others

---

## Paper Type

Editable.

Example

Offset

Art

Board

Sticker

Special

Digital

Packaging

---

## Paper Brand

Editable.

Example

Bashundhara

APP

Double A

Imported

Local

Others

---

## Paper GSM

Editable.

Example

60

70

80

90

100

120

150

170

220

250

300

350

400

---

## Paper Sheet Size

Editable.

Example

20 × 30

23 × 36

25 × 36

28 × 40

31 × 43

Custom

---

## Grain Direction

Editable.

Long Grain

Short Grain

Not Applicable

---

# Purchase Information

Purchase Unit

Purchase Rate

Supplier

Purchase Date

Remarks

---

# Stock Information

Opening Stock

Current Stock

Reserved Stock

Available Stock

Minimum Stock

Maximum Stock

---

# Cost Information

Current Rate

Average Rate

Last Purchase Rate

Standard Rate

---

# Future Expansion

Support

Roll Paper

Sheet Paper

Digital Media

PVC

Vinyl

Canvas

One Way Vision

Backlit

---

# System Rules

Every Paper Type must be editable.

Every GSM must be editable.

Every Brand must be editable.

Every Sheet Size must be editable.

Nothing should require programming.

---

# Connected Modules

Quotation

Formula Engine

Purchase

Inventory

Production

Accounts

Reports

---

# Development Goal

One paper entry

↓

Used everywhere

↓

No duplicate information

↓

No redesign in future.