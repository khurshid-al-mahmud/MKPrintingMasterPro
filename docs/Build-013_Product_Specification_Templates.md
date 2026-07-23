# MKPrintingMasterPro
# Build-013
# Product Specification Templates

Version : 1.0
Build : 013
Status : In Development

---

# PURPOSE

This document defines all Product Specification Templates used by MKPrintingMasterPro.

Every Product Category will have its own Dynamic Specification Template.

These templates will be used by:

- Dynamic Specification Engine
- Quotation Engine
- Formula Engine
- Production Engine
- Inventory Engine
- Workflow Engine
- AI Assistant
- AI Agent

No Product Specification will be hardcoded inside the software.

All Product Forms will be generated dynamically from these templates.

---

# TEMPLATE STRUCTURE

Each Product Specification Template contains:

- System Masters
- General Information
- Size & Dimension
- Material
- Paper / Board
- Printing
- Color
- Machine
- Binding
- Finishing
- Packaging
- Cost Components
- Delivery Information

---

# FIELD TYPES

Each Field may use one of the following types:

- Text
- Integer
- Decimal
- Dropdown
- Multi Dropdown
- Checkbox
- Radio Button
- Date
- Boolean (Yes / No)
- Auto Calculation

---

# FIELD PROPERTIES

Every Dynamic Field supports:

- Bangla Display Name
- English Display Name
- Internal Field Name
- Field Type
- Required / Optional
- Default Value
- Display Order
- Visibility Rule
- Validation Rule
- Dependency Rule
- Unit
- Calculation Rule

---

# LANGUAGE SUPPORT

Every Display Name supports:

- Bangla
- English
- Bangla + English

Language will be selected from System Settings.

---

# PERMISSION

Normal Users:

- View Templates
- Use Templates

Administrator:

- Create Template
- Edit Template
- Delete Template
- Reorder Fields
- Change Dependencies
- Add New Fields
- Remove Fields

Every modification must be Audit Logged.

---

# Product Template-001

## Product Category
Book

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Book Information

- Book Type
- Language
- ISBN
- Edition
- Volume
- Part
- Author
- Editor
- Translator
- Publisher
- Publication Year

---

# Size & Dimension

- Finished Width
- Finished Height
- Open Width
- Open Height
- Bleed
- Margin
- Spine Width

---

# Inside Paper

- Paper Brand
- Paper Type
- Paper GSM
- Paper Size
- Grain Direction

---

# Cover Paper

- Cover Brand
- Cover Type
- Cover GSM
- Cover Size

---

# Page Information

- Total Pages
- Total Sheets
- Total Forms
- Blank Pages
- Color Pages
- Black Pages

---

# Printing

- Printing Machine
- Printing Method
- Plate Type
- Plate Quantity
- Ink Type
- Printing Color (Inside)
- Printing Color (Cover)

---

# Binding

- Binding Type
- Glue Type
- Thread Sewing
- Center Pin
- Perfect Binding
- Hard Cover
- Jacket
- Ribbon
- Head Band

---

# Finishing

- Lamination
- Spot UV
- Foil
- Emboss
- Deboss
- Varnish
- Die Cutting
- Corner Cutting
- Folding
- Gathering
- Trimming

---

# Packaging

- Packing Type
- Carton Type
- Shrink Wrap
- Bundle Quantity

---

# Cost Components

- Paper Cost
- Plate Cost
- Printing Cost
- Binding Cost
- Finishing Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved
Template Version : 1.0

# Product Template-002

## Product Category
Magazine

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Magazine Information

- Magazine Type
- Language
- Issue Number
- Volume Number
- Publication Month
- Publication Year
- Editor
- Publisher

---

# Size & Dimension

- Finished Width
- Finished Height
- Open Width
- Open Height
- Bleed
- Margin
- Spine Width

---

# Inside Paper

- Paper Brand
- Paper Type
- Paper GSM
- Paper Size
- Grain Direction

---

# Cover Paper

- Cover Brand
- Cover Type
- Cover GSM
- Cover Size

---

# Page Information

- Total Pages
- Total Sheets
- Total Forms
- Cover Pages
- Inside Pages
- Color Pages
- Black Pages

---

# Printing

