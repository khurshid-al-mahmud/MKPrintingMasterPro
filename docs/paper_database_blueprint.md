# MKPrintingMasterPro ERP

# Paper Database Blueprint

Version : 1.0

Status : Database Design

---

# Purpose

This document defines the database structure of the Paper Management Engine.

No model should be written before this blueprint is finalized.

---

# Database Structure

Paper Type
        │
        ▼
Paper Brand
        │
        ▼
Paper GSM
        │
        ▼
Paper Size
        │
        ▼
Paper
        │
        ├─────────────┐
        ▼             ▼
Paper Rate      Paper Stock

---

# Table 1

paper_types

Purpose

Stores all paper categories.

Examples

Offset

Art Paper

Art Card

Duplex

Ivory

Sticker

Newsprint

PVC

Vinyl

Canvas

Others

---

Fields

id

name

code

display_order

is_active

remarks

created_at

updated_at

---

# Table 2

paper_brands

Purpose

Stores paper manufacturers.

Examples

Bashundhara

APP

Double A

Imported

Local

Others

---

Fields

id

name

country

display_order

is_active

remarks

created_at

updated_at

---

# Table 3

paper_gsm

Purpose

Stores GSM values.

Examples

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

Fields

id

gsm

display_order

is_active

remarks

created_at

updated_at

---

# Table 4

paper_sizes

Purpose

Stores sheet sizes.

Examples

20 × 30

23 × 36

25 × 36

28 × 40

31 × 43

Custom

---

Fields

id

name

width

height

unit

display_order

is_active

remarks

created_at

updated_at

---

# Table 5

papers

Purpose

Main Paper Master.

References

paper_type_id

paper_brand_id

paper_gsm_id

paper_size_id

---

Additional Fields

paper_name

purchase_unit

grain_direction

default_rate

minimum_stock

maximum_stock

is_active

remarks

created_at

updated_at

---

# Table 6

paper_rate_history

Purpose

Stores historical purchase prices.

Fields

id

paper_id

purchase_rate

supplier_id

effective_date

remarks

created_at

---

# Table 7

paper_stock

Purpose

Stores current stock.

Fields

id

paper_id

warehouse_id

opening_stock

current_stock

reserved_stock

available_stock

last_updated

---

# Relationships

paper_types

1

↓

∞

papers

---

paper_brands

1

↓

∞

papers

---

paper_gsm

1

↓

∞

papers

---

paper_sizes

1

↓

∞

papers

---

papers

1

↓

∞

paper_rate_history

---

papers

1

↓

∞

paper_stock

---

# Design Rules

No duplicate Paper Type.

No duplicate Brand.

No duplicate GSM.

No duplicate Size.

Paper Master references all Masters.

Rate history must never overwrite old prices.

Stock must remain independent from purchase history.

---

# Future Expansion

Roll Paper

Digital Media

Large Format Media

Security Paper

Packaging Board

Future Materials

No redesign required.