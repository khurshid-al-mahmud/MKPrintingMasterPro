# Party Module Design Document

# MKPrintingMasterPro ERP

---

# Version

Version : 1.1

Status : Final Draft

Module : Party Management

---

# 1. Purpose (উদ্দেশ্য)

Party Module হলো MKPrintingMasterPro ERP-এর অন্যতম Core Module।

এই Module-এর মাধ্যমে ERP-এর সকল ব্যক্তি (Individual) এবং প্রতিষ্ঠান (Business / Organization)-এর মূল তথ্য সংরক্ষণ করা হবে।

এই Module ব্যবহার করবে—

- Customer Management
- Supplier Management
- Employee Management
- Sales
- Purchase
- Accounts
- Production
- CRM (Future)

একজন ব্যক্তি বা প্রতিষ্ঠান Database-এ মাত্র একবার সংরক্ষিত হবে।

---

# 2. Core Design Principle

ERP-এর মূল Entity হবে **Party**।

Customer, Supplier অথবা Employee আলাদা Entity নয়।

সবাই Party-এর বিভিন্ন Business Role।

---

# 3. Business Requirement

System অবশ্যই নিচের Business Flow সমর্থন করবে।

## Direct Customer

Customer → Design → Printing → Delivery → Payment

## Print Partner

Print Partner → Design (Optional) → Printing → Delivery → Payment

## Design Only

Customer → Design → Payment

## Printing Only

Customer → Printing → Payment

## Complete Production

Customer

↓

Design

↓

Paper

↓

Plate

↓

Printing

↓

Binding

↓

Delivery

↓

Payment

---

# 4. Party Structure

```text
Party (Master)
│
├── Party Roles
│      ├── Customer
│      ├── Print Partner
│      ├── Supplier
│      ├── Employee
│      ├── Designer
│      ├── Courier
│      └── Transport Vendor
│
├── Party Contacts
│      ├── Contact Person
│      ├── Designation
│      ├── Mobile
│      └── Email
│
├── Customer Profile
│      └── Customer Number (CUS-000001)
│
├── Supplier Profile
│      └── Supplier Number (SUP-000001)
│
└── Employee Profile
       └── Employee Number (EMP-000001)
```

একটি Party-এর একাধিক Business Role থাকতে পারে।

---

## Example-1

```text
Party : ABC Traders

Party ID : 125

Roles
│
├── Print Partner
│      └── CUS-000015
│
└── Supplier
       └── SUP-000008

Contacts
│
├── Rahim
│      Purchase Officer
│
└── Karim
       Accounts Officer
```

---

## Example-2

```text
Party : Abdul Karim

Party ID : 281

Roles
│
├── Customer
│      └── CUS-000025
│
├── Supplier
│      └── SUP-000007
│
└── Employee
       └── EMP-000003
```

---

## Design Rules

- Party Record Database-এ মাত্র একটি থাকবে।
- একটি Party-এর একাধিক Business Role থাকতে পারবে।
- প্রতিটি Role-এর নিজস্ব Number থাকবে।
- একটি Company বা Organization-এর একাধিক Contact Person রাখা যাবে।
- ভবিষ্যতে নতুন Business Role যোগ করতে Database Structure পরিবর্তন করতে হবে না।

---

# 5. Party Master Table

Party Master হলো ERP-এর Central Table।

Customer, Supplier, Employee, Print Partner অথবা ভবিষ্যতের অন্য যেকোনো Business Role-এর মূল তথ্য এই Table-এ সংরক্ষিত হবে।

একই ব্যক্তি বা প্রতিষ্ঠানকে দ্বিতীয়বার Create করা যাবে না।

Role পরিবর্তন হলেও Party Record অপরিবর্তিত থাকবে।

Party ID হবে Internal Primary Key।

Customer Number, Supplier Number এবং Employee Number আলাদা Profile Table থেকে Generate হবে।



# 6. Party Master Table Fields

নিচে Party Master Table-এর প্রস্তাবিত Field List দেওয়া হলো।

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| id | Integer | Primary Key |
| party_type | Enum | Individual / Business / Organization |
| party_name | Varchar(200) | Full Name বা Company Name |
| display_name | Varchar(200) | Short Name (Invoice / Reports) |
| mobile | Varchar(20) | Primary Mobile Number |
| alternate_mobile | Varchar(20) | Secondary Mobile Number |
| whatsapp | Varchar(20) | WhatsApp Number |
| email | Varchar(150) | Email Address |
| website | Varchar(200) | Website |
| address | Text | Full Address |
| area | Varchar(100) | Area / Locality |
| district | Varchar(100) | District |
| division | Varchar(100) | Division |
| country | Varchar(100) | Country |
| remarks | Text | Additional Notes |
| is_active | Boolean | Active / Inactive |
| created_at | DateTime | Record Creation Time |
| updated_at | DateTime | Last Update Time |

---

# 7. Party Role Concept

একটি Party একাধিক Business Role ধারণ করতে পারবে।

উদাহরণ:

```text
Party : ABC Traders

Roles

✓ Print Partner

✓ Supplier
```

আরেকটি উদাহরণ:

```text
Party : Abdul Karim

Roles

✓ Customer

✓ Supplier

✓ Employee
```

Business Role ভবিষ্যতে আরও যোগ করা যাবে।

যেমন—

- Designer
- Courier
- Transport Vendor
- Contractor
- Consultant

Database Structure পরিবর্তন না করেই নতুন Role যুক্ত করা যাবে।

---

# 8. Contact Management

একটি Party-এর একাধিক Contact Person থাকতে পারবে।

উদাহরণ:

```text
ABC Traders

Rahim
Purchase Officer

Mobile:
017xxxxxxxx

------------------------------

Karim

Accounts Officer

Mobile:
018xxxxxxxx

------------------------------

Hasan

Managing Director

Mobile:
019xxxxxxxx
```