- Printing Machine
- Printing Method
- Plate Type
- Plate Quantity
- Ink Type
- Printing Color (Cover)
- Printing Color (Inside)

---

# Binding

- Binding Type
- Center Pin
- Perfect Binding
- Thread Sewing
- Glue Type

---

# Finishing

- Lamination
- Spot UV
- Foil
- Emboss
- Deboss
- Varnish
- Folding
- Trimming

---

# Packaging

- Packing Type
- Carton Type
- Shrink Wrap
- Bundle Quantity

---

# Cost Components

- Paper Cost
- Plate Cost
- Printing Cost
- Binding Cost
- Finishing Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-003

## Product Category
Visiting Card

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Card Information

- Card Type
- Single Side / Double Side
- Orientation (Portrait / Landscape)
- Corner Style
- Number of Designs

---

# Size & Dimension

- Card Width
- Card Height
- Bleed
- Safe Margin

---

# Paper

- Paper Brand
- Paper Type
- Paper GSM
- Paper Size
- Grain Direction

---

# Printing

- Printing Machine
- Printing Method
- Plate Type
- Plate Quantity
- Ink Type
- Front Printing Color
- Back Printing Color

---

# Finishing

- Matte Lamination
- Gloss Lamination
- Soft Touch Lamination
- Spot UV
- Foil
- Emboss
- Deboss
- Die Cutting
- Corner Cutting

---

# Packaging

- Packing Type
- Box Type
- Bundle Quantity

---

# Cost Components

- Paper Cost
- Plate Cost
- Printing Cost
- Finishing Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-004

## Product Category
Poster

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Poster Information

- Poster Type
- Indoor / Outdoor
- Single Side / Double Side
- Orientation (Portrait / Landscape)

---

# Size & Dimension

- Finished Width
- Finished Height
- Bleed
- Safe Margin

---

# Paper

- Paper Brand
- Paper Type
- Paper GSM
- Paper Size
- Grain Direction

---

# Printing

- Printing Machine
- Printing Method
- Plate Type
- Plate Quantity
- Ink Type
- Printing Color

---

# Finishing

- Matte Lamination
- Gloss Lamination
- UV Coating
- Spot UV
- Foil
- Emboss
- Varnish
- Mounting

---

# Packaging

- Packing Type
- Tube Packing
- Flat Packing
- Bundle Quantity

---

# Cost Components

- Paper Cost
- Plate Cost
- Printing Cost
- Finishing Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-005

## Product Category
Medicine Box

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Medicine Information

- Medicine Type
- Generic Name
- Brand Name
- Strength
- Dosage Form
- Pack Size

---

# Box Size & Dimension

- Length
- Width
- Height
- Flat Width
- Flat Height
- Bleed
- Safe Margin

---

# Board Information

- Board Brand
- Board Type
- Board GSM
- Board Size
- Grain Direction

---

# Printing

- Printing Machine
- Printing Method
- Plate Type
- Plate Quantity
- Ink Type
- Printing Color
- Pantone Color

---

# Finishing

- Matte Lamination
- Gloss Lamination
- Soft Touch Lamination
- Spot UV
- Foil
- Emboss
- Deboss
- Varnish
- Aqueous Coating

---

# Die Cutting

- Die Type
- Die Number
- Die Cutting
- Creasing
- Perforation

---

# Gluing & Pasting

- Glue Type
- Side Glue
- Bottom Lock
- Auto Lock
- Crash Lock

---

# Packaging

- Packing Type
- Carton Type
- Bundle Quantity
- Shrink Wrap

---

# Cost Components

- Board Cost
- Plate Cost
- Printing Cost
- Die Cost
- Cutting Cost
- Pasting Cost
- Finishing Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-006

## Product Category
Packaging Box

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Packaging Information

- Packaging Type
- Box Style
- Product Application
- Lock Type
- Window Type

---

# Box Size & Dimension

- Length
- Width
- Height
- Flat Width
- Flat Height
- Bleed
- Safe Margin

---

# Board Information

- Board Brand
- Board Type
- Board GSM
- Board Size
- Grain Direction

---

# Printing

- Printing Machine
- Printing Method
- Plate Type
- Plate Quantity
- Ink Type
- Printing Color
- Pantone Color

---

# Finishing

