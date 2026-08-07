# MKPrintingMasterPro ERP

# Printing Quotation Engine Architecture v1.0

---

## Purpose

The Quotation Engine is the heart of the ERP.

Every quotation must calculate the actual production cost automatically and generate a professional selling price.

The Quotation Engine will be the source for:

- Job Order
- Production
- Purchase Planning
- Inventory Consumption
- Invoice
- Profit Analysis

---

# Overall Workflow

Customer

↓

Quotation

↓

Cost Calculation

↓

Selling Price

↓

Approval

↓

Job Order

↓

Production

↓

Delivery

↓

Invoice

---

# Main Components

The quotation engine will consist of the following components.

## 1. Customer

Quotation belongs to one customer.

---

## 2. Product

Quotation is always created for one product.

Example

- Visiting Card
- Flyer
- Brochure
- Book
- Banner
- Sticker

---

## 3. Product Specification

Every quotation contains specifications.

Examples

Finished Size

Paper Size

Paper GSM

Paper Type

Printing Side

Color

Quantity

Binding

Lamination

UV

Foil

Emboss

Die Cut

Packing

Remarks

---

## 4. Formula Engine

The Formula Engine calculates:

Paper Consumption

↓

Printing Cost

↓

Finishing Cost

↓

Overhead

↓

Profit

↓

Selling Price

---

## 5. Cost Engine

The Cost Engine calculates every individual cost.

Paper Cost

Ink Cost

Plate Cost

Machine Cost

Labour Cost

Finishing Cost

Packing Cost

Delivery Cost

Misc Cost

---

## 6. Selling Price

Selling Price =

Production Cost

+

Overhead

+

Profit

−

Discount

+

VAT

---

# Future Modules Connected

Quotation will connect with:

Customer

↓

Product

↓

Paper

↓

Machine

↓

Finishing

↓

Formula

↓

Inventory

↓

Purchase

↓

Job Order

↓

Production

↓

Accounts

↓

Invoice

---

# Design Principle

No hardcoded calculation.

Every editable value must come from Master Data or Settings.

The engine should support:

Offset Printing

Digital Printing

Large Format Printing

Packaging Printing

without changing the architecture.

---

# Status

Architecture Version

v1.0

Status

Approved for Development