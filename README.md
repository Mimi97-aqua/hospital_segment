# Hospital Segment

## Table of Content

- [Overview]()
- [Directory Structure]()
- [Implementation]()

## Overview
This project implements a small section of a medical app where patient data is made available to doctors such that
caregivers can be assigned to them if need be and prescriptions can equally be given to them.

## Directory Structure

## Implementation

### Steps
1. **Identifying objects and creating data models**

Based on the Figma design, the database required 3 main objects (tables), namely:
- Participant 
- Prescriptions
- Care Giver

Using ORM, I defined and created the schemas for the above objects.

### API Docs

Base URL: `localhost:5000/`
1. **Participant**

Base endpoint: `/participants`

Example request route:
`POST localhost:5000/participants/create`

_The participant here is also referred to as the **patient**._

- **Create a participant**
  - Creates a new participant and stores their details in the database
  - `POST /create`

- **Participants list**
  - Displays participant details containing only the participant's name, date of birth, phone number, and address.
  - `GET /list`

- **Participants details**
  - Returns all participants and all their details.
  - `GET /details`

- **Delete participant**
  - Deletes a specified participant (using their ID) from the database.
  - `DELETE /delete/id`

- **Update Participant**
  - Edits a specified participant's details (using their ID)
  - `PATCH /update/id`