- Matte Lamination
- Gloss Lamination
- Soft Touch Lamination
- Spot UV
- Foil
- Emboss
- Deboss
- Varnish
- Aqueous Coating

---

# Die Cutting

- Die Type
- Die Number
- Die Cutting
- Creasing
- Perforation

---

# Gluing & Pasting

- Glue Type
- Side Glue
- Bottom Lock
- Auto Lock
- Crash Lock

---

# Packaging

- Packing Type
- Carton Type
- Shrink Wrap
- Bundle Quantity
- Pallet Packing

---

# Cost Components

- Board Cost
- Plate Cost
- Printing Cost
- Die Cost
- Cutting Cost
- Pasting Cost
- Finishing Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-007

## Product Category
Flyer

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Flyer Information

- Flyer Type
- Single Side / Double Side
- Orientation (Portrait / Landscape)
- Folding Type

---

# Size & Dimension

- Finished Width
- Finished Height
- Open Width
- Open Height
- Bleed
- Safe Margin

---

# Paper Information

- Paper Brand
- Paper Type
- Paper GSM
- Paper Size
- Grain Direction

---

# Printing

- Printing Machine
- Printing Method
- Plate Type
- Plate Quantity
- Ink Type
- Front Printing Color
- Back Printing Color

---

# Finishing

- Matte Lamination
- Gloss Lamination
- UV Coating
- Spot UV
- Varnish
- Folding

---

# Packaging

- Packing Type
- Bundle Quantity
- Shrink Wrap

---

# Cost Components

- Paper Cost
- Plate Cost
- Printing Cost
- Folding Cost
- Finishing Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-008

## Product Category
Brochure

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Brochure Information

- Brochure Type
- Number of Pages
- Number of Folds
- Orientation (Portrait / Landscape)

---

# Size & Dimension

- Finished Width
- Finished Height
- Open Width
- Open Height
- Bleed
- Safe Margin

---

# Cover Paper

- Paper Brand
- Paper Type
- Paper GSM
- Paper Size

---

# Inside Paper

- Paper Brand
- Paper Type
- Paper GSM
- Paper Size

---

# Printing

- Printing Machine
- Printing Method
- Plate Type
- Plate Quantity
- Ink Type
- Cover Printing Color
- Inside Printing Color

---

# Binding

- Binding Type
- Center Pin
- Perfect Binding
- Folding

---

# Finishing

- Matte Lamination
- Gloss Lamination
- Spot UV
- Foil
- Emboss
- Varnish

---

# Packaging

- Packing Type
- Bundle Quantity
- Shrink Wrap

---

# Cost Components

- Paper Cost
- Plate Cost
- Printing Cost
- Folding Cost
- Binding Cost
- Finishing Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-009

## Product Category
Leaflet

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Leaflet Information

- Leaflet Type
- Single Side / Double Side
- Orientation (Portrait / Landscape)
- Folding Type

---

# Size & Dimension

- Finished Width
- Finished Height
- Open Width
- Open Height
- Bleed
- Safe Margin

---

# Paper Information

- Paper Brand
- Paper Type
- Paper GSM
- Paper Size
- Grain Direction

---

# Printing

- Printing Machine
- Printing Method
- Plate Type
- Plate Quantity
- Ink Type
- Front Printing Color
- Back Printing Color

---

# Finishing

- Matte Lamination
- Gloss Lamination
- Spot UV
- Varnish
- Folding
- Creasing

---

# Packaging

- Packing Type
- Bundle Quantity
- Shrink Wrap

---

# Cost Components

- Paper Cost
- Plate Cost
- Printing Cost
- Folding Cost
- Creasing Cost
- Finishing Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-010

## Product Category
Sticker

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Sticker Information

- Sticker Type
- Shape
- Application Type
- Indoor / Outdoor
- Adhesive Type

---

# Size & Dimension

- Finished Width
- Finished Height
- Bleed
- Safe Margin

---

# Material

- Material Brand
- Material Type
- Material GSM
- Material Thickness
- Material Size

---

# Printing

- Printing Machine
- Printing Method
- Plate Type
- Plate Quantity
- Ink Type
- Printing Color

---

# Finishing

- Gloss Lamination
- Matte Lamination
- UV Coating
- Spot UV
- Foil
- Emboss
- Die Cutting
- Kiss Cutting
- Contour Cutting