প্রত্যেক Contact Person-এর জন্য সংরক্ষণ করা যাবে—

- Name
- Designation
- Mobile
- Email
- Notes

---

# 9. Number Generation

প্রতিটি Profile-এর নিজস্ব Running Number থাকবে।

Customer

```text
CUS-000001
CUS-000002
CUS-000003
```

Supplier

```text
SUP-000001
SUP-000002
```

Employee

```text
EMP-000001
EMP-000002
```

সব Number Global Number Generator Service দ্বারা Generate হবে।

---

# 10. Design Decision

এই Architecture নির্বাচন করার কারণ—

- Duplicate Party কমানো।
- Database Normalization বজায় রাখা।
- ভবিষ্যতে Role যোগ করা সহজ করা।
- একই ব্যক্তি বা প্রতিষ্ঠানের সকল লেনদেন এক জায়গায় দেখা।
- ERP-এর অন্যান্য Module-এর সাথে সহজ Integration নিশ্চিত করা।

---

# 11. Business Rules

Party Module-এর জন্য নিম্নলিখিত Business Rules অনুসরণ করা হবে।

### Rule-1

একই ব্যক্তি বা প্রতিষ্ঠান একাধিকবার Party হিসেবে Create করা যাবে না।

---

### Rule-2

একটি Party-এর একাধিক Business Role থাকতে পারবে।

যেমন—

- Customer
- Print Partner
- Supplier
- Employee

---

### Rule-3

প্রতিটি Role-এর নিজস্ব Running Number থাকবে।

উদাহরণ:

Customer → CUS-000001

Supplier → SUP-000001

Employee → EMP-000001

---

### Rule-4

একটি Company-এর একাধিক Contact Person রাখা যাবে।

---

### Rule-5

Party Delete করা হবে না।

প্রয়োজনে শুধুমাত্র Inactive করা হবে।

---

### Rule-6

Customer, Supplier অথবা Employee Profile Delete করা হবে না।

প্রয়োজনে Inactive করা হবে।

---

### Rule-7

সমস্ত Number Global Number Generator Service দ্বারা তৈরি হবে।



### Rule-8

Duplicate Party তৈরির আগে System Warning প্রদর্শন করবে।

Default Duplicate Check

- Party Name
- Mobile Number

Optional Duplicate Check

- Email
- Trade License Number
- BIN Number
- TIN Number

Operator চাইলে Warning উপেক্ষা করে নতুন Party তৈরি করতে পারবে।

---

# 12. Future Expansion

Party Module ভবিষ্যতে নিম্নলিখিত Feature সমর্থন করবে।

- Multiple Branch
- Multiple Billing Address
- Multiple Shipping Address
- Credit Limit
- Credit Days
- Price Category
- Customer Group
- Supplier Group
- Tax Information
- BIN
- TIN
- Trade License
- National ID
- Passport
- Bank Accounts
- Mobile Banking Accounts
- Multiple Contact Persons
- File Attachments
- Notes
- Activity History
- Party Merge (Administrator Only)

---

# 13. Integration

Party Module ভবিষ্যতে নিম্নলিখিত Module-এর সাথে সংযুক্ত থাকবে।

- Customer Module
- Supplier Module
- Employee Module
- Sales Module
- Purchase Module
- Inventory Module
- Accounts Module
- Production Module
- CRM Module
- Reporting Module

---

# 14. Payment Design Policy

ERP-এ একটি Payment Voucher-এর মধ্যে একাধিক Payment Method ব্যবহার করা যাবে।

উদাহরণ:

Invoice Total = 20,000 টাকা

Payment

- Cash = 2,000
- Mobile Banking = 5,000
- Bank Transfer = 10,000
- Card = 3,000

অর্থাৎ একটি Payment Voucher-এর মধ্যেই একাধিক Payment Line রাখা যাবে।

Supported Payment Categories

- Cash
- Mobile Banking
- Bank Transfer
- Bank Cheque
- Card
- Digital Wallet
- Other

Mobile Banking Examples

- bKash
- Nagad
- Rocket
- Upay

Transaction ID, Reference Number এবং Transaction Reference **ঐচ্ছিক (Optional)** থাকবে।

---

# 15. Outstanding & Adjustment Policy

ERP Partial Payment সমর্থন করবে।

উদাহরণ

Invoice = 20,000

Advance = 2,000

Delivery Time = 10,000

Outstanding = 8,000

পরবর্তীতে যেকোনো সময় Outstanding Payment গ্রহণ করা যাবে।

Customer যদি Discount, Waiver অথবা Bad Debt-এর কারণে সম্পূর্ণ অর্থ পরিশোধ না করে, তাহলে বকেয়া Balance Adjustment Entry-এর মাধ্যমে নিষ্পত্তি করা যাবে।

---

# 16. Design Philosophy

MKPrintingMasterPro ERP বাস্তব Printing Press-এর Business Flow অনুসরণ করে তৈরি করা হবে।

Design-এর মূল নীতিমালা—

- Simple
- Practical
- Scalable
- Modular
- ERP Standard
- Future Ready

---

# 17. Conclusion

Party Module হলো MKPrintingMasterPro ERP-এর Foundation Module।

ERP-এর প্রায় সকল Module এই Party Module-এর উপর নির্ভর করবে।

এই Design ভবিষ্যতে নতুন Feature যোগ করার জন্য প্রস্তুত এবং Database Structure পরিবর্তন ছাড়াই সম্প্রসারণযোগ্য (Scalable)।

---

**Document Status:** Final Draft v1.1

**Prepared For:** MKPrintingMasterPro ERP

**Prepared By:** Project Architecture Team