---

# Packaging

- Roll Packing
- Sheet Packing
- Bundle Quantity

---

# Cost Components

- Material Cost
- Plate Cost
- Printing Cost
- Die Cutting Cost
- Finishing Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-011

## Product Category
Envelope

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Envelope Information

- Envelope Type
- Window Envelope (Yes / No)
- Security Print (Yes / No)
- Flap Type
- Opening Direction

---

# Size & Dimension

- Finished Width
- Finished Height
- Flap Size
- Bleed
- Safe Margin

---

# Paper Information

- Paper Brand
- Paper Type
- Paper GSM
- Paper Size
- Grain Direction

---

# Printing

- Printing Machine
- Printing Method
- Plate Type
- Plate Quantity
- Ink Type
- Front Printing Color
- Back Printing Color

---

# Finishing

- Window Cutting
- Gum Type
- Self Adhesive
- Varnish
- Spot UV
- Foil

---

# Packaging

- Bundle Quantity
- Carton Type
- Shrink Wrap

---

# Cost Components

- Paper Cost
- Plate Cost
- Printing Cost
- Window Cutting Cost
- Gum Cost
- Finishing Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-012

## Product Category
Letterhead

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Letterhead Information

- Letterhead Type
- Company Type
- Single Side / Double Side
- Orientation (Portrait / Landscape)

---

# Size & Dimension

- Finished Width
- Finished Height
- Bleed
- Safe Margin

---

# Paper Information

- Paper Brand
- Paper Type
- Paper GSM
- Paper Size
- Grain Direction

---

# Printing

- Printing Machine
- Printing Method
- Plate Type
- Plate Quantity
- Ink Type
- Front Printing Color
- Back Printing Color

---

# Finishing

- Matte Finish
- Gloss Finish
- Spot UV
- Foil
- Emboss
- Watermark

---

# Packaging

- Bundle Quantity
- Carton Type
- Shrink Wrap

---

# Cost Components

- Paper Cost
- Plate Cost
- Printing Cost
- Finishing Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-013

## Product Category
Invoice / Money Receipt / Cash Memo

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Document Information

- Document Type
- Invoice Type
- Money Receipt Type
- Cash Memo Type
- Delivery Challan Type

---

# Size & Dimension

- Finished Width
- Finished Height
- Bleed
- Safe Margin

---

# Paper Information

- Paper Brand
- Paper Type
- Paper GSM
- Paper Size
- Number of Copies

---

# Numbering

- Auto Numbering
- Manual Numbering
- Duplicate Copy
- Triplicate Copy
- Serial Number Format

---

# Printing

- Printing Machine
- Printing Method
- Plate Type
- Plate Quantity
- Ink Type
- Front Printing Color
- Back Printing Color

---

# Finishing

- Numbering
- Perforation
- Padding
- Glue Binding
- Stapling

---

# Packaging

- Bundle Quantity
- Carton Type
- Shrink Wrap

---

# Cost Components

- Paper Cost
- Plate Cost
- Printing Cost
- Numbering Cost
- Perforation Cost
- Binding Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-013

## Product Category
Invoice / Money Receipt / Cash Memo

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Document Information

- Document Type
- Invoice Type
- Money Receipt Type
- Cash Memo Type
- Delivery Challan Type

---

# Size & Dimension

- Finished Width
- Finished Height
- Bleed
- Safe Margin

---

# Paper Information

- Paper Brand
- Paper Type
- Paper GSM
- Paper Size
- Number of Copies

---

# Numbering

- Auto Numbering
- Manual Numbering
- Duplicate Copy
- Triplicate Copy
- Serial Number Format

---

# Printing

- Printing Machine
- Printing Method
- Plate Type
- Plate Quantity
- Ink Type
- Front Printing Color
- Back Printing Color

---

# Finishing

- Numbering
- Perforation
- Padding
- Glue Binding
- Stapling

---

# Packaging

- Bundle Quantity
- Carton Type
- Shrink Wrap

---

# Cost Components

- Paper Cost
- Plate Cost
- Printing Cost
- Numbering Cost
- Perforation Cost
- Binding Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-014

## Product Category
Pad

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Pad Information

- Pad Type
- Number of Sheets
- Number of Pages
- Single Side / Double Side
- Numbering Required

---

# Size & Dimension

- Finished Width
- Finished Height
- Bleed
- Safe Margin

---

# Paper Information

- Paper Brand
- Paper Type
- Paper GSM
- Paper Size

---

# Printing

- Printing Machine
- Printing Method
- Plate Type
- Plate Quantity
- Ink Type
- Front Printing Color
- Back Printing Color

---

# Binding

- Glue Binding
- Top Glue
- Side Glue
- Stapling
- Hard Back Board

---

# Finishing

- Numbering
- Perforation
- Punch Hole
- Trimming

---

# Packaging

- Bundle Quantity
- Carton Type
- Shrink Wrap

---

# Cost Components

- Paper Cost
- Plate Cost
- Printing Cost
- Binding Cost
- Numbering Cost
- Perforation Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-015

## Product Category
ID Card

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Card Information

- Card Type
- Single Side / Double Side
- Orientation
- Card Standard
- Variable Data Printing

---

# Size & Dimension

- Finished Width
- Finished Height
- Bleed
- Safe Margin
- Corner Radius

---

# Material

- Card Material
- Material Thickness
- Material Finish

---

# Printing

- Printing Machine
- Printing Method
- Plate Type
- Plate Quantity
- Ink Type
- Front Printing Color
- Back Printing Color

---

# Personalisation

- Barcode
- QR Code
- Serial Number
- Magnetic Stripe
- RFID / NFC
- Signature Panel

---

# Finishing

- Matte Lamination
- Gloss Lamination
- Spot UV
- Foil
- Emboss
- Deboss
- Hole Punch
- Round Corner

---

# Packaging

- Individual Packing
- Bundle Quantity
- Carton Type

---

# Cost Components

- Material Cost
- Plate Cost
- Printing Cost
- Personalisation Cost
- Finishing Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-016

## Product Category
T-Shirt

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Garment Information

- Garment Type
- Sleeve Type
- Gender
- Size
- Fabric Type
- Fabric GSM
- Fabric Color
- Brand

---

# Printing Information

- Printing Method
- Printing Side
- Number of Colors
- Ink Type
- Print Position
- Design Size

---

# Printing Machine

- Printing Machine
- Heat Press
- Screen Printing Machine
- DTF Printer
- Sublimation Printer
- Vinyl Cutter

---

# Finishing

- Washing Test
- Heat Curing
- Folding
- Poly Bag Packing
- Tag Attachment

---

# Packaging

- Individual Packing
- Bundle Quantity
- Carton Type

---

# Cost Components

- Garment Cost
- Printing Cost
- Ink Cost
- Heat Press Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-017

## Product Category
Banner / Festoon

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Banner Information

- Banner Type
- Indoor / Outdoor
- Display Type
- Stand Type

---

# Size & Dimension

- Finished Width
- Finished Height
- Bleed
- Safe Margin

---

# Material

- Banner Material
- Material Brand
- Material GSM
- Material Thickness
- Material Finish

---

# Printing

- Printing Machine
- Printing Method
- Printing Resolution
- Ink Type
- Printing Color

---

# Finishing

- Eyelet
- Rope
- Pocket
- Stitching
- Welding
- Pole Support
- Lamination
- UV Protection

---

# Packaging

- Roll Packing
- Fold Packing
- Bundle Quantity

---

# Cost Components

- Material Cost
- Printing Cost
- Eyelet Cost
- Rope Cost
- Stitching Cost
- Welding Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-018

## Product Category
Calendar

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Calendar Information

- Calendar Type
- Year
- Month Format
- Number of Sheets
- Hanging Type
- Stand Type

---

# Size & Dimension

- Finished Width
- Finished Height
- Bleed
- Safe Margin

---

# Paper Information

- Cover Paper Brand
- Cover Paper Type
- Cover Paper GSM
- Inside Paper Brand
- Inside Paper Type
- Inside Paper GSM

---

# Printing

- Printing Machine
- Printing Method
- Plate Type
- Plate Quantity
- Ink Type
- Cover Printing Color
- Inside Printing Color

---

# Binding

- Wire Binding
- Spiral Binding
- Saddle Stitch
- Glue Binding

---

# Finishing

- Matte Lamination
- Gloss Lamination
- Spot UV
- Foil
- Emboss
- Die Cutting
- Corner Round

---

# Packaging

- Poly Bag Packing
- Bundle Quantity
- Carton Type

---

# Cost Components

- Cover Paper Cost
- Inside Paper Cost
- Plate Cost
- Printing Cost
- Binding Cost
- Finishing Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-019

## Product Category
Notebook / Diary

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Notebook / Diary Information

- Product Type
- Cover Type
- Usage Type
- Number of Pages
- Number of Sheets
- Ruled Type
- Perforation

---

# Size & Dimension

- Finished Width
- Finished Height
- Open Width
- Open Height
- Bleed
- Safe Margin
- Spine Width

---

# Cover Paper

- Cover Paper Brand
- Cover Paper Type
- Cover Paper GSM
- Cover Board Type

---

# Inside Paper

- Paper Brand
- Paper Type
- Paper GSM
- Paper Size

---

# Printing

- Printing Machine
- Printing Method
- Plate Type
- Plate Quantity
- Ink Type
- Cover Printing Color
- Inside Printing Color

---

# Binding

- Perfect Binding
- Spiral Binding
- Wire Binding
- Thread Sewing
- Hard Cover
- Soft Cover
- Elastic Band
- Ribbon Marker

---

# Finishing

- Matte Lamination
- Gloss Lamination
- Spot UV
- Foil
- Emboss
- Deboss
- Corner Round
- Die Cutting

---

# Packaging

- Individual Packing
- Shrink Wrap
- Bundle Quantity
- Carton Type

---

# Cost Components

- Cover Paper Cost
- Inside Paper Cost
- Plate Cost
- Printing Cost
- Binding Cost
- Finishing Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-020

## Product Category
Certificate / Certificate Folder

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Certificate Information

- Certificate Type
- Folder Type
- Orientation
- Security Level
- Serial Number
- QR Code
- Barcode

---

# Size & Dimension

- Finished Width
- Finished Height
- Open Width
- Open Height
- Bleed
- Safe Margin

---

# Material

- Paper Brand
- Paper Type
- Paper GSM
- Board Type
- Board GSM

---

# Printing

- Printing Machine
- Printing Method
- Plate Type
- Plate Quantity
- Ink Type
- Front Printing Color
- Back Printing Color

---

# Security Features

- Watermark
- Hologram
- Micro Text
- UV Security
- Invisible Ink
- Security Numbering

---

# Finishing

- Matte Lamination
- Gloss Lamination
- Spot UV
- Foil
- Emboss
- Deboss
- Die Cutting
- Corner Round

---

# Packaging

- Individual Packing
- Bundle Quantity
- Carton Type

---

# Cost Components

- Paper Cost
- Board Cost
- Plate Cost
- Printing Cost
- Security Feature Cost
- Finishing Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-021

## Product Category
Universal Custom Product

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Dynamic Specification Area

This section has no predefined fields.

Administrator can create unlimited Dynamic Specification Groups.

Examples:

- Size
- Material
- Paper
- Board
- Fabric
- Plastic
- Metal
- Wood
- Printing
- Machine
- Binding
- Finishing
- Packaging
- Delivery
- Others

Every Group may contain unlimited Dynamic Fields.

---

# Supported Field Types

- Text
- Integer
- Decimal
- Currency
- Percentage
- Dropdown
- Multi Dropdown
- Checkbox
- Radio Button
- Date
- Time
- Boolean
- Auto Calculation
- Formula Result
- Image
- File Attachment
- QR Code
- Barcode

---

# Field Properties

Each Dynamic Field supports:

- Bangla Display Name
- English Display Name
- Internal Field Name
- Field Type
- Required / Optional
- Default Value
- Display Order
- Validation Rule
- Visibility Rule
- Dependency Rule
- Formula Rule
- Unit
- Help Text

---

# Workflow

Workflow is fully configurable.

Administrator can define unlimited workflow steps.

Examples

Quotation

↓

Design

↓

Approval

↓

Production

↓

Packing

↓

Delivery

or

Any Custom Workflow

---

# Cost Components

Administrator can create unlimited Cost Heads.

Examples

- Material Cost
- Printing Cost
- Machine Cost
- Labour Cost
- Design Cost
- Outsourcing Cost
- Packaging Cost
- Delivery Cost
- Other Cost

---

# Permission

Administrator

- Create Template
- Edit Template
- Delete Template
- Create Groups
- Delete Groups
- Create Fields
- Delete Fields
- Change Formula
- Change Workflow

Normal User

- Use Template
- Fill Values

Cannot modify template structure.

---

# Audit

Every structural change must be Audit Logged.

Template Version History must be maintained.

Rollback must be supported.

---

Status : Approved

Template Version : 1.0

# Product Template-022

## Product Category
PVC Card / RFID Card / Smart Card

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Card Information

- Card Type
- Card Size
- Card Thickness
- Orientation
- Corner Type
- Surface Finish

---

# Material

- PVC Type
- PVC Thickness
- PVC Color
- Transparent PVC
- White PVC
- Metallic PVC
- Eco PVC

---

# Printing

- Printing Method
- Printing Machine
- Printing Side
- Printing Color (Front)
- Printing Color (Back)
- Ink Type
- Plate Type

---

# Security Features

- RFID
- NFC
- Magnetic Strip
- Barcode
- QR Code
- Serial Number
- Variable Data Printing
- Hologram
- UV Security Print
- Scratch Panel

---

# Personalisation

- Name Printing
- ID Number
- Employee Code
- Photo Printing
- Signature Printing
- Chip Encoding
- RFID Encoding
- NFC Encoding

---

# Finishing

- Gloss Lamination
- Matt Lamination
- Spot UV
- Foil
- Emboss
- Deboss
- Overlay
- Punch Hole
- Slot Punch

---

# Packaging

- Individual Sleeve
- Plastic Box
- Paper Box
- Bundle Quantity
- Carton Quantity

---

# Cost Components

- PVC Cost
- Printing Cost
- Encoding Cost
- Personalisation Cost
- Finishing Cost
- Packaging Cost
- Design Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-023

## Product Category
Flexible Packaging / Pouch / Roll Label

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Packaging Information

- Packaging Type
- Pouch Type
- Label Type
- Roll Label
- Flat Label
- Wrap Around Label
- Sachet Type

---

# Size & Dimension

- Width
- Height
- Gusset
- Bottom Fold
- Roll Width
- Roll Length
- Bleed
- Safe Margin

---

# Material

- Film Type
- Material Brand
- Material Thickness
- Material GSM
- Layer Structure
- Transparent
- White Film
- Metallic Film
- Aluminium Foil
- Kraft Paper

---

# Printing

- Printing Machine
- Printing Method
- Plate Type
- Plate Quantity
- Ink Type
- Printing Color
- Reverse Printing

---

# Finishing

- Matte Lamination
- Gloss Lamination
- Soft Touch Lamination
- Spot UV
- Foil
- Emboss
- Die Cutting
- Easy Tear Notch
- Zip Lock
- Euro Hole
- Window Cut
- Heat Seal

---

# Packaging

- Roll Packing
- Bundle Packing
- Carton Quantity

---

# Cost Components

- Material Cost
- Printing Cost
- Plate Cost
- Lamination Cost
- Die Cutting Cost
- Zip Lock Cost
- Heat Seal Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-024

## Product Category
Large Format Printing / Signage / Display / Miscellaneous Products

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Product Information

- Product Type
- Indoor / Outdoor
- Single Side
- Double Side
- Temporary
- Permanent

---

# Size & Dimension

- Width
- Height
- Depth
- Diameter
- Thickness
- Bleed
- Safe Margin

---

# Material

- Flex
- Vinyl
- Star Flex
- Frontlit
- Backlit
- One Way Vision
- Frosted Film
- Clear Sticker
- PVC Sheet
- Acrylic Sheet
- ACP Sheet
- Foam Board
- Sun Board
- MDF
- Wood
- Metal
- Glass
- Canvas
- Fabric

---

# Printing

- Printing Machine
- Printing Method
- Printing Resolution
- Ink Type
- Printing Color
- White Ink
- UV Printing
- Eco Solvent
- Solvent
- Latex Printing

---

# Structure

- Frame Type
- Pipe Size
- Angle Bar
- Box Frame
- Stand Type
- Hanging Type
- Wall Mounted
- Pole Mounted

---

# Electrical

- LED Type
- LED Color
- LED Quantity
- Power Supply
- Adapter
- Controller
- Wiring

---

# Finishing

- Lamination
- Cold Lamination
- Hot Lamination
- UV Coating
- Spot UV
- Foil
- Emboss
- Die Cutting
- CNC Cutting
- Laser Cutting
- Eyelet
- Rope
- Clip
- Welding
- Installation

---

# Packaging

- Roll Packing
- Bubble Wrap
- Carton
- Wooden Box

---

# Cost Components

- Material Cost
- Printing Cost
- Machine Cost
- Frame Cost
- LED Cost
- Installation Cost
- Transport Cost
- Packaging Cost
- Design Charge
- Proof Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method
- Installation Required

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-025

## Product Category
Mug Printing

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Mug Information

- Mug Type
- Mug Capacity (oz)
- Mug Shape
- Mug Finish
- Mug Grade

---

# Material

- Ceramic Mug
- Glass Mug
- Steel Mug
- Plastic Mug
- Magic Mug
- Frosted Mug
- Color Changing Mug

---

# Mug Color

- White
- Black
- Red
- Blue
- Green
- Yellow
- Custom Color

---

# Handle & Inner Color

- Same Color
- Different Handle Color
- Different Inner Color

---

# Printing

- Printing Method
- Sublimation Printing
- UV Printing
- DTF Transfer
- Screen Printing
- Laser Engraving

---

# Printing Area

- Front Only
- Back Only
- Double Side
- Full Wrap Around
- Inside Bottom
- Handle Printing

---

# Artwork

- Customer Artwork
- Design Required
- Photo Printing
- Logo Printing
- Text Printing
- QR Code
- Barcode

---

# Finishing

- Gloss Finish
- Matte Finish
- Protective Coating

---

# Quality Control

- Color Matching
- Heat Test
- Scratch Test
- Print Alignment

---

# Packaging

- Individual Mug Box
- Gift Box
- Foam Packing
- Bubble Wrap
- Carton Quantity

---

# Cost Components

- Mug Cost
- Printing Cost
- Design Charge
- Packaging Cost
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0

# Product Template-026

## Product Category
Crest / Trophy / Award Printing

---

# System Masters

- Product Category
- Product Sub Category
- Product Type
- Product Status
- Product Version

---

# General Information

- Product Name (Bangla)
- Product Name (English)
- Product Code
- SKU Code
- Customer Product Code
- Quantity
- Unit
- Remarks

---

# Award Information

- Award Type
- Crest Type
- Trophy Type
- Shield Type
- Memento Type
- Souvenir Type

---

# Material

- Wood
- Acrylic
- Crystal
- Glass
- Metal
- Brass
- Stainless Steel
- MDF
- Fiber
- Resin
- Mixed Material

---

# Size & Dimension

- Width
- Height
- Thickness
- Base Width
- Base Height
- Weight

---

# Base Information

- Base Type
- Base Material
- Base Color

---

# Printing / Engraving

- UV Printing
- Sublimation Printing
- Screen Printing
- Laser Engraving
- CNC Engraving
- Metal Etching

---

# Artwork

- Logo
- Organization Name
- Recipient Name
- Designation
- Award Title
- Event Name
- Date
- QR Code
- Barcode

---

# Decoration

- Gold Foil
- Silver Foil
- Gold Plate
- Silver Plate
- Color Plate
- Raised Logo

---

# Finishing

- Gloss Finish
- Matte Finish
- Polishing
- Edge Finishing
- Protective Coating

---

# Accessories

- Stand
- Gift Box
- Velvet Box
- Satin Cloth
- Foam Insert

---

# Packaging

- Individual Box
- Premium Gift Box
- Bubble Wrap
- Carton Quantity

---

# Cost Components

- Material Cost
- Printing Cost
- Engraving Cost
- Base Cost
- Finishing Cost
- Packaging Cost
- Design Charge
- Delivery Charge
- Other Charge

---

# Delivery

- Delivery Date
- Delivery Location
- Delivery Method

---

# Dynamic Field Support

Administrator can

- Add New Field
- Delete Field
- Edit Field
- Reorder Field
- Change Validation
- Change Dependency
- Enable / Disable Field

Normal User cannot modify template.

---

Status : Approved

Template Version : 1.0